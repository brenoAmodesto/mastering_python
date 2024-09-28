#Exercício - sistema de perguntas e respostas

perguntas = [
   {
       'Pergunta': 'Quanto é 2+2 ?',
       'Opcoes': ['1', '3', '4', '5'],
       'Resposta': '4',
   },
   { 
       'Pergunta': 'Quanto é 5*5',
       'Opcoes': ['25', '55', '10', '51'],
       'Resposta': '25',
       
   },
   {
       'Pergunta': 'Quanto é 10/2',
       'Opcoes': ['4', '5', '2', '1'],
       'Resposta': '5',
   },
]


total = 0
contador = 0
while contador < 3:
    def executa(dicionario):
        global total
        d1 = perguntas[dicionario]
        pergunta = d1['Pergunta']
        print(f'Pergunta: {pergunta}')

        for x, v in enumerate(d1['Opcoes']):
            print(f'{x}) {v}')
        p2 = input("")
        
        if p2 == d1['Resposta']:
            total = total + 1
            print('Acertou')
        else:
            print('Errou meu')

        if contador == 2:
            print(f'Vocẽ acertou {total} de 3') 
        
    executa(contador) 
    contador = contador + 1  




    





