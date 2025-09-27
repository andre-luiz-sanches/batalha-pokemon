import requests
import random
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
#------------------------------------- FUNÇÃO PEGAR POKEMON ---------------------------------------  
def pegar_pokemon(nome):
    url = f"https://pokeapi.co/api/v2/pokemon/{nome.lower()}"
    
    resposta = requests.get(url)

    if resposta.status_code == 200:
        
        return resposta.json()
    
#------------------------------------- FUNÇÃO SALVAR POKEMON -------------------------------------
def salvar_pokemon(pokemon):

    #------------------ CODIGO PARA SALVAR NOME DO POKEMON -----------------
    nome_pokemon = []
    for nome2_pokemon in pokemon['forms']:
        nome_pokemon.append(nome2_pokemon['name'])

    
    #------------------ CODIGO PARA LISTAR O CHAVE TYPES DO POKEMON -----------------
    lista1_tipo_pokemon1 = []
    for lista2_tipo_pokemon1 in pokemon['types']:
        lista1_tipo_pokemon1.append(lista2_tipo_pokemon1['type'])
    print("-"*50)    
    #------------------ CODIGO PARA LISTAR O NOME DO TIPOS DO POKEMON -----------------
    nome1_lista_pokemon1 = []
    for nome2_lista_pokemon1 in lista1_tipo_pokemon1:
        nome1_lista_pokemon1.append(nome2_lista_pokemon1['name'])
    print("-"*50)    
    #print("tipo de pokemon :",nome1_lista_pokemon1)
    #---------------------------- CODIGO PARA LISTAR URL DO TIPO DE POKEMON E ACESSAR URL --------------------
    lista1_url_tipo_pokemon1 = []
    for lista2_url_tipo_pokemon1 in lista1_tipo_pokemon1:
        lista1_url_tipo_pokemon1.append(requests.get(lista2_url_tipo_pokemon1['url']).json())            
    #---------------------------- CODIGO PARA LISTAR REGRA DE DANO --------------------
    #---------------------------- LISTA ZERADA - PARA SALVAR INFORMAÇÕES --------------------
    dobro_dano_de = []
    dobro_dano_em = []
    metade_dano_de = []
    metade_dano_em = []
    sem_dano_de = []
    sem_dano_em = []
    for t in lista1_url_tipo_pokemon1:
        
        dobro_dano_de.extend(t['damage_relations']['double_damage_from']),
        dobro_dano_em.extend(t['damage_relations']['double_damage_to']),
        metade_dano_de.extend(t['damage_relations']['half_damage_from']),
        metade_dano_em.extend(t['damage_relations']['half_damage_to']),
        sem_dano_de.extend(t['damage_relations']['no_damage_from']),
        sem_dano_em.extend(t['damage_relations']['no_damage_to']),
        
    #-----------------------------
    listadobro_dano_de = []
    for nome_dobro_dano_de in dobro_dano_de:
        listadobro_dano_de.append(nome_dobro_dano_de['name'])
    listadobro_dano_em = []
    for nome_dobro_dano_em in dobro_dano_em:
            listadobro_dano_em.append(nome_dobro_dano_em['name'])
    listametade_dano_de = []
    for nome_metade_dano_de in metade_dano_de:
        listametade_dano_de.append(nome_metade_dano_de['name'])
    listametade_dano_em = []
    for nome_metade_dano_em in metade_dano_em:
        listametade_dano_em.append(nome_metade_dano_em['name'])
    listasem_dano_de = []
    for nome_sem_dano_de in sem_dano_de:
        listasem_dano_de.append(nome_sem_dano_de['name'])
    listasem_dano_em = []
    for nome_sem_dano_em in sem_dano_em:
        listasem_dano_em.append(nome_sem_dano_em['name'])
        
     #----------------------------- TANSFORMAR O POKEMON EM DICIONARIO ---------------
    relacao = {
        'dobro_de': listadobro_dano_de,
        'dobro_em': listadobro_dano_em,
        'metade_de': listametade_dano_de,
        'metade_em': listametade_dano_em,
        'sem_de':listasem_dano_de,
        'sem_em':listasem_dano_em,
        'hp':100
        }
    
    print("-"*50)
    #print("dobro dano de: " , listadobro_dano_de)
    #print("dobro dano em: " , listadobro_dano_em)
    #print("metade dano de: " , listametade_dano_de)
    #print("metade dano em: " , listametade_dano_em)
    #print("sem dano de: " , listasem_dano_de)
    #print("sem dano em: " , listasem_dano_em)

    relacao['tipos'] = nome1_lista_pokemon1
    relacao['name'] =nome_pokemon
    print("-"*50)
    #print('teste',relacao)
    return relacao  
    
#------------------------------------- FUNÇÃO REGRA DE DANO ----------------------------------------  
   
