import cv2
from skimage.metrics import structural_similarity as ssim

# İki resmi yükleyin
image1 = cv2.imread("resim1.png")
image2 = cv2.imread("resim2.png")

# Resimleri gri tonlamalı olarak dönüştürün
gray_image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
gray_image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

# İki resim arasındaki yapısal benzerliği hesaplayın
(score, diff) = ssim(gray_image1, gray_image2, full=True)
diff = (diff * 255).astype("uint8")

# Sonuçları yazdırın
print("Benzerlik skoru: {}".format(score))
