import paho.mqtt.client as paho
from cryptography.fernet import Fernet

broker="broker.mqttdashboard.com"

def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed: "+str(mid)+" "+str(granted_qos))

def on_message(client, userdata, msg):
    decrypted_message = cipher.decrypt(msg.payload)
    print("received message =",str(decrypted_message.decode("utf-8")))
    print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))    

#cipher_key = Fernet.generate_key()
cipher_key = b'wwlAyqM9VCBQl-MdtBtbVeB0M9XsrL2nS7-EuR1D6YQ='
cipher = Fernet(cipher_key)

client = paho.Client()
client.on_subscribe = on_subscribe
client.on_message = on_message
client.connect(broker, 1883)
client.subscribe("Ayush/bulb1", qos=1)

client.loop_forever()
