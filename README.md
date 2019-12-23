# colortograyscaleimg
Merupakan program yang berfungsi mengubah gambar berwarna menjadi grayscale yang merupakan implementasi kecil dari proses segmentasi citra watershed

### About
- Tujuan
Menghasilkan transformasi gambar dari gambar berwarna menjadi gambar grayscale dengan memperhatikan detail gambar seperti ketajaman, kontras, bayangan, dan struktur gambar. Proses transformasi menggunakan perhitungan piksel yang dipublikasikan oleh C. Saravanan dalam paper nya (https://www.researchgate.net/publication/224130500). Berbeda dengan metode averaging, perhitungan ini menghasilkan gambar yang mempertahankan detail gambar. Proses ini merupakan awal dari segmentasi citra (watershed) dan metode ini digunakan untuk hasil yang maksimal. 

- Cara Kerja<br>
1. Program ini akan membaca input gambar dari user
2. Kemudian akan dilanjutkan dengan generate matriks kosong berukuran sama dengan piksel kolom dan baris gambar
3. Program akan mengisi matriks kosong dengan perhitungan metode di atas untuk setiap piksel
4. Program akan memplot matriks ke dalam figur dengan colormaps grey
5. Program akan save ke dalam format file png
6. Program akan memperlihatkan hasil transformasi

### Requirement
- Python 3.5+
- Gambar awal yang ingin ditransformasi
- Library Python : numpy dan matplotlib

### How to use
- Mengumpulkan Dataset Posts
1. Unduh/clone repository ini.
2. Install python dan library yang diperlukan. Untuk library dapat diinstall melalui cmd: ```pip install <nama library>```
3. Siapkan gambar yang ingin ditransformasi di direktori file yang sama
4. Jalankan script 
5. Isi input nama gambar dengan nama file contoh: butterfly.jpg
6. Hasil disave dengan nama resultconv.png di direktori yang sama

