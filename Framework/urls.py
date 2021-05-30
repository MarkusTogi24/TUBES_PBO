from django.conf.urls import url
from django.contrib import admin
from django.urls import path
# from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from SMIK import views

SV = views.smikviews

urlpatterns = [
    #login ke Django Admin { un=admin, pw=asdjkl123 }
    path('admin/',                          admin.site.urls                             ),

    #Buat akun dan berhasil buat akun, cuma tampilan tanpa fungsi
    path('register/',                       SV.register                                 ),
    path('sregister/',                      SV.success_register                         ),

    #halaman awal pengguna, admin dan login
    path('',                                SV.user_index                               ),
    path('login/',                          SV.login                                    ),
    path('home/',                           SV.index                                    ),
    path('guest-home/',                     SV.user_index                               ),
    
    # untuk menampilkan data ke halaman website bagian admin
    path('tampilgedung/',                   SV.TampilGedung                             ),
    path('tampilruang/',                    SV.TampilRuang                              ),
    path('tampilbarang/',                   SV.TampilBarang                             ),
    path('tampilpeminjam/',                 SV.TampilPeminjam                           ),
    path('tampilpeminjaman/',               SV.TampilPeminjaman                         ),
    
    # untuk operasi barang, khusus admin
    path('detailbarang/',                   SV.DetailBarang                             ),
    path('ubahbarang/<int:DataSunting>',    SV.SuntingBarang,   name='UbahBarang'       ),
    path('hapusbarang/<int:DataHapus>',     SV.HapusBarang,     name='HapusBarang'      ),

    # untuk menampilkan data ke halaman website bagian pengguna bukan admin
    path('infogedung/',                     SV.UserTampilGedung                         ),
    path('inforuang/',                      SV.UserTampilRuang                          ),
    path('infobarang/',                     SV.UserTampilBarang                         ),
    path('rincianbarang/',                  SV.UserDetailBarang                         ),
    path('peminjaman-berhasil/',            SV.UserTampilPeminjaman                     ),

    #untuk keperluan input data khusus admin
    path('gedungbaru/',                     SV.InputGedung                              ),
    path('ruanganbaru/',                    SV.InputRuangan                             ),
    path('barangbaru/',                     SV.InputBarang                              ),

    #untuk keperluan input data oleh pengguna
    path('peminjambaru/<int:BarangID>',     SV.InputPeminjam,   name='DataPeminjamBaru' ),
    path('peminjamanbaru/',                 SV.InputPeminjaman                          ),

    # untuk keperluan testing :)
    path('test/',                           SV.Test                                     ),

]
urlpatterns += staticfiles_urlpatterns()
