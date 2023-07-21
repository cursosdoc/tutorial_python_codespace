import flask
import csv

app = flask.Flask(__name__)


def cargar_filas_base_datos():
    filas_csv = []
    with open("frutas.csv", "r") as frutas:
        reader = csv.reader(frutas)
        filas_csv = [fila for fila in reader]
    encabezados = filas_csv.pop(0)
    return encabezados, filas_csv


def filtar_lista(lista, columna_indice, valor_a_filtar):
    lista_filtrada = []
    for fila in lista:
        if fila[columna_indice] == valor_a_filtar:
            lista_filtrada.append(fila)
    return lista_filtrada


@app.route("/hola_mundo")
def hola_mundo():
    return "<h1>Hola mundo</h1>"


@app.route("/contar_frutas/<color>")
def contar_frutas(color):
    parametros = flask.request.args
    porte_esperado = parametros["porte"]

    if porte_esperado not in ["grande", "mediana", "chica"]:
        return "Porte no valido", 400

    encabezados, filas_csv = cargar_filas_base_datos()

    lista_filtrada = filtar_lista(filas_csv, 1, color)
    lista_filtrada = filtar_lista(lista_filtrada, 2, porte_esperado)

    return f"Total {len(filas_csv)}, color {color} y porte {porte_esperado} = {len(lista_filtrada)}"


@app.route("/agregar_fruta", methods=["POST"])
def agregar_fruta():
    cuerpo = flask.request.json
    valores = [valor for valor in cuerpo.values()]
    linea_csv = "\n" + ",".join(valores)
    with open("frutas.csv", "a") as frutas:
        frutas.write(linea_csv)
    return "Fruta registrada con exito"


@app.route("/reporte_frutas")
def reporte_frutas():
    encabezados, filas_csv = cargar_filas_base_datos()
    html = flask.render_template(
        "plantilla_reporte_frutas.html", encabezados=encabezados, filas=filas_csv
    )
    return html
