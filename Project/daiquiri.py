# pip install daiquiri

import daiquiri

# Daiquiri 로깅 초기화
daiquiri.setup()

# 로거 가져오기
logger = daiquiri.getLogger(__name__)

# 로그 출력
logger.info("This is an info message")
logger.waring("This is a warning message")
logger.error("This is a error message")


>>>>
2024-01-01 12:00:00,000 INFO [module_name] This is an info message
2024-01-01 12:00:00,001 WARNING [module_name] This is a warning message
2024-01-01 12:00:00,002 ERROR [module_name] This is an error message


import logging
import daiquiri

# 로거 설정
daiquiri.setup(level=logging.INFO)
logger = daiquiri.getLogger(__name__)

logger.info("Hello from daiquiri!")
logger.debug("This is a debug message")
