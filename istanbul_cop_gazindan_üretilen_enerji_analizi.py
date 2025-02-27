import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Veriyi yükleme
df = pd.read_excel('istanbul-cop-gazndan-uretilen-enerji-miktarlar.xlsx')
df['tarih'] = pd.to_datetime(df['tarih'])
df.set_index('tarih', inplace=True)#! zamana göre sıralama yapabilmek için zaman indekslemesi yaptım

# bütün oluşturacağım grafikleri fonksiyonlar içerisinde yazdım
def yıllara_göre_toplam_üretim():
    yıllık_uretim = df.resample('YE')['toplam_mwh'].sum().sort_values(ascending=False) #? yıllık üretimin toplamını aldım ve büyükten küçüğe sıraladım
    fig, ax = plt.subplots(figsize=(12, 8))
    yıllık_uretim.plot(kind='bar', color='skyblue', ax=ax)
    ax.set_title('Yıllara Göre Toplam Üretim Miktarı')
    ax.set_xlabel('Yıl')
    ax.set_ylabel('Toplam Üretim Miktarı (MWh)')
    ax.set_xticklabels([item.year for item in yıllık_uretim.index], rotation=45)  # Yalnızca yılları göstermek için bu kod satırı gerekli
    ax.grid(axis='y')
    return fig

def son_3_yıl():
    df_son_3_yil = df[df.index.year.isin([2022, 2023, 2024])]#? sadece son 3 yılı ele almak için isin fonksiyonunu kullandım
    tesis_uretim = df_son_3_yil.groupby('tesis_adi')['toplam_mwh'].sum().sort_values(ascending=False)#? tesis adlarını grupladım ve toplam üretimi toplayıp büyükten küçüğe sıraladım
    fig, ax = plt.subplots(figsize=(12, 8))
    tesis_uretim.plot(kind='bar', color='skyblue', ax=ax)
    ax.set_title('Son 3 Yılın Tesislere Göre Üretim Miktarı')
    ax.set_xlabel('Tesis Adı')
    ax.set_ylabel('Toplam Üretim Miktarı (MWh)')
    ax.set_xticklabels(tesis_uretim.index, rotation=14)
    ax.grid(axis='y')
    return fig

def tüm_tesisler():
    yıllık_tesis_üretim = df.groupby([df.index.year, 'tesis_adi'])['toplam_mwh'].sum().unstack()
    fig, ax = plt.subplots(figsize=(12, 8))
    for tesis in yıllık_tesis_üretim.columns:
        ax.plot(yıllık_tesis_üretim.index, yıllık_tesis_üretim[tesis], marker='o', label=tesis)
    ax.set_title('Yıllara Göre Tesislerde Elektrik Üretim Miktarı')
    ax.set_xlabel('Yıl')
    ax.set_ylabel('Toplam Üretim Miktarı (MWh)')
    ax.legend(title='Tesis Adı', bbox_to_anchor=(1.5, 1), loc='upper left')
    ax.grid(True)
    return fig
def yıllı_üretim_pasta():
    tesis_uretim = df.groupby('tesis_adi')['toplam_mwh'].sum()
    fig, ax= plt.subplots(figsize=(12,8))
    tesis_uretim.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
    ax.set_title('Tesislere Göre Elektrik Üretim Oranları')
    ax.set_ylabel('')
    ax.axis('equal')
    return fig
# Tkinter arayüzü
def grafik_secimi():
    secim = secim_combobox.get()
    for widget in grafik_frame.winfo_children():
        widget.destroy()
    if secim == 'Yıllara Göre Toplam Üretim':
        fig = yıllara_göre_toplam_üretim()
    elif secim == 'Son 3 Yılın Tesislere Göre Üretim Miktarı':
        fig = son_3_yıl()
    elif secim == 'Yıllara Göre Tesislerde Elektrik Üretim Miktarı':
        fig = tüm_tesisler()
    elif secim== 'Tesislere Göre Elektrik Üretim Oranları':
        fig =yıllı_üretim_pasta()
    canvas = FigureCanvasTkAgg(fig, master=grafik_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

# Tkinter arayüzü oluşturma
root = tk.Tk()
root.title("Grafik Seçimi")

main_frame = tk.Frame(root)
main_frame.pack(fill='both', expand=True)

button_frame = tk.Frame(main_frame)
button_frame.pack(side='left', fill='y')

grafik_frame = tk.Frame(main_frame)
grafik_frame.pack(side='right', fill='both', expand=True)

secim_label = ttk.Label(button_frame, text="Grafik Seçin:")
secim_label.pack(pady=20)

secim_combobox = ttk.Combobox(button_frame, values=[
        'Yıllara Göre Toplam Üretim',
        'Tesislere Göre Elektrik Üretim Oranları',
        'Yıllara Göre Tesislerde Elektrik Üretim Miktarı',
        'Son 3 Yılın Tesislere Göre Üretim Miktarı'
    ])
secim_combobox.pack(pady=10)

goster_button = ttk.Button(button_frame, text="Grafiği Göster", command=grafik_secimi)
goster_button.pack(pady=20)

root.mainloop()
