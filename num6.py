import re
import zipfile

code = 90052
comments = []
#archive = zipfile.ZipFile(r'/Users/hjcho/Dropbox/programming/T2 python/Python Challenge/channel.zip', 'r')
archive = zipfile.ZipFile(r'/Users/School_Account/Dropbox/programming/T2 python/Python Challenge/channel.zip', 'r')

while True:
    #f = open(f"/Users/hjcho/Dropbox/programming/T2 python/Python Challenge/channel/{code}.txt", 'r')
    f = open(f"/Users/School_Account/Dropbox/programming/T2 python/Python Challenge/channel/{code}.txt", 'r')
    c = archive.getinfo(f"{code}.txt")
    c = c.comment
    c = c.decode("utf-8")
    comments.append(c)
    contents = f.readlines()
    content = contents[0]
    code = re.search(r'Next nothing is \d+', content)
    if code:
        code = code.group()
        code = code[16:21]
        print(code)
    else:
        print(content)
        break

print(comments)

comment = "".join(comments)
print(comment)