# Python Data Structures: Tuples, Sets, Dictionaries & Memory

A dedicated repository section tracking my progression into Python's advanced and non-sequential data structures. This collection moves beyond basic lists to explore immutable collections (Tuples), unique mathematical collections (Sets), and key-value mappings (Dictionaries). Additionally, it dives into intermediate memory management concepts, specifically shallow and deep copying.

## 🚀 Overview
This module covers the core behaviors, constraints, and methods associated with Tuples, Sets, and Dictionaries. The scripts demonstrate how to choose the right data structure based on the need for mutability, uniqueness, or fast key-based lookups. Furthermore, it explores how Python handles memory allocation when copying complex, nested data structures.

## 🛠️ Tech Stack & Tools
* **Language:** Python 3
* **Core Concepts:** Mutability vs. Immutability, Key-Value Pairs, Set Theory & Mathematical Operations, Memory Allocation (`id()`), Object References
* **Built-in Types:** `tuple`, `dict`, `set`, `frozenset`
* **Modules Used:** `copy` (`copy.copy()`, `copy.deepcopy()`)

## 📂 File Index & Structure

### Immutability & Fixed Collections
* `TupleIntroduction.py`: Covers the fundamentals of Tuples, highlighting their immutability compared to lists. Demonstrates tuple packing/unpacking (parentheses being optional), index/count methods, and converting lists to tuples using type casting.

### Key-Value Mappings
* `DictionaryIntroduction.py`: Explores Dictionaries (`dict`) for creating associative arrays. Covers adding/updating pairs, handling missing keys safely with `.get()`, merging dictionaries with `.update()`, and iterating using `.keys()`, `.values()`, and `.items()`. Highlights the rule that dictionary keys must be immutable data types.

### Mathematical Sets & Uniqueness
* `SetsIntroduction.py`: Introduces Sets for storing non-sequential, unique elements. Demonstrates adding/removing items (`add()`, `remove()`, `discard()`), and applying mathematical set operations like Union (`|`), Intersection (`&`), Difference (`-`), and Symmetric Difference (`^`). Also introduces immutable `frozenset`s.

### Memory Management & Object Copying
* `ShallowDeepCopy.py`: A deep dive into how Python references objects in memory using `id()`. Contrasts standard assignment (`=`) with Shallow Copy (`copy.copy()`) and Deep Copy (`copy.deepcopy()`), illustrating how nested lists behave differently when copied and modified across these methods.

## 💡 Key Learnings & Features
* **Choosing the Right Structure:** Understanding when to use a List (ordered, mutable), a Tuple (ordered, immutable - faster and safer for fixed data), a Set (unordered, unique elements - perfect for mathematical intersections), or a Dictionary (fast lookups via keys).
* **Safe Dictionary Access:** Learning to use `.get('key', default_value)` instead of direct bracket notation `['key']` to prevent `KeyError` exceptions when handling unpredictable data.
* **Set Theory in Code:** Utilizing bitwise operators (`&`, `|`, `-`) to perform elegant, single-line comparisons between different datasets (e.g., finding common subjects between students).
* **The Copy Trap:** Realizing that `list2 = list1` does not create a new list, but just a new reference to the same memory location. Mastering `copy.deepcopy()` is critical when working with nested matrices or complex JSON-like dictionaries in data science to prevent unintended overwrites.

---
## 👨‍💻 Author

**MD Shahnawaz Noor** *Aspiring Data Scientist* GitHub: [https://github.com/shahnawaznoor2020](https://github.com/shahnawaznoor2020)
