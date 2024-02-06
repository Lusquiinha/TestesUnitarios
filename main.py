from src.StringTools import StringTools

def main():
    st = StringTools()
    
    concat = st.concatenar('Lucas', ' de',' Oliveira', ' Rodrigues', ' Alves')
    print(concat)

    remove = st.removerCaracter(concat, 'aeiou')
    print(remove +' - aeiou')

    encontra = st.encontra(concat, 'Oliveira')
    print('encontrado em', encontra )

    remove = st.removerSequencia(concat, ' Rodrigues')
    print(remove)

if __name__ == '__main__':
    main()