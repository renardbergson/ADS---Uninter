'''
  Probabilidade significa a possibilidade de que algo pode ocorrer ou não. Analiticamente, esse dado pode ser obtido através da fórmula: 
  
  P(A) = n / N
  
  "n" é a possibilidade "desejada" de que o fato ocorra e "N" é o total de possibilidades que temos.
  
  Ex: a cada 10 cobranças de pênalty, um jogador acerta 8. Qual a probabilidade desse jogador acertar uma cobrança? 8/10 = 0,8 = 80% de chance.

  * Quanto à distribuição normal, consultar o material didático!

  QUESTÃO 1
  Em uma produção de 1.000 peças, 14 delas apresentam defeitos que impossibilitam o uso. Qual é a probabilidade de que uma dessas peças, escolhida aleatoriamente, NÃO apresente defeito?

  P(A) = 1000 - 14 = 986
  P(A) = 986 / 1000 = 0,986
  P(A) = 98,6%

  QUESTÃO 2 (distribuição normal)

  Considere um projetor multimídia cuja lâmpada tem vida útil de 5.000 horas com desvio-padrão de 300 horas. Supondo que os dados estão de acordo com uma "distribuição normal", por meio do Python, determine a probabilidade de que um projetor, selecionado ao acaso, tenha lâmpada com vida útil entre 5.000 e 5.500 horas.

  ************* IMPORTANTE! *************
  Como o Python considera as porcentagens da distribuição normal de forma acumulada (diferente do que consideramos na forma analítica, que é 50% para mais ou para menos, a partir da média), deve-se adotar o raciocínio a seguir:

  
  I - Para obter probabilidades acima da Média
    p = scipy.stats.norm(media, desvioPadrao).cdf(x)-0.5
  
  II - Para obter probabilidades abaixo da Média
    p = scipy.stats.norm(media, desvioPadrao).cdf(x)-0.5
'''
print("QUESTÃO 2");
import scipy.stats;
media = 5000; 
desvioPadrao = 300;
x = 5500; # valor acima da média (inserimos -0.5 depois)
p = scipy.stats.norm(media, desvioPadrao).cdf(x)-0.5;
print(f'Probabilidade: {p * 100:.2f}%');