from django import forms
from django.db.models.base import Model
from django.forms import fields, widgets
from django.utils.regex_helper import Choice
from . import models
# formRuang = forms.RuanganForms(request.POST)
            # if formRuang.is_valid() :
            #     formRuang.save()
            #     return HttpResponseRedirect("/home/tampilruang")

            # else : 
            #     print("Tydack valid mamang")
class GedungForms(forms.ModelForm) :
    class Meta :
        model = models.Gedung
        fields = "__all__"
        widgets = {
            'nama' : forms.TextInput(
                attrs = {
                    'class' : 'form-control form-control-user',
                    'placeholder' : 'Nama gedung'
                }
            )
        }

class RuanganForms(forms.ModelForm) :
    class Meta :
        model = models.Ruangan
        fields = "__all__"
        widgets = {
            'nama' : forms.TextInput(
                attrs= {
                    'class' : 'form-control form-control-user',
                    'placeholder' : 'Nama ruangan'
                }
            ),
            'id_gedung' : forms.Select(
                attrs= {
                    'class' : 'form-control form-control-user',
                }
            )
        }

class BarangForms(forms.ModelForm) :
    class Meta :
        model = models.Barang
        fields = "__all__"
        widgets = {
            'kode' : forms.TextInput(
                attrs = {
                    'class' : 'form-control form-control-user',
                    'placeholder' : 'Kode barang'
                }
            ),
            'kategori' : forms.Select(
                attrs = {
                    'class' : 'form-control form-control-user',
                }
            ),
            'nama' : forms.TextInput(
                attrs = {
                    'class' : 'form-control form-control-user',
                    'placeholder' : 'Nama barang'
                }
            ),
            'merek' : forms.TextInput(
                attrs = {
                    'class' : 'form-control form-control-user',
                    'placeholder' : 'Merek barang'
                }
            ),
            'stok' : forms.TextInput(
                attrs = {
                    'class' : 'form-control form-control-user',
                    'placeholder' : 'Jumlah stok'
                }
            ),
            'id_ruangan' : forms.Select(
                attrs = {
                    'class' : 'form-control form-control-user',
                }
            )
        }

class FormPinjamForms(forms.ModelForm):
    
    class Meta:
        model = models.FormPinjam
        exclude = (
            "no_peminjaman",
            "id_barang",
            "id_peminjam",
            "scan_form"
        )
        Labels = {
            'tanggal_pinjam' : "Tanggal Peminjaman",
            'tanggal_kembali' : "Tanggal Kembali",
            'jumlah_pinjam' : "Jumlah dipinjam"
        }
        
        widgets = {
            'tanggal_pinjam' : forms.DateInput(
                attrs = {
                    'class' : 'form-control form-control-user',
                    'type'  : 'date',
                    'placeholder' : 'Tanggal Pinjam'
                }
            ),
            'tanggal_kembali' : forms.DateInput(
                attrs = {
                    'class' : 'form-control form-control-user',
                    'type'  : 'date'
                }
            ),
            'jumlah_pinjam' : forms.TextInput(
                attrs = {
                    'class'         : 'form-control form-control-user',
                    'placeholder'   : 'Jumlah ingin dipinjam'
                }
            )
        }

class PeminjamForms(forms.ModelForm):
    
    class Meta:
        model = models.Peminjam
        fields = "__all__"
        widgets = {
            'no_pengenal' : forms.TextInput(
                attrs= {
                    'class' : 'form-control form-control-user',
                    'placeholder' : 'NIK / NIP / NRK / NIM'
                }
            ),
            'nama' : forms.TextInput(
                attrs= {
                    'class' : 'form-control form-control-user',
                    'placeholder' : 'Nama lengkap'
                }
            ),
            'email' : forms.EmailInput(
                attrs= {
                    'class' : 'form-control form-control-user',
                    'placeholder' : 'Alamat email'
                }
            )
        }
