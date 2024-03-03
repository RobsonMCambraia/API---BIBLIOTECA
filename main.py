from flask import Flask, jsonify, request
import pandas as pd

# cria uma instância da classe Flask e a associa ao nome do seu script ou módulo
app = Flask(__name__)

df_func = pd.read_excel("scr/BaseFuncionarios.xlsx")
dict_func = df_func.to_dict(orient='records')

@app.route('/funcionarios', methods=['GET'])
def get_funcionarios():
    return jsonify(dict_func)

@app.route('funcionarios/<int:id>', methods=['POST'])
def get_func_por_id(id):
    for funcionario in dict_func: 
        if funcionario.get('ID RH') == id:
            return jsonify(funcionario)

app.run(port=5000, host='localhost', debug=True)