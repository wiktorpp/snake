import curses
from random import randint

graphicsDict = {
    frozenset({ord("s"), ord("d")}): "╔",
    frozenset({ord("s"), ord("a")}): "╗",
    frozenset({ord("w"), ord("a")}): "╝",
    frozenset({ord("w"), ord("d")}): "╚",
    frozenset({ord("a"), ord("d")}): "═",
    frozenset({ord("w"), ord("s")}): "║",
}

def main(stdscr):
    curses.beep()
    #stdscr.addch("test")
    boardSize = stdscr.getmaxyx()
    snake = [(int(boardSize[0]/2), int(boardSize[1]/2))]
    moves = [ord("w")]
    score = 0
    pellet = None
    stdscr.timeout(5000)
    while True: 
        head = snake[0]
        snake2 = [head]
        for move in moves:
            if move == ord("w"):
                snake2.append((snake2[-1][0] - 1, snake2[-1][1]))
            if move == ord("s"):
                snake2.append((snake2[-1][0] + 1, snake2[-1][1]))
            if move == ord("d"):
                snake2.append((snake2[-1][0], snake2[-1][1] + 1))
            if move == ord("a"):
                snake2.append((snake2[-1][0], snake2[-1][1] - 1))

        curses.beep()
        key = stdscr.getch()
        if key == -1:
            key = moves[-1]
        moves.append(key)
        if key == ord("w"):
            snake.append((snake[-1][0] - 1, snake[-1][1]))
        if key == ord("s"):
            snake.append((snake[-1][0] + 1, snake[-1][1]))
        if key == ord("d"):
            snake.append((snake[-1][0], snake[-1][1] + 1))
        if key == ord("a"):
            snake.append((snake[-1][0], snake[-1][1] - 1))
        if key == ord("q"):
            exit()
        if len(snake) > 10:
            snake.pop(0)
        #board = [[False] * boardSize[1]] * boardSize[0]
        if pellet == snake[-1] or pellet == None:
            pellet = (randint(0, boardSize[0]), randint(0, boardSize[1]))
        stdscr.clear()
        for position in snake:
            stdscr.addstr(*position, "#")
        stdscr.addstr(*pellet, "#")
        stdscr.addstr(0, 0, str(snake))
        stdscr.addstr(1, 0, str(key))
        stdscr.addstr(2, 0, str(moves))
        stdscr.addstr(3, 0, str(snake2))
        stdscr.addstr(4, 0, str(list(reversed(snake2))))
        


    stdscr.addstr(0, 0, "te")

    print(stdscr.getmaxyx())

curses.wrapper(main)