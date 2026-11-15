# Python Data Structures: Lists & Operations

A dedicated repository section tracking my progression into Python's core data structures, specifically focusing on Lists. This collection covers list creation, dynamic manipulation, multidimensional indexing, and built-in numerical operations, which are essential for data management, analytics, and algorithmic problem-solving.

## 🚀 Overview
This module covers the complete lifecycle of Python lists. The scripts demonstrate how to initialize lists, traverse them using standard and nested indexing, dynamically modify their contents using built-in list methods, and perform aggregations using built-in mathematical functions.

## 🛠️ Tech Stack & Tools
* **Language:** Python 3
* **Core Concepts:** 1D & Multidimensional Lists, Indexing & Slicing, List Concatenation (`+`) & Repetition (`*`), Mixed Data Types, Membership Operators (`in`, `not in`)
* **List Methods:** `.append()`, `.insert()`, `.extend()`, `.remove()`, `.pop()`, `.reverse()`, `.sort()`, `.count()`
* **Built-in Functions:** `len()`, `min()`, `max()`, `sum()`

## 📂 File Index & Structure

### List Basics & Indexing
* `ListIntroduction.py`: Covers the fundamentals of list creation, accessing elements via positive and negative indexing, and determining list size using `len()`.
* `NestedList.py`: Explores multidimensional lists (lists within lists) containing mixed data types. Demonstrates how to access deep elements using chained indexing (e.g., `l2[-1][-1][-1]`).

### Modification & Growth
* `ListOperation.py`: Demonstrates list slicing, concatenation, and repetition. Introduces dynamic growth methods like `append()` (adding a single element to the end) and `insert()` (adding an element at a specific index).
* `ListOperation2.py`: Continues with list modification, showing how to merge multiple items using `extend()`, delete specific values using `remove()`, and extract/delete items by index using `pop()`.

### Sorting, Analysis & Math
* `ListOperation3.py`: Focuses on ordering and evaluating list data. Covers in-place reversal (`reverse()`), descending order sorting (`sort(reverse=True)`), frequency counting (`count()`), and boolean evaluations using membership operators.
* `NumericalOperationOfList.py`: Applies Python's built-in mathematical functions to lists of numbers, quickly calculating the minimum (`min()`), maximum (`max()`), and total sum (`sum()`) of the dataset.

## 💡 Key Learnings & Features
* **Mutability:** Understanding that unlike strings, lists are mutable. Methods like `.append()`, `.sort()`, and `.reverse()` modify the original list directly in memory rather than returning a new list.
* **Append vs. Extend:** Recognizing the critical difference between adding a single item (or a single nested list) with `.append()` versus unpacking multiple items into the current list using `.extend()`.
* **Multidimensional Traversal:** Mastering chained bracket notation (`[][]`) to navigate complex, nested data structures, a foundational skill for working with matrices and JSON-like data in data science.
* **In-Place Modification vs. Evaluation:** Differentiating between list methods that return `None` (because they modify the list in place, like `.sort()`) and functions that evaluate the list and return a value (like `sum()` or `len()`).

---
## 👨‍💻 Author

**MD Shahnawaz Noor**     
*Aspiring Data Scientist* 
   
GitHub: [https://github.com/shahnawaznoor2020](https://github.com/shahnawaznoor2020)
