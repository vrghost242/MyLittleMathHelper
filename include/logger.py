import logging
import colorlog

class Logger:
    def __init__(self, name, profile="lowvis", loglevel="DEBUG"):
        self.log = colorlog.getLogger(name)
        self.log.setLevel("DEBUG")

        # Let's create our handlers
        self.console = logging.StreamHandler()
        self.console.setLevel(loglevel)
        log_format = colorlog.ColoredFormatter(
            fmt="{log_color}{asctime} - {name:10s} - {levelname:10s} - {message}",
            style="{",
            datefmt="%H:%M:%S",
            log_colors=self.get_profile(profile),
        )
        self.console.setFormatter(log_format)
        self.log.addHandler(self.console)

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)
    def warning(self, msg):
        self.log.warning(msg)
    def info(self, msg):
        self.log.info(msg)
    def debug(self, msg):
        self.log.debug(msg)
    def error(self, msg):
        self.log.error(msg)
    def get_profile(self, profile):
        profiles = {
            "highvis": {
                "DEBUG": "cyan",
                "INFO": "light_green",
                "WARNING": "light_yellow",
                "ERROR": "light_red",
                "CRITICAL": "light_red,bg_white"
            },
            "lowvis": {
                "DEBUG": "cyan",
                "INFO": "green",
                "WARNING": "yellow",
                "ERROR": "red",
                "CRITICAL": "red,bg_white"
            }
        }
        return profiles[profile]

if __name__ == "__main__":
    logger = Logger("test")
    logger.info("Hello World")
    logger.debug("This is a debug message")
    logger.warning("This is a warning message")
    logger.console.setLevel("INFO")
    logger.info("This is an info message")
    logger.debug("This is a debug message after setting level to INFO")