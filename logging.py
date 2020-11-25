from enum import Enum


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
