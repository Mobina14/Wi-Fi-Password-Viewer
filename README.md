**🔐 Wi-Fi Password Viewer (Windows)**

A simple GUI-based Wi-Fi password viewer built with Python and Tkinter.
This tool retrieves and displays all saved Wi-Fi profiles and their passwords directly from your Windows system — clean, fast, and easy to use.

✨ Features

🧩 Retrieves all saved Wi-Fi profiles on Windows

🔍 Displays both SSID and password in a clean table

🪟 Simple Tkinter interface (no command line needed)

⚡ One-click “Show Wi-Fi Passwords” button

🧰 Works entirely offline — no internet or admin privileges required

⚙️ Requirements

Windows OS (tested on Windows 10 / 11)

Python 3.7+

Modules:

tkinter
subprocess


All modules used are built-in with Python — no external installation required.

**🖥️ How It Works**

The app runs the Windows command:

netsh wlan show profiles


to list all Wi-Fi profiles, and then:

netsh wlan show profile "ProfileName" key=clear


to extract each network’s password.

It then displays all results in a TreeView table with columns for Wi-Fi Name and Password.

**🧩 Project Structure**
wifi-password-viewer/
│
├── wifi_password_viewer.py   # Main application
├── README.md                 # Documentation
└── LICENSE                   # (Optional)

**🚀 How to Run**

Clone the repository:

git clone https://github.com/Mobina14/wifi-password-viewer.git
cd wifi-password-viewer


Run the Python script:

python wifi_password_viewer.py


Click “Show Wi-Fi Passwords” to view all saved networks.

**🧠 Technical Overview**
Component	Description
GUI Framework	Tkinter
Core Command	netsh wlan show profiles
Platform	Windows only
Output Table	Tkinter ttk.Treeview
Error Handling	Uses subprocess.CalledProcessError and message boxes
**🧑‍💻 Author**

Mobina RZ
📍 Mashhad, Iran
💡 Focused on educational and practical Python applications

