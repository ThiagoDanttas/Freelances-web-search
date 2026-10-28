from datetime import date
from pathlib import Path

from loguru import logger


def  setup_logging():
    today = date.today().strftime("")
    log_dir: Path = Path(__file__).parent.parent / "log" / f'{today}'
    log_dir.mkdir(exist_ok=True)
    log_file: str = str(log_dir/"app_{time:YYYY-MM-DD}.log")
    logger.add(log_file,
                format="{time:MMMM D, YYYY > HH:mm:ss} | {level} | {message} ", 
                rotation="10 MB", retention="10 days", mode="a"
                )
