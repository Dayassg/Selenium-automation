from pathlib import Path

path = Path.cwd()
path_name = Path("Test.txt")


print(path)
print(path_name.exists())
path_name.write_text("This is written using command")
print(path_name.read_text())




