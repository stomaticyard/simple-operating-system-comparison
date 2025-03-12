import tkinter as tk
from tkinter import messagebox

# Linux, Mac ve Windows özelliklerini döndüren fonksiyonlar
def get_linux_features():
    return [
        "Açık kaynak kodlu", "Yüksek özelleştirilebilirlik", "Çeşitli dağıtımlar mevcut",
        "Paket yöneticisi (apt, yum, zypper vb.)", "Terminal kullanımı yaygın", "Linux çekirdeği",
        "Çoğunlukla düşük sistem gereksinimleri", "Çoklu kullanıcı desteği", "Çeşitli dosya sistemleri",
        "Çoklu pencere yöneticisi seçenekleri", "Geliştiriciler için mükemmel bir ortam", 
        "Genel olarak daha az virüs ve zararlı yazılım tehdidi", "Ağ yönetimi güçlüdür",
        "Özelleştirilebilir terminal ve komut satırı arayüzü", "Kapsamlı yazılım depoları",
        "Mükemmel sunucu desteği", "Depolama alanını kolayca yönetebilme", "Çeşitli masaüstü ortamları",
        "Sürekli güncellenen yazılımlar", "Minimal kurulum seçenekleri", "Hızlı donanım tanıma",
        "Yüksek performanslı", "Sadece açık kaynak yazılımlarını kullanma", "Çoğunlukla ücretsiz ve açık kaynak yazılımlarına bağımlı",
        "Sistem kaynağını daha verimli kullanma", "Bağımsız geliştiricilerin desteği", "İleri düzey ağ güvenliği",
        "Gelişmiş script yazma ve otomasyon yetenekleri", "Çoklu işlemci desteği"
    ]

def get_mac_features():
    return [
        "Kapalı kaynak kodlu", "Daha kullanıcı dostu arayüz", "Çoğunlukla yüksek kaliteli donanım",
        "Eşsiz tasarım ve estetik", "MacOS üzerinde gelişmiş grafik desteği", "Apple ekosistemiyle entegrasyon",
        "Tartışmasız en iyi multimedya düzenleme yazılımları", "Mac App Store", "Sıkı güvenlik önlemleri",
        "Hızlı ve kolay sistem güncellemeleri", "Gelişmiş Time Machine yedekleme sistemi", "Hızlı başlangıç süresi",
        "Mükemmel pil ömrü", "MacOS üzerinde kolay yazılım güncellemeleri", "Özelleştirilebilen uygulama menüsü",
        "Çoklu dil desteği", "Genellikle sınırlı donanım seçenekleri", "Parmak izi ve yüz tanıma güvenliği",
        "Yüksek uyumluluk ve yazılım desteği", "Sistemi kolayca sıfırlama", "Farklı ekranlara kolayca geçiş yapabilme",
        "Apple Watch ile entegrasyon", "Hedefe yönelik güçlü geliştirme araçları", "Yüksek kalite ses ve video",
        "Kolayca ekran paylaşımı yapabilme", "Apple’ın sıkı uygulama onay süreci", "Mükemmel font ve tipografi desteği",
        "Yazılım ekosisteminin özgünlüğü", "Gelişmiş grafiksel arayüz", "Apple’ın donanım ve yazılım entegrasyonu"
    ]

def get_windows_features():
    return [
        "Kapalı kaynak kodlu", "Genel olarak geniş yazılım desteği", "Çok sayıda donanım desteği",
        "Yaygın olarak kullanılan işletim sistemi", "DirectX desteği ile oyunlarda en iyi performans", 
        "Geniş oyun desteği", "Windows Store", "Kapsamlı yazılım uyumluluğu", "Windows PowerShell ile güçlü komut satırı arayüzü",
        "Microsoft Office desteği", "Çoklu monitör desteği", "Kolay donanım takma ve çıkarma", 
        "Gelişmiş USB desteği", "Çok sayıda ticari yazılım desteği", "Gelişmiş multimedya desteği",
        "Parmak izi ve yüz tanıma güvenliği", "Windows Defender ile güçlü virüs koruması", "Windows Update ile düzenli güncellemeler",
        "Yüksek donanım desteği ve sürücü güncellemeleri", "Çeşitli güvenlik araçları", "Windows Sandbox özelliği",
        "Çoklu kullanıcı desteği", "Kapsamlı sistem yönetimi araçları", "Farklı ofis ve üretkenlik yazılımları desteği",
        "Kolay uzaktan bağlantı araçları", "Büyük yazılım geliştirme ekosistemi", "Veritabanı yazılımları ve işletim sistemi desteği",
        "Windows Subsystem for Linux (WSL)", "Gelişmiş ağ yönetimi", "Kolayca yedekleme yapabilme", "Verimli dosya yönetimi"
    ]

# Karşılaştırma fonksiyonu
def compare_features(features1, features2, os1, os2):
    result = f"{os1} ve {os2} karşılaştırması:\n"
    result += f"\n{os1} sahipken {os2} olmayan bazı özellikler:\n"
    for feature in features1:
        if feature not in features2:
            result += f"- {feature}\n"

    result += f"\n{os2} sahipken {os1} olmayan bazı özellikler:\n"
    for feature in features2:
        if feature not in features1:
            result += f"- {feature}\n"

    return result

# GUI'yi başlatma
def run_gui():
    def on_compare():
        os1 = os1_var.get().lower()
        os2 = os2_var.get().lower()

        if os1 == os2:
            messagebox.showerror("Hata", "Aynı işletim sistemi seçtiniz. Lütfen farklı işletim sistemleri seçin.")
            return

        if os1 == 'linux':
            features1 = get_linux_features()
        elif os1 == 'mac':
            features1 = get_mac_features()
        elif os1 == 'windows':
            features1 = get_windows_features()

        if os2 == 'linux':
            features2 = get_linux_features()
        elif os2 == 'mac':
            features2 = get_mac_features()
        elif os2 == 'windows':
            features2 = get_windows_features()

        result = compare_features(features1, features2, os1.capitalize(), os2.capitalize())
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, result)

    root = tk.Tk()
    root.title("İşletim Sistemi Karşılaştırıcı")
    root.geometry("600x500")

    # Kullanıcıdan giriş alınacak etiketler ve menüler
    tk.Label(root, text="İlk işletim sistemi seçin:").pack(pady=5)
    os1_var = tk.StringVar(value="windows")
    os1_menu = tk.OptionMenu(root, os1_var, "windows", "mac", "linux")
    os1_menu.pack(pady=5)

    tk.Label(root, text="İkinci işletim sistemi seçin:").pack(pady=5)
    os2_var = tk.StringVar(value="linux")
    os2_menu = tk.OptionMenu(root, os2_var, "windows", "mac", "linux")
    os2_menu.pack(pady=5)

    # Karşılaştırma butonu
    compare_button = tk.Button(root, text="Karşılaştır", command=on_compare)
    compare_button.pack(pady=10)

    # Sonuçları gösterecek metin alanı
    result_text = tk.Text(root, height=15, width=70)
    result_text.pack(pady=5)

    root.mainloop()

# Programı başlat
if __name__ == "__main__":
    run_gui()
