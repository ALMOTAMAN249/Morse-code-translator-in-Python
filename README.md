# 🧠 Morse Code Translator – Python Project

## 🔍 Project Idea
A simple Python program that converts any English text to **Morse code**, a code that uses dots (`.`) and dashes (`-`) to represent letters, numbers, and symbols.

---

## 🧱 How Does the Program Work?

### 🔤 1. Definition of a Morse Code Table
We created a dictionary containing:
- English letters (A–Z)
- Numbers (0–9)
- Some special symbols

Each key corresponds to its Morse code value.

### ⌨️ 2. User Input
The user enters any English text they want to translate.

### 🔁 3. Converting Letters to Morse Code
- Each letter is converted to **uppercase**.
- If the letter exists in the dictionary, it is converted and added to the result.
- Unsupported characters are either skipped or handled appropriately.

### 📤 4. Result Display
The translated text is printed in Morse code, with each character separated by spaces.

---

## 💡 Example

If the user enters:
HELLO WORLD

The result is:
.... . .-.. .-.. --- / .-- --- .-. .-.. -..

---

## 📦 Project Features

- ✅ **Simple and beginner-friendly**
- 🔧 **Easily extensible**:
  - Add reverse translation (Morse → English)
  - Add a GUI
  - Play Morse code as audio beeps
- 🧰 Teaches key Python concepts:
  - Dictionaries
  - Loops
  - User input handling

---

> Created with ❤️ by **Mohamed El-Motaman**
