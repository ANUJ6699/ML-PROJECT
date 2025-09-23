# import logging
# import os
# from datetime import datetime

# LOG_FILE = f"logs/app_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
# logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)
# os.makedirs(logs_path, exist_ok=True)


# LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# logging.basicConfig(
#     filename=LOG_FILE_PATH,
#     format="[%(asctime)s] %(levelname)s - %(message)s",
#     level=logging.INFO
# )

# if __name__ == "__main__":
#     logging.info("Logging setup complete.")
#     logging.info("This is an info message.")
#     logging.error("This is an error message.")

import logging
import os
from datetime import datetime

# Just the file name with timestamp
LOG_FILE = f"app_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"

# Directory for logs
logs_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_dir, exist_ok=True)  # create only the folder

# Full path to the log file
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(levelname)s - %(message)s",
    level=logging.INFO
)
