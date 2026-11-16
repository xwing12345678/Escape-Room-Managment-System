from datetime import datetime,time
from typing import Literal

def create_order(booking_id:int,customer_name:str,room_id:str,booking_time:datetime,start_time,players:int,total_price:int|float,status:Literal['Active','Cancelled']='Active',cancellation_fee:float = 0.0):
    new_order = {
        "booking_id": f"B{booking_id}",
        "customer_name": customer_name,
        "room_id": room_id,
        "booking_date": booking_time,
        "start_time": start_time,
        "players": players,
        "total_price": total_price,
        'status': status,
        "cancellation_fee": customer_name
    }

    return new_order

def toggle_order_status(order:dict)->dict:
    if order['status'] == 'Active':
        order['status'] = 'Cancelled'
    else:
        order['status'] = 'Active'
    return order



