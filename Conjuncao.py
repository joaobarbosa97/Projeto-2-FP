def cria_coordenada(n,m):
    
    if isinstance(n,int) and isinstance(m,int) and n >= 0 and m >= 0:

        return {'linha' : n, 'coluna' : m}
    
    raise ValueError('cria_coordenadas: argumentos invalidos')




def coordenada_linha(c):
    
    if e_coordenada(c):
        
        return int(c['linha'])
    
    raise ValueError('coordenada_coluna: argumento invalido')




def coordenada_coluna(c):
    
    if e_coordenada(c):
        
        return int(c['coluna'])
    
    raise ValueError('coordenada_coluna: argumento invalido')




def e_coordenada(u):
    
    return isinstance(u,dict) and len(u) == 2 and 'linha' in u and 'coluna' in u\
       and isinstance(u['linha'],int) and isinstance(u['coluna'],int)\
       and u['linha'] >= 0 and u['coluna'] >= 0

def coordenadas_iguais(c,q):
    
    if e_coordenada(c) and e_coordenada(q):
        
        return coordenada_linha(c) == coordenada_linha(q)\
        and coordenada_coluna(c) == coordenada_coluna(q)

    raise ValueError('coordenadas_iguais: argumentos invalidos')

def coordenada_para_cadeia(c):
    
    if e_coordenada(c):
        
        print('(' + str(coordenada_linha(c)) + ' : ' + str(coordenada_coluna(c)) + ')' )
        return
    
    raise ValueError('coordenada_para_cadeia: argumento invalido')


#----------------------------------------------------------------------------#
#                                                                            #
#                             TAD - TABULEIRO                                #
#                                                                            #
#----------------------------------------------------------------------------#


def cria_tabuleiro(t):
    
    if isinstance(t,tuple) and len(t) == 2 and isinstance(t[0],tuple)\
       and isinstance(t[1],tuple):
                
        res = {'esp-linha': t[0], 'esp-coluna': t[1],\
                        'celulas': [[0]*len(t[1])]}
                
        for i in range(len(t[0]) -1):
                    
            res['celulas'] += [[0]*len(t[1])]
                    
        return res
                
            
    raise ValueError('cria_tabuleiro: argumento invalido')
                
                
def tabuleiro_dimensoes(t):
    
    if e_tabuleiro(t):
        
        return (len(t['esp-linha']),len(t['esp-coluna']))

    raise ValueError('tabuleiro_dimensoes: argumento invalido')

def tabuleiro_especificacoes(t):
    
    if e_tabuleiro(t):
    
        return (t['esp-linha'],t['esp-coluna'])

    raise ValueError('tabuleiro_especificacoes: argumento invalido')

def tabuleiro_celula(t,c):
    
    if e_tabuleiro(t) and e_coordenada(c):
        
        return t['celulas'][coordenada_linha(c) -1][coordenada_coluna(c) -1]

    raise ValueError('tabuleiro_celula: argumento invalido')

def tabuleiro_preenche_celula(t,c,v):
    
    if e_tabuleiro(t) and e_coordenada(c) and isinstance(v,int) and 0 <= v <= 2:
               
        t['celulas'][coordenada_linha(c) -1][coordenada_coluna(c) -1] = v
        return t
    
    raise ValueError('tabuleiro_preenche_celula: argumento invalido')

def e_tabuleiro(t):
    
    if isinstance(t,dict) and len(t) == 3 and 'esp-linha' in t and\
       'esp-coluna' in t and 'celulas' in t and isinstance(t['esp-linha'],tuple) and\
       isinstance(t['esp-coluna'],tuple) and isinstance(t['celulas'],list)\
       and len(t['celulas']) == len(t['esp-linha']) and e_especificacao(t['esp-linha']) and\
       e_especificacao(t['esp-coluna']):
    
        for i in range(len(t['celulas'])):
                                                                
            if not isinstance(t['celulas'][i],list):
                                                                    
                return False
                                
            for n in range(len(t['celulas'][i])):
            
                if not isinstance(t['celulas'][i][n],int) and 0 <= t['celulas'][i][n] <= 2:
                
                    return False 
                                    
            for i in range(len(t['celulas'])):
                                                                                                    
                if not len(t['celulas'][i]) == len(t['esp-coluna']):
                                        
                    return False
                                            
        return True
                        
    return False
                            
                                       
                           
#----------------------------AUXILIARES-------------------------------#


def e_especificacao(t):
    
    for i in range(len(t)):
                
        if not isinstance(t[i],tuple):
                    
            return False
                
        for n in range(len(t[i])):
                    
            if not isinstance(t[i][n],int):
             
                return False   
            
    return True



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
                    
e = (((2,), (3,), (2,), (2, 2), (2,)), ((2,), (1, 2), (2,), (3,), (3,)))
t = cria_tabuleiro(e)
                
t2 = {'esp-coluna': ((2,), (1, 2), (2,), (3,), (3,)), 'esp-linha': ((2,), (3,), (2,), (2, 2), (2,)), 'celulas': [[1, 2, 2, 1, 1], [1, 1, 2, 2, 2], [1, 1, 1, 2, 2], [2, 0, 0, 2, 2], [2, 2, 1, 1, 1]]}

cria_especificacao(t2)