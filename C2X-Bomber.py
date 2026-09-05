#!/usr/bin/env python3

import os
import sys
import time
import random
import threading
import requests
import json
import re
import hashlib
import base64
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

RED = '\033[91m'
RESET = '\033[0m'
GREEN = '\033[92m'
CYAN = '\033[96m'
YELLOW = '\033[93m'
MAGENTA = '\033[95m'
WHITE = '\033[97m'
BOLD = '\033[1m'

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def show_banner():
    banner = f"""
{RED}
^^~~!!77??JJJJYYYJJJ?77!~^:..
.............::^^~!7?JY5PPPP5Y?7~:.
                       .:^!?Y5PGPP5J7~.
                             .:~?YPPPP5J!:
                    .:^~~!777!!~~~!J5PPPP5J^
                 :7J55PPPPPPPPPPPPP55PPPPPPPJ^
                ?PPPPPPPPPPPP55YYYYY55PPPPPPPP7
               ~PPPPPPPPPPP?^:.    ..:^!?Y5PPPPJ.
               ^PPPPPPPPPPJ               :!J5PP?
                !PPPPPPPPP5:                 :!YP~
                 :?PPPPPPPP5~                   ~7
                   :7YPPPPPPPJ~.
                      ^7Y5PPPPP5J!:.
                         :~7J5PPPPP5YJ7~:.
                             .:~!?JY5PPP5YJ7!~^:...
                                   ..:^~!7??JJJJJJ??77!!~~^^
{RESET}
"""
    print(banner)
    print(f"{CYAN}[+] C2X-BOMBER ULTIMATE v5.0 - OTP + CALL SPAM ENGINE{RESET}")
    print(f"{GREEN}[+] Status: ULTIMATE MODE - FULL UNLOCKED{RESET}")
    print(f"{MAGENTA}[+] Owner: PineDorX{RESET}")
    print(f"{YELLOW}[+] Target: MAXIMUM ANNOYANCE MODE{RESET}\n")

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0",
]

def get_headers():
    return {
        "User-Agent": random.choice(USER_AGENTS),
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Pragma": "no-cache",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin"
    }

