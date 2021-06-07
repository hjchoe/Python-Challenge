import pickle
from urllib.request import urlopen

#f = open("/Users/hjcho/Dropbox/programming/T2 python/Python Challenge/num3.txt", 'r')
#f = open("/Users/School_Account/Dropbox/programming/T2 python/Python Challenge/peak.txt", 'r')
data = pickle.load(urlopen("http://www.pythonchallenge.com/pc/def/banner.p"))

print(data)

for line in data:
    print("".join([i * j for i, j in line]))
