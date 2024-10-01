import os

def check_file_permissions():
    for root, dirs, files in os.walk('/'):
        for name in files:
            file_path = os.path.join(root, name)
            try:
                file_stat = os.stat(file_path)
                if file_stat.st_mode & 0o002:
                    print(f"World-writable file found: {file_path}")
                if file_stat.st_mode & 0o4000:
                    print(f"SUID file found: {file_path}")
                if file_stat.st_mode & 0o2000:
                    print(f"SGID file found: {file_path}")
            except Exception as e:
                print(f"Error checking file {file_path}: {e}")