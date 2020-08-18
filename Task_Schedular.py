import schedule
import time
import datetime

def fun_minute():
    print("Current time is")
    print(datetime.datetime.now())
    print("Schedular executed after Minute")


def fun_Hour():
    print("Current time is")
    print(datetime.datetime.now())
    print("Schedular executed after Hour")

def fun_Day():
    print("Current time is")
    print(datetime.datetime.now())
    print("Schedular executed after Day")

def fun_Afternoon():
    print("Current time is")
    print(datetime.datetime.now())
    print("Schedular executed after Afternoon")

def main():
     print("this program use Automation ")

     print("Python Job Schedular")
     print(datetime.datetime.now())

     schedule.every(1).minutes.do(fun_minute)
     
     schedule.every().hour.do(fun_Hour)

     schedule.every().day.at("00.00").do(fun_Afternoon)
     
     schedule.every().sunday.do(fun_Day)

     schedule.every(1).saturday.at("15.20").do(fun_Day)

     while True:
         schedule.run_pending()
         time.sleep(1)

if __name__=="__main__":
 main()
     