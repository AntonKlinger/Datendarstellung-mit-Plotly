import plotly.express as px


df = px.data.iris()     #liefer einen im Programm enthaltenen Datensatz
#print(df)

fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species")

fig.write_html('first_plot.html', auto_open=True)