import requests
#------------------------------------- FUNÇÃO PEGAR POKEMON ---------------------------------------  
def pegar_pokemon(nome):
    url = f"https://pokeapi.co/api/v2/pokemon/{nome.lower()}"
    
    resposta = requests.get(url)

    if resposta.status_code == 200:
        
        return resposta.json()
    
#------------------------------------- FUNÇÃO TIPO POKEMON ---------------------------------------  
def tipo_pokemon(url_tipo):
    
    
    resposta = requests.get(url_tipo)
    if resposta.status_code == 200:
        return resposta.json()
#------------------------------------- FUNÇÃO RELAÇÃO DANO ---------------------------------------
def relacao_dano(url):
    
    resposta = requests.get(url)
    dados = resposta.json
    print("Danos:")
    for t in dados["damage_relations"]:
        print(f" - {t['double_damage_from']['name'].title()}")


    
#------------------------------------- FUNÇÃO JOGAR POKEMON ---------------------------------------  
def jogar_pokemon (pokemon):
    url1 = f"https://pokeapi.co/api/v2/pokemon/{pokemon.lower()}"
    resposta1 = requests.get(url1)


    if resposta1.status_code == 200:
        dados = resposta1.json()
        print(f"\nNome: {dados['name'].title()}")
        print("Habilidades:")
        contador = 0
        for h in dados["abilities"]:
            print(f" {contador}- {h['ability']['name'].title()}")
            contador += 1
        print("-"*50)
        habilidade_numero = int(input("\nSelecione a habilidade pelo numero: "))
        print("-"*50)
        print(dados['abilities'][habilidade_numero]['ability']['name'].title())
        print("-"*50)
        

#------------------------------------- FUNÇÃO BUSCAR POKEMON -------------------------------------             
def buscar_pokemon(nome):
    url = f"https://pokeapi.co/api/v2/pokemon/{nome.lower()}"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        print(f"\nNome: {dados['name'].title()}")
        print(f"ID: {dados['id']}")
        print("Tipos:")
        for t in dados["types"]:
            print(f" - {t['type']['name'].title()}")
        print("Habilidades:")
        for h in dados["abilities"]:
            print(f" - {h['ability']['name'].title()}")
    else:
        print("Pokémon não encontrado!")


#------------------------------------- FUNÇÃO BUSCAR HABILIDADE---------------------------------------             
def buscar_habilidade(nome):
    url = f"https://pokeapi.co/api/v2/pokemon/{nome.lower()}"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        print(f"\nNome: {dados['name'].title()}")
        print("Habilidades:")
        for h in dados["abilities"]:
            print(f" > {h['ability']['name'].title()}")
    
#------------------------------------- FUNÇÃO RELAÇÃO DANO ---------------------------------------



#------------------------------------- J O G O ------------------------------------------------------  
while True:
    #------------------ MENU INICIAL-----------------
    print("-"*50)
    menu = input("\nEscolha as opções: Buscar - Jogar - Sair :")
    print("-"*50)
    #------------------ OPÇÃO BUSCAR JOGO -----------------
    if menu == "Buscar":
        nome = input("\nDigite o nome do Pokémon :")
        buscar_pokemon(nome)
    #------------------ OPÇÃO SAIR JOGO -----------------
    elif menu == "Sair":
        input("\nEncerrando o jogo!")
        break
    #------------------ OPÇÃO JOGAR JOGO -----------------
    elif menu =="Jogar":
        #------------------ ESCOLHA DOS POKEMON -----------------
        primeiro = ""
        while len(primeiro) ==0 :
            primeiro = input("\nDigite o nome do primeiro Pokémon : ")          #INSERIR PRIMEIRO POKEMON
            print("-"*50)
            try:    #TENTAR ACHAR NOME POKEMON NO JPSON DA TABELA DE POKEMON                                                     
                nome_primeiro = pegar_pokemon(primeiro)#NOME POKEMON NO JPSON DA TABELA DE POKEMON
                for t in nome_primeiro["types"]:
                    print(f" - {t['type']['name'].title()}")#TIPO POKEMON
                    print("-"*50)                         
                tipo_pokemon1 = tipo_pokemon(nome_primeiro['types'][0]['type']['url']) #URL DO TIPO DE POKEMON
                
                #print("\n")
                #dano = tipo_pokemon1['damage_relations']
                #print(dano)
                #dobro = dano['double_damage_from']

                #print("\n")
                #print(dobro)

                #print("\n")
                #print("***")
                #d = relacao_dano(nome_primeiro)
                #print(d)
                
            except:
                primeiro = ""
                print("\nPrimeiro pokémon não encontrado!")
                print("-"*50)

            #print(relacao_dano)
                 
        segundo = ""
        while len(segundo)==0:  
            segundo = input("\nDigite o nome do segundo Pokémon : ")
            print("-"*50)
            try:
                nome_segundo = pegar_pokemon(segundo)
                for t in nome_segundo["types"]:
                    print(f" - {t['type']['name'].title()}")
                    print("-"*50) 
                tipo_pokemon2 = tipo_pokemon(nome_segundo['types'][0]['type']['url'])
            except:
                segundo = ""
                print("\nSegundo pokémon não encontrado!")
                print("-"*50)
              
        break

    else:
        print("\nEscolha uma das opções")

     #------------------  -----------------
print("\nHORA DE JOGAR!!!!")
print("-"*50)
jogar_pokemon(primeiro)
print("-"*50)
