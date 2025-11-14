import time
from hashtable import HashTable
from products import PRODUCTS

# Baby Products entity class

class BabyProduct:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"[{self.product_id}] {self.name} - ${self.price:.2f} x{self.quantity}"

# INVENTORY SYSTEM

class InventorySystem:
    def __init__(self):
        self.hash_table = HashTable(capacity=10)
        self.array_storage = [] # array storage for comparison
        self.preload_data() # loading predefined data

    def preload_data(self):
        for pid, name, price, qty in PRODUCTS:
            product = BabyProduct(pid, name, price, qty)
            self.hash_table.insert(product.product_id, product)
            self.array_storage.append(product)

    def insert_product(self):
        pid = input("Enter Product ID: ")

        # Check if product ID already exists
        if self.hash_table.search(pid):
            print("\nProduct already exists. Please use [ Edit Product ] function instead")
            return
        
        name = input("Enter Product Name: ")
        price = float(input("Enter Price: "))
        qty = int(input("Enter Quantity: "))
        prod = BabyProduct(pid, name, price, qty)
        self.hash_table.insert(pid, prod)
        self.array_storage.append(prod)  # Append if not found
        
        print("\nProduct inserted successfully!")

    def edit_product(self):
        pid = input("Enter Product ID to edit: ")
        product = self.hash_table.search(pid)
        if product:
            name = input(f"New Name ({product.name}): ")
            price = input(f"New Price ({product.price}): ")
            qty = input(f"New Quantity ({product.quantity}): ")
            edited = BabyProduct(pid, name, float(price), int(qty))
            self.hash_table.insert(pid, edited)

            # Update in array_storage as well
            for i, p in enumerate(self.array_storage):
                if p.product_id == pid:
                    self.array_storage[i] = edited
                    break
            
            print("\nProduct updated successfully.")
        else:
            print("\nProduct not found.")

    def delete_product(self):
        pid = input("Enter Product ID to delete: ")
        if self.hash_table.delete(pid):
            # Remake array_storage without the deleted product
            # p = product
            self.array_storage = [p for p in self.array_storage if p.product_id != pid]
            print("Product deleted.")
        else:
            print("Product not found.")

    def display_products(self):
        print("\n--- All Products in Hash Table ---")
        self.hash_table.display()
        print("\n--- All Products in Array ---")
        for p in self.array_storage:
            print(p)

    def search_array(self, pid):
        for product in self.array_storage:
            if product.product_id == pid:
                return product
        return None

    def search_product(self):
        pid = input("Enter Product ID to search: ")
        
        # Hash Table Search
        start_hash = time.perf_counter()
        product_hash = self.hash_table.search(pid)
        end_hash = time.perf_counter()
        
        # Array Search
        start_arr = time.perf_counter()
        product_arr = self.search_array(pid)
        end_arr = time.perf_counter()
        
        if product_hash:
            print("\nProduct found:", product_hash)
        else:
            print("\nProduct not found in Hash Table.")
        
        print("\n--- Performance Comparison ---")
        print(f"Hash Table Search Time: {(end_hash - start_hash):.10f} ms")
        print(f"Array Search Time: {(end_arr - start_arr):.10f} ms")
        
        if not product_hash and not product_arr:
            print("\nProduct not found in both structures.")

    def compare_all_searches(self):
        if not self.array_storage:
            print("No products to search.")
            return
        
        hash_times = []
        arr_times = []
        
        # Hash Table: Search all products
        for product in self.array_storage:
            start = time.perf_counter()
            self.hash_table.search(product.product_id)
            end = time.perf_counter()

            search_time = end - start
            hash_times.append(search_time)
        
        # Array: Search all products
        for product in self.array_storage:
            start = time.perf_counter()
            self.search_array(product.product_id)
            end = time.perf_counter()

            search_time = end - start
            arr_times.append(search_time)
        
        total_hash_time = sum(hash_times) 
        total_arr_time = sum(arr_times) 
        num_products = len(self.array_storage)
        
        print(f"\n--- Performance Comparison for All {num_products} Products ---\n")
        print(f"Total Hash Table Search Time: {total_hash_time:.10f} ms")
        print(f"Total Array Search Time: {total_arr_time:.10f} ms\n")
        print(f"Average Hash Table Search Time: {total_hash_time / num_products:.10f} ms per product")
        print(f"Average Array Search Time: {total_arr_time / num_products:.10f} ms per product")

    def menu(self):
        choice = ''
        while choice != '7':
            print("\n===== Baby Shop Inventory System =====")
            print("1. Insert Product")
            print("2. Edit Product")
            print("3. Delete Product")
            print("4. Search Product")
            print("5. Compare All Searches Performance")
            print("6. Display All Products")
            print("7. Exit")
            choice = input("Enter choice: ")

            if choice == '1':
                self.insert_product()
            elif choice == '2':
                self.edit_product()
            elif choice == '3':
                self.delete_product()
            elif choice == '4':
                self.search_product()
            elif choice == '5':
                self.compare_all_searches()
            elif choice == '6':
                self.display_products()
            elif choice == '7':
                print("Exiting system... Goodbye!")
                break
            else:
                print("Invalid choice. Try again.")

# ==============================
# MAIN FUNCTION
# ==============================
def main():
    system = InventorySystem()
    system.menu()


if __name__ == "__main__":
    main()