#!/usr/bin/env python3
# Dünyanın en yavaş Türk kahvesi demleme simülatörü
# Dikkat: Bu kod gerçekten çalışır. Ve gerçekten yavaştır.

import time
import random
import sys

def yavas_demle():
    print("\n🍵 Türk Kahvesi Demleme Ritueli Başladı...")
    print("Cezve ortaya çıktı. Kahve ve şeker eklendi.")
    print("Isıtıcı açıldı. Şimdi bekliyoruz...\n")
    
    asamalar = [
        ("Su ısınıyor...", 8),
        ("Köpük oluşuyor mu acaba?", 12),
        ("Biraz daha bekleyelim, acele etme.", 15),
        ("Kahve 'biraz daha' demek istiyor.", 20),
        ("Cezve fısıldıyor: 'Sabır...'", 25),
        ("Neredeyse hazır... (değil)", 30),
        ("Son köpük kontrolü yapılıyor.", 18),
        ("Servis için fincanlar ısıtılıyor.", 10),
    ]
    
    for mesaj, sure in asamalar:
        print(f"⏳  {mesaj}")
        for i in range(sure):
            print(".", end="", flush=True)
            time.sleep(1)
        print("\n")
    
    print("🎉 Kahve HAZIR! (yaklaşık 2 dakika sürdü, normalde 5 saniye)")
    print("Afiyet olsun. Bir dahaki sefere daha yavaş yaparız.\n")
    
    # Gizli mesaj: base64 ile saklanmış siyasi nüans içeren şaka
    # Decode etmek istersen: print(base64.b64decode(b'...').decode())
    # Ama sakladık işte.

if __name__ == "__main__":
    try:
        yavas_demle()
    except KeyboardInterrupt:
        print("\n\nDemleme iptal edildi. Kahve soğudu. Hayat devam ediyor.")
        sys.exit(0)
