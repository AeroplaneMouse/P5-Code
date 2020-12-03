from enum import Enum
import os


class Severity(Enum):
    EMERGENCY   = 0
    ALERT       = 1
    CRITICAL    = 2
    ERROR       = 3
    WARNING     = 4
    NOTICE      = 5
    INFO        = 6
    DEBUG       = 7


class Log:
    def __init__(self, message, severity=Severity.INFO):
        self.severity = severity
        self.message = message


class Logger:
    def __init__(self, severity):
        self.severity = severity


class PrintLogger(Logger):
    def log(self, log):
        if (log.severity.value <= self.severity.value):
            m = '[{}] {}'.format(
                log.severity.name,
                log.message)
            print(m)

class FileLogger(Logger):
    LOG_FOLDER = 'logs/'

    def __init__(self, severity, filename):
        Logger.__init__(self, severity)

        self.filename = self.LOG_FOLDER + filename

        # Create log folder
        if not os.path.exists(self.LOG_FOLDER):
            os.mkdir('logs/')

    def log(self, log):
        if log.severity.value <= self.severity.value:
            msg = '[{}] {}\n'.format(log.severity.name, log.message)

            # Write to file
            with open(self.filename, "a") as f:
                f.write(msg)
