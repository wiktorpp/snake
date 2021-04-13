import curses
from random import randint

def main(stdscr):
    curses.beep()
    #stdscr.addch("test")
    boardSize = stdscr.getmaxyx()
    snake = [(int(boardSize[0]/2), int(boardSize[1]/2))]
    score = 0
    #while True:
    while True: 
        key = stdscr.getch()
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
        board = [[False] * boardSize[1]] * boardSize[0]
        stdscr.clear()
        for position in snake:
            stdscr.addstr(position[0], position[1], "#")
        stdscr.addstr(0, 0, str(snake))
        stdscr.addstr(1, 0, str(key))
                


    stdscr.addstr(0, 0, "te")

    print(stdscr.getmaxyx())

curses.wrapper(main)