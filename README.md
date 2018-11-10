# RasPi-Telegram

Proof of concept bot written by **Patrick Szalewicz** from [Hochschule Bremen](https://www.hs-bremen.de/internet/de/) for his presentation. This bot uses the Telegram API as well as a Raspberry Pi Zero W to illustrate how IOT devices are working. 

### Features

LED blinking!
What time is it?
Roll the dice!

Special feature: Blink LED at startup if network is present or not.

In my example I used four LEDs wired as following:

- Red = GPIO 21
- Yellow = GPIO 5
- Green = GPIO 10
- White = GPIO 27

Please change the values in the scripts if you use other GPIO pins.

### Installation

This bot requires the following programs:

- python
- telepot
- git
- gpio (should be already installed on Raspbian)
- nano (or any other text editor, like vim)

every command should be issued using the 'sudo' command.
It's easier to do the following once.

```sh
$ sudo su
```

Install the dependencies before you install the bot:

```sh
$ apt install python git nano
$ pip install telepot
```

installing the bot:

```sh
$ git clone https://github.com/fachinformatiker/RasPi-Telegram
$ cd RasPi-Telegram
$ cp opt/* /opt/
$ cd /opt
$ chmod +x *
```

insert your token inside the bot file:
`bot = telepot.Bot('INSERT YOUR BOT TOKEN HERE!')`

```sh
$ nano bot.py
```

autorun at startup:

```sh
$ crontab -e
```
and insert the two lines from the crontab.txt file.


### Development

Want to contribute? Great!

Just clone the repo, add your changes and create a pull request.
You can also create a new issue if you like or contact me via [e-mail](mailto:github@fachinformatiker.app).

### Todos

 - ~~beautify the code~~
 - create a "real" config file

### License

GNU General Public License v3.0