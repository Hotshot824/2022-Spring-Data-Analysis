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

