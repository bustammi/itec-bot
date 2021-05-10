# itec-bot
This project intends to create the Discord bot that checks the uptime status of Moodle 
(E-Class) Website that York University uses on their courses. 

If the discord admin or bot creator inputs the specified command in a discord channel, 
then the web chrome driver executes and automatically login with username and password.

> If login is successful, 
**the bot in discord channel responds back "E-Class is currently active"**

> If login is not successful,
**the bot in discord channel responds back "E-class is currently down for the moment"**

# Steps

1. Install [Python](https://www.python.org/downloads/)

2. If you have installed the latest version of pip on your system, try typing in your terminal: 

    ```sudo pip3 install -U selenium```

2. Download [Pycharm](https://www.jetbrains.com/pycharm/) or [VSCode](https://www.jetbrains.com/pycharm/)

3. Download [ChromeDriver](https://www.jetbrains.com/pycharm/)

4. **Line 12:** Change or keep the command prefix for discord bot
   ```python 
   client = commands.Bot(command_prefix='!i ')
   ```

5. Ensure the path for chromedriver is in ```/usr/local/bin```or somewhere visible

6. Line 39: Input your username 
```python
  username.send_keys('username')  # type username here
  ```
 
7. Line 41: Input your password
```python
  password.send_keys('password')  # type password here
  ```
  
8. Input your discord bot token [Step-by-step Guide](https://www.writebots.com/discord-bot-token/#:~:text=Generating%20Your%20Token%20Step-by-Step%201%20Go%20to%20the,Add%20Your%20Bot%20to%20a%20Discord%20Server.%20)
