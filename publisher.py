import paho.mqtt.client as mqtt
import time
import argparse
from datetime import datetime

# Parse the command-line arguments
parser = argparse.ArgumentParser(description="MQTT publisher")
parser.add_argument("broker", type=str, help="The address of the MQTT broker")
args = parser.parse_args()

# Configure the MQTT client
client = mqtt.Client()
client.connect(args.broker, 1883, 60)

# Publish a message every second with QoS level 2 and offline buffering
while True:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = f"Hello World! {timestamp}"
    (rc, mid) = client.publish("topic_test", message, qos=2, retain=True)
    if rc != mqtt.MQTT_ERR_SUCCESS:
        print(f"Error publishing message: {rc}")
    else:
        print(f"Published message: {message}")
    time.sleep(1)
