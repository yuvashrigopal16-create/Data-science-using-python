size = int(input("Enter hash table size: "))
hash_table = [None] * size

def insert():
    roll = int(input("Enter Roll Number: "))
    name = input("Enter Student Name: ")
    key = roll % size

    for i in range(size):
        index = (key + i) % size
        if hash_table[index] is None:
            hash_table[index] = [roll, name]
            print("Record inserted successfully")
            return
    print("Hash table is full")

def search():
    roll = int(input("Enter Roll Number to search: "))
    for record in hash_table:
        if record is not None and record != "DELETED":
            if record[0] == roll:
                print("Student Found:", record)
                return
    print("Student not found")

def delete():
    roll = int(input("Enter Roll Number to delete: "))
    for i in range(size):
        record = hash_table[i]
        if record is not None and record != "DELETED":
            if record[0] == roll:
                hash_table[i] = "DELETED"
                print("Record deleted successfully")
                return
    print("Student not found")

def display():
    print("\nHash Table")
    for i in range(size):
        print(i, ":", hash_table[i])

while True:
    print("\n1. Insert")
    print("2. Search")
    print("3. Delete")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        insert()
    elif choice == 2:
        search()
    elif choice == 3:
        delete()
    elif choice == 4:
        display()
    elif choice == 5:
        print("Program terminated")
        break
    else:
        print("Invalid choice")
