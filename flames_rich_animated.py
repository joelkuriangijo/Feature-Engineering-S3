# flames_rich_animated.py
# Requires: pip install rich
import time
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.live import Live

console = Console()

# -------------------- Cancellation (detailed logs) --------------------
def detailed_cancellation(name1: str, name2: str, delay=0.8):
    """
    Remove common letters pairwise and print detailed logs step-by-step.
    Returns the remaining-letter count (int).
    """
    a = [ch for ch in name1.lower() if ch.isalpha()]
    b = [ch for ch in name2.lower() if ch.isalpha()]

    console.print(f"\n[bold yellow]Cancellation details for:[/bold yellow]")
    console.print(f"[cyan]Name1:[/cyan] [bold]{''.join(a) or '(none)'}[/bold]")
    console.print(f"[magenta]Name2:[/magenta] [bold]{''.join(b) or '(none)'}[/bold]\n")
    time.sleep(0.35)

    # iterate over a copy of original name1 characters so repeated letters are handled left-to-right
    orig = [ch for ch in name1.lower() if ch.isalpha()]
    for ch in orig:
        if ch in b:
            a.remove(ch)
            b.remove(ch)
            console.print(f"[red]❌ Cancelled '{ch.upper()}' from both names[/red]")
            console.print(f"   → Remaining: [cyan]{''.join(a) or '(none)'}[/cyan]  |  [magenta]{''.join(b) or '(none)'}[/magenta]")
            time.sleep(delay)
        else:
            console.print(f"[dim]✔ '{ch.upper()}' not found in second name — kept[/dim]")
            time.sleep(delay * 0.6)

    count = len(a) + len(b)
    console.print(f"\n[bold magenta]Remaining letters count = {count}[/bold magenta]\n")
    time.sleep(0.6)
    return count

# -------------------- FLAMES rendering --------------------
BASE_LETTERS = list("FLAMES")

def render_flames(removed:set, highlight_idx:int|None) -> Text:
    """
    Return a rich.Text object for the current FLAMES line.
    removed: set of base indices (0..5) that are removed/dimmed.
    highlight_idx: index (0..5) currently highlighted (not the position in alive-list).
    """
    time.sleep(0.4)
    t = Text()
    for i, ch in enumerate(BASE_LETTERS):
        if i in removed:
            # dim + strike (if terminal supports) to show eliminated
            t.append(f" {ch} ", style="dim")
        elif i == highlight_idx:
            # reverse + bold highlight
            t.append(f" {ch} ", style="reverse bold yellow")
        else:
            t.append(f" {ch} ", style="bold cyan")
        t.append("  ")
    return t

# -------------------- Animated elimination (single-line, correct logic) --------------------
def animated_elimination(count:int, fps=10, step_delay=0.20, remove_pause=0.5):
    """
    Runs animated elimination using rich.Live and returns final letter (char).
    - count: remaining letters count from cancellation
    """
    removed = set()     # indices in BASE_LETTERS that have been removed
    pos = 0             # position in the current 'alive' list (index within alive list, not base index)

    with Live(render_flames(removed, None), refresh_per_second=fps, console=console) as live:
        time.sleep(0.25)
        while len(removed) < len(BASE_LETTERS) - 1:
            # build current alive list (indices into base letters)
            alive = [i for i in range(len(BASE_LETTERS)) if i not in removed]
            n_alive = len(alive)
            # compute elimination position within alive (where counting stops)
            elim_pos = (pos + count - 1) % n_alive

            # animate stepping from 'pos' to 'elim_pos' over the alive indices
            steps = (elim_pos - pos) % n_alive + 1  # number of highlights to perform inclusive
            for s in range(steps):
                cur_alive_index = alive[(pos + s) % n_alive]
                live.update(render_flames(removed, cur_alive_index))
                time.sleep(step_delay)

            # the index to remove in base-index space:
            elim_idx = alive[elim_pos]

            # mark removed and show brief removed animation
            removed.add(elim_idx)
            live.update(render_flames(removed, None))
            time.sleep(remove_pause)

            # next start position: elimination continues from the position after the removed one
            # convert elim_pos (position in old alive list) into new pos in the new alive list
            new_alive = [i for i in range(len(BASE_LETTERS)) if i not in removed]
            if new_alive:
                # find index of the element that was after eliminated one in old alive list
                # That is simply elim_pos (since after removal indices shift left); new pos = elim_pos % len(new_alive)
                pos = elim_pos % len(new_alive)
            else:
                pos = 0

        # only one remains
        remaining_idx = [i for i in range(len(BASE_LETTERS)) if i not in removed][0]

        # small final blink on the same single line
        for _ in range(3):
            live.update(render_flames(removed, remaining_idx))
            time.sleep(0.30)
            live.update(render_flames(removed, None))
            time.sleep(0.12)
        live.update(render_flames(removed, remaining_idx))
        time.sleep(0.25)

    # return char of remaining letter
    return BASE_LETTERS[remaining_idx]

# -------------------- mapping to final panel --------------------
def flames_panel(letter: str) -> Panel:
    mapping = {
        "F": ("💞 FRIENDS 💞", "cyan"),
        "L": ("❤ LOVE ❤", "red"),
        "A": ("💖 AFFECTION 💖", "magenta"),
        "M": ("💍 MARRIAGE 💍", "yellow"),
        "E": ("☠ ENEMIES ☠", "bright_red"),
        "S": ("👨‍👩‍👧‍👦 SIBLINGS 👨‍👩‍👧‍👦", "green"),
    }
    text, color = mapping[letter]
    return Panel.fit(text, style=f"bold {color}", border_style=color)

# -------------------- Main --------------------
def flames_game():
    console.clear()
    console.print(Panel("[bold magenta]💘 FLAMES - Animated[/bold magenta]\n", style="green"))

    name1 = console.input("[cyan]👉 Enter your name: [/cyan] ").strip()
    name2 = console.input("[cyan]👉 Enter crush's name: [/cyan] ").strip()

    if not name1 or not name2:
        console.print("[red]Both names required. Exiting.[/red]")
        return

    # Cancellation with detailed logs (colored)
    count = detailed_cancellation(name1, name2, delay=0.8)

    # special case: no remaining letters
    if count == 0:
        console.print("[yellow]No letters remain after cancellation — special case chosen: AFFECTION[/yellow]")
        final_letter = "A"
    else:
        console.print("\n[bold magenta]Step: FLAMES elimination (watch the single-line animation)[/bold magenta]\n")
        time.sleep(0.6)
        final_letter = animated_elimination(count)

    console.print("\n[bold green]Final Result[/bold green]\n")
    console.print(flames_panel(final_letter))
    console.print("\n[dim]Thanks for trying the animated FLAMES. Want the final art to pulse more or change colors/speeds? Tell me.[/dim]\n")

if __name__ == "_main_":
    flames_game()