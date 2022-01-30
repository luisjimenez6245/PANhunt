import os
import re
from typing import Dict, List, Optional
from core.Config import settings, logger
from models import File

class FolderReader:

    paths_to_ignore = []

    def __init__(
        self,
        paths_to_ignore: Optional[List[str]] = settings.folders_to_ignore,
    ):
        if paths_to_ignore is None:
            paths_to_ignore = []

        self.paths_to_ignore = paths_to_ignore

    def get_files(self, path: str) -> List[str]:
        result = []
        helper = os.listdir(path)
        for item in helper:
            full_path = os.path.join(path, item)
            if os.path.isfile(full_path):
                result.append(full_path)
        return result
    
    def should_include_path(self, *paths: List[str]) -> bool:
        for path in paths:
            if path in self.paths_to_ignore:
                return False
        for path in paths:
            for item in settings.regex_to_ignore:
                if item.search(path):
                    return False
        return True

    def get_all_files(self, path: str = settings.main_folder) -> Dict:
        paths = {}
        for root, dirs, files in os.walk(path):
            dirs[:] = [check_dir for check_dir in dirs if os.path.join(root, check_dir).lower() not in settings.folders_to_ignore]
            last_path = root.split(os.sep)[-1]
            if self.should_include_path(last_path, root):
                for file in files:
                    file_path = os.path.join(root, file)
                    if self.should_include_path(file, file_path):
                        file_model = File(file_path, file, root)
                        if(file_model.should_analyze()):
                            paths[file_path] = file_model
        logger.info("Found {} files".format(len(paths)))
        return paths
