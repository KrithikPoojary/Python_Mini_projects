# Python Mini Projects

## Projects

- Calculator
- Password Generator
- Unit Converter
- Hotel Management System
- Feature Extraction (Anime Dataset)

## Feature Extraction (Anime Dataset) Features

- Reading and exploring CSV data using `pandas`
- Custom function to extract **episode count** from the `Title` column (e.g., `"(64 eps)"` → `64`)
- String cleaning to remove unwanted text (`" eps"`) before type conversion
- Data type conversion (`str` → `int`) for numerical analysis
- Custom function to extract **Airing Date** from the `Title` column using character-by-character parsing
- Function to calculate **Total Months** between start and end airing dates (e.g., `Apr 2009 - Jul 2010` → `16`)
- Use of `pd.to_datetime()` with custom format (`%b %Y`) to parse month-year strings
- Data type verification at each transformation step using `type()`
- Row-wise data inspection using `.loc[]`
- Command-line / notebook-based data analysis

## Calculator Features

- Addition
- Subtraction
- Multiplication
- Division
- Average Calculation
- Square
- Cube
- Square Root
- Command-line Interface

## Password Generator Features

- User-defined password length
- Random letter generation
- Random number generation
- Random symbol generation
- Password randomization using `random.shuffle()`
- Strong password generation
- Command-line interface (CLI)
- User-friendly input prompts
- Dynamic password creation

## Unit Converter Features

- Length Conversion
- Weight Conversion
- Temperature Conversion
- Easy-to-use Interface
- Fast Unit Conversion
- Beginner-friendly Python Project

## Hotel Management System Features

- Room booking (Mid-range, Semi-luxury, Premium rooms)
- Stay-type selection (One day / One night / Few hours)
- Restaurant menu system (Chinese, Rice Meal, Chicken Meal, Drinks)
- Multi-item food ordering with quantity selection
- Itemized bill generation with subtotal per item
- Grand total calculation
- Check-in / checkout timestamp using `datetime`
- Object-Oriented design using classes
- Nested dictionaries for structured menu and room data
- Dictionary unpacking (`**`) to merge multiple menus into one
- Modular code split across multiple files (`main.py`, `room.py`, `menu.py`)
- Command-line interface (CLI)

## Technologies

- Python 3
- Random Module
- Time Module
- Datetime Module
- Pandas
- NumPy

## What I Learned

- Variables
- User Input
- Conditional Statements (`if-else`)
- Loops (`while`, `for`)
- Functions
- Lists
- Dictionaries (including nested dictionaries)
- Dictionary Unpacking (`**`)
- String Manipulation
- Random Module
- List Operations
- `random.choice()`
- `random.shuffle()`
- Object-Oriented Programming basics (Classes, Methods, `self`)
- Working with `datetime` for timestamps
- Modular code using separate files (imports across modules)
- Code Organization
- Beginner-friendly Project Structure
- Reading and analyzing CSV data with `pandas`
- Custom string parsing to extract structured data from unstructured text
- Data type conversion and verification (`str` to `int`, string to `datetime`)
- Using `pd.to_datetime()` for date parsing with custom formats
- Calculating date differences (month-level granularity) using `.dt` accessor
- Debugging and testing transformations row-by-row with `.loc[]`

## Project Structure

```text
Python-Mini-Projects/
├── Calculator/
│   └── main.py
├── Hotel_management_system/
│   ├── main.py
│   ├── menu.py
│   └── room.py
├── Password_Generator/
│   └── main.py
├── Unit_Convertor/
│   └── main.py
├── Feature_extraction/
│   ├── anime.csv
│   ├── main.py
│   └── Project1.ipynb
└── README.md
```

## About

This repository contains beginner-friendly Python projects that I built while learning Python programming.

Each project helped me practice Python fundamentals while solving simple real-world problems and improving my problem-solving skills. The Hotel Management System project pushed me further into Object-Oriented Programming, nested data structures, and building a more complete, multi-file, multi-step CLI application. The Feature Extraction project introduced me to data analysis with `pandas`, working with real-world messy data, and extracting structured features (episode counts, airing dates, duration in months) from raw text fields.

## Future Improvements

- Add more utility-based Python projects
- Improve user interface
- Add better input validation
- Optimize the code structure
- Learn Object-Oriented Programming (OOP) further
- Convert some projects into GUI applications
- Add persistent storage (CSV/JSON/SQLite) for hotel bookings and orders
- Combine room and food billing into a single unified invoice
- Extend feature extraction to more columns (e.g., Studio, Genre) from the anime dataset
- Handle edge cases in date/episode parsing (missing or malformed values)

## Note

This repository represents my Python learning journey.

- All projects are written by me.
- My goal is to keep building more Python projects as I continue learning.