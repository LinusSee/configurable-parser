from src.orchestration import parseText


def main():
    result = parseText('Loglevel: asdf')
    print(result)

if __name__ == "__main__":
    main()