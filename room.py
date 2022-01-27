from uuid import uuid4


def create_a_room(room_dict: dict, username: str) -> dict:
    room_id = uuid4().int
    room_dict[room_id] = {
        username: {
            'game points': 0,
            'lives': 9
        }
    }
    return room_dict


def join_a_room(room_dict: dict, room_id: str, username: str) -> dict:
    room = room_dict[room_id]
    room[username] = {
        'game_points': 0,
        'lives': 9
    }
    return room_dict


def leave_a_room(room_dict: dict, room_id: str, username: str) -> dict:
    room = room_dict[room_id]
    room.pop(username, None)
    return room_dict

