import pandas as pd
import statsmodels.stats.api as sms
import statsmodels.formula.api as smf
import statsmodels.api as sm
import statsmodels.stats.diagnostic as sms
from scipy.stats import shapiro

class testes_variancia:
    def __init__(self):
        pass

    def homoscedasticity_test(self,data):
        '''
        Function for testing the homoscedasticity of residuals in a linear regression model.
        It plots residuals and standardized residuals vs. fitted values and runs Breusch-Pagan and Goldfeld-Quandt tests.
        
        Args:
        * model - fitted OLS model from statsmodels
        '''
        model = smf.ols('Área ~ Concentração', data=data).fit()
        fitted_vals = model.predict()
        resids = model.resid
        resids_standardized = model.get_influence().resid_studentized_internal
    
        bp_test = pd.DataFrame([[x for x in sms.het_breuschpagan(resids, model.model.exog,True)]], 
                               columns=['Estatistica', 'P-valor', 'f-value', 'f p-value'])
        
        # Selecione apenas as duas primeiras colunas
        bp_test = bp_test[['Estatistica', 'P-valor']]
    
        gq_test = pd.DataFrame([sms.het_goldfeldquandt(resids, model.model.exog)[:-1]],
                               columns=['Estatistica', 'P-value'],)
        
        # realiza o teste de Breusch-Godfrey com 4 defasagens
        bg_test = sms.acorr_breusch_godfrey(model, nlags=4)

        # cria um DataFrame com o resultado do teste
        bg_test = pd.DataFrame({"Estatística": [bg_test[0]], "P-valor": [bg_test[1]]})
        
        # Calcule o teste de Shapiro-Wilk para x
        stat, p = shapiro(resids)

        teste_shapiro = pd.DataFrame({
            'Estatística': [stat],
            'P-valor': [p]
        }, index=[0])
        
        return bp_test, gq_test, bg_test, teste_shapiro
    
    def anova(self, data):
        model_ols = smf.ols('Área ~ Concentração', data=data).fit()
        aov_table = sm.stats.anova_lm(model_ols, typ=2)

        # Adicione uma coluna para os quadrados médios
        aov_table['mean_sq'] = aov_table['sum_sq'] / aov_table['df']

        # Altere a ordem das colunas
        aov_table = aov_table[['df', 'sum_sq', 'mean_sq', 'F', 'PR(>F)']]

        aov_table = aov_table.rename(columns={'df': 'G.L', 'F': 'Estat.F', 'PR(>F)': 'P-valor'})
        
        coef_table = pd.DataFrame({
        'Estimativa': model_ols.params,
        'Desvio Padrão': model_ols.bse,
        'Estatística T': model_ols.tvalues,
        'P-valor': model_ols.pvalues})

        # Calcule os intervalos de confiança de 95% para os parâmetros
        conf_int = model_ols.conf_int(alpha=0.05)

        # Renomeie as colunas do DataFrame resultante
        conf_int = conf_int.rename(columns={0: 'Limite Inferior', 1: 'Limite Superior'})

        # Crie uma tabela para o coeficiente de correlação de Pearson
        pearson_table = pd.DataFrame({
            'Desvio padrão dos resíduos': [model_ols.mse_resid ** 0.5],
            'Graus de Liberdade': [model_ols.df_resid],
            'R2': [model_ols.rsquared],
            'Coeficiente de Correlação': [model_ols.rsquared ** 0.5]
        })

        return aov_table, coef_table, conf_int, pearson_table
    




        