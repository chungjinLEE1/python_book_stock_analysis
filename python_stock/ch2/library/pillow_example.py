from PIL import Image

image = Image.open("c://test1.JPG")

print(type(image))

image.show()

from PIL import Image

img = Image.open("c://test1.JPG")
print(f'이미지파일이름 : {img.filename}')
print(f'이미지파일형식 : {img.format}')
print(f'이미지용량 : {img.size}')
print(f'이미지색상모드 : {img.mode}')
print(f'이미지width : {img.width}')
print(f'이미지 height : {img.height}')


# 이미지 크기 변경하기
resize_img = image.resize((800, 800))
resize_img.save("C://test2_800x800.jpg")