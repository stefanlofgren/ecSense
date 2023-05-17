import serial
import time

ser = serial.Serial('/dev/ttyS0', 9600)

# Send the command to get the CO level data
while 1:
    try:
        time.sleep(1)
        
        #Ask the ecSense device for a ppb reading
        ser.write(b'\xFF\x01\x86\x00\x00\x00\x00\x00\x79')

        # Wait for the response
        resp = ser.read(9)

        #calculate the bytes / hex from the response
        co_level = ((resp[6] * 256) + resp[7])

        # Print the CO level
        print("Current CO level: {} ppb".format(co_level))
        
  
    except KeyboardInterrupt:
        ser.close() # Close the serial connection

