from pathlib import Path

file_path = Path.cwd()/"my_folder"
print(file_path)


file_path.mkdir(exist_ok=True)
new_file_path = file_path / "my_file.txt"
new_file_path.touch()
print(file_path.exists())
print (file_path.exists())