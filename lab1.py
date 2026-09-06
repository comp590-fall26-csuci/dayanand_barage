import os

def save_fibonacci_to_file(n, directory, filename):
    # 1. Create the directory if it doesn't exist
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    # 2. Define the full path
    file_path = os.path.join(directory, filename)
    
    # 3. Generate and write the numbers
    a, b = 0, 1
    with open(file_path, "w") as f:
        for i in range(n):
            f.write(f"{a}\n")
            a, b = b, a + b
            
    print(f"Success! {n} numbers written to {file_path}")

# Run:
save_fibonacci_to_file(25, "output", "fibonacci-25.txt")

