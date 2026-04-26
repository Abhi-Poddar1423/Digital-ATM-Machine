# 🏦 ATM Simulation System (Python)

A modular, menu-driven ATM simulation project developed as part of my B.Tech CSE coursework. This project focuses on **Procedural Programming**, **File Handling**, and **Modular Architecture**.

## 🌟 Key Features
* **Secure Access:** PIN-based authentication system.
* **Balance Management:** Real-time balance updates for deposits and withdrawals.
* **Transaction Statement:** Automatically records every transaction in a local `statement.txt` file with timestamps.
* **Attractive UI:** Colorized terminal output using the `colorama` library for a better user experience.
* **Modular Design:** Separate files for Logic, Authentication, and the Main Menu (Package Architecture).

## 📂 Project Structure
```text
ATM_Project/
│── main.py            # Entry point: Infinite loop with the menu system.
│── logic.py           # Core: Handles deposits, withdrawals, and file logging.
│── auth.py            # Security: Manages PIN verification.
│── transactions.txt      # Database: Stores transaction history (Auto-generated).
└── .gitignore         # Keeps the repository clean by ignoring temp files.

🛠️ Requirements
To see the colors in the terminal, you need to install the colorama library:

Bash
pip install colorama

🚀 How to Run
Clone this repository:


git clone [https://github.com/YOUR_USERNAME/ATM-Simulation-Python.git](https://github.com/Abhi-Poddar1423/ATM-Simulation-Python.git)
Navigate to the folder:


cd ATM-Simulation-Python
Run the application:


python main.py
📝 General Instructions Followed
[x] Used an Infinite Loop (while True) for the menu.

[x] Followed Package Architecture (split into multiple files).

[x] Logic is kept out of the main.py file.

[x] Code is well-structured and readable.

Developed by: [Jitendra Kumar Poddar]

Tech Stack: Python, VS Code, Git/GitHub
