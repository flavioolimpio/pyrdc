import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
from texts import Texts
from testes import testes_variancia
from plots import Plots
#from normalidade import test_norm

def home():
    st.title("Página Inicial")
    gettext = Texts()
    
    text1 = gettext.text1()
    st.markdown('#pyRDC')
    st.markdown('{}'.format(text1), unsafe_allow_html=True)


def linearidade():
    st.title("Resultado da Análise")
    file = st.file_uploader("Arraste e solte um arquivo .csv ou .xlsx aqui", type=['csv', 'xlsx'])
    if file:    
        df = pd.read_csv(file)

        gettext = Texts()
    
        text2 = gettext.text2()
        st.markdown('{}'.format(text2), unsafe_allow_html=True)

        text3 = gettext.text3()
        st.markdown('{}'.format(text3), unsafe_allow_html=True)
        st.write("Table: Conjunto de dados para o estudo de Linearidade")
        st.table(df)

        text4 = gettext.text4()
        st.markdown('{}'.format(text4), unsafe_allow_html=True)

        gettestes = testes_variancia()
        
        aov_table, coef_table, conf_int, pearson_table = gettestes.anova(data=df)

        st.write("Tabela ANOVA: Esta tabela apresenta os resultados da análise de variância (ANOVA) para avaliar a significância das diferenças entre as médias dos grupos." +  
                 "A tabela inclui a fonte de variação, os graus de liberdade, a soma dos quadrados, a média dos quadrados, o valor F e o valor P")
        st.table(aov_table)

        p_value_anova = aov_table['P-valor'][0]

        text5 = gettext.text5(p_value=p_value_anova)
        st.markdown('{}'.format(text5), unsafe_allow_html=True)

        st.write("As estimativas dos parâmetros (coeficientes de regressão) e seus respectivos intervalos de confiança de 95% são:")
        st.write("Tabela dos coeficientes")
        st.table(coef_table)

        st.write("Intervalo de confiança para os parâmetros")
        st.table(conf_int)

        p_value_coef = coef_table['P-valor'][0]
        text6 = gettext.text6(p_value=p_value_coef)
        st.markdown('{}'.format(text6), unsafe_allow_html=True)

        cc = pearson_table['Coeficiente de Correlação']
        r_value = cc.item()
        text7 = gettext.text7(r_value=r_value)
        st.markdown('{}'.format(text7), unsafe_allow_html=True)
        st.write("Tabela do Coeficiente de Correlação de Pearson: Esta tabela apresenta o resultado do cálculo do coeficiente de correlação de Pearson entre duas variáveis." + 
        "O coeficiente mede a força e a direção da relação linear entre as variáveis.")
        st.table(pearson_table)

        bp_test, gq_test, shapiro = gettestes.homoscedasticity_test(data=df)

        st.write("Teste de homecedasticidade Breusch-Pagan")
        st.table(bp_test)
        st.write("Teste de homecedasticidade Goldfeld-Quandt")
        st.table(gq_test)

        st.write("Table 1: Teste de normalidade de Shapiro-Wilk com 95%")
        st.table(shapiro)

        getfigs = Plots()
        fig_residuo, fig_residuo_pad, fig_qqplot, fig_coleta = getfigs.graficos(df['Concentração'].values,df['Área'].values)

        st.write("Figura 1")
        st.pyplot(fig=fig_residuo)
        st.write("Figura 2")
        st.pyplot(fig=fig_residuo_pad)
        st.write("Figura 3")
        st.pyplot(fig=fig_qqplot)
        st.write("Figura 4")
        st.pyplot(fig=fig_coleta)


# Criação das páginas
PAGES = {
    "Home": home,
    "Linearidade": linearidade
}

# Criação do menu suspenso com ícones
with st.sidebar:
    selected = option_menu("Menu Principal", ["Home", 'Linearidade'], icons=['house', 'graph-up'], menu_icon="cast", default_index=1)
    selected

# Renderização da página selecionada
page = PAGES[selected]
page()
