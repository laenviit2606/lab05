def biggest(numbers):
    highest = numbers[0]
    for number in numbers:
        if number > highest:
            highest = number
    return highest
print(biggest([3, 4, 6, 10, 30, 21]))
print(biggest([-5,-2,-10]))
def average(numbers):
    if len(numbers) ==0:
        return 0
    return sum(numbers)/len(numbers)
print(average([]))

