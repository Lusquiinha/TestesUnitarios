from src.StringTools import StringTools

def test_concatenar_padrao():
    s1 = 'abcd'
    s2 = 'efgh'
    s3 = 'ijkl'
    s4 = 'mnop'
    st = StringTools()
    result = st.concatenar(s1,s2,s3,s4)

    assert result == s1+s2+s3+s4

def test_concatenar_vazio():
    st = StringTools()
    result = st.concatenar()

    assert result == ''