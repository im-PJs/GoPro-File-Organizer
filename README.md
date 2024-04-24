# 🎥 GoPro Chapter Organizer

Automatically organize your GoPro or action camera video files into neatly arranged folders based on their chapter numbers with this Python script. It supports .MP4, .LRV, and .THM files and includes a handy undo feature for easy reverts.

## ✨ Features

- **Automatic Organization**: Automatically sorts all video files into chapters, keeping single files alone
- **Supports Multiple File Types**: Handles .MP4, .LRV, and .THM files.
- **Undo Functionality**: Easily revert changes to the original file structure.

## 📋 Prerequisites

Before you get started, make sure you have:
- Python 3.x installed on your system.
- Basic knowledge of navigating the command line.

## 🚀 Installation

1. Clone this repository or download the script directly.
2. Place `main.py` in the directory containing your video files.

## 🛠 Usage

### Organizing Files

To organize your files, open your command prompt or terminal, navigate to the script's directory, and execute:

```bash
python main.py
```

📁 This command will create folders based on chapter numbers and move the relevant files into these folders.

### Undoing Organization

Made a mistake or need to revert? No problem! Just run:

```bash
python main.py -undoLast
```

🔄 This command restores files to their original locations and removes any empty folders created during organization.

## 📝 Example Commands

- **Organize Files**: `python main.py`
- **Undo Changes**: `python main.py -undoLast`

## ⚠️ Notes

- 🛡 Always back up your files before running the script to avoid accidental data loss.
- 📂 The script modifies file locations within its directory; it does not alter file contents.

## 🤝 Contribution

Contributions are welcome! 🌟 Please fork the repository and submit a pull request with your improvements.

## 📜 License

You are allowed to edit, just please credit me/this github page please
