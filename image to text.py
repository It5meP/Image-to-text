from PIL import Image
import PIL

#default string'$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft\|)1]?-_+~<>i!lI;:,"^`.⠀⠀⠀⠀⠀⠀⠀⠀⠀'
#black and white string'⬜⬛'
lightdark = '$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft\|)1]?-_+~<>i!lI;:,"^`.............'

#default resolution 128
#blackwhite 64
resolutionwidth=70
URL=r"E:/Visual/Random tools/image to text output.txt"

txtout = open(URL,"w")
len=len(lightdark)

URL = r"E:\Visual\material\image to text.png"
fimg = Image.open(URL)
fimg = fimg.convert("L")

frow = fimg.size[1]
fcol = fimg.size[0]

img = fimg.resize((resolutionwidth,round(frow*resolutionwidth/fcol/2)))
row = img.size[1]
column = img.size[0]
grayscale = [[img.getpixel((x,y)) for x in range (img.size[0])] for y in range (img.size[1])]
final = [[0 for x in range (column)] for y in range (row)]

for i in range(row):
    for j in range (column):
        stt=round(grayscale[i][j]/255*len)
        if (stt==len):
            final[i][j]=lightdark[len-1]

        else:
            final[i][j]=lightdark[stt]
for i in range(row):
    for j in range (column):
        txtout.write(str(final[i][j]))
        #print(final[i][j],end="")
    #print("")
    txtout.write("\n")
txtout.close()


