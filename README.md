# Restaurant Menu Analysis Tool
A Python-based tool to automate data analysis for restaurant menus. This application helps restaurants understand customer preferences, optimize their menu offerings, and improve customer satisfaction by analyzing sales, ratings, and other key metrics.

---

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Data Structure](#data-structure)
6. [Contributing](#contributing)
7. [License](#license)

---

## Overview

This project is designed to help restaurants analyze their menu data efficiently. It processes a CSV file containing menu items, validates the data, and generates actionable insights such as identifying popular dishes, underrated items, and unprofitable options. The tool also provides sample data generation and dynamic table visualizations for better readability.

---

## Features

### Core Functionalities
- **CSV Handling:**
  - Load an existing CSV file or generate a sample one.
  - Validate file structure and data integrity (e.g., price precision, required columns).
- **Menu Item Analysis:**
  - Identify **popular items** based on sales and ratings.
  - Detect **underrated items** (high ratings but low sales).
  - Highlight **unprofitable items** (low ratings and low sales).
- **Dynamic Visualizations:**
  - Display results in well-formatted tables with dynamic column sizing.
  - Add ASCII art for a professional and engaging user experience.
- **Error Handling:**
  - Clear error messages with emojis for better readability.
  - Prevent accidental overwrites of existing files.

### Technical Highlights
- Strong typing (`Dict`, `List`, `Optional`) for better code clarity.
- Object-oriented design using the `MenuItem` class for encapsulating menu-related logic.
- Modular functions for easy maintenance and scalability.

---

## Installation

### Prerequisites
- Python 3.9 or higher.
- Basic knowledge of running Python scripts.

### Steps
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/restaurant-menu-analysis.git
   cd restaurant-menu-analysis
   ```
   
## Usage
Running the Program
Navigate to the project directory:
```bash
cd restaurant-menu-analysis
```
Run the script:
```bash
python main.py
```

Follow the prompts:
Use an existing CSV file or generate a sample one.
View detailed reports on menu performance.
Example Output
   ```plaintext
             ('-.                           .-') _  
            _( OO)                        ( OO ) ) 
            (,------.     ,--. ,--.     ,--./ ,--,'  
            |  .---' .-')| ,| |  |.-') |   \ |  |\  
            |  |    ( OO |(_| |  | OO )|    \|  | ) 
           (|  '--. | `-'|  | |  |`-' ||  .     |/  
            |  .--' ,--. |  |(|  '---.'|  |\    |   
            |  `---.|  '-'  / |      | |  | \   |   
            `------' `-----'  `------' `--'  `--'   

Item               | Price  | Category | Avg Rating | Sales/Day
--------------------------------------------------------------------------------------------------------------
Chicken Parmigiana | $19.99 | Main     | 4.73       | Mon:10, Tue:15, Wed:20, Thu:25, Fri:30, Sat:35, Sun:40
Fish and Chips     | $18.99 | Main     | 4.80       | Mon:5, Tue:10, Wed:15, Thu:20, Fri:25, Sat:30, Sun:35
Margherita Pizza   | $15.99 | Main     | 4.17       | Mon:50, Tue:60, Wed:70, Thu:80, Fri:90, Sat:100, Sun:110
Caesar Salad       | $9.99  | Starter  | 4.63       | Mon:20, Tue:25, Wed:30, Thu:35, Fri:40, Sat:45, Sun:50
Garlic Bread       | $6.99  | Starter  | 4.80       | Mon:10, Tue:5, Wed:1, Thu:15, Fri:3, Sat:5, Sun:10
Tiramisu           | $7.99  | Dessert  | 4.80       | Mon:15, Tue:20, Wed:25, Thu:30, Fri:35, Sat:40, Sun:45
Cheesecake         | $6.99  | Dessert  | 2.67       | Mon:1, Tue:2, Wed:3, Thu:4, Fri:5, Sat:6, Sun:7

📊 Analysis of Popular Items:
Item               | Category | Avg Rating | Total Sales | Popularity Score
---------------------------------------------------------------------------
Chicken Parmigiana | Main     | 4.73       | 175         | 123.93
Fish and Chips     | Main     | 4.80       | 140         | 103.20
Margherita Pizza   | Main     | 4.17       | 560         | 352.67
Caesar Salad       | Starter  | 4.63       | 245         | 165.53
Garlic Bread       | Starter  | 4.80       | 49          | 48.60
Tiramisu           | Dessert  | 4.80       | 210         | 145.20
Cheesecake         | Dessert  | 2.67       | 28          | 27.47

🔍 Identification of Underrated Items:
Item         | Category | Avg Rating | Total Sales
--------------------------------------------------
Garlic Bread | Starter  | 4.80       | 49

❌ Identification of Unprofitable Items:
Item       | Category | Avg Rating | Total Sales
------------------------------------------------
Cheesecake | Dessert  | 2.67       | 28
```


## Data Structure
The CSV file must have the following structure:

| Field          | Description                                         | Example Value         |
|----------------|-----------------------------------------------------|-----------------------|
| item           | Name of the menu item                               | Chicken Parmigiana    |
| price          | Price of the item (up to 2 decimal places)          | 19.99                 |
| category       | Category of the item (e.g., Main, Starter)          | Main                  |
| ratings        | Comma-separated ratings                             | 4.5,4.7,5.0           |
| sales_per_day  | Comma-separated sales for each day of the week      | 10,15,20,25,30,35,40  |


## Example CSV:

```csv
item,price,category,ratings,sales_per_day
Chicken Parmigiana,19.99,Main,"4.5,4.7,5.0","10,15,20,25,30,35,40"
Fish and Chips,18.99,Main,"4.8,4.9,4.7","5,10,15,20,25,30,35"
Margherita Pizza,15.99,Main,"4.0,4.2,4.3","50,60,70,80,90,100,110"
Caesar Salad,9.99,Starter,"4.5,4.6,4.8","20,25,30,35,40,45,50"
Garlic Bread,6.99,Starter,"4.8,4.9,4.7","10,5,1,15,3,5,10"
Tiramisu,7.99,Dessert,"4.7,4.8,4.9","15,20,25,30,35,40,45"
Cheesecake,6.99,Dessert,"2.5,2.7,2.8","1,2,3,4,5,6,7"
```

## Contributing
We welcome contributions! Here’s how you can help:

Fork the Repository: Create your own fork of the project.
Make Changes: Implement new features, fix bugs, or improve documentation.
Submit a Pull Request: Describe your changes and submit them for review.

## Guidelines
Follow the existing coding style (PEP 8).
Write clear commit messages and include tests if applicable.
Ensure your changes do not break existing functionality.

## License
This project is licensed under the MIT License . See the LICENSE file for details.
