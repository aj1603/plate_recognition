import requests, json
from time import sleep
from datetime import datetime, timedelta
import cv2, time
import pytesseract
from main.db_migration_data.car_config import cars

id = 0
delay_seconds = 10
last_time = datetime.now()
treshold = 40
door_server_url = "http://127.0.0.1:6060"
timer = time.time()

# pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"
vid= cv2.VideoCapture(0)

def send_request():
	payload = {"command": "unlock_door", "state": 2, "action": ""}
	r = requests.post(
        	"{}{}".format(door_server_url,"/car/"),
		data = json.dumps(payload),
		headers = {'Content-Type': 'application/json'})


while True:
    ret , cap = vid.read()
    gray = cv2.cvtColor(cap, cv2.COLOR_BGR2GRAY)
    gary = cv2.bilateralFilter(gray, 11,17,17)
    an = cv2.Canny(cap ,  170,200)
    cnts , new = cv2.findContours(an.copy(),cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    cap1 = cap.copy()
    cv2.drawContours(cap1, cnts, -1, (0,255,0),3)
    cnts = sorted(cnts , key = cv2.contourArea, reverse = True)[:30]
    plate = None
    cap2 = cap.copy()
    cv2.drawContours(cap2, cnts , -1 ,(0,255,0),3)
    count= 0
    name = 1
    for i in cnts:
        perimetr = cv2.arcLength(i, True)
        approx= cv2.approxPolyDP(i , 0.02* perimetr, True)
        if (len(approx)==4):
            plate = approx
            x,y,w,h = cv2.boundingRect(i)
            crp_img = cap[y:y+h , x:x+w]
            cv2.imwrite(str(name)+'.png',crp_img)
            name +=1
            break
            cv2.drawContours(cap,[plate], -1,(0,255,0),3)
    crpImg = '1.png'
    cv2.imshow("doly",cv2.imread(crpImg))
    text = pytesseract.image_to_string(crpImg, lang= 'eng')
    print(text)
    if text:
        try:
            payload = {"plate": text}
            r = requests.post(
                    "{}{}".format(door_server_url,"/car"),
                data = json.dumps(payload),
                headers = {'Content-Type': 'application/json'})
            print("sending")
        except Exception as ex:
            print(ex)
        
        # if validate_car(id):
        #     print("sending")
        #     last_time = datetime.now()
        #     try:
        #         send_request()
        #     except Exception as ex:
        #         print(ex)
                #sleep(5)
    # cv2.imshow("asyl" , cap)
    # cv2.imshow('gray', gray)
    # cv2.imshow('gra1y', gray)
    # cv2.imshow('okno', an)
    # cv2.imshow('okno1', cap1)
    # cv2.imshow('okno1', cap2)
    # cv2.imshow('final', cap)



    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
vid.release()
cv2.destroyAllWindows()
