import logging
import daiquiri

# 로거 설정
daiquiri.setup(level=logging.INFO)
logger = daiquiri.getLogger(__name__)

logger.info("Hello from daiquiri!")
logger.debug("This is a debug message")
