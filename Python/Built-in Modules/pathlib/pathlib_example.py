# Reference: https://www.youtube.com/watch?v=yxa-DJuuTBI
from pathlib import Path

# Get current directory
print(Path.cwd())

# Show all files and directories in current directory
for p in Path().iterdir():
    print(p)

# directory / file objects
my_dir = Path("Directory_1")
my_file = Path("file_1.txt")

# Get file / directory name
print(my_dir.name)
print(my_file.name)

# Get file extensions. Null for directory
print(my_dir.suffix)
print(my_file.suffix)

# Get file name without extensions
print(my_dir.stem)
print(my_file.stem)

# Creating new file under directory_1
new_file1 = my_dir / "new_file1.txt"
new_file2 = my_dir.joinpath("new_file2.txt")

# Check if file / directory exists
print(new_file1.exists())

# Get parent directory
print(my_dir.parent)
print(my_file.parent)
print(new_file1.parent.parent)

# Get absolute path
print(my_dir.absolute())

# Use resolve when we want to find absolute path of current file, current dir (.) or parent dir (..)
p1 = Path(__file__).resolve()
print(p1)
p2 = Path(".").resolve()
print(p2)
p3 = Path("..").resolve()
print(p3)

# Use expanduser when the path involves root folder
p4 = Path("~/dotfiles").expanduser()
print(p4)

# Or home
dotfiles = Path.home() / "dotfiles" / "settings/VSCode-Settings.json"
print(dotfiles)

# Searching
for p in dotfiles.glob("*.json"):
    print(p)

try:
    with open(dotfiles) as f:
        print(f.read())

except FileNotFoundError:
    print("File not found.")

# Make new directory
direc1 = Path("TempDir")
direc1.mkdir()

# Remove directory
direc1.rmdir()

# Make sub directory inside directory that not exists yet
direc2 = Path("TempDir/Subdir")
direc2.mkdir(parents=True)

# Create file
file = Path("TempFile.txt")
file.touch()

# Rename a file
file.rename("tempfile.txt")

# Remove a file
file.unlink()
