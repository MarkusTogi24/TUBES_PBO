from django.db.models.aggregates import *
from django.forms.forms import Form
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render

from . import models
from . import forms

DataGedung      = models.Gedung.objects.all()
DataRuang       = models.Ruangan.objects.all()
DataBarang      = models.Barang.objects.all()
JumlahBarang    = models.Barang.objects.all().aggregate(Sum('stok')).get('stok__sum', 0)

class smikviews :

    def login(request) :
        return render(request,'login.html')

    def register(request) :
        return render(request,'register.html')

    def success_register(request) :
        return render(request,'success_register.html')

    def index(request) :
        DataGedung      = models.Gedung.objects.all()
        DataRuang       = models.Ruangan.objects.all()
        DataBarang      = models.Barang.objects.all()
        JumlahBarang    = models.Barang.objects.all().aggregate(Sum('stok')).get('stok__sum', 0)
        DataTampil = (
            models.Barang.objects.values('kode','nama','merek')
            .annotate(total_stok=Sum('stok')).order_by('kode')
        )

        Content = {
            "Judul"         : "Beranda",
            "DataGedung"    : DataGedung,
            "DataRuang"     : DataRuang,
            "DataBarang"    : DataBarang,
            "JumlahBarang"  : JumlahBarang,
            "DataTampil"    : DataTampil
        }
        return render(request,'index.html',Content)

    def user_index(request) :
        DataGedung      = models.Gedung.objects.all()
        DataRuang       = models.Ruangan.objects.all()
        DataBarang      = models.Barang.objects.all()
        JumlahBarang    = models.Barang.objects.all().aggregate(Sum('stok')).get('stok__sum', 0)

        Content = {
            "Judul"         : "Beranda",
            "DataGedung"    : DataGedung,
            "DataRuang"     : DataRuang,
            "DataBarang"    : DataBarang,
            "JumlahBarang"  : JumlahBarang
        }
        return render(request,'user_dashboard.html',Content)

    def TampilGedung(request) :
        DataGedung      = models.Gedung.objects.all()
        DataRuang       = models.Ruangan.objects.all()
        DataBarang      = models.Barang.objects.all()
        JumlahBarang    = models.Barang.objects.all().aggregate(Sum('stok')).get('stok__sum', 0)
        
        Content = {
            "Judul"         : "Gedung",
            "DataGedung"    : DataGedung,
            "DataRuang"     : DataRuang,
            "DataBarang"    : DataBarang,
            "JumlahBarang"  : JumlahBarang
        }
        return render(request,'01_Gedung/tampilgedung.html',Content)

    def UserTampilGedung(request) :
        DataGedung      = models.Gedung.objects.all()
        DataRuang       = models.Ruangan.objects.all()
        DataBarang      = models.Barang.objects.all()
        JumlahBarang    = models.Barang.objects.all().aggregate(Sum('stok')).get('stok__sum', 0)
        
        Content = {
            "Judul"         : "Gedung",
            "DataGedung"    : DataGedung,
            "DataRuang"     : DataRuang,
            "DataBarang"    : DataBarang,
            "JumlahBarang"  : JumlahBarang
        }
        return render(request,'01_Gedung/usertampilgedung.html',Content)

    def InputGedung(request) :
        formGedung = forms.GedungForms()

        if request.method == 'POST' :
            models.Gedung.objects.create(
                nama = request.POST['nama']
            )
            return HttpResponseRedirect("/tampilgedung")

        return render(request,'01_Gedung/inputgedung.html',{"form":formGedung})

    def TampilRuang(request) :
        DataGedung      = models.Gedung.objects.all()
        DataRuang       = models.Ruangan.objects.all()
        DataBarang      = models.Barang.objects.all()
        JumlahBarang    = models.Barang.objects.all().aggregate(Sum('stok')).get('stok__sum', 0)
        
        Content = {
            "Judul"         : "Ruangan",
            "DataGedung"    : DataGedung,
            "DataRuang"     : DataRuang,
            "DataBarang"    : DataBarang,
            "JumlahBarang"  : JumlahBarang
        }
        return render(request,'02_Ruangan/tampilruangan.html',Content)

    def UserTampilRuang(request) :
        DataGedung      = models.Gedung.objects.all()
        DataRuang       = models.Ruangan.objects.all()
        DataBarang      = models.Barang.objects.all()
        JumlahBarang    = models.Barang.objects.all().aggregate(Sum('stok')).get('stok__sum', 0)
        
        Content = {
            "Judul"         : "Ruangan",
            "DataGedung"    : DataGedung,
            "DataRuang"     : DataRuang,
            "DataBarang"    : DataBarang,
            "JumlahBarang"  : JumlahBarang
        }
        return render(request,'02_Ruangan/usertampilruangan.html',Content)

    def InputRuangan(request) :
        formRuang = forms.RuanganForms()

        if request.method == 'POST' :
            models.Ruangan.objects.create(
                nama        = request.POST['nama'],
                id_gedung   = models.Gedung.objects.get(id = request.POST['id_gedung'])
            )
            return HttpResponseRedirect("/tampilruang")

        return render(request,'02_Ruangan/inputruangan.html',{"form":formRuang})

    def TampilBarang(request) :
        DataGedung      = models.Gedung.objects.all()
        DataRuang       = models.Ruangan.objects.all()
        DataBarang      = models.Barang.objects.all()
        JumlahBarang    = models.Barang.objects.all().aggregate(Sum('stok')).get('stok__sum', 0)
        DataTampil = (
            models.Barang.objects.values('kode','nama','merek')
            .annotate(total_stok=Sum('stok')).order_by('kode')
        )

        Content = {
            "Judul"         : "Barang",
            "DataGedung"    : DataGedung,
            "DataRuang"     : DataRuang,
            "DataBarang"    : DataBarang,
            "JumlahBarang"  : JumlahBarang,
            "DataTampil"    : DataTampil
        }
        return render(request,'03_Barang/tampilbarang.html',Content)

    def DetailBarang(request) :
        DataGedung      = models.Gedung.objects.all()
        DataRuang       = models.Ruangan.objects.all()
        DataBarang      = models.Barang.objects.all()
        JumlahBarang    = models.Barang.objects.all().aggregate(Sum('stok')).get('stok__sum', 0)
        DataTampil = (
            models.Barang.objects.values('kode','nama','merek')
            .annotate(total_stok=Sum('stok')).order_by('kode')
        )

        Content = {
            "Judul"         : "Barang",
            "DataGedung"    : DataGedung,
            "DataRuang"     : DataRuang,
            "DataBarang"    : DataBarang,
            "JumlahBarang"  : JumlahBarang,
            "DataTampil"    : DataTampil
        }
        return render(request,'03_Barang/barang_ruangan.html',Content)

    def UserTampilBarang(request) :
        DataGedung      = models.Gedung.objects.all()
        DataRuang       = models.Ruangan.objects.all()
        DataBarang      = models.Barang.objects.all()
        JumlahBarang    = models.Barang.objects.all().aggregate(Sum('stok')).get('stok__sum', 0)
        DataTampil = (
            models.Barang.objects.values('kode','nama','merek')
            .annotate(total_stok=Sum('stok')).order_by('kode')
        )
        
        Content = {
            "Judul"         : "Barang",
            "DataGedung"    : DataGedung,
            "DataRuang"     : DataRuang,
            "DataBarang"    : DataBarang,
            "JumlahBarang"  : JumlahBarang,
            "DataTampil"    : DataTampil
        }
        return render(request,'03_Barang/usertampilbarang.html',Content)

    def UserDetailBarang(request) :
        DataGedung      = models.Gedung.objects.all()
        DataRuang       = models.Ruangan.objects.all()
        DataBarang      = models.Barang.objects.all()
        JumlahBarang    = models.Barang.objects.all().aggregate(Sum('stok')).get('stok__sum', 0)
        Content = {
            "Judul"         : "Barang",
            "DataGedung"    : DataGedung,
            "DataRuang"     : DataRuang,
            "DataBarang"    : DataBarang,
            "JumlahBarang"  : JumlahBarang
        }
        return render(request,'03_Barang/userdetailbarang.html',Content)

    def InputBarang(request) :
        formBarang = forms.BarangForms()

        if request.method == 'POST' :
            models.Barang.objects.create(
                kode        = request.POST['kode'],
                kategori    = request.POST['kategori'],
                nama        = request.POST['nama'],
                merek       = request.POST['merek'],
                stok        = request.POST['stok'],
                id_ruangan  = models.Ruangan.objects.get(id = request.POST['id_ruangan'])
            )
            return HttpResponseRedirect("/detailbarang")

        Content = {
            "Judul_Kartu" : "Tambah Data Barang",
            "form"        : formBarang
        }

        return render(request,'03_Barang/inputbarang.html',Content)
    
    def HapusBarang(request,DataHapus) :
        models.Barang.objects.filter(id=DataHapus).delete()
        return redirect("/detailbarang")

    def SuntingBarang(request,DataSunting) :
        SuntingData = models.Barang.objects.get(id=DataSunting)

        KondisiSekarang = {
            "kode"       : SuntingData.kode,
            "kategori"   : SuntingData.kategori,
            "nama"       : SuntingData.nama,
            "merek"      : SuntingData.merek,
            "stok"       : SuntingData.stok,
            "id_ruangan" : SuntingData.id_ruangan
        }

        FormSunting = forms.BarangForms(request.POST or None, initial=KondisiSekarang, instance=SuntingData)

        if request.method == 'POST' :
            if FormSunting.is_valid() :
                FormSunting.save()
                return HttpResponseRedirect("/detailbarang")

        Content = {
            "Judul_Kartu" : "Sunting Data Barang",
            "form"        : FormSunting
        }

        return render(request,'03_Barang/inputbarang.html',Content)

    def TampilPeminjam(request) :
        DataGedung      = models.Gedung.objects.all()
        DataRuang       = models.Ruangan.objects.all()
        DataBarang      = models.Barang.objects.all()
        DataPeminjam    = models.Peminjam.objects.all()
        DataPeminjaman  = models.FormPinjam.objects.all()
        JumlahBarang    = models.Barang.objects.all().aggregate(Sum('stok')).get('stok__sum', 0)
        
        Content = {
            "Judul"         : "Peminjam",
            "DataGedung"    : DataGedung,
            "DataRuang"     : DataRuang,
            "DataBarang"    : DataBarang,
            "JumlahBarang"  : JumlahBarang,
            "DataPeminjam"  : DataPeminjam,
            "DataPeminjaman": DataPeminjaman
        }
        return render(request,'04_Peminjam/tampilpeminjam.html',Content)

    def InputPeminjam(request,BarangID) :
        # BarangPinjam = models.Barang.objects.get(id=BarangID)
        formPeminjam = forms.PeminjamForms()

        if request.method == 'POST' :
            Peminjam = models.Peminjam.objects.create(
                no_pengenal = request.POST['no_pengenal'],
                nama        = request.POST['nama'],
                email       = request.POST['email']
            )
            PeminjamID = Peminjam.id

            global IDPeminjam
            def IDPeminjam():
                return PeminjamID

            global IDBarang
            def IDBarang() :
                return BarangID

            return HttpResponseRedirect("/peminjamanbaru")

        return render(request,'04_Peminjam/inputpeminjam.html',{"form":formPeminjam})

    def TampilPeminjaman(request) :
        DataGedung      = models.Gedung.objects.all()
        DataRuang       = models.Ruangan.objects.all()
        DataBarang      = models.Barang.objects.all()
        DataPeminjam    = models.Peminjam.objects.all()
        DataPeminjaman  = models.FormPinjam.objects.all()
        JumlahBarang    = models.Barang.objects.all().aggregate(Sum('stok')).get('stok__sum', 0)
        
        Content = {
            "Judul"         : "Peminjaman",
            "DataGedung"    : DataGedung,
            "DataRuang"     : DataRuang,
            "DataBarang"    : DataBarang,
            "JumlahBarang"  : JumlahBarang,
            
            "DataPeminjam"  : DataPeminjam,
            "DataPeminjaman": DataPeminjaman
        }
        return render(request,'05_Peminjaman/tampilpeminjaman.html',Content)

    def InputPeminjaman(request) :
        
        formPeminjaman = forms.FormPinjamForms()
        BarangDipinjam = models.Barang.objects.get(id=IDBarang())
        PeminjamBarang = models.Peminjam.objects.get(id=IDPeminjam())

        if request.method == 'POST' :
            Peminjaman = models.FormPinjam.objects.create(
                id_barang       = BarangDipinjam,
                id_peminjam     = PeminjamBarang,
                tanggal_pinjam  = request.POST['tanggal_pinjam'],
                tanggal_kembali = request.POST['tanggal_kembali'],
                jumlah_pinjam   = request.POST['jumlah_pinjam'],
                scan_form       = "LINK",
                no_peminjaman   = BarangDipinjam.kode +"_"+ request.POST['tanggal_pinjam']
            )

            global getIDpeminjaman
            def getIDpeminjaman() :
                return Peminjaman.id

            BarangDipinjam.stok -= int(request.POST['jumlah_pinjam'])
            BarangDipinjam.save()
            return HttpResponseRedirect("/peminjaman-berhasil")

        return render(request,'05_Peminjaman/inputpeminjaman.html',{"form":formPeminjaman})

    def UserTampilPeminjaman(request) :
        DataTampil = models.FormPinjam.objects.get(id=getIDpeminjaman())
        BarangDipinjam = DataTampil.id_barang
        Content = {
            "Judul"         : "Peminjaman Berhasil",
            "DataGedung"    : DataGedung,
            "DataRuang"     : DataRuang,
            "DataBarang"    : DataBarang,
            "JumlahBarang"  : JumlahBarang,

            "nomor"         : DataTampil.no_peminjaman,
            "nama"          : DataTampil.id_peminjam,
            "barang"        : BarangDipinjam.nama + " " + BarangDipinjam.merek,
            "jumlahpinjam"  : DataTampil.jumlah_pinjam,
            "tpinjam"       : DataTampil.tanggal_pinjam,
            "tkembali"      : DataTampil.tanggal_kembali,
        } 

        return render(request,'05_Peminjaman/infopeminjaman.html',Content)


        

    def Test(request) :

        Content = {
        }

        return render(request, 'testmysql.html', Content)
