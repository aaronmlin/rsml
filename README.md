**Aaron Mario Lin - 2206082341**

**rsml.adaptable.io**
1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

Tutorial tentu banyak membantu saya dalam mengerjakan tugas kali ini, tetapi saya juga mengalokasikan sedikit waktu untuk memahami bagaimana cara kerja Django framework, dan version control git pula. Saya menantang diri saya untuk membaca ulang tutorial dari awal sampai akhir, lalu mencoba untuk mengerjakan tugas ini tanpa sambil melihatnya sama sekali. Untungnya, pada percobaan pertama sudah berhasil. Suatu bantuan tambahan juga didapatkan dari internet ketika mencapai tahap dimana saya sedikit bingung

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
Request(Client)    --->    urls.py    --->    views.py    --->    models.py    --->    HTML File
              GET request          URL routing         Business logic     Database query       Render template

3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

Virtual environment digunakan dalam proyek ini untuk mengisolasi dependensi proyek, mengelola versi Python yang berbeda, dan juga mempermudah pengelolaan proyek Django. Ini memungkinkan developer untuk menghindari konflik dependensi, menjaga supaya proyek tetap terorganisir, dan melindungi sistem dari masalah potensial, menjadikannya praktik yang sangat disarankan dalam pengembangan Python. Secara teoritis, bisa saja membuat suatu proyek Django tanpa menggunakan virtual environment, tetapi tentu tidak disarankan, karena alasan-alasan di atas.

4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.

-MVC (Model-View-Controller)
