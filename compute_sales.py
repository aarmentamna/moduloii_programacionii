"""
This module calculates the total cost of sales .
"""

import json
import sys
import time


def load_json_file(filename):
    """
    Load JSON data from the specified file.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: File '{filename}' is not valid JSON.")
        return None


def compute_total_cost(price_catalogue, sales_record):
    """
    Compute the total cost of sales with catalogue and sales records.
    """
    total_cost = 0
    for sale in sales_record:
        product_name = sale["Product"]
        quantity = sale["Quantity"]
        for product in price_catalogue:
            if product["title"] == product_name:
                price = product["price"]
                total_cost += price * quantity
                break
    return total_cost


def main():
    """
    Main function to execute the program.
    """
    if len(sys.argv) != 3:
        print("Usage: python computeSales.py price.json salesRecord.json")
        sys.exit(1)

    start_time = time.time()

    price_catalogue_file = sys.argv[1]
    sales_record_file = sys.argv[2]

    price_catalogue = load_json_file(price_catalogue_file)
    if price_catalogue is None:
        sys.exit(1)

    sales_record = load_json_file(sales_record_file)
    if sales_record is None:
        sys.exit(1)

    total_cost = compute_total_cost(price_catalogue, sales_record)

    end_time = time.time()
    elapsed_time = end_time - start_time

    # Output results to screen
    print(f"Total cost of sales: ${total_cost}")
    print(f"Time elapsed: {elapsed_time} seconds")

    # Output results to file
    with open("SalesResults.txt", "w", encoding="utf-8") as result_file:
        result_file.write(f"Total cost of sales: ${total_cost}\n")
        result_file.write(f"Time elapsed: {elapsed_time} seconds\n")


if __name__ == "__main__":
    main()
