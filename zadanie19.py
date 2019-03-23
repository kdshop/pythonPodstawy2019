def creatematrix(column, row):
    temparr = []
    for i in range(row):
        temprow = []
        for j in range(column):
            if j == 0:
                temprow.append(i)
            elif j == 1:
                temprow.append(i**2)
            else:
                temprow.append(0)
        temparr.append(temprow)
    return temparr


creatematrix(10, 10)
