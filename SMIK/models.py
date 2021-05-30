from django.db import models

class Gedung(models.Model):
    id = models.BigAutoField(primary_key=True)
    nama = models.CharField(max_length=50)

    class Meta:
        db_table = 'gedung'

    def __str__(self) :
        return self.nama


class Ruangan(models.Model):
    id = models.BigAutoField(primary_key=True)
    nama = models.CharField(max_length=50)
    id_gedung = models.ForeignKey('Gedung', on_delete=models.CASCADE, db_column='id_gedung', default='')

    class Meta:
        db_table = 'ruangan'

    def __str__(self) :
        return self.nama


class Barang(models.Model):
    id = models.BigAutoField(primary_key=True)
    kode = models.CharField(max_length=50)

    LIST_KATEGORI = (
        ('Elektronik','Elektronik'),
        ('Transportasi','Transportasi'),
        ('Furnitur','Furnitur'),
        ('Lain-lain','Lain-lain')
    )

    kategori = models.CharField(
        max_length=50,
        choices=LIST_KATEGORI,
        default= 'Elektronik',
    )
    nama = models.CharField(max_length=50)
    merek = models.CharField(max_length=50)
    stok = models.IntegerField()
    id_ruangan = models.ForeignKey('Ruangan', on_delete=models.CASCADE, db_column='id_ruangan', default='')

    class Meta:
        db_table = 'barang'

    def __str__(self) :
        return self.nama


class FormPinjam(models.Model):
    id = models.BigAutoField(primary_key=True)
    no_peminjaman = models.CharField(max_length=50)
    id_peminjam = models.ForeignKey('Peminjam', on_delete=models.CASCADE, db_column='id_peminjam')
    id_barang = models.ForeignKey('Barang', on_delete=models.CASCADE, db_column='id_barang', default='')
    tanggal_pinjam = models.DateTimeField()
    tanggal_kembali = models.DateTimeField()
    jumlah_pinjam = models.PositiveIntegerField()
    scan_form = models.CharField(max_length=50)

    class Meta:
        db_table = 'form_pinjam'

    def __str__(self) :
        return self.no_peminjaman


class Peminjam(models.Model):
    id = models.BigAutoField(primary_key=True)
    no_pengenal = models.PositiveBigIntegerField()
    nama = models.CharField(max_length=50)
    email = models.CharField(max_length=20)

    class Meta:
        db_table = 'peminjam'

    def __str__(self) :
        return self.nama



