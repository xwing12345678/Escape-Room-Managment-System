from datetime import datetime,date,time,timedelta


def get_current_date_time()->datetime:
    return datetime.now()

def get_hour_str_from_datetime(date_time:datetime)->str:
    original_datetime = date_time
    formatted_datetime = original_datetime.strftime('%H:%M')
    return formatted_datetime

def get_current_time()->time:
    current_datetime = get_current_date_time()
    return current_datetime.time()

def get_current_date()->date:
    current_datetime = get_current_date_time()
    return current_datetime.date()

def get_time_slot_end(start:time,duration:int|float,start_date:date,prep_time:int|float = 15 )->time:
    end_time = datetime.combine(start_date, start) + timedelta(minutes= (duration + prep_time))
    return end_time.time()



def get_until_game_start():
    pass


def get_cancellation_percentage():
    pass









