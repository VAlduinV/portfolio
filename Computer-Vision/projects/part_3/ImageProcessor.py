import cv2 as cv
from dataclasses import dataclass


@dataclass
class ImageProcessor:
    image_path: str

    def apply_threshold(self, threshold_value=35):
        image = cv.imread(self.image_path)
        gray_image = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
        _, result = cv.threshold(gray_image, threshold_value, 255, cv.THRESH_BINARY)
        return result

    def apply_adaptive_threshold(self, block_size=81, constant=4):
        image = cv.imread(self.image_path)
        gray_image = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
        adaptive = cv.adaptiveThreshold(gray_image, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, block_size,
                                        constant)
        return adaptive


def main():
    image_path = 'images/book.png'
    image_processor = ImageProcessor(image_path)

    # Візуалізація оригінального зображення
    original_image = cv.imread(image_path)
    cv.imshow('Original Image', original_image)

    # Візуалізація зображення після застосування порогового перетворення
    result = image_processor.apply_threshold(threshold_value=35)
    cv.imshow('Result', result)

    # Візуалізація зображення після застосування адаптивного порогового перетворення
    adaptive_result = image_processor.apply_adaptive_threshold(block_size=81, constant=4)
    cv.imshow('Adaptive result', adaptive_result)

    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == "__main__":
    main()
