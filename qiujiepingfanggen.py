S=float(input("请输入你要求解平方根的正数："))
infinitesimal = 0.00000000000000000000001

a = S / 2

counter = 1
while True:
    b = S / a
    delta = a - b
    c = round(b,2)
    d = round(b,2)
    print(f'这是第{counter}轮，S={S}, a={c}, b={d}, delta={delta}, 是否结束：{delta < infinitesimal}')
    
    counter = counter + 1

    if delta < infinitesimal:
        break
    else:
        a = a = (a + b) / 2