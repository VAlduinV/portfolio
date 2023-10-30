# Game_banderogoose

[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/)
[![Static Badge](https://img.shields.io/badge/https:/PyGame-violet)](https://www.pygame.org/news)

<center>
<img src="./img/release.png" alt="release.png"/>
</center>

## Description of the game
Game description:
The game uses the Pygame graphics library and runs in a 1200x800 pixel window.
The main goal of the game is to control the goose character, which is in the background of the Kremlin city,
and avoid enemy objects and collect power-ups to score points.
The game continues until the goose collides with enemy objects.

## Main characteristics:
* The main character is a goose that moves up, down, left and right according to pressing the arrow keys.
* The background of the game is an animated picture of the image of the Kremlin of fire, which moves horizontally from left to right to create the illusion of movement.
* Enemy objects - represented by images of bombs, which are also animated and move from left to right across the screen.
* Bonuses - bonus images that are randomly generated and move down the screen.
* Rating - the player is awarded points for each collected bonus.
* The game ends when the goose collides with enemy objects.
* Logging - a log of the player's actions, such as collisions with enemy objects and collecting bonuses, is kept.

## Installation

1. Clone the repository to your local computer or download the source code files.
2. Make sure you have Python (version 3.x) installed on your system.
3. Install the necessary dependencies by running the following command:

```shell
poetry install
```

## Usage
To run the simulation, run the following command in a terminal or command prompt:

```shell
python main.py
```

## License
This project is available under the [MIT License](LICENSE).

## Acknowledgments
- Pygame library: [https://www.pygame.org](https://www.pygame.org)
