import requests

# API 호출을 위한 URL과 헤더 정보
url = "https://dapi.kakao.com/v2/vision/adult/detect"
headers = {"Authorization": "KakaoAK 여기에 넣으슈"}

# 이미지 파일 경로
image_path = "iot.png"

# API 호출
files = {"file": open(image_path, "rb")}
response = requests.post(url, headers=headers, files=files)

# 응답 확인
if response.status_code == 200:
    result = response.json()
    if "result" in result:
        result = result["result"]
        print("normal:", result["normal"])
        print("soft:", result["soft"])
        print("adult:", result["adult"])
    else:
        print("API 호출에 실패하였습니다.")
else:
    print("API 호출에 실패하였습니다. 응답 코드:", response.status_code)