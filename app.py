import os


def get_message(name: str = "World") -> str:
    return f"Hello, {name}!"


def main() -> None:
    name = os.getenv("APP_NAME", "Infinite")
    print(get_message(name))


if __name__ == "__main__":
    main()
