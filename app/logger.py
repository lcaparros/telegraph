import logging
from pythonjsonlogger import jsonlogger


# Get custom logger
def get_custom_logger(app):

    # Delete all the app default handlers
    del app.logger.handlers[:]

    loggers = [app.logger]
    handlers = []

    log_level = logging.DEBUG
    log_path = "logs"

    # Creating a console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)
    console_handler.setFormatter(common_formatter())
    handlers.append(console_handler)

    # Creating a file handler
    file_name = "app"
    file_handler = logging.FileHandler("{0}/{1}.log".format(log_path, file_name))
    file_handler.setLevel(log_level)
    file_handler.setFormatter(common_formatter())
    handlers.append(file_handler)

    # Creating a json handler
    json_file_name = "app_log"
    json_handler = logging.FileHandler("{0}/{1}.json".format(log_path, file_name))
    json_handler.setLevel(log_level)
    json_handler.setFormatter(json_formatter())
    handlers.append(json_handler)

    # Link each handler with each logger
    for l in loggers:
        for handler in handlers:
            l.addHandler(handler)
        l.propagate = False
        l.setLevel(logging.DEBUG)
    
    # Set root log to DEBUG level
    logging.basicConfig(level=logging.DEBUG)



# Log Common Formatter
def common_formatter():
    return logging.Formatter(
        "%(asctime)s.%(msecs)d\t %(levelname)s \t[%(name)s.%(funcName)s:%(lineno)d]\t %(message)s",
        datefmt="%d/%m/%Y %H:%M:%S"
    )

# Log Json Formater
def json_formatter():
    return jsonlogger.JsonFormatter(fmt="%(asctime)s %(levelname)s %(name)s %(funcName)s %(lineno)d %(message)s")
