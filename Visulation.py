import matplotlib.pyplot as plt
import cv2

# 5 adet görseli yükleyin (örnek olarak, yol ve dosya adlarını güncelleyin)
image = cv2.imread("bjorke_96.png")
image1 = cv2.imread('bjorke_96_gt.jpg')
image2 = cv2.imread('c2fvl.jpg')
image3 = cv2.imread('wt.jpg')
image4 = cv2.imread('unext.jpg')
image5 = cv2.imread('caranet.png')

# Görselleri yan yana göstermek için bir subplot oluşturun
plt.figure(figsize=(18, 5))

# İlk sütun
plt.subplot(161)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Gerçek Görüntü')
plt.axis('off')

plt.subplot(162)
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
plt.title('Gerçek Maske')
plt.axis('off')

# İkinci sütun
plt.subplot(163)
plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))
plt.title('C2FVL (Metinli)')
plt.axis('off')

# Üçüncü sütun
plt.subplot(164)
plt.imshow(cv2.cvtColor(image3, cv2.COLOR_BGR2RGB))
plt.title('C2FVL (Metinsiz)')
plt.axis('off')

# Dördüncü sütun
plt.subplot(165)
plt.imshow(cv2.cvtColor(image4, cv2.COLOR_BGR2RGB))
plt.title('UneXt')
plt.axis('off')

# Beşinci sütun
plt.subplot(166)
plt.imshow(cv2.cvtColor(image5, cv2.COLOR_BGR2RGB))
plt.title('CaraNet')
plt.axis('off')

# Görselleri göster
plt.show()
