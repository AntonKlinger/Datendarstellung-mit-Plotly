import plotly.express as px

df = px.data.iris()

fig = px.scatter_matrix(df, dimensions=["sepal_length", "sepal_width", "petal_length", "petal_width"], color="species")

fig.write_html('first_plot.html', auto_open=True)