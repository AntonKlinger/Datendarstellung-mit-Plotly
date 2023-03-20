import plotly.graph_objs as go

graph = go.Figure(
    data=go.Bar(
        x=[0, 1, 2],
        y=[39, 94, 48]
    ),
    layout=go.Layout(
        title=go.layout.Title(text="Diagramm")
    )
)
graph.write_html('first_plot.html', auto_open=True)
