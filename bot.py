import cv2
import requests
import time

cap = cv2.VideoCapture(0)  

fgbg = cv2.createBackgroundSubtractorMOG2()

min_contour_area = 20000

bot_token = '{yourTOKEn}'
chat_id = '{YOURid}'


count = 0
last_message_time = time.time()

while True:
    ret, frame = cap.read()

    fgmask = fgbg.apply(frame)

    contours, _ = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) > min_contour_area:
            current_time = time.time()
            if current_time - last_message_time > 7:  
                count += 1
                print("Alguém passou!", count)
                message = f"Alguém passou! Contagem: {count}"
                url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={message}"
                requests.get(url)
                last_message_time = current_time

    cv2.imshow('Frame', frame)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
