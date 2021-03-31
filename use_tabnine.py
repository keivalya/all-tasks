import os
import sys

# count lines of code in the given directory, separated by file extensions
def main(directory):
    line_count = {}
    for filename in os.listdir(directory):
        _, ext = os.path.splitext(filename)
        if ext not in line_count:
            line_count[ext] = 0
        for line in open(os.path.join(directory, filename)):
            line_count[ext] += 1
    for ext, count in line_count.items():
        print("Extension {} had {} lines".format(ext, count))

if __name__ == "__main__":
    main(sys.argv[1])