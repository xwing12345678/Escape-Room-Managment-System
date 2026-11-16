from datetime import datetime,date,time,timedelta
from Validations.time_validations import before_datetime
def get_current_date_time()->datetime:
    return datetime.now()
 
def get_time_str_from_datetime(date_time:datetime)->str:
    original_datetime = date_time
    time_string = original_datetime.strftime('%H:%M')
    return time_string

def get_date_str_from_datetime(date_time:datetime)->str:
    original_datetime = date_time
    time_string = original_datetime.strftime('%Y-%m-%d')
    return time_string

def get_time_str_from_time(time_object:time)->str:
    time_string = time_object.isoformat('minutes')
    return time_string

def get_date_str_from_date(date_object:date)->str:
    date_string = date_object.isoformat()
    return date_string

def get_current_time()->time:
    current_datetime = get_current_date_time()
    return current_datetime.time()

def get_current_date()->date:
    current_datetime = get_current_date_time()
    return current_datetime.date()

def get_time_slot_end(start:time,duration:int|float,start_date:date,prep_time:int|float = 15 )->time:
    end_time = datetime.combine(start_date, start) + timedelta(minutes= (duration + prep_time))
    return end_time.time()

def get_time_from_str(time_str:str)->time:
    time_object:time = time.fromisoformat(time_str)
    return time_object
print(get_date_str_from_datetime(datetime.now()))

test_time_str = time(12,39).isoformat('minutes')
test_date = get_current_date()
print(test_time_str)
print(get_time_from_str(test_time_str))
print(get_date_str_from_date(test_date))
print(test_date)

def get_hours_left(game_start:datetime)->int:
    current_datetime = get_current_date_time()
    if not before_datetime(game_start,current_datetime):
        return 0
    delta = game_start - current_datetime
    seconds_until_game = delta.seconds
    hours_until_game = seconds_until_game // 3600
    return hours_until_game

def get_cancellation_percentage(game_start:datetime)->float:
    hours_left = get_hours_left(game_start)
    if hours_left >24:
        return 0.0
    elif hours_left > 6:
        return 0.25
    else:
        return 0.5
    
        










