# Generated by Django 4.1.1 on 2022-09-14 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerService',
            fields=[
                ('id_cs', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('nama_cs', models.CharField(max_length=50)),
                ('nomer_telepon_cs', models.IntegerField()),
                ('alamat_cs', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Kelas_Mata_Kursus',
            fields=[
                ('Id_Kelas_Mata_Kursus', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('Jenis_Kursus', models.CharField(max_length=30)),
                ('Jenis_Kelas', models.CharField(max_length=30)),
                ('Jumlah_Pertemuan', models.IntegerField()),
                ('Jadwal', models.DateField()),
                ('Harga', models.IntegerField()),
                ('Status_Kelas', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='siswa',
            fields=[
                ('id_Siswa', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('Nama_Siswa', models.CharField(max_length=50)),
                ('Tanggal_Lahir', models.DateField()),
                ('Alamat_Siswa', models.CharField(max_length=50)),
                ('Nomor_Telepon_Siswa', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Transaksi',
            fields=[
                ('Id_Transaksi', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('Tanggal_Transaksi', models.DateField()),
                ('Id_CS', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.customerservice')),
                ('Id_Siswa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.siswa')),
            ],
        ),
        migrations.CreateModel(
            name='Registrasi',
            fields=[
                ('Id_Registrasi', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('id_Kelas_Mata_Kursus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.kelas_mata_kursus')),
                ('id_Transaksi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.transaksi')),
            ],
        ),
    ]