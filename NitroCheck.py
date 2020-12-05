print("███╗   ██╗██╗████████╗██████╗  ██████╗  ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗")
print("████╗  ██║██║╚══██╔══╝██╔══██╗██╔═══██╗██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝")
print("██╔██╗ ██║██║   ██║   ██████╔╝██║   ██║██║     ███████║█████╗  ██║     █████╔╝ ")
print("██║╚██╗██║██║   ██║   ██╔══██╗██║   ██║██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ")
print("██║ ╚████║██║   ██║   ██║  ██║╚██████╔╝╚██████╗██║  ██║███████╗╚██████╗██║  ██╗")
print("╚═╝  ╚═══╝╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝")
print("_______________________________________________________________________________")
import string
print("Imported string")
import requests
print("Imported requests")
import time
print("Imported time")
import random
print("Imported random")
import sys
print("Imported sys")
print("_______________________________________________________________________________")
print("For the following prompts press enter to continue")
start1 = input("Have you placed your codes in codes.txt and proxies in proxies.txt?")
if start1 == "":
    start2 = input("Have you made sure your codes are just 16 digits and don't include links?")
    if start2 == "":
        codeslist = open('codes.txt')
        codeslist = codeslist.readlines()
        proxies_list = open('proxies.txt', 'r')
        proxies_list = proxies_list.readlines()
        for code in codeslist:
            while True:
                try:
                    proxy_index = random.randint(0, len(proxies_list) - 1)
                    proxies = {"http": proxies_list[proxy_index].replace('\n', '').replace(' ', ''), "https": proxies_list[proxy_index].replace('\n', '').replace(' ', '')}
                    url = 'https://discordapp.com/api/v6/entitlements/gift-codes/' + code
                    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
                    headers={'User-Agent':user_agent}
                    request=requests.get(url, headers=headers, proxies=proxies, timeout=2)
                    response = request.json()
                except:
                    try:
                        try:
                            if response['code']==10038:
                                print("Unknown code: {code}".format(code=code.replace('\n', '')))
                            elif request.status_code == 200:
                                print("Code found! {code}".format(code=code.replace('\n', '')))
                                
                            else:
                                print("Unknown status code, perhaps means code was already claimed: {code}".format(code=code.replace('\n', '')))
                            break
                        except:
                             if request.status_code == 429:
                                if response['retry_after'] == 600000:
                                    del proxies_list[proxy_index]
                                    print("Error, unusable proxy {proxy} has been blacklisted or rate limited for a very long time. Deleted from list.".format(proxy=proxies['http']))
                                else:
                                    print("Rate limit on {proxies}, retry time: {retryafter}".format(proxies=proxies['http'], retryafter=response['retry_after']))
                            else:
                                print("Unknown exception")
                            continue
                    except:
                        del proxies_list[proxy_index]
                        print("Error timeout, unusable proxy {proxy}. Deleted from list.".format(proxy=proxies['http']))
                        continue
        print("_______________________________________________________________________________")
        close = input("Press enter to close...")
        if close == "":
            sys.exit()
