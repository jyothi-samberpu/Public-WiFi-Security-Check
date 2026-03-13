# Public Wi-Fi Security Checker

## Overview

Public Wi-Fi networks are widely used in places like cafés, airports, universities, and shopping malls. Many users connect to these networks without checking whether they are secure or encrypted. Open Wi-Fi networks can expose users to cyber threats such as data interception, packet sniffing, and man-in-the-middle attacks.

This project is a **Python-based desktop application** that helps users quickly check the security status of the Wi-Fi network they are connected to. The application detects the network name (SSID), authentication type, and alerts the user if the connection appears unsafe.

The tool uses a simple graphical user interface (GUI) built with Tkinter to display the network information in a clear and user-friendly way.

---

## Features

- Detects the currently connected Wi-Fi network
- Displays the **SSID (network name)**
- Displays the **authentication type** (Open, WPA2, WPA3, etc.)
- Warns users when connected to an **open or unsecured network**
- Clean and user-friendly graphical interface
- Status indicator showing **Safe / Unsafe network**

---

## Technologies Used

- **Python**
- **Tkinter** – for building the graphical user interface
- **Subprocess module** – to execute system commands
- **Windows Wi-Fi command**

The program retrieves Wi-Fi information using the following command:

```
netsh wlan show interfaces
```

---

## How the Application Works

1. The user opens the application.
2. The user clicks the **"Check Wi-Fi Security"** button.
3. The program runs a system command to retrieve Wi-Fi details.
4. The application extracts:
   - SSID (network name)
   - Authentication type

5. The program determines whether the network is:
   - **Open (unsafe)**
   - **Encrypted (safer)**

6. The GUI displays the result along with a warning or confirmation message.

---

## Example Output

Example when connected to an open network:

```
Network Name: CoffeeShopWiFi
Authentication: Open

Warning: This Wi-Fi appears open and may expose your data.
```

Example when connected to a secure network:

```
Network Name: HomeWiFi
Authentication: WPA2-Personal

Good: This Wi-Fi is encrypted and safer for daily use.
```

---

## How to Run the Project

### Step 1: Install Python

Make sure Python is installed on your system.

### Step 2: Clone the Repository

```
git clone https://github.com/yourusername/wifi-security-checker.git
```

### Step 3: Navigate to the Project Folder

```
cd wifi-security-checker
```

### Step 4: Run the Program

```
python wifi_checker.py
```

The graphical interface will open and you can check the Wi-Fi security status.

---

## Project Structure

```
wifi-security-checker/
│
├── wifi_checker.py
├── README.md
└── screenshots/
```

---

## Limitations

- Works primarily on **Windows systems** because it uses the `netsh` command.
- Detects only the **currently connected network**, not all nearby networks.
- Does not perform deep network security analysis.

---

## Future Improvements

Possible upgrades for this project include:

- Scanning nearby Wi-Fi networks
- Detecting **duplicate SSIDs (Evil Twin attacks)**
- Displaying **BSSID and signal strength**
- Adding a **network risk score**
- Supporting Linux and macOS systems
- Logging detected networks for analysis

---

## Learning Outcomes

This project demonstrates:

- Basic **network security awareness**
- Using **system commands in Python**
- Parsing command output
- Building desktop applications with **Tkinter**
- Designing a simple **cybersecurity utility tool**

---

## Conclusion

The Public Wi-Fi Security Checker helps users understand the security level of their Wi-Fi connection. By alerting users when they connect to open networks, the tool promotes safer internet usage and raises awareness about wireless security risks.

---

## Author

Developed as a cybersecurity mini project using Python.
