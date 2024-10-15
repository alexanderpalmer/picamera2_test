from picamera2 import Picamera2
from picamera2.encoders import H264Encoder
from picamera2.outputs import FileOutput
from time import sleep

# Kamera initialisieren
picam2 = Picamera2()

# Video-Konfiguration erstellen
video_config = picam2.create_video_configuration()
picam2.configure(video_config)

# Kamera starten
picam2.start()
sleep(2)  # Warte für Stabilisierung

# Encoder und Ausgabe definieren
encoder = H264Encoder()
output = FileOutput("video.h264")

# Videoaufnahme starten
picam2.start_recording(encoder, output)
sleep(10)  # Nimmt 10 Sekunden lang auf
picam2.stop_recording()

# Kamera stoppen
picam2.stop()
