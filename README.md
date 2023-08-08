# Chess Analysis Graphing Tool
This tool plots chess evaluation (centipawns) and logPositions analyzed (logNodes) per unit depth using the chess engine Stockfish.

# Setup
1. Install Python at https://www.python.org/downloads/.
2. Download repository.
3. Open file *main.py*.
4. In line 13, enter directory of Stockfish.
5. Open Terminal in repository folder.
6. Enter ```pip install chess```.
7. Enter ```pip install numpy```.
8. Enter ```pip install matplotlib```.
9. Enter ```python main.py```.

# Usage
Run *main.py* via ```python main.py``` in Terminal.
```Before position:``` will print.
Enter the Forsyth–Edwards Notation (FEN) of the position before the move to analyze is played.
After, ```After position:``` will print.
Enter the FEN of the position after the move to analyze is played.
After, ```Move:``` will print.
Enter the move played.

After all information is entered, the code will open Stockfish and analyze the first position entered.
While analyzing, the code will record and print the evaluation, nodes, and logNodes for each depth reached.
After reaching a depth of 60, the code will close Stockfish; print lists of all important information; and plot evaluation, a weighted average of evaluation, and logNodes against depth.
The code will then repeat this process for the second position entered.
After, two graphs will appear, indicating that the code has finished running.
The user can save these graphs by clicking the "save the figure" icon, the rightmost option located at the bottom left of the figure.

In lines 15 and 16 of the code, ```Threads``` and ```Hash``` are both set to ```1```.
Threads are the number of CPU cores Stockfish uses to analyze.
Increasing threads increases the speed with which Stockfish analyzes.
However, to generate deterministic results, threads must be set to 1.
If the user is content with in-deterministic results, the user can increase threads assuming the user's CPU has an equivalent or greater number of cores.

Hash is the amount of random access memory (RAM) Stockfish uses to analyze.
Since we are analyzing static positions, increasing hash is unnecessary.
Furthermore, increasing hash drastically increases calculation time.
For these reasons, hash is set to its minimum value of 1.

# Example
Suppose the user wants to analyze the positions before and after the King's Pawn Opening, **1. e2e4**.
First, record the FENs of the two positions by navigating to *lichess.org/analysis*.
Underneath the board, a textbox titled FEN will display text for the current position on the board.
Since the before position is the starting position, record the FEN displayed, **rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1**.
After, play the move **1. e2e4** on the board and record the FEN of the after position, **rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq - 0 1**.

Now, run *main.py* via ```python main.py``` in Terminal.
When ```Before position:``` prints, enter the first position recorded, **rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1**.
After, when ```After position:``` prints, enter the second position recorded, **rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq - 0 1**.
Finally, when ```Move:``` prints, enter the move played, **1. e2e4**.

Stockfish will analyze the two positions, printing depth, evaluation, nodes, and logNodes information.
When Stockfish finishes, two graphs will appear.
These graphs are the results of the analysis, and are titled *Figure_0.png* and *Figure_1.png* in this repository.

# Errors
1. ```invalid literal for int() with base 10: 'PovScore(Mate('```.
Solution: Stockfish found a forced checkmate sequence, and the code cannot plot checkmate.
Use a different version of Stockfish or analyze a different position.
2. ```engine process died unexpectedly``` OR ```engine event loop dead```.
Solution: Illegal position entered.
Enter the FEN of a legal position.
3. ```empty fen```.
Solution: No FEN entered.
Enter a FEN.
4. ```expected 8 rows in position part of fen```.
Solution: Invalid FEN entered.
Enter a valid FEN.

# Contact
For help, improvements, etc., feel free to contact **silveryystar** on Discord.
