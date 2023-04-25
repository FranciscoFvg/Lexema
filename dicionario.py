def getAcervo(option=1):
    if option == 1:
        acervo = []
        with open('palavras_cinco_letras.txt', 'r', encoding='utf-8') as arquivo:
            for linha in arquivo:
                linha = linha.strip()
                if len(str(linha)) == 5:
                    acervo.append(linha)
        
        return acervo
    else:
        acervoTeste = [
            'causa',
            'apraz'
        ]

        return acervoTeste