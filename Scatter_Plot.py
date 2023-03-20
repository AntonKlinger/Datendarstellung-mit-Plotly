import plotly.express as px


df = px.data.iris()     #liefer einen im Programm enthaltenen Datensatz
df["Fehler"] = df["sepal_width"]/50
#print(df)

fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species",    # erstellen eines Scaller Plots
                 marginal_x="box", marginal_y="violin",                     # hinzufügen der grafischen Auswertung
                 trendline="ols",
                 error_x="Fehler")                                           # hinzufügen der Trendlinie

fig.write_html('first_plot.html', auto_open=True)