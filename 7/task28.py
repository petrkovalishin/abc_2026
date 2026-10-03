#todo: Числа в буквы
Замените числа, написанные через пробел, на буквы. Не числа не изменять.

Пример.
Input	                            Output
8 5 12 12 15	                    hello
8 5 12 12 15 , 0 23 15 18 12 4 !	hello, world!



def numbers_to_letters(text):
    result = []
    for token in text.split(' '):
        if token.isdigit():
            num = int(token)
            if 1 <= num <= 26:
                result.append(chr(ord('a') + num - 1))
            else:
                result.append(token)
        else:
            result.append(token)
    return ' '.join(result)

if __name__ == '__main__':
    test1 = "8 5 12 12 15"
    test2 = "8 5 12 12 15 , 0 23 15 18 12 4 !"

    print(numbers_to_letters(test1))
    print(numbers_to_letters(test2))