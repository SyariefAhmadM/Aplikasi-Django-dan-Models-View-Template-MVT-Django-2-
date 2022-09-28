1. Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?
CSRF adalah singkatan dari Cross Site Request Forgery, yaitu salah satu serangan tertua dan paling sederhana pada suatu web. Django mempunyai built in protection untuk sebagian besar jenis CSRF. CSRF memiliki token yang berfungsi untuk melakukan validasi terhadap permintaan yang sesuai dan menolak permintaan apabila token dari CSRF tidak valid. Token dari CSRF akan dikirmkan secara sembunyi dalam bentuk <input> pada bagian Form HTML yang dikirimkan menggunakan metode POST.  Biasanya {% csrf_token %} ditempatkan dalam HTML sebelum input dan lokasi mana-pun di mana data yang dapat dikontrol user disematkan dalam HTML. Fungsi dari {% csrf_token %} adalah untuk mengurangi berbagai teknik di mana para penyerang web dapat menggunakan data yang dibuat untuk memanipulasi dokumen HTML dan menangkap bagian dari isi code HTML tersebut. Namun, apabila di dalam sebuah dokumen HTML tidak terdapat {% csrf_token %}, maka website tidak dapat melakukan validasi terhadap user yang seharusnya sehingga akan dengan mudah web tersebut dapat di hack oleh user lain.

2. Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.
Bisa, kita tidak harus menggunakan {{ form.as_table }} untuk membuat form. Kita dapat membuat Form secara manual dengan menggunakan tag input, textarea, select, option, dan masih banyak lagi. Tag tersebut dapat kita tambahkan dengan contoh atribut seperti name dan juga type yang sesuai dengan form. Nilai dari atribut name tersebut akan menjadi variable form.

3. Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
Ketika user klik tombol buat, maka akan dikirimkan

4.Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. Membuat django-app bernama todolist dan menambahkan todolist ke dalam variable INSTALLED_APPS pada file settings.py di folder project_django
2. Menambahkan aplikasi todolist ke dalam urls.py pada folder project_django
3. Membuat model task yang memiliki atribut user, date, title, description.
4. Membuat form registrasi, form Login fungsi logout, fungsi show_todolist, dan fungsi new_task pada views.py
5. Merestriksi akses halaman todolist
6. Menambahkan cookies
7. Membuat urls.py dan urlpatterns  
8. Menambahkan path url ke dalam urlpatterns dari seluruh fungsi pada views.py
9. Membuat 4 html yaitu, register, login, todolist, dan task. Fungsi dari views.py nantinya akan dilanjutkan ke html ini.
10. Git add, commit, push dan deploy ke Heroku
11. Membuat 2 akun dan 3 data pada akun Heroku
