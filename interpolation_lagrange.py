import numpy as np
import matplotlib.pyplot as plt

def lagrange_interpolation(x_points, y_points, x_target):
    """
    Menghitung nilai interpolasi di titik x_target menggunakan metode Lagrange.
    
    Args:
        x_points: Array dari titik data x yang diketahui
        y_points: Array dari titik data y yang diketahui
        x_target: Titik x yang ingin dicari nilai y-nya
        
    Returns:
        y_estimated: Nilai y hasil estimasi interpolasi
    """
    n = len(x_points)
    y_target = 0
    
    # Loop untuk setiap suku polinomial Lagrange (L_i)
    for i in range(n):
        # Hitung L_i(x)
        L_i = 1
        for j in range(n):
            if i != j:
                L_i = L_i * (x_target - x_points[j]) / (x_points[i] - x_points[j])
        
        # Tambahkan ke total: y_i * L_i(x)
        y_target += y_points[i] * L_i
        
    return y_target

def main():
    print("=== Program Interpolasi Lagrange ===")
    
    # Dataset Contoh: Pertumbuhan Bakteri (Misal)
    # Jam ke- (x) dan Jumlah Bakteri (y) dalam ribuan
    # Kita punya data jam 0, 2, 4, 6. Kita ingin taksir jam 3.
    x_known = np.array([0, 2, 4, 6])
    y_known = np.array([1.5, 3.2, 5.8, 8.9])
    
    # Titik yang ingin diprediksi (interpolasi)
    x_test = 3.0
    y_pred = lagrange_interpolation(x_known, y_known, x_test)
    
    print(f"Data Diketahui (x): {x_known}")
    print(f"Data Diketahui (y): {y_known}")
    print(f"Estimasi nilai y pada x = {x_test} adalah: {y_pred:.4f}")
    
    # Visualisasi
    # Buat titik x yang rapat untuk menggambar kurva halus
    x_curve = np.linspace(min(x_known), max(x_known), 100)
    y_curve = [lagrange_interpolation(x_known, y_known, xi) for xi in x_curve]
    
    plt.figure(figsize=(10, 6))
    
    # Plot kurva interpolasi
    plt.plot(x_curve, y_curve, label='Kurva Interpolasi Lagrange', color='blue')
    
    # Plot titik data asli
    plt.scatter(x_known, y_known, color='red', s=100, label='Data Diketahui', zorder=5)
    
    # Plot titik prediksi
    plt.scatter([x_test], [y_pred], color='green', s=150, marker='*', label=f'Prediksi (x={x_test})', zorder=10)
    
    plt.title('Penerapan Interpolasi Lagrange')
    plt.xlabel('x (Waktu/Input)')
    plt.ylabel('y (Nilai/Output)')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    
    # Simpan plot ke file
    output_filename = "grafik_interpolasi.png"
    plt.savefig(output_filename)
    print(f"\nGrafik berhasil disimpan sebagai '{output_filename}'")
    
    # Tampilkan plot (optional jika dijalankan di environment yang support GUI)
    # plt.show() 

if __name__ == "__main__":
    main()
