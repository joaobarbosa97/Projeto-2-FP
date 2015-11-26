from functools import reduce

def cria_coordenada(l, c):
    
    if isinstance(l, int) and isinstance(c, int) and l > 0 and c > 0:
        return {'linha' : l, 'coluna' : c}
    
    raise ValueError('cria_coordenada: argumentos invalidos')

def coordenada_linha(c):
    
    if e_coordenada(c):
        return int(c['linha'])
    
    raise ValueError('coordenada_linha: argumento invalido')

def coordenada_coluna(c):
    
    if e_coordenada(c):
        return int(c['coluna'])
    
    raise ValueError('coordenada_coluna: argumento invalido')

def e_coordenada(u):
    
    return isinstance(u, dict) and len(u) == 2 and 'linha' in u\
    and 'coluna' in u and isinstance(u['linha'], int)\
    and isinstance(u['coluna'], int) and u['linha'] > 0 and u['coluna'] > 0

def coordenadas_iguais(c, q):
    
    if e_coordenada(c) and e_coordenada(q):
        return coordenada_linha(c) == coordenada_linha(q)\
        and coordenada_coluna(c) == coordenada_coluna(q)

    raise ValueError('coordenadas_iguais: argumentos invalidos')

def coordenada_para_cadeia(c):
    
    if e_coordenada(c):
        print('"(' + str(coordenada_linha(c)) + ' : ' + str(coordenada_coluna(c)) + ')"', end = '')
    else:
        raise ValueError('coordenada_para_cadeia: argumento invalido')

#----------------------------------------------------------------------------#
#                                                                            #
#                             TAD - TABULEIRO                                #
#                                                                            #
#----------------------------------------------------------------------------#

#auxiliar que verifica
def tuplo_valido(t):

    if len(t[0]) == len(t[1]):    
        for i in t[0]:
            if reduce(lambda x, y: x + y, i) + len(i) - 1 > len(t[1]):
                return False
        return True
    else:
        return False

#auxiliar que verifica se o tuplo respeita as caracteristicas necessarias
def tuplo_de_tuplos(t):
    
    if isinstance(t, tuple) and len(t) >= 1:
        for t_contido in t:
            if isinstance(t_contido, tuple) and len(t_contido) > 0:
                for val in t_contido:
                    if not isinstance(val, int):
                        return False
            else:
                return False
    else:
        return False
    
    return True

def cria_tabuleiro(t):
    
    # verificacoes dos inputs
    if isinstance(t, tuple) and len(t) == 2 and tuplo_de_tuplos(t[0])\
    and tuplo_de_tuplos(t[1]) and tuplo_valido(t):    
        
        #Criacao do dicionario que representa o tabuleiro,
        #com os valores das especificacoes ja colocados
        res = {'esp-linha': t[0], 'esp-coluna': t[1], 'celulas': []}
        
        #Preenchimento das celulas i* linhas
        for i in range(len(t[0])):
            res['celulas'] += [[0] * len(t[1])]
                    
        return res
            
    raise ValueError('cria_tabuleiro: argumento invalido')                
                
def tabuleiro_dimensoes(t):
    
    if e_tabuleiro(t):
        return (len(t['esp-linha']), len(t['esp-coluna']))

    raise ValueError('tabuleiro_dimensoes: argumento invalido')

def tabuleiro_especificacoes(t):
    
    if e_tabuleiro(t):
        return (t['esp-linha'], t['esp-coluna'])

    raise ValueError('tabuleiro_especificacoes: argumento invalido')

def tabuleiro_celula(t, c):
    
    if e_tabuleiro(t) and e_coordenada(c):
        return t['celulas'][coordenada_linha(c) - 1][coordenada_coluna(c) - 1]

    raise ValueError('tabuleiro_celula: argumentos invalidos')

def tabuleiro_preenche_celula(t, c, v):
    
    if e_tabuleiro(t) and e_coordenada(c) and isinstance(v, int) and 0 <= v <= 2:
        t['celulas'][coordenada_linha(c) - 1][coordenada_coluna(c) - 1] = v
        return t
    
    raise ValueError('tabuleiro_preenche_celula: argumentos invalidos')

def e_tabuleiro(t):

    return isinstance(t, dict) and len(t) == 3\
    and 'esp-linha' in t and 'esp-coluna' in t and 'celulas' in t\
    and tuplo_de_tuplos(t['esp-linha']) and tuplo_de_tuplos(t['esp-coluna'])\
    and tuplo_valido((t['esp-linha'], t['esp-coluna']))\
    and celulas_validas(t['celulas'])

