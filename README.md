# Deskripsi

Aplikasi olah data industri sederhana

# Endpoint

| Endpoint             | Method | Deskripsi          |
| -------------------- | ------ | ------------------ |
| `/api/get_all_data ` | GET    | Ambil data dari DB |
| `/api/post_data`     | POST   | Tambah data ke DB  |
| `/api/delete_data`   | DELETE | Hapus data pada DB |

### /api/get_all_data

Ambil semua data yang ada pada DB. Terdapat query parameter `sort` untuk sorting data.

| Nilai query `sort` | Deskripsi                          |
| ------------------ | ---------------------------------- |
| `normal`           | Urut berdasar id                   |
| `dsc`              | Urut descending berdasar timestamp |
| `asc`              | urut ascending berdasar timestamp  |

### /api/post_data

Post atau tambahkan data ke DB. Terdapat parameter body yang harus diisi.

| Parameter pada body | Deskripsi       | Tipe data |
| ------------------- | --------------- | --------- |
| `nama`              | Nama pekerja    | String    |
| `umur`              | Umur pekerja    | Integer   |
| `jabatan`           | Jabatan pekerja | String    |

### /api/delete_data

Hapus data pada DB. Terdapat parameter body yang harus diisi.

| Parameter pada body | Deskripsi                     | Tipe data |
| ------------------- | ----------------------------- | --------- |
| `id`                | ID pekerja yang ingin dihapus | Integer   |

Dapetin ID pekerja dengan GET all data dulu.

# Cara pakai

1. Install Python 3
2. Install library SQLAlchemy, MySQL Client, dan Flask

```
$ pip3 install sqlalchemy
$ pip3 install mysqlclient
$ pip3 install flask
```

3. Install XAMPP dan MySQL di lokal, buat database dengan nama `simple_industry`
4. Install POSTMAN atau aplikasi semacamnya
5. Ganti variabel username, password, host, database dan port pada file `connection.py`, sesuaikan sama yang ada di local (MySQL)
6. Jalanin APP dengan command ini, eksekusi dari root direktori.

```
$ python main.py
```

atau

```
$ python3 main.py
```

7. Base URLnya `http://localhost:5000/`, jadi misal mau GET data, jadi `http://localhost:5000/api/get_all_data`

### Catatan

Metode GET parameternya di query, kalau POST dan DELETE di body dengan format urlencoded `x-www-form-urlencoded`

Video tutorial dibawah bisa membantu

[Video 1](https://www.youtube.com/watch?v=MYe0camYjmY)
[Video 2](https://www.youtube.com/watch?v=cR_FqveTewo)
