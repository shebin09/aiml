import cv2
import matplotlib.pyplot as plt
import os



def capture_image_from_webcam(save_path='captured_image.jpg'):
    cap=cv2.VideoCapture(0)
    if not cap.isOpened(): 
        raise RuntimeError('not opening')
    print('space to capture q to quit')
    img=None
    while True:
        ret,frame=cap.read()
        if not ret:
            print('failed to grab frame')
            break
        cv2.imshow('Webcam - press SPACE to capture', frame)

        k=cv2.waitKey(1)
        if k%256==32:
            img=frame.copy()
            cv2.imwrite(save_path,img)
            break
        elif k%256== ord('q'):
            print('image not taken')
            img = None
            break
    cap.release()
    cv2.destroyAllWindows()
    return save_path if img is not None  else None
    
captured= capture_image_from_webcam()

if os.path.exists('captured_image.jpg'):
    img_bgr=cv2.imread('captured_image.jpg')
    img_rgb=cv2.cvtColor(img_bgr,cv2.COLOR_BGR2RGB)
    plt.figure(figsize=(6,4))
    plt.imshow(img_rgb)
    plt.axis('off')
    plt.title("captured image")
    plt.show()