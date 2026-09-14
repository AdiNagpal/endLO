# Endlo 🎮

**Endlo** is a simple rhythm-based game built using Python and Pygame. The objective is to press the correct keys when falling notes reach the hit line. Players earn points for successful hits and maintain their combo by timing their inputs correctly.

## 🎵 Features

- Four playable lanes with the keys **W, D, J, and K**.
- Falling notes that move toward a designated hit line.
- Score system that awards points for correctly timed hits.
- Combo system that tracks successful and missed notes.
- Randomized note positions for each lane.
- Smooth gameplay running at 60 FPS.
- Simple dark-themed interface with a blue note design.

## 🛠️ Technologies Used

- **Python 3**
- **Pygame**

## 📋 Requirements

Before running the game, make sure you have:

- Python 3.8 or later installed.
- The Pygame library installed.
- A keyboard for controlling the game.

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/endlo.git
```

Replace `your-username` with your GitHub username and update the repository name if necessary.

### 2. Navigate to the project directory

```bash
cd endlo
```

### 3. Install Pygame

```bash
pip install pygame
```

### 4. Run the game

```bash
python main.py
```

Replace `main.py` with the actual name of your Python file if it is different.

## 🎮 How to Play

1. Launch the game.
2. Watch the colored notes fall down the four lanes.
3. Press the corresponding key when a note reaches the white hit line.
4. Earn **100 points** for each correctly timed hit.
5. Try to maintain your combo by avoiding missed or mistimed inputs.
6. Close the game window to exit.

### Controls

| Key | Lane |
|---|---|
| `W` | Lane 1 |
| `D` | Lane 2 |
| `J` | Lane 3 |
| `K` | Lane 4 |

## 🏆 Scoring System

- **Successful hit:** +100 points.
- **Missed note:** Combo resets to 0.
- **Incorrectly timed key press:** Combo resets to 0.
- **Combo:** Increases by 500 for every successful hit in the current implementation.

> **Note:** The combo currently increases by 500 rather than 1. This can be changed in the source code if a traditional rhythm-game combo system is preferred.

## 📁 Project Structure

```text
Endlo/
│
├── main.py
└── README.md
```

## 🚀 Future Improvements

Possible improvements for future versions include:

- Adding background music and sound effects.
- Introducing multiple difficulty levels.
- Adding a traditional combo multiplier system.
- Displaying hit accuracy, such as Perfect, Good, and Miss.
- Adding a start menu and game-over screen.
- Increasing note speed as the score increases.
- Adding more lanes and customizable key bindings.
- Implementing a high-score system.
- Adding visual effects for successful hits.

## 📄 License

This project is open-source and available for educational and personal use. A license can be added to the repository if required.

---

**Developed with Python and Pygame.**
