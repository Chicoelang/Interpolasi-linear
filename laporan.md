# Ringkasan Penerapan Metode Numerik: Interpolasi Lagrange

**Nama**: [Tulis Nama Anda Di Sini]
**NIM**: [Tulis NIM Anda Di Sini]
**Topik**: Interpolasi

---

## 1. Deskripsi Masalah dan Tujuan

Dalam pengolahan data saintifik dan rekayasa, kita seringkali hanya memiliki data sampel (diskrit) yang diambil pada interval tertentu. Namun, seringkali muncul kebutuhan untuk mengetahui nilai di antara titik-titik data tersebut yang tidak terukur secara langsung.

**Studi Kasus Sederhana**:
Bayangkan seorang peneliti mencatat pertumbuhan jumlah bakteri setiap 2 jam.
- Jam 0: 1.500 bakteri
- Jam 2: 3.200 bakteri
- Jam 4: 5.800 bakteri
- Jam 6: 8.900 bakteri

Masalah muncul ketika peneliti ingin mengetahui perkiraan jumlah bakteri pada **Jam ke-3**. Karena tidak ada pengukuran pada jam tersebut, kita perlu menggunakan metode estimasi.

**Tujuan**: Menggunakan metode numerik **Interpolasi Polinomial Lagrange** untuk mengestimasi nilai fungsi pada titik yang tidak diketahui, berdasarkan sekumpulan titik data yang diketahui valid.

---

## 2. Uraian Konsep dan Metode

Metode yang digunakan adalah **Interpolasi Lagrange**. Berbeda dengan regresi yang mencari garis best-fit yang mungkin tidak melewati titik data, interpolasi menjamin kurva hasil fungsi **melewati semua titik data sampel**.

### Konsep Dasar
Diberikan $n+1$ pasangan titik $(x_0, y_0), (x_1, y_1), ..., (x_n, y_n)$, kita mencari sebuah polinomial $P_n(x)$ berderajat maksimal $n$ yang memenuhi:
$$P_n(x_i) = y_i$$
untuk setiap $i = 0, 1, ..., n$.

### Algoritma Lagrange
Polinomial Lagrange dirumuskan sebagai jumlah dari perkalian nilai $y$ dengan fungsi basis $L$:

$$P(x) = \sum_{i=0}^{n} y_i L_i(x)$$

Dimana $L_i(x)$ adalah fungsi basis Lagrange yang didefinisikan sebagai:

$$L_i(x) = \prod_{j=0, j \neq i}^{n} \frac{x - x_j}{x_i - x_j}$$

Ide utamanya adalah fungsi $L_i(x)$ akan bernilai 1 jika $x = x_i$ dan bernilai 0 jika $x$ adalah titik data lainnya. Ini memastikan kurva "mengunci" setiap titik data yang diketahui.

---

## 3. Implementasi Kode Program

Program dibuat menggunakan bahasa **Python**. Implementasi dilakukan secara manual ("from scratch") untuk fungsi Lagrange guna mendemonstrasikan pemahaman algoritma, tanpa bergantung pada fungsi `scipy.interpolate` secara instan.

**Struktur Kode Utama**:
1.  **Fungsi `lagrange_interpolation`**: Menerima input array x, array y, dan nilai x target. Fungsi ini melakukan looping untuk menghitung nilai basis $L_i$ dan menjumlahkannya sesuai rumus di atas.
2.  **Visualisasi**: Menggunakan library `matplotlib` untuk memplot titik data asli (merah) dan kurva hasil interpolasi (garis biru).

*(Cuplikan Kode Inti)*:
```python
    # Loop untuk setiap suku polinomial Lagrange (L_i)
    for i in range(n):
        # Hitung L_i(x)
        L_i = 1
        for j in range(n):
            if i != j:
                L_i = L_i * (x_target - x_points[j]) / (x_points[i] - x_points[j])
        
        # Tambahkan ke total: y_i * L_i(x)
        y_target += y_points[i] * L_i
```

---

## 4. Hasil Demonstrasi Program

Program dijalankan dengan data sampel yang disebutkan sebelumnya.

**Data Input**:
- $x = [0, 2, 4, 6]$
- $y = [1.5, 3.2, 5.8, 8.9]$

**Titik Uji**: $x = 3$ (Jam ke-3)

**Hasil Output Terminal**:
```text
=== Program Interpolasi Lagrange ===
Data Diketahui (x): [0 2 4 6]
Data Diketahui (y): [1.5 3.2 5.8 8.9]
Estimasi nilai y pada x = 3.0 adalah: 4.4375
```

**Hasil Visualisasi Gambar**:
Program menghasilkan file `grafik_interpolasi.png`. Dari grafik terlihat bahwa kurva biru mulus menghubungkan semua titik merah. Titik hijau bintang menunjukkan hasil prediksi pada jam ke-3 yang terletak tepat pada jalur kurva tersebut. Nilai 4.4375 adalah estimasi logis yang berada di antara nilai jam 2 (3.2) dan jam 4 (5.8).

_(Disini Anda bisa menyisipkan gambar grafik_interpolasi.png pada dokumen final)_

---

## 5. Referensi

1.  Python Documentation, "NumPy Reference", [numpy.org](https://numpy.org/).
2.  Matplotlib Documentation, "Pyplot tutorial", [matplotlib.org](https://matplotlib.org/).
3.  Chapra, S. C., & Canale, R. P. (2010). *Numerical Methods for Engineers*. McGraw-Hill Education. (Bab tentang Interpolasi).
