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
Menurut artikel dari oracle.com, JSON lebih populer digunakan dalam pengembangan aplikasi web modern karena keunggulannya dalam kecepatan pertukaran data dan hasil-hasil layanan web. JSON juga lebih mudah ditulis dan dipahami, sehingga lebih sering digunakan daripada XML.

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial). ###

- [x] Membuat input `form` untuk menambahkan objek model pada app sebelumnya
Untuk membuat suatu input form, pertama-tama saya membuat suatu file bernama `forms.py ` untuk membuat struktur form input yang akan digunakan. File tersebut akan berisi kode sebagai berikut.

```
from django.forms import ModelForm
from main.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description"]
```
`model = Product` adalah model yang digunakan untuk form. Hasil dari form akan disimpun dalam objek `Product`
`fields` menunjukkan field dari model Product yang digunakan untuk form

Pada file `views.py` saya juga menambahkan beberapa import module dari Django yang digunakan untuk setup form input. Termasuk   `HttpResponseRedirect`,  `ProductForm`, dan `reverse `
Selanjutnya membuat _function_ baru dengan nama `create_product` yang menerima parameter request. Secara singkat, _function_ ini harus membuat suatu ProductForm baru berdasarkan input user, memvalidasi isi input form, menyimpannya, dan melakukan redirect setelah data form berhasil tersimpan.

Perubahan juga terjadi pada _function_ `show_main`. Menambahkan beberapa baris kode yang bertujuan untuk mengambil seluruh object Product pada database. 

Setelah itu, untuk mengakses perubahan pada `views.py` dan `forms.py`, saya juga  menambahkan _path url_ ke `urls.py`. Untuk melihat visualisai dari form input yang telah dibuat, saya membuat file HTML baru bernama `create_product.html`, yang akan dihubungkan dengan `main.html` dengan suatu reference `<a href="{% url 'main:create_product' %}"> `

- [x] Tambahkan 5 fungsi `views` untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID.

Cara saya menerapkan poin ini adalah dengan pertama meng-import modul yang diperlukan, yaitu `HttpResponse` dan `Serializer`. Secara singkat, kelima _function_ baru tersebut menerima parameter `request`, menbambil data dari object Product, dan menggunakan modul Serializer untuk me-_return_ data sesuai dengan bentuk yang diinginkan. Saat ingin me-_request_ data dengan ID, saya menambahkan parameter id pada _function_ tersebut pula, serta mem-filter object berdasarkan id-nya. Contohnya:

```
def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```

```
def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```


 - [x] Membuat routing URL untuk masing-masing `views` yang telah ditambahkan pada poin 2.
Untuk menyelesaikan tahap ini, pertama-tama saya mengimport semua _function_ ke file `urls.py`
```
from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id
```
Path yang ditambahkan pada file tersebut berupa:

```
urlpatterns = [
    ...
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    ...
]
```

Dokumentasi Screenshot Request POSTMAN

