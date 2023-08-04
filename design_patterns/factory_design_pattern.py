import logging
import datetime

class FileLogger:
    def __init__(self) -> None:
        print("File Logging")

    def logging(self, msg):
        return logging.info(f"File Logging {msg} at {datetime.datetime.now()}")

class ConsoleLogger:
    def __init__(self) -> None:
        print("Console Logging")

    def logging(self, msg):
        return logging.warning(f"Console Logging {msg} at {datetime.datetime.now()}")

class DatabaseLogger:
    def __init__(self) -> None:
        print("Database Logging")

    def logging(self, msg):
        return logging.info(f"Database Logging {msg} at {datetime.datetime.now()}")
    
def FactoryLogger(logger_type: str):
    """Factory Method"""

    loggers = {
        "File": FileLogger,
        "Console": ConsoleLogger,
        "Database": DatabaseLogger
    }
    return loggers[logger_type]()


logging.basicConfig(level=logging.INFO)

message = "secret"
file = FactoryLogger("File")
console = FactoryLogger("Console")
database = FactoryLogger("Database")

file.logging(message)
console.logging(message)
database.logging(message)
