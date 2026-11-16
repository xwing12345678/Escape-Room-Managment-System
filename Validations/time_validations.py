from datetime import datetime,date,time

def in_time_slice(checked_time:time, start:time,end:time)->bool:
    result = False
    if checked_time>start and checked_time<end:
        return True
    return result


def is_unoccupied_slot(checked_time_start:time,checked_time_end:time, start:time,end:time)->bool:
    if not in_time_slice(checked_time_start,start,end) or in_time_slice(checked_time_end,start,end):
        return False
    return True

def time_in_opened(checked_time:time)->bool:
    start = time(10, 0, 0)
    end = time(22, 0, 0)
    return in_time_slice(checked_time,start,end)

def past_date():
    pass

def game_started():
    pass
    











