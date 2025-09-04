def contoh_conditions():
    print("\n=== Conditions ===")
    age = 20
    if age < 13:
        print("Anak-anak")
    elif age < 18:
        print("Remaja")
    else:
        print("Dewasa") 

def contoh_looping():
    print("\n=== Looping ===")
    for i in range(5):
        print(f"Perulangan ke-{i}")

    count = 0
    while count < 3:
        print("Hitungan:", count)
        count += 1


def contoh_arithmetic():
    print("\n=== Arithmetic ===")
    a = 10
    b = 3
    print("Penjumlahan:", a + b)
    print("Pengurangan:", a - b)
    print("Perkalian:", a * b)
    print("Pembagian:", a / b)
    print("Modulus:", a % b)
    print("Pangkat:", a ** b)


def contoh_database():
    print("\n=== Database Connection ===")
    try:
        import mysql.connector
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="test_db"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        for row in cursor.fetchall():
            print(row)
        cursor.close()
        conn.close()
    except Exception as e:
        print("Database error:", e)
        print("Pastikan mysql-connector-python terinstal dan DB tersedia.")

def contoh_flask_api():
    from flask import Flask, request, jsonify
    app = Flask(__name__)

    @app.route('/hello', methods=['GET'])
    def hello_world():
        return jsonify({"message": "Hello, World!"})

    @app.route('/add', methods=['POST'])
    def add_numbers():
        data = request.get_json()
        a = data.get("a", 0)
        b = data.get("b", 0)
        return jsonify({"result": a + b})

    print("\n=== Flask API Running ===")
    app.run(debug=True)

if __name__ == "__main__":
    contoh_conditions()
    contoh_looping()
    contoh_arithmetic()
    contoh_database()

    # Jalankan API Flask di akhir
    # Buka http://127.0.0.1:5000/hello di browser
    contoh_flask_api()
