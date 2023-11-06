from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
import pymysql.cursors, os

application = Flask(__name__, template_folder='templates')

conn = cursor = None

@application.route('/')
def index():
    with openDb() as cursor:
        cursor.execute('SELECT * FROM buku_1122102059')
        results = cursor.fetchall()
        container = results

    return render_template('index_1122102059.html', container=container)

@application.route('/tambah', methods=['GET', 'POST'])
def tambah():
    if request.method == 'POST':
        Kode_Buku = int(request.form['Kode_Buku'])
        Nama_Buku = request.form['Nama_Buku']
        Penerbit = request.form['Penerbit']
        Pengarang = request.form['Pengarang']
        Jumlah_Buku = int(request.form['Jumlah_Buku'])  # Corrected data type

        with openDb() as cursor:
            cursor.execute("INSERT INTO buku_1122102059 (Kode_Buku, Nama_Buku, Penerbit, Pengarang, Jumlah_Buku) VALUES (%s, %s, %s, %s, %s)",
                           (Kode_Buku, Nama_Buku, Penerbit, Pengarang, Jumlah_Buku))
            conn.commit()

        return redirect(url_for('index'))

    return render_template('tambah_1122102059.html')

@application.route('/edit/<Kode_Buku>', methods=['GET', 'POST'])
def edit(Kode_Buku):
    with openDb() as cursor:
        cursor.execute(f"SELECT * FROM buku_1122102059 WHERE Kode_Buku={Kode_Buku}")
        data = cursor.fetchone()

    if request.method == 'POST':
        New_Kode_Buku = int(request.form['Kode_Buku'])
        Nama_Buku = request.form['Nama_Buku']
        Penerbit = request.form['Penerbit']
        Pengarang = request.form['Pengarang']
        Jumlah_Buku = request.form['Jumlah_Buku']

        with openDb() as cursor:
            cursor.execute("UPDATE buku_1122102059 SET Kode_Buku=%s, Nama_Buku=%s, Penerbit=%s, Pengarang=%s, Jumlah_Buku=%s WHERE Kode_Buku=%s",
                           (New_Kode_Buku, Nama_Buku, Penerbit, Pengarang, Jumlah_Buku, Kode_Buku))
            conn.commit()
        return redirect(url_for('index'))

    return render_template('edit_1122102059.html', data=data)


@application.route('/hapus/<Kode_Buku>', methods=['GET'])
def hapus(Kode_Buku):
    with openDb() as cursor:
        cursor.execute(f"DELETE FROM buku_1122102059 WHERE Kode_Buku={Kode_Buku}")
        conn.commit()

    return redirect(url_for('index'))

def openDb():
    global conn, cursor
    conn = pymysql.connect(host="localhost",user="root",passwd="",database="perpus_1122102059")
    cursor = conn.cursor()
    return cursor

if __name__ == '__main__':
    application.run(debug=True)
