from src.StringTools import StringTools

def test_removerSequencia_padrao():
    s = 'Lorem ipsum dolor sit amet, ipsum consectetur adipiscing elit.'
    
    st = StringTools()
    result = st.removerSequencia(s, 'ipsum')
    
    assert result == 'Lorem  dolor sit amet,  consectetur adipiscing elit.'

def test_removerSequencia_vazio():
    s = 'Lorem ipsum dolor sit amet, ipsum consectetur adipiscing elit.'
    
    st = StringTools()
    result = st.removerSequencia(s, '')
    
    assert result == 'Lorem ipsum dolor sit amet, ipsum consectetur adipiscing elit.'

def test_removerSequencia_vazio2():
    s = ''
    
    st = StringTools()
    result = st.removerSequencia(s, 'asd')
    
    assert result == ''

def test_removerSequencia_caracter():
    s = 'Lorem ipsum dolor sit amet, ipsum consectetur adipiscing elit.'
    
    st = StringTools()
    result = st.removerSequencia(s, 'i')
    
    assert result == 'Lorem psum dolor st amet, psum consectetur adpscng elt.'

def test_removerSequencia_seq_inexistente():
    s = 'Lorem ipsum dolor sit amet, ipsum consectetur adipiscing elit.'
    
    st = StringTools()
    result = st.removerSequencia(s, 'Lucas')
    
    assert result == s