import os
import logging
from logging.handlers import RotatingFileHandler
from hpilo import Ilo
from dotenv import load_dotenv

# Configure logging
LOG_DIR = 'logs'
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create a rotating file handler
log_file = os.path.join(LOG_DIR, 'hp_ilo_script.log')
handler = RotatingFileHandler(log_file, maxBytes=10*1024*1024, backupCount=5)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

ilo = None

def check_env():
    load_dotenv()
    required_env_vars = ["ILO_ADDRESS", "ILO_USERNAME", "ILO_PASSWORD"]
    for var in required_env_vars:
        if os.getenv(var) is None:
            logger.error(f"{var} not set")
            exit(1)

def start_server():
    global ilo
    logger.info("Starting Server...")
    try:
        server_status = ilo.get_host_power_status()
        logger.info(f"Server Status: {server_status}")
        if server_status != "ON":
            logger.info("Powering On Server...")
            ilo.press_pwr_btn()
            logger.info("Power button pressed.")
        else:
            logger.info("Server already ON.")
    except Exception as e:
        logger.error(f"Error while getting server status or powering on: {e}")

def run_script():
    global ilo
    try:
        ilo = Ilo(os.getenv("ILO_ADDRESS"), os.getenv("ILO_USERNAME"), os.getenv("ILO_PASSWORD"))
        ilo.get_product_name()  # Test connection
        logger.info("ILO Login Success")
        start_server()
    except Exception as e:
        logger.error(f"ILO Login Failed: {e}")

def main():
    logger.info("HP ILO Script by xSora")
    check_env()
    run_script()

if __name__ == "__main__":
    main()
