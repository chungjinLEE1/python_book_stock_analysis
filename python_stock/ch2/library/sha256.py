import hashlib

sha_src = hashlib.sha256()
sha_dst = hashlib.sha256()

with open ('test1.JPG', 'rb') as sf, open('test2.jpg', 'rb') as df:
    sha_src.update(sf.read())
    sha_dst.update(df.read())


print("src.png's hash : {}".format(sha_src.hexdigest()))
print("dst.png's hash : {}".format(sha_dst.hexdigest()))

# 파일 내용이 동일하기 때문에 해쉬 값이 같은지 확인되어야 한다.