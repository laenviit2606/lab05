def average(numbers):
    if not numbers:           # If the list is empty
        return 0              # Return 0 instead of crashing
    total = sum(numbers)      # Add all the numbers together
    count = len(numbers)      # Count how many numbers there are
    return total / count      # Divide the total by the count
print(average([4.50, 12.00, 3.25, 8.75])) 
print(average([]))          #average[]: calls the function average with an empty list, which should return 0
