import threading
import time
import math

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def main():
    total_times = []

    for round_num in range(1, 11):
        # Record global start time
        start_time = time.time_ns()

        # Create threads one by one
        t1 = threading.Thread(target=factorial, args=(50,))
        t2 = threading.Thread(target=factorial, args=(100,))
        t3 = threading.Thread(target=factorial, args=(200,))

        # Start threads one by one
        t1.start()
        t2.start()
        t3.start()

        # Join threads one by one
        t1.join()
        t2.join()
        t3.join()

        # Record global end time
        end_time = time.time_ns()

        elapsed = end_time - start_time
        total_times.append(elapsed)

        print(f"Round {round_num}: Time Taken = {elapsed} ns")

    avg_time = sum(total_times) / len(total_times)
    print(f"\nTotal Times per Round: {sum(total_times)} ns")
    print(f"Average Time (Multithreading): {avg_time} ns")

if __name__ == "__main__":
    print("=== Multithreading Factorial Test ===")
    main()
