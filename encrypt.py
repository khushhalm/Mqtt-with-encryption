import serial
import time
import paho.mqtt.client as paho
from cryptography.fernet import Fernet

broker="broker.mqttdashboard.com"

try:
	ser = serial.Serial('/dev/ttyACM0', 9600)
except:
	pass

#no of times you want to run the loop
t = 5

client= paho.Client("client-001")

#cipher_key = Fernet.generate_key()
cipher_key = b'wwlAyqM9VCBQl-MdtBtbVeB0M9XsrL2nS7-EuR1D6YQ='
#print (cipher_key)
cipher = Fernet(cipher_key)

print("connecting to broker ",broker)
#connect
client.connect(broker)
time.sleep(2)

while t:
	try:
		print (ser.readline())
		msg = ser.readline()
	except:
		print ("No data on serial. So msg = Random")
		msg = "Random".encode()

	message = msg
	encrypted_message = cipher.encrypt(message)
	# turn it into a string to send
	out_message = encrypted_message.decode()
	print("publishing encrypted message:", out_message)
	#publish
	client.publish("Ayush/bulb1",out_message)
	time.sleep(10)
	t = t-1

client.disconnect() #disconnect
