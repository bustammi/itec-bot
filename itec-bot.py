# Works with Python 2.7.16
import discord
from discord.ext import commands
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys

client = commands.Bot(command_prefix='!i ')
browser = webdriver.Chrome()


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


# Discord bot for automatically entering credentials and trigger a response from bot when condition is true

@client.command()
async def ping(ctx):
    status = "E-class is currently active"
    try:
        # Making selenium headless
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument("--window-size=1920x1080")
        browser = webdriver.Chrome(options=options, executable_path=r"/usr/local/bin/chromedriver")
        # Opening the url from inputted website
        browser.get('https://eclass.yorku.ca')
        # Finds the username and password element by id and send the keys (credentials) to their respective fill-in box
        username = browser.find_element_by_id('mli')
        username.send_keys('username')  # type username here
        password = browser.find_element_by_id('password')
        password.send_keys('password')  # type password here
        # Clicks the submit button by finding the element name
        elem = browser.find_element_by_name('dologin').click()
        # Bot responds with status and if the courses element ("page-container-4") is visible,
        # then bot response output is "E-class is currently active",
        WebDriverWait(browser, 10).until(
            ec.presence_of_element_located((By.ID, "page-container-4")))  # finds the element for course content by id
    except:
        # Otherwise, if that is not the case, then the bot responds with "E-class is currently down for the moment"
        status = "E-class is currently down for the moment"
    finally:
        await ctx.send(status)
        # The bot wait within 10 second until it finds the courses element visible and logs out
        elem = browser.find_element_by_xpath("//div[@class='dropdown']")
        elem.find_element_by_tag_name('a').click()
        # clicks the dropdown for menu and logout
        elem = browser.find_element_by_xpath("//div[@class='dropdown-menu dropdown-menu-right menu align-tr-br show']")
        elem.find_elements_by_tag_name('a')
        elem.find_elements_by_tag_name('a')[-1].click()


client.run('token')
