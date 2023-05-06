from log import logging
from config import Config
from ai import AI

logger = logging.getLogger('app.py')

config = Config()
ai = AI(config.openai_key)

exit_code = 0


try:
    ai.ask_gpt()


except Exception as e:
    exit_code = 1
    logger.error(f'Error in main app. Error: {str(e)}')


exit(exit_code)