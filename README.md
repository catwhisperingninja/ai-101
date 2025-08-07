# This Is Not Learning to Code. This Is Learning Core Tool Functions To Interact With An AI Coding For You.

People see "Python" and a Git repo and assume that because they have no interest in coding, spending a few hours learning core basics is not worth their time. Any 5th-grader can handle basic Git and package management.




# PyTerminus: The Package Mage's Trial

A fun interactive text adventure to teach Python module management with Poetry
on Ubuntu, written by the illustrious ChatGPT 4o.

# Modules and Package Management

You can think of a "module" as something similar to a web browser extension, or
Adobe Photoshop plug-in. They are little "packages" of code that do specific
things, like look up URLs, or do
[cool astrophysics stuff](https://www.astropy.org/).

Modules are essential. A Python application will not run without all modules
that the app requires. It's normal for these to number in the hundreds or
thousands. This is why "package managers" exist, although Poetry also creates a
smooth virtual environment experience as well as handling packages. We don't
need to worry about the why and how of virtual environments right this second.

All programming languages have their own specific package managers, usually
around 2 that are commonly used.

## Poetry vs. pip

Python uses another common package manager called "`pip`". It performs the same
function as Poetry, but it's best to not interchange them, as things get
confusing fast. You will commonly see documentation telling to `pip install`
something. You can simply swap that to:

`poetry add` <something>

Then: `poetry lock && poetry install`.

All done.

## Quick Start

**For absolute beginners:**

```bash
python3 RUN_ME_FIRST.py
```

This interactive script will:

- Check your Python version
- Help you install Poetry if needed
- Guide you through your first Poetry project
- Teach you package management basics

## Manual Setup

If you prefer to set up manually:

1. Make sure you have Python 3.8+ installed
2. Install Poetry: `curl -sSL https://install.python-poetry.org | python3 -`
3. Install dependencies: `poetry install`
4. Run the example: `poetry run python scroll.py`

## What's Included

- `RUN_ME_FIRST.py` - Interactive setup script for absolute beginners
- `scroll.py` - Entry point to the full interactive adventure
- `adventure.py` - The complete interactive Package Mage's trial
- `PyTerminus_PackageMage_Adventure.md` - Full tutorial documentation
- `simple_scroll.py` - Example script created during the tutorial
- `saying.py` - Custom module demonstrating local imports

## About

This tutorial teaches beginners:

- How to use Poetry for Python package management
- Creating virtual environments automatically
- Managing dependencies with `pyproject.toml`
- Running Python scripts in isolated environments
- Combining external packages with custom modules

Follow the adventure in `PyTerminus_PackageMage_Adventure.md` to learn Poetry
step by step!
