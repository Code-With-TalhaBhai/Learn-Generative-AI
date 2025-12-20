import os
import asyncio
from dotenv import load_dotenv
import base64
from typing import Literal, Union
from playwright.async_api import Browser, Page, Playwright, async_playwright
from agents import AsyncComputer, Environment, Button, Agent, ComputerTool, ModelSettings, trace, Runner


load_dotenv()

# secret = os.environ.get('OPENAI_API_KEY')


# uv run playwright install --------> To install Browser
async def main():
    async with local_playwright_computer() as computer:
        with trace("example trace"):
            agent = Agent(
                name="Computer Agent",
                instructions="You are a helpful agent",
                model="computer-use-preview-2025-03-11",
                tools=[ComputerTool(computer)],
                model_settings=ModelSettings(truncation="auto")
            )

            result = await Runner.run(agent, 'Search for Lionel Messi in India')
            print(result.final_output)
        

    



CUA_KEY_TO_PLAYWRIGHT_KEY = {
    "/": "Divide",
    "\\": "Backslash",
    "alt": "Alt",
    "arrowdown": "ArrowDown",
    "arrowleft": "ArrowLeft",
    "arrowright": "ArrowRight",
    "arrowup": "ArrowUp",
    "backspace": "Backspace",
    "capslock": "CapsLock",
    "cmd": "Meta",
    "ctrl": "Control",
    "delete": "Delete",
    "end": "End",
    "enter": "Enter",
    "esc": "Escape",
    "home": "Home",
    "insert": "Insert",
    "option": "Alt",
    "pagedown": "PageDown",
    "pageup": "PageUp",
    "shift": "Shift",
    "space": " ",
    "super": "Meta",
    "tab": "Tab",
    "win": "Meta",
}



class local_playwright_computer(AsyncComputer):

    def __init__(self):
        self._playwright: Union[Playwright, None] = None
        self._browswer: Union[Browser, None] = None
        self._page: Union[Page, None] = None


    async def _get_browser_and_page(self)-> tuple[Browser, Page]:
        width, height = self.dimensions
        launch_args = [f"--window-size={width},{height}"]
        browser = await self._playwright.chromium.launch(headless=False, args=launch_args)
        page = await browser.new_page()
        await page.set_viewport_size({"width":width, "height": height})
        await page.goto("https://www.bing.com")
        return browser,page
    
    async def __aenter__(self):
        self._playwright = await async_playwright().start()
        self._browswer, self._page = await self._get_browser_and_page()
        return self
    

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self._browswer:
            await self._browswer.close()
        if self._playwright:
            await self._playwright.stop()

    @property
    def playwright(self)->Playwright:
        assert self._playwright is not None
        return self._playwright

    @property
    def browser(self)->Browser:
        assert self._browser is not None
        return self._browswer


    @property
    def page(self)->Page:
        assert self._page is not None
        return self._page
    
    @property
    def environment(self)->Environment:
        return "browser"
    
    @property
    def dimensions(self)-> tuple[int,int]:
        return (1024,768)
    
    async def screenshot(self):
        """Capture only the viewport (not full_page)."""
        png_bytes = await self.page.screenshot(full_page=False)
        return base64.b64encode(png_bytes).decode('utf-8')
    

    async def click(self,x:int, y:int, button: Button = "left"):
        playwright_button: Literal["left","middle","right"] = "left"

        if button in ["left","right","middle"]:
            playwright_button = button
        await self.page.mouse.click(x,y,button=playwright_button)


    async def double_click(self, x:int, y:int):
        return self.page.mouse.dblclick
    

    async def scroll(self, x, y, scroll_x, scroll_y):
        await self.page.mouse.move(x,y)
        await self.page.evaluate(f"window.scrollBy({scroll_x}, {scroll_y})")

    async def type(self, text):
        await self.page.keyboard.type(text)

    async def wait(self, x, y):
        await asyncio.sleep(1)

    async def move(self, x, y):
        return self.page.mouse.move(x,y)


    async def keypress(self, keys: list[str]):
        mapped_keys = [CUA_KEY_TO_PLAYWRIGHT_KEY.get(key.lower(),key) for key in keys]
        
        for key in mapped_keys:
            await self.page.keyboard.down(key)
        for key in reversed(mapped_keys):
            await self.page.keyboard.up(key)
    


    async def drag(self, path: list[tuple[int, int]]):
        if not path:
            return
        
        await self.page.mouse.move(path[0][0],path[0][1])
        await self.page.mouse.down()

        for px,py in path[1:]:
            await self.page.mouse.move(px,py)

        await self.page.mouse.up()






if __name__ == "__main__":
    asyncio.run(main())
