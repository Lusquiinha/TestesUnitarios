from src.StringTools import StringTools

def main():
    st = StringTools()

    print('Exemplos de uso dos metodos de StringTools:\n')
    
    concat = st.concatenar('Lucas', ' de',' Oliveira', ' Rodrigues', ' Alves')
    print(f"""st.concatenar('Lucas', ' de',' Oliveira', ' Rodrigues', ' Alves'):
{st.concatenar('Lucas', ' de',' Oliveira', ' Rodrigues', ' Alves')}\n""")
    
    print(f"""st.removerCaracter('{concat}', 'aeiou'):
{st.removerCaracter(concat, 'aeiou')}\n""")
    
    print(f"""st.removerSequencia('{concat}', ' Rodrigues'):
{st.removerSequencia(concat, ' Rodrigues')}\n""")
    
    print(f"""st.encontra('{concat}', 'Oliveira'):
{st.encontra(concat, 'Oliveira')}\n""")

    print(f"""st.separa('{concat}'):
{st.separa(concat)}\n""")
    

if __name__ == '__main__':
    main()