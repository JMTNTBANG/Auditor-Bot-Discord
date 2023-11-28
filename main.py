# Import Dependencies
import os
import json
import datetime
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
config = json.loads(open("config.json", "r").read())

# Bot Variables
intents = discord.Intents.default()
intents.auto_moderation = True
intents.members = True
intents.message_content = True
bot = discord.Client(intents=intents)
cmd_tree = discord.app_commands.CommandTree(bot)
del intents


# Bot Code
@bot.event
async def on_ready():
    print(f"Signed in as: {bot.user}")


@bot.event
async def on_automod_rule_create(rule: discord.AutoModRule):
    if config[f"{rule.guild.id}"]["automod"]["rule_create"] == 1:
        embed = discord.Embed(
            title="Automod Rule Created",
            timestamp=datetime.datetime.now()
        )
        info = {
            "Name": (rule.name, True),
            "Creator": (rule.creator.mention, True),
            "ID": (rule.id, True),
        }
        # Trigger
        if rule.trigger.type.name == "keyword":
            info["Type"] = ("Keyword", True)
            keywords = ""
            for keyword in rule.trigger.keyword_filter:
                keywords += f"`{keyword}` "
            info["Keywords"] = (keywords, False)
            patterns = ""
            for pattern in rule.trigger.regex_patterns:
                patterns += f"`{pattern}` "
            info["Patterns"] = (patterns, True)
            whitelist = ""
            for keyword in rule.trigger.allow_list:
                whitelist += f"`{keyword}` "
            info["Whitelist"] = (whitelist, True)
        elif rule.trigger.type.name == "keyword_preset":
            info["Type"] = ("Preset", True)
            if rule.trigger.presets.profanity:
                info["Preset"] = ("Profanity", False)
            elif rule.trigger.presets.sexual_content:
                info["Preset"] = ("NSFW", False)
            elif rule.trigger.presets.slurs:
                info["Preset"] = ("Slurs", False)
            whitelist = ""
            for keyword in rule.trigger.allow_list:
                whitelist += f"`{keyword}` "
            info["Whitelist"] = (whitelist, True)
        elif rule.trigger.type.name == "mention_spam":
            info["Type"] = ("Ping Spam", True)
            info["Ping Limit"] = (rule.trigger.mention_limit, False)
        elif rule.trigger.type.name == "harmful_link":
            info["Type"] = ("Harmful Links", True)
        elif rule.trigger.type.name == "spam":
            info["Type"] = ("Spam", True)
        for i in info:
            embed.add_field(name=i, value=info[i][0], inline=info[i][1])
        await rule.guild.get_channel(int(config[f"{rule.guild.id}"]["log_channel"])).send(embed=embed)


# Sign In
if __name__ == '__main__':
    bot.run(token)
