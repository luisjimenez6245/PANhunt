from modules import FolderReader
from core.Config import settings, logger
from datetime import datetime


start_time = datetime.now()
logger.warning("Starting...")

folder_reader = FolderReader(settings.folders_to_ignore)
files = folder_reader.get_all_files()
finishing_time = datetime.now()
total_time = finishing_time - start_time
logger.warning(f"Finished scanning folders... {total_time}")

result_file = open("result.txt", "w+")
for file_path, file_model in files.items():
    result_file.write(f"{file_path} {file_model.size} {file_model.accessed} {file_model.modified} {file_model.created}\n")
result_file.close()
