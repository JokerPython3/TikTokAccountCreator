# Auto Creator Account TikTok
# download repo
```bash
git clone https://github.com/JokerPython3/TikTokAccountCreator
```
# add proxy in proxy.txt if you don't have proxy run tool 
```bash
python src/main.py
```
# defculat thread  is 10 you can edit thread in src/data/data.json
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
# in data.json you can edit password accounts
# remember download http2 with downloading httpx
# pip install httpx[http2]
# all this by -> @ntroatro | S1 | Ntro 
# *\
# in src have many file can use it
# ماعندي حيل اشرحهن 