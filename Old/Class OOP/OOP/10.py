def C_D(s):
    CHCD = {}
    for i in s:
        if i in CHCD:
            CHCD[i] += 1
        else:
            CHCD[i] = 1
    return CHCD

s = "assalom"
result_dict = C_D(s)
print("Natija:", result_dict)
