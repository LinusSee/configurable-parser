from src.orchestration import parseText

multilineStringWindows = 'Loglevel: \r\nLoglevel: \r\nLoglevel: '

def main():
    result = parseText('Loglevel: ')
    print(result)

    result2 = parseText(multilineStringWindows)
    print(result2)

if __name__ == '__main__':
    main()