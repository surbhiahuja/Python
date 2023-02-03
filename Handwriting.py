
import pywhatkit as kit
import cv2

txt = """retrfr
eweewew
erewrew"""

kit.text_to_handwriting("Hope you are doing well", save_to="handwriting.png")
img = cv2.imread("download.jpeg")
cv2.imshow("Text to Handwriting", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

kit.text_to_handwriting(txt, "demo3.png", [255,0,0])
print("END")