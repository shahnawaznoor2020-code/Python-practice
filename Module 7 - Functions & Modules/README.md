# Python Functions, Modules & Application Architecture

A dedicated repository section tracking my progression into Python's modular programming concepts. This collection transitions from writing linear, top-to-bottom scripts to structuring code into reusable blocks (functions) and multi-file architectures (modules). It culminates in the development of a fully interactive CLI banking application.

## 🚀 Overview
This module covers the core principles of the DRY (Don't Repeat Yourself) methodology in Python. The scripts demonstrate how to define and invoke functions, manage different types of arguments, utilize advanced functional programming concepts (lambdas, recursion), and organize code across multiple files using imports, standard libraries, and the `__name__ == "__main__"` paradigm.

## 🛠️ Tech Stack & Tools
* **Language:** Python 3
* **Core Concepts:** Function Definition (`def`), Variable Scope (`global`), Argument Unpacking (`*args`, `**kwargs`), Recursive Logic, Anonymous Functions (`lambda`), Higher-Order Functions (`map`, `filter`), Module Importation, Execution Context (`__name__`)
* **Standard Modules:** `math`, `datetime`, `random` (`random()`, `randint()`, `choice()`, `shuffle()`)

## 📂 File Index & Structure

### Function Fundamentals & Arguments
* `Functions_in_p.py`: A comprehensive guide to Python functions. Covers basic definitions, returning multiple values (as tuples), and handling various argument types: Positional, Default, Keyword, and Variable-Length (`*args` for tuples, `**kwargs` for dictionaries).
* `Doc_string.py`: Demonstrates best practices for documenting code using standard docstrings `"""` and utilizing the built-in `help()` function to retrieve function metadata.

### Advanced Functional Concepts
* `Recusive_function.py`: Explores recursive logic where a function calls itself, using factorial calculation as the primary example. Also demonstrates passing functions as arguments to other functions.
* `Lambda_Function.py`: Introduces anonymous, single-line functions using the `lambda` keyword. Shows how to integrate lambdas with Python's higher-order functions like `filter()` (to extract even numbers) and `map()` (to apply mathematical transformations across lists).

### Standard Libraries & Modularity
* `random_module.py`: Explores the `random` standard library, showcasing how to generate random floats (`random()`), integers (`randint()`), pick random choices from sequences (`choice()`), and shuffle lists in place (`shuffle()`).
* `Modules_in_Python.py`: Covers the basics of importing built-in Python libraries (`math`, `random`, `datetime`) using standard `import`, selective `from ... import`, and aliasing with `as`.
* `Arithemetic_for_user_defined_module.py`: Acts as a custom module containing basic math functions. Demonstrates the critical `if __name__ == "__main__":` block to prevent testing code from running when the file is imported elsewhere.
* `my_name.py` & `User_defined_module.py`: Companion scripts that demonstrate how to import and utilize the custom functions defined in `Arithemetic_for_user_defined_module.py`.

### Capstone Application
* `A_simple_banking_application.py`: A fully functional Command Line Interface (CLI) program that integrates loops, conditional logic, dictionaries (for KYC data), functions, and global variable management. Features include an interactive menu, deposit/withdrawal logic, balance checking, and dynamic dictionary updates.

## 💡 Key Learnings & Features
* **Flexible Parameters:** Mastering `*args` and `**kwargs` allows for the creation of highly flexible functions that can accept an unknown amount of data, mimicking how built-in functions like `print()` operate.
* **The `__name__` Variable:** Understanding how Python assigns the string `"__main__"` to the script currently being executed, allowing developers to write files that function as both importable modules and standalone executable scripts.
* **State Management via Globals:** Learning how to track application state (like an account balance or user dictionary) across multiple function calls using the `global` keyword.
* **Standard Library Integration:** Leveraging Python's built-in modules like `random` and `math` to add complex behavior (like unpredictability) without writing algorithms from scratch.
* **Functional Programming:** Shifting from iterative loops to applying single-line logic across datasets using `lambda` functions paired with `map()` and `filter()`.

---
## 👨‍💻 Author

**MD Shahnawaz Noor** GitHub: [https://github.com/shahnawaznoor2020](https://github.com/shahnawaznoor2020)
