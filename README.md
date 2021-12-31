# Flappy - Codeology Fall 2021

## **Description**
<hr>

Flappy is a game dev + AI project that uses the NEAT (Neuroevolution of Augmenting Topologies) algorithm to train a neural net for playing Flappy Bird.

## **Member Projects**
<hr>

Each member chose an extension to the original project and made it their own! See the results below:

Ash Chang - https://github.com/ashchangg/flappy_special

Ernest Goh - https://github.com/ernestggoh/SpaceInvadersNEAT

Ramya Chitturi - https://github.com/r-chitturi/flappy_NEAT_qlearning 

Euhan Kim - https://github.com/euhan123/NEAT-SpaceInvaders

Maya Zheng - 

## **Tutorial**
<hr>

Find the tutorial on Notion [here](https://chemical-linen-be0.notion.site/FlapPy-68ea8a19ea0c42fe853e27daf93ca3cb)!

## **Setup**
<hr>

### **Installing Python**
Make sure that you have Python 3.7.7 or higher:
```
python3 --version
```

**Linux (Ubuntu)**
```
sudo apt install python3
```

**macOS**

Download from this website: [Python 3](https://www.python.org/downloads/mac-osx/)

**Windows**

Download from this website: [Python 3](https://www.python.org/downloads/windows/)

### **Clone the Repository**
```
// Not finished yet
```

### **Setting Up a Virtual Environment**
Python virtual environments let us separate environments for each project we create. Why do we need them?
- To control dependencies and their versions
- To avoid installing packages globally. Instead, we'll be installing them within the virtual environment.
```
python3 -m venv .venv
source .venv/bin/activate
```

To deactivate an environment, use:
```
deactivate
```

### **Pygame**
Pygame will be the package we use to create our game.
```
python3 -m pip install -U pygame
python3 -m pygame.examples.aliens
```
If running the demo game works, you're good to go.

### **NEAT-Python**
NEAT-Python is a package that implements the NEAT (Neuro-Evolution of Augmenting Topologies) algorithm. The algorithm will be used to teach the machine how to play the game you develop.
```
pip install neat-python
``` 
