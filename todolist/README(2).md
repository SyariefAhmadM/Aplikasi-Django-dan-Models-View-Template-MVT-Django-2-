https://pbp-syarief.herokuapp.com/todolist/

1. Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?
Terdapat 3 cara untuk menerapkan CSS :
- Inline style         : Membuat style CSS langsung pada tag HTML-nya, biasanya menggunakan atribut `<style>`.
- Internal style sheet : Membuat style CSS di dalam file HTML-nya, biasanya diletakkan di dalam bagian <head> dengan atribut `<style>`.
- External style sheet : Membuat style CSS dengan file yang terpisah dari HTML-nya, yaitu dengan membuat file `.css` sendiri.

Kelebihan menggunakan Inline CSS:
-Berguna jika Anda ingin menguji dan melihat perubahan
-Berguna untuk perbaikan cepat
-Permintaan HTTP yang lebih kecil

Kekurangan menggunakan inline CSS:
-Inline CSS harus diterapkan pada setiap elemen

Kelebihan menggunakan internal CSS:
-Perubahan hanya terjadi pada 1 halaman
-Class dan ID bisa digunakan oleh internal stylesheet
-Tidak perlu meng-upload beberapa file karena HTML dan CSS bisa digunakan di file yang sama.

Kekurangan menggunakan Internal CSS:
-Meningkatkan waktu akses website
-Perubahan hanya terjadi pada 1 halaman – tidak efisien bila Anda ingin menggunakan CSS yang sama pada beberapa file.

Kelebihan menggunakan CSS eksternal:
-Ukuran file HTML menjadi lebih kecil dan strukturnya lebih rapi
-Kecepatan loading menjadi lebih cepat
-File CSS yang sama bisa digunakan di banyak halaman.

Kekurangan menggunakan CSS eksternal:
-Halaman belum tampil secara sempurna hingga file CSS selesai dipanggil.

2. Jelaskan tag HTML5 yang kamu ketahui.
HTML5 merupakan versi terbaru HTML. HTML 5 adalah revisi dari Hypertext Markup Language (HTML), bahasa pemrograman standar untuk menggambarkan konten dan tampilan halaman Web. HTML5 dikembangkan untuk menyelesaikan masalah kompatibilitas yang memengaruhi standar saat ini, HTML4. Salah satu perbedaan terbesar antara HTML5 dan versi standar sebelumnya adalah bahwa versi HTML yang lebih lama memerlukan plugins dan API eksklusif. (Inilah sebabnya mengapa halaman Web yang dibangun dan diuji dalam satu browser mungkin tidak dimuat dengan benar di browser lain.) HTML5 menyediakan satu antarmuka umum untuk membuat elemen dimuat dengan lebih mudah. Misalnya, tidak perlu menginstal plugin Flash di HTML5 karena elemen akan berjalan dengan sendirinya. Salah satu tujuan desain untuk HTML5 adalah mendukung multimedia di perangkat seluler. Fitur sintaksis baru diperkenalkan untuk mendukung ini, seperti tag video, audio dan kanvas. 
  
3. Jelaskan tipe-tipe CSS selector yang kamu ketahui.
Dalam memilih elemen berdasarkan nama tag untuk menambahkan style. selector class (misal : .login{}) akan memilih elemen berdasarkan nama class yang diberikan untuk menambahkan style. selector id (misal : #style {}) bersifat lebih unik sehingga dapat digunakan oleh satu elemen saja untuk menambahkan style. selector pseudo akan memilih elemen semu seperti state pada elemen, pada selector ini terdapat dua macam selector pseudo, yaitu pseudo-element dan pseudo-class. selector atribut akan memilih elemen berdasarkan atribut untuk menambahkan style.
  
4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
Meletakkan link bootstrap pada bagian head atau menginstall bootstrap agar bootstrap dapat connect ke HTML, dan jangan lupa meletakkan load static agar ketika kita menggunakan css external dapat terpanggil
Pada page login dan create task, saya hanya menggunakan css dengan menambahkan form. Serta mengubah tampilan dengan memberikan warna gradient serta shadow pada form. Pada register, saya menggunakan class cards lalu table register dimasukkan kedalam cards tersebut. Selanjutnya, mengatur posisi tengah pada cards tersebut
Pada page todolist, kita menambahkan class berupa cards yang mana cards tersebut di foorlop dan ketika cards berjumlah lebih dari 3, maka cards selanjutnya akan ditampilkan pada line berikutnya, saya juga menggunakan navbar collapse serta footer yang menandakan akhir bagian dalam page tsb
