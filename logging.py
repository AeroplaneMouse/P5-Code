import os
import time
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
    INSERT_TIMESTAMP = False
    INSERT_DATE = False

    def __init__(self, severity):
        self.severity = severity


class PrintLogger(Logger):
    def log(self, log):
        if (log.severity.value <= self.severity.value):
            logTime = getTime(self.INSERT_TIMESTAMP)
            logDate = getDate(self.INSERT_DATE)
            msg = '{:<12}{}{}| {}'.format(
                '['+log.severity.name+']',
                logDate,
                logTime,
                log.message)
            print(msg)

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
            logTime = getTime(self.INSERT_TIMESTAMP)
            logDate = getDate(self.INSERT_DATE)
            msg = '{:<12}{}{}| {}\n'.format(
                '['+log.severity.name+']',
                logDate,
                logTime,
                log.message)

            # Write to file
            with open(self.filename, "a") as f:
                f.write(msg)

def getDate(flag):
    if flag:
        localtime = time.localtime(time.time())
        return '{}-{:02}-{:02} '.format(
            localtime[0],
            localtime[1],
            localtime[2])
    else:
        return ''

def getTime(flag):
    if flag:
        localtime = time.localtime(time.time())
        return '{:02}:{:02}:{:02} '.format(
            localtime[3],
            localtime[4],
            localtime[5])
    else:
        return ''