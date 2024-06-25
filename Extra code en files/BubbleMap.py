from matplotlib import scale
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

df = pd.read_csv('BubbleMapData.csv')
groottes = [(0, 5), (5, 50), (50, 500), (500, 5000), (5000, 500000)]
colors = ["Black", "Yellow", "Red", "Green", "Blue"]

scale = 0.1

fig = go.Figure()

for i in range(len(groottes)):
    lim = groottes[i]
    df_sub = df[(df['ongelukken'] >= lim[0]) & (df['ongelukken'] < lim[1])]
    fig.add_trace(go.Scattergeo(
        locationmode='USA-states',
        lon=df_sub['lng'],
        lat=df_sub['lat'],
        text=df_sub['City'] + ': ' + df_sub['ongelukken'].astype(str) + ' ongelukken',
        mode='markers',
        marker=dict(
            size=df_sub['ongelukken'] * scale,
            color=colors[i],
            line_color='rgb(40,40,40)',
            line_width=0.5,
            sizemode='area'
        ),
        name=f'{lim[0]} - {lim[1]} ongelukken'
    ))

fig.update_layout(
    title_text='Aantal ongelukken per stad in de VS',
    showlegend=True,
    geo=dict(
        scope='usa',
        landcolor='rgb(217, 217, 217)',
    )
)

fig.show()
