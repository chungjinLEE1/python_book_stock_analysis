BUF_SIZE = 1024
with open('test1.jpg', 'rb') as sf, open('test2.JPG', 'wb') as df:
    while True:
        data = sf.read(BUF_SIZE)
        if not data:
            break
        df.write(data)