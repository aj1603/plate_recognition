import cv2
import pytesseract

cap = cv2.VideoCapture(0) # varsayılan kamera kullanılıyor

while True:
    ret, frame = cap.read() # kameradan bir kare yakala
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # görüntüyü gri tonlamalı hale getir
    
    # kenar algılama
    edges = cv2.Canny(gray, 50, 150)
    edges = cv2.dilate(edges, None, iterations=1)
    edges = cv2.erode(edges, None, iterations=1)
    
    # dikdörtgen şekli ile plaka bölgesini belirle
    contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        x,y,w,h = cv2.boundingRect(cnt)
        if w > 100 and h > 30:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            roi = frame[y:y+h, x:x+w]
            text = pytesseract.image_to_string(roi, config='--psm 11') # metni tanı
            print(text) # metni yazdır
    
    cv2.imshow('frame', frame) # işlenmiş görüntüyü göster
    
    if cv2.waitKey(1) & 0xFF == ord('q'): # q tuşuna basarak çıkış yap
        break

cap.release() # kamera aygıtını serbest bırak
cv2.destroyAllWindows() # tüm pencereleri kapat
