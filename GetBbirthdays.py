from datetime import datetime
from collections import defaultdict 

def get_birthdays_per_week(users):
    result = defaultdict(list) 
    today = datetime.today().date()
    
    for user in users:
        name = user["name"]
        birthday_this_year = user["birthday"].date().replace(year=today.year)

        if(birthday_this_year < today):
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
                   
        delta_days = (birthday_this_year - today).days       

        if(delta_days < 7):     
            week_day = birthday_this_year.strftime("%A")              
            if (week_day.lower() in ["saturday", "sunday"]): 
                result['Monday'].append(name)
            else:               
                result[week_day].append(name)

        
    for day, names in result.items():
        print(f"{day}: {names}")    
