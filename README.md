# BingoGamePlay

A simple desktop-based **Housie (Tambola)** game created using Python and MySQL for Class XII Computer Science Project (2021-22) by Prince Mathur.

## 📝 Project Description

This project is a simulation of the traditional Housie/Tambola game. It includes number calling functionality with audio playback and uses an SQL database to store game data like winners and settings.

### Features

- Automated number calling with real-time audio playback.
- Pre-recorded audio files for each number from 1 to 90.
- MySQL database integration to store:
  - Winner history
  - Game settings and options
- Database setup handled within the code itself.
- Simple and clean terminal-based interface.

## 📂 Folder Structure

```
📁 Prince Mathur CS Project Xll A 2021-22 Housie
├── Game.py             # Main game script
├── *.mp3 / *.m4a       # Audio files for number announcements
```

## 🚀 How to Run

Make sure you have Python 3, MySQL, and required libraries installed.

1. Clone this repository or download the ZIP.
2. Install MySQL on your system.
3. Update the MySQL password in `Game.py` to match your system's root password.
4. Install dependencies.
5. Run the main Python file:

```bash
python Game.py
```

> ⚠️ Ensure MySQL is installed and the credentials in the code match your local setup.

## 🛠 Dependencies

- Python Standard Library
- [`playsound`](https://pypi.org/project/playsound/) – For audio playback
- [`mysql-connector-python`](https://pypi.org/project/mysql-connector-python/) – For MySQL connection

Install dependencies via pip:

```bash
pip install playsound mysql-connector-python
```

## 🧠 MySQL Setup

The required database and tables are created automatically by the Python script. You only need to ensure:
- MySQL is installed
- Your password is updated in the script
- MySQL service is running

## 👨‍💻 Author

**Prince Mathur**  
Class XII – A  
Computer Science Project (2021-22)

## 📃 License

This project is intended for educational purposes only.
