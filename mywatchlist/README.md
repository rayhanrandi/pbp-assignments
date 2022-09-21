# README

### Link Aplikasi Heroku: [HTML](https://pbp-assignments-mywatchlist.herokuapp.com/mywatchlist/html/), [XML](https://pbp-assignments-mywatchlist.herokuapp.com/mywatchlist/xml/), [JSON](https://pbp-assignments-mywatchlist.herokuapp.com/mywatchlist/json/)


## HTML, XML, dan JSON

**HTML** atau _Hyper Text Markup Language_ merupakan sebuah _markup language_ yang dapat digunakan untuk menyajikan data pada _web browser_. Pada HTML, penyajian data dapat dibantu dengan _styling_ yang dapat ditentukan sesuai kemauan _developer_ melalui berbagai _tags_ atau _element_ seperti ```<img />``` yang terdapat pada HTML itu sendiri. 

**XML** atau _eXtensible Markup Language_ merupakan _markup language_ yang dibuat dengan fokus untuk menyajikan data dengan _simple, general,_ dan _usable_ di Internet. XML juga menggunakan format yang sangat _human-readable_ dan _machine-readable_ sehingga data yang disajikan mudah dipahami. Format penulisan XML mirip seperti HTML dengan menggunakan _tags_ ```< >``` dan  juga disusun oleh _element-element._

**JSON** atau _JavaScript Object Notation_ adalah format file yang bersifat _human-readable_ juga seperti XML namun ditulis dengan _attribute-value pairs_ serta _arrays_ agar data tersimpan dengan rapih dan mudah dipahami. Karena JSON merupakan turunan dari JavaScript, maka syntax dan tipe datanyua juga mirip dengan JavaScript sendiri.

## Mengapa _data delivery_ dibutuhkan dalam pengimplementasian sebuah platform?

Pada pengimplementasian platform, sebagian besar tumpuan platform yang dibuat berada pada data yang diterima dan disajikan oleh, maupun untuk penggunanya. Maka dari itu, _data delivery_ pada pengimplementasian sebuah platform merupakan aspek penting yang harus diperhatikan agar platform dapat dimanfaatkan dan digunakan secara maksimal oleh penggunanya, dan juga _developer_ untuk _debugging_. Dari urgensi itulah maka HTML, XML, serta JSON dibuat.

## Pengimplementasian aplikasi

Sebelum memulai, dinyalakan terlebih dahulu _virtual environment_ pada direktori project yang akan dikerjakan dan juga install requirements yang dibutuhkan project. Setelah itu, karena tugas ini merupakan project baru, maka jalankan command ```python manage.py startapp mywishlist```. Lalu, tambahkan nama aplikasi sebagai elemen baru pada variabel ```INSTALLED_APPS``` dalam file ```project_django/settings.py```. Langkah selanjutnya dilakukan dengan membuat models sesuai ketentuan tugas dan _me-migrate_ model ke databse django lokal. Karena model untuk data sudah tersedia, maka dilanjut dengan membuat object-object film yang akan ditampilkan dalam HTML dengan membuat file baru ```initial_watchlist_data.json``` dan mengisinya dengan object film yang memiliki field sesuai ketentuan modelnya. Untuk memasukkan data tersebut ke database django lokal, dijalankan _command_ ```python manage.py loaddata initial_watchlist_data.json```.

Setelah data tersedia, dapat diimplementasikan views project dengan mengisi file ```views.py``` dengan sebuah fungsi ```show_watchlist``` yang menerima request user, memuat data untuk ditampilkan di HTML, dan mengembalikan perintah render yang akan menampilkan HTML berisi data film-film yang telah dibuat. Dalam file ini juga dibuat fungsi seperti diatas namun untuk menampilkan data dalam format XML dan juga JSON yang dapat diakses secara keseluruhan maupun dari id tiap object yang dibuat.

File HTML yang akan digunakan untuk menampilkan data sendiri juga kita buat dalam sebuah folder bernama ```templates``` dengan nama file ```mywatchlist.html```. File tersebut berfungsi untuk memanggil tiap film dan menampilkannya sesuai format _styling_ yang dibuat dalam file HTML tersebut.

Lanjut pada routing, dibuat file baru ```urls.py``` pada folder ```mywatchlist``` yang diisi dengan path untuk membagi routing menjadi tiga yang dapat menampilkan data dalam format HTML, XML, dan juga JSON beserta dengan idnya. Lalu, pada file ```project_django/urls.py``` ditambahkan path yang memanggil file ```urls.py``` yang telah dibuat tadi untuk menyalurkan request sesuai format yang diinginkan.

Terakhir, untuk unit testing dilakukan dengan mengisi file ```tests.py``` dengan empat fungsi yang berfungsi untuk mencek apabila _url_ yang ditentukan dapat diakses/ada pada aplikasi atau tidak serta juga mencek apabila aplikasi menggunakan template yang benar. Setalah _unit test_ berjalan, aplikasi dapat _dideplou_ ke Heroku dengan ```git add```, ```git commit```, dan ```git push``` ke repository yang telah diatur API key dan nama aplikasinya agar aplikasi dapat _terdeploy_ ke Heroku.

## Preview aplikasi setelah _deployment_

##### HTML
![HTML](mywatchlist/postmanhtml.jpg)

##### XML
![XML](mywatchlist/postmanxml.jpg)

##### JSON
![JSON](mywatchlist/postmanjson.jpg)


##### _Rayhan Putra Randi | 2106705644 | PBP-A_
