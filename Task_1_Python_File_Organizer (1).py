from pathlib import Path
import shutil

# Folder that contains the files to organize
SOURCE_FOLDER = Path("Downloads")

# File types and their destination folders
FILE_GROUPS = {
    "Images": {".jpg", ".jpeg", ".png", ".gif"},
    "Documents": {".pdf", ".doc", ".docx", ".txt"},
    "Videos": {".mp4", ".mkv", ".avi"},
    "Audio": {".mp3", ".wav"},
    "Archives": {".zip", ".rar", ".7z"}
}


def find_category(file_extension):
    """Return the folder name for a file extension."""
    extension = file_extension.lower()

    for folder, extensions in FILE_GROUPS.items():
        if extension in extensions:
            return folder

    return "Others"


def organize_files():
    if not SOURCE_FOLDER.exists():
        print(f"Folder not found: {SOURCE_FOLDER}")
        return

    for item in SOURCE_FOLDER.iterdir():
        if not item.is_file():
            continue

        category = find_category(item.suffix)
        destination = SOURCE_FOLDER / category
        destination.mkdir(exist_ok=True)

        new_path = destination / item.name

        # Avoid replacing an existing file with the same name
        if new_path.exists():
            print(f"Skipped: {item.name} (already exists)")
            continue

        shutil.move(str(item), str(new_path))
        print(f"Moved: {item.name} -> {category}/")

    print("File organization completed.")


if __name__ == "__main__":
    organize_files()
