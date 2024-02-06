from src.StringTools import StringTools

def test_encontra_padrao():
    s = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
    
    st = StringTools()
    result = st.encontra(s, 'ipsum')
    
    assert result == 6

def test_encontra_nao_encontra():
    s = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
    
    st = StringTools()
    result = st.encontra(s, 'ipsummm')
    
    assert result == -1

def test_encontra_find_vazio():
    s = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
    
    st = StringTools()
    result = st.encontra(s, '')
    
    assert result == -1

def test_encontra_string_vazia():
    s = ''
    
    st = StringTools()
    result = st.encontra(s, 'asd')
    
    assert result == -1

def test_encontra_fim():
    s = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
    
    st = StringTools()
    result = st.encontra(s, 'elit.')
    
    assert result == 51

def test_encontra_inicio():
    s = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
    
    st = StringTools()
    result = st.encontra(s, 'Lorem')
    
    assert result == 0
