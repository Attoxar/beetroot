with open("myfile.txt", "r") as f:
    contents = f.read()
    print(contents)

# if you change the "with open("myfile.txt"... to open(path/any/dictionary you can create the file in a different dict)".
# in that case you have to put in the new file path into the "open("new/file/path/myfile.txt)" line

# Does the new file show up in the directory where you ran your scripts?
# yes since the myfile is being created in the first part

# What if you add a different directory path to the filename passed to open?
# Then it wouldn't find it and put out an error message unless u created the file in a different dictionary.
# Then you have to change the open path to the dictionary where the file is located it.
