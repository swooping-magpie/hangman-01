import redis


r = redis.Redis(host='127.0.0.1', port=6379)
print(r)
print(r.ping())
pubsub = r.pubsub()
pubsub.subscribe('room')


r.publish('room', 'hello 1')
r.publish('room', 'hello 2')
r.publish('room', 'hello 3')
r.publish('room', 'hello 5')


for message in pubsub.listen():
    data = message.get('data')
    print(data)
