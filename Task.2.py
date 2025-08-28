# Task 2: Write and Append Data to a File

# Step 1: Take user input and write to a file
data = input("Enter text to write to the file: ")
with open("output.txt", "w") as f:
    f.write(data + "\n")
print("Data successfully written to output.txt.")

# Step 2: Append additional data to the same file
append_data = input("Enter additional text to append: ")
with open("output.txt", "a") as f:
    f.write(append_data + "\n")
print("Data successfully appended.")

# Step 3: Read and display the final content of the file
print("\nFinal content of output.txt:")
with open("output.txt", "r") as f:
    content = f.read()
    print(content)
