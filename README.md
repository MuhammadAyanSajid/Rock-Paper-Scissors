# Rock Paper Scissors Game 🎮

A collection of Rock Paper Scissors games implemented in Python with both console and GUI versions, featuring advanced gameplay modes and customizable options.

## 🎯 Features

### Core Gameplay
- **Classic Rock Paper Scissors** - Traditional rules with rock beats scissors, scissors beats paper, paper beats rock
- **Score Tracking** - Keep track of player wins, computer wins, and ties
- **Random Computer Opponent** - Computer makes random choices for fair gameplay

### Advanced Features
- **Best of X Series Mode** - Play complete series (Best of 3, 5, 7, or 9)
- **Series Winner Detection** - Automatic detection and announcement of series winners
- **Customizable UI** - Toggle emojis on/off for personalized experience
- **Game State Management** - Smart button disable/enable and game reset functionality

## 📁 Project Structure

```
Rock Paper Scissors/
├── rock_paper_scissors.py          # Original GUI version with Tkinter
├── rock_paper_scissors_console.py  # Console version for compatibility
├── rock_paper_scissors_fixed.py    # Enhanced version with all features
├── test_tkinter.py                 # Tkinter compatibility test utility
└── README.md                       # This file
```

## 🚀 Getting Started

### Prerequisites
- Python 3.7 or higher
- Tkinter (usually included with Python)
- Windows, macOS, or Linux

### Installation
1. Clone or download this repository
2. Navigate to the project directory
3. Run any of the game versions:

```bash
# Enhanced GUI version (recommended)
python rock_paper_scissors_fixed.py

# Console version (no GUI required)
python rock_paper_scissors_console.py

# Original GUI version
python rock_paper_scissors.py
```

## 🎮 Game Versions

### 1. Enhanced GUI Version (`rock_paper_scissors_fixed.py`) ⭐ **Recommended**

**Features:**
- 🏆 **Best of X Series Mode** - Choose from Best of 3, 5, 7, or 9
- 🎨 **Emoji Toggle** - Enable/disable emojis in winner announcements
- 📊 **Advanced Score Tracking** - Series progress and completion detection
- 🎯 **Smart Game Management** - Auto-disable buttons when series complete
- 🔄 **New Game Function** - Easy series reset
- 🖥️ **Enhanced UI** - Separate displays for choices, results, and scores

**How to Play:**
1. Select your preferred series length (Best of 3, 5, 7, or 9)
2. Toggle emoji display on/off if desired
3. Click Rock, Paper, or Scissors to make your move
4. First to reach the target wins (e.g., 3 wins in Best of 5)
5. Click "New Game" to start a fresh series

### 2. Console Version (`rock_paper_scissors_console.py`)

**Features:**
- 💻 **No GUI Required** - Perfect for terminal/command line use
- 🎮 **Interactive Gameplay** - Type your choices directly
- 📈 **Score Tracking** - Tracks wins, losses, and ties
- 🔄 **Continuous Play** - Keep playing until you type "quit"

**How to Play:**
1. Run the script
2. Type `rock`, `paper`, or `scissors` when prompted
3. View results and updated scores after each round
4. Type `quit` to exit the game

### 3. Original GUI Version (`rock_paper_scissors.py`)

**Features:**
- 🖱️ **Simple GUI Interface** - Basic Tkinter buttons and labels
- 🎯 **Classic Gameplay** - Traditional Rock Paper Scissors rules
- 📊 **Basic Score Tracking** - Win/loss/tie counters

## 🎨 Customization Options

### Emoji Display
Toggle between:
- 🎉 **With Emojis**: `🎉 YOU WIN THE SERIES!` / `💻 COMPUTER WINS THE SERIES!`
- 📝 **Plain Text**: `YOU WIN THE SERIES!` / `COMPUTER WINS THE SERIES!`

### Series Length Options
- **Best of 3** - First to 2 wins
- **Best of 5** - First to 3 wins  
- **Best of 7** - First to 4 wins
- **Best of 9** - First to 5 wins

## 🔧 Technical Details

### System Requirements
- **Python Version**: 3.7+
- **GUI Framework**: Tkinter (included with Python)
- **Platform**: Cross-platform (Windows, macOS, Linux)

### Tkinter Setup (Windows)
If you encounter Tkinter issues on Windows, the enhanced version includes automatic path fixes for common Python installations.

### Dependencies
- `random` - For computer choice generation
- `tkinter` - For GUI versions
- `os` - For environment configuration

## 🎯 Gameplay Rules

### Classic Rules
- **Rock** beats **Scissors** (crushes)
- **Scissors** beats **Paper** (cuts)  
- **Paper** beats **Rock** (covers)
- Same choice = **Tie**

### Series Mode
- Select your series length
- First player to reach the target number of wins wins the series
- Ties don't count toward the target, but are tracked separately
- Series ends immediately when target is reached

## 🐛 Troubleshooting

### Common Issues

**Tkinter Not Working (Windows)**
```
Error: Can't find a usable init.tcl
```
**Solution**: Use `rock_paper_scissors_fixed.py` which includes automatic path fixes, or use the console version.

**Python Not Found**
```
Error: 'python' is not recognized
```
**Solution**: Use `python3` instead of `python` or check your Python installation.

### Testing Tkinter
Run the included test utility:
```bash
python test_tkinter.py
```

## 🤝 Contributing

Feel free to contribute improvements:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📝 Version History

- **v2.0** - Added Best of X series mode, emoji toggle, enhanced UI
- **v1.1** - Added console version for compatibility
- **v1.0** - Initial GUI version with basic gameplay

## 🎮 Screenshots

### Enhanced GUI Version
- Series selection dropdown
- Emoji toggle checkbox  
- Separate choice and result displays
- Series winner announcements
- New Game functionality

### Console Version
- Text-based interaction
- Continuous gameplay loop
- Score tracking display
- Simple quit command

## 🏆 Game Statistics

Track your performance across different series lengths and see how you match up against the computer's random strategy!

---

**Enjoy playing Rock Paper Scissors!** 🎉

*Made with Python and Tkinter*