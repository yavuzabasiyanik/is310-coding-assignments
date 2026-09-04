# Command Line Maze: The Meridian Trust Disclosure Maze

**By Yavuz Abasiyanik**

## About this maze

This maze is themed around real dark patterns from banking and
fintech UX — the deliberately confusing fee schedules, "courtesy"
overdraft enrollments, retention offers thrown at you when you try to
close an account, and compliance fine print that technically
discloses everything while practically explaining nothing. Having
worked on banking compliance and governance software at JPMorgan
Chase and Wells Fargo, I wanted to turn the *experience* of navigating
a bank's disclosures — technically transparent, practically opaque —
into a literal maze you navigate with the command line. Every clue is
written in-character as a fictional bank ("Meridian Trust & Savings")
burying the next step in legalese and marketing copy, the same way
real disclosures bury the information that actually matters.

## How to solve it

1. Unzip the maze:
   ```
   unzip banking-dark-patterns-maze.zip
   ```
2. Enter the maze at its starting point:
   ```
   cd maze/START_HERE
   ```
3. Use these three commands to work your way through:
   - `ls` and `ls -a` — list the files and folders in your current
     location (`-a` also shows hidden/dotfiles — you'll need this
     at least once)
   - `cat <filename>` — read the contents of a clue file
   - `cd <foldername>` — move into the folder a clue points you to
4. Read each file carefully — the "next stop" is always named
   somewhere in the text, though not always in the first sentence.
5. One clue is hidden in a dotfile. If you get stuck and `ls` doesn't
   show an obvious next step, try `ls -a` in your current folder.
6. You've solved the maze when you `cat` a file named `SOLUTION.txt`
   and receive your payoff message.

Good luck — and read the fine print.
