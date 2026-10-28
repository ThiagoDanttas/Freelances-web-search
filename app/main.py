from loguru import logger
from freelances_web_search.config.setup_log import setup_logging
from freelances_web_search.pipeline import Pipeline
from playwright.sync_api import sync_playwright, Page, Browser



def main() -> None:
    
    setup_logging()
    logger.info("Start web scraping freelancer project")

    try:
        with sync_playwright() as pw:
            browser: Browser = pw.chromium.launch(headless=False)
            ctx: Browser = browser.new_context()
            page: Page = ctx.new_page()
        Pipeline.run(page=page)

    except RuntimeError as e:
        logger.exception(f"Web scrap freelancer execution error: {e}")

    finally: 
        logger.info("End of execution.")

if __name__ == '__main__': 
    main()
  