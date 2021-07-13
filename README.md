# Análise de risco de credito

link do dataset: https://www.kaggle.com/laotse/credit-risk-dataset?select=credit_risk_dataset.csv

## Problema: 
 - Reduzir o índice de inadimplência.
 
## Solução:

 - Foi desenvolvido um modelo de machine learning que a partir das variáveis de entrada, é capaz de identificar quando o empréstimo é de risco ou não, com uma precisão de 95% para casos de risco, e que é capaz de reduzir cerca de 14% a inadimplência.


Utilizando o dataset acima, foi desenvolvido um projeto com objetivo de fazer uma análise exploratória dos dados e desenvolver um modelo utilizando machine learning de análise de risco de crédito.

Primeiro passo do projeto após obter os dados, foi tratamento dos mesmos, renomeando as colunas, substituindo valores internos do dataset e tratando valores ausentes.

Logo após isso foi feito uma análise exploratória dos dados, selecionando as features que tinham maior correlação com a variável "risco_empréstimo" e a partir dessa análise foi  possível o gerar alguns insights, como por exemplo, concluir que mais que 70% dos empréstimos considerados de risco são de pessoas que moram em casa alugada, clientes com renda abaixo de 69 k tendem a oferecer maior risco.

Após desenvolver um modelo, a solução foi entregue via web app, onde utilizei a biblioteca streamlit do python para criar toda a interface e também fazer o deploy do modelo.

link do webapp: 

