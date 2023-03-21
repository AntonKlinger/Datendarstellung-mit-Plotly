import plotly.express as px

df = px.data.gapminder()
df = df[df.country == "Germany"]
#print(df.columns) Augabe der Spaltennamen

fig = px.bar(df, x="year", y="pop", color="lifeExp")

fig.write_html('first_plot.html', auto_open=True)