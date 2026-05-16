
#
# /*
# this tool make account tiktok  75% of accounts band after crateing 
# You asked question why account's band
# i say you because diffrent using device_id and iid in two traffic (send_code, register_verify)
# use one device_id and iid for two traffic 
# and still account band
# you asked why ?
# i say you 
# because the new update tiktok add new verify in crateing account the tiktok add verify of phone mobile and code 
# if response of register return this -> "data":{"captcha":"","desc_url":"","description":"To continue, update to the latest version of the app","email_code_key":"b772b7d8c98e491f2ab71654b2ec4bd2","error_code":2100,"is_register_for_verify":"true"},"message":"error"}
# this mean he need to create account phone number and code
# you say 
# why don't complet this tool and get fake number and code
# i say i don't have api get phone number and code Withstands pressure(يتحمل الضغط)
# if you have device replace device_id and iid in request (send_code,register_verify)
# in line 349 add iid and in line 350 add device_id and in line 537 add device_id and in line 538 add iid
# and if you don't have device
# tool get device from txt file in src/data/device.txt
# if use proxy or use vpn the 90% of account were bands
# in src/data/data.json you can edit thread and others thing
# if retry email >= 1000
# change api email to mail.io and change get inbox and get code
# add proxy in proxy.txt if you have proxy
# all this by -> @ntroatro | S1 | Ntro 
# *\
#

import base64
import hashlib
import hmac
import os
import string
import httpx,json,asyncio,random
from typing import Any
import SignerPy,time
from mailtm import Email
# this libary use mailtm apis 
import aiofiles,sys
with open('proxy.txt', 'r') as f:
    proxylist = [line.strip() for line in f if line.strip()]
