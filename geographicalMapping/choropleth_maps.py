
from chart_studio import plotly
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs,init_notebook_mode, plot,iplot
import pandas as pd
init_notebook_mode(connected=True)

data = dict(type='choropleth',
            locations=['AZ','CA','NY'],
            locationmode='USA-states',
            colorscale='Jet',
            text=['Arizona','California','New York'],
            z = [1.0,2.0,3.0],
            colorbar={'title':'Colorbar Title Goes Here'})
layout = dict(geo={'scope':'usa'})
choromap = go.Figure(data = [data],layout=layout)
iplot(choromap)
df = pd.read_csv('2011_US_AGRI_Exports')
df.head()
data = dict(type='choropleth',
            colorscale='yiorrd',
            locations=df['code'],
            locationmode='USA-states',
            z=df['total exports'],
            text=df['text'],
            marker=dict(line=dict(color='rgb(255,255,255)',width=2)),
            colorbar = {'title':'Millions USD'})
layout = dict(title='2011 US Agriculture Exports by State',
              geo = dict(scope = 'usa', showlakes= True,lakecolor='rgb(85,173,240'))
choromap2 = go.Figure(data = [data],layout=layout)
iplot(choromap2)

df = pd.read_csv('2014_World_GDP')
df.head()
data = dict(type = 'choropleth',
            locations = df['CODE'],
            z = df['GDP (BILLIONS)'],
            text = df['COUNTRY'],
            colorbar = {'title': 'GDP in Billions USD'})
layout = dict(title = '2014 Global GDP',
              geo = dict(showframe = False,
                         projection = {'type': 'Mercator'}))
choromap3 = go.Figure(data=[data],layout=layout)
iplot(choromap3)

