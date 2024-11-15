import plotly.graph_objs as go
from plotly.offline import init_notebook_mode,iplot
init_notebook_mode(connected=True)
import chart_studio
import pandas as pd

df = pd.read_csv('2014_World_Power_Consumption')
df.head()
data = dict(type='choropleth',
            locations=df['Country'],
            colorscale='Virdis',
            reversescale=True,
            locationmode='country names',
            z = df['Power Consumption KWH'],
            text=df['Country'],
            colorbar = {'title':'Power Consumption KWH'})
layout = dict(title='2014 Power Consumption',
              geo=dict(showframe=False,projection={'type':'Mercantor'}))
choromap = go.Figure(data = [data],layout=layout)
iplot(choromap,validate=False)

#USA
usdf = pd.read_csv('2012_Election_Data')
usdf.head()
data = dict(type='choropleth',
            colorscale='Virdis',
            reversescale=True,
            locations = usdf['State Abv'],
            z = usdf['Voting-Age Population (VAP)'],
            locationmode = 'USA-states',
            text=usdf['State'],
            colorbar={'title':'Voting Age Population'})
layout = dict(title='2012 Election Data',
              geo=dict(scope='usa',showlakes=True,lakecolor='rgb(85,173,240'))
choromap = go.Figure(data=[data],layout=layout)
iplot(choromap,validate=False)