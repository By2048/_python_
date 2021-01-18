from xml.etree.ElementTree import parse


def main():
    with open("T:\\keymap.xml", 'r', encoding='utf-8') as file:
        data = parse(file).getroot()

    for action in data.findall('action'):
        if not action.findall('keyboard-shortcut'):
            continue
        print(action.attrib['id'].lstrip('$'))
        for keystroke in action.findall('keyboard-shortcut'):
            first = keystroke.attrib['first-keystroke']
            second = keystroke.attrib.get('second-keystroke')
            print(f'{first}{" " + second if second else ""}')
        print()


if __name__ == '__main__':
    main()
