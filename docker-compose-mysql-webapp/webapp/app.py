from flask import Flask , jsonify ,render_template
import mysql.connector

app = Flask(__name__)

def connection_to_mysql():
    mysql = { 'host':'mysql-service', 'user': 'admin' , 'password':'admin','database': 'employees','port':'3306'}
    return mysql



@app.route('/hello_world')
def hello_world():
    return "hello world"


@app.route('/' ,methods=['GET'])
def employees():
    try: 
        connection_function = connection_to_mysql()
        
        connection = mysql.connector.connect(**connection_function)
        con = connection.cursor()
        con.execute("SELECT * FROM employees")
        show_rows = con.fetchall()
        con.close()
        employees_list  =   [{"id": row[0], "name": row[1], "role": row[2]} for row in show_rows]

        return render_template('index.html', employees=employees_list)
    except Exception as e: 
        return jsonify({"error":str(e)}), 500
    

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')





