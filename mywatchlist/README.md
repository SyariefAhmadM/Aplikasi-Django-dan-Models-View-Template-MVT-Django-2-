Berikut adalkah link Herokku App :
https://pbp-syarief.herokuapp.com/mywatchlist/

Bukti Screenshot Postman :
<img width="1419" alt="Screen Shot 2022-09-22 at 02 22 20" src="https://user-images.githubusercontent.com/112609721/191592291-859af049-2bdd-47d2-bf61-6e88206049e6.png">
<img width="1420" alt="Screen Shot 2022-09-22 at 02 23 08" src="https://user-images.githubusercontent.com/112609721/191592479-9d1e4016-beec-4cb7-88f2-d94b71eeacfc.png">
<img width="1421" alt="Screen Shot 2022-09-22 at 02 23 32" src="https://user-images.githubusercontent.com/112609721/191592567-646359de-c84c-4892-ae60-32eb0faeb356.png">

Jelaskan perbedaan antara JSON, XML, dan HTML!
`JSON`    : json merupakan singkatan dari __JavaScript Object Notation__, JSON merupakan sebuah format yang digunakan untuk membaca, menyimpan, atau bahkan menukar informasi dari web server sehingga dapat dibaca oleh para __user__. json sangat mudah digunakan karena memang didesain menjadi __self describing__. Data yang disimpan pada JSON terdiri dari dua struktur, yaitu key
`XML`     :
`HTML`    :

Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Karena kita perlu mengirimkan data dari satu stack ke stack lainnya dalam mengembangkan sebuah platform. Banyak contoh format data yang dapat kita gunakan untuk mengirimkan suatu data, tetapi yang paling umum adalah HTML,XML, dan juga JSON.

Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. Nyalan __virtual environment__ terlebih dahulu
2. Membuat `django-app` dengan nama `mywatchlist` dengan perintah `python manage.py startapp mywatchlist`
3. Menambahkan aplikasi `mywatchlist` ke dalam variabel `INSTALLED_APPS` pada file `settings.py` di folder `project_django`
4. Membuat model `MyWatchList` pada file `models.py` di folder `mywatchlist` dengan atribut `watched` sebagai deskripsi film, `title` sebagai judul film, `rating` sebagai penilian film dalam rentang 1-5, `release_date` yaitu kapan film tersebut dirilis, `review` sebagai __review__ film.
5. Menjalankan perintah `python manage.py makemigrations` untuk mempersiapkan migrasi skema model ke dalam __database__ Django.
6. Melakukan perintah `python manage.py migrate` untuk menerapkan skema model yang sudah dibuat ke dalam database Django.
7. Membuat sebuah folder bernama `fixtures` pada folder aplikasi yang sudah dibuat yaitu `mywatchlist`, kemudian membuat sebuah file bernama `initial_mywatchlist_data.json`, lalu menambahkan 10 data untuk objek `MyWatchList` pada file json tersebut.
8. Memasukkan data yang sudah dibuat ke dalam __database__ Django dengan perintah `python manage.py loaddata initial_mywatchlist_data.json`.
9. Membuat fungsi yang menerima parameter `request` dan mengembalikan `render(request, "mywatchlist.html")` pada file `views.py` di folder `mywatchlist`.
10. Membuat folder bernama `templates` pada folder aplikasi `mywatchlist`, dan membuat file `mywatchlist.html` pada folder tersebut.
11. Menambahkan __code__ html pada file `mywatchlist.html`
12. Membuat file `urls.py` pada folder `mywatchlist` untuk melakukan routing terhadap fungsi `views` yang sudah dibuat agar halaman HTML dapat muncul lewat __browser__. Isi dari `urls.py` adalah :
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
14. Import __models__ pada fungsi __views__ yang sudah saya buat kedalam file `views.py`
15. Menambahkan kode pada fungsi `show_mywatchlist` untuk memanggil fungsi __query__ ke __model database__, kemudian menyimpan hasil __query__ tersebut ke dalam variabel.
16. Menambahkan `context` sebagai parameter ketiga pada __return__ fungsi render.
17. Pada file `mywatchlist.html`, lakukan __loop__ terhadap variabel `list_mywatchlist` dan memanggil nama variabel dari objek yang sudah saya buat.
18. Melakukan __Data Delievery__ dengan format data XML dan JSON seperti yang sudah dijelaskan pada Lab-2