![image](https://github.com/aaronmlin/rsml/assets/113165742/65a00c4b-ac05-4d24-bb0f-b357aa9018be)

![image](https://github.com/aaronmlin/rsml/assets/113165742/b6e8836f-9974-439e-a8ee-f32a4e03db8a)


![image](https://github.com/aaronmlin/rsml/assets/113165742/665516af-826e-4aeb-8a28-5f004e9009c2)

![image](https://github.com/aaronmlin/rsml/assets/113165742/843a032f-c5cd-474a-a02b-3d6f13223e35)

![image](https://github.com/aaronmlin/rsml/assets/113165742/2ee2226f-b4d9-40d7-91d1-0c3cc87b1496)


# Tugas 4 #

### 1. Apa itu Django `UserCreationForm`, dan jelaskan apa kelebihan dan kekurangannya? ###
Django `UserCreationForm` adalah suatu fitur dari framework Django yang digunakan untuk membuat suatu profil user yang dapat menggunakan aplikasi yang telah kita buat. 

## Keunggulan ##
- Memberikan suatu _layer_ keamanan, karena pengguna yang register harus membuat username dan password
- Lebih customizable

## Kekurangan ###
- Kurang fleksibel untuk aplikasi-aplikasi yang lebih kompleks
- Tidak bisa diintegrasikan dengan autentikasi platform-platform lain, seperti email atau sosial media.


### 2. Apa itu perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting? ###
Framework Django mempunyai fitur di mana pemilik aplikasi dapat meng-handle baik autentikasi maupun otorisasi dari para pengguna-pengguna yang memakainya. Secara singkat, autentikasi lebih berfokus untuk memverifikasi apakah seorang user adalah benar-benar user tersebut. Sementara, otorisasi merupakan istilah untuk menandakan hal apa saja yang dapat dilakukan oleh user yang telah diautentikasi. Tentu hal keduanya penting untuk aspek-aspek keamanan. Tanpa autentikasi, akan banyak akun yang akan diretas oleh pengguna lain, dan tanpa otorisasi, pengguna dapat melihat data-data pribadi yang mungkin awalnya hanya boleh dilihat oleh admin/pemilik aplikasi saja.


### 3. Apa itu _cookies_ dalam konteks aplikasi web, dan bagaimana Django menggunakan _cookies_ untuk mengelola data sesi pengguna? ###
_Cookies_ berbentuk text file kecil yang berisi data-data penting suatu pengguna, seperti username dan password. Hal ini digunakan untuk mengidentifikasi suatu pengguna/perangkat pada yang tersambung pada suatu jaringan. Pada umumnya, _cookies_ digunakan untuk memperhalus dan meningkatkan kualitas pengalaman pengguna saat sedang _web browsing_. Ambil contoh, ketika kita pertama kali register/login suatu website, kadang kala akan ada muncul suatu _pop-up_ yang menanyakan apakah kita boleh mengakses _cookies_ atau tidak. 
Cara Django menggunakan _cookies_ juga tak jauh berbeda dari aplikasi-aplikasi lain di internet:
- [x] _Request_ dikirimkan ke server dari browser
- [ ] Server men-_transmit_ response kepada browser beserta _cookies_
- [ ] _Cookie_ yang diterima disimpan oleh server, dan setiap kali ada _request_ ke server oleh browser, _cookie_ tersebut juga turut dikirimkan
- [ ] _Cookie_ akan dihapus dari browser saat _expired_


### 4. Apakah penggunaan _cookies_ aman secara _default_ dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?
Secara umum, suatu _cookie_ dari website yang ternama dapat dipercaya. Isi dari suatu _cookie_ tidak dapat digunakan untuk secara langsung mengidentifikasi suatu informasi penting, sementara lebih banyak digunakan supaya pengguna tidak perlu repot dalam menggunakan internet. _Cookies_ juga tidak bisa digunakan untuk men-_download_ suatu _malware_.


### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial). ###
- Menyalakan _virtual environment_
- Mengimpor modul-modul yang diperlukan, salah satunya adalah `UserCreationForm`
- Membuat suatu _function_ yang menerima request dari browser ke server. _Function_ ini kita namakan register
- Membuat suatu file HTML yang menjadi tampilan dari form register yang telah dibuat
- Mengimpor fungsi register ke dalam file `urls.py` , dan menambahkan _path url_ ke dalam `urlpatterns`
- Mengulangi langkah-langkah yang sama untuk membuat login form. Kali ini, modul yang di-import adalah `authenticate` dan `login`
- _Function_ yang dibuat dinamakan login_user
- Mengulangi langkah yang sama untuk membuat logout, dan modul yang di-import adalah `logout`
- Perbedaan terletak di pembuatan file HTML, kali ini logout hanya membutuhkan suatu _hyperlink tag_ di file `main.html`
- Untuk otorisasi, menggunakan modul `login_required` untuk membatasi akses hanya pada pengguna yang sudah login. Koden ditambahkan pada `views.py` sebagai berikut:
```
@login_required(login_url='/login')
def show_main(request):
```
- Selanjutnya, membuat dua akun dan memasukkan beberapa data seperti yang tertera di soal
- Untuk menghubungkan model `Item` dengan `Product`, menambahkan import User ke dalam `models.py`, dan menambahkan kode untuk menghubungkan satu Item dengan User
- Kemudian melakukan beberapa perubahan kepada `create_product` di `views.py` supaya Django mengenali bahwa objek yang sedang dibuat dimiliki oleh user tersebut.
- Perubahan juga terjadi di `show_main` untuk hanya menunjukkan produk yang dimiliki oleh user tertentu
- Lakukan migrate dan runserver

## Tugas 5 ##

### 1. Jelaskan manfaat dari setiap ___element selector___ dan kapan waktu yang tepat untuk menggunakannya.
Menurut w3schools.com,  CSS memiliki 5 jenis selector.

- Simple selector 
- Combinator selector
- Pseudo-class selector
- Pseudo-element selector
- Attribute selector

### 2. Jelaskan HTML5 Tag yang kamu ketahui ###

Berikut beberapa HTML5 tag yang saya pernah gunakan:

- `<link>` --> digunakan untuk menghubungkan file HTML dengan file eksternal
- `<img>` --> merepresentasikan sebuah image
- `<h1> - <h6>` --> ukuran heading
- `<nav>` --> merepresentasikan link-link navigasi yang dapat dituju
- `<li> dan <ul>` --> _list_ dan _unordered list_
- `<div>` --> merepresentasikan sebuah _division_ atau _section_ dalam sebuah HTML
- `<form>` --> melambangkan form input

### 3. Jelaskan perbedaan antara _margin_ dan _padding_ ###

Secara singkat, _margin_ dalam CSS melambangkan suatu tempat kosong yang berada diluar _border_ suatu elemen. Sedangkan _padding_ melambangkan jarak antara suatu _border_ dari elemen dengan isi elemen tersebut

### 4. Jelaskan perbedaan antara _framework_ CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya? ###

Tailwind dan Bootstrap keduanya merupakan framework CSS yang sangat populer untuk digunakan. Berikut adalah beberapa perbedaan antar keduanya:

Bootstrap:
- Populer digunakan sebagai salah satu framework HTML, CSS, dan JavaScript untuk membuat aplikasi-aplikasi _mobile_ yang responsif
- Menawarkan banyak tema dan template yang siap digunakan
- Aplikasi yang dibuat dengan Bootstrap akan cenderung sama karena penggunaan template tersebut
- Butuh ukuran file yang besar
Tailwind CSS:
- Hanya menawarkan framework CSS untuk membuat tampilan _user interface_ yang _customizable_
- Menawarkan fitur-fitur yang mengutamakan utilitas
- Aplikasi yang dibuat dengan Tailwind CSS lebih beragam dan fleksibel
- Butuh ukuran file yang lebih kecil

Bootstrap lebih cocok digunakan ketika proyek yang kita kerjakan lebih fokus di _back-end_, dan tema-tema serta tampilan yang tidak begitu kompleks. Sedangkan, ketika kita membuat suatu proyek yang lebih berfokus kepada _front-end_, _user interfaces_, dan tampilan-tampilan, maka Tailwind CSS-lah yang akan menjadi pilihan utama.

### Jelaskan bagaimana kamu menerapkan checklist di atas secara step-by-step ###

- [x] Menyalakan _virtual environment_
- [ ] Membiasakan diri dan mempelajari basic syntax dan serba-serbi dari CSS, beserta Tailwind dan Bootstrap
- [ ] Memilih untuk menggunakan Bootstrap karena terdapat banyak template yang sudah siap untuk digunakan
- [ ] Membuat penyesuaian terhadap file-file html yang ingin diubah
- [ ] Mencoba menggunakan external CSS dengan staticfiles tetapi belum berhasil
- [ ] Melakukan git add, commit, dan push
