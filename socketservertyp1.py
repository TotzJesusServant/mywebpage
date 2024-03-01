import socket

def main():
    # Membuat socket TCP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Mengikat socket ke alamat dan port yang ditentukan (misalnya port 12345)
    server_socket.bind(('localhost', 12345))
    
    # Mendengarkan permintaan masuk (maksimum 5 koneksi dalam antrian)
    server_socket.listen(5)
    
    print("Menunggu koneksi...")
    
    while True:
        # Menerima koneksi dari klien
        client_socket, client_address = server_socket.accept()
        print(f"Koneksi dari {client_address}")
        
        # Menerima data dari klien
        data = client_socket.recv(1024)
        print(f"Data diterima dari klien: {data.decode('utf-8')}")
        
        # Mengirim respons ke klien
        client_socket.sendall(b"Terima kasih!")
        
        # Menutup koneksi dengan klien
        client_socket.close()
        
        print("Menunggu koneksi baru...")

if __name__ == "__main__":
    main()
