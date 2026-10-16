def calculate_average(numbers):
    total = 0
    for n in numbers:
        total += n  # <-- Click in the gutter next to this line
    average = total / len(numbers)
    return average

scores = [10, 20, 30]
result = calculate_average(scores)
print(result)