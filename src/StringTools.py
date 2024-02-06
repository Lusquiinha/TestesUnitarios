class StringTools:
    def concatenar(self, *args: str) -> str:
        """Concatena as strings que são colocadas como parametro."""

        string = ''
        for i in args:
            string += i 

        return string
    
    def removerCaracter(self, string: str, remover: str) -> str:
        """Remove da string os caracteres que estão em remover"""

        res = ''
        for c in string:
            if c not in remover:
                res += c
        
        return res
    
    def encontra(self, string: str, find: str) -> int:
        """Encontra o indice da primeira ocorrencia de find\n
        na string se não encontrar retorna -1"""
        if len(find) == 0: return -1
        pos = 0
        while pos <= len(string) - len(find):
            if string[pos:pos+len(find)] == find:
                return pos
            pos += 1

        return -1
    
    def removerSequencia(self, string: str, seq: str) -> str:
        """remove da string a sequencia que esta em seq"""
        res = string
        existe = self.encontra(res, seq)

        while existe != -1:

            res = res[0:existe] + res[existe+len(seq):]
            existe = self.encontra(res, seq)

        return res

    def separa(self, string: str, char: str = ' ') -> list[str]:
        """separa a string em uma lista de strings\n
        separadas pelos delimitadores em char de valor padrão '  '"""
        res = []
        slow, fast = 0, 0

        while slow < len(string):
            if fast==len(string) or string[fast] in char:
                res.append(string[slow:fast])
                slow = fast + 1
            fast += 1
        
        return res


