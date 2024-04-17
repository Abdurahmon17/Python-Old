def CSD(n):
    sd = {}
    for i in range(1, n + 1):
        sd[i] = i * i
    return sd

n = int(input("n sonini kiriting: "))
result_dict = CSD(n)
print(result_dict)
