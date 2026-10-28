# Built-in imports
import os
from dotenv import load_dotenv
from loguru import logger

from playwright.sync_api import Page, Response

from ..models.freelance import Freelancer


load_dotenv()

class Workana:

    def __init__(self):
        
        self.url = os.getenv("WORKANA_URL")

        if not self.base_url:
            msg = "WORKANA_URL environment variable is not set"
            logger.error(msg)
            raise ValueError(msg)

            
    def fetch_web(self) -> list[Freelancer]:
        try:
            

    

if __name__ == "__main__":
    workana = Workana()
    
        
            
    

    
