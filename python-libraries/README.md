# Command Line Data Curation: Chess Game Annotation

A tool for annotating my own chess games with the things no chess database records: why I made a key decision, whether I was under time pressure, my emotional state, and whether I actually understood the position. It feeds the "create" half of my semester project, which compares hand-built subjective game data against the Lichess open database.

I built the same workflow twice (Pathway 2): a Python CLI and an HTML form.

## What it collects

| Field | Type | Allowed values |
|---|---|---|
| `date` | constrained | `YYYY-MM-DD`, not in the future |
| `color` | constrained | white, black |
| `time_control` | constrained | minutes+increment, e.g. `10+0` |
| `result` | constrained | win, loss, draw |
| `end_reason` | constrained | checkmate, resigned, timeout, draw agreed, stalemate, repetition, abandoned, other |
| `opening` | free text | |
| `critical_moment` | free text | |
| `why` | free text | |
| `time_pressure` | constrained | yes, no, unknown |
| `emotional_state` | free text | |
| `understood_position` | constrained | yes, partly, no, unknown |

Every field is required. If I genuinely don't know an answer, I type `unknown` rather than leaving the field blank.

## Files

- `cli_data_entry.py`: Python CLI
- `chess_data_entry.html`: HTML version (no server needed)
- `chess_games.csv`: sample data produced by the CLI
- `chess_games_html.csv`: sample data produced by the HTML form
- `rich_example.py`: Rich library walkthrough from the lesson
- `requirements.txt`: Python dependencies
- `ai-chat-log.md`: AI prompts and responses

## How to run

### Python CLI

From the repository root:

```bash
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
python -m pip install -r requirements.txt
python python-libraries/cli_data_entry.py
```

The script shows two example games in a table, then asks for each field in turn. After every entry it asks you to confirm; `n` restarts that entry. Each confirmed game is appended to `chess_games.csv`, and the full path is printed.

### HTML

Open `chess_data_entry.html` in any browser. Fill in the form, click **Review entry**, confirm, and repeat. **Download CSV** saves every confirmed game.

## Comparing the two interfaces
1. What does each interface make easier or harder?
  - CLI: Fast once you know what to enter, since you dont have to click around, but you cant see them at once or go back to edit a field. Typo means you have to redo all fields which is not ideal. 

  - HTML: Much cleaner. You can see and edit any field whenever you want, though it can be a little slower than the CLI.
  
2. Did the interfaces lead to different choices about fields, instructions, or validation?
  Yes, select fields do not let you choose something that doesnt make sense in HTML, for example in CLI you might not know what to enter for a field like "end_reason" as there are many ways you can win or lose a chess game, with HTML it is a select field so you dont have to worry.

  Also the date field can be tricky in CLI while it is pretty straight forward in HTML

3. What did AI contribute, and what did you change, reject, or troubleshoot?

    AI helped me write the code, told me what to focus on, and write the HTML.

4. Which interface fits the material and the intended user better, and why?

    For entering data, the HTML fits better. I can see every field at once, fix one without redoing the rest, and the dropdowns stop me from typing values that don't make sense. But my sample data shows neither interface solved the actual problem. The constrained fields came out clean in both, while the fields that matter most for my project came out as "no", "abd", "unknown", and "I checkmated him." Validation can force the right format, but it can't force me to actually explain why I made a move. The HTML has a better chance because the big text box for `why` invites a real answer more than a one-line terminal prompt does, but the real fix is annotating games right after I play them, not at 1:30am.