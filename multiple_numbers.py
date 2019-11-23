def multipleNumbers(i):
    entry = ''
    if i%3 == 0:
        entry += 'Three'
    if i%5 == 0:
        entry += 'Five'
    if not entry:
        entry += str(i)

    return entry


def listMultiplesNumbers(start, end):
    numbers = list()

    for i in range(start, end+1):
        numbers.append(multipleNumbers(i))

    return numbers


def showNumbers(numbers):
    for number in numbers:
        print(number)


if __name__ == "__main__":
    start = 1
    end = 100
    showNumbers(listMultiplesNumbers(start, end))