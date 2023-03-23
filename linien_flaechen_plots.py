import plotly.express as px

df = px.data.gapminder().query("continent=='Europe'")
fig = px.line(df, x="year",
              y="lifeExp",
              color="country",
              line_group="country",
              hover_name="country",
              line_shape="spline",
              render_mode="svg"
              )

fig = px.area(df, x="year",
              y="pop",
              color="country",
              line_group="country",
              hover_name="country",
              line_shape="spline"
              )

fig.show()