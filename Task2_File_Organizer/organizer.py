
import os
import shutil
from pathlib import Path
from datetime import datetime

# File extension to category mapping
FILE_CATEGORIES = {
    # Documents
    ".pdf": "Documents",
    ".doc": "Documents",
    ".docx": "Documents",
    ".txt": "Documents",
    ".rtf": "Documents",
    ".odt": "Documents",
    ".xls": "Documents",
    ".xlsx": "Documents",
    ".csv": "Documents",
    ".ppt": "Documents",
    ".pptx": "Documents",

    # Images
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".bmp": "Images",
    ".webp": "Images",
    ".svg": "Images",
    ".tiff": "Images",

    # Videos
    ".mp4": "Videos",
    ".mkv": "Videos",
    ".mov": "Videos",
    ".avi": "Videos",
    ".wmv": "Videos",
    ".webm": "Videos",

    # Archives
    ".zip": "Archives",
    ".rar": "Archives",
    ".7z": "Archives",
    ".tar": "Archives",
    ".gz": "Archives",

    # Code
    ".py": "Code",
    ".java": "Code",
    ".cpp": "Code",
    ".c": "Code",
    ".h": "Code",
    ".js": "Code",
    ".ts": "Code",
    ".html": "Code",
    ".css": "Code",
    ".json": "Code",
    ".xml": "Code",
    ".sql": "Code",
}


def get_unique_destination(destination):
    """Generate a filename that does not already exist."""
    if not destination.exists():
        return destination

    folder = destination.parent
    stem = destination.stem
    suffix = destination.suffix
    counter = 1

    while True:
        candidate = folder / f"{stem}_{counter}{suffix}"
        if not candidate.exists():
            return candidate
        counter += 1


def organize_directory(folder_path, preview=True):
    """Organize files in one directory without scanning subfolders."""
    folder = Path(folder_path).expanduser().resolve()

    if not folder.is_dir():
        print(f"ERROR: Directory not found: {folder}")
        return

    moved = 0
    skipped = 0
    failed = 0
    logs = []

    print("\n" + "=" * 60)
    print("             AUTOMATIC FILE ORGANIZER")
    print("=" * 60)
    print(f"Folder: {folder}")
    print(f"Mode: {'PREVIEW (no files moved)' if preview else 'LIVE'}")
    print("-" * 60)

    try:
        with os.scandir(folder) as entries:
            for entry in entries:
                try:
                    # Process regular files only; skip folders and symlinks.
                    if not entry.is_file(follow_symlinks=False):
                        continue

                    source = Path(entry.path)
                    category = FILE_CATEGORIES.get(
                        source.suffix.lower()
                    )

                    # Unknown extensions are left untouched.
                    if category is None:
                        skipped += 1
                        logs.append(
                            f"SKIPPED: {source.name} (unmapped extension)"
                        )
                        continue

                    destination_folder = folder / category

                    # Preview mode does not create folders or move files.
                    if preview:
                        destination = get_unique_destination(
                            destination_folder / source.name
                        )
                        moved += 1
                        logs.append(
                            f"PREVIEW: {source.name} -> "
                            f"{category}/{destination.name}"
                        )
                        continue

                    destination_folder.mkdir(
                        parents=True, exist_ok=True
                    )

                    destination = get_unique_destination(
                        destination_folder / source.name
                    )

                    shutil.move(str(source), str(destination))

                    moved += 1
                    logs.append(
                        f"MOVED: {source.name} -> "
                        f"{category}/{destination.name}"
                    )

                except PermissionError as error:
                    failed += 1
                    logs.append(
                        f"PERMISSION ERROR: {entry.name}: {error}"
                    )

                except (OSError, shutil.Error) as error:
                    failed += 1
                    logs.append(f"ERROR: {entry.name}: {error}")

    except PermissionError as error:
        print(f"Cannot access the directory: {error}")
        return

    except OSError as error:
        print(f"Directory scanning error: {error}")
        return

    print("\nEXECUTION LOG")
    print("-" * 60)

    for message in logs:
        print(message)

    print("\nEXECUTION SUMMARY")
    print("-" * 60)
    print(f"Files moved / planned : {moved}")
    print(f"Files skipped         : {skipped}")
    print(f"Files failed          : {failed}")
    print(f"Execution time        : {datetime.now():%Y-%m-%d %H:%M:%S}")
    print(f"Mode                  : {'PREVIEW' if preview else 'LIVE'}")
    print("=" * 60)


def main():
    print("Automatic File Organizer")
    print("Start with a test folder, not your real Downloads folder.")

    folder_path = input(
        "\nEnter the folder path to organize: "
    ).strip().strip('"')

    if not folder_path:
        print("No folder path provided. Exiting.")
        return

    # Preview first to reduce the risk of unwanted file moves.
    organize_directory(folder_path, preview=True)

    choice = input(
        "\nMove these files now? Type YES to confirm: "
    ).strip()

    if choice == "YES":
        organize_directory(folder_path, preview=False)
    else:
        print("\nCancelled. No files were moved.")


if __name__ == "__main__":
    main()
