import curses
import time

def typing_test(stdscr):
    curses.curs_set(0)
    curses.start_color()

    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, 244, curses.COLOR_BLACK)
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)

    stdscr.nodelay(1)
    stdscr.timeout(100)

    target_text = "This is a typing test.\nasdfasdfasdf"
    current_text = []
    wpm = 0
    start_time = time.time()

    stdscr.addstr(0, 0, target_text)

    while True:
        time_elapsed = max(time.time() - start_time, 1)
        wpm = len(current_text) / (time_elapsed / 60) / 5

        stdscr.addstr(2, 0, f"WPM: {wpm:.2f}")

        char = stdscr.getch()
        if char == 27:
            break
        if char in (curses.KEY_BACKSPACE, 127):
            if current_text:
                current_text.pop()
        elif 0 < char < 256:
            current_text.append(chr(char))

        stdscr.clear()
        stdscr.addstr()
        stdscr.addstr(0, 0, target_text)
        stdscr.addstr(1, 0, "".join(current_text))
        stdscr.addstr(2, 0, f"WPM: {wpm:.2f}")

        if "".join(current_text) == target_text:
            stdscr.addstr(3, 0, "Test completed!")
            stdscr.refresh()
            stdscr.getch()
            break

        stdscr.refresh()

curses.wrapper(typing_test)
