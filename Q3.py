#---------- Q3 -----------#

import threading
import time
import random

# Simulate task generate 100 random numbers
def generate_numbers():
    return [random.randint(0, 10000) for _ in range(100)]

# Time using multithreading
def time_multithreading():
    results = [None, None, None]
    threads = []
    start = time.time_ns()

    # Create and start 3 threads
    for i in range(3):
        t = threading.Thread(target=lambda idx=i: results.__setitem__(idx, generate_numbers()))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    end = time.time_ns()
    return end - start

# Time without multithreading
def time_non_multithreading():
    start = time.time_ns()
    generate_numbers()
    generate_numbers()
    generate_numbers()
    end = time.time_ns()
    return end - start

# Table row formatter
def format_row(c1, c2, c3, c4):
    return f"| {str(c1).center(6)} | {str(c2).center(24)} | {str(c3).center(27)} | {str(c4).center(20)} |"

# Collect timing data
rounds = 10
multi_times = []
non_multi_times = []
diffs = []

for _ in range(rounds):
    mt = time_multithreading()
    nt = time_non_multithreading()
    diff = mt - nt
    multi_times.append(mt)
    non_multi_times.append(nt)
    diffs.append(diff)

# Round-by-round table result
print("Round-by-Round Performance Comparison:")
print("+" + "-"*8 + "+" + "-"*26 + "+" + "-"*29 + "+" + "-"*22 + "+")
print("| Round | Multithreading Time (ns) | Non-Multithreading Time (ns) | Difference (ns)     |")
print("+" + "-"*8 + "+" + "-"*26 + "+" + "-"*29 + "+" + "-"*22 + "+")

for i in range(rounds):
    print(format_row(i + 1, multi_times[i], non_multi_times[i], diffs[i]))

print("+" + "-"*8 + "+" + "-"*26 + "+" + "-"*29 + "+" + "-"*22 + "+")

# Summary of results
total_mt = sum(multi_times)
total_nt = sum(non_multi_times)
total_diff = total_mt - total_nt

avg_mt = total_mt / rounds
avg_nt = total_nt / rounds
avg_diff = avg_mt - avg_nt

# Print results
print("\nSummary of Results:")
print("+" + "-"*14 + "+" + "-"*26 + "+" + "-"*29 + "+" + "-"*22 + "+")
print("|  Metric      | Multithreading           | Non-Multithreading          | Difference           |")
print("+" + "-"*14 + "+" + "-"*26 + "+" + "-"*29 + "+" + "-"*22 + "+")
print(format_row("Total Time  ", total_mt, total_nt, total_diff))
print(format_row("Average Time", f"{avg_mt:.1f}", f"{avg_nt:.1f}", f"{avg_diff:.1f}"))
print("+" + "-"*14 + "+" + "-"*26 + "+" + "-"*29 + "+" + "-"*22 + "+")
