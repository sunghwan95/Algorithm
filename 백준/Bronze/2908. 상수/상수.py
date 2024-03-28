A, B = input().split()

arrA = list(A)
arrB = list(B)

arrA.reverse()
arrB.reverse()

strA = "".join(arrA)
strB = "".join(arrB)

if int(strA) > int(strB):
    print(strA)
else:
    print(strB)
