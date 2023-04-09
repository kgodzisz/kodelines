import os

directory = "/app/" # Change it to the correct path.

total_lines = 0
for filename in os.listdir(directory):
    if (filename.endswith(".txt")) or (filename.endswith(".py")) or (filename.endswith(".log")): # Change it to the correct file extension.
        with open(os.path.join(directory, filename), "r") as file:
            lines = file.readlines()
            non_empty_lines = [line.strip() for line in lines if line.strip()]
            total_lines += len(non_empty_lines)

print("The number of lines of code in the folder {}: {}".format(directory, total_lines))
