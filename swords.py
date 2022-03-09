#!/bin/python3
#andres
#Wed 09 Mar 2022 03:41:42 AM EST

def current_swords(swords):
    print("You currently have", len(swords),"swords: \n",swords)

swords=["Umbra","Penumbra","Avassaladora"]
current_swords(swords)
print("Hm...")
import time
time.sleep(2)
quest=input("Have you ever killed a god? \n")

if quest.casefold()=="yes".casefold() or "y.+".casefold():
    swords.append("Novabreaker")
    import time
    time.sleep(1.5)
    print("...impressive. I shall grant you the equalizer, then.")
    time.sleep(2.5)
    print("You have acquired the Novabreaker.")
    time.sleep(2)
    current_swords(swords)
else:
    time.sleep(2)
    print("...Come back here when you are ready.")
    raise SystemExit()

import time
time.sleep(1)

quest2=input("Are you willing to destroy the city of Naskar?\n")

if quest2.casefold()=="yes".casefold() or "y.+".casefold():
    swords.append("Blade of Destruction")
    print("Hoh..")
    import time
    time.sleep(1.5)
    print("You have passed. You have acquired the Blade of Destruction.")
    current_swords(swords)
else:
    del swords[-1]
    print("I see...")
    time.sleep(1.5)
    print("You are not fit for battle. -1 sword.")
    current_swords(swords)




