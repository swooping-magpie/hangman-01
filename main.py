from flask import Flask, render_template
from flask_sock import Sock


app = Flask(__name__)
sock = Sock(app)
room_dict: dict = {}


@sock.route('/echo')
def echo(ws):
    while True:
        data = ws.receive()
        ws.send(data)
        print(f'Received {data}')


@sock.route('/room/join/<room_id>')
def join_room(ws, room_id):
    global room_dict
    if room_id not in room_dict:
        room_dict[room_id] = {'num_people': 1}
        room_dict['clients'] = [ws]
    else:
        room_dict[room_id]['num_people'] += 1
        room_dict['clients'].append(ws)

    ws.send(f'You are in room {room_id}.')

    total_people_in_room: int = room_dict[room_id]["num_people"]
    for client in room_dict['clients']:
        if client.connected:
            client.send(f'There are {total_people_in_room} in this room.')
        else:
            room_dict['clients'].remove(client)

    while ws.connected:
        continue


@sock.route('/room/leave/<room_id>')
def leave_room(ws, room_id):
    global room_dict
    room_dict[room_id]['num_people'] -= 1
    message = f'You have left room {room_id}. There are {room_dict[room_id]["num_people"]} in this room'
    ws.send(message)


if __name__ == '__main__':
    # when testing locally, pick your local ipv4 address as the host
    # otherwise it wont work
    app.run(host='192.168.1.129', port=5050, debug=True)
