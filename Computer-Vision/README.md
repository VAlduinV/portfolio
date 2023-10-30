# Computer-Vision

[![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/)
[![OpenCV](https://img.shields.io/badge/OpenCV-red.svg)](https://opencv.org/)
[![Wikipedia](https://img.shields.io/badge/Wikipedia-green.svg)](https://en.wikipedia.org/wiki/Computer_vision)
[![CV](https://img.shields.io/badge/Computer-Vision-violet.svg)](https://github.com/VAlduinV/Computer-Vision)
[![Typing SVG](https://readme-typing-svg.demolab.com?font=Arial+Black&weight=500&size=30&pause=1000&color=F70000&center=true&vCenter=true&width=435&lines=Computer+Vision)](https://git.io/typing-svg)

# Projects

## Part_1

## Віднімання фону з відео за допомогою OpenCV

Цей код демонструє використання OpenCV для віднімання фону з відео і отримання маски переднього плану для кожного кадру 
відео.

## Встановлення залежностей
Перед використанням коду, впевніться, що у вас встановлені такі залежності:
- Python 3.x
- OpenCV (cv2 бібліотека)
- NumPy

```shell
   pip install -r requirements.txt
```

## Використання коду

1. Завантажте відеофайл, з якого ви хочете видалити фон, та збережіть його у папці video.
2. Запустіть скрипт VideoProcessor.py, який буде зчитувати відео та обробляти його кадри.

```shell
   python VideoProcessor.py
```

## Part_2

## Методи Лапласіана та Кенні
Матеріал для ознайомлення можете знайти перейшовши за наступним посиланням:
- <span style="color: red;">Реалізація методів Лапласіана та Кенні https://en.wikipedia.org/wiki/Canny_edge_detector .</span>


## Деталі реалізації
Скрипт LaplacianProcessor.py містить клас LaplacianProcessor, який інкапсулює логіку камери та обробки методом Лапласіана. 
Для обробки зображення та відео використовується бібліотека OpenCV. 
Скрипт здійснює захоплення кадрів з камери, застосовує метод Лапласіана та Кенні
для виявлення ребер (країв) і відображає результати за допомогою функції imshow з OpenCV.

## Part_3

## Image Thresholding з використанням OpenCV
Цей код демонструє використання OpenCV для застосування 
порогового перетворення та адаптивного порогового перетворення на зображеннях.

## Використання коду
- Завантажте зображення, на якому ви хочете виконати порогове перетворення, та збережіть його у папці images. 
- Замініть book.png на ім'я свого зображення у файлі ImageProcessor.py.
- Запустіть скрипт ImageProcessor.py, який застосує порогове перетворення та адаптивне порогове перетворення до зображення.

## Клас ImageProcessor
Цей клас використовується для обробки зображень і застосування порогового перетворення та адаптивного порогового 
перетворення.

# Ліцензія
Цей код надається [ліцензією MIT](LICENSE).  
Вільно використовуйте і змінюйте його згідно з вашими потребами.

