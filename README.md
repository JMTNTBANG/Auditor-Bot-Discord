# Auditor-Bot-Discord
An Auditor Bot for Discord created in Python

## Prerequisites

Have the following installed on your system:

1. **[Python 3.10+](https://www.python.org/downloads/)**
2. **[Poetry (For installing required packages)](https://python-poetry.org/docs/#installation)**

## Required Packages

Using **[Poetry](https://python-poetry.org/docs/#installation)** (or manually), please install the following packages using `poetry install`: 

1. **[discord.py](https://pypi.org/project/discord.py/)**

## Configuration

In order to use the script, you will need to create an app with a bot on the **[Discord Developer Portal](https://discord.com/developers/applications)** where you will obtain a **Bot Token**

Once you have done that, you will need to copy the bot token and paste it into a .env file in the top directory. Make sure the file contains the following:

```bash
BOT_TOKEN={YOUR BOT TOKEN HERE}
```