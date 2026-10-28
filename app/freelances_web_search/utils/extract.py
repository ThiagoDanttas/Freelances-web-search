
from playwright.sync_api import Page, Response
from loguru import logger

from ..services.workana import Workana

class Extract:

    def __init__(self):
        self.workana = Workana()


    def goto_page(self, page: Page):

        try:
            response: Response = page.goto(self.workana.url, wait_until="domcontentloaded", timeout=10000)
            
            if response.ok:
                logger.success(f"Successful connection to Workana: status={response.status}")

                workana: list = self.workana.workana_service(self, page=page)


            logger.error(f"Connection failure to Workana: status={response.status}, body={response.body}")
            return []
            
        except Exception as e:
            logger.exception(f"Workana returned an error: Error={e} status={response.status}, body={response.body}")
            return []

        