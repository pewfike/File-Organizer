# File Organizer - Automating tedious work with Python.

## Overview

The Desktop File Organizer is a Python script designed to help you automatically organize the clutter on your desktop. It categorizes files based on their types (documents, images, music, videos, etc.) and moves them into corresponding folders, making your workspace more tidy and efficient.

## Features

- **Automatic Organization**: Moves files from your desktop into specific folders based on file extensions.
- **Customizable**: You can easily add new file types and categories by modifying the script.
- **Name Conflict Handling**: Automatically renames files if a file with the same name already exists in the destination folder.
- **Simple and Lightweight**: The script is lightweight and can be run from the command line with minimal setup.

## File Organization Structure

By default, the script categorizes files into the following folders:

- **Documents**: `.pdf`, `.docx`, `.txt`, `.pptx`, `.xlsx`
- **Images**: `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`
- **Music**: `.mp3`, `.wav`, `.aac`
- **Videos**: `.mp4`, `.mkv`, `.mov`, `.avi`
- **Archives**: `.zip`, `.rar`, `.tar`, `.gz`
- **Scripts**: `.py`, `.js`, `.sh`, `.bat`
- **Others**: Files that do not match any of the above categories

You can customize these categories and add new file types by editing the `file_types` dictionary in the script.

## Getting Started

### Prerequisites

- Python 3.6 or higher

### Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/your-username/desktop-file-organizer.git
    ```

2. Navigate to the directory:

    ```bash
    cd desktop-file-organizer
    ```

3. Ensure you have Python installed. You can check your Python version with:

    ```bash
    python --version
    ```

### Usage

1. Save the script `file_organizer.py` to your desktop or any directory you prefer.
2. Run the script using Python:

    ```bash
    python file_organizer.py
    ```

3. The script will automatically organize your desktop files into the appropriate folders. Any files that do not match a specific category will be moved to the `Others` folder.

### Customization

To customize the file categories:

1. Open `file_organizer.py` in a text editor.
2. Modify the `file_types` dictionary to include new file types or remove existing ones.
3. Save the changes and rerun the script.

### Troubleshooting

- **PermissionError / FileExistsError**: Ensure that there are no files on your desktop with the same name as the folders (e.g., a file named `Others`).
- **Files Not Moving**: Verify that the file extensions in the `file_types` dictionary match the files you are trying to organize.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an Issue if you have any suggestions or improvements.