def escreve_tabuleiro(t):
    
    if e_tabuleiro(t):
        
        # dimensao
        dim = tabuleiro_dimensoes(t)[0]
        esp = tabuleiro_especificacoes(t)
        
        # especificacoes linha e coluna
        esp_ls = esp[0]
        esp_cs = esp[1]
        
        # dimensao maxima de uma especificacao de uma linha e de uma coluna
        max_esp_l = max_esp(esp_ls)
        max_esp_c = max_esp(esp_cs)
        
        # lista que contem os caracteres a apresentar
        char = ['?', '.', 'x']
        
      
        for i in range(max_esp_c):
            l = ''
            ct = 0
            for i_ in range(len(esp_cs)):
                
                if len(esp_cs[i_]) >= max_esp_c - i:
                    l +='     '*(i_-ct-1)+ '  ' +str(esp_cs[i_][-(max_esp_c - i)]) + '  '
                    ct = i_
            print(l)   
       
        
        for i in range(dim):
            l = ''
            for i_ in range(dim):
                # valor da celula correspondente
                c = tabuleiro_celula(t, cria_coordenada(i + 1, i_ + 1))
                # imprime-se o caracter correspondente
                l += '[ ' + char[c] + ' ]'
                
            # especificacoes da linha
            esp_l = esp_ls[i]
            
            # le-se o tuplo das especificacoes da linha
            for i_ in range(len(esp_l)):
                l += ' ' + str(esp_l[i_])
            
            # colocam-se as '|' no final, reservando um espaco previo
            l += '  ' * (max_esp_l - len(esp_l)) + '|'

            print(l)
        
    else:
        raise ValueError('escreve_tabuleiro: argumento invalido')


#----------------------------AUXILIARES-------------------------------#
def cria_especificacao(t):
    
    if e_tabuleiro(t):
            
        res = ()
        
        ac = 0
            
        for i in range(len(t['celulas'])):
            
            res = res[:i] + ((ac,),) + res[(i+1):] 
                                    
            ac = 0            
            
            res = res + ((),)
            
            for y in range(len(t['celulas'][i])):
                
                if t['celulas'][i][y] == 2:
                    
                    ac = ac + 1
                    
                if ac != 0 and t['celulas'][i][y] != 2:
                    
                    res = res[:i] + ((ac,),) + res[(i+1):] 
                        
                    ac = 0
                        
            for x in range(len(res)):
                
                if res[x] == ():
                    
                    res = res[:x] + ((0,),) + res[(x+1):]                    
    return res

# auxiliar que nos da a dimensao maxima de uma especificacao para uma linha/coluna
def max_esp(v):
    m = 1
    
    for i in v:
        if len(i) > m:
            m = len(i)
    
    return m

# auxiliar que verifica se as celulas dadas sao validas
def celulas_validas(c):
    
    if isinstance(c, list):
        # n. linhas
        dim = len(c)
        
        for i in c:
            if isinstance(i, list):
                if len(i) == dim:
                    for i_ in i:
                        if not(isinstance(i_, int) and 0 <= i_ <= 2):
                            return False
                else:
                    return False
            else:
                return False
    else:
        return False
    
    return True

                    
#-----------------------------------------------------------------------------#
#                                                                             #
#                               TAD-JOGADA                                    #
#                                                                             #
#-----------------------------------------------------------------------------#

def cria_jogada(c, n):
    
    if isinstance(n, int) and 1 <= n <= 2 and e_coordenada(c):        
        return {'coordenada': c , 'valor': n }
    
    raise ValueError('cria_jogada: argumentos invalidos')

def jogada_coordenada(j):
    
    return j['coordenada']

def jogada_valor(j):
    
    return j['valor']

def e_jogada(u):
    
    return isinstance(u,dict) and len(u) == 2 and 'valor' in u and\
           'coordenada' in u and isinstance(u['valor'],int) and\
           1 <= u['valor'] <= 2 and e_coordenada(u['coordenada'])

def jogadas_iguais(j1,j2):
    
    return jogada_valor(j1) == jogada_valor(j2) and coordenadas_iguais(jogada_coordenada(j1),jogada_coordenada(j2))

def jogada_para_cadeia(j):
    
    coordenada_para_cadeia(jogada_coordenada(j))
    print('--> ' + str(jogada_valor(j)))
    return



t = cria_tabuleiro((((3,),(5,),(3,1),(2,1),(3,3,4),(2,2,7),(6,1,1),(4,2,2),(1,1),(3,1),(6,),(2,7),(6,3,1),(1,2,2,1,1),(4,1,1,3),(4,2,2),(3,3,1),(3,3),(3,),(2,1)),((2,),(1,2),(2,3),(2,3),(3,1,1),(2,1,1),(1,1,1,2,2),(1,1,3,1,3),(2,6,4),(3,3,9,1),(5,3,2),(3,1,2,2),(2,1,7),(3,3,2),(2,4),(2,1,2),(2,2,1),(2,2), (1,),(1,))))
