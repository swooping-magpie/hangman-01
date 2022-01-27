import websocket
import time
import argparse


base_ws = 'ws://192.168.1.129:5050'


def connect_to_websocket(path: str):
    url = f'{base_ws}{path}'
    ws_one = websocket.WebSocket()
    ws_one.connect(url)
    return ws_one


def echo():
    c = 0
    ws_one = connect_to_websocket(path='/echo')

    while True:
        message = f'hello-{c}'
        ws_one.send(message)
        msg = ws_one.recv()
        print(msg)
        c += 1
        time.sleep(5)


def join_room(room_id):
    ws_one = connect_to_websocket(path=f'/room/join/{room_id}')

    while True:
        msg = ws_one.recv()
        print(msg)


def leave_room(room_id):
    ws_one = connect_to_websocket(path=f'/room/leave/{room_id}')
    message = ws_one.recv()
    print(message)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A script to connect to a local websocket as a client')
    parser.add_argument("function", help="Execute the function in the script.", default="join_room", type=str)
    parser.add_argument("-r", "--roomId", help="Room Id", default="1", type=str)
    args = parser.parse_args()

    if args.function == 'echo':
        echo()
    elif args.function == 'join':
        if args.roomId:
            join_room(args.roomId)
        else:
            raise Exception('Please pass in roomId')
    elif args.function == 'leave':
        if args.roomId:
            leave_room(args.roomId)
        else:
            raise Exception('Please pass in roomId')
    else:
        raise Exception('Invalid function. Please choose "echo", "join", "leave".')
