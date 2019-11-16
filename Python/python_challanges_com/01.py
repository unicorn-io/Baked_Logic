# ceaser cipher with key as 2

key = int(input("Enter the Key: "))
string = str(input("Enter the String: "))

answer = ""

print("\n\n")

for x in string:
    k = ord(x) + key
    if (ord(x) >= 65 and ord(x) <= 90):   
        if (k > 90):
            k = ((k - 90) % 26) + 64
        answer = answer + str(chr(k))
    elif (ord(x) >= 97 and ord(x) <= 122):
        if (k > 122):
            k = ((k - 122) % 26) + 96
        answer = answer + str(chr(k))
    else:
        answer = answer + str(chr(k - key))
print(answer)

