def date_fun():
    
    from datetime import datetime

    initial_date='2/9/2016'
    release_date=input("Enter release date (dd/mm/yyyy):")
    prediction_date=input("Enter prediction date(dd/mm/yyyy):")
    #release_date='24/4/2017'
    #prediction_date='24/6/2017'
    
    initial_date= datetime.strptime(initial_date, "%d/%m/%Y")
    release_date = datetime.strptime(release_date, "%d/%m/%Y")
    prediction_date = datetime.strptime(prediction_date, "%d/%m/%Y")



    day1=abs((release_date-initial_date).days)
    day1+=1
    day2=abs((prediction_date-initial_date).days)
    day2+=1
    print(day1)
    print(day2)
    if(day1>366):
        s=int(day1/366)
        day1=day1-s*366
        
    if(day2>366):
        s=int(day2/366)
        day2=day2-s*366
    
    days=[]
    days.append(day1)
    days.append(day2)
    #print (days)
    return days

