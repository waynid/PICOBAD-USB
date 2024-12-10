
---

<p align="center">
  <img src="https://cdn-shop.adafruit.com/970x728/4864-00.jpg" alt="Raspberry Pi Pico" width="300"/>
</p>

# <p align="center">**PICOBAD-USB**</p>

Turn your **Raspberry Pi Pico** into an HID (keyboard) device capable of sending commands to a computer. This project uses **CircuitPython** and supports different keyboard layouts.

By default, the keyboard is configured in **French (AZERTY)**, but you can easily modify it to use other languages.

---

## **📥 Installation**

### 1. Prepare the Raspberry Pi Pico

1. **Connect your Raspberry Pi Pico** while holding down the **BOOTSEL** button.
2. The Pico will appear as a storage device on your computer. Download and install **CircuitPython** for the Raspberry Pi Pico from the following link:
   - [Download CircuitPython for Raspberry Pi Pico (French version)](https://downloads.circuitpython.org/bin/raspberry_pi_pico/fr/adafruit-circuitpython-raspberry_pi_pico-fr-9.2.1.uf2)
3. **Drag and drop** the `.uf2` file into the Pico's directory to install CircuitPython.

---

### 2. Clone the repository

1. Open your terminal and clone the GitHub repository with the following command:
   ```bash
   git clone https://github.com/WAYNID/PICOBAD-USB.git
   ```
2. Go to the project folder:
   ```bash
   cd PICOBAD-USB
   ```

---

### 3. Copy the files to the Pico

1. **Replace the `lib` folder** in your **CIRCUITPY** directory with the one from the **PICOBAD-USB** project. This folder contains all the libraries necessary for the proper functioning of the project.

2. **Also replace the `code.py` file** in your **CIRCUITPY** directory with the **`code.py`** file from the project. This file is automatically executed when you plug in the Raspberry Pi Pico.

---

## ⚠️ **Warning**

**CAUTION**: If you edit and save the **`code.py`** file, it will be **automatically executed** by the Raspberry Pi Pico. Depending on the **payload** you have created, this could lead to **irreversible** effects on the target computer, such as file deletion or system setting modifications.

Be extremely careful when modifying this file. Make sure you fully understand the actions you are programming before executing them.

---

## **🖥️ Usage**

The **`code.py`** file is automatically executed as soon as you connect the Raspberry Pi Pico. By default, it opens the command prompt and sends commands to the target computer.

### Example of operation:

- The script sends the keys **`WIN + R`**, types **`cmd`**, and presses **`ENTER`** to open the command prompt.
- It then displays the following message in the command prompt:  
  `Welcome to PICOBAD-USB! THIS IS THE BASE CODE.`

### Customizing the code

Modify the **`code.py`** file to add your own **payloads**. For example, to automatically open Notepad:

```python
keyboard.send(badUSB.WINDOWS, badUSB.R)
time.sleep(1)
layout.write("notepad")
keyboard.send(badUSB.ENTER)
```

---

## **🔤 Configuring the Keyboard Layout**

The default keyboard layout is **French (AZERTY)**. If you want to use a different keyboard layout, here are the steps to follow:

1. Visit [GitHub - CircuitPython Keyboard Layouts](https://github.com/Neradoc/Circuitpython_Keyboard_Layouts).
2. Download and install the layout of your choice.
3. Modify the **`code.py`** file to use the new layout.

---

## **📚 Additional Resources**

- [Official CircuitPython Documentation](https://circuitpython.org/)
- [Adafruit HID Library - GitHub](https://circuitpython.org/libraries)
- [CircuitPython Keyboard Layouts - GitHub](https://github.com/Neradoc/Circuitpython_Keyboard_Layouts)
- To understand how HID devices work with CircuitPython, check out [Adafruit_CircuitPython_HID](https://github.com/adafruit/Adafruit_CircuitPython_HID/).

---

## **👨‍💻 Authors**

- **WAYNID** - Project creator.

---
