# RasPi-Telegram

Proof of concept bot written by Patrick Szalewicz from Hochschule Bremen for his presentation. This bot uses the Telegram API as well as a Raspberry Pi Zero W to illustrate how IOT devices are working. 

### Features



### Installation

This bot requires the following programs:

- python
- telepot
- git
- gpio (should be already installed on Raspbian)

every command should be issued using the 'sudo' command.
It's easier to do the following once.

```sh
$ sudo su
```

Install the dependencies before you install the bot:

```sh
$ apt install python git
$ pip install telepot
```

installing the bot:

```sh
$ git clone 
$ NODE_ENV=production node app
```

autorun at startup:

```sh
$ crontab -e
```
and insert the two lines from the crontab.txt file.


### Development

Want to contribute? Great!

Dillinger uses Gulp + Webpack for fast developing.
Make a change in your file and instantanously see your updates!


### Todos

 - Write MORE Tests
 - Add Night Mode

### License

GNU General Public License v3.0