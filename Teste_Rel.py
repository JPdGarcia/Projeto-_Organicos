import os
import requests
from json import loads
from datetime import datetime
from time import sleep

os.system("cls")

# Tela de abertura do prograna
tamanho_linha=73
title1="••• O R G Â N I C O ' S •••"
title2="Grupo 1 • Teste do Módulo de Relatórios"
title3="\033[93m"+"Anderson & Câmara"+"\033[m"

espaço1=(tamanho_linha-len(title1))//2-3
espaço2=(tamanho_linha-len(title2))//2-3
espaço3=(tamanho_linha-len(title3))//2+1
linha_vazia="|"+" "*(tamanho_linha-2)+"|"

print("-"*tamanho_linha)
print(linha_vazia)
print("|"," "*espaço1, title1," "*espaço1,"|")
print(linha_vazia)
print("|"," "*espaço2, title2," "*espaço2,"|")
print(linha_vazia)
print(linha_vazia)
print(linha_vazia)
print(linha_vazia)
print(linha_vazia)
print(linha_vazia)
print("|"," "*espaço3, title3," "*espaço3,"|")
print("-"*tamanho_linha)
sleep(8)

print ("\n\n••• AMBIENTE PARA REALIZAÇÃO DOS TESTES••• ")
sleep(0.8)
print("\n\tP ►  Produção")
print("\tD ►  Desenvolvimento")

ambiente=input("\n\tOpção desejada: ").lower().strip()

while True:
    if ambiente=="p":
        bd="receita"
        break
    elif ambiente=="d":
        bd="des_receita"
        break

