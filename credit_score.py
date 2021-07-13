import streamlit as st
import pandas as pd
import pickle



st.set_page_config(page_title = 'Credit Scoring', 
				   layout = 'wide', 
				   initial_sidebar_state = 'auto')

st.title('Análise de risco de crédito')


paginas=['Home','Objetivo','Simulação']
pagina=st.sidebar.selectbox('Selecione a opção que deseja navegar',paginas)

# page1
if pagina=='Home':
	imagem = 'img3.jpg'
	st.markdown('# **Seja bem vindo** ao analisedecreditoapp')
	st.image(imagem,use_column_width='always')

# page2
if pagina=='Objetivo':
	insight='insight.jpg'
	st.write(' Este web app foi desenvolvido baseado em um dataset do que traz operações bancárias com montante entre 4 mil e 35 mil Euros, e tem como objetivo reduzir o índice de inadimplência, que inicialmente era de 21% , chegando a ficar em torno de 6%, como pode ser observado no gráfico abaixo. ')
	st.image(insight)

# page3	 
if pagina=='Simulação':
	
	st.markdown('## **Preencha os dados de acordo com perfil do cliente**')
	

	st.markdown('---')
	st.markdown(' ')

	# sidebar
	

	# colunas 
	col1, col2 = st.beta_columns(2)
	col1.markdown('## Dados do cliente')
	x1 = col1.slider('Idade', 18, 95, 25, 1)
	x2 = col1.slider('Tempo de Emprego', 0, 41, 5, 1)
	x7 = col1.slider('Renda por ano', 0,250000,2000,500)
	x3 = col1.radio('Tipo de Moradia', ['alugada','hipoteca', 'propria'])


	col2.markdown('## Histórico financeiro e objetivo do empréstimo')
	x9 = col2.radio('Classificação de risco histórico',['A','B', 'C', 'D'])
	x10 = col2.radio('Inadimplência histórica', [0,1])
	x11 = col2.slider('Quantidade de anos do primeiro emprestimo ', 0,20,1,1)
	x4 = col2.selectbox('Objetivo do Empréstimo', ['consolidacao_debito','educacao', 'pessoal','risco', 'reformar_casa','saude' ])



	st.markdown('---')
	st.markdown('## Dados referentes ao empréstimo')
	x5 = st.slider('Montante do Empréstimo', 0,35000,1000,50)
	x6 = st.number_input('Taxa de Juros')
	
	x8 = (float(x5/x7)*100)
	st.write('Porcentagem da renda anual {}%'.format(round(x8,2)))

	st.markdown('### Simulação')

	# Criando um dataframe para entrada do modelo 
	dicionario  =  {'idade':[x1], 
			  'tempo_de_emprego':x2,
			  'tipo_moradia':[x3], 
			  'objetivo_emprestimo':[x4],
	       	  'montante_emprestimo':[x5], 
	       	  'taxa_juros':[x6], 
	       	  'renda_por_ano':[x7],
	       	  'porc_empr_renda_anual':[x8/100], 
	       	  'class_risco_historico':[x9], 
	       	  'inadimplencia_hist':[x10],
	       	  'qtd_anos_primeiro_emprestimo':[x11]}


	dados = pd.DataFrame(dicionario) 

	#  encoding das variaveis categoricas do dataframe
	dic_tipo_moradia={'propria':0, 'hipoteca':1, 'alugada':2, }
	dados['tipo_moradia'] = dados['tipo_moradia'].map(dic_tipo_moradia)

	dic_objetivo_emprestimo={'educacao':0, 'saude':1, 'risco':2, 'pessoal':3, 'reformar_casa':4,'consolidacao_debito':5}
	dados['objetivo_emprestimo'] = dados['objetivo_emprestimo'].map(dic_objetivo_emprestimo)

	dic_class_risco_historico={'A':0,'B':1,'C':2,'D':3}
	dados['class_risco_historico'] = dados['class_risco_historico'].map(dic_class_risco_historico)


	st.write(dados)

	st.markdown('---')

	modelo = open('best_model_lgbm', 'rb')
	modelo = pickle.load(modelo)



	if st.button('Executar a Simulação'):
		pred = modelo.predict(dados)
		if pred==1:
			st.markdown('**Crédito negado**')
		else:
			st.markdown('**Crédito aprovado**')
		


