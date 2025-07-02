# 🐍 PyTerminus: The Package Mage's Trial

_An interactive text adventure to teach Python module management with Poetry on
Ubuntu._

---

## 🌟 The Awakening Chamber

_You materialize in the Package Mage's training chamber, having been summoned
here through the git portal. Ancient artifacts glow on floating shelves, and the
air crackles with Python magic. Your Warp Terminal pulses with otherworldly
energy, ready to channel your commands._

> "Welcome, apprentice. You have successfully traversed the git realm and
> arrived at my sanctum. But before you can face the trials ahead, we must
> ensure your magical apparatus is properly attuned."

### 🏛️ Sanctum Verification

First, confirm you stand in the correct mystical space. Type:

```bash
pwd
```

You should see the path ends with your cloned repository name. If not, use `cd`
to navigate to the right location.

### 🐍 The Python Serpent Awakening

Call forth the Python serpent to ensure it's ready for battle. Type:

```bash
python3 --version
```

The serpent should respond with version 3.8 or newer. If the serpent doesn't
respond or is too ancient, you may need to summon system elements.

### ⚡ Ubuntu Elemental Gathering

_The Ubuntu spirits require certain elements to be present. If your Python
serpent was absent or weak, gather the elemental powers:_

Type:

```bash
sudo apt update && sudo apt install python3 curl
```

> "The elements align... Python strengthens... curl awakens... Good."

---

## 📚 The Poetry Tome Ritual

_Before you lies the most powerful artifact in the chamber - the Poetry Tome.
This ancient book contains spells for managing Python packages with elegance and
precision._

### 🔮 Tome Detection

Check if the Poetry Tome already resonates with your terminal. Type:

```bash
poetry --version
```

If the tome responds with a version number, excellent! Skip to the "Tome
Communion" step below.

### 📖 Awakening the Slumbering Tome

_If the tome remains silent, you must perform the awakening ritual:_

Type:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

_The tome installs itself, weaving its magic into your system..._

After installation, you may need to refresh your terminal's magical pathways.
Type:

```bash
source ~/.bashrc
```

Or simply close and reopen your Warp Terminal.

### 🔗 Tome Communion

Test your connection to the Poetry Tome. Type:

```bash
poetry --help
```

_The tome should reveal its secrets - a list of powerful commands at your
disposal._

### 🌌 Warp Terminal Enhancement

_Your Warp Terminal possesses an AI Oracle that can assist you with Poetry
incantations. As you progress through this adventure, try asking your terminal's
AI about Poetry commands - it can provide additional guidance and explanations._

> "Excellent, apprentice. Your chamber is prepared, the Python serpent is
> strong, and the Poetry Tome responds to your call. You are ready to face the
> trials ahead."

---

## 📜 Prologue

_You step deeper into the archive, now filled with confidence. The glowing tomes
and swirling code seem less mysterious now that you understand the power at your
fingertips._

A voice intones:

> "The language is Python. The magic, no longer misunderstood. With the Poetry
> Tome as your guide, you shall master the ancient arts of package management."

A prompt flashes before you:

```bash
python3 --version
```

_You type it confidently, knowing your serpent will respond. Your true journey
begins now._

---

## 🧪 Chapter 1: The Scroll of Import

You find a crumpled scroll on the ground. You read it:

```python
# scroll.py
import pyfiglet

print(pyfiglet.figlet_format("Magic"))
```

_Create this file in your chamber. You can use your Warp Terminal's built-in
editor or any text editor you prefer._

You try to cast the spell by typing:

```bash
python3 scroll.py
```

The archive trembles. An error bursts forth:

```
ModuleNotFoundError: No module named 'pyfiglet'
```

> "Ah," the voice sighs knowingly. "The old masters would have you
> `pip install pyfiglet` and pollute your system's magical essence. But you,
> apprentice, have the Poetry Tome. You shall learn the elegant way."

---

## ✨ Chapter 2: The Poetry Tome's Power

_Gone are the crude methods of old. You approach the altar where the Poetry Tome
awaits, its pages glowing with structured magic._

### 🏗️ Consecrating Your Workspace

First, consecrate this space as a Poetry project. Type:

```bash
poetry init
```

_The tome guides you through a ritual of questions:_

- **Package name**: Accept the default (just press Enter)
- **Version**: Accept the default (just press Enter)
- **Description**: Type something like "Learning Python package magic"
- **Author**: Enter your name
- **License**: Accept the default (just press Enter)
- **Compatible Python versions**: Accept the default (just press Enter)

When asked about dependencies, type `n` for now - you'll add them with more
precision shortly.

### 🎭 Summoning the Required Magic

