# Step 1: Create and write to input.txt (optional if already exists)
with open("input.txt", "w") as file:
    file.write("Learning Python is fun and rewarding.\n")
    file.write("It helps you build software projects.\n")
    file.write("Python is great for automation.\n")
    file.write("Data science uses Python extensively.\n")
    file.write("Practice makes perfect with Python.\n")

# Step 2: Read the contents of input.txt
with open("input.txt", "r") as file:
    content = file.read()

# Step 3: Process content
word_count = len(content.split())
uppercase_content = content.upper()

# Step 4: Write processed content to output.txt
with open("output.txt", "w") as file:
    file.write(uppercase_content)
    file.write(f"\n\nTotal Word Count: {word_count}\n")

# Step 5: Print success message
print("✅ output.txt has been created successfully with processed text and word count.")



def modify_file_content(content):
    """
    Modify the file content as needed.
    In this example, we convert it to uppercase.
    """
    return content.upper()

def main():
    # Ask user for the input file name
    filename = input("Enter the name of the file you want to read: ")

    try:
        # Try to open and read the file
        with open(filename, 'r') as file:
            content = file.read()

        # Modify content
        modified_content = modify_file_content(content)

        # Define new file name
        new_filename = "modified_" + filename

        # Write modified content to a new file
        with open(new_filename, 'w') as new_file:
            new_file.write(modified_content)

        print(f"Modified content has been written to '{new_filename}'.")

    except FileNotFoundError:
        print("Error: File not found. Please check the filename and try again.")
    except IOError:
        print("Error: Could not read the file due to an I/O error.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the program
if __name__ == "__main__":
    main()
