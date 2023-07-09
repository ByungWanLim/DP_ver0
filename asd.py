import pytesseract
import cv2

# 이미지 파일 경로
image_path = 'C:\Workspace\DP_ver0/lalaland.jpg'

# 이미지 열기
image = cv2.imread(image_path)
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 이미지에서 텍스트 추출
text = pytesseract.image_to_string(image, lang='kor')

# 추출된 텍스트 출력
print(text)