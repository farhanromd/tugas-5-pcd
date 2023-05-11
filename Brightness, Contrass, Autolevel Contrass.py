import numpy as np
import cv2 
import imageio.v2 as imageio
import matplotlib.pyplot as plt

#load gambar
img = cv2.imread("harley.jpg")

#mendapatkan/define resolusi dan tipe gambar
#dipake diperulangan
img_height = img.shape[0] 
#tinggi gambar
img_widht = img.shape[1] 
#lebar gambar
img_channel = img.shape[2]
 #banyaknya channel setiap pixel
img_type = img.dtype #type gambar

#BRIGHTNESS GRAYSCALE
#menampung image yang sudah dicerahkan
img_brightnes = np.zeros(img.shape, dtype=np.uint8)

#fungsi penambahan brightness dengan nilai yang menjadi parameter
def brighter(nilai):
    for y in range(0,img_height): #height
        for x in range(0,img_widht):
            red = img[y][x][0]
            green = img[y][x][1]
            blue = img[y][x][2]
            gray = (int(red)+int(green)+int(blue))/3
            gray += nilai
            if gray >255:
                gray = 255
            if gray<0:
                gray=0
            img_brightnes[y][x] = (gray,gray,gray)
#menampilkan gambar dengan parameter brightness-100 dan 100
brighter(-100)
plt.imshow(img_brightnes)
plt.title("Brightness -100")
plt.show()

brighter(100)
plt.imshow(img_brightnes)
plt.title("Brightness 100")
plt.show()

#BRIGHTNES RGB
#membuat variabel img_rgbbright untuk menampung hasil
img_rgbbrightness = np.zeros(img.shape, dtype=np.uint8)
#Melakukan penambahan brightness dengan nilai yg menjadi parameter
def rgbbrighter(nilai):
    for y in range(0,img_height):
        for x in range(0,img_widht):
            red= img[y][x][0]
            red+=nilai
            if red>255:
                red = 255
            if red<0:
                red=0
            green= img[y][x][1]
            green+=nilai
            if green>255:
                green = 255
            if green<0:
                green=0
            blue= img[y][x][2]
            blue+=nilai
            if blue>255:
                blue=255
            if blue<0:
                blue=0
            img_rgbbrightness[y][x]=(red,green,blue)
#Menampilkan beberapa hasil dengan nilai brightness -100 dan 100
rgbbrighter(-100)
plt.imshow(img_rgbbrightness)
plt.title("Brightness -100")
plt.show()

rgbbrighter(100)
plt.imshow(img_rgbbrightness)
plt.title("Brightness 100")
plt.show()

#CONTRAS
#Membuat variabel img_contrass untuk menampung hasil
img_contras = np.zeros(img.shape,dtype=np.uint8)

#Melakukan penambahan contrass dengan nilai yg menjadi parameter
def contras(nilai):
    for y in range(0,img_height):
        for x in range(0,img_widht):
            red = img[y][x][0]
            green = img[y][x][1]
            blue = img[y][x][2]
            gray=(int(red)+int(green)+int(blue))/3
            gray+=nilai
            if gray>255:
                gray=255
            img_contras[y][x]=(gray,gray,gray)
#Menampilkan beberapa hasil dengan nilai brightness -100 dan 100
contras(2)
plt.imshow(img_contras)
plt.title("contrass 2")
plt.show()

contras(10)
plt.imshow(img_contras)
plt.title("contrass 3")
plt.show()

#CONTRASS AUTOLEVEL

#Membuat variabel img_contrass untuk menampung hasil
img_rgbcontrass = np.zeros(img.shape, dtype=np.uint8)

#Melakukan penambahan contrass secara otomatis
def rgbcontrass(nilai):
    for y in range(0, img_height):
        for x in range(0, img_widht):
            red= img[y][x][0]
            red += nilai
            if red > 255:
                red = 255
            
            green= img[y][x][1]
            green += nilai
            if green > 255:
                green = 255
            
            blue= img[y][x][2]
            blue += nilai
            if blue > 255:
                blue = 255
            
            img_rgbcontrass[y][x]= (red, green, blue)
#Menampilkan hasil autolevel contrass
rgbcontrass(20)
plt.imshow(img_rgbcontrass)
plt.title('Contrass Autolevel 20')
plt.show()

rgbcontrass(100)
plt.imshow(img_rgbcontrass)
plt.title('Contrass Autolevel 100')
plt.show()

#contrast autoleve dengan grayscale
img_autocontrass=np.zeros(img.shape,dtype=np.uint8)

def autocontrass():
    xmax = 255
    xmin=0
    d=0

    for y in range(0,img_height):
        for x in range(0,img_widht):
            red = img[y][x][0]
            green = img[y][x][1]
            blue = img[y][x][2]
            gray = (int(red)+int(green)+int(blue))/3
            if gray<xmax:
                xmax=gray
            if gray>xmin:
                xmin=gray
    d=xmin-xmax
    for y in range(0,img_height):
        for x in range(0,img_widht):
            red=img[y][x][0]
            green=img[y][x][1]
            blue=img[y][x][2]
            gray=(int(red)+int(green)+int(blue))/3
            gray=int(float(255/d)*(gray-xmax))
            img_autocontrass[y][x]=(gray,gray,gray)
autocontrass()
plt.imshow(img_autocontrass)
plt.title('autocontrass')
plt.show()  