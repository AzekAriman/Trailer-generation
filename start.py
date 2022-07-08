import os
import numpy as np
import cv2
from glob import glob

def create_dir(path):
    try:
        if not os.path.exists(path):
            os.makedirs(path)
    except OSError:
        print(f"ERROR: creating directory with name {path}")

def save_frame(video_path, save_dir, gap=10): 
    print(video_path)
    name = video_path.split("\\")[-1].split(".")[0]
    save_path = os.path.join(save_dir, name)
    print(name)
    create_dir(save_path)

    # читаем видео из файла
    cap = cv2.VideoCapture(video_path)
    idx = 0     # номер кадра
    while True:
        # Метод cap.read() возвращают кортеж, первым элементом 
        # является логическое значение а вторым кадр
        ret, frame = cap.read()
        # отображение текущего фрейма в окне
        #if ret == True:
           # cv2.imshow('Look', frame)
           # key = cv2.waitKey(20)
           # if (key == ord('q')) or key == 27:
           #     break
            
        if ret == False:
            #Освободить камеру
            cap.release()
            break

        if idx == 0:
            # сохранить изображение 
            cv2.imwrite(f"{save_path}/{idx}.png", frame)
        else:
            if idx % gap == 0:
                cv2.imwrite(f"{save_path}/{idx}.png", frame)

        idx += 1

def main():
    video_paths = glob("videos/*") # glob возвращает список имен путей, которые находятся в каталоге
    print(video_paths)
    save_dir = "save"
    for path in video_paths:
        save_frame(path, save_dir, gap=10)

if __name__ == "__main__":
    main()
    