#!/usr/bin/env python3
import os
import sys
import time
import subprocess
import shutil

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def type_text(text, delay=0.021):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def wait_for_enter():
    input("\n[Press Enter to continue...]")

def get_command_with_validation(expected_cmd, hint="", error_msg="Ah, yes, the curse of the command typo. Bane of apprentices everywhere! You likely typed incorrectly. Please try again."):
    """Get user input and validate against expected command"""
    while True:
        if hint:
            print(f"\n💡 Hint: {hint}")
        user_input = input("\n$ ").strip()
        
        if user_input == expected_cmd:
            # Execute the actual command
            result = subprocess.run(user_input, shell=True, capture_output=True, text=True)
            if result.stdout:
                print(result.stdout.strip())
            if result.stderr:
                print(result.stderr.strip())
            return result
        else:
            type_text(f"\n{error_msg}")
            if user_input:
                type_text(f"You typed: '{user_input}'")
                type_text(f"Expected: '{expected_cmd}'")

def chapter_separator(title):
    clear_screen()
    print("=" * 60)
    print(f"✨ {title} ✨".center(60))
    print("=" * 60)
    print()

def main():
    clear_screen()
    
    # Title Screen
    print("🐍" + "=" * 56 + "🐍")
    print("PYTERMINUS: THE PACKAGE MAGE'S TRIAL".center(60))
    print("An Interactive Python Adventure".center(60))
    print("🧙‍♂️" + "=" * 56 + "🧙‍♂️")
    print()
    
    type_text("Welcome back to the Package Mage's sanctum...")
    type_text("Your journey into the depths of Python magic continues.")
    type_text("\n⚡ IMPORTANT: You will type commands yourself to build mastery!")
    
    wait_for_enter()
    
    # Chapter 1: The Awakening Chamber
    chapter_separator("Chapter 1: The Awakening Chamber")
    
    type_text("You materialize in the Package Mage's training chamber.")
    type_text("Ancient artifacts glow on floating shelves, and the")
    type_text("air crackles with Python magic.\n")
    
    type_text("> \"Welcome, apprentice. Before the trials ahead,")
    type_text("> we must ensure your magical apparatus is properly attuned.\"\n")
    
    wait_for_enter()
    
    # Sanctum Verification
    type_text("🏛️ SANCTUM VERIFICATION")
    type_text("First, confirm you stand in the correct mystical space.")
    type_text("Type 'pwd' (without quotations) to Print Working Directory.")
    type_text("This shows where you are on the computer system.")
    
    get_command_with_validation("pwd", 
        hint="pwd stands for 'print working directory'",
        error_msg="The magic falters! Remember, type exactly 'pwd' to see your location.")
    
    type_text("\n> \"Good. You have located yourself in the digital realm.\"")
    
    wait_for_enter()
    
    # Python Check
    type_text("\n🐍 THE PYTHON SERPENT AWAKENING")
    type_text("Call forth the Python serpent to ensure it's ready.")
    type_text("Type 'python3 --version' to check which Python serpent answers.")
    type_text("The --version flag asks Python to reveal its identity.")
    
    result = get_command_with_validation("python3 --version",
        hint="Use python3 with two dashes before version",
        error_msg="The serpent does not respond to that incantation! Remember the exact spell: 'python3 --version'")
    
    type_text("\n> \"Excellent! The serpent responds with its version.\"")
    type_text("> \"Version 3.8 or higher shows a strong serpent.\"")
    
    wait_for_enter()
    
    # Poetry Check
    type_text("\n📚 THE POETRY TOME RITUAL")
    type_text("Check if the Poetry Tome resonates with your terminal.")
    type_text("Type 'poetry --version' to detect the tome's presence.")
    type_text("Poetry is our magical package manager.")
    
    result = get_command_with_validation("poetry --version",
        hint="Similar to python3, use poetry with --version",
        error_msg="The tome remains silent to that call! Type exactly 'poetry --version'")
    
    if result.returncode == 0:
        type_text("\n> \"Excellent! The Poetry Tome is already bound to you.\"")
    else:
        type_text("\n> \"The tome is silent... You must awaken it!\"")
        type_text("Run this in your terminal to install Poetry:")
        print("\ncurl -sSL https://install.python-poetry.org | python3 -\n")
        type_text("Then return to continue your journey.")
        return
    
    wait_for_enter()
    
    # Test Poetry help
    type_text("\n🔮 TESTING YOUR CONNECTION TO THE TOME")
    type_text("Let's ensure the tome truly hears you.")
    type_text("Type 'poetry --help' to see the tome's available spells.")
    type_text("The --help flag reveals all commands you can use.")
    
    get_command_with_validation("poetry --help",
        hint="Replace --version with --help",
        error_msg="The tome's secrets remain hidden! Use 'poetry --help' exactly.")
    
    type_text("\n> \"Marvelous! The tome reveals its commands.\"")
    type_text("> \"You are ready for the trials ahead.\"")
    
    wait_for_enter()
    
    # Chapter 2: The Scroll of Import
    chapter_separator("Chapter 2: The Scroll of Import")
    
    type_text("You find a crumpled scroll on the ground.")
    type_text("Let me show you its contents...\n")
    
    # Show the simple scroll
    print("```python")
    print("# simple_scroll.py")
    print("import pyfiglet")
    print("")
    print('print(pyfiglet.figlet_format("Magic"))')
    print("```")
    
    # Create the file if it doesn't exist
    if not os.path.exists("simple_scroll.py"):
        with open("simple_scroll.py", "w") as f:
            f.write("""# simple_scroll.py
import pyfiglet

print(pyfiglet.figlet_format("Magic"))
""")
        type_text("\n✨ The scroll materializes as 'simple_scroll.py'")
    else:
        type_text("\nThis scroll exists as 'simple_scroll.py'")
    
    type_text("\nLet's try to cast this spell properly with Poetry.")
    type_text("Type 'poetry run python simple_scroll.py' to run the script.")
    type_text("Always use 'poetry run' to ensure proper isolation.")
    
    result = get_command_with_validation("poetry run python simple_scroll.py",
        hint="poetry run python followed by the filename",
        error_msg="The spell misfires! Remember: 'poetry run python simple_scroll.py'")
    
    if result.returncode != 0:
        type_text("\n💥 The archive trembles. An error bursts forth!")
        type_text("ModuleNotFoundError: No module named 'pyfiglet'\n")
        type_text("> \"Ah, the spell requires components you lack.\"")
        type_text("> \"But fear not - the Poetry Tome shall provide!\"")
    else:
        type_text("\n✨ Wait... the spell works? You must already have pyfiglet!")
        type_text("> \"Interesting... but let's ensure it's properly managed.\"")
    
    wait_for_enter()
    
    # Chapter 3: The Poetry Tome's Power
    chapter_separator("Chapter 3: The Poetry Tome's Power")
    
    type_text("Gone are the crude methods of old.")
    type_text("You approach the altar where the Poetry Tome awaits.\n")
    
    # Check if project already initialized
    if not os.path.exists("pyproject.toml"):
        type_text("🏗️ CONSECRATING YOUR WORKSPACE")
        type_text("First, we must consecrate this space as a Poetry project.")
        type_text("Type 'poetry init' to begin the ritual.")
        type_text("(You can press Enter to accept defaults for most questions)")
        
        get_command_with_validation("poetry init",
            hint="Just 'poetry init' with no extra flags",
            error_msg="The consecration fails! Type exactly 'poetry init'")
    else:
        type_text("✅ This space is already consecrated as a Poetry project!")
        type_text("Let's verify by examining the tome.")
        type_text("Type 'ls' to list files in this directory.")
        
        get_command_with_validation("ls",
            hint="The list command is just two letters",
            error_msg="To see files, type exactly 'ls'")
        
        type_text("\n> \"See the pyproject.toml? That's your project's essence.\"")
    
    wait_for_enter()
    
    # Add pyfiglet
    type_text("\n🎭 SUMMONING THE REQUIRED MAGIC")
    type_text("Now, with surgical precision, add the pyfiglet spell.")
    type_text("Type 'poetry add pyfiglet' to add this package to your project.")
    type_text("This is Poetry's way of installing external magic.")
    
    result = get_command_with_validation("poetry add pyfiglet",
        hint="poetry add followed by the package name",
        error_msg="The summoning fails! Use 'poetry add pyfiglet' precisely.")
    
    type_text("\n✨ Watch what Poetry just did:")
    type_text("  🔮 Created an isolated virtual environment")
    type_text("  📜 Added pyfiglet to pyproject.toml")
    type_text("  🔒 Locked exact versions in poetry.lock")
    type_text("  ⚡ Installed pyfiglet in the virtual realm")
    
    wait_for_enter()
    
    # Cast the spell with Poetry
    type_text("\n🌟 CASTING THE SPELL AGAIN")
    type_text("Now that pyfiglet is installed, let's cast the spell again.")
    type_text("Type 'poetry run python simple_scroll.py' - same command as before.")
    type_text("Notice how Poetry manages everything seamlessly!")
    
    get_command_with_validation("poetry run python simple_scroll.py",
        hint="Same command as before - poetry run python simple_scroll.py",
        error_msg="Remember to always use Poetry! Type 'poetry run python simple_scroll.py'")
    
    type_text("\n> \"Perfect! Now the spell works flawlessly.\"")
    type_text("> \"You've learned the cardinal rule: ALWAYS use 'poetry run'\"")
    type_text("> \"This ensures you're using the project's environment.\"")
    
    wait_for_enter()
    
    # Chapter 4: Understanding the Tome
    chapter_separator("Chapter 4: Understanding the Tome's Wisdom")
    
    type_text("Let's explore what Poetry has created.")
    type_text("Type 'cat pyproject.toml' to read your project configuration.")
    type_text("The 'cat' command displays file contents.")
    
    get_command_with_validation("cat pyproject.toml",
        hint="cat followed by the filename",
        error_msg="To read the tome, type 'cat pyproject.toml'")
    
    type_text("\n> \"This file declares your project's identity and needs.\"")
    
    wait_for_enter()
    
    type_text("\nNow examine the lock file.")
    type_text("Type 'head -20 poetry.lock' to see the first 20 lines.")
    type_text("The 'head' command shows the beginning of a file.")
    
    get_command_with_validation("head -20 poetry.lock",
        hint="head -20 followed by filename",
        error_msg="To peek at the lock file, type 'head -20 poetry.lock'")
    
    type_text("\n> \"This lock file ensures everyone gets identical packages.\"")
    type_text("> \"It's Poetry's way of preventing version conflicts.\"")
    
    wait_for_enter()
    
    # Chapter 5: Creating Your Own Magic
    chapter_separator("Chapter 5: Mastering Your Own Magical Modules")
    
    type_text("The final trial: creating your own magical components")
    type_text("and combining them with external magic.\n")
    
    # Show saying.py content
    type_text("📝 You need to create a module called 'saying.py'")
    type_text("Here's what it should contain:\n")
    
    print("```python")
    print("def chant():")
    print('    return "You have mastered the ancient ways of the Poetry Tome."')
    print("")
    print("def power_level():")
    print('    return "🧙‍♂️ Package Mage Level: Expert"')
    print("```")
    
    # Create saying.py if needed
    if not os.path.exists("saying.py"):
        type_text("\n✨ Let me create this for you...")
        with open("saying.py", "w") as f:
            f.write('''def chant():
    return "You have mastered the ancient ways of the Poetry Tome."

def power_level():
    return "🧙‍♂️ Package Mage Level: Expert"
''')
        type_text("✅ Created: saying.py")
    else:
        type_text("\n✅ The module 'saying.py' already exists!")
    
    wait_for_enter()
    
    # Show enhanced scroll
    type_text("\n🔮 Now we'll create an enhanced spell that combines magics.")
    type_text("Here's the enhanced scroll.py:\n")
    
    print("```python")
    print("import pyfiglet")
    print("from saying import chant, power_level")
    print("")
    print("# External magic")
    print('print(pyfiglet.figlet_format("MASTERY"))')
    print("")
    print("# Your own magic")
    print("print(chant())")
    print("print(power_level())")
    print("```")
    
    # Create scroll.py
    if not os.path.exists("scroll.py") or True:  # Always recreate for the adventure
        with open("scroll.py", "w") as f:
            f.write('''import pyfiglet
from saying import chant, power_level

# External magic
print(pyfiglet.figlet_format("MASTERY"))

# Your own magic
print(chant())
print(power_level())
''')
        type_text("\n✅ Created: scroll.py")
    
    wait_for_enter()
    
    # Final casting
    type_text("\n⚡ THE FINAL CASTING")
    type_text("Perform the ultimate spell!")
    type_text("Type 'poetry run python scroll.py' to combine all magics.")
    
    get_command_with_validation("poetry run python scroll.py",
        hint="Same pattern: poetry run python filename",
        error_msg="The final spell requires precision! Type 'poetry run python scroll.py'")
    
    type_text("\n✨ The chamber fills with light as both external")
    type_text("and internal magic combine in perfect harmony!")
    
    wait_for_enter()
    
    # Test Poetry show
    type_text("\n🔍 REVEALING YOUR MAGICAL ARSENAL")
    type_text("Let's see all the packages in your virtual realm.")
    type_text("Type 'poetry show' to list all installed packages.")
    
    get_command_with_validation("poetry show",
        hint="Just poetry and show",
        error_msg="To reveal your spells, type 'poetry show'")
    
    type_text("\n> \"See how Poetry tracks every magical component!\"")
    
    wait_for_enter()
    
    # The Ascension
    chapter_separator("The Mage's Ascension")
    
    type_text("🎉 CONGRATULATIONS, APPRENTICE!\n")
    type_text("> \"You have transcended. You understand the Poetry Tome's")
    type_text("> wisdom and can now combine magics with precision.\"\n")
    
    type_text("🔮 SPELLS YOU'VE MASTERED:")
    type_text("  ✅ poetry init - Consecrate a new project")
    type_text("  ✅ poetry add <package> - Summon external magic")
    type_text("  ✅ poetry run python <file> - Cast spells safely (ALWAYS USE THIS!)")
    type_text("  ✅ poetry show - Reveal installed packages")
    type_text("  ✅ cat/head commands - Read magical texts\n")
    
    type_text("⚠️  REMEMBER THE GOLDEN RULE:")
    type_text("   ALWAYS use 'poetry run python' - never just 'python'")
    type_text("   This ensures you're using the correct environment!\n")
    
    type_text("🌟 CONTINUE YOUR JOURNEY WITH:")
    type_text("  • poetry install - Recreate environment from lock file")
    type_text("  • poetry shell - Enter the virtual realm directly")
    type_text("  • poetry remove <package> - Banish unwanted magic")
    type_text("  • poetry update - Refresh your magical components\n")
    
    print("\n" + "🎊 " * 15)
    print("YOU ARE NOW A TRUE PACKAGE MAGE!".center(60))
    print("🎊 " * 15)
    print()
    
    type_text("May your code be bug-free and your dependencies always resolve!")
    type_text("Happy coding, Package Mage! 🧙‍♂️✨")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 The magic fades as you step away from the tome...")
        print("   Return when you're ready to continue your journey!")
    except Exception as e:
        print(f"\n❌ A magical disturbance occurred: {e}")
        print("   Check your environment and try again.")