import plotly.express as px

df = px.data.tips()

fig = px.histogram(df, x="total_bill", nbins=5, y="tip", color="sex")
fig.update_layout(bargap=0.1)

fig.show()