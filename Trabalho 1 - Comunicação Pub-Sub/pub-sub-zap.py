from __future__ import print_function
from is_wire.core import Channel, Subscription, Message
import time

# Connect to the broker
channel = Channel("amqp://guest:guest@10.10.0.91:5672")

# Subscribe to the desired topic(s)
subscription = Subscription(channel)
subscription.subscribe(topic = "Aluno.Matheus")
# ... subscription.subscribe(topic="Other.Topic")

message = Message()
message.reply_to = "Matheus"

while True:
    receive = channel.consume()
    print(f'{receive.reply_to}: {receive.body.decode()}')

    message_writer = str(input("Digite sua resposta: "))
    message.body = message_writer.encode('utf-8')

    channel.publish(message, topic = f'Aluno.{receive.reply_to}')

