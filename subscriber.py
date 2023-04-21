import paho.mqtt.client as mqtt
from pynput import keyboard

# Function to handle incoming messages
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))

# Function to execute upon connecting to the MQTT broker
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Successful connection to MQTT broker")
    else:
        print("Error connecting to MQTT broker")

# Function to execute upon subscribing to an MQTT topic
def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed to MQTT topic")

# Configure the MQTT client
client = mqtt.Client()
client.on_message = on_message
client.on_connect = on_connect
client.on_subscribe = on_subscribe
client.connect("localhost", 1883, 60)

# Subscribe to the MQTT topic
client.subscribe("topic_test")

# Create keyboard listener
def on_press(key):
    if key == keyboard.Key.esc:
        return False

listener = keyboard.Listener(on_press=on_press)
listener.start()

# Main loop of the script
while True:
    # Wait for incoming MQTT messages
    client.loop()

    # Exit the loop if the "esc" key is pressed
    if not listener.running:
        break
