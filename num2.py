#f = open("/Users/hjcho/Dropbox/programming/T2 python/Python Challenge/num2.txt", 'r')
f = open("/Users/School_Account/Dropbox/programming/T2 python/Python Challenge/num2.txt", 'r')
code = f.readlines()

characters = []
for line in code:
    for char in line:
        characters.append(char)

#characters.sort()

for i in range(10):
    maxchar = ''
    maxn = 1000000
    diffchars = []
    for char in characters:
        if char not in diffchars:
            curn = characters.count(char)
            if curn < maxn:
                maxn = curn
                maxchar = char
            diffchars.append(char)

    for x in range(maxn):
        characters.pop(characters.index(maxchar))

    print(maxn, maxchar)