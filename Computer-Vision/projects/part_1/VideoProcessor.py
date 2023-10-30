import cv2 as cv
from dataclasses import dataclass
from typing import Union


@dataclass
class VideoProcessor:
    video: Union[str, cv.VideoCapture]
    subtractor: cv.BackgroundSubtractorMOG2

    def get_foreground_mask(self, frame):
        """
        Метод приймає кадр зображення (frame) та застосовує об'єкт віднімання фону (bg_subtractor) до нього,
        щоб отримати маску переднього плану (foreground mask).
        Згадайте, що bg_subtractor це об'єкт віднімання фону, створений з cv.createBackgroundSubtractorMOG2(Num1, Num2).
        """
        return self.subtractor.apply(frame)


def main():
    video_path = 'video/double_pp.mp4'
    video_capture = cv.VideoCapture(video_path)
    if not video_capture.isOpened():
        print(f"Помилка: Неможливо відкрити відеофайл: {video_path}")
        return

    bg_subtractor = cv.createBackgroundSubtractorMOG2(60, 50)
    video_processor = VideoProcessor(video=video_capture, subtractor=bg_subtractor)

    while True:
        ret, frame = video_capture.read()
        if not ret:
            # Якщо кадр не може бути зчитаний, припинити цикл
            break

        # Отримання маски переднього плану для поточного кадру
        mask = video_processor.get_foreground_mask(frame)
        # Маска відображається за допомогою
        cv.imshow('Маска', mask)

        # Додати невелику затримку (20 мілісекунд) між кадрами, щоб контролювати частоту кадрів
        if cv.waitKey(20) & 0xFF == ord('X'):
            break

    # Звільнити ресурс зчитування відео та закрити вікна OpenCV
    video_capture.release()
    cv.destroyAllWindows()


if __name__ == "__main__":
    main()
