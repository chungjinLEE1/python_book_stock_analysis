# 리쿼스트로 인터넷에서 이미지 파일 가져오기
# 파일 객체를 이용하여 일정 크기로 읽고 쓰면서 파일 복사하기
# SHA-256 해시값으로 두 파일의 동일 여부 확인하기
# 맷플롯립으로 이미지를 가공해서 비교하기.

# 리쿼스트로 이미지 파일 가져오기.
import requests

url = 'https://www.google.co.kr/url?sa=i&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DH-L6ylrziJE&psig=AOvVaw1HdfgE7q1aP9LBJy9VQgJS&ust=1648702072556000&source=images&cd=vfe&ved=0CAgQjRxqFwoTCPCMg4mE7fYCFQAAAAAdAAAAABAP'
r = requests.get(url, stream=True).raw


print(r)

