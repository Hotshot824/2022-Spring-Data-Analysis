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
import plotly.express as px

df = px.data.tips()

fig = px.parallel_categories(df, color="size", color_continuous_scale=px.colors.sequential.Inferno)

fig.show()

#=====================================================================
import plotly.express as px

df = px.data.gapminder()

fig = px.scatter(df.query("year==2007"), x="gdpPercap", y="lifeExp", size="pop", color="continent",
           hover_name="country", log_x=True, size_max=60)

fig.show()
#=====================================================================
#-------------------------------------------------------------


