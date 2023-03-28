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
    
    mean_x = np.mean(x)
    mean_y = np.mean(y)
    mode_x = statistics.mode(x)
    mode_y = statistics.mode(y)
    median_x = np.median(x)
    median_y = np.median(y)
    std_x = np.std(x)
    std_y = np.std(y)
    corr_coef = np.corrcoef(x, y)[0][1]
    
    data = [
        go.Scatter(
            x=x,
            y=y,
            mode='markers'
        )
    ]
    
    layout = go.Layout(
        title=f'Scatter Plot'
    )
    
    fig = go.Figure(data=data, layout=layout)
    plot_div = plot(fig, output_type='div')
    
    stats = {
        'mean_x': mean_x,
        'mean_y': mean_y,
        'mode_x': mode_x,
        'mode_y': mode_y,
        'median_x': median_x,
        'median_y': median_y,
        'std_x': std_x,
        'std_y': std_y,
        'corr_coef': corr_coef
    }
    
    return render(request, 'scatter.html', {'plot_div': plot_div, 'stats': stats})