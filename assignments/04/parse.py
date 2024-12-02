import re
from collections import Counter

def main():
    
    # Read the CSV file with the product orders
    with open('./csv/orders.csv') as f_in:
        text = f_in.read()

    # Define the regular expression to extract all order numbers
    order_numbers = re.findall(r'Order #(\d+)', text)
    print(f"Order Numbers: {order_numbers}")

    # Define the regular expression to extract all product names
    products = re.findall(r'Product: (\w+)', text)
    print(f"Product Names: {products}")

    # Define the regular expression to extract all prices
    prices = re.findall(r'Price: \$(\d+\.\d{2})', text)
    print(f"Prices: {prices}")

    # Define the regular expression to extract all order dates
    order_dates = re.findall(r'Date: (\d{4}-\d{2}-\d{2})', text)
    print(f"Order Dates: {order_dates}")

    # Find all orders for products priced over $500
    expensive_orders = [p for p, price in zip(products, prices) if float(price) > 500]
    print(f"Expensive Orders (over $500): {expensive_orders}")

    # Change the date format to DD/MM/YYYY
    formatted_dates = [re.sub(r'(\d{4})-(\d{2})-(\d{2})', r'\3/\2/\1', date) for date in order_dates]
    print(f"Formatted Dates: {formatted_dates}")

    # Extract product names that have more than 6 characters
    products_gt_6 = [product for product in products if len(product) > 6]
    print(f"Products with more than 6 characters: {products_gt_6}")

    # Count the occurrence of each product
    product_counts = Counter(products)
    print(f"Product Occurrences: {product_counts}")

    # Extract products with prices ending in .99
    products_ending_99 = [p for p, price in zip(products, prices) if price.endswith('.99')]
    print(f"Products with prices ending in .99: {products_ending_99}")

    # Find the cheapest product
    cheapest_price = min(prices, key=lambda x: float(x))
    cheapest_product = products[prices.index(cheapest_price)]
    print(f"The cheapest product is {cheapest_product} with a price of ${cheapest_price}")

if __name__ == '__main__':
    main()
