import time
import math

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def main():
    total_times = []

    for round_num in range(1, 11):  # 10 rounds
        start_time = time.time_ns()
        factorial(50)
        factorial(100)
        factorial(200)
        end_time = time.time_ns()

        elapsed = end_time - start_time
        total_times.append(elapsed)
        print(f"Round {round_num}: Time Taken = {elapsed} ns")

    avg_time = sum(total_times) / len(total_times)
    print(f"\nTotal Times per Round: {sum(total_times)} ns")
    print(f"Average Time: {avg_time} ns")

if __name__ == "__main__":
    print("=== Non-Multithreading Factorial Test ===")
    main()


