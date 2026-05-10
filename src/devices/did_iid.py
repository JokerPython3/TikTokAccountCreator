import httpx
import json
import uuid
import time
import random
import SignerPy
import secrets

from concurrent.futures import ThreadPoolExecutor
class DeviceGenerator:
    def __init__(self):
       self.tokens = secrets.token_hex(16)
       self.data = str(__file__).split("src/devices/gen.py")[0] + "src/data/"
      
       self.cookies = {
            "passport_csrf_token":self.tokens,
            "passport_csrf_token_default": self.tokens
        }
       self.brands_by_manufacturer = {
    "Samsung": [
        "Galaxy S24 Ultra", "Galaxy S23", "Galaxy S22", 
        "Galaxy Z Fold 5", "Galaxy A54", "Galaxy Note20 Ultra"
    ],
    "OnePlus": [
        "OnePlus 12", "OnePlus 11", "OnePlus 10 Pro", 
        "OnePlus Nord 3", "OnePlus Open"
    ],
    "Xiaomi": [
        "Xiaomi 14 Ultra", "Xiaomi 13 Pro", "Redmi Note 13 Pro", 
        "Poco F5 Pro", "Poco X6 Pro", "Xiaomi Mix Fold 3"
    ],
    "Huawei": [
        "Mate 60 Pro", "P60 Pro", "Nova 11", 
        "Mate X5", "Pura 70 Ultra"
    ],
    "Google": [
        "Pixel 8 Pro", "Pixel 7 Pro", "Pixel 7a", 
        "Pixel Fold", "Pixel 6 Pro"
    ],
    "Oppo": [
        "Find X7 Ultra", "Find X6 Pro", "Reno 11 Pro", 
        "Find N3", "Oppo A98"
    ],
    "Vivo": [
        "Vivo X100 Pro", "Vivo V30 Pro", "iQOO 12", 
        "Vivo X Fold 3"
    ],
    "Realme": [
        "Realme GT5", "Realme 12 Pro+", "Realme GT Neo 5"
    ],
    "Motorola": [
        "Moto Edge 40 Pro", "Moto Razr 40 Ultra", "Moto G84"
    ],
    "Sony": [
        "Xperia 1 V", "Xperia 5 V", "Xperia 10 V"
    ],
    "Asus": [
        "ROG Phone 8", "Zenfone 10"
    ],
    "Honor": [
        "Honor Magic 6 Pro", "Honor 90", "Honor V Purse"
    ]
}
       self.device_manufacturer = random.choice(list(self.brands_by_manufacturer.keys()))
       self.device_brand = random.choice(self.brands_by_manufacturer[self.device_manufacturer])
       self.current_time_ms = int(time.time() * 1000)
       self.current_time_s = int(time.time())
       self.region = random.choice(["US", "EU", "AS", "AF", "SA","FR","DE","GB","IT","ES","RU","CN","JP","KR"])
       self.client = self.__client_build()
    def __client_build(self) -> httpx.Client:
       return httpx.Client(http2=True,follow_redirects=True)
    def gen__device(self):
      payload = {
        "header": {
          "os": "Android",
          "os_version": str(random.choice([9, 10, 11, 12])),
          "os_api": random.choice([28, 29, 30, 31]),
          "device_model": f"SM-{random.randint(1000,9999)}",
          "device_brand": self.device_brand,
          "device_manufacturer":self.device_manufacturer,
          "cpu_abi": "arm64-v8a",
          "density_dpi": 240,
          "display_density": "hdpi",
          "resolution": "900x1600",
          "display_density_v2": "hdpi",
          "resolution_v2": "1600x900",
          "access": "wifi",
          "rom": f"S.c{random.randint(100000,999999)}-{random.randint(1,99)}_{random.randint(10,99)}f",
          "rom_version": f"NE2211_{random.randint(10,99)}_C.{random.randint(10,99)}",
          "language": random.choice(["en", "ar", "fr", "es"]),
          "timezone": 3,
          "tz_name": "Asia/Baghdad",
          "tz_offset": 10800,
          "sim_region": self.region.lower(),
          "carrier": random.choice(["AT&T", "Verizon", "T-Mobile"]),
          "mcc_mnc": "310410",
          "clientudid": str(uuid.uuid4()),
          "openudid": str(uuid.uuid4().hex),
          "channel": "googleplay",
          "not_request_sender": 1,
          "aid": 1233,
          "release_build": f"d8db25e_{random.randint(20250000,20259999)}",
          "ab_version": "40.7.3",
          "gaid_limited": 0,
          "custom": {
            "ram_size": random.choice(["2GB","3GB","4GB"]),
            "dark_mode_setting_value": 1,
            "is_foldable": 0,
            "screen_height_dp": 1067,
            "apk_last_update_time": self.current_time_ms,
            "filter_warn": 0,
            "priority_region": self.region,
            "user_period": 0,
            "is_kids_mode": 0,
            "web_ua": f"Dalvik/2.1.0 (Linux; U; Android 9; SM-NE2211 Build/SKQ1.220617.001)",
            "screen_width_dp": 648,
            "user_mode": -1
          },
          "package": "com.zhiliaoapp.musically",
          "app_version": "40.7.3",
          "app_version_minor": "",
          "version_code": 400703,
          "update_version_code": 2024007030,
          "manifest_version_code": 2024007030,
          "app_name": "musical_ly",
          "tweaked_channel": "googleplay",
          "display_name": "TikTok",
          "sig_hash": uuid.uuid4().hex,
          "cdid": str(uuid.uuid4()),
          "device_platform": "android",
          "git_hash": uuid.uuid4().hex[:7],
          "sdk_version_code": 2050990,
          "sdk_target_version": 30,
          "req_id": str(uuid.uuid4()),
          "sdk_version": "2.5.9",
          "guest_mode": 0,
          "sdk_flavor": "i18nInner",
          "apk_first_install_time": self.current_time_ms,
          "is_system_app": 0
        },
        "magic_tag": "ss_app_log",
        "_gen_time": self.current_time_ms
      }
      paramss = {
          "req_id": payload["header"]["req_id"],
          "device_platform": payload["header"]["device_platform"],
          "os": payload["header"]["os"].lower(),
          "ssmix": "a",
          "_rticket": str(self.current_time_ms),
          "cdid": payload["header"]["cdid"],
          "channel": payload["header"]["channel"],
          "aid": str(payload["header"]["aid"]),
          "app_name": payload["header"]["app_name"],
          "version_code": str(payload["header"]["version_code"]),
          "version_name": payload["header"]["app_version"],
          "manifest_version_code": str(payload["header"]["manifest_version_code"]),
          "update_version_code": str(payload["header"]["update_version_code"]),
          "ab_version": payload["header"]["ab_version"],
          "resolution": payload["header"]["resolution_v2"].replace("x","*"),
          "dpi": str(payload["header"]["density_dpi"]),
          "device_type": payload["header"]["device_model"],
          "device_brand": payload["header"]["device_brand"],
          "language": payload["header"]["language"],
          "os_api": str(payload["header"]["os_api"]),
          "os_version": payload["header"]["os_version"],
          "ac": payload["header"]["access"],
          "is_pad": "0",
          "app_type": "normal",
          "sys_region": self.region,
          "last_install_time": str(self.current_time_s),
          "mcc_mnc": payload["header"]["mcc_mnc"],
          "timezone_name": payload["header"]["tz_name"],
          "carrier_region_v2": payload["header"]["mcc_mnc"][:3],
          "app_language": payload["header"]["language"],
          "carrier_region": self.region,
          "timezone_offset": str(payload["header"]["tz_offset"]),
          "host_abi": payload["header"]["cpu_abi"],
          "locale": payload["header"]["language"],
          "ac2": "unknown",
          "uoo": "1",
          "op_region": self.region,
          "build_number": payload["header"]["app_version"],
          "region": self.region,
          "ts": str(self.current_time_s),
          "openudid": payload["header"]["openudid"],
          "okhttp_version": "4.2.228.19-tiktok",
          "use_store_region_cookie": "1",
      }

      headers = {
        'User-Agent': f"com.zhiliaoapp.musically/2024007030 (Linux; U; Android {payload['header']['os_version']}; {payload['header']['language']}; {payload['header']['device_model']}; Build/SKQ1.220617.001;tt-ok/3.12.13.20)",
        'Accept-Encoding': "gzip",
        'Content-Type': "application/json",
        'x-tt-app-init-region': f"carrierregion={self.region};mccmnc=310410;sysregion={self.region};appregion={self.region}",
        'x-tt-request-tag': "t=0;n=1",
        'x-tt-dm-status': "login=0;ct=0;rt=7",
        'sdk-version': "2",
        'passport-sdk-version': "-1",
        'x-vc-bdturing-sdk-version': "2.3.13.i18n",
        'content-type': "application/json; charset=utf-8"
      }

      url = "https://log-boot.tiktokv.com/service/2/device_register/"

      response = self.client.post(url, data=json.dumps(payload), headers=headers, params=paramss)
      print(response.text)
      try:
        device_id = response.json()["device_id_str"]
        iid = response.json()["install_id_str"]
        return {"device_id":device_id,"iid":iid}
      except Exception as e:
         return {"message":"error","error_code":str(e)}
print(DeviceGenerator().gen__device())