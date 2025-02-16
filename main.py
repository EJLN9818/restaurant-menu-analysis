import csv
import os
from typing import Dict, List, Optional


# ---------------------- ASCII Art ----------------------
def ascii_art():
    """Display ASCII Art."""
    art = r'''
             ('-.                           .-') _  
            _( OO)                        ( OO ) ) 
            (,------.     ,--. ,--.     ,--./ ,--,'  
            |  .---' .-')| ,| |  |.-') |   \ |  |\  
            |  |    ( OO |(_| |  | OO )|    \|  | ) 
           (|  '--. | `-'|  | |  |`-' ||  .     |/  
            |  .--' ,--. |  |(|  '---.'|  |\    |   
            |  `---.|  '-'  / |      | |  | \   |   
            `------' `-----'  `------' `--'  `--'   
    '''
    print(art)


# ---------------------- Class MenuItem ----------------------
class MenuItem:
    """Represents a menu item with attributes and sales data."""
    def __init__(self, item: str, price: float, category: str, ratings: str, sales_per_day: str):
        self.item = item
        self.price = price
        self.category = category
        
        # Validate ratings
        self.ratings: List[float] = [float(r) for r in ratings.split(',')]
        if not self.ratings:
            raise ValueError(f"Ratings cannot be empty for item '{item}'.")
        
        # Validate sales_per_day
        days_of_week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        sales_values = sales_per_day.split(',')
        if len(sales_values) != 7:
            raise ValueError(f"Sales per day must have exactly 7 values for item '{item}'.")
        self.sales_per_day: Dict[str, int] = {day: int(sales) for day, sales in zip(days_of_week, sales_values)}
    
    def average_rating(self) -> float:
        """Calculate average rating with error handling for empty lists."""
        return sum(self.ratings) / len(self.ratings) if self.ratings else 0.0


# ---------------------- Float Precision Validator ----------------------
def validate_float_precision(value: float, max_decimals: int = 2) -> bool:
    """
    Validate that a floating-point number has at most `max_decimals` decimal places.
    Raises ValueError if the precision exceeds the allowed limit.
    
    Args:
        value (float): The floating-point number to validate.
        max_decimals (int): Maximum allowed decimal places.
        
    Returns:
        bool: True if the value is valid.
        
    Raises:
        ValueError: If the value exceeds the allowed decimal precision.
    """
    # Convert the value to string and split by the decimal point
    str_value = f"{value:.{max_decimals + 1}f}"  # Ensure enough precision for checking
    _, fractional_part = str_value.split('.')
    
    # Check the length of the fractional part
    if len(fractional_part.rstrip('0')) > max_decimals:
        raise ValueError(f"Value {value} exceeds the allowed {max_decimals} decimal places.")
    
    return True


# ---------------------- CSV Handling ----------------------
def handle_csv_creation(default_filename: str) -> Optional[str]:
    """
    Handle CSV file creation logic with user prompts.
    
    Returns:
        Optional[str]: The path to the CSV file to use, or None if the program should terminate.
    """
    while True:
        # Check if the default file exists
        if os.path.exists(default_filename):
            use_existing = input(
                f"⚠️  The file '{default_filename}' exists. Use it? (yes/no): "
            ).strip().lower()
            
            if use_existing == 'yes':
                return default_filename  # Use the existing file
            
            # If not using the existing file, ask what to do next
            print("What would you like to do instead?")
            choice = input(
                "1. Generate a sample CSV\n"
                "2. Exit\n"
                "Enter your choice (1/2): "
            ).strip()
            
            if choice == '1':
                # Confirm before overwriting
                confirm = input(
                    f"⚠️  This will overwrite '{default_filename}'. Proceed? (yes/no): "
                ).strip().lower()
                if confirm == 'yes':
                    generate_sample_csv(default_filename)
                    print(f"✅ Sample CSV created: {default_filename}")
                    return default_filename
                else:
                    print("❌ Overwrite canceled.")
                    continue  # Retry
            
            elif choice == '2':
                print("🛑 Program terminated by user.")
                return None  # Exit the program
            
            else:
                print("❌ Invalid choice. Please enter 1 or 2.")
                continue  # Retry
        
        else:
            # File does not exist
            print(f"⚠️  The file '{default_filename}' does not exist.")
            generate = input(
                "Would you like to generate a sample CSV? (yes/no): "
            ).strip().lower()
            
            if generate == 'yes':
                generate_sample_csv(default_filename)
                print(f"✅ Sample CSV created: {default_filename}")
                return default_filename
            
            else:
                print("🛑 Program terminated: No CSV file available.")
                return None


