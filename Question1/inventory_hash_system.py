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

# INVENTORY SYSTEM (HashTable-only)

class InventoryHashSystem:
	def __init__(self):
		self.hash_table = HashTable(capacity=10)
		self.product_ids = []  # keep ids for benchmarking
		self.preload_data()  # load predefined data

	def preload_data(self):
		for pid, name, price, qty in PRODUCTS:
			product = BabyProduct(pid, name, price, qty)
			self.hash_table.insert(product.product_id, product)
			self.product_ids.append(product.product_id)

	def insert_product(self):
		pid = input("Enter Product ID: ")

		# Check if product ID already exists in hash table
		if self.hash_table.search(pid):
			print("\nProduct already exists. Please use [ Edit Product ] function instead")
			return

		name = input("Enter Product Name: ")
		price = float(input("Enter Price: "))
		qty = int(input("Enter Quantity: "))
		prod = BabyProduct(pid, name, price, qty)
		self.hash_table.insert(pid, prod) # for tracking
		self.product_ids.append(pid)

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
			print("\nProduct updated successfully.")
		else:
			print("\nProduct not found.")

	def delete_product(self):
		pid = input("Enter Product ID to delete: ")
		if self.hash_table.delete(pid):
			# also remove from benchmarking list if present
			self.product_ids = [x for x in self.product_ids if x != pid]
			print("Product deleted.")
		else:
			print("Product not found.")

	def display_products(self):
		print("\n--- All Products in Hash Table ---")
		self.hash_table.display()

	def search_product(self):
		pid = input("Enter Product ID to search: ")

		# Hash Table Search
		start_hash = time.perf_counter()
		product_hash = self.hash_table.search(pid)
		end_hash = time.perf_counter()

		if product_hash:
			print("\nProduct found:", product_hash)
		else:
			print("\nProduct not found in Hash Table.")

		print("\n--- Performance ---")
		print(f"Hash Table Search Time: {(end_hash - start_hash):.9f} ms")

	def compare_all_searches(self):
		if not self.product_ids:
			print("No products to search.")
			return

		hash_times = []

		# Hash Table: Search all products
		for pid in self.product_ids:
			start = time.perf_counter()
			self.hash_table.search(pid)
			end = time.perf_counter()
			hash_times.append(end - start)

		total_hash_time = sum(hash_times)
		num_products = len(self.product_ids)

		print(f"\n--- Hash Table Search Performance for All {num_products} Products ---\n")
		print(f"Total Hash Table Search Time: {total_hash_time:.9f} ms\n")
		print(f"Average Hash Table Search Time: {total_hash_time / num_products:.9f} ms per product")

	def menu(self):
		choice = ''
		while choice != '7':
			print("\n===== Baby Shop Inventory System (Hash Table Only) =====")
			print("1. Insert Product")
			print("2. Edit Product")
			print("3. Delete Product")
			print("4. Search Product")
			print("5. Benchmark All Searches")
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
	system = InventoryHashSystem()
	system.menu()


if __name__ == "__main__":
	main()
