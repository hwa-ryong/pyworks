import cv2

img = cv2.imread("./source/activity.jpg", cv2.IMREAD_COLOR)
cv2.imshow('activity', img)
cv2.waitKey(0) # 계속 대기, 2000 - 2초

# 파일 쓰기(복사)
cv2.imwrite('./source/activity2.jpg', img)  #imwrite(경로, 파일)

# 회색 스타일 수정
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('activity', img_gray)
cv2.waitKey(0)

# 파일 쓰기 (복사)
cv2.imwrite('./source/activity3.jpg', img_gray)  #imwrite(경로, 파일)