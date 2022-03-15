import plotly.express as px

df = px.data.iris()

fig = px.scatter(
          df,
          x="sepal_length",
          y="sepal_width",
          color="species",
)

fig.show()

fig = px.line(
          df,
          x="sepal_length",
          y="sepal_width",
          color="species",
)
fig.show()


df = px.data.gapminder()

fig = px.line(
          df.query("continent=='Oceania'"),
          #df,
          x="year",
          y="lifeExp", 
          color="country",
          #line_group="country",
          #line_shape="spline",
          #render_mode="svg",
)

fig.show()

fig = px.scatter(
          df.query("continent=='Oceania'"),
          #df,
          x="year",
          y="lifeExp", 
          color="country",
          #line_group="country",
          #line_shape="spline",
          #render_mode="svg",
)

fig.show()