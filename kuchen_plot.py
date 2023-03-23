import plotly.express as px

# df = px.data.gapminder().query("year==2007").query("continent=='Europe'")

# df.loc[df["pop"] < 4000000, "country"] = "Other" #herausfiltern zu kleiner Daten mit Pandas
# fig = px.pie(df, values="pop", names="country", title="Population in Europa")
df = px.data.gapminder().query("year==2007")
fig = px.sunburst(df, path=['continent', 'country'], values="pop", title='Population')
fig.show()
