numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

position_ = numbers.index(None)
summ_ = sum(numbers[0: position_])+sum(numbers[position_+1: len(numbers)+1])
lenn_ = len(numbers)
numbers[position_] = summ_/lenn_
print("Измененный список:", numbers)
