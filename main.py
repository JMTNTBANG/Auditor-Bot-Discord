# Import Dependencies
import os
try:
    import discord
    import dotenv
except ImportError:
    print("Please Run \"poetry install\" before running the bot")
    exit(1)

# Load .env
dotenv.load_dotenv()
token = os.getenv("BOT_TOKEN")
if token is None:
    print("Please Add Discord Bot Token in .env")
    exit(1)

# Checks for config file
if "config.json" not in os.listdir("./"):
    with open("./config.json", "w") as update:
        update.write("{\n\n}")

# Bot Variables
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = discord.Client(intents=intents)
cmd_tree = discord.app_commands.CommandTree(bot)
del intents


# Bot Code
@bot.event
async def on_ready():
    print(f"Signed in as: {bot.user}")

# Sign In
if __name__ == '__main__':
    bot.run(token)
