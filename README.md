# MQTT Simple Python Test

Functional tests and examples for MQTT using Paho libraries.

## Notes

- Python 3.7+ compatible scripts
- Package transactions are being printed to output
- You can check special behaviors like when publisher is having a different QoS than subscriber easily
- You can check offline buffering and client re-connection with broker easily
  (plenty of options, turn client network down for a while, stop the broker, etc.)
- QoS level used by the sender determines the level of confirmation required for 
  successful message delivery, which can affect the QoS level used to deliver the message to the receiver.
