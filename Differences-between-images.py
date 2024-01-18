import cv2
import numpy as np
import matplotlib.pyplot as plt

def farkli_pikselleri_bul(goruntu1, goruntu2):
    # İki görüntü arasındaki farkları bul
    farklar = cv2.absdiff(goruntu1, goruntu2)
    farklar_griton = cv2.cvtColor(farklar, cv2.COLOR_BGR2GRAY)
    _, farklar_thresh = cv2.threshold(farklar_griton, 30, 255, cv2.THRESH_BINARY)

    return farklar_thresh

def goruntuleri_karsilastir(goruntu1, goruntu2):
    # Farklı pikselleri bul
    farklar = farkli_pikselleri_bul(goruntu1, goruntu2)

    # Görüntüleri çiz
    plt.figure(figsize=(10, 5))
    plt.subplot(131), plt.imshow(cv2.cvtColor(goruntu1, cv2.COLOR_BGR2RGB)), plt.title('Gerçek Maske')
    plt.subplot(132), plt.imshow(cv2.cvtColor(goruntu2, cv2.COLOR_BGR2RGB)), plt.title('C2FVL (Metinli)')
    plt.subplot(133), plt.imshow(farklar, cmap='gray'), plt.title('Farklar')

    plt.axis('off')
    plt.show()

# Örnek kullanım
goruntu1 = cv2.imread('bjorke_96_gt.jpg')
goruntu2 = cv2.imread('c2fvl.jpg')

goruntuleri_karsilastir(goruntu1, goruntu2)