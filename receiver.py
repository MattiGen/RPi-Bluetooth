import socket
import RPi.GPIO as GPIO        #calling for header file which helps in using GPIOs of PI
LED=18
 
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(LED,GPIO.OUT)  #initialize GPIO21 (LED) as an output Pin
GPIO.output(LED,0)

hostMAC = "B8:27:EB:12:F1:A2"
port = 1
backlog = 1
size = 1024

server_socket=socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
server_socket.bind((hostMAC,port))
server_socket.listen(backlog)
 
client_socket,address = server_socket.accept()
print ("Accepted connection from ",address)
while 1:
 
 data = client_socket.recv(1024)
 data = str(data[:-2], 'utf-8')
 print ("Received: %s" % data)
 if (data == "0"):    #if '0' is sent from the Android App, turn OFF the LED
  print ("GPIO 21 LOW, LED OFF")
  GPIO.output(LED,0)
 if (data == "1"):    #if '1' is sent from the Android App, turn OFF the LED
  print ("GPIO 21 HIGH, LED ON")
  GPIO.output(LED,1)
 if (data == "q"):
  print ("Quit")
  break
 
client_socket.close()
server_socket.close()
