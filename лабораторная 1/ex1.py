numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
summa_chisel=sum(numbers[0:4])+sum(numbers[5:20])
srednee=summa_chisel/len(numbers)
numbers[4]=srednee
print("Измененный список:", numbers)


