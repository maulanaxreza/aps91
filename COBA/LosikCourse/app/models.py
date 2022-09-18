from tokenize import blank_re
from django.db import models

# Create your models here.
class siswa(models.Model):
    id_Siswa = models.CharField(max_length=7, primary_key=True)
    Nama_Siswa = models.CharField(max_length=50)
    Tanggal_Lahir = models.DateField() 
    Alamat_Siswa = models.TextField(blank=True, null=True)
    Nomor_Telepon_Siswa = models.PositiveIntegerField()

    def __str__ (self):
        return str(self.Nama_Siswa)

class CustomerService(models.Model):
    id_cs = models.CharField(max_length=7, primary_key=True)
    nama_cs = models.CharField(max_length=50)
    nomer_telepon_cs = models.PositiveIntegerField()
    Alamat_Cs = models.TextField()

    def __str__(self):
        return str(self.nama_cs)

class Transaksi(models.Model):
    Id_Transaksi = models.CharField(max_length=7, primary_key=True)
    Id_Siswa = models.ForeignKey(siswa, on_delete=models.CASCADE)
    Id_CS = models.ForeignKey(CustomerService, on_delete=models.CASCADE)
    Tanggal_Transaksi = models.DateField()

    def __str__(self):
        return str(self.Id_Siswa)

class Kelas_Mata_Kursus(models.Model):
    JENISKURSUS = {
        ('Full-stack Web Developer', 'Full-stack Web Developer'),
        ('UI/UX Design and Product Management', 'UI/UX Design and Product Management'),
        ('Graphic and Motion Designer', 'Graphic and Motion Designer'),
        ('Digital Marketing', 'Digital Marketing')
    }
    JENISKELAS = {
        ('PROCLASS', 'PROCLASS'),
        ('MINICLASS', 'MINICLASS'),
    }
    STATUS = {
        ('dimulai', 'Dimulai'),
        ('belum dimulai', 'Belum Dimulai')
     }
    HARI = {
        ('Senin', 'Senin'),
        ('Selasa', 'Selasa'),
        ('Rabu','Rabu'),
        ('Kamis','Kamis'),
        ('Jumat', 'Jumat'),
        ('Sabtu','Sabtu'),
        ('Minggu','Minggu')
    }
    WAKTU = {
        ('10:00', '10:00'),
        ('13:00', '13:00'),
        ('15:00', '15:00'),
        ('19:30', '19:30')
    }
    Id_Kelas_Mata_Kursus = models.CharField(max_length=7, primary_key=True)
    Jenis_Kursus = models.TextField(choices=JENISKURSUS, max_length=50)
    Jenis_Kelas = models.TextField(choices=JENISKELAS, max_length=50)
    Jumlah_Pertemuan = models.PositiveIntegerField()
    Jadwal = models.TextField(choices=HARI, max_length=50)
    Harga = models.FloatField()
    Status_Kelas = models.TextField(choices=STATUS, max_length=30)

    def __str__(self):
        return str(self.Jenis_Kursus)

class Registrasi(models.Model):
    Id_Registrasi = models.CharField(max_length=7, primary_key=True)
    id_Transaksi = models.ForeignKey(Transaksi, on_delete=models.CASCADE)
    id_Kelas_Mata_Kursus = models.ForeignKey(Kelas_Mata_Kursus, on_delete=models.CASCADE)

    def __str__(self):
        return(self.Id_Transaksi)
    