import streamlit as st
import pandas as pd
import numpy as np
import pickle



st.set_page_config(page_title = 'Credit Scoring', 
				   layout = 'wide', 
				   initial_sidebar_state = 'auto')




st.title('Credit Scoring App')

st.sidebar.title('Dados do Cliente') 



st.markdown('---')
st.markdown('### Dados do hitórico financeiro e de posses do proponente')
st.markdown(' ')

# sidebar
x1 = st.sidebar.slider('Idade', 18, 95, 25, 1)
x2 = st.sidebar.slider('Tempo de Emprego', 0, 41, 5, 1)

# colunas 
col1, col2 = st.beta_columns(2)
x3 = col1.radio('Tipo de Moradia', ['alugada','hipoteca', 'propria','outro'])
x4 = col1.radio('Objetivo do Empréstimo', ['consolidacao_debito','educacao', 'pessoal','risco', 'reformar_casa','saude' ])
x5 = col1.slider('Montante do Empréstimo', 0,35000,1000,50)
# x6 = st.selectbox('Taxa de Juros', 1,24,2,0.1)
x7 =  col2.slider('Renda por ano', 0,205000,10000,250)
# x8 = st.slider('Porcentagem da renda anual', 0,1,.5)
x9 = col2.selectbox('Classificação de risco histórico',['A','B', 'C', 'D', 'E', 'F', 'G'])
x10 = col2.selectbox('Inadimplência histórica', [0,1])
x11 = col2.slider('Quantidade de anos do primeiro emprestimo ', 0,20,1,1)
 
# x9 = st.sidebar.selectbox('Status', ['masculino/divorciado', 'feminino/divorciado',
#        'masculino/solteiro', 'masculino/casado'])
# x20 = st.sidebar.selectbox('Estrangeiro', ['não', 'sim'])
# x18 = st.sidebar.selectbox('Dependentes', [1,2])
# x17 = st.sidebar.selectbox('Trabalho', ['desempregado',  'nível 1',  'nível 2',  'nível 3' ])
# x7 = st.sidebar.selectbox('Emprego', ['desempregado', '< 1 ano',  '[1,4) anos',
#         '[4,7) anos', '> 7 anos'])


# col1, col2, col3, col4 = st.beta_columns(4)
# # col1
# x1 = col1.radio('Conta', ['negativo', '[0-200)', '200+', 'sem conta'], help = 'Essa variável é tchululu tchalala')
# x14 = col1.radio('Financiamentos', ['bancos', 'lojas', 'nenhum'])
# x15 = col1.radio('Moradia', ['alugada', 'própria', 'de graça'])

# # col2
# x6 = col2.radio('Poupança', ['<100', '[100-500)', '[500-1000)',
#        '>1000', 'sem conta'])
# x10 = col2.radio('Garantia', ['nenhum', 'co-aplicante', 'fiador'])
# x11 = col2.radio('Residencia', [1,2,3,4])

# # col3
# x3 = col3.radio('Historico', ['primeira vez', 'creditos quitados', 'pagamento em dia', 
#        'já atrasou pagamentos', 'conta crítica'])
# x16 = col3.radio('Creditos', [1, 2, 3, 4])
# x12 = col3.radio('Propriedades', ['imobiliario', 'seguro  de vida',
#       'carro', 'sem propriedades'])

# # col4
# x8 = col4.radio('Taxa', [1,2,3, 4])
# x19 = col4.radio('Telefone', [ 'não', 'sim'])



# st.markdown('---')
# st.markdown('### Dados referentes ao empréstimo')

# col1, col2 = st.beta_columns(2)
# x4 = col1.radio('Motivo', ['carro novo', 'carro usado', 'móveis', 
#        'radio/televisão', 'itens de casa', 'reparos', 
#        'educação', 'férias', 'retreinamentos', 
#        'negócios', 'outros'])
# x2 = col2.slider('Duração', 3, 72, 12, 1)
# x5 = col2.slider('Quantia', 250, 25000, 1000, 50)

# st.markdown('---')


 
# dicionario  =  {'idade':[X1], 
# 		  'tempo_de_emprego',
# 		  'tipo_moradia', 
# 		  'objetivo_emprestimo',
#        	  'montante_emprestimo', 
#        	  'taxa_juros', 
#        	  'renda_por_ano',
#        	  'porc_empr_renda_anual', 
#        	  'class_risco_historico', 
#        	  'inadimplencia_hist',
#        	  'qtd_anos_primeiro_emprestimo', 
#        	  'risco_emprestimo'}

# dados = pd.DataFrame(dicionario) 

# st.write(dados)

# st.markdown('---')

# modelo = load_model('best_rf_model')



# if st.button('EXECUTAR O MODELO'):
# 	saida = predict_model(modelo, dados)
# 	prob = float(saida['Score'])
# 	clas = int(saida['Label']) 

# 	if clas == 0:
# 		prob = 1 - prob
# 		st.markdown('### Previsão do Modelo: **Bom Pagador**, com score = {}'.format(round(prob, 2))) 
# 		st.balloons() 
# 	else:
# 		st.markdown('### Previsão do Modelo: **Mau Pagador**, com score = {}'.format(round(prob, 2)))     

# 	if prob < 0.44:  
# 		st.success('Usuário na Faixa de Score A - APROVADO SEM RESTRIÇÕES')
# 		st.balloons() 
# 	elif prob < 0.50:
# 		st.info('Usuário dnaa Faixa de Score B - APROVADO COM RESTRIÇÕES')
# 		st.balloons() 
# 	elif prob < 0.55:
# 		st.error('Usuário na Faixa de Score C - CONVERSAR COM O GERENTE')
# 	else:
# 		st.error('Usuário na Faixa de Score D - NEGAR CRÉDITO/REVER CONDIÇÕES')



# 	#pred = float(saida['Label'].round(2)) 
# 	#pred = saida['Score']
# 	#s1 = 'Custo Estimado do Seguro: ${:.2f}'.format(pred) 
# 	#st.markdown('### **' + pred + '**')  
