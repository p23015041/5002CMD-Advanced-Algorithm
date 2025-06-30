#---------- Q1 ----------#

import random

# Generate 12-digit Malaysian IC number
def generate_ic():
    # YYMMDD Birthdate
    year = random.randint(0, 25)
    month = random.randint(1, 12)
    day = random.randint(1, 31)

    birth = f"{year:02d}{month:02d}{day:02d}"

    # State code
    state_codes = ['01', '02', '03', '04', '05', '06', '07', '08', '09',
                   '10', '11', '12', '13', '14', '15', '16', '21', '22',
                   '23', '24', '25', '26', '27', '28', '29']
    state = random.choice(state_codes)

    # Serial number
    serial = f"{random.randint(0, 9999):04d}"

    return birth + state + serial

# Hash function using folding method
def fold_hash(ic, table_size):
    group = 4
    total = 0
    for i in range(0, len(ic), group):
        total += int(ic[i:i+group])

    # Return hash index using modulo
    return total % table_size

# Build hash table and show entries
def build_and_print_table(size, ic_list, label):
    table = [[] for _ in range(size)]
    collisions = 0

    for ic in ic_list:
        index = fold_hash(ic, size)
        if table[index]:
            collisions += 1
        table[index].append(ic)

    # Display hash table contents
    print(f"\nHash Table with size {size}:")
    for i in range(size):
        if table[i]:
            row = f"table[{i}] --> " + " --> ".join(table[i])
        else:
            row = f"table[{i}]"
        print(row)

    # Calculate and return collision rate
    collision_rate = (collisions / len(ic_list)) * 100
    return collision_rate

# Main Function
def main():
    ic_list = [generate_ic() for _ in range(1000)]

    small_size = 1009
    big_size = 3001

    collision_small = build_and_print_table(small_size, ic_list, "Smaller Table")
    collision_big = build_and_print_table(big_size, ic_list, "Bigger Table")

    print(f"\nCollision Rate for Smaller Hash Table: {collision_small:.2f} %")
    print(f"Collision Rate for Bigger Hash Table: {collision_big:.2f} %")
    print("\nProcess finished with exit code 0")

# Run the program
if __name__ == "__main__":
    main()
