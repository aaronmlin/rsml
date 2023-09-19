# Aaron Mario Lin - 2206082341 # 

# Tugas 2 #

## rsml.adaptable.io ##
### 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial). ###

Tutorial tentu banyak membantu saya dalam mengerjakan tugas kali ini, tetapi saya juga mengalokasikan sedikit waktu untuk memahami bagaimana cara kerja Django framework, dan version control git pula. Saya menantang diri saya untuk membaca ulang tutorial dari awal sampai akhir, lalu mencoba untuk mengerjakan tugas ini tanpa sambil melihatnya sama sekali. Untungnya, pada percobaan pertama sudah berhasil. Suatu bantuan tambahan juga didapatkan dari internet ketika mencapai tahap dimana saya sedikit bingung

### 2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html. ###
![image](https://github.com/aaronmlin/rsml/assets/113165742/4e26fd17-7194-4a5a-ba8f-fad9ccbd70e0)

### 3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment? ###

Virtual environment digunakan dalam proyek ini untuk mengisolasi dependensi proyek, mengelola versi Python yang berbeda, dan juga mempermudah pengelolaan proyek Django. Ini memungkinkan developer untuk menghindari konflik dependensi, menjaga supaya proyek tetap terorganisir, dan melindungi sistem dari masalah potensial, menjadikannya praktik yang sangat disarankan dalam pengembangan Python. Secara teoritis, bisa saja membuat suatu proyek Django tanpa menggunakan virtual environment, tetapi tentu tidak disarankan, karena alasan-alasan di atas.

### 4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya. ###

1. MVC (Model-View-Controller):
- Model --> Bertanggung jawab untuk memproses, menyimpan, serta mengelola data aplikasi dan logika bisnisnya. Bagian ini yang berurusan dengan pemrosesan data dan interaksi dengan basis data jika diperlukan.
- View --> Berperan sebagai suatu interface/tampilan yang akan menampilkan data ke pengguna aplikasi
- Controller --> Berperan sebagai penengah dari model dan view. Controller akan menerima input dari user, memprosesnya, dan memperbarui model sesuai input. Setelah itu, model memberi tahu pengontrol yang kemudian memperbarui tampilan. Controller bertanggung jawab untuk menjaga sinkronisasi antara model dan tampilan, dan ini merupakan salah satu prinsip utama dalam arsitektur MVC yang meningkatkan pemeliharaan dan pengujian aplikasi.

2. MVT (Model-View-Template)
- Model --> Memiliki peran yang sama seperti model pada MVC
- View --> Menampilkan data pada pengguna, tetapi tidak terdapat logika bisnis
- Template --> Sebuah layer yang akan menangani seluruh bagian user interface

3. MVVM (Model-View-ViewModel)
- Model --> Memiliki peran yang sama seperti model pada MVC dan MVT
- View --> Menampilkan bagian user interface, umumnya pada MVVM menggunakan bahasa XAML
- ViewModel --> Berperan juga sebagai perantara antara model dan view, ia akan menyimpan kondisi view sekarang dan melaksanakan perintah untuk mengubah data di model untuk ditampilkan ke view

### Perbedaan ###

Perbedaan utama antara ketiganya adalah bagaimana tampilan dan logika bisnis dipisahkan dan bagaimana data dikomunikasikan antara mereka. MVC menggunakan Controller sebagai perantara antara Model dan View, MVT memisahkan tampilan dengan Template, sedangkan MVVM menggunakan ViewModel untuk menghubungkan Model dan View dengan cara yang lebih longgar dan memungkinkan tampilan untuk secara otomatis menanggapi perubahan dalam Model.



# Tugas 3 #

### 1. Apa perbedaan utama antara form POST dan form GET pada Django? ###
Form POST:
- Mengirim data ke server dalam badan permintaan HTTP
- Bentuk data dikirimkan secara tersembunyi; tidak melalui URL. Sehingga lebih aman untuk mengirimkan data sensitif
- Cocok digunakan untuk mengirim data-data besar
- Umumnya digunakan untuk mengirimkan data yang akan memiliki perubahan pada server, contohnya form input

Form GET:
- Mengirimkan data ke server melalui query string --> ditambahkan ke URL
- Bentuk data tidak tersembunyi; bebas dilihat untuk siapapun
- Terdapat batasan jumlah data, sehingga tidak cocok untuk data-data besar
- Umumnya digunakan untuk permintaan pencarian/pembacaan data dari server


### 2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
XML (eXtensible Markup Language):
- XML yaitu bahasa markup yang digunakan untuk mengirimkan bentuk data yang ter-hierarki dalam basis teks
- Memiliki dukungan yang kuat dalam struktur data kompleks
- Sering digunakan dalam pengiriman data antara aplikasi yang tidak hanya berbasis lewat web

JSON (JavaScript Object Notation):
- JSON adalah format pertukaran data yang ringan --> berbasis teks
- Memiliki _syntax_ yang mudah dipahami manusia dan mudah diurai oleh mesin
- Sering digunakan dalam pengembangan aplikasi web modern karena dapat digunakan untuk mengirimkan data antara aplikasi klien dan server
- Tidak hanya dapat digunakan dalam JavaScript

HTML (Hypertext Markup Language)
- Suatu bahasa markup yang digunakan untuk membangun struktur dan tampilan halaman web
- Tidak dirancang khusus untuk pertukaran data antar aplikasi, seperti XML dan JSON.
- Lebih fokus pada representasi visual dan struktural dari konten web

### 3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern? ###
