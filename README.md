# Naruto D&D Game Master (Terminal-Based AI RPG Engine)

**A local, terminal-based solo RPG system that brings the Naruto universe to life using D&D 5e mechanics and AI-powered scene narration.**

---

## 🌌 Project Overview

**Naruto D&D Game Master** is a modular Python application designed to simulate a solo tabletop RPG experience set in the Naruto universe. Built around D&D 5e mechanics, the game includes character creation, jutsu usage, experience-based progression, and tactical choices — all enriched with dynamic, AI-generated storytelling.

> This is not just a game — it's a narrative engine where your choices matter, and your journey is guided by a cinematic Game Master powered by local LLMs (such as Mistral via Ollama).

---

## 🎮 Key Features

- 🧬 **Character System** – Build unique shinobi characters with clan, element, stats, CP, EXP, and leveling mechanics.
- 🔥 **Jutsu Mechanics** – Use, learn, and evolve jutsus based on CP consumption and experience.
- 🗺️ **Mission Engine** – Accept tasks from a JSON-based mission pool or dynamically generated by AI.
- 🧠 **AI-Driven Scene Narration** – Generate immersive environmental descriptions using local language models.
- 🧩 **Choice & Consequence** – Every decision affects the world around your character.
- 🛏️ **Rest & Recovery** – Short/Long rests regenerate CP and HP in accordance with 5e rules.
- 🎭 **NPC Dialogue (Coming Soon)** – Natural language interaction with in-world characters.
- 🧠 **Memory-Aware Game Master (Planned)** – Context-aware AI that remembers your past.

---

## 🛠️ Tech Stack

- **Language**: Python 3.13+
- **Interface**: Terminal (CLI)
- **Local AI Models**: [Ollama](https://ollama.com) with Mistral, LLaMA, or other GGUF-compatible models
- **Structure**: Fully modular, Clean Code architecture

```

📁 Directory Structure
├── src/
│   ├── application/      # CLI interaction
│   ├── domain/           # Core RPG logic
│   ├── infrastructure/   # File/IO & data access
│   ├── presentation/     # Text presentation
│   ├── data/             # Static JSON data (jutsu, missions, scenes)
│   └── ai/               # AI prompt generation (LLM scene engine)

````

---

## 🚀 Getting Started

### Prerequisites

- Python 3.13+
- [Ollama](https://ollama.com/) installed locally
- Compatible local LLM (e.g., `mistral`, `llama2`, etc.)

### Installation

```bash
git clone https://github.com/yagizsahinler/dnd-naruto-gm.git
cd dnd-naruto-gm
python -m venv venv
source venv/bin/activate   # or `venv\Scripts\activate` on Windows
pip install -r requirements.txt
````

### Run the Game

```bash
python src/app/main.py
```

---

## 🧠 AI Capabilities (WIP)

| Feature              | Status     | Description                                                |
| -------------------- | ---------- | ---------------------------------------------------------- |
| Scene Narration      | ✅ Complete | Uses local LLM to describe immersive environments          |
| NPC Dialogue         | 🔜 Planned | Interact naturally with in-game characters                 |
| Mission Generator    | 🔜 Planned | AI-tailored mission generation per character history       |
| Story Memory Engine  | 🔜 Planned | AI that tracks past choices and reflects them in narration |
| Dynamic World Events | 🔜 Future  | AI-modulated world changes based on actions                |

---

## 🧪 Sample Character

```
Name: Uchiha Ren
Rank: Genin
Element: Fire
CP: 14 / HP: 20 / EXP: 0 / Level: 1
Jutsus:
- Katon: Hōsenka (1D8 + INT, 4 CP)
- Substitution Jutsu (3 CP)
- Bunshin no Jutsu (2 CP)
```

---

## 🧱 Design Principles

* ✅ Clean Code (modularized, testable)
* 📦 Data-Driven (JSON-based missions, jutsus, scenes)
* 🎨 Cinematic Presentation (anime-style storytelling)
* 🔒 Lore Faithfulness (100% Naruto canon compatibility)

---

## 📚 Contribution & Future Vision

This is an open-source, non-commercial project inspired by the love for RPGs and Naruto. Contributions are welcome — from system enhancements to new missions and AI prompt designs.

> Future plans include: GUI version, multiplayer co-op, visual storytelling modules, and real-time AI interactions.

---

## 📄 License

MIT License © 2025 Yagiz Sahinler
This project is intended for educational and entertainment use only. Naruto is © by Masashi Kishimoto and Shueisha.
