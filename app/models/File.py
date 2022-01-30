from typing import List
from .utils import Model
from datetime import datetime
from core.Config import settings, logger
import os
import sys


class File(Model):

    size: int
    accessed: datetime
    modified: datetime
    created: datetime

    def __init__(self, self_path: str, self_name: str, self_folder: str):
        self.file_name = self_name
        self.file_path = self_path
        self.root_folder = self_folder
        self.file_extension = str(self_path.split('.')[-1]).lower()
        self.is_readable = settings.is_in_readable_extensions(self.file_extension)

    def set_file_stats(self):
        try:
            stat = os.stat(self.file_path)
            self.size = stat.st_size
            self.accessed = self.dtm_from_ts(stat.st_atime)
            self.modified = self.dtm_from_ts(stat.st_mtime)
            self.created = self.dtm_from_ts(stat.st_ctime)
        except Exception as ex:
            logger.exception(ex)

    def dtm_from_ts(self, ts):
        try:
            return datetime.fromtimestamp(ts)
        except ValueError:
            if ts == -753549904:
                # Mac OSX "while copying" thing
                return datetime(1946, 2, 14, 8, 34, 56)
            else:
                raise sys.exc_info()

    def should_analyze(self) -> bool:
        self.set_file_stats()
        return self.is_readable and self.size < settings.max_file_size

    file_name: str
    file_path: str
    file_extension: str
    is_readable: bool

    @classmethod
    def get_models_from_paths(cls, paths: List[str]) -> List:
        files = []
        print(paths)
        for path in paths:
            files.append(cls(path))
        return files
