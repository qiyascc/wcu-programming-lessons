import datetime as q
import random as tesaduf

def q(day, hour, minute):
    now = q.datetime.now()
    last_date = now - q.timedelta(days=day, hours=hour, minutes=minute)
    week_day = last_date.weekday()
    names = ["Emil", "Qiyas", "Sadiq", "Şirin"]
    
    if week_day == 5 or week_day == 6:
        random_user = tesaduf.choice(names)
        print(f"{random_user}")
    else:
        print(last_date)
        for name in names:
            print(name)
            
q(56, 18, 25)