Now, with surgical precision, add the pyfiglet spell to your tome. Type:

```bash
poetry add pyfiglet
```

_Watch as Poetry weaves its magic:_

- 🔮 Creates an isolated virtual realm (virtual environment)
- 📜 Records the exact spell components in `pyproject.toml`
- 🔒 Locks the precise magical formulas in `poetry.lock`
- ⚡ Installs pyfiglet and its dependencies safely

### 🌟 Casting the Perfected Spell

Now, cast your spell through the Poetry Tome's power. Type:

```bash
poetry run python scroll.py
```

_The ASCII magic unfurls in glorious display!_ 🌟

> "Behold! You have learned to summon external magic without corrupting your
> system's essence. The Poetry Tome has created a sacred space where your spells
> can flourish."

---

## 📚 Chapter 3: Understanding the Tome's Wisdom

_A glowing comparison materializes before you, showing the difference between
the old ways and the Poetry Tome's elegance:_

| Aspect              | The Old Ways (pip/venv)            | The Poetry Tome                        |
| ------------------- | ---------------------------------- | -------------------------------------- |
| **Virtual Realms**  | Manual creation (`python -m venv`) | Automatic, per project                 |
| **Spell Records**   | Crude lists (`requirements.txt`)   | Elegant lockfiles (`poetry.lock`)      |
| **Dependencies**    | Loose requirements files           | Semantic versioning (`pyproject.toml`) |
| **Spell Casting**   | Manual activation needed           | `poetry run` & `[tool.poetry.scripts]` |
| **Realm Isolation** | Easy to forget activation          | Always isolated, always safe           |

> "The old ways are a collection of tools. The Poetry Tome is a complete magical
> system, designed for mastery."

### 🔍 Exploring Your Magical Workspace

Examine what the Poetry Tome has created. Type:

```bash
ls -la
```

You'll see:

- `pyproject.toml` - _Your project's magical configuration_
- `poetry.lock` - _The exact spell formulas, locked in time_
- `scroll.py` - _Your spell scroll_

Peer into the project tome. Type:

```bash
cat pyproject.toml
```

_Notice how it records your project's essence and the pyfiglet dependency._

---

## 🗝️ Chapter 4: Mastering Your Own Magical Modules

_The final trial: creating your own magical components and combining them with
external magic._

### 📝 Creating Your Spell Component

Create a new file called `saying.py` with this content:

```python
def chant():
    return "You have mastered the ancient ways of the Poetry Tome."

def power_level():
    return "🧙‍♂️ Package Mage Level: Expert"
```

### 🔮 Enhancing Your Main Spell

Update your `scroll.py` to combine your magic with external power:

```python
import pyfiglet
from saying import chant, power_level

# External magic
print(pyfiglet.figlet_format("MASTERY"))

# Your own magic
print(chant())
print(power_level())
```

### ⚡ The Final Casting

Perform the ultimate spell. Type:

```bash
poetry run python scroll.py
```

_The chamber fills with light as both external and internal magic combine in
perfect harmony!_

---

## 🎉 The Mage's Ascension

_The voice returns, now warm with approval:_

> "You have transcended, apprentice. You understand the Poetry Tome's wisdom -
> how to create isolated magical realms, manage dependencies with precision, and
> combine your own spells with those of other mages. You are now a true Package
> Mage."

### 🔮 Your New Powers

You now know how to:

- ✨ Create Poetry projects with `poetry init`
- 📚 Add dependencies with `poetry add <package>`
- 🚀 Run spells safely with `poetry run python <file>`
- 🔒 Lock magical formulas with automatic `poetry.lock` generation
- 🏰 Maintain isolated virtual realms for each project

### 🌟 Beyond This Realm

Continue your journey by exploring:

- `poetry install` - _Recreate magical environments from `pyproject.toml`_
- `poetry shell` - _Enter the virtual realm directly_
- `poetry remove <package>` - _Banish unwanted magic_
- `poetry show` - _Reveal all active spells_

```
🎊 CONGRATULATIONS, PACKAGE MAGE! 🎊
```

_Your mastery of the Poetry Tome is now complete. Go forth and create wonders!_

---

### 🆘 Troubleshooting Incantations

_If spells fail in the Ubuntu realm:_

- **Poetry not found**: Try `source ~/.bashrc` or restart your terminal
- **Permission denied**: Never use `sudo` with Poetry commands
- **Python version issues**: Ensure Python 3.8+ with `python3 --version`
- **Warp Terminal issues**: Restart Warp or use default terminal (`Ctrl+Alt+T`)

_May your code be bug-free and your dependencies always resolve!_ 🧙‍♂️✨
