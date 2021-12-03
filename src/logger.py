import logging
import os

logging.basicConfig(
    format="%(levelname)s: %(message)s",
)

logger = logging.getLogger("logger")

silent = os.environ["AWS_INFO_EXTRACTOR_SILENT"].lower() == "true"
verbose = os.environ["AWS_INFO_EXTRACTOR_VERBOSE"].lower() == "true"

log_level = logging.INFO
if silent:
    log_level = logging.ERROR
elif verbose:
    log_level = logging.DEBUG
logger.setLevel(log_level)