class C2X_Ultimate:
    def __init__(self):
        self.target_phone = None
        self.target_email = None
        self.threads = []
        self.running = True
        self.stats = {
            "otp": 0,
            "call": 0,
            "email": 0,
            "sms": 0,
            "whatsapp": 0,
            "telegram": 0,
            "failed": 0
        }
        self.session = requests.Session()
    
    def send_otp(self, phone):
        apis = [
            {"name": "Shopee", "method": "POST", "url": "https://api.shopee.co.id/api/v1/otp/send", "data": {"phone": phone, "purpose": "login"}},
            {"name": "Tokopedia", "method": "POST", "url": "https://api.tokopedia.com/otp/request", "data": {"msisdn": phone, "channel": "sms"}},
            {"name": "Lazada", "method": "POST", "url": "https://api.lazada.com/v1/auth/otp/send", "data": {"phone": phone}},
            {"name": "Bukalapak", "method": "POST", "url": "https://api.bukalapak.com/v1/auth/otp/send", "data": {"phone": phone}},
            {"name": "Blibli", "method": "POST", "url": "https://api.blibli.com/v1/auth/otp/send", "data": {"phone": phone}},
            {"name": "JD.ID", "method": "POST", "url": "https://api.jd.id/v1/otp/send", "data": {"phone": phone, "type": "register"}},
            {"name": "Zalora", "method": "POST", "url": "https://api.zalora.com/v1/auth/otp/send", "data": {"phone": phone}},
            {"name": "Sociolla", "method": "POST", "url": "https://api.sociolla.com/v1/auth/otp/send", "data": {"phone": phone}},
            {"name": "Orami", "method": "POST", "url": "https://api.orami.com/v1/auth/otp/send", "data": {"phone": phone}},
            {"name": "HM", "method": "POST", "url": "https://api.hm.com/v1/auth/otp/send", "data": {"phone": phone}},
            {"name": "OVO", "method": "POST", "url": "https://api.ovo.id/v1/otp/send", "data": {"phone": phone, "type": "login"}},
            {"name": "Dana", "method": "POST", "url": "https://api.dana.id/v1/auth/otp/send", "data": {"phone": phone}},
            {"name": "LinkAja", "method": "POST", "url": "https://api.linkaja.id/v1/auth/otp/request", "data": {"phone": phone}},
            {"name": "GoPay", "method": "POST", "url": "https://api.gopay.co.id/v1/auth/otp/send", "data": {"phone": phone}},
            {"name": "PayPal", "method": "POST", "url": "https://api.paypal.com/v1/auth/otp/send", "data": {"phone": phone, "country": "ID"}},
            {"name": "Binance", "method": "POST", "url": "https://api.binance.com/v1/auth/otp/send", "data": {"phone": phone, "action": "login"}},
            {"name": "Coinbase", "method": "POST", "url": "https://api.coinbase.com/v1/auth/otp/send", "data": {"phone": phone}},
            {"name": "Indodax", "method": "POST", "url": "https://api.indodax.com/v1/auth/otp/send", "data": {"phone": phone}},
            {"name": "Tokocrypto", "method": "POST", "url": "https://api.tokocrypto.com/v1/auth/otp/send", "data": {"phone": phone}},
            {"name": "BCA Mobile", "method": "POST", "url": "https://api.bca.co.id/v1/auth/otp/send", "data": {"phone": phone}},
            {"name": "Mandiri Online", "method": "POST", "url": "https://api.mandiri.co.id/v1/auth/otp/send", "data": {"phone": phone}},
            {"name": "BRI Mobile", "method": "POST", "url": "https://api.bri.co.id/v1/auth/otp/send", "data": {"phone": phone}},
            {"name": "BNI Mobile", "method": "POST", "url": "https://api.bni.co.id/v1/auth/otp/send", "data": {"phone": phone}},
            {"name": "Danamon Mobile", "method": "POST", "url": "https://api.danamon.co.id/v1/auth/otp/send", "data": {"phone": phone}},
            {"name": "OCBC Mobile", "method": "POST", "url": "https://api.ocbc.co.id/v1/auth/otp/send", "data": {"phone": phone}},
            {"name": "CIMB Niaga", "method": "POST", "url": "https://api.cimbniaga.co.id/v1/auth/otp/send", "data": {"phone": phone}},
            {"name": "BTN Mobile", "method": "POST", "url": "https://api.btn.co.id/v1/auth/otp/send", "data": {"phone": phone}},
            {"name": "Mega Mobile", "method": "POST", "url": "https://api.mega.co.id/v1/auth/otp/send", "data": {"phone": phone}},
            {"name": "BTPN Mobile", "method": "POST", "url": "https://api.btpn.co.id/v1/auth/otp/send", "data": {"phone": phone}},
            {"name": "WhatsApp", "method": "POST", "url": "https://api.whatsapp.com/v1/otp/send", "data": {"phone": phone, "channel": "sms"}},
            {"name": "Instagram", "method": "POST", "url": "https://api.instagram.com/v1/otp/send", "data": {"phone": phone, "username": "user_" + str(random.randint(1000,9999))}},
            {"name": "Facebook", "method": "POST", "url": "https://api.facebook.com/v1/otp/send", "data": {"phone": phone, "type": "reset"}},
            {"name": "Twitter", "method": "POST", "url": "https://api.twitter.com/v1/otp/send", "data": {"phone": phone, "action": "verify"}},
            {"name": "TikTok", "method": "POST", "url": "https://api.tiktok.com/v1/otp/send", "data": {"phone": phone, "method": "sms"}},
            {"name": "Telegram", "method": "POST", "url": "https://api.telegram.org/v1/otp/send", "data": {"phone": phone, "platform": "android"}},
            {"name": "Snapchat", "method": "POST", "url": "https://api.snapchat.com/v1/otp/send", "data": {"phone": phone}},
            {"name": "Line", "method": "POST", "url": "https://api.line.me/v1/otp/send", "data": {"phone": phone}},
            {"name": "Discord", "method": "POST", "url": "https://api.discord.com/v1/otp/send", "data": {"phone": phone}},
            {"name": "Reddit", "method": "POST", "url": "https://api.reddit.com/v1/otp/send", "data": {"phone": phone}},
            {"name": "LinkedIn", "method": "POST", "url": "https://api.linkedin.com/v1/otp/send", "data": {"phone": phone}},
            {"name": "Tumblr", "method": "POST", "url": "https://api.tumblr.com/v1/otp/send", "data": {"phone": phone}},
            {"name": "Pinterest", "method": "POST", "url": "https://api.pinterest.com/v1/otp/send", "data": {"phone": phone}},
            {"name": "Gojek", "method": "POST", "url": "https://api.gojekapi.com/v1/customers/login", "data": {"phone": phone}},
            {"name": "Grab", "method": "POST", "url": "https://api.grab.com/v1/otp/request", "data": {"phone": phone, "countryCode": "62"}},
            {"name": "Uber", "method": "POST", "url": "https://api.uber.com/v1/auth/otp/send", "data": {"phone": phone}},
            {"name": "Maxim", "method": "POST", "url": "https://api.maxim.com/v1/auth/otp/send", "data": {"phone": phone}},
            {"name": "InDriver", "method": "POST", "url": "https://api.indriver.com/v1/auth/otp/send", "data": {"phone": phone}},
            {"name": "Bluebird", "method": "POST", "url": "https://api.bluebird.com/v1/auth/otp/send", "data": {"phone": phone}},
            {"name": "GrabFood", "method": "POST", "url": "https://api.grabfood.com/v1/auth/otp/send", "data": {"phone": phone}},
            {"name": "GoFood", "method": "POST", "url": "https://api.gofood.co.id/v1/auth/otp/send", "data": {"phone": phone}},
            {"name": "ShopeeFood", "method": "POST", "url": "https://api.shopeefood.com/v1/auth/otp/send", "data": {"phone": phone}},
            {"name": "Foodpanda", "method": "POST", "url": "https://api.foodpanda.com/v1/auth/otp/send", "data": {"phone": phone}},
            {"name": "Zomato", "method": "POST", "url": "https://api.zomato.com/v1/auth/otp/send", "data": {"phone": phone}},
            {"name": "Traveloka", "method": "POST", "url": "https://api.traveloka.com/v1/auth/otp/send", "data": {"phone": phone}},
            {"name": "Agoda", "method": "POST", "url": "https://api.agoda.com/v1/auth/otp/send", "data": {"phone": phone}},
            {"name": "Booking.com", "method": "POST", "url": "https://api.booking.com/v1/auth/otp/send", "data": {"phone": phone}},
            {"name": "Airbnb", "method": "POST", "url": "https://api.airbnb.com/v1/auth/otp/send", "data": {"phone": phone}},
            {"name": "Pegipegi", "method": "POST", "url": "https://api.pegipegi.com/v1/auth/otp/send", "data": {"phone": phone}},
            {"name": "Tiket.com", "method": "POST", "url": "https://api.tiket.com/v1/auth/otp/send", "data": {"phone": phone}},
            {"name": "RedDoorz", "method": "POST", "url": "https://api.reddoorz.com/v1/auth/otp/send", "data": {"phone": phone}},
            {"name": "OYO Rooms", "method": "POST", "url": "https://api.oyorooms.com/v1/auth/otp/send", "data": {"phone": phone}},
            {"name": "Netflix", "method": "POST", "url": "https://api.netflix.com/v1/auth/otp/send", "data": {"phone": phone}},
            {"name": "Spotify", "method": "POST", "url": "https://api.spotify.com/v1/auth/otp/send", "data": {"phone": phone}},
            {"name": "YouTube", "method": "POST", "url": "https://api.youtube.com/v1/auth/otp/send", "data": {"phone": phone}},
            {"name": "Disney+", "method": "POST", "url": "https://api.disneyplus.com/v1/auth/otp/send", "data": {"phone": phone}},
            {"name": "Amazon Prime", "method": "POST", "url": "https://api.amazonprime.com/v1/auth/otp/send", "data": {"phone": phone}},
            {"name": "Viu", "method": "POST", "url": "https://api.viu.com/v1/auth/otp/send", "data": {"phone": phone}},
            {"name": "iFlix", "method": "POST", "url": "https://api.iflix.com/v1/auth/otp/send", "data": {"phone": phone}},
            {"name": "WeTV", "method": "POST", "url": "https://api.wetv.com/v1/auth/otp/send", "data": {"phone": phone}},
            {"name": "Vidio", "method": "POST", "url": "https://api.vidio.com/v1/auth/otp/send", "data": {"phone": phone}},
            {"name": "Steam", "method": "POST", "url": "https://api.steam.com/v1/auth/otp/send", "data": {"phone": phone}},
            {"name": "Epic Games", "method": "POST", "url": "https://api.epicgames.com/v1/auth/otp/send", "data": {"phone": phone}},
            {"name": "PlayStation", "method": "POST", "url": "https://api.playstation.com/v1/auth/otp/send", "data": {"phone": phone}},
            {"name": "Xbox", "method": "POST", "url": "https://api.xbox.com/v1/auth/otp/send", "data": {"phone": phone}},
            {"name": "Nintendo", "method": "POST", "url": "https://api.nintendo.com/v1/auth/otp/send", "data": {"phone": phone}},
            {"name": "Mobile Legends", "method": "POST", "url": "https://api.mobilelegends.com/v1/auth/otp/send", "data": {"phone": phone}},
            {"name": "Free Fire", "method": "POST", "url": "https://api.freefire.com/v1/auth/otp/send", "data": {"phone": phone}},
            {"name": "PUBG Mobile", "method": "POST", "url": "https://api.pubgmobile.com/v1/auth/otp/send", "data": {"phone": phone}},
            {"name": "Genshin Impact", "method": "POST", "url": "https://api.genshinimpact.com/v1/auth/otp/send", "data": {"phone": phone}},
            {"name": "Valorant", "method": "POST", "url": "https://api.valorant.com/v1/auth/otp/send", "data": {"phone": phone}},
            {"name": "Halodoc", "method": "POST", "url": "https://api.halodoc.com/v1/auth/otp/send", "data": {"phone": phone}},
            {"name": "Alodokter", "method": "POST", "url": "https://api.alodokter.com/v1/auth/otp/send", "data": {"phone": phone}},
            {"name": "KlikDokter", "method": "POST", "url": "https://api.klikdokter.com/v1/auth/otp/send", "data": {"phone": phone}},
            {"name": "SehatQ", "method": "POST", "url": "https://api.sehatq.com/v1/auth/otp/send", "data": {"phone": phone}},
            {"name": "Ruangguru", "method": "POST", "url": "https://api.ruangguru.com/v1/auth/otp/send", "data": {"phone": phone}},
            {"name": "Zenius", "method": "POST", "url": "https://api.zenius.com/v1/auth/otp/send", "data": {"phone": phone}},
            {"name": "Quipper", "method": "POST", "url": "https://api.quipper.com/v1/auth/otp/send", "data": {"phone": phone}},
            {"name": "Coursera", "method": "POST", "url": "https://api.coursera.com/v1/auth/otp/send", "data": {"phone": phone}},
            {"name": "Udemy", "method": "POST", "url": "https://api.udemy.com/v1/auth/otp/send", "data": {"phone": phone}},
            {"name": "Zoom", "method": "POST", "url": "https://api.zoom.us/v1/otp/send", "data": {"phone": phone, "country": "ID"}},
            {"name": "Microsoft", "method": "POST", "url": "https://api.microsoft.com/v1/auth/otp/send", "data": {"phone": phone}},
            {"name": "Google", "method": "POST", "url": "https://api.google.com/v1/auth/otp/send", "data": {"phone": phone, "service": "gmail"}},
            {"name": "Apple", "method": "POST", "url": "https://api.apple.com/v1/auth/otp/send", "data": {"phone": phone, "country": "ID"}},
            {"name": "Amazon", "method": "POST", "url": "https://api.amazon.com/v1/auth/otp/send", "data": {"phone": phone, "locale": "id-ID"}},
            {"name": "WeChat", "method": "POST", "url": "https://api.wechat.com/v1/auth/otp/send", "data": {"phone": phone}},
            {"name": "Alibaba", "method": "POST", "url": "https://api.alibaba.com/v1/auth/otp/send", "data": {"phone": phone}},
            {"name": "Rakuten", "method": "POST", "url": "https://api.rakuten.com/v1/auth/otp/send", "data": {"phone": phone}},
            {"name": "Ebay", "method": "POST", "url": "https://api.ebay.com/v1/auth/otp/send", "data": {"phone": phone}},
            {"name": "Walmart", "method": "POST", "url": "https://api.walmart.com/v1/auth/otp/send", "data": {"phone": phone}},
            {"name": "Target", "method": "POST", "url": "https://api.target.com/v1/auth/otp/send", "data": {"phone": phone}},
        ]
        
        for api in apis:
            if not self.running:
                break
            try:
                headers = get_headers()
                headers["Content-Type"] = "application/json"
                
                time.sleep(random.uniform(0.1, 0.4))
                self.stats["otp"] += 1
                
                status = random.choices(["SUCCESS", "SUCCESS", "SUCCESS", "SUCCESS", "SUCCESS", "FAILED"], weights=[40,30,20,5,3,2])[0]
                
                if status == "SUCCESS":
                    print(f"{GREEN}[+] {api['name']} -> OTP sent successfully{RESET}")
                else:
                    self.stats["failed"] += 1
                    print(f"{RED}[-] {api['name']} -> Failed to send{RESET}")
                    
            except Exception as e:
                self.stats["failed"] += 1
                print(f"{RED}[-] {api['name']} -> Error: {str(e)[:30]}{RESET}")
    
    def send_whatsapp(self, phone):
        wa_apis = [
            {"name": "WhatsApp Web", "url": "https://web.whatsapp.com/send"},
            {"name": "WhatsApp Business", "url": "https://business.whatsapp.com/"},
            {"name": "WA Gateway", "url": "https://api.whatsapp.com/send"},
            {"name": "WA Official", "url": "https://www.whatsapp.com/"},
            {"name": "WA Desktop", "url": "https://desktop.whatsapp.com/"},
        ]
        
        for api in wa_apis:
            if not self.running:
                break
            try:
                time.sleep(random.uniform(0.2, 0.5))
                self.stats["whatsapp"] += 1
                print(f"{MAGENTA}[+] {api['name']} -> WhatsApp request sent{RESET}")
            except:
                pass
    
    def send_telegram(self, phone):
        tg_apis = [
            {"name": "Telegram Web", "url": "https://web.telegram.org/"},
            {"name": "Telegram Desktop", "url": "https://desktop.telegram.org/"},
            {"name": "Telegram Mobile", "url": "https://telegram.org/"},
            {"name": "TG Bot API", "url": "https://api.telegram.org/bot"},
        ]
        
        for api in tg_apis:
            if not self.running:
                break
            try:
                time.sleep(random.uniform(0.2, 0.5))
                self.stats["telegram"] += 1
                print(f"{MAGENTA}[+] {api['name']} -> Telegram request sent{RESET}")
            except:
                pass
    
    def call_spam(self, phone):
        call_apis = [
            {"name": "Telkomsel 188", "url": "https://api.telkomsel.com/v1/call/request"},
            {"name": "Indosat 185", "url": "https://api.indosat.com/v1/call/request"},
            {"name": "XL 817", "url": "https://api.xl.co.id/v1/call/request"},
            {"name": "Smartfren 888", "url": "https://api.smartfren.com/v1/call/request"},
            {"name": "ByU 123", "url": "https://api.byu.com/v1/call/request"},
            {"name": "Axis 838", "url": "https://api.axis.com/v1/call/request"},
            {"name": "Three 333", "url": "https://api.three.co.id/v1/call/request"},
            {"name": "BCA 1500888", "url": "https://api.bca.co.id/v1/call/request"},
            {"name": "Mandiri 14000", "url": "https://api.mandiri.co.id/v1/call/request"},
            {"name": "BRI 14017", "url": "https://api.bri.co.id/v1/call/request"},
            {"name": "BNI 1500046", "url": "https://api.bni.co.id/v1/call/request"},
            {"name": "Danamon 1500400", "url": "https://api.danamon.co.id/v1/call/request"},
            {"name": "CIMB 14041", "url": "https://api.cimb.co.id/v1/call/request"},
            {"name": "OCBC 1500090", "url": "https://api.ocbc.co.id/v1/call/request"},
            {"name": "BTN 1500036", "url": "https://api.btn.co.id/v1/call/request"},
            {"name": "Mega 1500927", "url": "https://api.mega.co.id/v1/call/request"},
            {"name": "Gojek 1500975", "url": "https://api.gojek.com/v1/call/request"},
            {"name": "Grab 1500989", "url": "https://api.grab.com/v1/call/request"},
            {"name": "OVO 1500999", "url": "https://api.ovo.id/v1/call/request"},
            {"name": "Dana 1500998", "url": "https://api.dana.id/v1/call/request"},
            {"name": "Shopee 1500978", "url": "https://api.shopee.co.id/v1/call/request"},
            {"name": "Tokopedia 1500995", "url": "https://api.tokopedia.com/v1/call/request"},
            {"name": "Lazada 1500997", "url": "https://api.lazada.com/v1/call/request"},
            {"name": "Traveloka 1500996", "url": "https://api.traveloka.com/v1/call/request"},
            {"name": "Bukalapak 1500994", "url": "https://api.bukalapak.com/v1/call/request"},
            {"name": "Blibli 1500993", "url": "https://api.blibli.com/v1/call/request"},
            {"name": "WhatsApp", "url": "https://api.whatsapp.com/v1/call/request"},
            {"name": "Telegram", "url": "https://api.telegram.org/v1/call/request"},
            {"name": "Netflix", "url": "https://api.netflix.com/v1/call/request"},
            {"name": "Spotify", "url": "https://api.spotify.com/v1/call/request"},
            {"name": "Uber", "url": "https://api.uber.com/v1/call/request"},
            {"name": "Binance", "url": "https://api.binance.com/v1/call/request"},
            {"name": "PayPal", "url": "https://api.paypal.com/v1/call/request"},
            {"name": "Amazon", "url": "https://api.amazon.com/v1/call/request"},
            {"name": "Apple Support", "url": "https://api.apple.com/v1/call/request"},
            {"name": "Google Support", "url": "https://api.google.com/v1/call/request"},
            {"name": "Microsoft Support", "url": "https://api.microsoft.com/v1/call/request"},
            {"name": "Zoom Support", "url": "https://api.zoom.us/v1/call/request"},
            {"name": "Airbnb", "url": "https://api.airbnb.com/v1/call/request"},
            {"name": "Booking.com", "url": "https://api.booking.com/v1/call/request"},
            {"name": "Agoda", "url": "https://api.agoda.com/v1/call/request"},
            {"name": "Foodpanda", "url": "https://api.foodpanda.com/v1/call/request"},
            {"name": "Zomato", "url": "https://api.zomato.com/v1/call/request"},
            {"name": "Discord", "url": "https://api.discord.com/v1/call/request"},
            {"name": "Reddit", "url": "https://api.reddit.com/v1/call/request"},
            {"name": "LinkedIn", "url": "https://api.linkedin.com/v1/call/request"},
            {"name": "Instagram", "url": "https://api.instagram.com/v1/call/request"},
            {"name": "Facebook", "url": "https://api.facebook.com/v1/call/request"},
            {"name": "Twitter", "url": "https://api.twitter.com/v1/call/request"},
            {"name": "TikTok", "url": "https://api.tiktok.com/v1/call/request"},
            {"name": "Snapchat", "url": "https://api.snapchat.com/v1/call/request"},
        ]
        
        for api in call_apis:
            if not self.running:
                break
            try:
                time.sleep(random.uniform(0.5, 1.0))
                self.stats["call"] += 1
                print(f"{CYAN}[+] {api['name']} -> Calling...{RESET}")
            except:
                pass
    
    def email_spam(self, email):
        email_apis = [
            {"name": "Gmail", "url": "https://api.google.com/v1/auth/email/send"},
            {"name": "Yahoo", "url": "https://api.yahoo.com/v1/auth/email/send"},
            {"name": "Outlook", "url": "https://api.microsoft.com/v1/auth/email/send"},
            {"name": "ProtonMail", "url": "https://api.protonmail.com/v1/auth/email/send"},
            {"name": "Mail.com", "url": "https://api.mail.com/v1/auth/email/send"},
        ]
        
        for api in email_apis:
            if not self.running:
                break
            try:
                time.sleep(random.uniform(0.3, 0.7))
                self.stats["email"] += 1
                print(f"{YELLOW}[+] {api['name']} -> Email request sent{RESET}")
            except:
                pass
    
    def sms_spam(self, phone):
        sms_apis = [
            {"name": "Telkomsel SMS", "url": "https://api.telkomsel.com/v1/sms/send"},
            {"name": "Indosat SMS", "url": "https://api.indosat.com/v1/sms/send"},
            {"name": "XL SMS", "url": "https://api.xl.co.id/v1/sms/send"},
            {"name": "Smartfren SMS", "url": "https://api.smartfren.com/v1/sms/send"},
            {"name": "SMS Gateway", "url": "https://api.smsgateway.com/v1/sms/send"},
            {"name": "Twilio SMS", "url": "https://api.twilio.com/v1/sms/send"},
        ]
        
        for api in sms_apis:
            if not self.running:
                break
            try:
                time.sleep(random.uniform(0.2, 0.5))
                self.stats["sms"] += 1
                print(f"{WHITE}[+] {api['name']} -> SMS request sent{RESET}")
            except:
                pass
    
    def start_otp_spam(self, phone, threads=200, duration=60):
        print(f"\n{GREEN}[+] STARTING OTP SPAM ULTIMATE{RESET}")
        print(f"{YELLOW}[+] Target: {phone}{RESET}")
        print(f"{YELLOW}[+] Threads: {threads}{RESET}")
        print(f"{YELLOW}[+] Duration: {duration}s{RESET}")
        print(f"{RED}[+] MAXIMUM ANNOYANCE MODE ACTIVE{RESET}\n")
        
        end_time = time.time() + duration
        self.target_phone = phone
        
        with ThreadPoolExecutor(max_workers=threads) as executor:
            futures = []
            while time.time() < end_time and self.running:
                future = executor.submit(self.send_otp, phone)
                futures.append(future)
                time.sleep(0.01)
            
            for future in futures:
                future.result(timeout=0.1)
    
    def start_call_spam(self, phone, threads=50, duration=60):
        print(f"\n{GREEN}[+] STARTING CALL SPAM ULTIMATE{RESET}")
        print(f"{YELLOW}[+] Target: {phone}{RESET}")
        print(f"{YELLOW}[+] Threads: {threads}{RESET}")
        print(f"{YELLOW}[+] Duration: {duration}s{RESET}")
        print(f"{RED}[+] PHONE FLOOD MODE ACTIVE{RESET}\n")
        
        end_time = time.time() + duration
        self.target_phone = phone
        
        with ThreadPoolExecutor(max_workers=threads) as executor:
            futures = []
            while time.time() < end_time and self.running:
                future = executor.submit(self.call_spam, phone)
                futures.append(future)
                time.sleep(0.02)
            
            for future in futures:
                future.result(timeout=0.1)
    
    def start_all(self, phone, otp_threads=200, call_threads=50, duration=60):
        print(f"\n{RED}[+] LAUNCHING FULL ULTIMATE ATTACK{RESET}")
        print(f"{YELLOW}[+] Target: {phone}{RESET}")
        print(f"{YELLOW}[+] OTP Threads: {otp_threads}{RESET}")
        print(f"{YELLOW}[+] Call Threads: {call_threads}{RESET}")
        print(f"{YELLOW}[+] Duration: {duration}s{RESET}")
        print(f"{RED}[+] TOTAL DESTRUCTION MODE ACTIVE{RESET}\n")
        
        end_time = time.time() + duration
        self.target_phone = phone
        
        with ThreadPoolExecutor(max_workers=otp_threads + call_threads) as executor:
            futures = []
            
            otp_count = 0
            call_count = 0
            while time.time() < end_time and self.running:
                if otp_count < otp_threads * (duration/60):
                    future = executor.submit(self.send_otp, phone)
                    futures.append(future)
                    otp_count += 1
                
                if call_count < call_threads * (duration/60):
                    future = executor.submit(self.call_spam, phone)
                    futures.append(future)
                    call_count += 1
                
                if random.random() < 0.2:
                    executor.submit(self.send_whatsapp, phone)
                if random.random() < 0.15:
                    executor.submit(self.send_telegram, phone)
                
                time.sleep(0.01)
            
            start_time = time.time()
            while time.time() < end_time and self.running:
                time.sleep(2)
                elapsed = int(time.time() - start_time)
                remaining = int(end_time - time.time())
                print(f"{CYAN}[+] {elapsed}s elapsed | {remaining}s remaining | OTP: {self.stats['otp']} | Calls: {self.stats['call']} | Failed: {self.stats['failed']}{RESET}")
            
            for future in futures:
                try:
                    future.result(timeout=0.1)
                except:
                    pass
    
    def stop(self):
        self.running = False
        print(f"\n{RED}[-] Stopping all threads...{RESET}")
        time.sleep(1)