def validate_csv_structure(filename: str) -> bool:
    """Validate CSV structure with detailed error reporting."""
    required_fields: List[str] = ['item', 'price', 'category', 'ratings', 'sales_per_day']
    
    try:
        with open(filename, 'r', encoding='utf-8-sig') as file:
            reader = csv.DictReader(file)
            
            if not reader.fieldnames:
                print(f"❌ Error: '{filename}' is empty or malformed.")
                return False
                
            missing_fields = [field for field in required_fields 
                             if field not in reader.fieldnames]
            
            if missing_fields:
                print(f"❌ Invalid CSV structure. Missing columns: {', '.join(missing_fields)}")
                print(f"Required columns: {', '.join(required_fields)}")
                return False
                
            return True
            
    except FileNotFoundError:
        print(f"❌ Critical Error: File '{filename}' not found after creation.")
        return False
    except Exception as e:
        print(f"❌ Unexpected error during CSV validation: {str(e)}")
        return False


def generate_sample_csv(filename: str) -> None:
    """Generate a sample CSV file with realistic data."""
    sample_data: List[List[str]] = [
        ["item", "price", "category", "ratings", "sales_per_day"],
        ["Chicken Parmigiana", "19.99", "Main", "4.5,4.7,5.0", "10,15,20,25,30,35,40"],
        ["Fish and Chips", "18.99", "Main", "4.8,4.9,4.7", "5,10,15,20,25,30,35"],
        ["Margherita Pizza", "15.99", "Main", "4.0,4.2,4.3", "50,60,70,80,90,100,110"],
        ["Caesar Salad", "9.99", "Starter", "4.5,4.6,4.8", "20,25,30,35,40,45,50"],
        ["Garlic Bread", "6.99", "Starter", "4.8,4.9,4.7", "10,5,1,15,3,5,10"],  # Underrated item
        ["Tiramisu", "7.99", "Dessert", "4.7,4.8,4.9", "15,20,25,30,35,40,45"],
        ["Cheesecake", "6.99", "Dessert", "2.5,2.7,2.8", "1,2,3,4,5,6,7"],  # Unprofitable item
    ]
    
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(sample_data)


# ---------------------- Data Processing ----------------------
def load_data_from_csv(filename: str) -> Optional[Dict[str, MenuItem]]:
    """Load and validate menu items from CSV."""
    menu_items: Dict[str, MenuItem] = {}
    
    try:
        with open(filename, 'r', encoding='utf-8-sig') as file:
            reader = csv.DictReader(file)
            
            for row_num, row in enumerate(reader, 1):
                try:
                    # Validate price precision before creating MenuItem
                    price = float(row['price'])
                    validate_float_precision(price)
                    
                    # Create MenuItem instance
                    item = MenuItem(
                        row['item'],
                        price,
                        row['category'],
                        row['ratings'],
                        row['sales_per_day']
                    )
                    menu_items[row['item']] = item
                    
                except (KeyError, ValueError) as e:
                    print(f"❌ Data Error in row {row_num}: {str(e)}")
                    print(f"Problematic row: {row}")
                    return None
                    
        return menu_items
        
    except Exception as e:
        print(f"❌ Critical Load Error: {str(e)}")
        return None


# ---------------------- Display Logic ----------------------
def display_menu(menu_items: Dict[str, MenuItem]) -> None:
    """Display menu in a dynamic table format."""
    headers: List[str] = ["Item", "Price", "Category", "Avg Rating", "Sales/Day"]
    rows: List[List[str]] = [
        [
            item.item,
            f"${item.price:.2f}",  # Always show two decimal places (ISO 80000-1 compliance)
            item.category,
            f"{item.average_rating():.2f}",
            ", ".join(f"{k}:{v}" for k, v in item.sales_per_day.items())
        ] for item in menu_items.values()
    ]
    # Dynamic column sizing
    col_widths: List[int] = [
        max(len(str(row[i])) for row in [headers] + rows) 
        for i in range(len(headers))
    ]
    
    # Header
    header = " | ".join(f"{h:<{w}}" for h, w in zip(headers, col_widths))
    print(header)
    print("-" * (sum(col_widths) + 3 * (len(headers) - 1)))
    
    # Rows
    for row in rows:
        print(" | ".join(f"{cell:<{w}}" for cell, w in zip(row, col_widths)))


