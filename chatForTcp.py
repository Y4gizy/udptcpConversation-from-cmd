import socket
import threading
import time

# Sunucu IP adresi ve Port numarası
SERVER_IP = '0.0.0.0'  # Tüm arayüzlerden gelen bağlantıları dinler
SERVER_PORT = 12345    # Dinlenecek port numarası

# UDP soketi oluşturma
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Soketi IP ve port'a bağla
try:
    sock.bind((SERVER_IP, SERVER_PORT))
    print(f"UDP Sunucusu {SERVER_IP}:{SERVER_PORT} adresinde dinlemeye başladı...")
except socket.error as e:
    print(f"Soket bağlanırken hata oluştu: {e}")
    exit()

# Son bağlantı yapan istemcinin adresini saklama
last_client_addr = None

# Alıcı işlevi - gelen mesajları dinler
def receive_messages():
    global last_client_addr
    while True:
        try:
            data, addr = sock.recvfrom(1024)
            message = data.decode('utf-8')
            last_client_addr = addr  # son istemci adresini güncelle
            print(f"[{addr[0]}:{addr[1]}] adresinden gelen mesaj: {message}")

            # Otomatik yanıt
            response_message = f"yabisy ({message})"
            sock.sendto(response_message.encode('utf-8'), addr)
            print(f"[{addr[0]}:{addr[1]}] adresine yanıt gönderildi.")
        except Exception as e:
            print(f"Hata oluştu (receive): {e}")
            break

# Gönderici işlevi - konsoldan yazılan mesajları gönderir
def send_messages():
    global last_client_addr
    while True:
        try:
            if last_client_addr:
                msg = input("İstemciye gönderilecek mesaj: ")
                sock.sendto(msg.encode('utf-8'), last_client_addr)
                print(f"Mesaj gönderildi → {last_client_addr[0]}:{last_client_addr[1]}")
            else:
                print("Henüz bir istemciden mesaj alınmadı, bekleniyor...")
                time.sleep(2)  # spam oluşumunu engellemek için
        except Exception as e:
            print(f"Hata oluştu (send): {e}")
            break

# Alıcı ve gönderici iş parçacıkları başlatma
receive_thread = threading.Thread(target=receive_messages, daemon=True)
send_thread = threading.Thread(target=send_messages)

receive_thread.start()
send_thread.start()

# Ana thread, gönderici bitene kadar bekler
send_thread.join()
sock.close()
print("Sunucu kapatıldı.")
