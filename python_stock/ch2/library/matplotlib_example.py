import matplotlib.pyplot as plt
import matplotlib.image as mpimg

dst_img = mpimg.imread('test1.jpg')

print(dst_img)

print("##################")
# 의사 색상 적용하기
pseudo_img = dst_img [:, :, 0]
print(pseudo_img)

# matplot로 이미지 비교하기
plt.suptitle('Image Processing', fontsize=18)
plt.subplot(1,2,1)
plt.title('Original Image')
plt.imshow(mpimg.imread('test1.jpg'))

plt.subplot(122)
plt.title('Pseudocolor Image')
dst_img = mpimg.imread('test1.jpg')
pseudo_img = dst_img [:, :, 0]
plt.imshow(pseudo_img)
plt.show()