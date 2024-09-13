import time

waiting_time = 1
attemt = 0 
max_retry = 5

while (attemt < max_retry):
    print("Atempt",attemt+1,"waiting_time",waiting_time)
    time.sleep(waiting_time)
    attemt = attemt+1
    waiting_time = waiting_time*2