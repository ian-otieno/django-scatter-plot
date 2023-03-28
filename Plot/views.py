from django.shortcuts import render
import plotly.graph_objs as go
from plotly.offline import plot
import numpy as np
import statistics
# Create your views here.
def home(request):
    return render(request, 'home.html')

def scatter_view(request):
    x = [1, 2, 3]
    y = [4, 2, 5]
    data = [
        go.Scatter(
            x=x,
            y=y,
            mode='markers'
        )
    ]
    layout = go.Layout(
        title=f'Scatter Plot - Mean: {np.mean(x):.2f},{np.mean(y):.2f}; Mode: {statistics.mode(x)},{statistics.mode(y)}; Median: {np.median(x)},{np.median(y)}; Standard Deviation: {np.std(x):.2f},{np.std(y):.2f}; Coefficient of Correlation: {np.corrcoef(x, y)[0][1]:.2f}'
    )
    fig = go.Figure(data=data, layout=layout)
    plot_div = plot(fig, output_type='div')
    return render(request, 'scatter.html', {'plot_div': plot_div})

