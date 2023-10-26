for i in range(100, 1000):
    sum_num = sum(int(j)**3 for j in str(i))
    if sum_num == i:
        print(i)
