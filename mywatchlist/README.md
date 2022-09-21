Berikut adalkah link Herokku App :
https://pbp-syarief.herokuapp.com/mywatchlist/

Bukti Screenshot Postman :
<img width="1419" alt="Screen Shot 2022-09-22 at 02 22 20" src="https://user-images.githubusercontent.com/112609721/191592291-859af049-2bdd-47d2-bf61-6e88206049e6.png">
<img width="1420" alt="Screen Shot 2022-09-22 at 02 23 08" src="https://user-images.githubusercontent.com/112609721/191592479-9d1e4016-beec-4cb7-88f2-d94b71eeacfc.png">
<img width="1421" alt="Screen Shot 2022-09-22 at 02 23 32" src="https://user-images.githubusercontent.com/112609721/191592567-646359de-c84c-4892-ae60-32eb0faeb356.png">

Jelaskan perbedaan antara JSON, XML, dan HTML!

JSON    : JSON merupakan singkatan dari **JavaScript Object Notation**, JSON merupakan sebuah format yang digunakan untuk membaca, menyimpan, atau bahkan menukar informasi dari web server sehingga dapat dibaca oleh para **user**. JSON sangat mudah digunakan karena telah didesain menjadi **self describing**. Data yang disimpan pada JSON terdiri dari **key** dan **value**. **value** dapat terbagi menjadi dua struktur, yaitu **value** yang saling berpasangan seperti **object** dan **value** yang berupaa tipe data primitif seperti **string, number, boolean**. Sintaks JSON adalah turunan dari **Object JavaScript**. Namun, format json berupa **text**, sehingga membuat & membaca JSON dapat digunakan oleh bahasa pemrograman lain seperti PHP, C++, Python, dan juga Ruby. 

XML     : XML merupakan singkatan dari **eXtensible Markup Language**. XML telah digunakan pada banyak aplikasi web ataupun **mobile**, yang berfungsi untuk mengirimkan dan menyimpan sebuah data. XML telah didesain menjadi **self-descriptive**, sehingga kita dapat mengerti informasi apa yang ingin disampaikan dari data yang tertulis dengan membaca XML tersebut. XML ini hanyalah informasi yang dibungkas dalam tag.

HTML    : HTML merupakan singkatan dari **Hypertext Markup Language** atau "bahasa markup". Secara umum, HTML merupakan standar pemrograman yang berfungsi untuk membuat / membangun sebuah halaman pada **website** yang nantinya dapat diakses dan ditampilkan melalui internet. 

Perbedaan JSON dan XML adalah : 
- JSON lebih mudah dibaca dibanding XML.
- JSON mengandung tags awal dan akhir sedangkan XML tidak
- JSON support array sedangkan XML tidak

Perbedaan antara HTML dan XML adalah :
- HTML digunakan untuk menampilkan sesuatu pada **browser** internet
- XML berfungsi untuk transpor dan penyimpanan suatu data.

Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Karena kita perlu mengirimkan data dari satu stack ke stack lainnya dalam mengembangkan sebuah platform. Banyak contoh format data yang dapat kita gunakan untuk mengirimkan suatu data, tetapi yang paling umum adalah HTML,XML, dan juga JSON.

Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. Nyalan **virtual environment** terlebih dahulu
2. Membuat `django-app` dengan nama `mywatchlist` dengan perintah `python manage.py startapp mywatchlist`
3. Menambahkan aplikasi `mywatchlist` ke dalam variabel `INSTALLED_APPS` pada file `settings.py` di folder `project_django`
4. Membuat model `MyWatchList` pada file `models.py` di folder `mywatchlist` dengan atribut `watched` sebagai deskripsi film, `title` sebagai judul film, `rating` sebagai penilian film dalam rentang 1-5, `release_date` yaitu kapan film tersebut dirilis, `review` sebagai **review** film.
5. Menjalankan perintah `python manage.py makemigrations` untuk mempersiapkan migrasi skema model ke dalam **database** Django.
6. Melakukan perintah `python manage.py migrate` untuk menerapkan skema model yang sudah dibuat ke dalam database Django.
7. Membuat sebuah folder bernama `fixtures` pada folder aplikasi yang sudah dibuat yaitu `mywatchlist`, kemudian membuat sebuah file bernama `initial_mywatchlist_data.json`, lalu menambahkan 10 data untuk objek `MyWatchList` pada file json tersebut.
8. Memasukkan data yang sudah dibuat ke dalam **database** Django dengan perintah `python manage.py loaddata initial_mywatchlist_data.json`.
9. Membuat fungsi yang menerima parameter `request` dan mengembalikan `render(request, "mywatchlist.html")` pada file `views.py` di folder `mywatchlist`.
10. Membuat folder bernama `templates` pada folder aplikasi `mywatchlist`, dan membuat file `mywatchlist.html` pada folder tersebut.
11. Menambahkan **code** html pada file `mywatchlist.html`
12. Membuat file `urls.py` pada folder `mywatchlist` untuk melakukan routing terhadap fungsi `views` yang sudah dibuat agar halaman HTML dapat muncul lewat **browser**. Isi dari `urls.py` adalah :
```
from django.urls import path
from mywatchlist.views import show_mywatchlist

app_name = 'mywatchlist'

urlpatterns = [
    path('', show_mywatchlist, name='show_mywatchlist'),
]
```
13. Mendaftarkan aplikasi `mywatchlist` ke dalam `urls.py` pada variabel `urlpatterns` di folder `project_django` dengan tambahan kode : 
`path('wishlist/', include('wishlist.urls')),`
14. Import **models** pada fungsi **views** yang sudah saya buat kedalam file `views.py`
15. Menambahkan kode pada fungsi `show_mywatchlist` untuk memanggil fungsi **query** ke **model database**, kemudian menyimpan hasil **query** tersebut ke dalam variabel.
16. Menambahkan `context` sebagai parameter ketiga pada **return** fungsi render.
17. Pada file `mywatchlist.html`, lakukan **loop** terhadap variabel `list_mywatchlist` dan memanggil nama variabel dari objek yang sudah saya buat.
18. Melakukan **Data Delievery** dengan format data XML dan JSON seperti yang sudah dijelaskan pada Lab-2
