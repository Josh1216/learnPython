import socket

ip = "127.0.0.1"
port = 50
maxConnectNumber = 5

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

s.bind((ip,port))
s.listen(maxConnectNumber)

user = []

con,addr = s.accept()
print(addr)


while True:    
    data = con.recv(1024)
    print(data.decode())
    if data.decode() == "END":
        break
    else:
        inPut = input("請輸入要傳送的話: ")
        con.send(inPut.encode())
        if inPut == "END":
            break
con.close()