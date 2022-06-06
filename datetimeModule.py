import datetime

if __name__ == "__main__":
    print(datetime.datetime.today().strftime("%Y%m%d"))
    now = datetime.datetime.now()
    print(now)
    then = datetime.datetime(2014,2,26)
    delta = now - then
    print(delta.days)
    print(delta.years)