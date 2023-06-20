def xor_binary_strings(str1, str2):
    # Ensure both strings have the same length
    if len(str1) != len(str2):
        raise ValueError("Input strings must have the same length")

    # Perform XOR operation bit by bit
    result = ""
    for bit1, bit2 in zip(str1, str2):
        if bit1 == bit2:
            result += "0"
        else:
            result += "1"

    return result

# Example usage
binary_string1 = "000000000000000000000000000000000000000000111110011111000011001100110101000000100001100100101010011100010011010100100100001001000111100000100101000110000000101100110011001000100011001000111010"
binary_string2 = "010001100100110001000001010001110111101101000110010011000100000101000111011110110100011001001100010000010100011101111011010001100100110001000001010001110111101101000110010011000100000101000111"

print(len(binary_string1))
print(len(binary_string2))

xor_result = xor_binary_strings(binary_string1, binary_string2)
print("XOR Result:", xor_result)
