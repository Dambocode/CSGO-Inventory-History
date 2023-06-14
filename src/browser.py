import asyncio
from pyppeteer import launch
import time


async def main(user, steamid):
    # Launch the browser
    browser = await launch({'headless': False})

    # Create a new page
    page = await browser.newPage()

    # Navigate to a URL
    await page.goto('https://steamcommunity.com/login/home/?goto=profiles%2F')
    
    desired_url = 'https://steamcommunity.com/profiles/' + steamid + "/"
    while True:
        # Get the current URL
        current_url = page.url

        # Check if the current URL matches the desired URL
        if current_url == desired_url:
            break

        # Wait for a short duration before checking again
        await asyncio.sleep(1)
        print("Navigate to profile...")
    
    current_url=page.url
    
    await page.goto(current_url + "/inventoryhistory/?app%5B%5D=730")

    while True:
        print("Loading more items...")
        try:
            await page.waitForSelector('#load_more_button', timeout=15000)
            await page.click('#load_more_button')
            time.sleep(5)
        except TimeoutError:
            print("Got History")
            break
        except Exception as e:
            print("Got History")
            break

    # Get the HTML content of the page
    html_content = await page.content()

    # Save the HTML content to a file
    with open(f'inventory/{user}.html', 'w', encoding='utf-8') as file:
        file.write(html_content)

    # Close the browser
    await browser.close()


