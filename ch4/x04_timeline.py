#=====================================================================
# timeline
#=====================================================================
import plotly.express as px
import pandas as pd

# dataframe formed from a list of dict
df = pd.DataFrame([
     dict(Task="Job A", Start='2021-09-01', Finish='2021-10-28'),
     dict(Task="Job B", Start='2021-08-05', Finish='2021-10-15'),
     dict(Task="Job C", Start='2021-09-05', Finish='2021-11-15'),
     dict(Task="Job D", Start='2021-08-05', Finish='2021-12-15'),
     dict(Task="Job E", Start='2021-09-20', Finish='2021-11-30')])

fig = px.timeline(
          df,
          x_start='Start',
          x_end='Finish',
          y='Task',
          )

fig.show()

#-------------------------------------------------
df = pd.DataFrame([
     dict(Task="Job A", Start='2021-09-01', Finish='2021-10-28', Resource="Alice"),
     dict(Task="Job B", Start='2021-08-05', Finish='2021-10-15', Resource="Ron"  ),
     dict(Task="Job C", Start='2021-09-05', Finish='2021-11-15', Resource="Ron"  ),
     dict(Task="Job D", Start='2021-08-05', Finish='2021-12-15', Resource="Ron"  ),
     dict(Task="Job E", Start='2021-09-20', Finish='2021-11-30', Resource="Alice")])

fig = px.timeline(
          df,
          x_start="Start",
          x_end="Finish",
          y="Task",
          color = "Resource",
          template = "gridon",
          )

fig.show()

#=====================================================================
#-------------------------------------------------
#-----------------------------

