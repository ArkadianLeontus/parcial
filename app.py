# Importa las librerías que se usaran
from flask import Flask, render_template
import pyodbc


app = Flask(__name__)

# Configura la conexión a la base de datos Access
db_connection = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                               r'DBQ=C:\Users\aldeb\OneDrive\Documentos\TallerDB.accdb;')

# Define Las rutas para la pagina de inicio, el listado de los estudiantes y el listado de los cursos
@app.route('/')
def inicio():
    return "Aplicacion TallerDB De José Alcázar"


@app.route('/estudiantes')
def listar_estudiantes():
    cursor = db_connection.cursor()
    cursor.execute('SELECT * FROM Estudiantes')
    estudiantes = cursor.fetchall()
    return render_template('estudiantes.html', estudiantes=estudiantes)


@app.route('/cursos')
def listar_cursos():
    cursor = db_connection.cursor()
    cursor.execute('SELECT * FROM cursos')
    cursos = cursor.fetchall()
    return render_template('cursos.html', cursos=cursos)

#Ejecuta
if __name__ == '__main__':
    app.run(debug=True) 


    
