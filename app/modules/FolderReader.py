import os
from typing import List, Optional
from pathlib import Path


class FolderReader:

    paths_to_ignore = []

    def __init__(
        self,
        paths_to_ignore: Optional[List[str]] = None,
    ):
        if paths_to_ignore is None:
            paths_to_ignore = []

        self.paths_to_ignore = paths_to_ignore

    def get_all_files(self, path: str = Path.home()) -> List[str]:
        paths = self.get_paths(path)
        files = []
        for path in paths:
            try:
                files += self.get_files(path)
            except Exception as e:
                print(e)
        return files

    def get_files(self, path: str) -> List[str]:
        result = []
        helper = os.listdir(path)
        for item in helper:
            full_path = os.path.join(path, item)
            if os.path.isfile(full_path):
                result.append(full_path)
        return result

    def get_paths(self, path: str) -> List[str]:
        paths = []
        for root, dirs, files in os.walk(path):
            if(dirs is not None):
                for dir in dirs:
                    if(dir not in self.paths_to_ignore):
                        full_path = os.path.join(root, dir)
                        if(full_path not in self.paths_to_ignore):
                            paths.append(full_path)
        return paths
