if __name__ == '__main__':
    x = input("Text: ")

    new_string=''
    i = len(x)

    while i > 0:
        i = i - 1
        new_string = new_string + x[i]

    print(new_string)
