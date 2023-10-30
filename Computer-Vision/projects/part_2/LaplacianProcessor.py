import cv2 as cv
import numpy as np
from dataclasses import dataclass


@dataclass
class LaplacianProcessor:
    camera: cv.VideoCapture

    def process_frame(self, frame):
        laplacian = cv.Laplacian(frame, cv.CV_64F)
        laplacian = np.uint8(laplacian)
        return laplacian


def main():
    camera = cv.VideoCapture(0)
    processor = LaplacianProcessor(camera)

    while True:
        _, frame = camera.read()
        cv.imshow('camera', frame)

        laplacian_frame = processor.process_frame(frame)
        cv.imshow('Laplacian', laplacian_frame)

        edges = cv.Canny(frame, 50, 50)
        cv.imshow('Canny', edges)

        if cv.waitKey(5) == ord('X'):
            break

    camera.release()
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()
