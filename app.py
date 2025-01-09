from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Konfigurasi database MySQL
db_config = {
    'host': 'localhost',
    'user': 'root',  # Ganti dengan username MySQL Anda
    'password': '',  # Ganti dengan password MySQL Anda
    'database': 'flask_crud'
}

# Fungsi koneksi database
def get_db_connection():
    conn = mysql.connector.connect(**db_config)
    return conn

# Route untuk halaman utama
@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM mahasiswa')
    mahasiswa = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', mahasiswa=mahasiswa)

# Route untuk menambahkan data
@app.route('/tambah', methods=('GET', 'POST'))
def tambah():
    if request.method == 'POST':
        nim = request.form['nim']
        nama = request.form['nama']
        asal = request.form['asal']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO mahasiswa (nim, nama, asal) VALUES (%s, %s, %s)', 
                       (nim, nama, asal))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('index'))

    return render_template('form.html')

# Route untuk mengubah data
@app.route('/ubah/<int:id>', methods=('GET', 'POST'))
def ubah(id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM mahasiswa WHERE id = %s', (id,))
    mahasiswa = cursor.fetchone()

    if request.method == 'POST':
        nim = request.form['nim']
        nama = request.form['nama']
        asal = request.form['asal']

        cursor.execute('UPDATE mahasiswa SET nim = %s, nama = %s, asal = %s WHERE id = %s',
                       (nim, nama, asal, id))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('index'))

    cursor.close()
    conn.close()
    return render_template('form.html', mahasiswa=mahasiswa)

# Route untuk menghapus data
@app.route('/hapus/<int:id>', methods=('POST',))
def hapus(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM mahasiswa WHERE id = %s', (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
