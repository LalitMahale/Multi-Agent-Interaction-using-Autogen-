import logging
import logging.handlers
import sys
import os 

if not os.path.exists("logs"):
    os.makedirs("logs",exist_ok=True)
logging.basicConfig(level=logging.INFO,format="[%(asctime)s  %(message)s]",handlers=[logging.FileHandler("logs/agent.log"),logging.StreamHandler(sys.stdout)])

logger = logging.getLogger("Multi Agent interaction")


logging.info("Started")