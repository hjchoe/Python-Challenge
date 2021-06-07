import string

def charTOpos(letter):
    return ord(letter) - 96

def posTOchar(pos):
    return chr(pos + 96)

s = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
url = "map"
code = ["nothing", 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k','l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

message = ''
for char in s:
    if char in code:
        #pos = charTOpos(char)
        #npos = pos + 2
        #if npos > 26:
        #    npos = 0 + (npos - 26)
        #message += posTOchar(npos)
        pos = code.index(char)+2
        if pos > 26:
            pos = pos-26
        message += code[pos]
    else:
        message += char

print(message)
print("\n")


message = ''
for char in url:
    if char in code:
        #pos = charTOpos(char)
        #npos = pos + 2
        #if npos > 26:
        #    npos = 0 + (npos - 26)
        #message += posTOchar(npos)
        pos = code.index(char)+2
        if pos > 26:
            pos = pos-26
        message += code[pos]
    else:
        message += char

print(message)