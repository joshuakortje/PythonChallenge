import string

text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
answer = ""
url = "map"

for c in url:
    if 97 <= ord(c) <= 122:
        new_c = chr(ord(c) + 2)
        answer = answer + new_c
    else:
        answer = answer + c

print(answer)
