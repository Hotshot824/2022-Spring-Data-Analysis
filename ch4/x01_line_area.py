#=====================================================================
# line
#=====================================================================
#-------------------------------------------------
import plotly.express as px

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

#=====================================================================
# area
#=====================================================================
import plotly.express as px

df = px.data.gapminder()

fig = px.area(
          #df.query("continent=='Africa'"),
          df,
          x="year",
          y="pop",
          color="continent",
          line_group="country",
)

fig.show()

#-------------------------------------------------


#=====================================================================
#-------------------------------------------------
#-----------------------------

