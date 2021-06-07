from PIL import Image

im = Image.open("/Users/School_Account/Dropbox/programming/T2 python/Python Challenge/num7.png")
#im = Image.open("/Users/hjcho/Dropbox/programming/T2 python/Python Challenge/num7.png")

pixels = list(im.getdata())
width, height = im.size
pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]
print(height)
print(width)
pixelrow = [im.getpixel((j, height/2)) for j in range(width)]
pixelrow = pixelrow[::7]

print(pixels)

rightpixels = []
for r, g, b, a in pixelrow:
    if r == g == b:
        rightpixels.append(r)

message = ''
for n in rightpixels:
    message += chr(n)
print('\n' + message)

nextlvl = [105, 110, 116, 101, 103, 114, 105, 116, 121]

message = ''
for n in nextlvl:
    message += chr(n)
print('\n' + message)