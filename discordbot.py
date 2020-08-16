from discord.ext import commands
import discord
import os
import traceback
import random
import makewords
import makeweather
from MarkovWords import GenerateText

# 接続に必要なオブジェクトを生成
client = discord.Client()
bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

CHANNEL_ID  =721620922527776789


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    channel = client.get_channel(CHANNEL_ID)   
    
    #--メッセージの感情解析
    RankEmotion = makewords.analyzeWord(message.content)[1]
#    RankEmotion = -0.8

    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content[0] == '/':
        if "天気" in message.content:
            outword = makeweather.analyzeWeather(message.content)
            if outword==0:
                await message.channel.send('あたいその場所しらんわぁ') 
            else:
                await message.channel.send(outword) 

        elif "/help()" == message.content:
            outtext ="""
            2008116 ver1.1　
            ・2017年10月から2020年8月までの3810コメントを学習させた
            ・感情極性による応答は停止中
            
            ・todo・
            -Destiny2のAPIからSawayaka393のアクティビティ履歴を返す
            -makeweatherの精緻化.緊急地震速報にも対応させる
            -学習した単語集合に感情極性を付与する
            """

        else:
            generator = GenerateText.GenerateText()
            gen_txt = generator.generate()
            await message.channel.send(gen_txt) 
            
        # await message.channel.send('ほにゃにゃ！！')
        # await message.channel.send('感情極性実数値：%s'%(RankEmotion))


        # if RankEmotion>0:
        #     RE = abs(RankEmotion)
        #     if (RE>0)&(RE<0.1):
        #         await message.channel.send('それってオモロン？')

        #     elif (RE>=0.1)&(RE<0.2):
        #         await message.channel.send('うれちいいいいいいいいいいいいいいいいいいいいいい')     
            
        #     elif (RE>=0.2)&(RE<0.3):
        #         await message.channel.send('パフェくいてぇな')    

        #     elif (RE>=0.3)&(RE<0.4):
        #         await message.channel.send('ほっ♥ほっ♥')    
                
        #     else:
        #         await message.channel.send('おっおっおっおっおっおっおっおっおっおっおっおっおっおっおっ')       
            
        # elif RankEmotion<0:
        #     RE = abs(RankEmotion)

        #     if (RE>0)&(RE<0.2):
        #         await message.channel.send('うっちゅれぇわ')

        #     elif (RE>=0.2)&(RE<0.4):
        #         await message.channel.send('きょわわ')     
            
        #     elif (RE>=0.4)&(RE<0.6):
        #         await message.channel.send('ぽんち？ちんぽ？')    

        #     elif (RE>=0.6)&(RE<0.8):
        #         await message.channel.send('ヒトリハ…サビシイイイイイイイイイイイイイイイイ')  

        #     else:
        #         await message.channel.send('ほにい')     
                   
        # else:
        #     li = ["あたいもうやだ","あたいもうねるわ","ほにい","それほんほ？"]
            
        #     out_rand = random.choice(li)
            
        #     await message.channel.send(out_rand)

    else:
        return

# Botの起動とDiscordサーバーへの接続
client.run(token)
