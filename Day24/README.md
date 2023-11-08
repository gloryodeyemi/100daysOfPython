## Day 24 - Files, Directories, and Paths

**Stage:** Intermediate

**Project:** Mail Merge

**Topics:**
* **Python file**
    ```
    # Read a file - option 1
    file = open("my_file.txt")
    contents = file.read()
    file.close()

    # Read a file - option 2 - file closes automatically when done.
    with open("my_file.txt") as file:
        contents = file.read()

    # write to a file - override the current content in file
    with open("my_file.txt", 'w') as file:
        file.write("I am a new text.")
    
    # add to a file - add to the content of the file
    with open("my_file.txt", 'a') as file:
        file.write("\nI am another text.")
    
    # create a new file
    with open("new_file.txt", 'w') as file:
        file.write("I am a new file.")
    ```
  
* **File directories**
  - Absolute file path - starts from the origin.
  ```
  with open("/Users/Folder/Folder/my_file.txt", 'a') as file:
    file.write("\nI am a text.")
  ```
  
  - Working directory - the directory or folder we are working from.

  - Relative file path - starts from the working directory (use ./, ../, etc.).
  ```
  with open("../my_file.txt", 'a') as file:
    file.write("\nI am a text.")
  ```
  