import string

input_file = open("input.txt")
text = "".join([line.strip() for line in input_file])
answer = ""

for letter in text:
    if 97 <= ord(letter)  <= 122:
        answer = answer + letter


print('Answer: ' + answer)