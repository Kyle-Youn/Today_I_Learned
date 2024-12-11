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
