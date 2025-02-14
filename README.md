# 🔐 PyPassword Generator

## 📝 Overview
This project is a simple password generator written in Python. It allows users to create a secure password containing a mix of letters, numbers, and symbols based on their desired length and composition.

## ⭐ Features
- 🔢 Generates a random password with user-specified numbers of letters, symbols, and numbers.
- 🎲 Uses Python's built-in `random` module to ensure randomness.
- 🛡️ Ensures the password has a mix of characters for better security.

## ⚙️ How It Works
The script follows these steps to generate a password:
1. **🖊️ User Input:** The program prompts the user to input how many letters, symbols, and numbers they want in their password.
2. **🔠 Character Selection:**
   - The program randomly selects the specified number of letters from a predefined list of uppercase and lowercase letters.
   - The program randomly selects the specified number of symbols from a predefined list.
   - The program randomly selects the specified number of numbers from 0-9.
3. **🔀 Shuffling:** The selected characters are added to a list and shuffled randomly to ensure randomness.
4. **🔑 Password Generation:** The shuffled list is converted into a string and displayed as the final password.

## 🖥️ Code Explanation
```python
import random
```
- The `random` module is imported to facilitate random selection of characters.

```python
letters=['a','b','c',...,'Z']
numbers=["0","1","2",...,"9"]
symbols=['!','#','$','%','&','(',')','*','+']
```
- Three lists are defined containing possible letters (both uppercase and lowercase), numbers, and symbols.

```python
print("Welcome to the pypassword generator!")
nr_letters=int(input("How many letters would you like in your password?\n"))
nr_symbols=int(input("How many symbols would you like?\n"))
nr_numbers=int(input("How many numbers would you like in your password?\n"))
```
- The program asks the user to input the number of letters, symbols, and numbers they want in their password.

```python
list=[]
for char in range(0,nr_letters):
    x=random.choice(letters)
    list.append(x)
```
- A list is created to store the password characters. Random letters are selected and added to the list.

```python
for char in range(0,nr_symbols):
    list.append(random.choice(symbols))
for char in range(0,nr_numbers):
    list.append(random.choice(numbers))
```
- Random symbols and numbers are selected and added to the list.

```python
y=random.shuffle(list)
```
- The list is shuffled to ensure randomness in the password structure.

```python
print(list)
password=""
for char in list:
    password+=char
print(f"Your password is: {password}")
```
- The shuffled list is converted into a string and displayed as the final password.

## ▶️ How to Run the Program
1. ✅ Ensure you have Python installed.
2. 📋 Copy and paste the script into a Python file (e.g., `password_generator.py`).
3. 🏃 Run the script using `python password_generator.py`.
4. ✍️ Follow the prompts to enter the number of letters, symbols, and numbers.
5. 🔑 Get your randomly generated password.

## 📌 Example Output
```
Welcome to the pypassword generator!
How many letters would you like in your password?
5
How many symbols would you like?
2
How many numbers would you like in your password?
3
Your password is: aT#7pK1*9
```

## 🚀 Improvements
- ❌ Allow users to exclude specific characters.
- 🔄 Add an option to generate multiple passwords at once.
- ✅ Improve user experience by validating inputs.

## 🎯 Conclusion
This Python password generator is a simple yet effective way to create secure passwords. It ensures randomness by selecting characters from predefined lists and shuffling them. This tool can help users generate strong passwords quickly. 🔒

