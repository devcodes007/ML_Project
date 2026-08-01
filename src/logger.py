import logging
import os
from datetime import datetime

# Log file name with current date and time
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Create logs directory
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)
os.makedirs(os.path.dirname(logs_path), exist_ok=True)

# Configure logging
logging.basicConfig(
    filename=logs_path,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

logger = logging.getLogger(__name__)