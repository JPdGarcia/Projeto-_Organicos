from flask import Flask
from flask import render_template
from flask import url_for, redirect
from flask import request
import pandas as pd
import sqlite3 as sql


#criar banco de dados
conexao = sql.connect('inventory.db')
cursor = conexao.cursor()


drop_table = '''
DROP TABLE if EXISTS estoque;
'''
#criar tabela
create_table_estoque = '''
CREATE TABLE estoque(
   produto    TEXT NOT NULL PRIMARY KEY
  ,preco     MONEY NOT NULL
  ,quantidade INT  NOT NULL
);'''

insert_valors_estoque = '''
INSERT INTO estoque(produto,preco,quantidade) VALUES
 ('maça',4,42)
,('pera',3,22)
,('melancia',8,30)
,('queijo',25,60)
,('melao',8,38)
,('manga',8,50)
,('leite',10,70)
,('ovos',10,60)
,('Abacaxi',6,30)
,('agua',2,43)
,('farofa',10,40)
,('goiba',6,50)
,('pitanga',5,45);
'''

select_produto = '''
SELECT preco FROM estoque WHERE produto=? 
'''
select_quantidade = '''
SELECT quantidade FROM estoque WHERE produto=?
'''

nova_quantiade = '''
UPDATE estoque SET quantidade = :resultado WHERE produto= :item
'''

cursor.execute(drop_table)
cursor.execute(create_table_estoque)
cursor.execute(insert_valors_estoque)

conexao.commit()
conexao.close()

app = Flask(__name__)

carrinho = pd.DataFrame(data={
        'produto': [],
        'preco': [],
        'quantidade': []
    }).set_index('produto')

@app.route('/')
def index():
    return redirect(url_for('static', filename='Landing_page.html'))


@app.route('/adicionarCarrinho')
def adicionarCarrinho():
    conexao = sql.connect('inventory.db')
    cursor = conexao.cursor()

    argumentos = request.args.to_dict()
    prod = argumentos['produto']
    quantidade = argumentos['quantidade']
    cursor.execute(select_produto, [prod])
    price = cursor.fetchone()[0]
    print(price)
    carrinho.loc[prod] = [float(price),int(quantidade)]
    print(carrinho)
    conexao.close()
    return redirect('static/Carrinho.html')

@app.route('/fecharVenda')
def fecharVenda():
    conexao = sql.connect('inventory.db')
    cursor = conexao.cursor()

    global carrinho
    for item in carrinho.index:
        cursor.execute(select_quantidade, [item])
        quantidade_estoque = cursor.fetchone()[0]
        print(quantidade_estoque)
        resultado = quantidade_estoque-int(carrinho.loc[item,'quantidade']) 
        print(int(carrinho.loc[item,'quantidade']))
        print(resultado)
        cursor.execute(nova_quantiade, {'resultado':resultado,'item':item})
    carrinho['total'] = carrinho['quantidade']*carrinho['preco']
    
    print(carrinho)
    print('__________________________')
    print(carrinho['total'])
    print(carrinho['total'].sum())
    print('________________________')
    df_html = carrinho.to_html()
    carrinho = pd.DataFrame(data={
            'produto': [],
            'preco': [],
            'quantidade': []
        }).set_index('produto')
    print(carrinho),
    conexao.commit()
    conexao.close()
    return render_template('fecharvenda.html', table = df_html)


@app.route('/removerCarrinho')
def removerCarrinho():
    global carrinho

    argumentos = request.args.to_dict()
    produto = argumentos['produto']

    carrinho.drop(index=produto, inplace=True)
    print(carrinho)

    return redirect('/static/removerCarrinho.html')



if __name__=='__main__':
    app.run(debug=True)