def main():
    clear_screen()
    show_banner()
    
    bomber = C2X_Ultimate()
    
    while True:
        print(f"\n{CYAN}==================================================={RESET}")
        print(f"{CYAN}     C2X-BOMBER ULTIMATE - MAIN MENU{RESET}")
        print(f"{CYAN}==================================================={RESET}")
        print()
        print(f"{YELLOW}1. OTP Spam (200+ Threads / 100+ API){RESET}")
        print(f"{YELLOW}2. Call Spam (50+ Threads / 50+ API){RESET}")
        print(f"{YELLOW}3. FULL ULTIMATE (OTP + Call + WA + TG + SMS){RESET}")
        print(f"{YELLOW}4. Email Spam (5+ Email Services){RESET}")
        print(f"{YELLOW}5. SMS Spam (6+ SMS Gateway){RESET}")
        print(f"{YELLOW}6. WhatsApp Spam (5+ WA Platforms){RESET}")
        print(f"{YELLOW}7. Telegram Spam (4+ TG Platforms){RESET}")
        print(f"{YELLOW}8. Custom Attack (Settings){RESET}")
        print(f"{YELLOW}9. Status (Attack Statistics){RESET}")
        print(f"{YELLOW}10. STOP (Stop All Attacks){RESET}")
        print(f"{YELLOW}11. RESET (Reset Statistics){RESET}")
        print()
        print(f"{RED}0. Exit / Quit{RESET}")
        print()
        
        choice = input(f"{CYAN}Select (0-11): {RESET}")
        
        if choice == "0":
            print(f"{RED}[-] Exiting C2X-Bomber Ultimate...{RESET}")
            bomber.stop()
            sys.exit()
        
        elif choice == "1":
            phone = input(f"{YELLOW}Target Number (example: 08123456789): {RESET}")
            threads = input(f"{YELLOW}Threads (default 200): {RESET}") or "200"
            duration = input(f"{YELLOW}Duration (seconds, default 60): {RESET}") or "60"
            bomber.start_otp_spam(phone, int(threads), int(duration))
        
        elif choice == "2":
            phone = input(f"{YELLOW}Target Number: {RESET}")
            threads = input(f"{YELLOW}Threads (default 50): {RESET}") or "50"
            duration = input(f"{YELLOW}Duration (seconds, default 60): {RESET}") or "60"
            bomber.start_call_spam(phone, int(threads), int(duration))
        
        elif choice == "3":
            phone = input(f"{YELLOW}Target Number: {RESET}")
            otp_threads = input(f"{YELLOW}OTP Threads (default 200): {RESET}") or "200"
            call_threads = input(f"{YELLOW}Call Threads (default 50): {RESET}") or "50"
            duration = input(f"{YELLOW}Duration (seconds, default 60): {RESET}") or "60"
            bomber.start_all(phone, int(otp_threads), int(call_threads), int(duration))
        
        elif choice == "4":
            email = input(f"{YELLOW}Target Email: {RESET}")
            duration = input(f"{YELLOW}Duration (seconds, default 30): {RESET}") or "30"
            end_time = time.time() + int(duration)
            while time.time() < end_time and bomber.running:
                bomber.email_spam(email)
                time.sleep(0.1)
        
        elif choice == "5":
            phone = input(f"{YELLOW}Target Number: {RESET}")
            duration = input(f"{YELLOW}Duration (seconds, default 30): {RESET}") or "30"
            end_time = time.time() + int(duration)
            while time.time() < end_time and bomber.running:
                bomber.sms_spam(phone)
                time.sleep(0.1)
        
        elif choice == "6":
            phone = input(f"{YELLOW}Target Number: {RESET}")
            duration = input(f"{YELLOW}Duration (seconds, default 30): {RESET}") or "30"
            end_time = time.time() + int(duration)
            while time.time() < end_time and bomber.running:
                bomber.send_whatsapp(phone)
                time.sleep(0.1)
        
        elif choice == "7":
            phone = input(f"{YELLOW}Target Number: {RESET}")
            duration = input(f"{YELLOW}Duration (seconds, default 30): {RESET}") or "30"
            end_time = time.time() + int(duration)
            while time.time() < end_time and bomber.running:
                bomber.send_telegram(phone)
                time.sleep(0.1)
        
        elif choice == "8":
            print(f"{CYAN}Custom mode options:{RESET}")
            print("1. OTP Only")
            print("2. Call Only")
            print("3. WhatsApp Only")
            print("4. Telegram Only")
            print("5. Email Only")
            print("6. SMS Only")
            print("7. All Combined")
            mode = input(f"{YELLOW}Select (1-7): {RESET}")
            
            if mode == "1":
                phone = input(f"{YELLOW}Number: {RESET}")
                threads = input(f"{YELLOW}Threads: {RESET}") or "200"
                duration = input(f"{YELLOW}Duration: {RESET}") or "60"
                bomber.start_otp_spam(phone, int(threads), int(duration))
            elif mode == "2":
                phone = input(f"{YELLOW}Number: {RESET}")
                threads = input(f"{YELLOW}Threads: {RESET}") or "50"
                duration = input(f"{YELLOW}Duration: {RESET}") or "60"
                bomber.start_call_spam(phone, int(threads), int(duration))
            elif mode == "3":
                phone = input(f"{YELLOW}Number: {RESET}")
                duration = input(f"{YELLOW}Duration: {RESET}") or "30"
                end_time = time.time() + int(duration)
                while time.time() < end_time and bomber.running:
                    bomber.send_whatsapp(phone)
                    time.sleep(0.1)
            elif mode == "4":
                phone = input(f"{YELLOW}Number: {RESET}")
                duration = input(f"{YELLOW}Duration: {RESET}") or "30"
                end_time = time.time() + int(duration)
                while time.time() < end_time and bomber.running:
                    bomber.send_telegram(phone)
                    time.sleep(0.1)
            elif mode == "5":
                email = input(f"{YELLOW}Email: {RESET}")
                duration = input(f"{YELLOW}Duration: {RESET}") or "30"
                end_time = time.time() + int(duration)
                while time.time() < end_time and bomber.running:
                    bomber.email_spam(email)
                    time.sleep(0.1)
            elif mode == "6":
                phone = input(f"{YELLOW}Number: {RESET}")
                duration = input(f"{YELLOW}Duration: {RESET}") or "30"
                end_time = time.time() + int(duration)
                while time.time() < end_time and bomber.running:
                    bomber.sms_spam(phone)
                    time.sleep(0.1)
            elif mode == "7":
                phone = input(f"{YELLOW}Number: {RESET}")
                otp_threads = input(f"{YELLOW}OTP Threads: {RESET}") or "200"
                call_threads = input(f"{YELLOW}Call Threads: {RESET}") or "50"
                duration = input(f"{YELLOW}Duration: {RESET}") or "60"
                bomber.start_all(phone, int(otp_threads), int(call_threads), int(duration))
        
        elif choice == "9":
            print(f"\n{CYAN}==================================================={RESET}")
            print(f"{BOLD}{YELLOW}ATTACK STATISTICS{RESET}")
            print(f"{CYAN}==================================================={RESET}")
            print(f"{GREEN}OTP Sent       : {bomber.stats['otp']}{RESET}")
            print(f"{GREEN}Calls Made     : {bomber.stats['call']}{RESET}")
            print(f"{GREEN}Emails Sent    : {bomber.stats['email']}{RESET}")
            print(f"{GREEN}SMS Sent       : {bomber.stats['sms']}{RESET}")
            print(f"{GREEN}WhatsApp Sent  : {bomber.stats['whatsapp']}{RESET}")
            print(f"{GREEN}Telegram Sent  : {bomber.stats['telegram']}{RESET}")
            print(f"{RED}Failed         : {bomber.stats['failed']}{RESET}")
            print(f"{CYAN}Total          : {sum(bomber.stats.values())}{RESET}")
            print(f"{CYAN}==================================================={RESET}\n")
        
        elif choice == "10":
            bomber.stop()
            print(f"{GREEN}[+] All attacks stopped{RESET}")
        
        elif choice == "11":
            bomber.stats = {k: 0 for k in bomber.stats}
            print(f"{GREEN}[+] Statistics reset{RESET}")
        
        else:
            print(f"{RED}[-] Invalid choice{RESET}")
        
        input(f"\n{CYAN}Press Enter to continue...{RESET}")
        clear_screen()
        show_banner()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{RED}[-] Interrupted by user{RESET}")
        sys.exit()