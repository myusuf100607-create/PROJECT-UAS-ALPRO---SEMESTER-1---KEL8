## JUDUL PROJECT : MANAGEMENT IGD RUMAH SAKIT
**KELOMPOK 8 :**

Muhamad Yusuf
Muhamad Rivaldi Aropiq
Muhammad Ikbar Rifa
Elza Olgi Aulia


**STUDI KASUS**

Sistem antrian IGD ini digunakan untuk mengatur urutan pelayanan pasien berdasarkan tingkat kegawatdaruratan (Triage), bukan sekadar waktu kedatangan.

Dalam sistem ini, petugas menginput data pasien berupa nama, NIK, penanggung jawab, serta kategori pasien (BPJS atau Umum). Sistem secara otomatis mendeteksi kata kunci pada keluhan pasien untuk menentukan status prioritas: pasien Kritis akan langsung mendapatkan status "DITANGANI" dan menempati urutan teratas, sedangkan pasien Tidak Gawat akan masuk ke status "Menunggu".

Sistem ini menyimpan data pasien ke dalam daftar antrian digital yang dapat dicari berdasarkan Nama, NIK, atau nomor BPJS secara cepat. Selain menampilkan daftar pasien secara teratur dan terurut, sistem juga memungkinkan petugas untuk memperbarui keterangan penanganan atau menghapus data pasien yang layanannya telah selesai.



## Deskripsi
Pelayanan di Instalasi Gawat Darurat (IGD) menuntut penanganan pasien yang cepat, tepat, dan terorganisir dengan baik. Dalam kondisi darurat, banyaknya pasien yang datang secara bersamaan sering menyebabkan antrian tidak teratur, keterlambatan penanganan, serta risiko kesalahan dalam menentukan prioritas pasien. Jika proses pencatatan dan pengelolaan data pasien masih dilakukan secara manual, petugas IGD dapat mengalami kesulitan dalam memantau kondisi pasien, mencari data pasien tertentu, maupun memperbarui status penanganan pasien.

Selain itu, penentuan tingkat kegawatan pasien sering bergantung pada penilaian awal petugas, yang berpotensi tidak konsisten apabila tidak didukung oleh sistem yang terstruktur. Hal ini dapat menyebabkan pasien dengan kondisi kritis tidak segera mendapatkan penanganan yang seharusnya. Oleh karena itu, dibutuhkan sebuah sistem sederhana yang mampu membantu proses registrasi pasien, penentuan prioritas triage, pengelolaan antrian, serta pembaruan data pasien secara cepat dan teratur. Sistem ini diharapkan dapat meminimalkan kesalahan, meningkatkan efisiensi pelayanan IGD, dan membantu petugas dalam mengambil keputusan awal secara lebih sistematis.

Fitur Utama (Fungsionalitas CRUD):

1. Create (Registrasi Pasien): Mencatat data lengkap: NIK, Nama, Penanggung Jawab, dan Keluhan.
2. Conditional Input: Sistem hanya meminta "No. Kartu BPJS" jika kategori yang dipilih adalah BPJS. Pasien Umum akan otomatis mengisi kolom tersebut dengan tanda hubung (-).

3. Auto-Status: Pasien kritis langsung berstatus "DITANGANI", sedangkan pasien normal berstatus "Menunggu".

4. Read & Sort (Monitoring Real-time):Menampilkan data dalam bentuk tabel yang rapi.Mengurutkan pasien berdasarkan urgensi medis agar tim medis tahu siapa yang harus diproses terlebih dahulu.

5. Search (Pencarian Multi-data):Fitur pencarian cerdas yang memungkinkan petugas menemukan data pasien hanya dengan mengetikkan Nama, NIK, atau Nomor BPJS mereka.

6. Update (Evaluasi Kondisi): Memungkinkan perubahan status (misal: dari "Menunggu" menjadi "Observasi").

7. Re-Triage: Jika keluhan pasien diperbarui, sistem akan menghitung ulang tingkat urgensi dan mengatur ulang posisi antrian jika diperlukan.

8. Delete (Manajemen Selesai): Menghapus data pasien dari daftar aktif jika pasien sudah dinyatakan sembuh, dirujuk ke ruang rawat inap, atau keluar dari rumah sakit.