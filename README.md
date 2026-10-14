# Dino Runner Game

A small Dino Runner-style game built with Python and Raylib. This is a learning project focused on practicing game loops, keyboard input, movement, textures, audio, and collision detection.

## Features

- Dino running animation using two sprite images
- Jumping with the **Space** key
- Moving cactus obstacles
- Scrolling cloud-position logic (cloud drawing is currently commented out)
- Background music and a jump sound asset
- Score counter
- Rectangle-based collision detection

> This project is a work in progress. Some gameplay logic and visual elements may still need tuning.

## Tech Stack

- **Python**
- **Raylib** through the `raylib` / `pyray` Python bindings

## Project Structure

```text
dino_start_project/
├── code/
│   └── flappy_bird.py
├── assets/
│   ├── cactii/       # Cactus sprites
│   ├── clouds/       # Cloud sprites
│   ├── dino/         # Dino running and jumping sprites
│   ├── enemy/        # Enemy sprites
│   └── floor/        # Floor sprites
├── audio/
│   ├── jump.wav
│   └── music.mp3
├── fonts/
│   └── RETRO_SPACE.ttf
├── credits.txt
└── README.md
```

## Requirements

- Python 3
- The Python Raylib bindings

Install the dependency:

```bash
python3 -m pip install raylib
```

## How to Run

1. Download or clone this project.
2. Open a terminal and move into the project root — the folder containing `assets/`, `audio/`, and `code/`.
3. Run:

   ```bash
   python3 code/flappy_bird.py
   ```

Run the command from the project root because the game loads images and audio using relative paths.

## Controls

| Key | Action |
| --- | --- |
| `Space` | Jump |
| `A` | Exit the game (the current code also attempts to play the jump sound on this key) |
| Window close button | Close the game |

## Current Notes

- The game window is set to **1280 × 720** and targets **40 FPS**.
- Cactus obstacles move from right to left and are repositioned after leaving the screen.
- The score increases over time and decreases when a collision is detected.
- Cloud sprites are loaded, but their drawing calls are currently commented out.
- The current collision rectangles use the dino and cactus sprite dimensions directly, so collision behavior may need adjustment as the game develops.

## Possible Next Improvements

- Add a game-over screen and restart option.
- Improve collision handling so a collision ends the run only once.
- Add the cloud and floor sprites to the scene.
- Unload textures, sounds, and music before closing.
- Separate game state, updates, and drawing into functions for easier maintenance.

## Credits

See [`credits.txt`](credits.txt) for asset credits and attribution.
