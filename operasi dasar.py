#OPERASI DASAR CITRA
import matplotlib.pyplot as plt

from skimage import data
from skimage.io import imread
from skimage.color import rgb2gray
from skimage.util import invert

import numpy as np
import cv2
#percobaan 1 crop image
img = cv2.imread("harley.jpg")
img2 = cv2.imread("sawah.jpg")

imgcroped = img.copy()
imgcroped = imgcroped[0:256,64:320]
astronautImage = data.astronaut()
cameraImage = data.camera()

astroCropped = astronautImage.copy()
astroCropped = astroCropped[0:256,64:320]

cameraCropped = cameraImage.copy()
cameraCropped = cameraCropped[64:256,128:320]

img2croped = img2.copy()
img2croped = img2croped[0:256,64:320]

fig,axes = plt.subplots(2,2, figsize=(12,12))
ax=axes.ravel()

ax[0].imshow(img)
ax[0].set_title("Citra Input 1")

ax[1].imshow(img2,cmap='gray')
ax[1].set_title("Citra Input 2")

ax[2].imshow(imgcroped)
ax[2].set_title("Citra output 1")

ax[3].imshow(img2croped,cmap='gray')
ax[3].set_title("Citra output 2")

plt.show()

# Citra Negative
inv = invert(imgcroped)
print('Shape Input : ', imgcroped.shape)
print('Shape Output : ',inv.shape)

fig, axes = plt.subplots(2, 2, figsize=(12, 12))
ax = axes.ravel()

ax[0].imshow(imgcroped)
ax[0].set_title("Citra Input")

ax[1].hist(imgcroped.ravel(), bins=256)
ax[1].set_title('Histogram Input')

ax[2].imshow(inv)
ax[2].set_title('Citra Output (Inverted Image)')

ax[3].hist(inv.ravel(), bins=256)
ax[3].set_title('Histogram Output')
plt.show()

copyCamera = cameraCropped.copy().astype(int)

m1,n1 = copyCamera.shape
output1 = np.empty([m1, n1])

for baris in range(0, m1-1):
    for kolom in range(0, n1-1):
        a1 = baris
        b1 = kolom
        output1[a1, b1] = copyCamera[baris, kolom] + 100
        
fig, axes = plt.subplots(2, 2, figsize=(12, 12))
ax = axes.ravel()

ax[0].imshow(cameraCropped, cmap='gray')
ax[0].set_title("Citra Input")

ax[1].hist(astroCropped.ravel(), bins=256)
ax[1].set_title('Histogram Input')

ax[2].imshow(output1, cmap='gray')
ax[2].set_title('Citra Output (Brightnes)')

ax[3].hist(output1.ravel(), bins=256)
ax[3].set_title('Histogram Input')
plt.show()
