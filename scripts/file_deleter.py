import os

def clear_folder(folder_path):

    if not os.path.isdir(folder_path):
        print(f"[SKIP] Folder not found: {folder_path}")
        return

    deleted_any = False
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            try:
                os.remove(file_path)
                print(f"[OK] Deleted file: {file_path}")
                deleted_any = True
            except Exception as e:
                print(f"[ERROR] Could not delete {file_path}: {e}")
    if not deleted_any:
        print(f"[INFO] No files to delete in: {folder_path}")

def main():
    # Folders to clean
    folders_to_clear = [
        "data/raw",
        "data/synthetic"
    ]

    for folder in folders_to_clear:
        clear_folder(folder)