import csv
from collections import Counter
import matplotlib.pyplot as plt
from matplotlib import style

arqtweets = open('tweets.txt')
lendotweets = csv.reader(arqtweets)

#word stop - data cleansing
lista_stop_words = ['a',
                    'as',
                    'antes',
                    'ao',
                    'en',
                    'mais',
                    'até',
                    'após',
                    'aqui',
                    'cada',
                    'com',
                    'como',
                    'contra',
                    'de',
                    'da',
                    'das',
                    'do',
                    'desde',
                    'desta',
                    'deste',                    
                    'e',
                    'em',
                    'entre',
                    'esse',
                    'essa',
                    'esta',
                    'este',
                    'mas',
                    'nesta',
                    'neste',
                    'na',
                    'no',
                    'o',
                    'os',
                    'para',
                    'por',
                    'perante',
                    'pra',
                    'brasil',
                    'brasil.',
                    'tem',
                    'pelo',
                    'vai',
                    'gente',
                    'vamos',
                    'eu',
                    'ta',
                    'qual',
                    'quais',
                    'quando',
                    'que',
                    'quem',
                    'rt',
                    'se',
                    'sem',
                    'sob',
                    'sobre',
                    'um',
                    'uma',
                    'vez',
                    'in',
                    'to',
                    'and',
                    'when',
                    'how',
                    'from',
                    'since',
                    'the',
                    'on',
                    'me',
                    'this',
                    'that',
                    'what',
                    'is',
                    'not',
                    'why',
                    'who',
                    'he',
                    'at',
                    'i',
                    'for',
                    'u']

todostweets = []

for row in lendotweets:
    lista = str(row)[3:-3]
    lista = lista.replace(",","")
    lista = lista.replace("'","")
    lista = lista.split()
    
    for cadapalavra in lista:
        cada= cadapalavra[1:]
        if cada not in lista_stop_words:
            todostweets.append(cada)

conta = Counter(todostweets)
contador = conta.most_common(20)
print(contador)

#gerando a lista
global x
global y
x = []
y = []

for k ,v in contador:
    x.append(k)
    y.append(v)

print(x)
print(y)

#plotando gráfico de barras

style.use('ggplot')

plt.bar(range(len(y)), y, align='center')
plt.xticks(range(len(y)), x, size='medium')

#plt.legend()
plt.xlabel('Palavras')
plt.ylabel('Contagem')
plt.title('Contagem de Palavras\nTwitter')

plt.show()
