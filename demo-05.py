from picamera2 import Picamera2
import cv2
from time import sleep, time

# Kamera initialisieren
picam2 = Picamera2()

# Vorschau-Konfiguration erstellen
preview_config = picam2.create_preview_configuration(main={"size": (640, 480)})
picam2.configure(preview_config)

# Kamera starten
picam2.start()
sleep(2)  # Stabilisierung

# Haar-Cascade-Klassifikator laden
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# FPS-Messung
frame_count = 0
start_time = time()

try:
    while True:
        # Frame von der Kamera erfassen
        frame = picam2.capture_array()

        # Konvertiere das Frame in Graustufen
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Gesichter im Graustufen-Frame erkennen
        faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.05, minNeighbors=5, minSize=(30, 30))

        # Zeichne Rechtecke um erkannte Gesichter
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Zeigt das Frame mit den erkannten Gesichtern an
        cv2.imshow("Face Detection", frame)

        # FPS berechnen und anzeigen
        frame_count += 1
        elapsed_time = time() - start_time
        if elapsed_time > 1:
            fps = frame_count / elapsed_time
            print(f"FPS: {fps:.2f}")
            frame_count = 0
            start_time = time()

        # Beende mit 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
finally:
    # Kamera stoppen und OpenCV-Fenster schließen
    picam2.stop()
    cv2.destroyAllWindows()
