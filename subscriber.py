import argparse
from time import sleep

import paho.mqtt.client as mqtt
from pynput import keyboard

# Parameters
qos_level = 2


# Parse the command-line arguments
# Expected argument of broker ip address
parser = argparse.ArgumentParser(description="MQTT publisher")
parser.add_argument("broker", type=str, help="The address of the MQTT broker")
args = parser.parse_args()


# MQTT Client callbacks
def on_connect(client, userdata, flags, rc):
    print(f"Connected to {args.broker}...")

    # Subscribe to the MQTT topic
    topic = "topic_test"
    print(f"Subscribing to {topic}...")
    client.subscribe(topic, qos=qos_level)


def on_disconnect(client, userdata, rc):
    print(f"Disconnected to {args.broker}...")


def on_log(client, userdata, level, buf):
    print(f"Log: {buf}")


def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))

    # Storing data so we can check for data loss easily
    with open('incoming.txt', 'a') as file:
        file.write(f'{msg.payload}\n')



def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed to MQTT topic")


# Configure the MQTT client
client = mqtt.Client()
client.on_message = on_message
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_log = on_log
client.on_subscribe = on_subscribe
client.connect(args.broker, 1883, 60)
"""This handles re-connection automatically including offline buffering.

Check: https://www.eclipse.org/paho/index.php?page=clients/python/docs/index.php#network-loop
"""
client.loop_start()


# Create keyboard listener
def on_press(key):
    if key == keyboard.Key.esc:
        return False

listener = keyboard.Listener(on_press=on_press)
listener.start()

# Main loop of the script
while True:

    # Exit the loop if the "esc" key is pressed
    if not listener.running:
        break

    sleep(0.1)
