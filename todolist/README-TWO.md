 1. Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
Asynchronous programming adalah proses jalannya program bisa dilakukan secara bersamaan tanpa harus menunggu proses antrian, sehingga dapat terus berinteraksi dengan halaman pada saat data sedang di-loads.
Synchronous programming adalah proses jalannya program secara sequential, disini yang dimaksud sequential ada berdasarkan antrian ekseskusi program. Pengguna harus menunggu saat halaman baru di-load (klik, tunggu, segarkan)

 2. Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
Event-Driven Programming merupakan paradigma yang menjelaskan bahwa alur yang dijalankan suatu program bergantung pada event atau tindakan yang terjadi antara user dan client. Pada tugas 6 ini paradigma terdapat pada dokumen yang akan ditampilkan, button untuk membuat form baru, dan event saat pemanggilan AJAX berhasil.

 3. Jelaskan penerapan asynchronous programming pada AJAX.
 Penerapan asyncronous programming pada AJAX terdapat pada fakta bahwa browser tidak perlu meng-suspend segala operasi yang dilakukan selama request AJAX berlangsung. Browser akan terus berjalan seperti biasa, bahkan dapat melaksanakan perintah lainnya di mana request tersebut berjalan di latar belakang. Oleh karena itu, AJAX dapat digunakan untuk mengubah tampilan website berdasarkan hasil tanpa memerlukan reload. AJAX juga menggunakan paradigma Event-Driven Programming, di mana setelah AJAX dilakukan, dapat memanggil fungsi yang diberikan pada onSuccess dan memberi data hasil ke fungsi tersebut.

 4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. Membuat 3 fungsi baru pada views.py yang masing-masingnya diberikan kode untuk autentikasi pengguna.
2. Membuat 3 routing tambahan untuk 3 fungsi yang baru dibuat di views.py tersebut.
3. Mengubah rendering menjadi AJAX, serta melakukan GET ke JSON B yang dilanjut dengan pembuatan card dari data yang dimasukkan.
4. Menyambungkan button create task dengan event onClick untuk menerapkan AJAX.
5. Mengatur ulang task untuk di render kembali ketika ada perubahaan yang dilakukan.
6. Mengerjakan bonus dengan menambahkan delete dengan id atau AJAX DELETE ke dalam program.
7. Membuat path khusus untuk delete berdasarkan id yang didapat dengan parameter id integer.
8. Menyambungkan button Delete pada card task untuk melakukan AJAX DELETE yang memungkinkan laman utama langsung ter-update.