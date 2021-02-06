# Knights AI

## Overview

Knights game with the possibility of playing with artificial intelligence, based on the Monte Carlo Tree Search algorithm. 🏆

<!-- TABLE OF CONTENTS -->
## Table of Contents

- [Knights AI](#knights-ai)
  - [Overview](#overview)
  - [Table of Contents](#table-of-contents)
  - [About The Project](#about-the-project)
    - [Description](#description)
      - [Rules](#rules)
      - [Algorithm](#algorithm)
    - [Built With](#built-with)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
  - [Usage](#usage)
  - [Roadmap](#roadmap)
  - [Contributing](#contributing)
  - [License](#license)
  - [Contact](#contact)
  - [Acknowledgements](#acknowledgements)


<!-- ABOUT THE PROJECT -->
## About The Project

![Main Screen Shot][main-screenshot]

### Description

#### Rules
Knights game is played on an 8x8 board. Each of the two players has 16 knights. Each of them can move one square in any direction. They can also jump over several other knights in one move (like in draughts). The goal of the game is to put all of the knights at the end of the board.

#### Algorithm
Monte Carlo Tree Search (MCTS) is one of the best algorithms for board game engines. It uses much less resources than classical versions of tree search algorithms. MCTS keeps perfect balance between exploration and exploitation of the tree. The implementation of this algorithm is based on the implementation of Mr. Jeff Brady. Big credits for him!

### Built With

* [Pygame](https://www.pygame.org/)


<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

* [Python 3.x](https://www.python.org/)
* [Virtualenv](https://virtualenv.pypa.io/)


### Installation

1. Clone the repo
```sh
git clone https://github.com/DavidSolomon22/knights-ai.git
```
2. Create virtual enviroment by using below command inside the root direcotry of this project
```sh
virtualenv venv
```
3. Activate virtual enviroment
```sh
source venv/bin/activate
```
4. Install required packages
```sh
pip install -r requirements.txt
```
5. Go inside working directory
```sh
cd knights-ai
```
6. Run program
```sh
python3 main.py
```


<!-- USAGE EXAMPLES -->
## Usage

![Start Screen Shot][start-screenshot]

![In-game Screen Shot][in-game-screenshot]


<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/DavidSolomon22/knights-ai/issues) for a list of proposed features (and known issues).

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/amazing-feature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.


<!-- CONTACT -->
## Contact

David Solomon - via [Linkedin](https://www.linkedin.com/in/david-solomon-107305192)


<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [mcts](https://github.com/jbradberry/mcts)



<!-- MARKDOWN LINKS & IMAGES -->
[main-screenshot]: docs/main.png
[start-screenshot]: docs/start.png
[in-game-screenshot]: docs/in-game.png
