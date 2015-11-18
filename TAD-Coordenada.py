def cria_coordenada(n,m):
    
    if isinstance(n,int) and isinstance(m,int):
        
        return {'linha' : n, 'coluna' : m}
    
    raise ValueError('cria_coordenadas: argumentos invalidos')




def coordenada_linha(c):
    
    if e_coordenada(c):
        
        return c['linha']
    
    raise ValueError('coordenada_coluna: argumento invalido')




def coordenada_coluna(c):
    
    if e_coordenada(c):
        
        return c['coluna']
    
    raise ValueError('coordenada_coluna: argumento invalido')




def e_coordenada(u):
    
    if isinstance(u,dict):
        
        if len(u) == 2:
            
            if 'linha' in u and 'coluna' in u:
                
                if isinstance(u['linha'],int) and isinstance(u['coluna'],int):
        
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

