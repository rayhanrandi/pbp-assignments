# README 4

### Link Aplikasi Heroku: [Todolist](http://pbp-assignment4.herokuapp.com/todolist/)

## 1. ```{% csrf_token %}```

CSRF (_Cross Site Request Forgery_) token merupakan sebuah _secure random token_ yang berfungsi untuk menghindari adanya _actions_ tidak diinginkan yang dilakukan oleh _malicious_ user dengan meng-_assign_ setiap sesi user dengan sebuah token yang memiliki _value_ besar dan random sehingga sulit untuk diretas.

Pada elemen ```<form>```, ```{% csrf_token %}``` digunakan untuk memastikan bahwa user yang terautentikasi benar-benar merupakan user yang mengirimkan data melalui ```<form>``` tadi dengan cara memvalidasi field ```csrfmiddlewaretoken``` sesuai dengan value yang tersimpan di cookie. Tanpa ada ```{% csrf_token %}``` pada elemen ```<form>```, halaman tetap bisa berjalan namun akan menjadi lebih _vulnerable_ karena ada kemungkinan user yang tidak terautentikasi dapat mengakses halaman yang seharusnya _restricted_ untuk user yang sedang berada pada sesi.


## 2. Pembuatan elemen ```<form>``` secara manual

Implementasi elemen ```<form>``` tidak harus menggunakan sebuah generator seperti contohnya ```{{ form.as_table }}```. Untuk membuat sebuah elemen ```<form>``` secara manual, pertama kita dapat membuat sebuah elemen ```<form>``` nya sendiri dengan memasukkan url untuk fungsi yang akan kita panggil dengan menggunakan method ```POST```. Lalu, pada elemen yang diletakkan di table, diberikan sebuah nama agar nanti data yang dimasukkan ke form dapat dipanggil ulang dengan cara ```request.POST.get(<nama_field_form>)``` dan diolah sesuai dengan fungsi yang dipanggil.


## 3. Proses alur data form HTML dari submisi hingga _template_

Dari submisi ```<form>``` pada field yang sudah diberi nama, data lalu dipanggil pada fungsi yang bersesuaian dengan ```<form>``` tersebut pada file ```views.py```. Misal pada ```create_task.html```, terdapat dua field form yang diberi nama "title" dan "description". Ketika user meng-klik tombol "Tambah Task", maka akan terpanggil url fungsi yang telah di-_map_ kepada tombol "Tambah Task" tadi untuk mengolah input user sesuai dengan field yang telah diberi nama tadi. Data dapat diambil dengan menggunakan ```request.POST.get(<nama_field>)``` dimana pada kasus ini nama field dapat berupa "title" atau "description". Lalu, setelah kedua data diambil, maka akan dibuat sebuah object Task baru dengan field user sesuai dengan user yang membuat request, date yang berisikan tanggal user membuat task, dan juga title dan description sesuai dengan data yang disubmit user tadi. Setelah object dibuat, maka akan dipanggil lagi fungsi untuk menampilkan halaman todolist agar Task yang baru dibuat dapat dilihat kembali oleh user yang membuatnya. Saat pemanggilan object Task tadi, digunakan juga ```Task.objects.filter(user=user)``` agar halaman todolist hanya menampilkan task-task yang dibuat oleh user tersebut saja.


## 4. Proses pengimplementasian app

