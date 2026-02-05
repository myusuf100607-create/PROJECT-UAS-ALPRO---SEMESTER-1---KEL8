antrian_igd = [
    {
    "nama": "Budi",
    "nik": "222222",
    "kategori": "BPJS",
    "no_bpjs": "9237856",
    "pj": "Badi (083273832)",
    "keluhan": "Sesak",
    "deskripsi": "Desk Budi",
    "skor": 1,
    "keterangan": "DITANGANI"
    },

    {
    "nama": "Samsul",
    "nik": "222222",
    "kategori": "BPJS",
    "no_bpjs": "9237856",
    "pj": "Badi (083273832)",
    "keluhan": "Demam",
    "deskripsi": "Desk Samsul",
    "skor": 2,
    "keterangan": "Menunggu"
    },
    {
    "nama": "mukhlis",
    "nik": "222222",
    "kategori": "BPJS",
    "no_bpjs": "9237856",
    "pj": "Badi (083273832)",
    "keluhan": "pilek",
    "deskripsi": "Desk Mukhlis",
    "skor": 2,
    "keterangan": "Menunggu"
    }]

def info():
    print("\n" + "="*100)
    print(f"{'>>> SISTEM MANAGEMENT IGD <<<':^100}")
    print("="*100)
    print("1. Registrasi Pasien")
    print("2. Lihat Daftar Pasien")
    print("3. Cari Pasien")
    print("4. Update Data")
    print("5. Pasien Selesai")
    print("6. Keluar")
    print("="*100)

def tampilkan_tabel(data_list):
    header = f"{'NO':<3} | {'STATUS':<13} | {'NAMA':<12} | {'NIK':<16} | {'NO. BPJS':<13} | {'PENANGGUNG JAWAB':<20} | {'DESKRIPSI PASIEN':<20} | {'KELUHAN':<20} | {'KETERANGAN'}"
    print("\n" + "-" * 155)
    print(header)
    print("-" * 155)

    if not data_list:
        print(f"{'ANTRIAN KOSONG':^155}")
    else:
        for i, p in enumerate(data_list, 1):
            status = "🔴 KRITIS" if p['skor'] == 1 else "🟢 NORMAL"
            # Menampilkan data ke kolom masing-masing
            print(f"{i:<3} | {status:<11} | {p['nama']:<12} | {p['nik']:<16} | {p['no_bpjs']:<13} | {p['pj']:<20} | {p['deskripsi']:<20} | {p['keluhan']:<20} | {p['keterangan']}")
    print("-" * 155)

# --- PROGRAM UTAMA ---
while True:
    info()
    pilihan = input("Pilih Menu [1-6]: ")

    if pilihan == '1':
        print("\n" + "-"*30)
        print("[ REGISTRASI PASIEN IGD ]")
        print("-"*30)
        try:
            nama = input("Nama Pasien            : ")
            nik  = input("NIK                    : ")
            umur = input("Umur                   : ")
            gender = input("Gender(L/P)            : ")

            print("Kategori Pasien        : 1. BPJS | 2. Umum")
            kat_pilih = input("Pilih (1/2)            : ")
            if kat_pilih == '1':
                kategori = "BPJS"
                no_bpjs = input("No. Kartu BPJS         : ")
            else:
                kategori = "Umum"
                no_bpjs = "-"

            pj_nama = input("Nama Penanggung Jawab  : ")
            deskripsi = input("Deskripsi Pasien      : ")
            kontak = input("No. HP PJ              : ")
            keluhan = input("Keluhan/Kondisi        : ")
        except:
                print("[GAGAL] Input tidak valid.")

        # Logika Otomatis Triage
        kata_kunci = ["stroke", "jantung", "sesak", "pendarahan", "kecelakaan", "tidak sadar", "kejang", "ginjal", "kanker"]
        is_kritis = any(k in keluhan.lower() for k in kata_kunci)

        skor = 1 if is_kritis else 2
        ket_awal = "DITANGANI" if is_kritis else "Menunggu"

        antrian_igd.append({
            "nama": nama,
            "nik": nik,
            "umur": umur,
            "gender": gender,
            "kategori": kategori,
            "no_bpjs": no_bpjs,
            "pj": f"{pj_nama} ({kontak})",
            "deskripsi": deskripsi,
            "keluhan": keluhan,
            "skor": skor,
            "keterangan": ket_awal
        })

        antrian_igd.sort(key=lambda x: x['skor'])
        print(f"\n[SUKSES] Pasien {nama} berhasil didaftarkan.")

    elif pilihan == '2':
        print(f"{'<<<  DAFTAR ANTRIAN & TINDAKAN IGD  >>>':^155}")
        tampilkan_tabel(antrian_igd)

    elif pilihan == '3':
        cari = input("\nCari Nama/NIK/No.BPJS: ").lower()
        hasil = [p for p in antrian_igd if cari in p['nama'].lower() or cari in p['nik'] or cari in p['no_bpjs']]
        tampilkan_tabel(hasil)

    elif pilihan == '4':
        tampilkan_tabel(antrian_igd)
        if antrian_igd:
            try:
                no = int(input("Masukkan Nomor Urut Pasien: ")) - 1
                print(f"\n--- UPDATE DATA: {antrian_igd[no]['nama']} ---")
                print("1. Ubah Data Identitas (Nama/NIK/BPJS/PJ)")
                print("2. Ubah Keluhan (Re-Triage Otomatis)")
                print("3. Ubah Keterangan (Status Penanganan)")
                print("4. Ubah Deskripsi Pasien")
                aksi = input("Pilih aksi (1/2/3/4): ")

                if aksi == '1':
                    antrian_igd[no]['nama'] = input("Nama Baru: ")
                    antrian_igd[no]['nik'] = input("NIK Baru: ")
                    antrian_igd[no]['no_bpjs'] = input("No BPJS Baru (isi '-' jika Umum): ")
                    pj_baru = input("Nama PJ Baru: ")
                    kontak_baru = input("No HP PJ Baru: ")
                    antrian_igd[no]['pj'] = f"{pj_baru} ({kontak_baru})"
                    print("[SUKSES] Identitas diperbarui.")

                elif aksi == '2':
                    antrian_igd[no]['keluhan'] = input("Keluhan Baru: ")
                    kata_kunci = ["stroke", "jantung", "sesak", "pendarahan", "kecelakaan", "tidak sadar", "kejang", "ginjal", "kanker"]
                    antrian_igd[no]['skor'] = 1 if any(k in antrian_igd[no]['keluhan'].lower() for k in kata_kunci) else 2
                    antrian_igd.sort(key=lambda x: x['skor'])
                    print("[SUKSES] Keluhan & Prioritas diperbarui.")

                elif aksi == '3':
                    antrian_igd[no]['keterangan'] = input("Keterangan Baru: ")
                    print("[SUKSES] Keterangan diperbarui.")

                elif aksi == '4':
                    antrian_igd[no]['deskripsi'] = input("Deskripsi Baru: ")
                    print("[SUKSES] Deskripsi Pasien diperbarui.")
            except:
                print("[GAGAL] Nomor urut atau input tidak valid.")

    elif pilihan == '5':
        tampilkan_tabel(antrian_igd)
        if antrian_igd:
            try:
                no = int(input("Nomor urut pasien selesai: ")) - 1
                p = antrian_igd.pop(no)
                print(f"[SUKSES] Pasien {p['nama']} selesai ditangani.")
            except:
                print("[GAGAL] Nomor tidak ditemukan.")

    elif pilihan == '6':
        print("\nSistem IGD ditutup. Terima kasih.")
        break