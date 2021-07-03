import streamlit as st
import pandas as pd
import pickle



st.set_page_config(page_title = 'Credit Scoring', 
				   layout = 'wide', 
				   initial_sidebar_state = 'auto')




st.title('Credit Scoring App')

st.sidebar.title('Dados do Cliente') 



st.markdown('---')
st.markdown('### Histórico financeiro,tipo de moradia e objetivo do empréstimo')
st.markdown(' ')

# sidebar
x1 = st.sidebar.slider('Idade', 18, 95, 25, 1)
x2 = st.sidebar.slider('Tempo de Emprego', 0, 41, 5, 1)

# colunas 
col1, col2 = st.beta_columns(2)
x3 = col1.radio('Tipo de Moradia', ['alugada','hipoteca', 'propria','outro'])
x4 = col1.radio('Objetivo do Empréstimo', ['consolidacao_debito','educacao', 'pessoal','risco', 'reformar_casa','saude' ])


x9 = col2.radio('Classificação de risco histórico',['A','B', 'C', 'D', 'E', 'F', 'G'])
x10 = col2.radio('Inadimplência histórica', [0,1])
x11 = col2.slider('Quantidade de anos do primeiro emprestimo ', 0,20,1,1)



st.markdown('---')
st.markdown('### Dados referentes ao empréstimo')
x5 = st.slider('Montante do Empréstimo', 0,35000,1000,50)
x6 = st.slider('Taxa de Juros', 1,24,11,1)
x7 =  st.slider('Renda por ano', 0,205000,10000,250)
x8 = (float(x5/x7)*100)
st.write('Porcentagem da renda anual {}%'.format(round(x8,2)))

st.markdown('### Simulação')

# Criando um dataframe para entrada do modelo 
dicionario  =  {'idade':[x1], 
		  'tempo_de_emprego':x2,
		  'tipo_moradia':[x3], 
		  'objetivo_emprestimo':[x4],
       	  'montante_emprestimo':[x5], 
       	  'taxa_juros':[x6/100], 
       	  'renda_por_ano':[x7],
       	  'porc_empr_renda_anual':[x8/100], 
       	  'class_risco_historico':[x9], 
       	  'inadimplencia_hist':[x10],
       	  'qtd_anos_primeiro_emprestimo':[x11]}


dados = pd.DataFrame(dicionario) 

#  encoding das variaveis categoricas do dataframe
dic_tipo_moradia={'propria':0, 'hipoteca':1, 'alugada':2, 'outro':3}
dados['tipo_moradia'] = dados['tipo_moradia'].map(dic_tipo_moradia)

dic_objetivo_emprestimo={'educacao':0, 'saude':1, 'risco':2, 'pessoal':3, 'reformar_casa':4,'consolidacao_debito':5}
dados['objetivo_emprestimo'] = dados['objetivo_emprestimo'].map(dic_objetivo_emprestimo)

dic_class_risco_historico={'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6}
dados['class_risco_historico'] = dados['class_risco_historico'].map(dic_class_risco_historico)


st.write(dados)

st.markdown('---')

modelo = open('modelo_analise_credito', 'rb')
modelo = pickle.load(modelo)



if st.button('Executar a Simulação'):
	proba = modelo.predict_proba(dados)[:,1]
	st.markdown('probabilidade: {}'.format(proba))
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