1. Buat app baru pada directory tugas yang lalu dengan ```python manage.py startapp todolist```
2. Membuat routing sesuai ketentuan app pada ```project_django/urls.py```, ```todolist/urls.py```, dan juga membuat template yang diakses oleh routing url tadi pada file ```templates``` yang akan diisi ```create_task.html```, ```login.html```, ```register.html```, dan ```todolist.html```.
3. Membuat model dengan field-field sesuai ketentuan lalu me-_migrate_ model tersebut ke database dengan ```python manage.py makemigrations``` lalu ```python manage.py migrate```.
4. Membuat sebuah file baru ```/todolist/forms.py``` untuk menampilkan form ```create_task.html``` yang dapat digunakan user untuk mensubmit data untuk ditampilkan pada halaman todolist nanti.
5. Isi file-file template yang telah dibuat dengan form-form yang dapat digunakan user untuk me-register user, melakukan login, dan mensubmit data untuk ditampilkan pada halaman ```todolist.html```.
6. Buat fungsi-fungsi yang dibutuhkan pada ```todolist/views.py``` untuk login, logout, register, melakukan hal-hal yang diinginkan user pada halaman tertentu, dan juga untuk mengambil data dari form pada file-file di template, mengolahnya, lalu menampilkannya kembali di ```templates/todolist.html```.
7. Deploy project yang telah dibuat ke github dan Heroku dengan ```git add```, ```git commit```, dan ```git push``` setelah menyesuaikan API_KEY dan APP_NAME secrets pada repository github.
8. Buat akun _dummy_ beserta tasknya sesuai dengan ketentuan soal.



# README 5

## 1. Inline, Internal, dan External CSS

Inline CSS merupakan metode untuk menerapkan styling pada elemen-elemen HTML dengan memberikan
style ke tag HTML tertentu menggunakan ```<style>``` yang dituliskan di dalam file HTMLnya juga.
Penggunaan Inline CSS bermanfaat jika kita ingin mencoba-coba perubahan dalam skala kecil serta
juga untuk memperbaiki suatu kesalahan pada styling dengan cepat. Selain itu, request yang dibuat
untuk mengakses halaman dengan Inline CSS juga lebih kecil. Walaupun begitu, Inline CSS kurang 
efektif karena harus diterapkan untuk setiap elemen satu per satu.

Internal CSS merupakan penerapan styling mirip seperti Inline CSS, namun untuk kode CSSnya diletakkan
dalam tag ```<head>``` halaman HTML yang dimodifikasi. Intenal CSS berguna jika kita hanya ingin 
merubah sesuatu yang ada di spesifik suatu halaman. Internal CSS juga memiliki kelebihan dimana
Class dan ID bisa digunakan oleh internal stylesheet dan juga kita tidak perlu meng-upload 
berbagai macam file untuk styling karena styling digunakan di dalam halaman yang sama.
Metode styling ini juga memiliki kekurangan, yaitu akan meningkatkan waktu akses ke halaman dan
juga perubahan yang dibuat hanya akan berlaku di halaman dimana styling dibuat, sehingga tidak
efektif jika ada elemen yang perubahannya seharusnya berlaku untuk setiap halaman.

External CSS, best practice untuk styling, merupakan metode dimana stylesheet untuk suatu halaman
diletakkan di file .CSS external, tidak di dalam file HTMLnya. Untuk menerapkan style yang sudah
dibuat dalam file .CSS, file .CSS external ditulis dalam bagian <head> dari HTML. Metode ini merupakan
best practice karena ukuran file HTML menjadi lebih kecil, loading halaman menjadi lebih cepat, 
serta juga style yang dibuat pada CSS bersifat reusable untuk halaman-halaman lainnya. Namun, 
halaman yang menggunakan external CSS hanya akan tampil secara sempurna ketika file .CSSnya 
selesai dipanggil.


## 2. Tag pada HTML

- ```<table>```: untuk membuat table yang dapat diisi data yang ingin ditampilkan
- ```<th>```: header untuk sebuah cell dalam table
- ```<tr>```: untuk membuat baris dalam sebuah table
- ```<td>```: untuk membuat cell dalam table
- ```<h1>-<h6>```: header untuk teks
- ```<form>```: untuk membuat sebuah form yang didalamnya terdapat kode yang mengambil sebuah input
- ```<button>```: untuk membuat sebuah tombol yang dapat diinteraksikan oleh user
- ```<style>```: untuk mendefinisikan styling yang digunakan halaman (CSS)
- ```<a>```: membuat sebuah hyperlink


## 3. Selector-selector CSS

