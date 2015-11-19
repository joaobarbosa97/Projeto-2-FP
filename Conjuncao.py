def cria_coordenada(n,m):
    
    if isinstance(n,int) and isinstance(m,int):
        
        if n >= 0 and m >= 0:

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
    
    if isinstance(u,dict):
        
        if len(u) == 2:
            
            if 'linha' in u and 'coluna' in u:
                
                if isinstance(u['linha'],int) and isinstance(u['coluna'],int):
        
                    if u['linha'] >= 0 and u['coluna'] >= 0:
                        
                        return True
    return False

def coordenadas_iguais(c,q):
    
    if e_coordenada(c) and e_coordenada(q):
        
        if coordenada_linha(c) == coordenada_linha(q)\
        and coordenada_coluna(c) == coordenada_coluna(q):
            
            return True
        
        return False
            
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
    
    if isinstance(t,tuple):
        
        if len(t) == 2:
            
            if isinstance(t[0],tuple) and isinstance(t[1],tuple):
                
                res = {'esp-linha': t[0], 'esp-coluna': t[1],\
                        'celulas': [[0]*len(t[1])]}
                
                for i in range(len(t[0]) -1):
                    
                    res['celulas'] += [[0]*len(t[1])]
                    
                return res
                
            
    raise ValueError('cria_tabuleiro: argumento invalido')
                
                
def tabuleiro_dimensoes(t):
    
    if e_tabuleiro(t):
        
        return (len(t['esp-linha']),len(t['esp-coluna']))

def tabuleiro_especificacoes(t):
    
    if e_tabuleiro(t):
    
        return (t['esp-linha'],t['esp-coluna'])

def tabuleiro_celula(t,c):
    
    if e_tabuleiro(t) and e_coordenada(c):
        
        return t['celulas'][coordenada_linha(c) -1][coordenada_coluna(c) -1]

def tabuleiro_preenche_celula(t,c,v):
    
    if e_tabuleiro(t) and e_coordenada(c) and isinstance(v,int):
        
        if 0 <= v <= 2:
               
            t['celulas'][coordenada_linha(c) -1][coordenada_coluna(c) -1] = v
            return t

def e_tabuleiro(t):
    
    if isinstance(t,dict):
        
        if len(t) == 3:
            
            if 'esp-linha' in t and 'esp-coluna' in t and 'celulas' in t:
                
                if isinstance(t['esp-linha'],tuple) and isinstance(t['esp-coluna'],tuple) and isinstance(t['celulas'],list):
                                
                    if len(t['celulas']) == len(t['esp-linha']):
                            
                        if e_especificacao(t['esp-linha']) and e_especificacao(t['esp-coluna']):
                                
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

t1 = (((2,),(3,),(2,),(2, 2),(2,)),((2,),(1, 2),(2,),(3,),(3,)))

tab = cria_tabuleiro(t1)

