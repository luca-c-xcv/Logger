import logging

class Logger:
    _logger = None

    def __init__(self, log_path):
        logging.basicConfig(filename=log_path, level=logging.DEBUG,format='%(asctime)s [%(levelname)s] ::: %(message)s')
        self.logger = logging.getLogger(__name__)

    @classmethod
    def init(cls, log_path='/tmp/logger.log'):
        if not cls._logger:
            cls._logger = cls(log_path)
        return cls._logger

    def _log_message(self, message, level=logging.DEBUG):
        """ define the type of log message """
        self.logger.log(level, message)
    def debug(self, message):
        """ print a debug message """
        self._log_message(message, level=logging.DEBUG)
    def info(self, message):
        """ print an info message """
        self._log_message(message, level=logging.INFO)
    def warning(self, message):
        """ print a warning message """
        self._log_message(message, level=logging.WARNING)
    def error(self, message):
        """ print an error message """
        self._log_message(message, level=logging.ERROR)
    def critical(self, message):
        """ print a critical message """
        self._log_message(message, level=logging.CRITICAL)
