# 🐵 Monkey-CLI

A minimalistic typing test application for your terminal - inspired by [Monkeytype](https://monkeytype.com).

## Features

✨ **Real-time Statistics**: Track your WPM (Words Per Minute) and accuracy as you type  
🎨 **Color-Coded Feedback**: Green for correct characters, red for mistakes  
⏱️ **Timed Tests**: 30-second typing challenges  
🔄 **Restart Anytime**: Press ESC to restart, Ctrl+C to quit  
📊 **Detailed Results**: See your performance summary at the end  

## Installation

Clone this repository:
```bash
git clone https://github.com/arbkm22/monkey-cli.git
cd monkey-cli
```

No external dependencies needed! The application uses Python's built-in `curses` library.

### Windows Users
If you're on Windows, you'll need to install `windows-curses`:
```bash
pip install windows-curses
```

## Usage

Run the typing test:
```bash
python3 monkey_cli.py
```

Or make it executable and run directly:
```bash
chmod +x monkey_cli.py
./monkey_cli.py
```

## How to Play

1. **Start**: Press any key to begin the test
2. **Type**: Type the displayed words as accurately and quickly as possible
3. **Monitor**: Watch your real-time WPM and accuracy stats at the top
4. **Complete**: Finish the test or wait for the timer to run out
5. **Review**: Check your final statistics
6. **Restart**: Press ESC to try again or Ctrl+C to quit

## Keyboard Shortcuts

- **Any Key**: Start the test
- **Backspace**: Delete the last character
- **ESC**: Restart the test
- **Ctrl+C**: Quit the application

## Customization

You can customize the test by modifying the parameters in `monkey_cli.py`:

```python
# Change duration (in seconds) and word count
test = TypingTest(stdscr, duration=60, word_count=100)
```

## Requirements

- Python 3.6+
- Terminal with color support
- Unix/Linux/macOS (native curses support) or Windows (with windows-curses)

## Screenshots

The application features:
- Color-coded text (green for correct, red for incorrect)
- Real-time WPM and accuracy display
- Clean, distraction-free interface
- Comprehensive results screen

## License

MIT

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

---

Made with ❤️ for terminal enthusiasts
