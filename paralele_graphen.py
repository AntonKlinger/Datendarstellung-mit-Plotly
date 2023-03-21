import plotly.express as px

df = px.data.iris()

fig = px.parallel_coordinates(df, color="species_id", labels={
    "sepal_length": "Sepal Length",
    "sepal_width": "Sepal Width",
    "petal_length": "Petal Length",
    "petal_width": "Petal Width"
})

fig.write_html("Plot.html", auto_open="True")