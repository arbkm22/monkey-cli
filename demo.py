#!/usr/bin/env python3
"""
Demo script to show Monkey-CLI interface without actual typing.
This creates a simulated screenshot of what the application looks like.
"""

# ANSI color codes
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
CYAN = '\033[96m'
WHITE = '\033[97m'
GRAY = '\033[90m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
RESET = '\033[0m'


def print_demo():
    """Print a demo of what the Monkey-CLI looks like."""
    
    print("\n" + "=" * 80)
    print(f"{CYAN}{BOLD}🐵 MONKEY-CLI - Terminal Typing Test{RESET}")
    print(f"{YELLOW}Time: 25.3s | WPM: 45 | Accuracy: 96.2%{RESET}")
    print("─" * 80)
    print()
    
    # Sample text with color coding
    # Green = typed correctly, Red = typed incorrectly, White = not yet typed
    typed_correct = "the quick brown fox jumps over"
    typed_incorrect = "t"
    remaining = "he lazy dog and runs through the field"
    
    print(f"{GREEN}{typed_correct}{RESET}{RED}{typed_incorrect}{RESET}{UNDERLINE}h{RESET}{WHITE}e lazy dog and runs through the field{RESET}")
    print(f"{WHITE}with great speed and agility in the morning sunshine{RESET}")
    print()
    
    print(f"{GRAY}ESC: Restart | Ctrl+C: Quit{RESET}")
    print("=" * 80)
    print()
    
    # Results screen demo
    print("\n" + "=" * 80)
    print(f"{CYAN}{BOLD}🎉 Test Complete!{RESET}")
    print()
    print(f"{YELLOW}WPM: 52.34{RESET}")
    print(f"{YELLOW}Accuracy: 96.50%{RESET}")
    print(f"{YELLOW}Correct Characters: 193{RESET}")
    print(f"{YELLOW}Incorrect Characters: 7{RESET}")
    print(f"{YELLOW}Total Characters: 200{RESET}")
    print()
    print(f"{GRAY}Press ESC to restart or Ctrl+C to quit{RESET}")
    print("=" * 80)
    print()

if __name__ == "__main__":
    print("\n" + CYAN + BOLD + "Monkey-CLI Interface Preview" + RESET)
    print(GRAY + "This shows what the application looks like during and after a typing test:" + RESET)
    
    print_demo()
    print(f"{GREEN}✓ Ready to run! Execute: python3 monkey_cli.py{RESET}")
    print()
