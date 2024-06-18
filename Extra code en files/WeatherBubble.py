from matplotlib import scale
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

df = pd.read_csv('WeatherBubbleData.csv')

grootte = [(0,0.30),(0.30,0.35),(0.35,0.40),(0.40,0.45),(0.45,0.50),(0.50,1)]
color_scale = px.colors.diverging.Tealrose

def assign_size(score):
    for i, (min_range, max_range) in enumerate(grootte):
        if min_range <= score < max_range:
            return (i + 1) * 10  # Adjust multiplier for desired bubble sizes
    return 10  # Default size

# Create hover text
hover_text = []
for index, row in df.iterrows():
    hover_text.append(f"City: {row['city']}<br>Score: {row['score']}")

# Create figure
fig = go.Figure()

# Add scattergeo trace
fig.add_trace(go.Scattergeo(
    locationmode='USA-states',
    lon=df['lng'],
    lat=df['lat'],
    mode='markers',
    marker=dict(
        size=[assign_size(score) for score in df['score']],  # Assign size based on score
        color=df['score'],  # Assign color based on score
        colorscale=color_scale,  # Set colorscale
        colorbar=dict(title='Weather Score'),  # Colorbar title
        line_color='rgb(40, 40, 40)',
        line_width=0.5,
        sizemode='diameter',  # Use diameter for bubble sizes
        opacity=0.8
    ),
    text=hover_text,  # Hover text
    hoverinfo='text',  # Show only text on hover
))

# Update layout
fig.update_layout(
    title='Weather score per grote stad in Amerika',
    geo=dict(
        scope='usa',
        landcolor='rgb(217, 217, 217)',
    )
)

# Show plot
fig.show()