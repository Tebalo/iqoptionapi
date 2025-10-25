# import time
# from iqoptionapi.stable_api import IQ_Option
# Iq=IQ_Option("btebalo@gmail.com","Hesoyam76624449")
# goal="EURUSD"
# print("get candles")
# print(Iq.get_candles(goal,60,111,time.time()))

from iqoptionapi.stable_api import IQ_Option
import logging

logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(message)s')
I_want_money=IQ_Option("btebalo@gmail.com","Hesoyam76624449")
check, reason=I_want_money.connect()#connect to iqoption
print(check, reason)