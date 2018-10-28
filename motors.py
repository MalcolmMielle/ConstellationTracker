import serial

class Motor:
    def __init__(self):
        self.ser = serial.Serial('/dev/ttyUSB0', 9600)
    
    def write_data(self, azimut, altitude):
        
        #print(azimut)
        
       
        print ("writing")
        values = "az:" + str(azimut[0]) + ":alt:" + str(altitude[0]) 
        values_bytes = str(values).encode()
        print(values_bytes)
        self.ser.write(values_bytes)
        
        
        
        
        #self.ser.flushInput()
        #self.ser.flushOutput()
        
        #val = self.ser.readline()
        #print("AZIMUT WRITTEN ", val)
        
        
        self.ser.flushInput()
        self.ser.flushOutput()
        print("read")
        
        val = self.ser.readline()
        print(val)
        while val != b's\n':
            val = self.ser.readline()
            print(val)
        
        
        #print(azimut)
        values = "az:" + str(azimut[1]) + ":alt:" + str(altitude[1]) 
        values_bytes = str(values).encode()
        print(values_bytes)
        self.ser.write(values_bytes)
        
        
