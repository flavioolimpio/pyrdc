class Texts:
    def __init__(self):
        pass

    def text1(self):
        TEXT1 = """
        Esta aplicação consiste em realizar a validação de métodos analíticos baseados na RDC 166 de 2017 da ANVISA, assim como as resoluções do MAPA e INMETRO. As referênncias podem ser visualizadas em:                               
        [1] https://www.in.gov.br/materia/-/asset_publisher/Kujrw0TZC2Mb/content/id/19194581/do1-2017-07-25-resolucao-rdc-n-166-de-24-de-julho-de-2017-19194412 \n
        [2] https://www.gov.br/agricultura/pt-br/assuntos/laboratorios/arquivos-publicacoes-laboratorio/guia-de-validacao-controle-de-qualidade-analitica.pdf
        

        ## About
        Validation foi desenvolvido para pesquisadores/analistas que atuam no setor de desenvolvimento analítico de uma indústria. De maneira amigável, a aplicação pode ser
        utilizada para realizar validação de metódos analíticos preconizados pelas resoluções dos principais orgãos reguladores do país.

        ## Supporters
        Dr. Flávio Olimpio Sanches Neto                              
        https://www.linkedin.com/in/fl%C3%A1vio-olimpio-sanches-neto/
        https://www.researchgate.net/profile/Flavio-Neto-3           
        flavio_olimpio@outlook.com
        
        """

        return TEXT1
    
    def text2(self):
        TEXT2 = """
        <body style='text-align: justify; color: black;'>
        <h1 style='text-align: justify; color: black;'>1. Introdução</h1>
        <p> A linearidade de um procedimento analítico é a sua capacidade de obter resultados que sejam diretamente proporcionais à concentração de um analito em uma amostra.
        </p>
        </body>
        """

        return TEXT2
    
    def text3(self):
        TEXT3 = """
        <body style='text-align: justify; color: black;'>
        <h1 style='text-align: justify; color: black;'>2. Coleta de Dados</h1>
        <p> A seguir, apresentam-se os dados coletados:
        </p>
        </body>
        """

        return TEXT3
    
    def text4(self):
        TEXT4 = """
        <body style='text-align: justify; color: black;'>
        <h1 style='text-align: justify; color: black;'>3. Método dos Mínimos Quadrados Ordinários Estimação</h1>
        <p> O método dos mínimos quadrados é uma eficiente estratégia de estimação dos parâmetros da
        regressão e sua aplicação não é limitada apenas às relações lineares. Nesta seção utilizou-se o
        Método dos Mínimos Quadrados Ordinários.
        </p>
        </body>
        <body style='text-align: justify; color: black;'>
        <h1 style='text-align: justify; color: black;'>3.1. Teste do coeficiente angular</h1>
        <p> Para avaliar a significância do modelo utilizou-se o teste F da ANOVA. Neste caso, testou-se as hipóteses:</p>
        <p>H0: coeficiente angular igual a zero; </p>
        <p>H1: coeficiente angular diferente de zero.
        </p>
        </body>

        """

        return TEXT4
    

    def text5(self, p_value):
        if p_value > 0.05:
            TEXT5 = f"""
            <body style='text-align: justify; color: black;'>
            <p> Como P-valor ({p_value}) do teste ANOVA é maior que 0,05 (conforme especificado), não rejeita-se a hipótese nula (intercepto igual ao zero) ao nível de significância de 5%. Logo, conclui-se que o intercepto é estatísticamente igual ao zero.
            </p>
            </body>
            """
        else:
            TEXT5 = f"""
            <body style='text-align: justify; color: black;'>
            <p> Como P-valor ({p_value}) do teste ANOVA é menor ou igual a 0,05 (conforme especificado), rejeita-se a hipótese nula (intercepto igual ao zero) ao nível de significância de 5%. Logo, conclui-se que o intercepto é estatísticamente diferente de zero.
            </p>
            </body>
            """
        return TEXT5
    
    def text6(self, p_value):
        if p_value > 0.05:
            TEXT6 = f"""
            <body style='text-align: justify; color: black;'>
            <h1 style='text-align: justify; color: black;'>3.2. Teste do intercepto (coeficiente linear)</h1>
            <p> Para avaliar o intercepto (coeficiente linear) utilizou-se a estatística t de Student. Neste caso, as hipóteses foram as seguintes::</p>
            <p>H0: coeficiente angular igual a zero; </p>
            <p>H1: coeficiente angular diferente de zero.
            </p>
            </body>

            <body style='text-align: justify; color: black;'>
            <p> Como P-valor ({p_value}) do teste t é maior que 0,05 (conforme especificado), não rejeita-se a hipótese nula (intercepto igual ao zero) ao nível de significância de 5%. Logo, conclui-se que o intercepto é estatísticamente igual ao zero.
            </p>
            </body>
            """
        else:
            TEXT6 = f"""
            <body style='text-align: justify; color: black;'>
            <h1 style='text-align: justify; color: black;'>3.2. Teste do intercepto (coeficiente linear)</h1>
            <p> Para avaliar o intercepto (coeficiente linear) utilizou-se a estatística t de Student. Neste caso, as hipóteses foram as seguintes::</p>
            <p>H0: coeficiente angular igual a zero; </p>
            <p>H1: coeficiente angular diferente de zero.
            </p>
            </body>

            <body style='text-align: justify; color: black;'>
            <p> Como P-valor ({p_value}) do teste t é menor ou igual a 0,05 (conforme especificado), rejeita-se a hipótese nula (intercepto igual ao zero) ao nível de significância de 5%. Logo, conclui-se que o intercepto é estatísticamente diferente de zero.
            </p>
            </body>
            """
        return TEXT6
    
    def text7(self, r_value):
        if r_value > 0.9900:
            TEXT7 = f"""
            <body style='text-align: justify; color: black;'>
            <h1 style='text-align: justify; color: black;'>3.3. Coeficiente de correlação de Pearson</h1>
            <p> O coeficiente de correlação de Pearson mede a força e a direção da relação linear entre duas variáveis. Neste caso, o coeficiente de correlação é {r_value}, 
            o que é maior do que o valor especificado de 0,9900. Isso indica que existe uma forte relação linear entre as duas variáveis. Portanto, podemos concluir que a relação linear entre as variáveis é adequada.
            </p>
            </body>
            """ 
        else:
            TEXT7 = f"""
            <body style='text-align: justify; color: black;'>
            <h1 style='text-align: justify; color: black;'>3.3. Coeficiente de correlação de Pearson</h1>
            O coeficiente de correlação de Pearson mede a força e a direção da relação linear entre duas variáveis. Neste caso, o coeficiente de correlação é {r_value}, 
            o que é menor do que o valor especificado de 0,9900. Isso indica que a relação linear entre as duas variáveis não é tão forte. Portanto, podemos concluir que a relação linear entre as variáveis não é adequada.
            </p>
            </body>
            """            
        return TEXT7
    
    def text8(self):
        TEXT8 = """
        <body style='text-align: justify; color: black;'>
        <h1 style='text-align: justify; color: black;'>4. Análise Gráfica</h1>
        <p>Existem vários gráficos que podem ser usados para avaliar a qualidade do ajuste de um modelo estatístico aos dados. Alguns exemplos incluem:</p>
        <h1 style='text-align: justify; color: black;'>4.1. Diagóstico dos resíduos do modelo</h1>
        <ul>
            <li><strong>Gráfico de Resíduos Padronizados vs Valores Ajustados:</strong> Este gráfico é usado para verificar se os resíduos se distribuem aleatoriamente e para detectar a presença de valores extremos (outliers) nos dados. Geralmente, consideram-se outliers os pontos que excedem o limite de 3 desvios padrão.</li>
            <li><strong>Gráfico de Probabilidade Normal dos Resíduos:</strong> Este gráfico é usado para verificar a pressuposição de que os resíduos são distribuídos normalmente. Em caso de normalidade, os resíduos em geral seguem aproximadamente uma linha reta.</li>
            <li><strong>Gráfico de Resíduos vs Valores Ajustados:</strong> Este gráfico é usado para verificar a pressuposição de que os resíduos se distribuem aleatoriamente e têm variância constante.</li>
            <li><strong>Gráfico de Resíduos vs Ordem de Coleta:</strong> Este gráfico mostra os resíduos na ordem em que foram coletados e é usado para verificar a pressuposição de independência. Em geral, para que se cumpra tal requisito, os dados devem se dispor aleatoriamente em torno da linha central.</li>
        </ul>
        <p>As figuras dos 4 gráficos são mostradas a seguir.</p>
        </body>
        """
        return TEXT8
    

    def text9(self, p_value):
        if p_value > 0.05:
            TEXT9 = f"""
            <body style='text-align: justify; color: black;'>
            <h1 style='text-align: justify; color: black;'>5. Avaliação dos Resíduos</h1>
            <h2 style='text-align: justify; color: black;'>5.1. Avaliação da normalidade via teste de Shapiro-Wilk</h2>
            <p> O teste de Shapiro-Wilk é usado para avaliar a pressuposição de normalidade dos resíduos. Neste caso, as hipóteses foram as seguintes:</p>
            <p>H0: Os resíduos seguem uma distribuição normal.</p>
            <p>H1: Os resíduos não seguem uma distribuição normal.</p>
            <p> Como o P-valor ({p_value}) do teste de Shapiro-Wilk é maior que 0,05 (conforme especificado), não rejeita-se a hipótese nula ao nível de significância de 5%. Logo, conclui-se que não há evidências suficientes para afirmar que os resíduos não seguem uma distribuição normal.</p>
            </body>
            """
        else:
            TEXT9 = f"""
            <body style='text-align: justify; color: black;'>
            <h1 style='text-align: justify; color: black;'>5. Avaliação dos Resíduos</h1>
            <h2 style='text-align: justify; color: black;'>5.1. Avaliação da normalidade via teste de Shapiro-Wilk</h2>
            <p> O teste de Shapiro-Wilk é usado para avaliar a pressuposição de normalidade dos resíduos. Neste caso, as hipóteses foram as seguintes:</p>
            <p>H0: Os resíduos seguem uma distribuição normal.</p>
            <p>H1: Os resíduos não seguem uma distribuição normal.</p>
            <p> Como o P-valor ({p_value}) do teste de Shapiro-Wilk é menor ou igual a 0,05 (conforme especificado), rejeita-se a hipótese nula ao nível de significância de 5%. Logo, conclui-se que há evidências suficientes para afirmar que os resíduos não seguem uma distribuição normal.</p>
            </body>
            """
        return TEXT9
    

    def text10(p_value):
        if p_value > 0.05:
            TEXT10 = f"""
            <body style='text-align: justify; color: black;'>
            <h2 style='text-align: justify; color: black;'>5.2. Avaliação da homocedasticidade via teste de Breusch-Pagan</h2>
            <p> O teste de Breusch-Pagan é usado para avaliar a pressuposição de homocedasticidade dos resíduos. Neste caso, as hipóteses foram as seguintes:</p>
            <p>H0: Os resíduos têm variância constante.</p>
            <p>H1: Os resíduos não têm variância constante.</p>
            <p> Como o P-valor ({p_value}) do teste de Breusch-Pagan é maior que 0,05 (conforme especificado), não rejeita-se a hipótese nula ao nível de significância de 5%. Logo, conclui-se que não há evidências suficientes para afirmar que os resíduos não têm variância constante.</p>
            </body>
            """
        else:
            TEXT10 = f"""
            <body style='text-align: justify; color: black;'>
            <h2 style='text-align: justify; color: black;'>5.2. Avaliação da homocedasticidade via teste de Breusch-Pagan</h2>
            <p> O teste de Breusch-Pagan é usado para avaliar a pressuposição de homocedasticidade dos resíduos. Neste caso, as hipóteses foram as seguintes:</p>
            <p>H0: Os resíduos têm variância constante.</p>
            <p>H1: Os resíduos não têm variância constante.</p>
            <p> Como o P-valor ({p_value}) do teste de Breusch-Pagan é menor ou igual a 0,05 (conforme especificado), rejeita-se a hipótese nula ao nível de significância de 5%. Logo, conclui-se que há evidências suficientes para afirmar que os resíduos não têm variância constante.</p>
            </body>
            """
        return TEXT10


