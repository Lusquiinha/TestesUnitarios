from src.StringTools import StringTools

def test_separa_padrao():
    s = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
    
    st = StringTools()
    result = st.separa(s)
    
    assert result == ['Lorem', 'ipsum', 'dolor', 'sit', 'amet,', 'consectetur', 'adipiscing', 'elit.']

def test_separa_vazio():
    s = ''
    
    st = StringTools()
    result = st.separa(s)
    
    assert result == []

def test_separa_delim_i():
    s = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
    
    st = StringTools()
    result = st.separa(s, 'i')
    
    assert result == ['Lorem ', 'psum dolor s', 't amet, consectetur ad', 'p', 'sc', 'ng el', 't.']

def test_separa_delim_ie():
    s = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
    
    st = StringTools()
    result = st.separa(s, 'ie')
    
    assert result == ['Lor', 'm ', 'psum dolor s', 't am', 't, cons', 'ct', 'tur ad', 'p', 'sc', 'ng ', 'l', 't.']