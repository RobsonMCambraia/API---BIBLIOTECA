from flask import Flask, jsonify, request
import pandas as pd

# cria uma instância da classe Flask e a associa ao nome do seu script ou módulo
app = Flask(__name__)

df_func = pd.read_excel("scr/BaseFuncionarios.xlsx")
dict_func = df_func.to_dict(orient='records')

@app.route('/funcionarios', methods=['GET'])
def getFuncionarios():
    return jsonify(dict_func)

@app.route('/funcionarios/<int:id>', methods=['GET'])
def getFunc_por_id(id):
    for funcionario in dict_func: 
        if funcionario.get('ID RH') == id:
            return jsonify(funcionario)

@app.route('/funcionarios/<int:id>', methods=['PUT'])
def putAdd_func(id):
    func_alt = request.get_json()
    for indice, funcionario in enumerate(dict_func):
        if funcionario.get('ID RH') == id:
            dict_func[indice].update(func_alt)
            return jsonify(dict_func[indice])

@app.route('/funcionarios', methods=['POST'])
def postFunc():
    novo_func = request.get_json()
    dict_func.append(novo_func)
    return jsonify(dict_func) 

app.run(port=5000, host='localhost', debug=True)