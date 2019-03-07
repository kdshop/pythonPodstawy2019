firstArray = [[1, 2, 3], [1, 2, 0], [1, 0, 2]]
secondArray = [[5], [5], [5]]

firstArray[0][0] = secondArray[0][0]
firstArray[1][1] = secondArray[1][0]
firstArray[2][2] = secondArray[2][0]

sumaPrzekatnej = firstArray[0][2] + firstArray[1][1] + firstArray[2][0]

print("Suma przekatnej to:", sumaPrzekatnej)
