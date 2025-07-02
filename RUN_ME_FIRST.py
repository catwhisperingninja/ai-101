#!/usr/bin/env python3
import os
import sys
import time
import subprocess
import platform

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def type_text(text, delay=0.021):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def wait_for_enter():
    input("\n[Press Enter to continue...]")

def check_python_version():
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("\n⚠️  Python 3.8 or newer is required!")
        print(f"   You have: Python {version.major}.{version.minor}.{version.micro}")
        return False
    return True

def check_poetry_installed():
    try:
        result = subprocess.run(['poetry', '--version'], capture_output=True, text=True)
        return result.returncode == 0
    except FileNotFoundError:
        return False

def install_poetry():
    type_text("\n📚 The Poetry Tome is not yet in your possession...")
    type_text("   Would you like me to summon it for you?")
    
    response = input("\n[Type 'yes' to install Poetry, or 'no' to exit]: ").lower()
    
    if response == 'yes':
        type_text("\n🔮 Summoning the Poetry Tome...")
        type_text("   (This may take a moment...)\n")
        
        if platform.system() == "Windows":
            cmd = "(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -"
            subprocess.run(["powershell", "-Command", cmd])
        else:
            cmd = "curl -sSL https://install.python-poetry.org | python3 -"
            subprocess.run(cmd, shell=True)
        
        type_text("\n✨ The Poetry Tome has been summoned!")
        type_text("   Please restart your terminal and run this script again.")
        return False
    else:
        type_text("\n   Come back when you're ready to begin your journey!")
        return False

