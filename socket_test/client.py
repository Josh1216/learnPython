import socket

ip = "127.0.0.1"
port = 50

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
x =(ip,port)

s.connect( x )

while True:
    data = input("請輸入想說的話或想結束對話請輸入END: ")
    s.send(data.encode())
    if data == "END":
        print("一切都結束了,下次再會")
        break
    getData = s.recv(1024)
    endData = getData.decode()
    print(endData)
    if endData == "END":
        break
s.close()