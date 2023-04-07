A = int(input())
B = int(input())
C = int(input())
mul_num = A*B*C
mul_str = str(mul_num)
print(mul_str.count("0"))
for i in range(1, 10):
    print(mul_str.count(f'{i}'))
