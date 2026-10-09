# Space Defender

A 2D arcade space shooter written in **Python** with **Pygame**. You move a ship around the screen, shoot the enemies that fall from the top, and try not to get hit. Each enemy destroyed adds points, and each collision costs a life.

Space Defender was developed as a course project.

The project is organised as a small game package (`game/`) with one module per game object, plus a `main.py` that runs the game loop.

## Gameplay

| Action | Control |
|---|---|
| Move | Arrow keys (← → ↑ ↓) |
| Shoot | Space |
| Quit | Close the window |

- A new enemy spawns at a random horizontal position every 60 frames (about once per second at 60 FPS) and falls straight down.
- A bullet that hits an enemy destroys both and adds **10 points**.
- An enemy that touches the player is removed and costs **1 life**. The player starts with 3 lives, and the game closes when they reach 0.
- Enemies and bullets that leave the screen are removed automatically.
- The current score and lives are drawn in the top-left corner (HUD).

## Technologies

| Technology | Use |
|---|---|
| Python 3.10+ | Language. The code uses `X \| None` type hints, which need Python 3.10 or newer. |
| [Pygame](https://pypi.org/project/pygame/) | Window, rendering, keyboard input, timing and collision rectangles |
| `random` (standard library) | Random enemy spawn positions |

## How It Works

### Game loop (`main.py`)

`run()` creates an 800 × 600 window and runs a classic game loop that repeats 60 times per second:

1. **Spawn:** a frame counter adds a new `Enemy` every 60 frames.
2. **Input:** held arrow keys move the player (`player.handle_input`). A `KEYDOWN` event for Space creates a `Bullet` at the top of the ship.
3. **Update:** every object updates its position, and objects that left the screen are filtered out of their lists.
4. **Collisions:** `pygame.Rect.colliderect` checks bullet ↔ enemy and enemy ↔ player collisions. The loops iterate over copies of the lists (`bullets[:]`) so items can be removed safely while looping.
5. **Draw:** the background is cleared, then the player, bullets, enemies and HUD are drawn.
6. **Display:** `pygame.display.flip()` shows the finished frame (double buffering), and `clock.tick(FPS)` caps the frame rate.

### Game objects (`game/`)

Every object follows the same pattern: an image, a `pygame.Rect` for position and collisions, an `update()` method and a `draw()` method.

| Module | Responsibility |
|---|---|
| `player.py` | `Player`: starts at the bottom centre and moves in four directions. `clamp_ip` keeps the ship inside the screen. |
| `bullet.py` | `Bullet`: moves upwards. `off_screen` property for clean-up. |
| `enemy.py` | `Enemy`: spawns above the screen at a random x position and moves downwards. |
| `hud.py` | `HUD`: draws score and lives. It also has `draw_centered_text()`, ready for future start or game-over screens. |
| `assets.py` | Loading helpers for images, sounds and fonts (see below) |
| `settings.py` | Global constants: window size, FPS, speeds and background colour |

### Fault-tolerant asset loading

`assets.py` builds paths relative to the project root and **never crashes when a file is missing**:

- `load_image()` returns a **magenta placeholder rectangle** of the right size if a sprite cannot be found.
- `load_sound()` returns `None` if a sound file is missing.
- `get_font()` falls back to Pygame's default font.

The `assets/` folder is listed in `.gitignore`, so it is not part of this repository. A fresh clone therefore runs with magenta rectangles instead of sprites. To use real graphics, add these files:

```text
assets/
└── sprites/
    ├── player.png
    ├── enemy.png
    └── bullet.png
```

## Project Structure

```text
Space_defender/
├── main.py          # Entry point and game loop
└── game/
    ├── __init__.py
    ├── settings.py  # Constants (screen size, FPS, speeds, colours)
    ├── assets.py    # Image/sound/font loading with fallbacks
    ├── player.py    # Player ship
    ├── bullet.py    # Bullets
    ├── enemy.py     # Falling enemies
    ├── hud.py       # Score and lives display
    └── scenes.py    # Empty, reserved for future scenes
```

## Getting Started

### Requirements

- Python 3.10 or newer
- Pygame

### Installation

```bash
git clone https://github.com/beatrizestfr/Space_defender.git
cd Space_defender
python -m venv .venv
```

Activate the virtual environment. On Windows:

```bash
.venv\Scripts\activate
```

On macOS or Linux:

```bash
source .venv/bin/activate
```

Then install Pygame:

```bash
pip install pygame
```

If `pygame` has no pre-built package for your Python version (for example on very recent Python releases), install the compatible community edition instead. It is imported with the same `import pygame`:

```bash
pip install pygame-ce
```

### Run

```bash
python main.py
```

The game starts immediately. There is no start menu yet.

## What This Project Demonstrates

- Structuring a game as a Python package with one class per game object
- The update/draw game loop pattern, frame-rate control and double buffering
- Keyboard input handling with both held keys and key events
- Rectangle-based collision detection and safe removal from lists while iterating
- Defensive resource loading with fallbacks instead of crashes
- Separating configuration (`settings.py`) from logic

## Roadmap

These features are planned in the notes at the top of `main.py` and are **not implemented yet**:

- [ ] Increase the speed as time passes
- [ ] Lose a life when a number of enemies get past a certain point (a "base" to defend)
- [ ] Sound effects (`load_sound()` is already prepared)
- [ ] Start and game-over screens (`HUD.draw_centered_text()` and `scenes.py` are already prepared)
- [ ] Levels

## Project Status

In development. The core gameplay works: movement, shooting, enemies, collisions, score and lives. Note: the score currently starts at `123` instead of `0` (a leftover test value in `main.py`).
