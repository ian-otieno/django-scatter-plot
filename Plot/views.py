from django.shortcuts import render
import plotly.graph_objs as go
from plotly.offline import plot


# Create your views here.
def home(request):
    return render(request, 'home.html')


def scatter_view(request):
    data = [
        go.Scatter(
            x=[1, 2, 3],
            y=[4, 2, 5],
            mode='markers'
        )
    ]
    layout = go.Layout(
        title='Scatter Plot'
    )
    fig = go.Figure(data=data, layout=layout)
    plot_div = plot(fig, output_type='div')
    return render(request, 'scatter.html', {'plot_div': plot_div})    

