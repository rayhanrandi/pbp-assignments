# README-TWO Tugas 6

## Perbedaan _asynchronous_ dan _synchronous programming_
Pada _asynchronous programming_, ketika kita membuat sebuah _request_, akan terbuat suatu _endpoint_ yang akan dijalankan kembali setelah _request_ terproses. Lalu, _request_ akan diproses dan setelah selesai, endpoint yang tadi terbuat akan dipanggil kembali. Selain itu, _asynchronous programming_ tidak memberhentikan operasi-operasi lainnya pada aplikasi sambil menunggu _return_ dari _request_ kita. Sementara itu pada _synchronous programming_, ketika kita membuat _request_ maka operasi-operasi lain akan berhenti dan mulai kembali ketika kita sudah menerima data hasil _return_ dari _request_ tadi.

## _Event-Driven Programming_
_Event-Driven Programming_ merupakan paradigma pemrograman dimana alur dari program ditentukan oleh berbagai tipe _event_ seperti _mouse-click_, _keypress_, dan lain-lain. _Event-Driven Programming_ bekerja dengan cara membuat sebuah _trigger_ yang akan memanggil sebuah fungsi atau blok-blok kode yang akan dijalankan ketika _trigger_ teraktivasi. Setelah blok-blok kode dijalankan, maka alur program akan berlanjut seperti semula sebelum _trigger_ teraktivasi.

Pada pengimplementasian aplikasi ini, penerapan _Event-Driven Programming_ sendiri terdapat pada fitur _Create New Task_ dimana jika tombol tersebut di-klik pengguna, maka flow program akan menjalankan fungsi yang bersesuaian untuk membuat sebuah form yang dapat diisi dengan data-data _task_ oleh pengguna, flow dialhikan kembali dengan memanggil fungsi yang menampilkan _tasks_ yang dimiliki pengguna untuk melihat _task_ yang baru saja ditambahkan.

## _Asynchronous programming_ pada AJAX
_Asynchronous programming_ diterapkan pada AJAX melalui kemungkinan dibuatnya aplikasi yang dapat menjalankan sebuah function yang mengubah berbagai macam elemen pada halaman tanpa _refresh_ yang dapat memberhentikan operasi-operasi lainnya yang berjalan selain function tersebut, sehingga _return_ dari function yang telah dipanggil secara _asynchronous_ dapat ditampilkan kembali tanpa me-_refresh_ halaman.

## Implementasi aplikasi
Pengimplementasian aplikasi dengan AJAX dilakukan dengan menggunakan _functions_ untuk setiap fitur yang ada agar fitur dapat di-_execute_ dan mengembalikan hasil tanpa me-_refresh_ halaman. _Function_ ```getTasks()``` dibuat untuk mengambil data berbentuk JSON dengan AJAX GET, lalu data yang telah diambil dialirkan ke _function_ ```showTasks()``` untuk menampilkan data secara _asynchronous_ dengan menggunakan forEach loop yang mengiterasi tiap data dan menampilkannnya dengan meng-_append_ data dan elemen HTMLnya ke sebuah elemen yang telah ditentukan dalam sebuah variabel. Selain itu, dibuat juga 3 _function_ lain yaitu ```deleteTasks()```, ```toggleTasks()```, dan ```addTasks()```. ```deleteTasks()``` merupakan sebuah _function_ AJAX DELETE yang berfungsi untuk memanggil views yang sesuai untuk menghapus task dengan id yang sesuai. ```toggleTasks()``` berfungsi untuk memanggil url toggle yang juga akan memanggil view yang bersesuaian untuk mengatur apabila _task_ sudah selesai atau belum. Yang terakhir yaitu ```addTasks()```, berfungsi untuk menampilkan sebuah modal yang didialamnya terdapat form yang berisi field title dari task dan description dari task. Terdapat juga tombol _Create new task_ dalam modal, yang berfungsi untuk memanggil view yang berguna untuk membuat task baru sesuai input dari field yang ada pada modal lalu juga menampilkan kembali _task-task_ tersebut.


##### _Rayhan Putra Randi | 2106705644 | PBP-A_
