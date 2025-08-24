# File Objects

# Reading files
with open("test.txt", "r") as f:
    print(f.name)
    print(f.mode)

    # Looping through every line of a file
    for line in f:
        print(line, end="")

    # Every time you inflict a read function, the file pointer goes to next line
    # Move file pointer to beginning
    f.seek(0)

    # Reading the first 100 characters
    f_contents = f.read(100)
    print(f_contents)

    # Readlines return a list of lines in the file
    f_lines = f.readlines()
    print(f_lines)

    f.seek(0)

    # Show current position
    size_to_read = 10
    f_contents = f.read(size_to_read)
    print(f.tell())

    f.seek(0)
    f_contents = f.read(size_to_read)
    # Chunking
    while len(f_contents) > 0:
        print(f_contents, end="*")
        f_contents = f.read(size_to_read)


# Writing files
# If the file exists, it overwrites;
# If it doesn't exists, it creates a new file.
with open("test2.txt", "w") as f:
    f.write("Test")
    f.seek(0)
    f.write("R")  # Rest

# Copying text files
with open("test.txt", "r") as rf:
    with open("test_copy.txt", "w") as wf:
        for line in rf:
            wf.write(line)

# Copying image files
# mode change to rb, wb (binary)
with open("cat.jpeg", "rb") as rf:
    with open("cat_copy.jpeg", "wb") as wf:
        for line in rf:
            wf.write(line)

# Chunk files for memory efficiency, performance, and reliability
with open("cat.jpeg", "rb") as rf:
    with open("cat_chunk_copy.jpeg", "wb") as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)
