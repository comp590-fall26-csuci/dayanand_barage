import os

def fib_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fib_recursive(n - 1) + fib_recursive(n - 2)

def save_fibonacci_to_file(n, directory, filename):
    # 1. Create the directory if it doesn't exist
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    # 2. Define the full path
    file_path = os.path.join(directory, filename)
    
    # 3. Generate the numbers recursively and store them in a list
    fib_numbers = [fib_recursive(i) for i in range(n)]
    
    # 4. Reverse the list
    fib_numbers.reverse()
    
    # 5. Write the reversed sequence to the file
    with open(file_path, "w") as f:
        for num in fib_numbers:
            f.write(f"{num}\n")
            
    print(f"Success! {n} numbers written to {file_path} in reverse order.")

# Run:
save_fibonacci_to_file(25, "output", "fibonacci-25-rec.txt")
