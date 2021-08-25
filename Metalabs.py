import requests
import json
import time
import discord
import datetime
from colorama import init
from termcolor import colored
from discord import Webhook, RequestsWebhookAdapter, AsyncWebhookAdapter
import os
import copy
import io
from discord.ext import commands
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import asyncio
import re
from licensing.models import *
from licensing.methods import Key, Helpers
from pypresence import Presence





try:
  to_unicode = unicode
except NameError: 
  to_unicode = str

def ArsenalLogo():
  print(""" 
 █████╗ ██████╗  ██████╗███████╗███╗  ██╗ █████╗ ██╗
██╔══██╗██╔══██╗██╔════╝██╔════╝████╗ ██║██╔══██╗██║
███████║██████╔╝╚█████╗ █████╗  ██╔██╗██║███████║██║
██╔══██║██╔══██╗ ╚═══██╗██╔══╝  ██║╚████║██╔══██║██║
██║  ██║██║  ██║██████╔╝███████╗██║ ╚███║██║  ██║███████╗
╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚══╝╚═╝  ╚═╝╚══════╝""")




# define our clear function 
def clear(): 
  
    # for windows 
    if os.name == 'nt': 
        _ = system('cls') 

def Mainthread():
  clear()
  #client_id = "753034404586324132"
  #RPC = Presence(client_id, pipe=0)
  #RPC.connect() # Start the handshake loop
  #RPC.update(large_image="large", details="Cooking the Competition!", state='v0.0.1', small_image="smal", start=1)

  with open('Token.json') as datas_file:
    global token_loaded
    token_loaded = json.load(datas_file)
    
  with open('Webhook.json') as daters_file:
    global webhook_loaded
    webhook_loaded = json.load(daters_file)    

  ArsenalLogo()
  print("""


Home
----------------------------------------------------------------

Mode 1 | Metalabs Free Auto

Mode 2 | Metalabs Free Manuel

Mode 3 | ZephyrAIO

Mode 4 | Discord Auto Joiner

Mode 5 | Coming Soon...

Mode 6 | Coming Soon...

Mode 7 | Settings
  """)

  ModePicker = input('What mode do you want: ')

  if (ModePicker == '7'):

    clear()

    ArsenalLogo()
    print("""


Settings
----------------------------------------------------------------  

  Mode 1 | Webhook

  Mode 2 | Token                                                                                                                                                                                                               
    """) 

    SettingsPicker = input('What mode do you want: ')
    
    if (SettingsPicker == '1'):

      clear()

      ArsenalLogo()
      print("""


Settings | Webhook
----------------------------------------------------------------  
      """)

      SaveWebhook = input('Enter a Webhook: ')

      data = {
      'Webhook' : SaveWebhook
      }

      with io.open('Webhook.json', 'w', encoding='utf8') as outfile:
          str_ = json.dumps(data,indent=4, sort_keys=True, separators=(',', ': '), ensure_ascii=False)
          outfile.write(to_unicode(str_))
        
      with open('Webhook.json') as data_file:
          Webhook_loaded = json.load(data_file)
      Back = input('Type "back" to go Home: ')
      if (Back == 'back'):
        Mainthread()
    
    if (SettingsPicker == '2'):

      clear()

      ArsenalLogo()
      print("""


Settings | Token
----------------------------------------------------------------  
      """)

      UserToken = input('Enter a Token: ')

      data = {
      'Tokens' : UserToken
      }
      with io.open('Token.json', 'w', encoding='utf8') as outfile:
          str_ = json.dumps(data,indent=4, sort_keys=True, separators=(',', ': '), ensure_ascii=False)
          outfile.write(to_unicode(str_))
        
      with open('Token.json') as data_file:
        token_loaded  = json.load(data_file)

      Back = input('Type "back" to go Home: ')
      if (Back == 'back'):
        Mainthread()
      

  elif (ModePicker == '1'):
    clear()

    ArsenalLogo()
    print("""


MetaLabs Free Account Creation
----------------------------------------------------------------                                                                                                                                                                                                                 
    """)

    Name = input('Whats your Name: ')
    Email = input('Whats your email: ')
    ChannelId = input('Whats the Channel ID: ')

    data = {
    'Name' : str(Name),
    'Email' : str(Email),
    }

    with io.open('ArsenalData.json', 'w', encoding='utf8') as outfile:
      str_ = json.dumps(data,indent=4, sort_keys=True, separators=(',', ': '), ensure_ascii=False)
      outfile.write(to_unicode(str_))

    with open('ArsenalData.json') as data_file:
      data_loaded = json.load(data_file)

    clear()

    ArsenalLogo()
    print(""" ACCOUNT INFORMATION
    """)
    print('['+str(Name)+']')
    print('['+str(Email)+']'"""
----------------------------------------------------------------

    """)

    while True:
      try:
        global link
        
        TOKEN = token_loaded['Tokens']

        client = discord.Client()

        @client.event
        async def on_message(message):
          #Search for a message in discord
          if message.channel.id == int(ChannelId):
            something = message.content
            try:
              embeds = message.embeds # return list of embeds
              for embed in embeds:
                emmi = embed.to_dict() # it's content of embed in dict
            except Exception:
              pass
            global link 
            try:
              linker = re.search("(?P<url>https?://[^\s]+)", something).group("url")
              link = linker.replace("`", "")
              print(link)
            except Exception:
              pass
            try:
              linker = re.search("(?P<url>https?://[^\s]+)", emmi['description']).group("url")
              link = linker.replace("`", "")
              print(link)
            except Exception:
              pass
            start = time.time()
            try:
              r = requests.get(link)
              print('200 OK | Found URL...')
              soup = BeautifulSoup(r.text, "html.parser")
              script = soup.find('script',{ "id" : "__NEXT_DATA__" }).string.strip()

              data = json.loads(script)
              
            
              ReleaseID = data['props']['pageProps']['release']['id']
              AccountID = data['props']['pageProps']['release']['plan']['account']
            except Exception:
              pass
            
            try:
              #Once it found the link try and POST to it with checkout information
              print('200 OK | Found Release ID: %s...' % str(ReleaseID))

              print(colored('200 OK | Found Datadome Cookie','white')) 

              print(colored('200 OK | Generating Checkout','white')) 

              url = "https://portal-api.metalabs.io/v1/checkouts"

              payload="{\"release\":\"%s\",\"billing_details\":{\"name\":\"%s\",\"email\":\"%s\",\"address\":null},\"payment_method\":null}" % (ReleaseID,Name,Email)
              headers = {
                'authority': 'portal-api.metalabs.io',
                'pragma': 'no-cache',
                'cache-control': 'no-cache',
                'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
                'content-type': 'application/json;charset=UTF-8',
                'accept': 'application/json, text/plain, */*',
                'meta-labs-account': AccountID,
                'x-amz-req-id': 'null',
                'x-amz-cf-id': 'null',
                'origin': '%s' % os.path.dirname(link),
                'sec-fetch-site': 'cross-site',
                'sec-fetch-mode': 'cors',
                'sec-fetch-dest': 'empty',
                'referer': '%s' % os.path.dirname(link),
                'accept-language': 'en-US,en;q=0.9',
                'Cookie': '__cfduid=de97e1abd441db95e1f666c44abfa1cf51615409168; datadome=0wQiOdDEaDmdGgUgmsd_X2_NcgKIhMMhppVieTc-Rsr72DX7pLJ28JsLD4Qd-yeoA-BNY-zLJXlEzW6Wjikk34sa0SczMM-GDHWjVKWp.0'
              }   
              
              print(colored('200 OK | Entered Information... | Processing...','white'))

              #Tests to see if the checkout went through
              karry = requests.request("POST", url, headers=headers, data=payload)
              larry = karry.text

              print(karry)

              end = time.time()
              delta = end - start

            


              b_in_dict =  "processing" in larry
              if (b_in_dict == True):
                #The POST was succesfull
                print(colored('200 OK | Succesfully Purchased. Check Email!','green'))  
                
                client = discord.Client()
                webhook = Webhook.from_url(webhook_loaded["Webhook"], adapter=RequestsWebhookAdapter())
                embed = discord.Embed(title='Succesfully Checked Out!', description='', color = discord.Colour.green(), footer='ArsenalFNF')

                embed.add_field(name="Website", value=link)
                embed.add_field(name="Checkout Time", value=str(delta)[:5] + ' Seconds')
                embed.add_field(name="Email", value="||" + Email + "||")
                webhook.send(embed=embed)

              else:
                #The POST was not succesfull
                print(colored('400 Bad Request | OOS/Error. Maybe next time.', 'red'))
                client = discord.Client()
                webhook = Webhook.from_url(webhook_loaded["Webhook"], adapter=RequestsWebhookAdapter())
                embed = discord.Embed(title='Unlucky. OOS/Error.', description='', color = discord.Colour.red())

                embed.add_field(name="Website", value=link)
                embed.add_field(name="Checkout Time", value=str(delta)[:5] + ' Seconds')
                embed.add_field(name="Email", value="||" + Email + "||")
                webhook.send(embed=embed)

              #Prints how long it took to purchase. Usually it was around 200ms but was greatly determined on internet speed
              print("It took %.2f seconds to purchase" % delta)
              link = None
            except Exception:
              pass
        
        client.run(TOKEN, bot=False)

      except Exception:
        pass

    else:
      pass

  elif (ModePicker == '2'):

    clear()

    ArsenalLogo()
    print("""


 MetaLabs Free Account Creation
----------------------------------------------------------------                                                                                                                                                                                                                 
    """)

    Name = input('Whats your Name: ')
    Email = input('Whats your email: ')

    data = {
      'Name' : str(Name),
      'Email' : str(Email),
    }

    with io.open('ArsenalData.json', 'w', encoding='utf8') as outfile:
        str_ = json.dumps(data,indent=4, sort_keys=True, separators=(',', ': '), ensure_ascii=False)
        outfile.write(to_unicode(str_))
      
    with open('ArsenalData.json') as data_file:
        data_loaded = json.load(data_file)

    clear()

    ArsenalLogo()
    print(""" ACCOUNT INFORMATION
    """)
    print('['+str(Name)+']')

    print('['+str(Email)+']'"""
----------------------------------------------------------------

    """)

    BaseLink = input('Whats the Base Link: ')
    PasswordName = input('Password: ')
    start = time.time()

    #This mode does not use discord to find the link but instead asks the user for the link
    url = 'https://%s/purchase?password=%s' % (BaseLink, PasswordName)
    r = requests.get(url)
    print('200 OK | Found URL...')
    soup = BeautifulSoup(r.text, "html.parser")
    script = soup.find('script',{ "id" : "__NEXT_DATA__" }).string.strip()

    data = json.loads(script)

    #Tries to find the ReleaseID of the metalabs link
    ReleaseID = data['props']['pageProps']['release']['id']
    #Tries to find the AccountID of the metalabs website
    AccountID = data['props']['pageProps']['release']['plan']['account']

    #Once it finds the information it needs to will try and POST the checkout information
    print('200 OK | Found Release ID: %s...' % str(ReleaseID))

    print(colored('200 OK | Found Datadome Cookie','white')) 

    print(colored('200 OK | Generating Checkout','white')) 

    url = "https://portal-api.metalabs.io/v1/checkouts"

    payload="{\"release\":\"%s\",\"billing_details\":{\"name\":\"%s\",\"email\":\"%s\",\"address\":null},\"payment_method\":null}" % (ReleaseID,Name,Email)
    headers = {
      'authority': 'portal-api.metalabs.io',
      'pragma': 'no-cache',
      'cache-control': 'no-cache',
      'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
      'sec-ch-ua-mobile': '?0',
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
      'content-type': 'application/json;charset=UTF-8',
      'accept': 'application/json, text/plain, */*',
      'meta-labs-account': AccountID,
      'x-amz-req-id': 'null',
      'x-amz-cf-id': 'null',
      'origin': '%s' % os.path.dirname(url),
      'sec-fetch-site': 'cross-site',
      'sec-fetch-mode': 'cors',
      'sec-fetch-dest': 'empty',
      'referer': '%s' % os.path.dirname(url),
      'accept-language': 'en-US,en;q=0.9',
      'Cookie': '__cfduid=de97e1abd441db95e1f666c44abfa1cf51615409168; datadome=0wQiOdDEaDmdGgUgmsd_X2_NcgKIhMMhppVieTc-Rsr72DX7pLJ28JsLD4Qd-yeoA-BNY-zLJXlEzW6Wjikk34sa0SczMM-GDHWjVKWp.0'
    }    
    end = time.time()
    delta = end - start

    print(colored('200 OK | Entered Information... | Processing...','white'))

    karry = requests.request("POST", url, headers=headers, data=payload)
    print(karry)
    larry = karry.text

    b_in_dict =  "processing" in larry
    if (b_in_dict == True):
      print(colored('200 OK | Succesfully Purchased. Check Email!','green'))
      webhook = Webhook.from_url(Webhook_loaded['Webhook'], adapter=RequestsWebhookAdapter())
      webhook.send("Checked out")
    else:
      print(colored('400 Bad Request | OOS/Error. Maybe next time.', 'red'))


    print("It took %.2f seconds to AApurchase" % delta)

    input('Push Any Key to exit: ')

  elif (ModePicker == '3'):

    clear()

    ArsenalLogo()
    print(""" ACCOUNT INFORMATION
----------------------------------------------------------------
    """)

    ClaimerToken = input("Enter Claimer Token (DO NOT USE YOUR MAIN):")
    ChannelId = input("Enter Channel ID: ")

    TOKEN = token_loaded['Tokens']

    client = discord.Client()


    @client.event
    async def on_message(message):
      #Tries to find a discord link within a discord channel
        if message.channel.id == int(ChannelId):
            something = message.content
            try:
                embeds = message.embeds # return list of embeds
                for embed in embeds:
                    emmi = embed.to_dict() # it's content of embed in dict

            except Exception:
                pass

                global link 
            try:
                linker = re.search("(?P<url>https?://[^\s]+)", something).group("url")
                link = linker.replace("`", "")
                print(link)

            except Exception:
                pass

            try:
                linker = re.search("(?P<url>https?://[^\s]+)", emmi['description']).group("url")
                link = linker.replace("`", "")
                print(link)

            except Exception:
                pass



        try:
            start = time.time()
            page = requests.get(link)

            #Tries to scrape a website for the stockbutton id and find the link associated with it
            soup = BeautifulSoup(page.content, 'html.parser')

            for a in soup.find_all('a', {"id" : "stockButton"}, href=True):
                print("Found the URL:", a['href'])
                laggers = a['href']

            #Once it finds the link it will try and POST information to join the discord server
            url = "https://discord.com/api/v8/invites/%s" % laggers

            payload={}
            headers = {
            'authority': 'discord.com',
            'content-length': '0',
            'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
            'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzg4LjAuNDMyNC4xNDYgU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6Ijg4LjAuNDMyNC4xNDYiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6Imh0dHBzOi8vd3d3Lmdvb2dsZS5jb20vIiwicmVmZXJyaW5nX2RvbWFpbiI6Ind3dy5nb29nbGUuY29tIiwidXRtX3NvdXJjZSI6Imdvb2dsZSIsInV0bV9tZWRpdW0iOiJhZHZlcnRpc2luZyIsInV0bV9jYW1wYWlnbiI6IjIwMjAtMDFfZ29vZ2xlLXVzLXJlZ2lzdHJhdGlvbnMtYnJhbmRfYnJvYWQiLCJ1dG1fY29udGVudCI6Ii0tdDpwYSIsInV0bV90ZXJtIjoiRU5HLVRleHQtQ2hhdC1EZXNrdG9wLU5BLUFsbC1BbGwtQWxsIiwic2VhcmNoX2VuZ2luZSI6Imdvb2dsZSIsInJlZmVycmVyX2N1cnJlbnQiOiIiLCJyZWZlcnJpbmdfZG9tYWluX2N1cnJlbnQiOiIiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo3NjA2OSwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0=',
            'x-context-properties': 'eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6IjgwNDQ5ODkyNDg5OTQwMTc2MCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4MDQ0OTg5MjQ4OTk0MDE3NjMiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4MDc3NTEzOTgwMjgyMTQyNzIifQ==',
            'authorization': ClaimerToken,
            'accept-language': 'en-US',
            'sec-ch-ua-mobile': '?0',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36',
            'accept': '*/*',
            'origin': 'https://discord.com',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://discord.com/channels/804498924899401760/804498924899401763',
            'cookie': '_ga=GA1.2.497515654.1609898159; _gac_UA-53577205-2=1.1609898159.EAIaIQobChMIyJWe_pmG7gIVljizAB1Zpwg2EAAYASAAEgLwnPD_BwE; __cfduid=df5a305facacfcb7bb396a58525537f831612550701; locale=en-US'
            }

            end = time.time()
            delta = end - start

            response = requests.request("POST", url, headers=headers, data=payload)   
            
            print("Got Invite in %s" % delta)
            link = None
        except Exception:
          pass
    client.run(TOKEN, bot=False)

  elif (ModePicker == '4'):

    ArsenalLogo()
    print("""


Discord Invite Joiner
----------------------------------------------------------------  

  Mode 1 | Auto

  Mode 2 | Manuel                                                                                                                                                                                                          
    """) 

    SettingsPicker = input('What mode do you want: ')
    
    if (SettingsPicker == '1'):

      clear()

      ArsenalLogo()
      print("""


  Discord Invite Joiner | Auto
  ----------------------------------------------------------------                                                                                                                                                                                                                 
      """)

      ClaimerToken = input("Enter Claimer Token (DO NOT USE YOUR MAIN):")
      ChannelId = input("Enter Channel ID: ")
      
      clear()

      TOKEN = token_loaded['Tokens']

      client = discord.Client()

      @client.event
      async def on_message(message):
        if message.channel.id == int(ChannelId):
            something = message.content
            try:
                embeds = message.embeds # return list of embeds
                for embed in embeds:
                    emmi = embed.to_dict() # it's content of embed in dict

            except Exception:
                pass

                global link 
            try:
                linker = re.search("(?P<url>https?://[^\s]+)", something).group("url")
                link = linker.replace("`", "")
                print(link)
                DiscordInv = link.rsplit('/', 1)[-1]

            except Exception:
                pass

            try:
                linker = re.search("(?P<url>https?://[^\s]+)", emmi['description']).group("url")
                link = linker.replace("`", "")
                print(link)
                MixedInv = link.rsplit('/', 1)[-1]
                DiscordInv = re.sub('[\W\_]','',MixedInv)


            except Exception:
                pass
            
            start = time.time()
            url = "https://discord.com/api/v8/invites/%s" % DiscordInv

            payload={}
            headers = {
            'authority': 'discord.com',
            'content-length': '0',
            'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
            'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzg4LjAuNDMyNC4xNDYgU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6Ijg4LjAuNDMyNC4xNDYiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6Imh0dHBzOi8vd3d3Lmdvb2dsZS5jb20vIiwicmVmZXJyaW5nX2RvbWFpbiI6Ind3dy5nb29nbGUuY29tIiwidXRtX3NvdXJjZSI6Imdvb2dsZSIsInV0bV9tZWRpdW0iOiJhZHZlcnRpc2luZyIsInV0bV9jYW1wYWlnbiI6IjIwMjAtMDFfZ29vZ2xlLXVzLXJlZ2lzdHJhdGlvbnMtYnJhbmRfYnJvYWQiLCJ1dG1fY29udGVudCI6Ii0tdDpwYSIsInV0bV90ZXJtIjoiRU5HLVRleHQtQ2hhdC1EZXNrdG9wLU5BLUFsbC1BbGwtQWxsIiwic2VhcmNoX2VuZ2luZSI6Imdvb2dsZSIsInJlZmVycmVyX2N1cnJlbnQiOiIiLCJyZWZlcnJpbmdfZG9tYWluX2N1cnJlbnQiOiIiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo3NjA2OSwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0=',
            'x-context-properties': 'eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6IjgwNDQ5ODkyNDg5OTQwMTc2MCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4MDQ0OTg5MjQ4OTk0MDE3NjMiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4MDc3NTEzOTgwMjgyMTQyNzIifQ==',
            'authorization': ClaimerToken,
            'accept-language': 'en-US',
            'sec-ch-ua-mobile': '?0',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36',
            'accept': '*/*',
            'origin': 'https://discord.com',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://discord.com/channels/804498924899401760/804498924899401763',
            'cookie': '_ga=GA1.2.497515654.1609898159; _gac_UA-53577205-2=1.1609898159.EAIaIQobChMIyJWe_pmG7gIVljizAB1Zpwg2EAAYASAAEgLwnPD_BwE; __cfduid=df5a305facacfcb7bb396a58525537f831612550701; locale=en-US'
            }

            end = time.time()
            delta = end - start

            response = requests.request("POST", url, headers=headers, data=payload)
            print(response)   


            

            if resp == "<Response [200]>":
              embed = discord.Embed(title='Succesfully Checked Out!', description='', color = discord.Colour.green(), footer='ArsenalFNF')
              embed.add_field(name="Discord Invite", value=link)
              embed.add_field(name="Checkout Time", value=str(delta)[:5] + ' Seconds')
              webhook.send(embed=embed)  
              print(colored('LFG! Success!','green'))
            else:
              embed = discord.Embed(title='Unlucky OOS or Error', description='', color = discord.Colour.red(), footer='ArsenalFNF')
              embed.add_field(name="Discord Invite", value=link)
              embed.add_field(name="Checkout Time", value=str(delta)[:5] + ' Seconds')
              webhook.send(embed=embed)  
              print(colored('Little to slow on that one, OOS','red'))
            
            print("Got Invite in %s" % delta)
      client.run(TOKEN, bot=False)
    elif (SettingsPicker == '2'):

      clear()

      ArsenalLogo()
      print("""


  Discord Invite Joiner | Manuel
  ----------------------------------------------------------------                                                                                                                                                                                                                 
      """)

      
      ClaimerToken = input("Enter Claimer Token (DO NOT USE YOUR MAIN):")

      Clear()
      MixedInv = input('Input Discord Invite: ')
      DiscordInv = re.sub('[\W\_]','',MixedInv)
      start = time.time()
      url = "https://discord.com/api/v8/invites/%s" % DiscordInv

      payload={}
      headers = {
      'authority': 'discord.com',
      'content-length': '0',
      'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
      'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzg4LjAuNDMyNC4xNDYgU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6Ijg4LjAuNDMyNC4xNDYiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6Imh0dHBzOi8vd3d3Lmdvb2dsZS5jb20vIiwicmVmZXJyaW5nX2RvbWFpbiI6Ind3dy5nb29nbGUuY29tIiwidXRtX3NvdXJjZSI6Imdvb2dsZSIsInV0bV9tZWRpdW0iOiJhZHZlcnRpc2luZyIsInV0bV9jYW1wYWlnbiI6IjIwMjAtMDFfZ29vZ2xlLXVzLXJlZ2lzdHJhdGlvbnMtYnJhbmRfYnJvYWQiLCJ1dG1fY29udGVudCI6Ii0tdDpwYSIsInV0bV90ZXJtIjoiRU5HLVRleHQtQ2hhdC1EZXNrdG9wLU5BLUFsbC1BbGwtQWxsIiwic2VhcmNoX2VuZ2luZSI6Imdvb2dsZSIsInJlZmVycmVyX2N1cnJlbnQiOiIiLCJyZWZlcnJpbmdfZG9tYWluX2N1cnJlbnQiOiIiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo3NjA2OSwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0=',
      'x-context-properties': 'eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6IjgwNDQ5ODkyNDg5OTQwMTc2MCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4MDQ0OTg5MjQ4OTk0MDE3NjMiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4MDc3NTEzOTgwMjgyMTQyNzIifQ==',
      'authorization': ClaimerToken,
      'accept-language': 'en-US',
      'sec-ch-ua-mobile': '?0',
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36',
      'accept': '*/*',
      'origin': 'https://discord.com',
      'sec-fetch-site': 'same-origin',
      'sec-fetch-mode': 'cors',
      'sec-fetch-dest': 'empty',
      'referer': 'https://discord.com/channels/804498924899401760/804498924899401763',
      'cookie': '_ga=GA1.2.497515654.1609898159; _gac_UA-53577205-2=1.1609898159.EAIaIQobChMIyJWe_pmG7gIVljizAB1Zpwg2EAAYASAAEgLwnPD_BwE; __cfduid=df5a305facacfcb7bb396a58525537f831612550701; locale=en-US'
      }

      end = time.time()
      delta = end - start

      response = requests.request("POST", url, headers=headers, data=payload)
      print(response)   



