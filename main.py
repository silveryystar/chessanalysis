import chess.engine
import numpy as np
import matplotlib.pyplot as plt
import math


def analysis(board, color, label, move):
    depth_list = []
    eval_list = []
    node_list = []
    lognode_list = []

    engine = chess.engine.SimpleEngine.popen_uci(r"")

    engine.configure({"Threads": 1,
                      "Hash": 1})

    with engine.analysis(board) as result:
        for i in result:
            if "score" in i and "lowerbound" not in i and "upperbound" not in i:
                depth = int(i["depth"])
                depth_list.append(depth)

                eval = str(i["score"]).removeprefix("PovScore(Cp(")
                if "WHITE" in eval:
                    eval_reduced = int(eval.removesuffix("), WHITE)"))

                else:
                    eval_reduced = -int(eval.removesuffix("), BLACK)"))
                eval_list.append(eval_reduced)

                nodes = int(i["nodes"])
                node_list.append(nodes)
                lognodes = math.log10(nodes)
                lognode_list.append(lognodes)

                print(f"Depth: {depth} Eval: {eval_reduced} Nodes: {nodes} logNodes: {lognodes}")

                if depth == 60:
                    break

    weighted_avg = np.average(eval_list,
                              weights=depth_list)

    print(f"Depths: {depth_list}")
    print(f"Evals: {eval_list}")
    print(f"Nodes: {node_list}")
    print(f"logNodes: {lognode_list}")
    print(f"Weighted avg: {weighted_avg}")

    plt.figure(0)
    plt.plot(depth_list,
             eval_list,
             color=color,
             label=label,
             linestyle="-")

    plt.axhline(y=weighted_avg,
                color=color,
                linestyle="--")

    plt.xlabel("Depth")
    plt.ylabel("Evaluation (centipawns)")
    plt.title(f"Evaluation before and after {move}.")
    plt.legend()
    plt.xlim(1, 60)

    plt.figure(1)
    plt.plot(depth_list,
             lognode_list,
             color=color,
             label=label,
             linestyle="-")

    plt.xlabel("Depth")
    plt.ylabel("logPositions (logNodes)")
    plt.title(f"logPositions analyzed before and after {move}.")
    plt.legend()
    plt.xlim(1, 60)
    plt.ylim(0)


before_pos = input("Before position: ")
after_pos = input("After position: ")
move = input("Move: ")

board1 = chess.Board(before_pos)
analysis(board1, "b", "Before", move)

board2 = chess.Board(after_pos)
analysis(board2, "r", "After", move)

plt.show()