def main():
    clear_screen()
    
    print("=" * 60)
    print("🐍 PYTERMINUS: THE PACKAGE MAGE'S TRIAL 🧙‍♂️".center(60))
    print("=" * 60)
    print()
    
    type_text("Greetings, young apprentice...")
    time.sleep(1)
    type_text("\nYou stand at the threshold of magical knowledge.")
    type_text("Before you lies a journey to master the ancient art")
    type_text("of Python package management with the Poetry Tome.")
    
    wait_for_enter()
    clear_screen()
    
    # Check Python version
    print("🔍 Checking your magical apparatus...\n")
    
    if not check_python_version():
        type_text("\n❌ Your Python serpent is too ancient!")
        type_text("   Please upgrade to Python 3.8 or newer.")
        return
    
    type_text(f"✅ Python {sys.version.split()[0]} - The serpent is strong!")
    
    # Check Poetry
    if not check_poetry_installed():
        if not install_poetry():
            return
    else:
        type_text("✅ Poetry is installed - The tome responds to your call!")
    
    wait_for_enter()
    clear_screen()
    
    # Story begins
    type_text("\n📖 YOUR JOURNEY BEGINS...\n")
    type_text("You find yourself in a mystical chamber filled with")
    type_text("floating scrolls and glowing runes. The air crackles")
    type_text("with Python magic.\n")
    
    type_text("A weathered scroll lies on the ground before you.")
    type_text("It appears to contain a spell...\n")
    
    wait_for_enter()
    
    # Create the scroll.py file
    type_text("\n📜 Creating the ancient scroll...\n")
    
    with open('simple_scroll.py', 'w') as f:
        f.write("""# A mysterious scroll with an incomplete spell
import pyfiglet

print(pyfiglet.figlet_format("Magic"))
""")
    
    type_text("✅ Created: simple_scroll.py")
    type_text("\nThe scroll contains a spell, but something is missing...")
    
    wait_for_enter()
    
    # Try to run it (will fail)
    type_text("\n🎯 Let's try casting this spell the RIGHT way...")
    type_text("Type 'poetry run python simple_scroll.py' to run the script.")
    type_text("(Always use 'poetry run' for proper environment isolation)")
    
    while True:
        user_cmd = input("\n$ ").strip()
        if user_cmd == "poetry run python simple_scroll.py":
            result = subprocess.run(['poetry', 'run', 'python', 'simple_scroll.py'], capture_output=True, text=True)
            break
        else:
            type_text("\nAh, the command typo curse strikes again!")
            type_text("Type exactly: poetry run python simple_scroll.py")
    
    if result.returncode != 0:
        type_text("💥 The spell fails!\n")
        type_text("❌ ModuleNotFoundError: No module named 'pyfiglet'")
        type_text("\nThe scroll requires magical components you don't possess!")
    else:
        type_text("✨ The spell works! (You must have pyfiglet already installed)")
    
    wait_for_enter()
    clear_screen()
    
    # Teach about Poetry
    type_text("\n🧙‍♂️ A wise mage appears...\n")
    type_text('"Ah, I see you\'ve discovered the limitation of raw Python."')
    type_text('"To cast spells that use external magic, you need the Poetry Tome!"')
    type_text('"Let me teach you the proper way..."\n')
    
    wait_for_enter()
    
    # Initialize Poetry project
    type_text("\n📚 First, we consecrate this space as a Poetry project:\n")
    
    if not os.path.exists('pyproject.toml'):
        type_text("Type 'poetry init --no-interaction' to create a project quickly.")
        type_text("(The --no-interaction flag uses default settings)")
        
        while True:
            user_cmd = input("\n$ ").strip()
            if user_cmd == "poetry init --no-interaction":
                subprocess.run(['poetry', 'init', '--no-interaction'])
                type_text("\n✅ Poetry project initialized!")
                break
            else:
                type_text("\nExact precision needed for the spell!")
                type_text("Type: poetry init --no-interaction")
    else:
        type_text("✅ Poetry project already exists!")
    
    wait_for_enter()
    
    # Add pyfiglet
    type_text("\n🔮 Now, let's add the magical component (pyfiglet):")
    type_text("Type 'poetry add pyfiglet' to install your first package.")
    type_text("(This is how Poetry manages external libraries)")
    
    while True:
        user_cmd = input("\n$ ").strip()
        if user_cmd == "poetry add pyfiglet":
            subprocess.run(['poetry', 'add', 'pyfiglet'])
            break
        else:
            type_text("\nThe spell requires precision!")
            type_text("Type exactly: poetry add pyfiglet")
    
    type_text("\n✅ The pyfiglet magic has been added to your tome!")
    
    wait_for_enter()
    
    # Run with Poetry
    type_text("\n✨ Now, let's cast the spell properly with Poetry:")
    type_text("Type 'poetry run python simple_scroll.py' to run in Poetry's realm.")
    type_text("(The 'poetry run' prefix uses Poetry's isolated environment)")
    
    while True:
        user_cmd = input("\n$ ").strip()
        if user_cmd == "poetry run python simple_scroll.py":
            subprocess.run(['poetry', 'run', 'python', 'simple_scroll.py'])
            break
        else:
            type_text("\nPoetry requires the exact incantation!")
            type_text("Type: poetry run python simple_scroll.py")
    
    type_text("\n🎉 SUCCESS! The spell works perfectly!")
    
    wait_for_enter()
    clear_screen()
    
    # Conclusion
    type_text("\n🏆 CONGRATULATIONS, APPRENTICE!\n")
    type_text("You have learned the first lesson of the Poetry Tome:")
    type_text("- ✅ How to initialize a Poetry project")
    type_text("- ✅ How to add magical components (packages)")
    type_text("- ✅ How to cast spells in an isolated realm")
    type_text("- ⚠️  ALWAYS use 'poetry run python' - never just 'python'!\n")
    
    type_text("📖 Your journey continues in the full tutorial!")
    type_text("   Read: PyTerminus_PackageMage_Adventure.md\n")
    
    type_text("🎮 Want to begin the full adventure?")
    response = input("   Type 'yes' to start the complete journey: ").lower()
    
    if response == 'yes':
        type_text("\n🌟 Launching the Package Mage's Adventure...\n")
        time.sleep(1)
        subprocess.run(['poetry', 'run', 'python', 'scroll.py'])
    
    type_text("\n🧙‍♂️ May your code be bug-free and your dependencies always resolve!")
    type_text("   Happy coding, Package Mage!\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Farewell, apprentice! Come back when you're ready...")
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")
        print("   Please check your environment and try again.")