now = datetime.datetime.now()
init()


RSAPubKey = "<RSAKeyValue><Modulus>qTmfRtq0cnfwG3T35SkWNnwKLYLcOp8vrkHUII09v8iSaebz7ZAMx6/oENgerkdTJQxg8IP50lFmuoyoNtCjdDL7pxPu2noHyHSl7StRJ98vIt+cpUhBrcbFCu0wUBxDSpr/+rJuswk4S4n4kNeLH4/97pawj0jzG8x+djzAK2L/1tolkhK94Y4U3tIAR+lxoR8UpH9XdBwBwFCwKgkdolyP9p+AZnTzStj+xD2OX7I32tWKJTBzeDmGWHUDnFzvC0q+3nCicDI0URYzlGxbkN5L7ae1LjvxW8BoJ5UoWkPs2OvS9JEckS+bLgEHkPXjEy7+2RtF7np2kAeQI7zs7Q==</Modulus><Exponent>AQAB</Exponent></RSAKeyValue>"
auth = "WyI0MTUxNTQiLCJubHpjRGxrb1BLZTU5bGFUZXpmTW1NNjNadWEwOVYwVmVkWDZtL09RIl0="



with open('LicenseKey.json') as datass_file:
    global key_loaded
    key_loaded = json.load(datass_file)

b_in_dict =  "Key" in key_loaded
if (b_in_dict == False):
  LicenseKey = input('Input Your License Key: ')

  data = {
  'Key' : LicenseKey
  }

  with io.open('LicenseKey.json', 'w', encoding='utf8') as outfile:
      str_ = json.dumps(data,indent=4, sort_keys=True, separators=(',', ': '), ensure_ascii=False)
      outfile.write(to_unicode(str_))

else:
  pass

with open('LicenseKey.json') as datass_file:
  key_loaded = json.load(datass_file)

time.sleep(.5)
result = Key.activate(token=auth,\
                   rsa_pub_key=RSAPubKey,\
                   product_id=9637, \
                   key=key_loaded["Key"],\
                   machine_code=Helpers.GetMachineCode())

if result[0] == None or not Helpers.IsOnRightMachine(result[0]):
    # an error occurred or the key is invalid or it cannot be activated
    # (eg. the limit of activated devices was achieved)
    print("The license does not work: {0}".format(result[1]))
else:
    # everything went fine if we are here!
    print("The license is valid!")
    os.system("title Arsenal AIO Welcome Back: %s" % key_loaded["Key"])

time.sleep(1)

Mainthread()




   




  
