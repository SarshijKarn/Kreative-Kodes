# Graphics — Kreative Kodes

A small gallery of creative code experiments: Python Turtle graphics, animated hearts, and a Ganesha drawing with ambient music. This repo is organized into focused mini-projects and simple HTML demos.


## Contents

- Ganesha (Python Turtle + background music)
  - Python script: `Ganesha/JaiGanesha.py`
  - Assets: `Ganesha/assets/ganesha.mp3`, `Ganesha/assets/ganesha.png`
  - HTML demos: `Ganesha/Html Version/ganesha1.html`, `ganesha2.html`
- Heart (two variations)
  - `Heart/mysthic_dil.py` — fast parametric heart rendered with dots
  - `Heart/mysthic_dil2.py` — animated, glowing heart + typewriter text


## Requirements

- Python 3.8+ (Turtle comes with the standard library; requires Tk support)
- Pygame (for audio in the Ganesha sketch):
  - Install via: `pip install pygame`
- A desktop OS capable of showing Turtle graphics windows (Windows/macOS/Linux)


## Quick Start

Clone or download the repository, then run any of the sketches from their own folders.

### 1) Ganesha (with music)

Important: Run the script from inside the `Ganesha` folder so the relative `assets/` path resolves correctly.

```
cd Ganesha
pip install pygame
python JaiGanesha.py
```

- The background music (`assets/ganesha.mp3`) will loop automatically if the file is present.
- A Turtle graphics window will draw the Ganesha outline and title text.

### 2) Heart (parametric/dots)

```
cd Heart
python mysthic_dil.py
```

- Renders a heart using a parametric curve and dot plotting.

### 3) Heart (animated + typewriter text)

```
cd Heart
python mysthic_dil2.py
```

- Draws an outline, fills the heart with a pulsing effect, and types mood text with a soft glow.

### 4) HTML Demos (no Python needed)

Open directly in your browser:
- `Ganesha/Html Version/ganesha1.html`
- `Ganesha/Html Version/ganesha2.html`


## Project Structure

```
Graphics/
├─ Ganesha/
│  ├─ JaiGanesha.py
│  ├─ assets/
│  │  ├─ ganesha.mp3
│  │  └─ ganesha.png
│  └─ Html Version/
│     ├─ ganesha1.html
│     └─ ganesha2.html
├─ Heart/
│  ├─ mysthic_dil.py
│  └─ mysthic_dil2.py
└─ README
```


## Troubleshooting

- ModuleNotFoundError: No module named 'pygame'
  - Run: `pip install pygame` (consider `python -m pip install pygame` to use the right interpreter)
- No sound in Ganesha
  - Ensure `Ganesha/assets/ganesha.mp3` exists and you launched from the `Ganesha` folder
  - Verify your system volume and audio output
- Turtle window not showing / blank
  - Make sure Python has Tkinter support; try updating Python if needed


## Credit

Crafted by: Sarshij Karn (GitHub: @SarshijKarn)
- https://github.com/SarshijKarn

Please attribute the work if you share or remix.


## Roadmap

More graphics, generative art, and similar kreative-kodes will be uploaded here. Stay tuned for new sketches, animations, and visual experiments.


## Contributing

Issues and small suggestions are welcome. If you have an idea for a new sketch or optimization, feel free to open an issue or a pull request.
