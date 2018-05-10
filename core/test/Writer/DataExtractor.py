import cv2
import numpy as np

file_loc = 'C:\\Users\\vince\\Desktop\\book5_cut\\{}.png'
images = []

for i in range(1, 200):
    print(file_loc.format(i))
    images.append(cv2.imread(file_loc.format(i)))

i = 0
for img in images:
    xy = 0
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    template = cv2.imread('C:\\Users\\vince\\Desktop\\patterns\\number.png', 0)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):
        sub = img[pt[1]+15:pt[1] + h-2, pt[0]+15:pt[0] + w-2]
        cv2.imwrite('C:\\Users\\vince\\Desktop\\res\\{}.png'.format(i), sub)
        import time
        time.sleep(3)
        xy += 1
    i += 1
    print(i)