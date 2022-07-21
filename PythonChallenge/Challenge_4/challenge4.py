import string

input_file = open("input.txt")
text = "".join([line.strip() for line in input_file])
answer = ""

for i in range(4,len(text)-4):
    letter = text[i]
    # definitely not the most elegent way to do it, but the input text is short enough
    if text[i-4].islower() and text[i-3].isupper() and text[i-2].isupper() and text[i-1].isupper() and \
            text[i].islower() and text[i+1].isupper() and text[i+2].isupper() and text[i+3].isupper() and text[i+4].islower():
        answer = answer + letter


print('Answer: ' + answer)