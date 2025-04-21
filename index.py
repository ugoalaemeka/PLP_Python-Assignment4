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
