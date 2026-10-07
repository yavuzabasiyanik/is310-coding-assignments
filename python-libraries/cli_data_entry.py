import csv
import re
from datetime import date
from pathlib import Path

from rich.console import Console
from rich.table import Table

FIELDS = [
    "date",
    "color",
    "time_control",
    "result",
    "end_reason",
    "opening",
    "critical_moment",
    "why",
    "time_pressure",
    "emotional_state",
    "understood_position",
]

CHOICES = {
    "color": ["white", "black"],
    "result": ["win", "loss", "draw"],
    "end_reason": ["checkmate", "resigned", "timeout", "draw agreed", "stalemate", "repetition", "abandoned", "other"],
    "time_pressure": ["yes", "no", "unknown"],
    "understood_position": ["yes", "partly", "no", "unknown"],
}


def validate(field, answer):
    """Return an error message, or None if the answer is acceptable."""
    if not answer:
        return "Required. Type 'unknown' if you genuinely don't know."
    if field in CHOICES and answer.lower() not in CHOICES[field]:
        return f"Must be one of: {', '.join(CHOICES[field])}"
    if field == "date":
        try:
            if date.fromisoformat(answer) > date.today():
                return "Date can't be in the future."
        except ValueError:
            return "Use YYYY-MM-DD."
    if field == "time_control" and not re.fullmatch(r"\d+\+\d+", answer):
        return "Use minutes+increment, e.g. 10+0 or 5+3."
    return None

games = [
    {
        "date": "2026-10-05",
        "color": "white",
        "time_control": "10+0",
        "result": "loss",
        "end_reason": "resigned",
        "opening": "Caro-Kann",
        "critical_moment": "move 23, took the pawn",
        "why": "thought it was free, missed Bg5",
        "time_pressure": "yes",
        "emotional_state": "tilted",
        "understood_position": "partly",
    },
    {
        "date": "2026-10-06",
        "color": "black",
        "time_control": "5+3",
        "result": "win",
        "end_reason": "timeout",
        "opening": "Sicilian",
        "critical_moment": "move 31, traded queens",
        "why": "simplified when ahead on the clock",
        "time_pressure": "no",
        "emotional_state": "calm",
        "understood_position": "yes",
    },
]

console = Console()

table = Table(title="Chess Games")
for field in FIELDS:
    table.add_column(field)

for game in games:
    table.add_row(*[game[field] for field in FIELDS])

console.print(table)

OUTPUT_FILE = Path(__file__).parent / "chess_games.csv"


def enter_game():
    """Ask for every field, show the record, repeat until the user confirms it."""
    while True:
        new_game = {}
        for field in FIELDS:
            while True:
                answer = input(f"{field}: ").strip()
                error = validate(field, answer)
                if error is None:
                    break
                console.print(f"[red]{error}[/red]")
            new_game[field] = answer.lower() if field in CHOICES else answer

        while True:
            confirm = input("Is this correct? (y/n): ").strip().lower()
            if confirm in ("y", "n"):
                break

        if confirm == "y":
            return new_game
        console.print("[yellow]Okay, re-enter the game.[/yellow]")


def save_game(game):
    """Append one confirmed game to the CSV, writing the header if the file is new."""
    is_new_file = not OUTPUT_FILE.exists()
    with OUTPUT_FILE.open("a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        if is_new_file:
            writer.writeheader()
        writer.writerow(game)


console.print("\n[bold cyan]Enter new games below, one field at a time.[/bold cyan]")

while True:
    game = enter_game()
    save_game(game)
    console.print(f"[green]Saved to:[/green] {OUTPUT_FILE.resolve()}")

    again = input("Add another game? (y/n): ").strip().lower()
    if again != "y":
        break

console.print("[bold]Done.[/bold]")
