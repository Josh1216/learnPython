import serial
import modbus_tk
from modbus_tk import modbus_rtu
import modbus_tk.defines as cst 

PORT = "COM1"

master = modbus_rtu.RtuMaster(serial.Serial(port=PORT,baudrate=9600,bytesize=8,parity="N",stopbits=1))
master.set_timeout(3.0)
master.set_verbose(True) #怕被干擾,是否重發
master.execute(1,cst.WRITE_MULTIPLE_REGISTERS,0x2,3,[81,74,63])
value = master.execute(1,cst.READ_HOLDING_REGISTERS,0x3,2)
print(value)
master.close()