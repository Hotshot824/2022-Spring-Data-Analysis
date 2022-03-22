#=====================================================================
# scatter plot, iris dataset
#=====================================================================
import plotly.express as px

df = px.data.iris()
type(df) # what operations

# 2 dim plot of data points, change the fields
fig = px.scatter(
          df,
          x="sepal_width",
          y="sepal_length",
          color="species",
)

fig.show()

#-------------------------------------------------
# scatter matrix
#-------------------------------------------------
fig = px.scatter_matrix(
          df,
          dimensions=["sepal_width", "sepal_length", "petal_width", "petal_length"],
          color="species"
          )

fig.show()

#-------------------------------------------------
# tips dataset
#-------------------------------------------------
df = px.data.tips()
  
fig = px.scatter(df,
          x='day', 
          y='total_bill',
          color='sex', # tip?
          symbol='time',
          size='tip',
)
fig.show()

#=====================================================================
#-------------------------------------------------
#-----------------------------
import plotly.express as px
df = px.data.gapminder()

fig = px.scatter(df, x="gdpPercap", y="lifeExp", animation_frame="year", animation_group="country",
           size="pop", color="continent", hover_name="country", facet_col="continent",
           log_x=True, size_max=45, range_x=[100,100000], range_y=[25,90])

fig.show()

#----------------------------------------------
import plotly.express as px
df = px.data.gapminder()

fig = px.scatter(df.query("year==2007"), x="gdpPercap", y="lifeExp", size="pop", color="continent",
           hover_name="country", log_x=True, size_max=60)
           
fig.show()

