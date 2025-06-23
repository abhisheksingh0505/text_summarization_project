import os
import logging
from datetime import datetime

# Logging format
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s ]"

# Log directory and file
log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_logs.log")

# Create log directory if not exists
os.makedirs(log_dir, exist_ok=True)

# Logging configuration
logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler()
    ]
)

# Exportable logger instance
logger = logging.getLogger("textSummarizationLogger")
