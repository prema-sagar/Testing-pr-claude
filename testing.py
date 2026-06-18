def calculate_total(price, quantity):
    """Calculate total amount."""
    return price * quantity


def main():
    total = calculate_total(100, 2)
    print(f"Total Amount: {total}")


if __name__ == "__main__":
    main()