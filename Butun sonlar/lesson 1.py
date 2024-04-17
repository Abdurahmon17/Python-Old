import datetime

year = int(input("Tug'ilgan yillingizni kiriting - "))
mothr = int(input("Tug'ilgan oyingizni kiriting - "))
day = int(input("Tug'ilgan kuningizni kiriting - "))

birth = datetime.datetime(year, mothr, day)
now = datetime.datetime.now()

harq = now-birth

m = harq.days < 10000

print(harq)
print("b = ",m)
