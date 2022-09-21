# README

### Link Aplikasi Heroku
##### [HTML](https://pbp-assignments-mywatchlist.herokuapp.com/mywatchlist/html/)
##### [XML](https://pbp-assignments-mywatchlist.herokuapp.com/mywatchlist/xml/)
##### [JSON](https://pbp-assignments-mywatchlist.herokuapp.com/mywatchlist/json/)


## HTML, XML, dan JSON

**HTML** atau _Hyper Text Markup Language_ merupakan sebuah _markup language_ yang dapat digunakan untuk membuat suatu aplikasi web. Pada **HTML**, kita dapat menampilkan 

## Mengapa _data delivery_ dibutuhkan dalam pengimplementasian sebuah platform?



## Pengimplementasian aplikasi

Sebelum memulai, dinyalakan terlebih dahulu _virtual environment_ pada direktori project yang akan dikerjakan dan juga install requirements yang dibutuhkan project. Setelah itu, karena ```models.py``` sudah disediakan, dilakukan juga _migration_ untuk memuat model ke database Django lokal. Lalu, load juga data barang yang ada pada ```initial_catalog_data.json``` ke database Django lokal. Barulah diisi file-file yang rumpang.

### ```views.py```

File ini saya isi dengan fungsi ```show_catalog``` yang menerima parameter request dan mengembalikan fungsi render yang berfungsi untuk menampilkan html berisi data yang telah diambil pada fungsi dan disimpan di variabel ```data_barang_catalog```.

```
...
def show_catalog(request):
    data_barang_catalog = CatalogItem.objects.all()
    context = {
        'list_barang': data_barang_catalog,
        'nama': 'Rayhan Putra Randi',
        'id': '2106705644'
    }
    return render(request, "katalog.html", context)
```

### ```urls.py``` (Routing)

Untuk routing, pada file ```project_django\urls.py``` ditambahkan sebuah elemen pada variabel ```urlpatterns``` agar program dapat mengambil data yang sesuai dengan request client sebagai berikut:
```
...
urlpatterns = [
    path('katalog/', include('katalog.urls')),
    path('admin/', admin.site.urls),
    path('', include('example_app.urls')),
]
```
Sementara itu, pada file ```katalog\urls.py```, ditambahkan sebuah elemen pada variabel ```urlpatterns``` juga yang berfungsi untuk memanggil fungsi ```show_catalog``` untuk menampilkan data yang telah dikumpulkan dan disimpan pada variabel di dalam fungsi tersebut seperti berikut:
```
...
urlpatterns = [
    path('', show_catalog, name='show_catalog')
]
```

### ```katalog.html``` (Template)

Pada file ini, ditambahkan sebuah loop dalam _table_ yang mengiterasi variabel ```list_barang```, dimana variabel tersebut menyimpan data-data yang ingin ditampilkan pada web. Data barang ditampilkan dengan cara memanggil attribut-attribut dari barang yang telah ditentukan pada file ```models.py``` untuk setiap barang yang diiterasi seperti berikut:
```
...
{% for item in list_barang %}
    <tr>
        <th>{{item.item_name}}</th>
        <th>{{item.item_price}}</th>
        <th>{{item.item_stock}}</th>
        <th>{{item.rating}}</th>
        <th>{{item.description}}</th>
        <th>{{item.item_url}}</th>
    </tr>
...
```

### _Deployment_

Proses ini sama seperti pada tutorial, yaitu melakukan ```git add```, ```git commit```, lalu ```git push``` untuk men- _deploy_ project ke repository github. Pada github, atur juga API key dan nama aplikasi yang ingin di deploy agar aplikasi bisa dibuka di web browser melalui Heroku.
 
##### _Rayhan Putra Randi | 2106705644 | PBP-A_

###### _sources_:
https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Home_page

https://www.javatpoint.com/django-virtual-environment-setup#:~:text=The%20virtual%20environment%20is%20an,create%20an%20isolated%20Python%20environment
