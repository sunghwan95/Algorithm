import sys

input = sys.stdin.readline

ipv6 = input().rstrip()
ipv6 = ipv6.split(":")

if ipv6[0] == "":
    ipv6 = ipv6[1:]

if ipv6[-1] == "":
    ipv6 = ipv6[:-1]

result = ""
for i in ipv6:
    if i == "":
        result += "0000:" * (8 - len(ipv6) + 1)
    else:
        result += i.zfill(4) + ":"

print(result[:-1])
