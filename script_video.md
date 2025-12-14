# Naskah Video Tugas Metode Numerik: Interpolasi

**Durasi perkiraan**: 3 - 4 menit

---

### [00:00 - 00:30] Pembukaan
**(Visual: Wajah Presenter / Judul Slide)**

"Halo semuanya. Perkenalkan nama saya [Nama Anda] dengan NIM [NIM Anda].
Pada kesempatan kali ini, saya akan mempresentasikan tugas mandiri Metode Numerik dengan topik **Interpolasi**."

"Studi kasus yang saya angkat adalah bagaimana cara kita memperkirakan data yang hilang di antara data pengukuran yang kita miliki, misalnya memperkirakan jumlah populasi bakteri atau suhu pada jam tertentu yang tidak sempat tercatat."

---

### [00:30 - 01:15] Konsep Metode
**(Visual: Slide Rumus Lagrange atau Gambar Kurva Sederhana)**

"Metode yang saya gunakan adalah **Interpolasi Polinomial Lagrange**.
Berbeda dengan regresi yang mencari garis tren, Interpolasi bertujuan mencari fungsi kurva yang **tepat melewati** setiap titik data yang kita punya."

"Prinsipnya sederhana: Kita membangun sebuah persamaan polinomial berdasarkan titik-titik data tersebut. Algoritma Lagrange bekerja dengan menjumlahkan fungsi basis yang bobotnya diatur sedemikian rupa sehingga kurva akan 'terkunci' pada nilai y yang sesuai saat melewati setiap titik x."

---

### [01:15 - 02:45] Demonstrasi Kode
**(Visual: Screen Recording Layar Laptop / VS Code)**

"Berikut adalah implementasi kode programnya menggunakan bahasa Python."

*(Scroll perlahan kode `interpolation_lagrange.py`)*

"Di sini saya tidak menggunakan library instan untuk fungsinya, tapi saya menulis algoritmanya secara manual.
Bisa dilihat di fungsi `lagrange_interpolation` ini, terdapat dua loop. Loop luar untuk menjumlahkan suku polinomial, dan loop dalam untuk menghitung perkalian basis $L_i$-nya sesuai rumus Lagrange."

"Sebagai contoh data, saya masukkan data fiktif pertumbuhan bakteri pada jam ke 0, 2, 4, dan 6.
Tujuannya: Kita ingin tahu estimasi jumlah bakteri pada **jam ke-3**."

*(Jalankan terminal / Run Code)*

"Saat program dijalankan... bisa dilihat outputnya muncul.
Estimasi nilai pada x=3 adalah **4.4375**."

---

### [02:45 - 03:30] Hasil & Penutup
**(Visual: Tampilkan file gambar `grafik_interpolasi.png` yang dihasilkan)**

"Program juga secara otomatis menghasilkan grafik visualisasi seperti ini.
Titik-titik **merah** adalah data pengukuran asli kita. Garis **biru** adalah kurva interpolasi Lagrange yang terbentuk.
Dan tanda **bintang hijau** ini adalah hasil prediksi kita di jam ke-3."

"Terlihat bahwa estimasinya sangat masuk akal karena berada mulus di jalur kurva pertumbuhan tersebut."

**(Visual: Wajah Presenter)**

"Kesimpulannya, metode Interpolasi Lagrange sangat efektif untuk mengisi gap data yang hilang dengan presisi tinggi asalkan pola datanya cenderung mulus (smooth)."

"Sekian presentasi dari saya. Kode sumber dan laporan lengkap dapat diakses pada link yang terlampir. Terima kasih."

---
