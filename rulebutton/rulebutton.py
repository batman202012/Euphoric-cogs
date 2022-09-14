from redbot.core import data_manager
from redbot.core import commands
from redbot.core.bot import Red
from redbot.core.config import Config
import discord
from discord import ui


class rulebutton(commands.Cog):
    """
    Cog for creating the rules buttons
    """

    def __init__(self, bot: Red) -> None:
        self.bot = bot


    class MyView(discord.ui.View): # Create a class called MyView that subclasses discord.ui.View
        @ui.button(label="Accept Rules", style=discord.ButtonStyle.primary, emoji="✅") # Create a button with the label ":sunglasses: Click me!" with color Blurple
        async def rulesAccepted(self, interaction, button):
            role = interaction.guild.get_role(1008771067982131252)
            await interaction.user.add_roles(role)
            await interaction.response.send_message("You've accepted the rules, don't forget to <#916326482819842078> to unlock all channels", ephemeral=True) # Send a message when the button is clicked
        button = discord.ui.Button(label="Discord ToS", style=discord.ButtonStyle.link, emoji="📗", url="https://discord.com/terms") # Create a button with the label ":sunglasses: Click me!" with color Blurple
        async def button_callback(self, interaction, button):
            await interaction.response.send_message("https://discord.com/terms", ephemeral=True) # Send a message when the button is clicked
        @ui.button(label="Discord Community Guidelines", style=discord.ButtonStyle.link, emoji="📕")
        async def communityGuidelines(self, interaction, button, url="https://discord.com/guidelines"):
            await interaction.response.send_message("https://discord.com/guidelines", ephemeral=True)
    
    async def create_menu(self, ctx):
        await ctx.send(view=rulebutton.MyView()) # Send a message with our View class that contains the button