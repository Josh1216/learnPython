import serial
from modbus_tk import modbus_rtu
import modbus_tk.defines as cst
from time import sleep

PORT = "COM3"

def settingup():
    master = modbus_rtu.RtuMaster(serial.Serial(port=PORT,baudrate=38400,bytesize=8,parity="N",stopbits=1))
    master.set_timeout(5,0)
    master.set_verbose(True)
    return master
def servoOn(master):
    master.execute(3,cst.WRITE_MULTIPLE_REGISTERS,0X2042,1,[1])
    print("SERVO ON\n")
def servoOff(master):
    master.execute(3,cst.WRITE_MULTIPLE_REGISTERS,0X2042,1,[0])
    print("SERVO OFF\n")
def initial(master):
    master.execute(3,cst.WRITE_MULTIPLE_REGISTERS,0X2041,1,[0])
    sleep(0.5)
    master.execute(3,cst.WRITE_MULTIPLE_REGISTERS,0X2041,1,[1])
    print("原點歸位中",end="")
    while master.execute(3,cst.READ_HOLDING_REGISTERS,0x1021,1)[0]!=1:
        print(".",end="")
        sleep(2)
    print("\n原點歸位完成！\n")
def designatedLocation(master):
    desloc=input("請輸入位置 -- ")
    try:
        desloc=int(desloc)
        desloc*=100
        left=desloc>>16
        right=desloc&0XFFFF
        master.execute(3,cst.WRITE_MULTIPLE_REGISTERS,0X2044,1,[0]) # START 0
        master.execute(3,cst.WRITE_MULTIPLE_REGISTERS,0X9010,1,[1])
        master.execute(3,cst.WRITE_MULTIPLE_REGISTERS,0X9011,2,[left,right])
        master.execute(3,cst.WRITE_MULTIPLE_REGISTERS,0X9013,1,[100])
        master.execute(3,cst.WRITE_MULTIPLE_REGISTERS,0X9014,1,[100])
        master.execute(3,cst.WRITE_MULTIPLE_REGISTERS,0X9016,2,[0,0])
        master.execute(3,cst.WRITE_MULTIPLE_REGISTERS,0X9018,2,[0,0])
        master.execute(3,cst.WRITE_MULTIPLE_REGISTERS,0X901A,1,[300])
        master.execute(3,cst.WRITE_MULTIPLE_REGISTERS,0X901B,1,[300])
        master.execute(3,cst.WRITE_MULTIPLE_REGISTERS,0X901C,1,[0])
        master.execute(3,cst.WRITE_MULTIPLE_REGISTERS,0X901D,1,[65535])
        master.execute(3,cst.WRITE_MULTIPLE_REGISTERS,0X2045,1,[1])
        master.execute(3,cst.WRITE_MULTIPLE_REGISTERS,0X2046,1,[0])
        master.execute(3,cst.WRITE_MULTIPLE_REGISTERS,0X2047,1,[0])
        master.execute(3,cst.WRITE_MULTIPLE_REGISTERS,0X2048,1,[0])
        master.execute(3,cst.WRITE_MULTIPLE_REGISTERS,0X2049,1,[0])
        master.execute(3,cst.WRITE_MULTIPLE_REGISTERS,0X204A,1,[0])
        master.execute(3,cst.WRITE_MULTIPLE_REGISTERS,0X204B,1,[0])
        master.execute(3,cst.WRITE_MULTIPLE_REGISTERS,0X2044,1,[1])
        print()
    except:
        print("輸入無效，請再試一次。\n")
        designatedLocation(master)
def closeup(master):
    master.close()
    print("Program terminated.")

if __name__ == "__main__":
    master = settingup()
    servoOn(master)
    initial(master)
    servoOff(master)