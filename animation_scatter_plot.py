import plotly.express as px

df = px.data.gapminder()
print(df)
print(df.columns)

fig = px.scatter(df, x="gdpPercap", y="lifeExp",
                 animation_frame="year", animation_group="country",
                 range_x=[100, 80000], range_y=[25, 90],
                 color="continent", size="pop", hover_name="country",
                 size_max=100)

fig.write_html("Plot.html", auto_open="True")