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
        st.markdown('#pyRDC')
        st.markdown('{}'.format(text2), unsafe_allow_html=True)

        text3 = gettext.text2()
        st.markdown('{}'.format(text3), unsafe_allow_html=True)
        st.write("Table: Conjunto de dados para o estudo de Linearidade")
        st.table(df)

        gettestes = testes_variancia()
        
        aov_table, coef_table, conf_int, pearson_table = gettestes.anova(data=df)

        st.write("Tabela da ANOVA")
        st.table(aov_table)

        if aov_table['P-valor'][0] < 0.05:
            st.write("Rejeitamos a hipótese nula de que os grupos são iguais.")
        else:
            st.write("Não podemos rejeitar a hipótese nula de que os grupos são iguais.")

        st.write("Tabela dos coeficientes")
        st.table(coef_table)

        st.write("Intervalo de confiança para os parâmetros")
        st.table(conf_int)

        st.write("Medida descritiva da qualidade do ajuste")
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
