import mysql.connector
from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

nome_bd="receita" # banco padrão
@app.route("/banco_dados")
def banco_dados():
    global nome_bd
    nome_bd = request.args.get('bd')
    return(nome_bd)

@app.route("/registro_de_vendas_realizadas")
def registro_de_vendas_realizadas():
    
    conex = mysql.connector.connect(host="127.0.0.1",
            user="root", password="12345678", database=nome_bd)
    cursor = conex.cursor(dictionary=True)
    cursor.execute('''
    
    Select  COUNT(Nome_Prd)     AS Qtd,  
            SUM(Vlr_Unit_Prd)   AS Soma 
            FROM vendas
    ''')
    resultado = cursor.fetchall()
    conex.close()
    return jsonify(resultado)


@app.route("/relatório_de_vendas_por_produto")
def relatório_de_vendas_por_produto():

    conex = mysql.connector.connect(host="127.0.0.1",
            user="root", password="12345678", database=nome_bd)
    cursor = conex.cursor(dictionary=True)
    cursor.execute('''
    
    Select  Cod_Prd, 
            Nome_Prd, 
            SUM(Vlr_Unit_Prd) AS Soma 
            FROM vendas GROUP BY Nome_Prd
    ''')
    resultado = cursor.fetchall()
    conex.close()
    return jsonify(resultado)


@app.route("/total_de_vendas_com_qtd_e_valor")
def total_de_vendas_com_qtd_e_valor():

    conex = mysql.connector.connect(host="127.0.0.1",
        user="root", password="12345678", database=nome_bd)
    cursor = conex.cursor(dictionary=True)
    cursor.execute('''
    
    Select  Cod_Prd, 
            Nome_Prd, 
            COUNT(Nome_Prd)     As Qtd, 
            SUM(Vlr_Unit_Prd)   AS Soma 
            FROM vendas 
            GROUP BY Nome_Prd 
    ''')
    resultado = cursor.fetchall()
    conex.close()
    return jsonify(resultado)


@app.route("/ranking_de_produtos_mais_vendidos")
def ranking_de_produtos_mais_vendidos():
    conex = mysql.connector.connect(host="127.0.0.1",
            user="root", password="12345678", database=nome_bd)
    
    cursor = conex.cursor(dictionary=True)
    cursor.execute('''
    Select  Cod_Prd, 
            Nome_Prd, 
            COUNT(Nome_Prd)     AS Quantidade, 
            SUM(Vlr_Unit_Prd)   AS Soma 
            FROM vendas 
            GROUP BY Nome_Prd
            ORDER BY Quantidade DESC, Soma DESC
            LIMIT 10    
    ''')
    resultado = cursor.fetchall()
    conex.close()
    return jsonify(resultado)


@app.route("/limpar_tabela_de_vendas")
def limpar_tabela_de_vendas():
    conex = mysql.connector.connect(host="127.0.0.1",
            user="root", password="12345678", database=nome_bd)
    cursor = conex.cursor(dictionary=True)
    cursor.execute("DROP TABLE vendas")
    conex.close()
    return " "

    
@app.route('/consulta_de_vendas')
def consulta_de_vendas():
    data_recebida = request.args.get('data')
    data_recebida = datetime.strptime(data_recebida, '%d/%m/%Y').strftime('%Y-%m-%d')
    
    conex = mysql.connector.connect(host="127.0.0.1",
            user="root", password="12345678", database=nome_bd)
    cursor = conex.cursor(dictionary=True)
   
    cursor.execute(f'''
    Select  Cod_Prd, 
            Nome_Prd, 
            COUNT(Nome_Prd)     AS Qtd_Prod,
            SUM(Vlr_Unit_Prd)   AS Som_Valor,
            Dt_Venda_Prd
            FROM vendas
            WHERE Dt_Venda_Prd <= '{data_recebida}'
            GROUP BY Dt_Venda_Prd, Nome_Prd
            ORDER BY Dt_Venda_Prd DESC, Som_Valor DESC
    ''')
    resultado = cursor.fetchall()
    conex.close()
    return jsonify(resultado)


if __name__ == '__main__':
    app.run(debug=True)
