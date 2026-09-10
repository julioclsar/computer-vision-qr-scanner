import cv2 as cv

cap = cv.VideoCapture(0)
qrDecoder = cv.QRCodeDetector()

while True:
    ret, img = cap.read()
    if not ret:
        break

    dados, pontos, imgReta = qrDecoder.detectAndDecode(img)

    if dados and pontos is not None:
        print(f"Dados detectados: {dados}")
        pontos = pontos.astype(int)
        pontos = pontos.reshape((-1, 1, 2)) 
        cv.polylines(img, [pontos], isClosed=True, color=(0, 255, 0), thickness=3)

    cv.imshow("Detector de QR Code", img)

    if cv.waitKey(1) & 0xFF == ord('s'):
        break

cap.release()
cv.destroyAllWindows()