flag_menu=True # liga / desliga os comando While  
while flag_menu:
    try:
        teste_resposta = requests.get('http://127.0.0.1:5000/')
        status_servidor="\033[93mServidor online\033[m"
    except requests.exceptions.ConnectionError:
        status_servidor="   \033[1;31mServidor fora do ar\033[m"

    resposta = requests.get(f"http://127.0.0.1:5000/banco_dados?bd={bd}")
    status_request = resposta.status_code
    conteúdo=resposta.content
    
    os.system("cls")
    data_hora=datetime.now() # Recebe a data e a hora atual

    title1="••• R E L A T Ó R I O S •••"
    title2=""
  
    qtd_caracter_data=len(data_hora.strftime("%d/%m/%Y"))
    qtd_caracter_hora=len(data_hora.strftime("%H:%M"))
    
    # Qtd de caracteres para calcular o posicionamento dos títulos, data e hora
    espaço1=(tamanho_linha-len(title1))//2-1
    espaço2=(tamanho_linha-len(title2))//2-1
    espaço3=tamanho_linha-(qtd_caracter_data+qtd_caracter_hora)

    print (F"{status_servidor} \t\t\t\t\t \033[93mBD:{bd:>13}\033[m")
    print(F"{'-'*tamanho_linha}\n{title1:^{tamanho_linha}}\n{title2:^{tamanho_linha}}\n{'-'*tamanho_linha}")
    print(data_hora.strftime("%d/%m/%Y")+" "*espaço3+data_hora.strftime("%H:%M"),"\n")
    
    print("\t\t1 ►  Registro de vendas realizadas")
    print("\t\t2 ►  Relatório de vendas por produto")
    print("\t\t3 ►  Total de vendas realizadas com quantidade e valor")
    print("\t\t4 ►  Ranking de produtos mais vendidos")
    print("\t\t5 ►  Limpar tabela de vendas")
    print("\t\t6 ►  Consulta de vendas")
   
    print("\n\t\tS ►  S A I R   D O   S I S T E M A")
 
    opção=input("\n\t\tOpção desejada: ").lower().strip()

    if opção=="1":
        os.system("cls")
        resposta = requests.get('http://127.0.0.1:5000/registro_de_vendas_realizadas')
        status_request = resposta.status_code
        conteúdo=resposta.content
        
        print(F"\033[93mStatus Request: {status_request}\033[m")
        print("-"*54)
        print("\t ••• REGISTRO DE VENDAS REALIZADAS •••")
        print("-"*54)
        
        if status_request != 200:
            print("\n\033[1;31mR E T O R N O   I N E S P E R A D O.  V E R I F I C A R\033[m")
            input("\n\n\033[;7m<ENTER>\033[0;0m para retornar ")
            continue
        
        conteúdo_lista=loads(conteúdo)
        tot_geral_vendido=conteúdo_lista
                        
        print(F"TOTAL GERAL  ►  \033[93mQuantidade: {tot_geral_vendido[0]['Qtd']}\033[m  •••  \033[93mVendas: R$ {tot_geral_vendido[0]['Soma']:.02f}\033[m")
        print("-"*54)
        input("\n\033[;7m<ENTER>\033[0;0m para retornar ")


    elif opção=="2":
        os.system("cls")
        resposta = requests.get('http://127.0.0.1:5000/relatório_de_vendas_por_produto')
        status_request = resposta.status_code
        conteúdo=resposta.content
        
        print(F"\033[93mStatus Request: {status_request}\033[m")
        print("-"*42)
        print(" ••• RELATÓRIO DE VENDAS POR PRODUTO •••")
        print("-"*42)
        print("Código\tProduto\t\t     Total Vendido")

        if status_request != 200:
            print("\n\033[1;31mR E T O R N O   I N E S P E R A D O.  V E R I F I C A R\033[m")
            input("\n\n\033[;7m<ENTER>\033[0;0m para retornar ")
            continue
        
        conteúdo_lista=loads(conteúdo)
        total_geral_vendido=0
        for item_lista in conteúdo_lista:  
            cod = item_lista["Cod_Prd"]
            nom = item_lista["Nome_Prd"]
            Som = item_lista["Soma"]
            
            total_geral_vendido += Som
                        
            print(F"{cod:>3}\t{nom:<23} R${Som:>7.02f}")        
        
        print("-"*42)    
        print("TOTAL GERAL DE VENDAS","\t", " "*6, F"R$ {total_geral_vendido:>6.02f}")
        input("\n\033[;7m<ENTER>\033[0;0m para retornar ")
                

    elif opção=="3": 
        os.system("cls")
        resposta = requests.get('http://127.0.0.1:5000/total_de_vendas_com_qtd_e_valor')
        status_request = resposta.status_code
        conteúdo=resposta.content
        
        print(F"\033[93mStatus Request: {status_request}\033[m")
        print("-"*58)
        print(" ••• TOTAL DE VENDAS REALIZADAS COM QUANTIDADE E VALOR •••")
        print("-"*58)
        print("Código\tProduto\t\t       Qtd Vendida   Total Vendido")

        if status_request != 200:
            print("\n\033[1;31mR E T O R N O   I N E S P E R A D O.  V E R I F I C A R\033[m")
            input("\n\n\033[;7m<ENTER>\033[0;0m para retornar ")
            continue        

        conteúdo_lista=loads(conteúdo)
        tot_geral_vendido=0
        qtd_geral_vendida=0
        for item_lista in conteúdo_lista:  
            cod = item_lista["Cod_Prd"]
            nom = item_lista["Nome_Prd"]
            qtd = item_lista["Qtd"]
            som = item_lista["Soma"]
            
            
            qtd_geral_vendida += qtd
            tot_geral_vendido += som
                        
            print(F" {cod:>3}\t{nom:<23}{qtd:>6} \t\tR${som:>7.02f}")        
        
        print("-"*58)    
        print(F"TOTAL GERAL QUANTIDADE / VENDAS    {qtd_geral_vendida:>1}\t\t R$ {tot_geral_vendido:>6.02f}")
        input("\n\033[;7m<ENTER>\033[0;0m para retornar ")


    elif opção=="4":
        os.system("cls")
        resposta = requests.get('http://127.0.0.1:5000/ranking_de_produtos_mais_vendidos')
        status_request = resposta.status_code
        conteúdo=resposta.content
        
        
        print(F"\033[93mStatus Request: {status_request}\033[m")
        print("-"*58)
        print(" "*5,"••• RANKING DOS \033[93m10 PRODUTOS\033[m MAIS VENDIDOS •••")
        print("-"*58)
        print("Código\tProduto\t\t       Qtd Vendida   Total Vendido")

        if status_request != 200:
            print("\n\033[1;31mR E T O R N O   I N E S P E R A D O.  V E R I F I C A R\033[m")
            input("\n\n\033[;7m<ENTER>\033[0;0m para retornar ")
            continue

        conteúdo_lista=loads(conteúdo)
        tot_geral_vendido=0
        qtd_geral_vendida=0
        for item_lista in conteúdo_lista:  
            cod = item_lista["Cod_Prd"]
            nom = item_lista["Nome_Prd"]
            Qtd = item_lista["Quantidade"]
            Som = item_lista["Soma"]
            
            tot_geral_vendido += Som
            qtd_geral_vendida += Qtd
            print(F" {cod:>3}\t{nom:<23}{Qtd:>6} \t\t R${Som:>7.02f}")        
        
        print("-"*58)    
        print(F"TOTAL GERAL QUANTIDADE / VENDAS    {qtd_geral_vendida:>1}\t\t R$ {tot_geral_vendido:>6.02f}")
        input("\n\033[;7m<ENTER>\033[0;0m para retornar ")
    
    
    elif opção=="5":
        os.system("cls")
        print("\t\t••• LIMPAR TABELA DE VENDAS •••")
        print("-"*60)
        print("\033[1;31m\t\t\tA T E N Ç Ã O\033[m\n")
        print("\t\033[93mTODAS AS INFORMAÇÕES DE VENDAS SERÃO APAGADAS\033[m")
        print("-"*60)

        print("\n\n\t\tS ►  Limpar tabela de vendas")
        print("\t\tV ►  Voltar ao menu principal")
                
        limpar_tabela=input("\n\t\tOpção desejada: ").lower().strip()
    
        if limpar_tabela=="s":
            resposta = requests.get("http://127.0.0.1:5000/limpar_tabela_de_vendas")
            status_request = resposta.status_code
            
            sleep(0.7)
            print(F"\n\n\n\033[93mStatus Request: {status_request}\033[m")
            sleep(0.7)

            if status_request == 500:
                print("\n\033[1;31mT A B E L A   D E   V E N D A S   N Ã O   E X I S T E\033[m\n\n") 
            elif status_request == 200:
                 print("\n\033[93mT A B E L A   D E   V E N D A S   A P A G A D A   C O M   S U C E S S O\033[m\n\n")
            else:
                print("\n\033[1;31mE R R O  I N E S P E R A D O\033[m") 
            
            sleep(1)
            input("\n\033[;7m<ENTER>\033[0;0m para retornar ")

    elif opção=="6": 
        while True:
            os.system("cls")
            print("\n","-"*58)
            print("\t    ••• CONSULTA DE VENDAS POR DATA •••\n")

            data_consulta=input("\033[93mData para geração do relatório (DD/MM/AAAA):\033[m ")
            try:
                datetime.strptime(data_consulta, '%d/%m/%Y')
                break
            except ValueError as e:
                print("\033[1;31mA data deve ser digitada no formato DD/MM/AAAA\033[m")
                input("\n\033[;7m<ENTER>\033[0;0m tentar novamente ")

        resposta = requests.get(f'http://127.0.0.1:5000/consulta_de_vendas?data={data_consulta}')
        status_request = resposta.status_code
        conteúdo=resposta.content
                
        os.system("cls")
        print(F"\033[93mStatus Request: {status_request}\033[m")
        print("-"*58)
        print("\t    ••• CONSULTA DE VENDAS POR DATA •••")
        print(F"\033[93m{data_consulta}\033[m")
        print("-"*58)
        print("Data Venda  Cód  Produto\t    Qtd Vend\tTotal Vend")
        
        if status_request != 200:
            print("\n\033[1;31mR E T O R N O   I N E S P E R A D O.  V E R I F I C A R\033[m")
            input("\n\n\033[;7m<ENTER>\033[0;0m para retornar ")
            continue
        
        conteúdo_lista=loads(conteúdo)
        tot_geral_vendido = 0
        qtd_geral_vendida = 0
        data_anterior = None
        for item_lista in conteúdo_lista:  
            Dat = item_lista["Dt_Venda_Prd"]
            Cod = item_lista["Cod_Prd"]
            Nom = item_lista["Nome_Prd"]
            Qtd = item_lista["Qtd_Prod"]
            Som = item_lista["Som_Valor"]
            
            Dat = datetime.strptime(Dat[5:16], '%d %b %Y').strftime('%d/%m/%Y')
            tot_geral_vendido += Som
            qtd_geral_vendida += Qtd
            
            if data_anterior == Dat:
                Dat = "    .     "
            else:    
                data_anterior = Dat

            print(F"{Dat:<10} {Cod:>4}\t {Nom:<23}{Qtd:>1}\t R${Som:>7.02f}")       
     
        print("-"*58)    
        print("TOTAL GERAL QUANTIDADE / VENDAS"," "*6,F"{qtd_geral_vendida:>1}\t R$ {tot_geral_vendido:>6.02f}")
        input("\n\033[;7m<ENTER>\033[0;0m para retornar ")
    
    elif opção=="s":
        flag_menu=False        

print("\nA P L I C A Ç Ã O   E N C E R R A D O\n")