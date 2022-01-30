from logging import Logger
from pathlib import Path
from .logger.DefaultLogger import DefaultLogger
import re


class Settings():
    main_folder = Path.home()
    folders_to_ignore = [
        ".git",
        ".nuget",
        "Library",
        "node_modules"
    ]
    regex_to_ignore = [
        "(?:^|\W)Library(?:$|\W)",
        "(?:^|\W)node_modules(?:$|\W)",
        "(?:^|\W).git(?:$|\W)",
        "(?:^|\W).nuget(?:$|\W)",
        "(?:^|\W).vs(?:$|\W)",
        "(?:^|\W).vscode(?:$|\W)",
        "(?:^|\W)site-packages(?:$|\W)",
    ]

    text_readable_extensions = [
        ".doc",
        ".xls",
        ".xml",
        ".txt",
        ".json",
        ".md",
        ".html",
        ".css",
        ".js",
        ".py",
        ".java",
        ".c",
        ".cpp",
        ".h",
        ".hpp",
        ".cs",
        ".go",
        ".php",
        ".sql",
        ".sh",
        ".bat",
        ".ini",
        ".yml",
        ".yaml",
        ".conf",
        ".csv",
        ".log",
        ".tmp",
        ".rtf",
        ".htm",
        ".ppt"
    ]
    zip_extensions = [
        ".zip",
        ".docx",
        ".xlsx",
    ]
    especial_extensions = [
        ".msg"
    ]
    email_extensions = [
        ".eml",
        ".msg",
        ".pst"
    ]
    other_extensions = [
        ".ost",
        ".accdb",
        ".mdb"
    ]
    max_file_size = 1073741824

    def is_in_readable_extensions(self, extension: str) -> bool:
        extension = "." + extension.lower()

        return (
            extension in self.text_readable_extensions
            or extension in self.zip_extensions
            or extension in self.especial_extensions
            or extension in self.email_extensions
            or extension in self.other_extensions
        )

    def compile_regex_to_ignore(self):
        self.regex_to_ignore = [
            re.compile(item, re.IGNORECASE)
            for item in self.regex_to_ignore
        ]


settings = Settings()
settings.compile_regex_to_ignore()
logger: Logger = DefaultLogger("Panhunt")
