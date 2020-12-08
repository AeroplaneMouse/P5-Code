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

class ProgressLog(Log):
    def __init__(self, message, severity=Severity.INFO, progress=0):
        Log.__init__(self, message, severity)
        self.progress = progress


class Logger:
    INSERT_TIMESTAMP = False
    INSERT_DATE = False

    def __init__(self, severity):
        self.severity = severity


class PrintLogger(Logger):
    def log(self, log):
        if type(log) == ProgressLog:
            printProgressBar(
                log.progress,
                1,
                log.message,
                'Complete')
        else:
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


class MultiLogger(Logger):
    def __init__(self, loggers=[]):
        self.loggers = loggers

    def log(self, log):
        for logger in self.loggers:
            logger.log(log)


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

# Print iterations progress
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 49, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + ' ' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total:
        print()
