# Picture Database Program

## Overview
This Python program manages a database of pictures stored in a text file (`Pictures.txt`). Each picture has a description, width, height, and frame color. Users can search for pictures that meet specific requirements, and the program outputs matching results and saves them to a new file (`NewPictureData.txt`).

The program demonstrates file handling, user input validation, data filtering, and case-insensitive search functionality.

---

## Features

1. **File Reading and Storage**
   - Reads picture data from `Pictures.txt`.
   - Each picture’s description, width, height, and frame color are stored in a Python list.
   - Supports multiple pictures in the text file.

2. **User Input Validation**
   - Prompts the user to enter a frame color.
   - Accepts any capitalization (e.g., `Black`, `black`, `BLACK`).
   - Only allows valid colors: `black`, `grey`, or `white`.

3. **Search Functionality**
   - Users enter the maximum width and height along with the frame color.
   - The program searches through all pictures to find matches that meet all requirements.
   - Prints matching picture details: description, width, height, and color.

4. **Output to File**
   - Matching picture data is saved to a new file (`NewPictureData.txt`).
   - Each entry includes the description, width, and height.

5. **User Feedback**
   - Notifies the user if no matches are found.
   - Confirms when the output file has been successfully created.

---

## How to Run

1. Ensure Python 3 is installed on your system.
2. Place `Pictures.txt` in the same directory as the program.
3. Run the program:

```bash
python PictureDatabase.py
```
