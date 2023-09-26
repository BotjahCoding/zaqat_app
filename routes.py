from flask import Flask, render_template

app = Flask(__name__)


@app.route("/coba")
def coba():
    return render_template('index.html')


@app.route("/")
def homepage_user():
    # halaman data penerima zakat keseluruhan
    return render_template('homepage_user.html')


@app.route("/login")
def login():
    return render_template('login.html')


@app.route("/register")
def register():
    return render_template('register.html')


@app.route("/mainpage_user1")  # halaman data penerima zakat gampong
def mainpage_user1():
    return render_template('mainpage_user1.html')


@app.route("/profile_user1")
def profile_user1():
    return render_template('profile_user1.html')  # halaman profil


@app.route("/add_data1")
def add_data1():
    # halaman tambah penerima zakat gampong
    return render_template('add_data1.html')


@app.route("/add_data_fakir")
def add_data_fakir():
    # halaman lanjutan tambah data penerima zakat gampong
    return render_template('add_data_fakir.html')


@app.route("/add_data_miskin")
def add_data_miskin():
    # halaman lanjutan tambah data penerima zakat gampong
    return render_template('add_data_miskin.html')


@app.route("/add_data_miskin_insidentil")
def add_data_miskin_insidentil():
    # halaman lanjutan tambah data penerima zakat gampong
    return render_template('add_data_miskin_insidentil.html')


@app.route("/add_data_guru_dayah")
def add_data_guru_dayah():
    # halaman lanjutan tambah data penerima zakat gampong
    return render_template('add_data_guru_dayah.html')


@app.route("/add_data_santri_dayah")
def add_data_santri_dayah():
    # halaman lanjutan tambah data penerima zakat gampong
    return render_template('add_data_santri_dayah.html')


@app.route("/add_data_santri_dayah_luar")
def add_data_santri_dayah_luar():
    # halaman lanjutan tambah data penerima zakat gampong
    return render_template('add_data_santri_dayah_luar.html')


@app.route("/add_data_anak_yatim")
def add_data_anak_yatim():
    # halaman lanjutan tambah data penerima zakat gampong
    return render_template('add_data_anak_yatim.html')


@app.route("/add_data_disabilitas")
def add_data_disabilitas():
    # halaman lanjutan tambah data penerima zakat gampong
    return render_template('add_data_disabilitas.html')


@app.route("/add_data_lanjut_belajar")
def add_data_lanjut_belajar():
    # halaman lanjutan tambah data penerima zakat gampong
    return render_template('add_data_lanjut_belajar.html')


@app.route("/add_data_pelajar_muallaf")
def add_data_pelajar_muallaf():
    # halaman lanjutan tambah data penerima zakat gampong
    return render_template('add_data_pelajar_muallaf.html')


@app.route("/add_data_muallaf")
def add_data_muallaf():
    # halaman lanjutan tambah data penerima zakat gampong
    return render_template('add_data_muallaf.html')


@app.route("/add_data_gharimin")
def add_data_gharimin():
    # halaman lanjutan tambah data penerima zakat gampong
    return render_template('add_data_gharimin.html')


@app.route("/add_data_santri_berprestasi")
def add_data_santri_berprestasi():
    # halaman lanjutan tambah data penerima zakat gampong
    return render_template('add_data_santri_berprestasi.html')


@app.route("/add_data_madrasah")
def add_data_madrasah():
    # halaman lanjutan tambah data penerima zakat gampong
    return render_template('add_data_madrasah.html')


@app.route("/add_data_waqaf")
def add_data_waqaf():
    # halaman lanjutan tambah data penerima zakat gampong
    return render_template('add_data_waqaf.html')


@app.route("/add_data_pelajar_rantau")
def add_data_pelajar_rantau():
    # halaman lanjutan tambah data penerima zakat gampong
    return render_template('add_data_pelajar_rantau.html')


@app.route("/add_data_ibnu_sabil")
def add_data_ibnu_sabil():
    # halaman lanjutan tambah data penerima zakat gampong
    return render_template('add_data_ibnu_sabil.html')


@app.route("/mainpage_user2")
def mainpage_user2():
    return render_template('mainpage_user2.html')


@app.route("/resultpage_user2")
def resultpage_user2():
    return render_template('resultpage_user2.html')


@app.route("/data_gampong_user2")
def data_gampong_user2():
    return render_template('data_gampong_user2.html')


@app.route("/profile_user2")
def profile_user2():
    return render_template('profile_user2.html')


@app.route("/mainpage_admin")
def mainpage_admin():
    return render_template('mainpage_admin.html')


@app.route("/register_staf")
def register_staf():
    return render_template('register_staf.html')


@app.route("/data_gampong_admin")
def data_gampong_admin():
    return render_template('data_gampong_admin.html')


@app.route("/data_staf_admin")
def data_staf_admin():
    return render_template('data_staf_admin.html')


if __name__ == '__main__':
    app.run(port=8181, host="0.0.0.0", debug=True)
