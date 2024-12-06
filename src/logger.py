import logging
import os

logging.basicConfig(
    format="%(levelname)s: %(message)s",
)

logger = logging.getLogger("logger")

silent = os.getenv("RUPAN_SILENT", "false").lower() == "true"
verbose = os.getenv("RUPAN_VERBOSE", "false").lower() == "true"

log_level = logging.INFO
if silent:
    log_level = logging.ERROR
elif verbose:
    log_level = logging.DEBUG
logger.setLevel(log_level)
