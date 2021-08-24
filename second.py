def cycle(s: str, val: int) -> str:
    '''
    Rotate the characters in a string by a given input and have
    the overflow appear at the beginning

        Parameters:
            s(str):       string to rotate
            val(int):     rotate input string by val places
        
        Return:
            result(str):  rotated string
    '''

    result = ''
    position = (-val) % len(s)
    for i in range(len(s)):
        result += s[position]
        position = (position + 1) % len(s)
    return result


def main():
    while True:
        s = input('Input string: ')
        val = int(input('Rotation(integer): '))
        print(cycle(s, val))
        print()


if __name__ == '__main__':
    main()