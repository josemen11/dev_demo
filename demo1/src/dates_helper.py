from datetime import date,datetime, timedelta

def append_dates(count_date,convert_end_date):
    dates=[]
    while(count_date<=convert_end_date):
        to_string=count_date.strftime('%#m/%d/%Y')
        dates.append(to_string)
        count_date+= timedelta(days=1)
    return dates    


def get_dates_in_interval(start_date,end_date):
    dates=[]
    if(start_date is None or end_date is None  ):
        return 
    convert_start_date= datetime.strptime(start_date,'%m/%d/%Y').date()
    convert_end_date= datetime.strptime(end_date,'%m/%d/%Y').date()
    count_date=convert_start_date
    if(convert_start_date> convert_end_date):
        return  
    dates=append_dates(count_date,convert_end_date)
    return dates    
    