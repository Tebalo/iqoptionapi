from iqoptionapi.stable_api import IQ_Option 
import json
account=IQ_Option("btebalo@gmail.com","Hesoyam76624449")
_,r=account.connect()
if r !="":
    r=json.loads(r)
    if "method" in r:
        r=account.TWO_FA(method="sms",token=r["token"])
        code=input("Please input SMS CODE\n")
        r=account.TWO_FA(code=code,token=r["token"])
        if r["code"]=="success":
            account.setting_2FA_TOKEN(r["token"])
            check,_=account.connect()
            if check:
                print("Login OK!!")