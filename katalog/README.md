Link Heroku = https://pbp-syarief.herokuapp.com/katalog/
![Bagan-PBP](https://user-images.githubusercontent.com/112609721/190241819-26f90bc0-7ae3-44c1-b623-bf69ae413350.png)
Sesuai bagan tersebut, kaitan antara urls.py, views.py, models.py, dan berkas html adalah :
Permintaan user yang masuk kedalam server django akan diproses melalui urls agar dapat diteruskan kedalam views yang didefinisikan oleh developer untuk memproses request tersebut. Namun, apabila terdapat proses yang membutuhkan keterlibatan database(Basis data) akan mengembalikan hasil dari query tersebut kedalam views. Setelah request tersebut selsai diproses, hasil dari proses tersebut akan dihubungkan ke dalam HTML yang sudah didefinisikan sebelum akhirnya HTML tersebut dikembalikan ke user sebagai respons
Karena dengan Virtual environment (lingkungan virtual), kita dapat memisahkan pengaturan dan package yang diinstal pada setiap proyek django yang kita buat, sehingga perubahan yang dilakukan pada satu proyek tidak mempengaruhi proyek lainnya. Dengan kata lain, setiap proyek Django sebaiknya memiliki virtualenv-nya sendiri. Kita tetap bisa membuat sebuah aplikasi web berbasis django tanpa menggunakan virtual environment, tetapi dikhawatirkan apabila kita melakukan suatu perubahan pada satu proyek, maka proyek lainnya ikut terubah.
Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.
1. Pertama-tama, sebelum kita melakukan modifikasi pada template yang diberikan, masuk kedalam repository yang sudah kita clone lalu buatlah terlebih dahulu virtual enviroment dengan perintah : python -m venv env
2. Nyalakan virtual environment dengan perintah yang sesuai dengan jenis sistem operasi masing-masing, disini saya menggunakan MAC OS : source env/bin/activate
3. Install dependencies yang diperlukan untuk menjalankan proyek Django dengan perintah pip install -r requirements.txt
4. Jalankan proyek django yang telah dibuat dengan perintah python manage.py runserver dan membuka http://localhost:8000 di browser untuk memastikan bahwa proyek Django dapat berjalan dengan baik.
5. Lakukan perintah python manage.py makemigrations untuk mempersiapkan migrasi skema model ke dalam database Django lokal.
6. Menjalankan perintah python manage.py migrate untuk menerapkan skema model yang telah dibuat ke dalam database Django lokal.
7. Menjalankan perintah python manage.py loaddata initial_catalog_data.json untuk memasukkan data tersebut ke dalam database Django lokal.
8. Pada views.py yang ada dalam folder katalog, kita membuat sebuah fungsi yang menerima parameter request dan mengembalikan render(request, "katalog.html"), yaitu dengan kode 
def show_katalog(request): 
    return render(request, "katalog.html")
10. Melakukan routing terhadap fungsi views yang telah dibuat sehingga nantinya halaman HTML dapat ditampilkan lewat browser. Isi dari urls.py tersebut adalah 
from django.urls import path
from katalog.views import show_katalog

app_name = 'katalog'
urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
]
10. Mendaftarkan aplikasi katalog ke dalam urls.py pada folder project_django dengan menambahkan kode : 
path('katalog/', include('katalog.urls')),

11. Menjalankan proyek Django dengan perintah python manage.py runserver dan membuka http://localhost:8000/wishlist/ di browser untuk melihat halaman yang sudah dibuat.
12.  Meng-import models yang sudah dibuat (CatalogItem) ke dalam file views.py. Dengan " from wishlist.models import CatalogItem ", kita akan menggunakan class tersebut untuk melakukan pengambilan data dari database.
Menambahkan potongan kode dibawah ini ke dalam fungsi show_catalog yang sudah dibuat. Potongan kode ini berfungsi untuk memanggil fungsi query ke model database dan menyimpan hasil query tersebut ke dalam sebuah variabel.
data_katalog_item = CatalogItem.objects.all()
    context = {
        'list_catalog': data_katalog_item,
        'nama': 'mas Syarief',
        'npm': '2106653445'
    }
13. Menambahkan context sebagai parameter ketiga pada pengembalian fungsi render di fungsi yang sudah dibuat. Data yang ada pada variabel context tersebut akan ikut di-render oleh Django sehingga nantinya dapat memunculkan data tersebut pada halaman HTML.
return render(request, "katalog.html", context)
14. Mengubah Fill me! di file HTML yang ada pada folder template, dalam HTML tag <p> menjadi {{nama}} dan {{npm}} untuk menampilkan nama dan npm di halaman HTML.
15. Menambahkan potongan kode berikut untuk menampilkan daftar katalog ke dalam tabel.
  {% for katalog in lsit_catalog %}
    <tr>
        <th>{{katalog.item_name}}</th>
        <th>{{katalog.item_price}}</th>
        <th>{{katalog.item_stock}}</th>
        <th>{{katalog.description}}</th>
        <th>{{katalog.rating}}</th>
        <th>{{katalog.item_url}}</th>
    </tr>
{% endfor %}
16. Melakukan add, commit, dan push untuk menyimpan kedalam repositori GitHub.
17. Membuat nama aplikasi pada Heroku dan menyimpan API key, kemudian menambahkan 2 variabel repository secret baru yaitu HEROKU_API_KEY dengan API key kita dan HEROKU_APP_NAME dengan nama aplikasi yang telah kita buat pada Heroku, lalu melakukan re-run jobs pada GitHub Actions. 
