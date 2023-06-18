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