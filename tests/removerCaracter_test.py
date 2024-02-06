from src.StringTools import StringTools

def test_removerCaracter_padrao():
    s1 = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'

    st = StringTools()
    result = st.removerCaracter(s1, 'oei')

    assert result == 'Lrm psum dlr st amt, cnscttur adpscng lt.'

def test_removerCaracter_string_vazia():
    st = StringTools()
    result = st.removerCaracter('', 'aeiou')

    assert result == ''

def test_removerCaracter_remover_vazia():
    s1 = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
    st = StringTools()
    result = st.removerCaracter(s1, '')

    assert result == s1

def test_removerCaracter_remover_espacos():
    s1 = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
    st = StringTools()
    result = st.removerCaracter(s1, ' ')

    assert result == 'Loremipsumdolorsitamet,consecteturadipiscingelit.'
    