def regra_dano (atacante,defensor):
    multiplicador = 1.0
    for tipo_defesa in defensor['tipos']:
        # E vai comparar com as relações de dano do PRIMEIRO Pokémon (o atacante)
            if tipo_defesa in atacante['dobro_em']:
                multiplicador *= 2.0
            elif tipo_defesa in atacante['metade_em']:
                multiplicador *= 0.5
            elif tipo_defesa in atacante['sem_em']:
                multiplicador *= 0.0
               
           #print(f"O multiplicador de dano final é de {multiplicador}x.")    
    return multiplicador
    
#------------------------------------- FUNÇÃO JOGAR POKEMON ---------------------------------------  
def jogar_pokemon (pokemon):
    #print("pokemon jodado",pokemon)
    nome_pokemon = pokemon['name']
    url1 = f"https://pokeapi.co/api/v2/pokemon/{ nome_pokemon[0].lower()}"
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
        try:
            print(dados['abilities'][habilidade_numero]['ability']['name'].title())
            print("-"*50)
        except:
            print("Opção invalida")
        




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
    
#------------------------------------- FUNÇÃO JOGAR--------------------------------------- 
def jogar(vida_primeiro,vida_segundo,primeiro,segundo):
    turno =1
    while vida_primeiro > 0 and vida_segundo > 0:
        print("\nturno numeoro",turno)
#definindo o turno
        if turno % 2 !=0:
            atacante = primeiro
            defensor = segundo
            vida_defensor = vida_segundo
           #print("ataque",atacante)
            #print("defesa",defensor)
        else:
            atacante = segundo
            defensor = primeiro
            vida_defensor = vida_primeiro
            #print(atacante)
            #print(defensor)
#mostrando as habilidades
        jogar_pokemon(atacante)
#definindo dano
        dano = random.randint(1, 10)
        #print(dano)
#multiplicar dano
        multiplicador = regra_dano (atacante,defensor)
        dano_sofrido = dano*multiplicador
        print("\ndando causado foi de:" ,dano_sofrido)
        if turno %2!=0:
            vida_segundo -= dano_sofrido
            print("\nvida atual:",vida_segundo)
            vida_segundo = max(0,vida_segundo)
        else:
            vida_primeiro -= dano_sofrido
            print("\nvida atual:",vida_primeiro)
            vida_primeiro = max(0,vida_primeiro)
        turno+=1
    if vida_primeiro <= 0:
        print("\nO Segundo Pokémon venceu!")
    elif vida_segundo <= 0:
        print("\nO Primeiro Pokémon venceu!")









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
        primeiro = "" #Alakazam
        while len(primeiro) ==0 :
            print("-"*50)
            primeiro = input("\nDigite o nome do primeiro Pokémon : ")          #INSERIR PRIMEIRO POKEMON
            print("-"*50)
            
            try:#PARA NÃO COLOCAR NOME INCORRETO
                nome_primeiro = pegar_pokemon(primeiro)#NOME POKEMON NO JPSON DA TABELA DE POKEMON
                primeiro_pokemon = salvar_pokemon(nome_primeiro)#FUNÇÃO PARA SALVAR INFORMAÇÕES DO POKEMON
                break
            except:
                primeiro = ""
                print("\nPrimeiro pokémon não encontrado!")
                print("-"*50)
                
        segundo = "" #Alakazam
        while len(segundo) ==0 :
            print("-"*50)
            segundo = input("\nDigite o nome do segundo Pokémon : ")          #INSERIR SEGUNDO POKEMON
            print("-"*50)
            
            try:#PARA NÃO COLOCAR NOME INCORRETO
                nome_segundo = pegar_pokemon(segundo)#NOME POKEMON NO JPSON DA TABELA DE POKEMON
                segundo_pokemon = salvar_pokemon(nome_segundo)
                break
            except:
                segundo = ""
                print("\nSegundo pokémon não encontrado!")
                print("-"*50)
                
         #------------------FIM -----------------  
         
        hp_primeiro = primeiro_pokemon['hp']
        hp_segundo = segundo_pokemon['hp']
        
        print("-"*50)
        print('\nvida do ', primeiro, hp_primeiro)
        print('\nvida do ', segundo, hp_segundo) 
        print("-"*50)
        
        #print("\nRELAÇÃO DE DANOS!!!!")
        #print("-"*50)
        #print(primeiro)
        #regra_dano(primeiro_pokemon,segundo_pokemon)
        #print("-"*50)
        #print(segundo)
        #regra_dano(segundo_pokemon,primeiro_pokemon)

#--------------------------------------------------------------------------




        print("-"*50)
        print("\nHORA DE JOGAR!!!!")
        print("-"*50)
        jogar(hp_primeiro,hp_segundo,primeiro_pokemon,segundo_pokemon)


        break
    else:
        print("\nEscolha uma das opções")

     #------------------  -----------------

