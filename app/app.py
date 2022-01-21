from modules import FolderReader
from core.Config import Settings

folder_reader = FolderReader(Settings.folders_to_ignore)
files = folder_reader.get_all_files()
for file in files:
    print(file)