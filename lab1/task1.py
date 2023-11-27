numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
position = numbers.index(None)
summ = sum(numbers[: position]) + sum(numbers[position + 1:])
lenn = len(numbers)
numbers[position] = summ / lenn
print("Измененный список:", numbers)

