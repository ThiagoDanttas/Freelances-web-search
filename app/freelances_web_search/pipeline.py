
from playwright.sync_api import Page

from .services.workana import Workana
from .utils.extract import Extract
from .utils.transform import Transform
from .utils.load import Load

class Pipeline:
    
    def __init__(self):
        self.extraction = Extract()
        self.transform = Transform()
        self.load = Load()
        

    def run(self, page: Page):
        extraction: list = self.extraction.














