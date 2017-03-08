from datetime import datetime, timedelta
h, m = map(int, input().split(' '))
dt = datetime(2017,1,1,hour=h, minute=m)
td = dt - timedelta(minutes=45)
print (td.hour, td.minute)