class TikTokAccountCreator:
    success = 0
    send_code = 0
    retry = 0
    get_code = 0
    error_code = 0
    retry_register = 0
    retry_email = 0
    def __init__(self) -> None:
        self.proxies = self.__load_proxies()
       
        self.password = self.__load_data()["password"]
        

        
        # self.token = self.__load_data()["token"]
        # self.id = self.__load_data()["id"]
        self.threads = int(self.__load_data()["threads"])
        self.data = self.__get_path()
        
        self.semaphore = asyncio.Semaphore(1) 
    def __get_path(self) -> str:
        if sys.platform == "win32":
            return str(__file__).split("\\main.py")[0] + "\\data\\"
            # if windows
        else:
            return str(__file__).split("/main.py")[0] + "/data/"
            # if unix systems(linux,mac)
    def __load_proxies(self) -> list:
     
        try:
            with open('proxy.txt', 'r') as f:
                return [line.strip() for line in f if line.strip()]
        except FileNotFoundError:
           
            return []
    def __format_proxy(self, proxy_str: str) -> str:
        protoclo = "http://"
        parts = proxy_str.split(':')
        if len(parts) == 4:
            host, port, user, pw = parts
            return f"{protoclo}{user}:{pw}@{host}:{port}"
        elif len(parts) == 2:
            host, port = parts
            return f"{protoclo}{host}:{port}"
        return f"{protoclo}{proxy_str}"
    async def run(self) -> None:
        tasks = []
        for _ in range(self.threads):
            tasks.append(asyncio.create_task(self.crate()))
        await asyncio.gather(*tasks)
    def __client_build(self) -> httpx.AsyncClient:
        
        if self.proxies:
            p = random.choice(self.proxies)
            proxy_url = self.__format_proxy(p)
            
        
            return httpx.AsyncClient(
                proxy=proxy_url,
                http2=False,
                follow_redirects=True,
                
              
            )
  
        return httpx.AsyncClient(http2=False, follow_redirects=True)
        
    # def __client_build(self) -> httpx.AsyncClient:
    #     try:
    #         if proxylist:
    #             p = random.choice(proxylist)
    #             print(p)
                
    #             proxy_url = f"http://{p}" if not p.startswith("http") else p
    #             return httpx.AsyncClient(http2=True, follow_redirects=True, proxy=proxy_url)
    #         else:
    #             return httpx.AsyncClient(http2=True,follow_redirects=True)
    #     except :
    #         return self.__client_build()


        
    def __list_host(self)->list:
        return  [
        "api16-normal-va.tiktokv.com",
        "api16-normal-zr.tiktokv.com",
        "api31-normal-useast2a.tiktokv.com",
        "api16-normal-useast5.us.tiktokv.com",
        "api19-normal-useast8.us.tiktokv.com",
        "api31-normal-alisg.tiktokv.com",
        "api16-normal-c-tw.tiktokv.com",
        "api31-normal-zr.tiktokv.com",
        "api16-normal-no1a.tiktokv.eu",
        "api19-normal-ycru.tiktokv.com",
        "api16-normal.tiktokv.com",
        "api16-normal.ttapis.com",
        "api31-normal.tiktokv.com",
        "api22-normal.tiktokv.com",
        "api19-normal.tiktokv.com",
        "api-normal.tiktokv.com",
        "api21-normal.tiktokv.com",
        "api16-core.tiktokv.com",
        "api16-core-va.tiktokv.com",
        "api32-normal.tiktokv.com",
        "api33-normal.tiktokv.com"
    ]
    def __gen_username_tmail(self) -> str:
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=16))
    def __gen_password_tmail(self) -> str:
        return ''.join(random.choices(string.ascii_letters + string.digits, k=12))
    async def __get_tmail(self) -> dict:
        try:
            loop = asyncio.get_running_loop()

            test = Email()

            username = self.__gen_username_tmail()
            password = self.__gen_password_tmail()

        
            account = await loop.run_in_executor(
                None,
                lambda: test.register(
                    username=username,
                    password=password
                )
            )

            return {
                "status": "success",
                "username": username,
                "password": password,
                "email": test.address,
                "obj": test
            }

        except Exception as e:
            return {
                "status": "error",
                "message": str(e)
            }
    async def __get_inbox_tmail(self,email:str,obj:Email) -> httpx.Response.json:
        try:
            test = obj
            test.address=email
            
            
            return test.message_list()
        except Exception as e:
            return str(e)
    async def __extract_verification_code_tmail(self,inbox:httpx.Response.json) -> str:
        # data =[{'@id': '/messages/69fc8d078c467db17b4d5ec5', '@type': 'Message', 'id': '69fc8d078c467db17b4d5ec5', 'msgid': '<fc6e0b12-e67e-4788-b4da-25fd4cb8cf31.register@account.tiktok.com>', 'from': {'address': 'register@account.tiktok.com', 'name': 'TikTok'}, 'to': [{'address': 'lw42mhle6p6wapw1cv8hdceq@wshu.net', 'name': ''}], 'subject': '708952 is your TikTok code', 'intro': 'Icon Frame Verify your email Click the link or enter the code 708952 This will confirm that l***q@wshu.net is the right email…', 'seen': False, 'isDeleted': False, 'hasAttachments': False, 'size': 11577, 'downloadUrl': '/messages/69fc8d078c467db17b4d5ec5/download', 'sourceUrl': '/sources/69fc8d078c467db17b4d5ec5', 'createdAt': '2026-05-07T13:00:53+00:00', 'updatedAt': '2026-05-07T13:00:55+00:00', 'accountId': '/accounts/69fc8d04e655872c460a4df2'}]
        try:
            subject = inbox[0]["subject"]
            code = subject.split(" is your TikTok code")[0]
            return code
        except (IndexError, KeyError) as e:
            return {"data":{"message":"error extracting verification code","status":"ok","error":str(e)},"message":"error"}
    async def __get_email(self) -> str:
       try:
           response = await httpx.post('https://api.internal.temp-mail.io/api/v3/email/new')
           return response.json()["email"]
       except json.JSONDecodeError as e:
           return e
    async def __get_inbox(self,email:str) -> httpx.Response.json:
       # if response == [] get new email and get new inbox from temp mail so
       try:
          response = await httpx.get(f'https://api.internal.temp-mail.io/api/v3/email/{email}/messages')
          return response.json()
       except json.JSONDecodeError as e:
            return e
    async def __extract_verification_code(self,inbox:httpx.Response.json,email:str) -> str:
        try:
            
            subject = inbox[0]['subject']
            code = subject.split(" is your TikTok code")[0]
           
            return code
        except (IndexError, KeyError) as e:
            return {"data":{"message":"error extracting verification code","status":"ok","error":str(e)},"message":"error"}
            # inbox = await self.__get_inbox(email)
            # return await self.__extract_verification_code(inbox,email)
    def __get_host(self) -> str:
        return random.choice(self.__list_host())
    def __load_data(self) -> dict[str, str : str:str]:
        with open("src/data/data.json","r") as f:
            return json.load(f)
    def __get_device(self) -> dict[str, str : str:str]:
        with open("src/data/devices.txt","r") as f:
            devices = f.read().splitlines()
        device = random.choice(devices)
        device_id,iid,device_type,device_brand,cdid,openudid,secrets,user_agent = device.split(":")
        return {"device_id":device_id,"install_id":iid,"did":device_id,"iid":iid,"openudid":openudid,"device_type":device_type,"device_brand":device_brand,"cdid":cdid,"secrets":secrets,"user-agent":user_agent}
    def __xor(self,String:str) -> str:
        return "".join([hex(ord(c) ^ 5)[2:] for c in String])
    def __get_client_data(self,paylod:dict[str:str,str:str]) -> str:
        # this line from teacher many  thanks to @P_W_7
        return base64.b64encode(json.dumps(paylod, separators=(',', ':')).encode()).decode()
    # شكرن معلمي
    ############################################################
    def __get_graud_keys(self,payload:dict[str:str], params:dict[str:str,str:str], device_id:str, iid:str) -> str:
    
        payload_str = json.dumps(payload, separators=(',', ':'), sort_keys=True)
        param_str = "&".join([f"{k}={v}" for k, v in sorted(params.items())])
        raw_data = f"{device_id}{iid}{param_str}{payload_str}".encode()
        
  
        hash1 = hashlib.sha256(raw_data).digest()
        hash2 = hashlib.sha256(hash1 + b"ticket_salt").digest()
        
        ecc_pub_key_mock = b'\x04' + hash1 + hash2
        
     
        return base64.b64encode(ecc_pub_key_mock).decode()
     
    def __get_key(self,payload:dict[str:str,str:str], params:dict[str:str,str:str], device_id:str, iid:str) -> str:
   
        payload_str = json.dumps(payload, separators=(',', ':'), sort_keys=True)
        param_str = "&".join([f"{k}={v}" for k, v in sorted(params.items())])
        raw_data = f"{param_str}{payload_str}{device_id}{iid}".encode()
        

        signature = hmac.new(b"bd_client_salt", raw_data, hashlib.sha512).digest()
        exact_60_bytes = signature[:60]
        
        encoded_val = base64.b64encode(exact_60_bytes).decode()
        return f"#0{encoded_val}"
        
    async def __send_code(self,client:httpx.AsyncClient) -> httpx.Response:
        device = self.__get_device()
        data =  await self.__get_tmail()
        
        if data["status"] != "success":
            #rate limit in mailtm -> 
            # {'data': {'message': 'error getting temp mail', 'status': 'ok', 'error': {'status': 'error', 'message': '429 Client Error: Too Many Requests for url: https://api.mail.tm/accounts'}}, 'message': 'error'}
            TikTokAccountCreator.retry_email+=1
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Success -> {} | Send Code -> {} | Retry -> {} | Get Code -> {} | Error Get Code -> {} | Retry Email -> {} | Retry Register -> {} ".format(TikTokAccountCreator.success,TikTokAccountCreator.send_code,TikTokAccountCreator.retry,TikTokAccountCreator.get_code,TikTokAccountCreator.error_code,TikTokAccountCreator.retry_email,TikTokAccountCreator.retry_register))
            
            return {"data":{"message":"error getting temp mail","status":"ok","error":data},"message":"error"}
        email = data["email"]
        obj = data["obj"]
        username_tmail = data["username"]
        password_tmail = data["password"]
       

        
     
        
        params = {
            "passport-sdk-version": "6031990",
            "device_platform": "android",
            "os": "android",
            "ssmix": "a",
            "_rticket": str(int(time.time() * 1000)),
            "cdid": device["cdid"],
            "channel": "googleplay",
            "aid": "1233",
            "app_name": "musical_ly",
            "version_code": "370805",
            "version_name": "37.8.5",
            "manifest_version_code": "2023708050",
            "update_version_code": "2023708050",
            "ab_version": "37.8.5",
            "resolution": "900*1600",
            "dpi": "240",
            "device_type": device["device_type"],
            "device_brand": device["device_brand"],
            "language": "en",
            "os_api": "28",
            "os_version": str(random.randint(7,33)) + "." + str(random.randint(0,9)) + "."+str(random.randint(0,9)),
            "ac": "wifi",
            "is_pad": "0",
            "current_region": "TW",
            "app_type": "normal",
            "sys_region": "US",
            "last_install_time": "1752871588",
            "mcc_mnc": "46692",
            "timezone_name": "Asia/Baghdad",
            "carrier_region_v2": "466",
            "residence": "TW",
            "app_language": "en",
            "carrier_region": "TW",
            "timezone_offset": "10800",
            "developer":"S1",
            "host_abi": "arm64-v8a",
            "locale": "en-GB",
            "ac2": "wifi",
            "uoo": "0",
            "op_region": "TW",
            "build_number": "37.8.5",
            "region": "GB",
            "ts": str(int(time.time())),
            #  "iid": "7528525992324908807",
            #         "device_id": "7528525775047132680",
            #  "iid":"7528868319269930784",
            #         "device_id":"7528868258653947424",
            #  "iid": "7528525992324908807",
            #         "device_id": "7528525775047132680",
            # "iid": "7528525992324908807",
            #         "device_id": "7528525775047132680",
            "iid":device["iid"],
            "device_id": device["device_id"],
            "openudid": device["openudid"],
            "support_webview": "1",
            "reg_store_region": "tw",
            "user_selected_region": "0",
            "okhttp_version": "4.2.210.6-tiktok",
            "use_store_region_cookie": "1",
            "app_version":"37.8.5"
        }
        payload = {
        'rules_version': "v2",
        'password':self.__xor(self.password),
        'account_sdk_source': "app",
        'mix_mode': "1",
        'multi_login': "1",
        'type': "34",
        'email': self.__xor(email),
        'email_theme': "2"
        }
        m = SignerPy.sign(params=params,cookie={
    "install_id":params["iid"],
    "passport_csrf_token": device["secrets"],
    "passport_csrf_token_default": device["secrets"],
  
},data=payload)
       
        headers = {
        'User-Agent': device["user-agent"],
        'Connection': "Keep-Alive",
        'Accept-Encoding': "gzip",
        'X-SS-STUB': m['x-ss-stub'],
        'x-tt-pba-enable': "1",
         'tt-ticket-guard-public-key': self.__get_graud_keys(payload=payload,params=params,device_id=params["device_id"],iid=params["iid"]),
    'tt-ticket-guard-client-data': self.__get_client_data(payload),
    'x-bd-client-key': self.__get_key(payload,params,params["device_id"],params["iid"]),
        'x-bd-kmsv': "0",
        'x-tt-dm-status': "login=1;ct=1;rt=8",
        'X-SS-REQ-TICKET': m['x-ss-req-ticket'],
        'x-tt-passport-csrf-token': device["secrets"],
        'sdk-version': "2",
        'x-tt-token': SignerPy.xtoken(),
        'tt-ticket-guard-iteration-version': "0",
        'tt-ticket-guard-version': "3",
        'passport-sdk-settings': "x-tt-token",
        'passport-sdk-sign': "x-tt-token",
        'passport-sdk-version': "6031990",
        'x-tt-bypass-dp': "1",
        'oec-vc-sdk-version': "3.0.5.i18n",
        'x-vc-bdturing-sdk-version': "2.3.8.i18n",
        'x-tt-request-tag': "n=0;nr=011;bg=0",
        'x-tt-pba-enable': "1",
        'X-Ladon': m['x-ladon'],
        'X-Khronos': m['x-khronos'],
        'X-Argus': m['x-argus'],
        'X-Gorgon': m['x-gorgon'],
        
        }
        try:
            response =await client.post("https://api16-normal-c-alisg.tiktokv.com/passport/email/send_code/", data=payload, headers=headers,params=params,cookies={
    "install_id":params["iid"],
    "passport_csrf_token": device["secrets"],
    "passport_csrf_token_default": device["secrets"],
  
})
            
          
            # print("Host -> ", str(response.url).split("/passport/email/send_code/")[0].split("https://")[1])
            
            if response.json()["message"] == "success":
                TikTokAccountCreator.send_code+=1
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Success -> {} | Send Code -> {} | Retry -> {} | Get Code -> {} | Error Get Code -> {} | Retry Email -> {} | Retry Register -> {} ".format(TikTokAccountCreator.success,TikTokAccountCreator.send_code,TikTokAccountCreator.retry,TikTokAccountCreator.get_code,TikTokAccountCreator.error_code,TikTokAccountCreator.retry_email,TikTokAccountCreator.retry_register))
                    
                await asyncio.sleep(3)  
               

                
                
                inbox = await self.__get_inbox_tmail(email,obj=obj)
                if "is your TikTok code" in inbox[0]["subject"]:
                    code = await self.__extract_verification_code_tmail(inbox)
                   
                    TikTokAccountCreator.get_code+=1
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("Success -> {} | Send Code -> {} | Retry -> {} | Get Code -> {} | Error Get Code -> {} | Retry Email -> {} | Retry Register -> {} ".format(TikTokAccountCreator.success,TikTokAccountCreator.send_code,TikTokAccountCreator.retry,TikTokAccountCreator.get_code,TikTokAccountCreator.error_code,TikTokAccountCreator.retry_email,TikTokAccountCreator.retry_register))
                   
                    
                
                   
                    return {"email":email,"email_xor":payload["email"],"device":device,"response":response,"payload":payload,"headers":headers,"params":params,"host":str(response.url).split("/passport/email/send_code/")[0].split("https://")[1],"code":code,"username":username_tmail,"password":password_tmail ,"client_data":headers["tt-ticket-guard-client-data"],"bd-key":headers["x-bd-client-key"],"public-key":headers["tt-ticket-guard-public-key"],"x_token":headers["x-tt-token"]}

                
                
                
                else:
                    TikTokAccountCreator.error_code+=1
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("Success -> {} | Send Code -> {} | Retry -> {} | Get Code -> {} | Error Get Code -> {} | Retry Email -> {} | Retry Register -> {} ".format(TikTokAccountCreator.success,TikTokAccountCreator.send_code,TikTokAccountCreator.retry,TikTokAccountCreator.get_code,TikTokAccountCreator.error_code,TikTokAccountCreator.retry_email,TikTokAccountCreator.retry_register))
                    return {"data":{"message":"verification code not found in inbox","status":"ok","error":inbox},"message":"error"}

            elif response.json()["data"]["error_code"] == 1383:
                TikTokAccountCreator.retry+=1
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Success -> {} | Send Code -> {} | Retry -> {} | Get Code -> {} | Error Get Code -> {} | Retry Email -> {} | Retry Register -> {} ".format(TikTokAccountCreator.success,TikTokAccountCreator.send_code,TikTokAccountCreator.retry,TikTokAccountCreator.get_code,TikTokAccountCreator.error_code,TikTokAccountCreator.retry_email,TikTokAccountCreator.retry_register))
                return {"data":{"message":"IP is blocked for sending code","status":"ok","error":response.text},"message":"error"}
            else:
                TikTokAccountCreator.retry+=1
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Success -> {} | Send Code -> {} | Retry -> {} | Get Code -> {} | Error Get Code -> {} | Retry Email -> {} | Retry Register -> {} ".format(TikTokAccountCreator.success,TikTokAccountCreator.send_code,TikTokAccountCreator.retry,TikTokAccountCreator.get_code,TikTokAccountCreator.error_code,TikTokAccountCreator.retry_email,TikTokAccountCreator.retry_register))
                return {"data":{"message":"error sending code","status":"ok","error":response.text},"message":"error"}
        except Exception as e:
            TikTokAccountCreator.retry+=1
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Success -> {} | Send Code -> {} | Retry -> {} | Get Code -> {} | Error Get Code -> {} | Retry Email -> {} | Retry Register -> {} ".format(TikTokAccountCreator.success,TikTokAccountCreator.send_code,TikTokAccountCreator.retry,TikTokAccountCreator.get_code,TikTokAccountCreator.error_code,TikTokAccountCreator.retry_email,TikTokAccountCreator.retry_register))

            
         
            return {"data":{"message":"error sending code","status":"ok","error":str(e)},"message":"error"}
    async def crate(self) -> dict[str:str,str:str]:
        async with self.__client_build() as client:
            data = await self.__send_code(client=client)
            # print(data)
            
        
            try:
                
                device = data["device"]
                
                email = data["email_xor"]
                email_un = data["email"]
                client_data = data["client_data"]
                x_bd_key = data["bd-key"]
                public_key = data["public-key"]
                
                code = data["code"]
                host = data["host"]
                username_tmail = data["username"]   
                password_tmail = data["password"]
                x_token = data["x_token"]
                params = {
                    "passport-sdk-version": "6031990",
                    "device_platform": "android",
                    "os": "android",
                    "ssmix": "a",
                    "_rticket":  str(int(time.time() * 1000)),
                    "cdid": device["cdid"],
                    "channel": "googleplay",
                    "aid": "1233",
                    "app_name": "musical_ly",
                    "version_code": "370805",
                    "version_name": "37.8.5",
                    "manifest_version_code": "2023708050",
                    "update_version_code": "2023708050",
                    "ab_version": "37.8.5",
                    "resolution": "900*1600",
                    "dpi": "240",
                    "device_type": device["device_type"],
                    "device_brand": device["device_brand"],
                    "language": "en",
                    "os_api": "28",
                    "os_version": str(random.randint(7,33)) + "." + str(random.randint(0,9)) + "."+str(random.randint(0,9)),
                    "ac": "wifi",
                    "is_pad": "0",
                    "current_region": "TW",
                    "app_type": "normal",
                    "sys_region": "US",
                    "last_install_time": "1752871588",
                    "mcc_mnc": "46692",
                    "timezone_name": "Asia/Baghdad",
                    "carrier_region_v2": "466",
                    "residence": "TW",
                    "app_language": "en",
                    "carrier_region": "TW",
                    "timezone_offset": "10800",
                    "host_abi": "arm64-v8a",
                    "developer":"S1",
                    "locale": "en-GB",
                    "ac2": "wifi",
                    "uoo": "0",
                    "op_region": "TW",
                    "build_number": "37.8.5",
                    "region": "GB",
                    "ts": str(int(time.time())),
                    ### [dont tachhhhhhh] iid and device_id 
                    # "iid": "7528525992324908807",
                    # "device_id": "7528525775047132680",
                   
                    # don't tach devices 
                    "iid":device["iid"],
                    "device_id": device["device_id"],
                    # "iid":"7528868319269930784",
                    # "device_id":"7528868258653947424",
                   ###
                   
                    "openudid": device["openudid"],
                    "support_webview": "1",
                    "reg_store_region": "tw",
                    "user_selected_region": "0",
                    "okhttp_version": "4.2.210.6-tiktok",
                    "use_store_region_cookie": "1",
                    "app_version":"37.8.5"
                }
                payload = {
                    'birthday': str(random.randint(1990, 2007)) + "-" + str(random.randint(1, 12)).zfill(2) + "-" + str(random.randint(1, 28)).zfill(2),
                    'fixed_mix_mode': "1",
                    'code': self.__xor(code),
                    'account_sdk_source': "app",
                    'mix_mode': "1",
                    'multi_login': "1",
                    'type': "34",
                    'email': email
                    }
            
                m = SignerPy.sign(params=params,cookie={
        "install_id":params["iid"],
        "passport_csrf_token": device["secrets"],
        "passport_csrf_token_default": device["secrets"],
    
    },data=payload)
                headers = {
                    'User-Agent': device["user-agent"],
                    'Connection': "Keep-Alive",
                    'Accept-Encoding': "gzip",
                    'X-SS-STUB': m['x-ss-stub'],
                    'x-tt-pba-enable': "1",
                    'x-bd-kmsv': "0",
                       'tt-ticket-guard-public-key':public_key,
    'tt-ticket-guard-client-data':client_data ,
    'x-bd-client-key': x_bd_key,
                    'x-tt-dm-status': "login=1;ct=1;rt=8",
                    'X-SS-REQ-TICKET':  m['x-ss-req-ticket'],
                    
                    'x-tt-passport-csrf-token': device["secrets"],
                     'x-tt-token': x_token,
                
                    'sdk-version': "2",
                    'tt-ticket-guard-iteration-version': "0",
                    'tt-ticket-guard-version': "3",
                    'passport-sdk-settings': "x-tt-token",
                    'passport-sdk-sign': "x-tt-token",
                    'passport-sdk-version': "6031990",
                    'x-tt-bypass-dp': "1",
                    'oec-vc-sdk-version': "3.0.5.i18n",
                    'x-vc-bdturing-sdk-version': "2.3.8.i18n",
                    'x-tt-request-tag': "n=0;nr=011;bg=0",
                    'x-tt-pba-enable': "1",
                    'X-Ladon': m['x-ladon'],
                    'X-Khronos': m['x-khronos'],
                    'X-Argus': m['x-argus'],
                    'X-Gorgon': m['x-gorgon'],

                    }    
                response = await client.post("https://api16-normal-c-alisg.tiktokv.com/passport/email/register_verify_login/", data=payload, headers=headers,params=params,cookies={
        "install_id":params["iid"],
        "passport_csrf_token": device["secrets"],
        "passport_csrf_token_default": device["secrets"],
    })
               
               
            
                try:
                    sessionid = response.json()["data"]["session_key"]
                    TikTokAccountCreator.success +=1
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("Success -> {} | Send Code -> {} | Retry -> {} | Get Code -> {} | Error Get Code -> {} | Retry Email -> {} | Retry Register -> {} ".format(TikTokAccountCreator.success,TikTokAccountCreator.send_code,TikTokAccountCreator.retry,TikTokAccountCreator.get_code,TikTokAccountCreator.error_code,TikTokAccountCreator.retry_email,TikTokAccountCreator.retry_register))
                   
                
                    
                
                    username = response.json()["data"]["name"]
                    id = response.json()["data"]["user_id"]
                    async with aiofiles.open(self.data + "accounts.json","a") as f:
                        await f.write(json.dumps({"username":username,"id":id,"sessionid":sessionid,"password":self.password,"email":email_un,"username_tmail":username_tmail,"password_tmail":password_tmail,'code':code,"device":device,"programmer":"@ntroatro","programmer_name":"S1"}, indent=4) + "\n")
                    async with aiofiles.open(self.data + "session.txt","a") as f:
                        await f.write(sessionid + "\n")
                    
                   
                    

                except Exception as e:
                    
                    TikTokAccountCreator.retry_register+=1
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("Success -> {} | Send Code -> {} | Retry -> {} | Get Code -> {} | Error Get Code -> {} | Retry Email -> {} | Retry Register -> {} ".format(TikTokAccountCreator.success,TikTokAccountCreator.send_code,TikTokAccountCreator.retry,TikTokAccountCreator.get_code,TikTokAccountCreator.error_code,TikTokAccountCreator.retry_email,TikTokAccountCreator.retry_register))
                    return {"data":{"message":"error creating account","status":"ok","error":response.text},"message":"error"}
            except Exception as e:
                # print(e)
                TikTokAccountCreator.retry_email+=1
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Success -> {} | Send Code -> {} | Retry -> {} | Get Code -> {} | Error Get Code -> {} | Retry Email -> {} | Retry Register -> {} ".format(TikTokAccountCreator.success,TikTokAccountCreator.send_code,TikTokAccountCreator.retry,TikTokAccountCreator.get_code,TikTokAccountCreator.error_code,TikTokAccountCreator.retry_email,TikTokAccountCreator.retry_register))
                return {"data":{"message":"error creating account","status":"ok","error":str(e)},"message":"error"}

