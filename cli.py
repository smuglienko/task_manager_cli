import sys


def main(args: list[str]) -> None:
    if len(args) >= 2:
        command = args[0]
        title = args[1]
        if command == "add":
            print(title)
        else:
            print("Неизвестная команда")
    else:
        print("Укажите команду и название задачи")


if __name__ == "__main__":
    main(sys.argv[1:])