- ```.<nama class>```: akan menerapkan styling untuk setiap elemen yang memiliki class sesuai nama
- ```#<id elemen>```: menerapkan styling ke elemen yang memiliki id sesuai nama
- ```*:``` akan menerapkan styling ke setiap elemen
- ```element1>element2:``` menerapkan styling ke elemen2 yang memiliki parent elemen1
- ```:first-child:``` menerapkan styling ke elemen yang merupakan elemen child pertama dari parent elemennya
- ```:hover:``` menerapkan styling yang aktif ketika cursor berada diatas elemen
- ```:link:``` menerapkan styling kepada semua link yang belum dibuka user
- ```:visited:``` menerapkan styling kepada semua link yang sudah dibuka user


## 4. Proses pengimplementasian app

Untuk app ini, dilakukan styling pada template-template yang digunakan oleh aplikasi. Styling yang digunakan pada app ini berfokus kepada container dengan class _cards_, dimana contoh pengimplementasiannya salah satunya terdapat pada file ```todolist.html``` seperti berikut:

```
...
<div class="container">
    <h2>Welcome, <span style="color: var(--blue);">{{ request.user }}</span></h2>
    <br>
    <h4 style="font-weight: bold;">Tasks:</h4>
    <ul class="cards">
      {% for task in list_todolist %}
        <li class="card">
          <div>
            <h3 class="card-title">{{ task.title }}</h3>
            <h6 class="card-date">{{ task.date }}</h6>
            {% if task.is_finished %}
              <h6 style="font-weight: bold; color: green">DONE</h6>
            {% else %}
              <h6 style="font-weight: bold; color: red">NOT DONE</h6>
            {% endif %}
              <div class="card-content">
              <p>{{ task.description }}</p>
            </div>
          </div>
          <div class="card-link-wrapper">
            <form action="{% url 'todolist:toggle_task' id=task.id %}" method="post">
              {% csrf_token %}
              <button style="float: left; margin-right: 4px;"class="btn btn-success" type="submit" ><i class="btn-success"></i>Toggle</button>
            </form>
            <form action="{% url 'todolist:delete_task' id=task.id %}" method="post">
              {% csrf_token %}
              <button style="margin-left: 4px;" class="btn btn-danger" type="submit" ><i class="btn-danger"></i>Delete</button>
           </form>
          
          </div>
        </li>
      {% endfor %}
      </ul>
      
  </div>
  ...
  ```
  
  Potongan kode diatas akan mengiterasi tiap objek Task dan akan memasukkan _field-field_ nya ke dalam container dengan class _cards_, dimana class tersebut memungkinkan container untuk dimodifikasi sekreatif mungkin. Contoh salah satu modifikasi yang dapat dilakukan pada _cards_ untuk membuatnya menjadi responsive adalah dengan ```:hover```, yang membuat _card_ menjadi responsive ketika cursor user berada diatas elemen _card_ tersebut. Respon _card_ dapat berupa munculnya bayangan, berubahnya warna, dan lain-lain. Contoh pengimplementasian yang saya gunakan untuk membuat _card_ menjadi responsive adalah dengan mengganti warnanya ketika cursor berada pada _card_ dengan:
  
  ```
  .card:hover {
  color: var(--white);
  background: var(--blue);
}
```

Selain itu, masih banyak lagi modifikasi yang dapat dilakukan terhadap _cards_ tadi. Namun secara garis besar, tugas ini dapat diselesaikan dengan mengimplementasikan _cards_ sesuai contoh diatas dan menyesuaikan isinya dengan elemen-elemen yang ingin ditampilkan kepada user serta modifikasi-modifikasinya yang memanfaatkan class dan juga id dari sebuah elemen serta berbagai macam selector juga yang dapat diletakkan dalam file dengan ```<style>``` atau juga menggunakan file CSS eksternal seperti yang telah dijelaskan pada no. 1.

##### _Rayhan Putra Randi | 2106705644 | PBP-A_
