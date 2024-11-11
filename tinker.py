import tkinter as tk  # Mengimpor modul tkinter untuk membuat GUI

# Membuat jendela utama aplikasi
window = tk.Tk()  # Membuat instance dari jendela utama aplikasi
window.title("Aplikasi Prediksi Prodi Pilihan")  # Mengatur judul jendela aplikasi
window.geometry("400x500")  # Mengatur ukuran jendela aplikasi dengan lebar 400px dan tinggi 500px

# Membuat label judul
judul_label = tk.Label(window, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 16))  # Membuat label dengan teks judul dan ukuran font 16
judul_label.pack(pady=10)  # Meletakkan label judul di jendela utama dengan padding vertikal sebesar 10px

# Membuat frame untuk menampung input nilai mata pelajaran
frame_nilai = tk.Frame(window)  # Membuat frame di dalam jendela utama untuk mengelompokkan input nilai
frame_nilai.pack(pady=20)  # Meletakkan frame dengan padding vertikal sebesar 20px dari elemen lain

# Membuat 10 input nilai mata pelajaran
nilai_entries = []  # Membuat list kosong untuk menyimpan entry nilai setiap mata pelajaran
for i in range(1, 11):  # Loop untuk membuat 10 input nilai
    label = tk.Label(frame_nilai, text=f"Nilai Mata Pelajaran {i}:")  # Membuat label untuk setiap mata pelajaran
    label.grid(row=i, column=0, padx=10, pady=5, sticky="w")  # Meletakkan label di dalam grid pada frame_nilai
    entry = tk.Entry(frame_nilai, width=10)  # Membuat entry (input box) untuk nilai mata pelajaran
    entry.grid(row=i, column=1, padx=10, pady=5)  # Meletakkan entry di dalam grid pada frame_nilai
    nilai_entries.append(entry)  # Menambahkan entry ke dalam list nilai_entries

# Fungsi untuk menampilkan hasil prediksi program studi yang direkomendasikan
def hasil_prediksi():  # Mendefinisikan fungsi yang akan dijalankan saat tombol prediksi ditekan
    # Mengambil semua nilai dari entry mata pelajaran, jika ada proses prediksi, dapat diterapkan di sini
    # Pada contoh ini, hanya menampilkan prediksi statis
    hasil_label.config(text="Prodi yang Direkomendasikan: Teknologi Informasi")  # Menampilkan hasil prediksi pada label hasil

# Membuat tombol untuk memproses hasil prediksi
prediksi_button = tk.Button(window, text="Hasil Prediksi", command=hasil_prediksi)  # Membuat tombol dengan teks "Hasil Prediksi" yang menjalankan fungsi hasil_prediksi
prediksi_button.pack(pady=20)  # Meletakkan tombol di jendela utama dengan padding vertikal sebesar 20px

# Membuat label untuk menampilkan hasil prediksi program studi
hasil_label = tk.Label(window, text="", font=("Arial", 12))  # Membuat label kosong untuk menampilkan hasil prediksi dengan ukuran font 12
hasil_label.pack(pady=10)  # Meletakkan label hasil prediksi di jendela utama dengan padding vertikal sebesar 10px

# Menjalankan aplikasi
window.mainloop()  # Memulai loop utama aplikasi agar jendela tetap tampil

#end----------------------------------------------------------------------
#-------------

