import cv2
import os
from PIL import Image
import pytesseract
import discord
from discord.ext  import commands
from gtts import gTTS
__author__ = 'info-lab'

client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game =  discord.Game("\'타임머신\' 독서")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    #책 1
    if message.content.startswith("!책 1"):
        await message.channel.send(file=discord.File("ta1.png"))
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
        text = pytesseract.image_to_string("ta1.png", lang='kor')
        tts = gTTS( text, lang='ko', slow=False ) 
        tts.save('ta1.mp3')
        embed = discord.Embed(title="타임머신 1장", description=text, color=0x62c1cc)
        embed.set_footer(text="tts로 읽는 타임머신")
        await message.channel.send("타임머신", embed=embed)
        file = discord.File("ta1.mp3")
        await message.channel.send(file=file)
        
        #책 2
    elif message.content.startswith("!책 2"):
        await message.channel.send(file=discord.File("ta2.png"))
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
        text = pytesseract.image_to_string("ta2.png", lang='kor')
        tts = gTTS( text, lang='ko', slow=False ) 
        tts.save('ta2.mp3')
        embed = discord.Embed(title="타임머신 2장", description=text, color=0x62c1cc)
        embed.set_footer(text="tts로 읽는 타임머신")
        await message.channel.send("타임머신", embed=embed)
        file = discord.File("ta2.mp3")
        await message.channel.send(file=file)
        #책 3
    elif message.content.startswith("!책 3"):
        await message.channel.send(file=discord.File("ta3.png"))
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
        text = pytesseract.image_to_string("ta3.png", lang='kor')
        tts = gTTS( text, lang='ko', slow=False ) 
        tts.save('ta3.mp3')
        embed = discord.Embed(title="타임머신 3장", description=text, color=0x62c1cc)
        embed.set_footer(text="tts로 읽는 타임머신")
        await message.channel.send("타임머신", embed=embed)
        file = discord.File("ta3.mp3")
        await message.channel.send(file=file)
        #책 4
    elif message.content.startswith("!책 4"):
        await message.channel.send(file=discord.File("ta4.png"))
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
        text = pytesseract.image_to_string("ta4.png", lang='kor')
        tts = gTTS( text, lang='ko', slow=False ) 
        tts.save('ta4.mp3')
        embed = discord.Embed(title="타임머신 4장", description=text, color=0x62c1cc)
        embed.set_footer(text="tts로 읽는 타임머신")
        await message.channel.send("타임머신", embed=embed)
        file = discord.File("ta4.mp3")
        await message.channel.send(file=file)
        #책 5
    elif message.content.startswith("!책 5"):
        await message.channel.send(file=discord.File("ta5.png"))
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
        text = pytesseract.image_to_string("ta5.png", lang='kor')
        tts = gTTS( text, lang='ko', slow=False ) 
        tts.save('ta5.mp3')
        embed = discord.Embed(title="타임머신 5장", description=text, color=0x62c1cc)
        embed.set_footer(text="tts로 읽는 타임머신")
        await message.channel.send("타임머신", embed=embed)
        file = discord.File("ta5.mp3")
        await message.channel.send(file=file)
        #책 6
    elif message.content.startswith("!책 6"):
        await message.channel.send(file=discord.File("ta6.png"))
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
        text = pytesseract.image_to_string("ta6.png", lang='kor')
        tts = gTTS( text, lang='ko', slow=False ) 
        tts.save('ta6.mp3')
        embed = discord.Embed(title="타임머신 6장", description=text, color=0x62c1cc)
        embed.set_footer(text="tts로 읽는 타임머신")
        await message.channel.send("타임머신", embed=embed)
        file = discord.File("ta6.mp3")
        await message.channel.send(file=file)
        #책 7
    elif message.content.startswith("!책 7"):
        await message.channel.send(file=discord.File("ta7.png"))
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
        text = pytesseract.image_to_string("ta7.png", lang='kor')
        tts = gTTS( text, lang='ko', slow=False ) 
        tts.save('ta7.mp3')
        embed = discord.Embed(title="타임머신 7장", description=text, color=0x62c1cc)
        embed.set_footer(text="tts로 읽는 타임머신")
        await message.channel.send("타임머신", embed=embed)
        file = discord.File("ta7.mp3")
        await message.channel.send(file=file)
        #책 8
    elif message.content.startswith("!책 8"):
        await message.channel.send(file=discord.File("ta8.png"))
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
        text = pytesseract.image_to_string("ta8.png", lang='kor')
        tts = gTTS( text, lang='ko', slow=False ) 
        tts.save('ta8.mp3')
        embed = discord.Embed(title="타임머신 8장", description=text, color=0x62c1cc)
        embed.set_footer(text="tts로 읽는 타임머신")
        await message.channel.send("타임머신", embed=embed)
        file = discord.File("ta8.mp3")
        await message.channel.send(file=file)
        #책 9
    elif message.content.startswith("!책 9"):
        await message.channel.send(file=discord.File("ta9.png"))
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
        text = pytesseract.image_to_string("ta9.png", lang='kor')
        tts = gTTS( text, lang='ko', slow=False ) 
        tts.save('ta9.mp3')
        embed = discord.Embed(title="타임머신 9장", description=text, color=0x62c1cc)
        embed.set_footer(text="tts로 읽는 타임머신")
        await message.channel.send("타임머신", embed=embed)
        file = discord.File("ta9.mp3")
        await message.channel.send(file=file)
        #책 10
    elif message.content.startswith("!책 10"):
        await message.channel.send(file=discord.File("ta10.png"))
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
        text = pytesseract.image_to_string("ta10.png", lang='kor')
        tts = gTTS( text, lang='ko', slow=False ) 
        tts.save('ta10.mp3')
        embed = discord.Embed(title="타임머신 10장", description=text, color=0x62c1cc)
        embed.set_footer(text="tts로 읽는 타임머신")
        await message.channel.send("타임머신", embed=embed)
        file = discord.File("ta10.mp3")
        await message.channel.send(file=file)

client.run("ODE4MjI0MDgzNzk1MzEyNjQy.YEU8jw.UTST5I-okPnDV8p-_yX9aVXafAg")