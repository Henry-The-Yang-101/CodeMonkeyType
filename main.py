import curses
import time

def typing_test(stdscr):
    curses.curs_set(0)
    curses.start_color()

    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_RED)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(4, 244, curses.COLOR_BLACK)

    stdscr.nodelay(1)
    stdscr.timeout(100)

    with open('LeetcodeSolutions/3sum.cpp', 'r') as file:
        target_text = file.read()
    typed_text_correctness = []

    tpm = 0
    accuracy = 0
    start_time = time.time()

    final_tpm = 0
    final_accuracy = 0

    while True:
        typed_text_current_index = len(typed_text_correctness)

        if typed_text_current_index == 0:
            start_time = time.time()

        typed_char = stdscr.getch()

        if typed_char == 27:
            break
        if typed_char in (curses.KEY_BACKSPACE, 127):
            if typed_text_correctness:
                typed_text_correctness.pop()
                typed_text_current_index -= 1
        elif 0 < typed_char < 256:
            if target_text[typed_text_current_index] == '\n':
                if typed_char == 10 or typed_char == 13 or typed_char == 32:
                    typed_text_correctness.append(True)
                    typed_text_current_index += 1
                    while target_text[typed_text_current_index] == '\n' or target_text[typed_text_current_index] == ' ':
                        typed_text_correctness.append(True)
                        typed_text_current_index += 1
            else:
                typed_text_correctness.append(target_text[typed_text_current_index] == chr(typed_char))
                typed_text_current_index += 1

        stdscr.clear()

        time_elapsed = max(time.time() - start_time, 1)
        tpm = typed_text_current_index / (time_elapsed / 60) / 5
        accuracy = 0 if typed_text_current_index == 0 else sum(typed_text_correctness) * 100 / typed_text_current_index
        stdscr.addstr(0, 0, f"3sum.cpp Solution || Tokens Per Minute (TPM): {tpm:.2f} || Accuracy: {accuracy:.1f}%")

        current_display_char_index = 0
        current_line = 1
    
        for line in target_text.splitlines():
            for i in range(len(line)):
                if current_display_char_index > typed_text_current_index:
                    stdscr.addch(current_line, i, line[i], curses.color_pair(4))
                elif current_display_char_index == typed_text_current_index:
                    stdscr.addch(current_line, i, line[i], curses.color_pair(3))
                elif typed_text_correctness[current_display_char_index]:
                    stdscr.addch(current_line, i, line[i], curses.color_pair(1))
                else:
                    stdscr.addch(current_line, i, line[i], curses.color_pair(2))
                current_display_char_index += 1
            current_display_char_index += 1
            current_line += 1

        if typed_text_current_index == len(target_text):
            final_tpm = tpm
            final_accuracy = accuracy
            break

        stdscr.refresh()

    stdscr.addstr(0, 0, f"Test completed!!! Your final coding speed was {final_tpm} TPM (tokens per minute) with an accuracy of {final_accuracy}% for the 3sum.cpp solution.")

curses.wrapper(typing_test)
