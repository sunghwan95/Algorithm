base64_table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

char_to_val = {ch: idx for idx, ch in enumerate(base64_table)}

T = int(input())
for tc in range(1, T + 1):
    encoded = input().strip()

    binary_str = ""
    for ch in encoded:
        val = char_to_val[ch]
        bin6 = format(val, "06b")
        binary_str += bin6

    decoded_chars = []
    for i in range(0, len(binary_str), 8):
        byte = binary_str[i : i + 8]
        if len(byte) < 8:
            break
        decoded_chars.append(chr(int(byte, 2)))

    result = "".join(decoded_chars)
    print(f"#{tc} {result}")
