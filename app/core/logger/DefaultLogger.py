from .ColoredFormatter import ColoredFormatter
import logging

RESET_SEQ = "\033[0m"
COLOR_SEQ = "\033[1;%dm"


def formatter_message(message):
    m = message.replace(
        "$RESET", RESET_SEQ
    )
    return m


class DefaultLogger(logging.Logger):

    FORMAT = "%(levelname)s%(message)s \t(%(pathname)s Line:%(lineno)d$RESET)"
    COLOR_FORMAT = formatter_message(FORMAT)
    NONE_FORMAT = "%(levelname)s%(message)s \t(%(pathname)s:%(lineno)d)"

    def __init__(
        self,
        name,
        log_format=None,
    ):
        super().__init__(f"{name}")
        self.addHandler(self.get_handler_logger(log_format))

    @classmethod
    def get_handler_logger(
            cls, 
            log_format=None,
        ) -> logging.Handler:
        handler = None
        if(log_format is None):
                log_format = cls.COLOR_FORMAT
        color_formatter = ColoredFormatter(log_format)
        handler = logging.StreamHandler()
        handler.setFormatter(color_formatter)
        return handler