import socket

# Sunucu IP adresi ve Port numarası
# Sunucu bilgisayarınızın yerel IP adresini buraya yazın
# Eğer aynı bilgisayarda test ediyorsanız '127.0.0.1' kullanabilirsiniz.
SERVER_IP = '0.0.0.0' # Tüm arayüzlerden gelen bağlantıları dinlemek için '0.0.0.0' kullanın
SERVER_PORT = 12345   # Seçtiğiniz port numarası

# UDP soketi oluşturma
# AF_INET: IPv4 adres ailesini kullanacağımızı belirtir.
# SOCK_DGRAM: UDP protokolünü kullanacağımızı belirtir.
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Soketi belirli bir IP adresi ve port numarasına bağlama
try:
    sock.bind((SERVER_IP, SERVER_PORT))
    print(f"UDP Sunucusu {SERVER_IP}:{SERVER_PORT} adresinde dinlemeye başladı...")
except socket.error as e:
    print(f"Soket bağlanırken hata oluştu: {e}")
    exit()

# Gelen mesajları dinleme döngüsü
while True:
    try:
        # Gelen veriyi bekle.
        # buffer_size: Alınabilecek maksimum bayt sayısı (örneğin 1024)
        # data: Gelen mesaj
        # addr: Mesajı gönderen istemcinin IP adresi ve port numarası
        data, addr = sock.recvfrom(1024) # 1024 baytlık tampon boyutu

        # Gelen mesajı decode ederek ekrana yazdır
        message = data.decode('utf-8')
        print(f"[{addr[0]}:{addr[1]}] adresinden mesaj alındı: {message}")

        # İstemciye yanıt gönderme
        response_message = f"Sunucu: Mesajınız alındı! ({message})"
        sock.sendto(response_message.encode('utf-8'), addr)
        print(f"[{addr[0]}:{addr[1]}] adresine yanıt gönderildi.")

    except KeyboardInterrupt:
        print("\nSunucu kapatılıyor...")
        break
    except socket.error as e:
        print(f"Soket hatası: {e}")
        break
    except Exception as e:
        print(f"Beklenmedik bir hata oluştu: {e}")
        break

# Soketi kapatma
sock.close()
print("Sunucu kapatıldı.")