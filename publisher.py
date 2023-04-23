import argparse
from datetime import datetime
from threading import Event
from time import sleep

import paho.mqtt.client as mqtt


# Parameters
qos_level = 2
pub_period = 1.0  # [s]


# Global variables
stop_flag = Event()
count = 0


# Parse the command-line arguments
# Expected argument of broker ip address
parser = argparse.ArgumentParser(description="MQTT publisher")
parser.add_argument("broker", type=str, help="The address of the MQTT broker")
args = parser.parse_args()


# MQTT Client callbacks
def on_connect(client, userdata, flags, rc):
    print(f"Connected to {args.broker}...")


def on_disconnect(client, userdata, rc):
    print(f"Disconnected to {args.broker}...")


def on_log(client, userdata, level, buf):
    print(f"Log: {buf}")


# Configure the MQTT client
client = mqtt.Client()
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_log = on_log
client.connect(args.broker, 1883, 60)
"""This handles re-connection automatically including offline buffering.

Check: https://www.eclipse.org/paho/index.php?page=clients/python/docs/index.php#network-loop
"""
client.loop_start()


# Publish a message every second with QoS level 2
while not stop_flag.wait(pub_period):

    print(f"Client is connected: {client.is_connected()}")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    count += 1
    message = f"{count} Hello World! {timestamp}"
    (rc, mid) = client.publish("topic_test", message, qos=qos_level)
    if rc != mqtt.MQTT_ERR_SUCCESS:
        print(f"Error publishing message: {rc}")
    else:
        print(f"Published message: {message}")

