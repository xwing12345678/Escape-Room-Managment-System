from typing import Literal

def create_room(next_id,name:str,difficulty:Literal['Easy','Medium','Hard'],duration:int,min_players:int,max_player:int,price_per_player:int|float,is_active:bool =True)->dict:
    new_room = {
        "room_id": f'R{next_id}',
        "name": name,
        "difficulty": "Easy",
        "duration":duration ,
        "min_players":min_players,
        "max_players": max_player,
        "price_per_player":price_per_player,
        "is_active":is_active
    }
    return new_room

def toggle_order_status(room:dict)->dict:
    if room['is_active'] == True:
        room['status'] = False
    else:
        room['status'] = False
    return room

