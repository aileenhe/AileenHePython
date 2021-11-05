str1 = input ("What is your string? ")
ascii_values = []
equal_sign = ('=')
for character in str1:
    ascii_values.append(ord(character))
for i in range(len(str1)): 
    print(str1[i],equal_sign,ascii_values[i], sep="")