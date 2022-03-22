#=====================================================================
# bar
#=====================================================================
import plotly.express as px

df = px.data.tips()

fig = px.bar(
          df,
          x="sex",
          y="total_bill",
          color="smoker",
          barmode="group",
          )

fig.show()

#-------------------------------------------------
df = px.data.medals_long()

fig = px.bar(
          df,
          x="medal",
          y="count",
          color="nation",
          pattern_shape="nation",
          pattern_shape_sequence=[".", "x", "+"],
          )

fig.show()

#=====================================================================
#-------------------------------------------------
#-----------------------------

mport plotly.express as px
df = px.data.iris()
fig = px.parallel_coordinates(df, color="species_id", labels={"species_id": "Species",
                  "sepal_width": "Sepal Width", "sepal_length": "Sepal Length",
                  "petal_width": "Petal Width", "petal_length": "Petal Length", },
                    color_continuous_scale=px.colors.diverging.Tealrose, color_continuous_midpoint=2)
fig.show()

#====================================================================
#-----------------------------------------------


