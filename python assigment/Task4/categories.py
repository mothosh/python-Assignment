def product_categories():
    # i - Create set with duplicates (duplicates will be removed automatically)
    categories = {"Electronics", "Clothing", "Groceries", "Electronics", "Furniture", "Toys", "Clothing"}

    # ii - Display set
    print(f"Initial Categories (duplicates removed): {categories}")

    # iii - Add new category using add()
    categories.add("Books")
    print(f"After adding Books: {categories}")

    # iv - Remove one category using remove()
    categories.remove("Toys")
    print(f"After removing Toys: {categories}")

    # v - Display final set
    print(f"Final Categories: {categories}")

    # vi - Explanation
    print("\nExplanation: A set automatically removes duplicate values and stores only unique items. This helps the company maintain a clean list of product categories without repetition.")

product_categories()
