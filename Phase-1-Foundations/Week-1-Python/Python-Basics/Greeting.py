import time

t=int(time.strftime('%H'))

if(t>=5 and t<12):
    print("Good Morning!")
elif(t>=12 and t<16):
    print("Good Afternoon!")
elif(t>=16 and t<20):
    print("Good Evening!")
elif(t>=20 or t<5):
    print("Good Night!")