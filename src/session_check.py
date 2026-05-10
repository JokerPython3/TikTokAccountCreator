import requests
sessionid = input("Enter sessionid -> :")
r = requests.get("https://vm.tiktok.com/ZSky7XAvV/",cookies={"sessionid":sessionid})
print(r.json())
if r.json()["message"] == "success":
    print("Success -> ", sessionid)
else:
    print("faild -> ", sessionid)