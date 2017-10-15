import sys
import console_display
import move_script


def main():
    width = int(sys.argv[1])
    height = int(sys.argv[2])
    script = move_script.MoveScript()
    display = console_display.ConsoleDisplay(script, width, height)
    display.run()


if __name__ == '__main__':
    main()
