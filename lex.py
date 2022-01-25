import math


def main():
    main_string = input("Enter the string : ")
    k = int(input("Enter the number : "))
    length = len(main_string)
    result = ""
    remainder = k-1
    for i in range(length-1, 0, -1):
        fact = math.factorial(i)
        result += str(remainder//fact)
        remainder = remainder % fact
    print(result)
    final = ""
    for _ in range(length-1):

        index = int(result[0])
        print(result + " | " + main_string + " | " + main_string[index])
        final += main_string[index]
        result = result[1:]
        main_string = main_string[:index] + main_string[index+1:]
    print(" | " + main_string[0] + ' | ' + main_string[0])
    print(final + main_string[0])


if __name__ == '__main__':
    main()
