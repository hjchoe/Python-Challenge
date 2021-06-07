import urllib.request
import re

code = 12345

while True:
    with urllib.request.urlopen(f'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={code}') as response:
        html = response.read()
    html = html.decode("utf-8") 
    divide = re.search(r'Divide by two and keep going.', html)
    if divide:
        print("DIVIDED by TWO")
        code = int(code)/2
    else:
        try:
            code = re.search(r'the next nothing is \d+', html)
            code = code.group()
            code = code[20:25]
            print(code)
        except:
            try:
                code = re.search(r'the next nothing \d+', html)
                code = code.group()
                code = code[20:25]
                print(code)
            except:
                break

print(html)