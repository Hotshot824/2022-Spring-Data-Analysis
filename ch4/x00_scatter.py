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
