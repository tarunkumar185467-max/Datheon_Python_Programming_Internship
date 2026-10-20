
# Automatic File Organizer

## About the Project

Have you ever opened your Downloads folder and found it full of documents, images, videos, and other files? It can be difficult to find the file you need when everything is mixed together.

I created this Automatic File Organizer using Python to solve that problem. It helps keep a folder clean and organized by sorting files into different folders according to their file extensions.

For example, text documents go into the Documents folder, images go into the Images folder, and Python files go into the Code folder.

## What Can It Do?

- Organizes files into separate folders based on their extensions.
- Supports Documents, Images, Videos, Archives, and Code files.
- Shows a preview of the changes before moving any files.
- Asks for confirmation before starting the actual organization.
- Handles duplicate filenames by adding a number to the new filename instead of overwriting an existing file.
- Skips files with extensions that are not supported.
- Handles permission problems and other file-operation errors.
- Displays a summary showing the number of files processed, skipped, and affected by errors.

## Tools and Technologies

I built this project using Python and its built-in modules:

- `os` for accessing and scanning directories.
- `shutil` for moving files.
- `pathlib` for working with file and folder paths.
- `datetime` for displaying the execution date and time.

No additional third-party Python packages are required.

## Project Structure

```text
File_Organizer/
├── organizer.py
└── README.md
```

## File Categories

The program recognizes common file extensions and sorts them into these categories:

| Folder | Examples |
|---|---|
| Documents | PDF, DOCX, TXT, XLSX, CSV |
| Images | JPG, JPEG, PNG, GIF, WEBP |
| Videos | MP4, MKV, AVI, MOV |
| Archives | ZIP, RAR, 7Z, TAR, GZ |
| Code | PY, JAVA, CPP, HTML, CSS, JS, SQL |

Files with extensions that are not supported are skipped.

## How to Run the Project

Follow these simple steps to use the organizer:

1. Install Python on your computer.
2. Open the `File_Organizer` project folder in VS Code.
3. Open the terminal.
4. Run the following command:

   ```bash
   python organizer.py
   ```

5. Enter the full path of the folder you want to organize.
6. Check the preview to see where the files will go.
7. If everything looks correct, type `YES` to confirm.

The program will then move the supported files into their respective folders.

## Testing the Project

I tested the program using a temporary folder containing different types of files.

During testing, I checked whether the program could:

- Sort documents, images, and Python files correctly.
- Show a preview before moving files.
- Avoid overwriting files with duplicate names.
- Skip files with unsupported extensions.
- Display a summary after execution.

The tests confirmed that these features were working as expected.

## A Few Things to Keep in Mind

- Always test the program with a temporary folder before using it on important files.
- Review the preview carefully before confirming any changes.
- Keep a backup of important files.
- The program processes files directly inside the selected folder. It does not automatically organize files inside nested subfolders.

## What I Learned

While building this project, I got practical experience with Python file handling, directory scanning, exception handling, and working with file paths.

I also learned how to handle duplicate filenames and why it is useful to preview changes before performing file operations.

This project helped me understand how Python can be used to automate everyday tasks and make them easier.

## Useful Resources

- Python `shutil` documentation: https://docs.python.org/3/library/shutil.html
- Python `os` documentation: https://docs.python.org/3/library/os.html
- Python `pathlib` documentation: https://docs.python.org/3/library/pathlib.html

## Conclusion

Building this project was a useful learning experience. It gave me an opportunity to apply my Python knowledge to a practical problem and create a simple tool that can help keep files organized.

This is one of my steps toward improving my programming skills and learning more about automation.
