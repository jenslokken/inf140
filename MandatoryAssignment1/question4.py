secret = "I leave twenty million dollars to my friendly cousin Bill"
secret = secret.lower()
secret = "".join([i for i in secret if ord(i) >= 97 and ord(i) <= 122])
def tth(text):
    grid_list = []
    idx = 0
    value_list = []
    grid_list2 = []

    for j in range(len(secret) // 16 + 1):
        grid = []
        grid2 = []
        for i in range(4):
            temp = []
            for _ in range(4):
                try:
                    temp.append(ord(text[idx]) - 97)
                    idx += 1
                except:
                    temp.append(0)
            grid.append(temp)
            temp2 = [i for i in temp]
            id = i + 1
            for k in range(i):
                temp2.append(temp[k])
            temp2 = temp2[id:]
            grid2.append(temp2)
        grid_list.append(grid)
        grid_list2.append(grid2)

    for g in grid_list:
        temp = []
        for j in range(4):
            sum = 0
            for k in range(4):
                sum = (sum + g[k][j]) % 26
            temp.append(sum)
        value_list.append(temp)
    for v in grid_list:
        for k in v:
            print(k)
        print()
    print("----------------")
    for value in grid_list2:
        for g in value:
            print(g)
        print()
tth(secret)
        