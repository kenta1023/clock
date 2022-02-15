import time
import datetime
import winsound


timeH=int(input('時：'))
timeM=int(input('分：'))
timeS=int(input('秒：'))
timeA=datetime.timedelta(hours=timeH,minutes=timeM,seconds=timeS)
sec=timeA.total_seconds()

def start():
    for i in range(2):
        winsound.Beep(262,300)
    winsound.Beep(523,300)
    print('タイマースタート')

start()
time_1= time.perf_counter()     #誤差測定のスタート基準値
for i in range(0,int(sec))[::-1]:
    print(datetime.timedelta(seconds=i))
    time.sleep(1)
time_2 = time.perf_counter()   #誤差測定のエンド基準値
print('タイマー終了です')
for i in range(5):
    winsound.Beep(500,500)
error=time_2-time_1-timeS
print('誤差は'+str(error)+'sです')
