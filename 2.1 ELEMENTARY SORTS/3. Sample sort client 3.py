# Sort the files in a given directory by filename
import os, fnmatch

class FileSorter:
    def sort():
        listOfPyFiles = []
        pattern = "*.py"
        for root, dirs, files in os.walk("."):
            for filename in files:
                if fnmatch.fnmatch(filename, pattern):
                    listOfPyFiles.append(filename)
        return sorted(listOfPyFiles)

if __name__ == '__main__':
    FileSorter.sort()