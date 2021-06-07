def checkifanswer(everything, i):
    try:
        code = everything[i] + everything[i+1] + everything[i+2] + everything[i+3] + everything[i+4] + everything[i+5] + everything[i+6]
    except:
        return False, None
    if everything[i].isupper() and everything[i+1].isupper() and everything[i+2].isupper() and everything[i+3].islower() and everything[i+4].isupper() and everything[i+5].isupper() and everything[i+6].isupper():
        if everything[i-1].isupper() or everything[i+7].isupper():
            return False, code
        else:
            return True, code
    else:
        return False, code


#f = open("/Users/hjcho/Dropbox/programming/T2 python/Python Challenge/num3.txt", 'r')
f = open("/Users/School_Account/Dropbox/programming/T2 python/Python Challenge/num3.txt", 'r')
whole = f.readlines()

everything = ''
for line in whole:
    for char in line:
        if char != '\n':
            everything += char

answers = []
i = 0
while i <= 100000:
    state, code = checkifanswer(everything, i)
    print(f"({i}) {code}: {state}")
    if state == True:
        print(code)
        answers.append(code)
    i += 1

finalanswer = ''
for item in answers:
    finalanswer += item[3]
print(answers)
print(finalanswer)