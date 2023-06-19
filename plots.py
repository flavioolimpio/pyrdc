import numpy as np
import seaborn as sns
import scipy.stats as stats
#import plotly.graph_objs as go
#import plotly.express as px
from scipy import stats
from sklearn.preprocessing import StandardScaler
from statsmodels.graphics.gofplots import qqplot
import matplotlib.pyplot as plt

class Plots:
    def __init__(self):
        pass

# histograma
    #def hist(self,x):
    #    x_axis = np.arange(0.95*min(x), 1.025*max(x), 0.001)
    #    normal = stats.norm.pdf(x_axis, np.mean(x), np.std(x))
#
    #    kde = stats.gaussian_kde(x)
    #    kde_plot = kde.evaluate(x_axis)
#
    #    fig_hist = px.histogram(x = x, nbins=10,
    #                      histnorm='probability density', color_discrete_sequence=["silver"])
    #    fig_hist.update_traces(name='Data probability density', showlegend = True)
    #    fig_hist.add_traces(go.Scatter(x=x_axis,
    #                              y=normal,
    #                              name = "Normal distribution",
    #                              mode = 'lines',
    #                              line = dict(color='red')
    #                              )
    #                  )
    #    fig_hist.add_traces(go.Scatter(x=x_axis,
    #                              y=kde_plot,
    #                              name = "Non parametric density",
    #                              mode = 'lines',
    #                              line = dict(color='black')
    #                              )
    #                  )
    #    fig_hist.update_layout(template='simple_white', # deixando o layout branco
    #                    legend = dict(orientation="h",
    #                                yanchor="bottom",
    #                                y=1.02,
    #                                xanchor="right",
    #                                x=1),
    #                           yaxis = dict(title="Probability density"),
    #                           xaxis = dict(title="Área do pico"),
    #                      margin={"r":0,"l":0,"b":0}, # removendo margens desnecessárias
    #                    )
    #    fig_hist.update_xaxes(showline=True, linewidth=1, linecolor='black', mirror=True) # adicionando linhas no eixo x do grafico
    #    fig_hist.update_yaxes(showline=True, linewidth=1, linecolor='black', mirror=True) # adicionando linhas no eixo y do gráfico
#
    #    return fig_hist

    
    def graficos(self, conc, resp, ordem):
        slope, intercept, _, _, _ = stats.linregress(conc, resp)

        y_pred = intercept + (slope*conc)

        fig_residuo, ax_residuo = plt.subplots()
        resplot = sns.residplot(x=y_pred, y=resp - y_pred, ax=ax_residuo)

        scaler = StandardScaler()
        rp = resp - y_pred
        rp = rp.reshape(-1,1)
        residuo_prad = scaler.fit_transform(rp)

        fig_residuo_pad, ax_residuo_pad = plt.subplots()
        resplot_prad = sns.residplot(x=y_pred, y=residuo_prad, ax=ax_residuo_pad)

        fig_qqplot = qqplot(resp - y_pred, line='s')

        #ordem_coleta = [14,13,9,7,10,2,15,11,8,1,12,6,4,5,3]
        ordem_coleta = ordem
        fig_coleta, ax_coleta = plt.subplots()
        ordem = sns.lineplot(x=ordem_coleta, y=resp - y_pred, ax=ax_coleta, markers=True, dashes=False)

        return fig_residuo, fig_residuo_pad, fig_qqplot, fig_coleta





