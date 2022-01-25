import math


def main():
    main_string = input("Enter the string : ")
    k = int(input("Enter the number : "))
    length = len(main_string)
    temp = 2
    fact = math.factorial(length)
    remainder = k-1
    result = ""
    for _ in range(length-1):
        t = fact//math.factorial(temp)

        result += str(remainder//t)
        temp += 1
        remainder = remainder % t
    bigger = 0
    for _ in range(len(result)):
        bigger = bigger*10 + int(_+1)
    random_ = str(bigger - int(result))
    difference = len(result) - len(random_)
    for _ in range(difference):
        random_ = '0' + random_
    for index in range(length-1):
        first = int(random_[index])
        temp_ = index+1
        print(str(first) + " | " + str(temp_) + " | " + main_string)
        temp = main_string[first]
        main_string = main_string[:first] + \
            main_string[temp_] + main_string[first+1:]
        main_string = main_string[:temp_] + temp + main_string[temp_+1:]
    print(main_string)


if __name__ == '__main__':
    main()