# async def main():
#     while True:
#         creator = TikTokAccountCreator()
#         await creator.run()

# asyncio.run(main())
async def worker(creator: TikTokAccountCreator, worker_id: int):

    while True:
        try:
            async with creator.semaphore:
                await creator.crate()
        except Exception as e:
          
            continue

async def main():
    creator = TikTokAccountCreator()
    num_threads = creator.threads
    
   
    tasks = []
    for i in range(num_threads):
        tasks.append(asyncio.create_task(worker(creator, i + 1)))

  
    await asyncio.gather(*tasks, return_exceptions=True)
    
# اهم شي دفايزات متشابه بين اتصالين حتى مينحضر حساب
if __name__ == "__main__":
    asyncio.run(main())
# اذا فعلت vpn تنحضر حساب
# اذا بدون vpn ماينحضر
# {"data":{"captcha":"","desc_url":"","description":"Maximum number of attempts reached. Try again later.","error_code":7},"message":"error"}
# {"data":{"captcha":"","desc_url":"","description":"To continue, update to the latest version of the app","email_code_key":"b772b7d8c98e491f2ab71654b2ec4bd2","error_code":2100,"is_register_for_verify":"true"},"message":"error"}
            
# {"data":{"captcha":"","desc_url":"","description":"Couldn't create account. Try again.","error_code":1388},"message":"error"}
# by -> @ntroatro | S1 | Ntro 
            


    
    
            