# ---------------------- Additional Analyses ----------------------
def analyze_popular_items(menu_items: Dict[str, MenuItem]) -> None:
    """Analyze and display the most popular items based on sales and ratings."""
    print("\n📊 Analysis of Popular Items:")
    headers = ["Item", "Category", "Avg Rating", "Total Sales", "Popularity Score"]
    rows = []

    for item in menu_items.values():
        total_sales = sum(item.sales_per_day.values())
        avg_rating = item.average_rating()
        popularity_score = (total_sales * 0.6) + (avg_rating * 10 * 0.4)
        rows.append([
            item.item,
            item.category,
            f"{avg_rating:.2f}",
            total_sales,
            f"{popularity_score:.2f}"
        ])

    # Dynamic column sizing
    col_widths = [
        max(len(str(row[i])) for row in [headers] + rows) 
        for i in range(len(headers))
    ]

    # Header
    header = " | ".join(f"{h:<{w}}" for h, w in zip(headers, col_widths))
    print(header)
    print("-" * (sum(col_widths) + 3 * (len(headers) - 1)))

    # Rows
    for row in rows:
        print(" | ".join(f"{cell:<{w}}" for cell, w in zip(row, col_widths)))


def identify_underrated_items(menu_items: Dict[str, MenuItem]) -> None:
    """Identify items with high ratings but low sales."""
    print("\n🔍 Identification of Underrated Items:")
    headers = ["Item", "Category", "Avg Rating", "Total Sales"]
    rows = []

    for item in menu_items.values():
        total_sales = sum(item.sales_per_day.values())
        avg_rating = item.average_rating()
        if avg_rating >= 4.5 and total_sales < 50:  # Thresholds for underrated items
            rows.append([
                item.item,
                item.category,
                f"{avg_rating:.2f}",
                total_sales
            ])

    if not rows:
        print("No underrated items found.")
        return

    # Dynamic column sizing
    col_widths = [
        max(len(str(row[i])) for row in [headers] + rows) 
        for i in range(len(headers))
    ]

    # Header
    header = " | ".join(f"{h:<{w}}" for h, w in zip(headers, col_widths))
    print(header)
    print("-" * (sum(col_widths) + 3 * (len(headers) - 1)))

    # Rows
    for row in rows:
        print(" | ".join(f"{cell:<{w}}" for cell, w in zip(row, col_widths)))


def identify_unprofitable_items(menu_items: Dict[str, MenuItem]) -> None:
    """Identify items with low sales and low ratings."""
    print("\n❌ Identification of Unprofitable Items:")
    headers = ["Item", "Category", "Avg Rating", "Total Sales"]
    rows = []

    for item in menu_items.values():
        total_sales = sum(item.sales_per_day.values())
        avg_rating = item.average_rating()
        if avg_rating < 3.5 and total_sales < 30:  # Thresholds for unprofitable items
            rows.append([
                item.item,
                item.category,
                f"{avg_rating:.2f}",
                total_sales
            ])

    if not rows:
        print("No unprofitable items found.")
        return

    # Dynamic column sizing
    col_widths = [
        max(len(str(row[i])) for row in [headers] + rows) 
        for i in range(len(headers))
    ]

    # Header
    header = " | ".join(f"{h:<{w}}" for h, w in zip(headers, col_widths))
    print(header)
    print("-" * (sum(col_widths) + 3 * (len(headers) - 1)))

    # Rows
    for row in rows:
        print(" | ".join(f"{cell:<{w}}" for cell, w in zip(row, col_widths)))


# ---------------------- Main Flow ----------------------
def main() -> None:
    ascii_art()

    sample_csv = 'menu.csv'
    
    # 1. File Handling
    if not handle_csv_creation(sample_csv):
        print("🛑 Program terminated: CSV file required.")
        return
        
    # 2. Structure Validation (Single Source of Truth)
    if not validate_csv_structure(sample_csv):
        print("🛑 Program terminated: Invalid CSV structure.")
        return
    
    # 3. Data Loading (No redundant validation)
    menu_data = load_data_from_csv(sample_csv)
    if not menu_data:
        print("🛑 Program terminated: Failed to load valid data.")
        return
    
    # 4. Display and Reporting
    display_menu(menu_data)
    
    # Additional analyses
    analyze_popular_items(menu_data)
    identify_underrated_items(menu_data)
    identify_unprofitable_items(menu_data)

if __name__ == "__main__":
    main()
