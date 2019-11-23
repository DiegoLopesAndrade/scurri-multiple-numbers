def multipleNumbers(i):
    """
    Function with logic to know if numbers are multiples of 3, 5 or 3 and 5
    """
    entry = ''
    if i%3 == 0:
        entry += 'Three'
    if i%5 == 0:
        entry += 'Five'
    if not entry:
        entry += str(i)

    return entry


def listMultiplesNumbers(start, end):
    """
    Function to create a list of numbers and "added" into that
    """
    numbers = list()

    for i in range(start, end+1):
        numbers.append(multipleNumbers(i))

    return numbers


def showNumbers(numbers):
    """
    Function to display our numbers(when the number is multiple, not display the number)
    """
    for number in numbers:
        print(number)


if __name__ == "__main__":
    start = 1
    end = 100
    showNumbers(listMultiplesNumbers(start, end))
