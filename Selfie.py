import cv2
import time

start_time = time.time() 

def take_selfie():
    number = 1
    total_selfies = 3 
    # Change this value to capture a different number of photos
    videoCaptureObject = cv2.VideoCapture(0)
    result = True

    while result and number <= total_selfies:
        ret, frame = videoCaptureObject.read()
        img_name = f"img{number}.png"
        cv2.imwrite(img_name, frame)
        print("Photo " + str(number))
        number += 1
        #Creating downtime inbetweet photos
        time.sleep(1)  

    videoCaptureObject.release()
    cv2.destroyAllWindows()

def main():
    while True:
        user_input = input("Press S to take 3 selfies and choose the best one (or 'exit' to quit): ")
        if user_input == "s" or "S":
            take_selfie()
            
        elif user_input == 'exit':
            break
main()
