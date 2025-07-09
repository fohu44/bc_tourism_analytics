import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

# --- Load & prepare data ---
df = (
    pd.read_csv('monthly_tourism_cleaned.csv', parse_dates=['period'])
      .set_index('period')
      .asfreq('MS')
      .fillna(0)
)

# --- Metric labels ---
traveller_metric_labels = {
    'overnight':      'Overnight Visitors',
    'same_day':       'Same-Day Visitors',
    'overseas_total': 'Total Overseas Visitors',
    'asia':           'Visitors from Asia',
    'europe':         'Visitors from Europe',
    'other':          'Visitors from Other Regions'
}
food_metric_labels = {
    'bc_food_services':  'BC Food Services',
    'bc_drinking_places':'BC Drinking Places',
    'ca_food_services':  'Canada Food Services',
    'ca_drinking_places':'Canada Drinking Places'
}
transport_metric_labels = {
    'air_vancouver_domestic':     'Vancouver Air ‑ Domestic',
    'air_vancouver_trans_border': 'Vancouver Air ‑ Trans-border',
    'air_vancouver_other_int':    'Vancouver Air ‑ Other Int’l',
    'victoria_total':             'Victoria Air Traffic',
    'bc_ferries_vehicles':        'BC Ferries ‑ Vehicles',
    'bc_ferries_passengers':      'BC Ferries ‑ Passengers'
}
other_metric_labels = {
    'employement_air_transport':            'Employment: Air Transport',
    'employement_accomodation':            'Employment: Accommodation',
    'employement_food_and_beverage':       'Employment: Food & Beverage',
    'employement_art_entertainment_recreation': 'Employment: Arts & Rec',
    'hotel_occupancy_rate':                'Hotel Occupancy Rate',
    'hotel_room_rate':                     'Hotel Room Rate',
    'hotel_room_revenue':                  'Hotel Room Revenue',
    'cpi_traveller_accomodation':          'CPI: Traveller Accommodation',
    'cpi_restaurant_meals':                'CPI: Restaurant Meals'
}
all_metric_labels = {
    **traveller_metric_labels,
    **food_metric_labels,
    **transport_metric_labels,
    **other_metric_labels
}

# --- Event annotations data ---
# --- Event annotations data ---
events = [
    { 'label': '9/11 Attacks',
      'start': '2001-09-01', 'end': '2001-12-01',
      'color': 'gray' },

    { 'label': 'SARS Outbreak',
      'start': '2002-11-01', 'end': '2003-07-01',
      'color': 'lightpink' },

    { 'label': 'Global Financial Crisis',
      'start': '2008-09-01', 'end': '2009-12-01',
      'color': 'lightblue' },

    { 'label': 'Vancouver Olympics 2010',
      'start': '2010-02-12', 'end': '2010-02-28',
      'color': 'mediumblue' },

    { 'label': 'Canada 150 Celebrations',
      'start': '2017-01-01', 'end': '2017-12-31',
      'color': 'gold' },

    { 'label': 'BC Wildfires 2017',
      'start': '2017-07-01', 'end': '2017-09-30',
      'color': 'orange' },

    { 'label': 'COVID-19 Pandemic',
      'start': '2020-03-01', 'end': '2022-06-01',
      'color': 'lightcoral' },

    { 'label': 'BC Wildfires 2021',
      'start': '2021-07-01', 'end': '2021-09-01',
      'color': 'darkorange' },

    { 'label': 'BC Wildfires 2023',
      'start': '2023-06-01', 'end': '2023-09-30',
      'color': 'red' }
]
df_events = pd.DataFrame(events)

# --- Dropdown options ---
years = sorted(df.index.year.unique())
year_options = [{'label': str(y), 'value': y} for y in years]
date_options = [{'label': dt.strftime('%b %Y'), 'value': dt.strftime('%Y-%m-%d')} for dt in df.index]

# --- Dash setup ---
app = dash.Dash(__name__, suppress_callback_exceptions=True)
server = app.server

# --- Layout ---
app.layout = html.Div([
    html.H1("BC Tourism Dashboard", style={'textAlign': 'center'}),

    html.Div([
        html.Label("Display Mode:"),
        dcc.RadioItems(
            id='mode-selector',
            options=[
                {'label': 'Compare Years', 'value': 'year'},
                {'label': 'Select Date Range', 'value': 'range'}
            ],
            value='year',
            inline=True
        )
    ], style={'textAlign': 'center', 'padding': '10px'}),

    html.Div([
        html.Div([
            html.Label("Base Year:"),
            dcc.Dropdown(id='year1', options=year_options,
                         value=years[-1], clearable=False),
            html.Label("Compare Year 2 (optional):", style={'marginTop':'10px'}),
            dcc.Dropdown(id='year2', options=year_options,
                         value=None, clearable=True, placeholder="(none)"),
            html.Label("Compare Year 3 (optional):", style={'marginTop':'10px'}),
            dcc.Dropdown(id='year3', options=year_options,
                         value=None, clearable=True, placeholder="(none)")
        ], id='year-inputs', style={'width': '300px', 'margin': 'auto'}),

        html.Div([
            html.Label("Start Period:"),
            dcc.Dropdown(id='start-period', options=date_options,
                         value=date_options[0]['value'], clearable=False),
            html.Label("End Period:", style={'marginTop':'10px'}),
            dcc.Dropdown(id='end-period', options=date_options,
                         value=date_options[-1]['value'], clearable=False)
        ], id='range-inputs', style={'width': '300px', 'margin': 'auto', 'display': 'none'})
    ]),

    html.Div([
        html.Label("Select Metrics:"),
        dcc.Dropdown(
            id='selected_metrics',
            options=[{'label': lbl, 'value': key} for key, lbl in all_metric_labels.items()],
            multi=True,
            value=[list(all_metric_labels.keys())[0]],
            placeholder="Pick one or more metrics..."
        )
    ], style={'width': '60%', 'margin': '20px auto'}),

    dcc.Graph(id='line-chart'),
    dcc.Graph(id='bar-chart'),

    html.H2("Advanced Analytics", style={'textAlign': 'center', 'marginTop': '40px'}),
    dcc.Checklist(
        id='adv-chart-selector',
        options=[
            {'label': 'Horizon Chart', 'value': 'horizon'},
            {'label': 'Stacked Area Chart', 'value': 'stacked_area'},
            {'label': 'Event Annotations', 'value': 'annotations'}
        ],
        value=[],
        inline=True,
        style={'textAlign': 'center', 'marginBottom': '20px'}
    ),
    html.Div(id="horizon-container"),
    html.Div(id="stacked-area-container"),
    html.Div(id="annotations-container")
])

# --- Callbacks ---
@app.callback(
    Output('year-inputs', 'style'),
    Output('range-inputs', 'style'),
    Input('mode-selector', 'value')
)
def toggle_inputs(mode):
    if mode == 'year':
        return {'display': 'block', 'margin': 'auto'}, {'display': 'none'}
    return {'display': 'none'}, {'display': 'block', 'margin': 'auto'}

@app.callback(
    Output('line-chart', 'figure'),
    Output('bar-chart', 'figure'),
    Input('mode-selector', 'value'),
    Input('year1', 'value'),
    Input('year2', 'value'),
    Input('year3', 'value'),
    Input('start-period', 'value'),
    Input('end-period', 'value'),
    Input('selected_metrics', 'value')
)
def update_core(mode, y1, y2, y3, start, end, metrics):
    if not metrics:
        return go.Figure(), go.Figure()

    if mode == 'year':
        yrs = [y1] + [y for y in (y2, y3) if y]
        tmp = df.reset_index()
        tmp['Year'] = tmp['period'].dt.year
        tmp['Month'] = tmp['period'].dt.strftime('%b')
        sel = tmp[tmp['Year'].isin(yrs)][['Year', 'Month'] + metrics]
        long_df = sel.melt(['Year', 'Month'], metrics, 'Metric', 'Value')
        long_df['Metric'] = long_df['Metric'].map(all_metric_labels)

        line_fig = px.line(long_df, x='Month', y='Value', color='Year', line_dash='Metric', markers=True,
                           title="Year-to-Year Comparison")
        line_fig.update_layout(template='plotly_white')

        bar_fig = px.bar(long_df, x='Month', y='Value', color='Metric', pattern_shape='Year',
                         barmode='group', pattern_shape_sequence=['', '/', '\\', 'x'],
                         title="Monthly Metrics Comparison")
        bar_fig.update_layout(template='plotly_white', legend_title_text="", legend=dict(itemsizing='constant'))

    else:
        start_dt, end_dt = pd.to_datetime(start), pd.to_datetime(end)
        sub = df.loc[start_dt:end_dt].reset_index().rename(columns={'period': 'Date'})
        sel = sub[['Date'] + metrics]
        long_df = sel.melt(['Date'], metrics, 'Metric', 'Value')
        long_df['Metric'] = long_df['Metric'].map(all_metric_labels)

        line_fig = px.line(long_df, x='Date', y='Value', color='Metric', markers=True,
                           title="Time-Series Over Selected Range")
        line_fig.update_layout(template='plotly_white')

        agg = long_df.groupby('Metric')['Value'].sum
        agg = long_df.groupby('Metric')['Value'].sum().reset_index()
        bar_fig = px.bar(
            agg, x='Metric', y='Value',
            color='Metric', barmode='group',
            title="Aggregate Metrics Over Range"
        )
        bar_fig.update_layout(template='plotly_white', legend_title_text='Metric')

    return line_fig, bar_fig

# --- Advanced Analytics with Fully Synced Time Windows ---
@app.callback(
    Output("horizon-container",     "children"),
    Output("stacked-area-container","children"),
    Output("annotations-container", "children"),
    Input("adv-chart-selector",     "value"),
    Input("mode-selector",          "value"),
    Input("year1",                  "value"),
    Input("year2",                  "value"),
    Input("year3",                  "value"),
    Input("start-period",           "value"),
    Input("end-period",             "value"),
    Input("selected_metrics",       "value")
)
def render_advanced(chosen, mode, y1, y2, y3, start, end, metrics):
    horizon = stacked = ann = None

    # Filter data based on selected time window
    if mode == 'year':
        yrs = [y for y in [y1, y2, y3] if y]
        tmp = df.reset_index()
        tmp['Year'] = tmp['period'].dt.year
        tmp = tmp[tmp['Year'].isin(yrs)]
        window_df = tmp.set_index('period')
    else:
        start_dt = pd.to_datetime(start)
        end_dt   = pd.to_datetime(end)
        window_df = df.loc[start_dt:end_dt]

    # Horizon Chart
    if 'horizon' in chosen and metrics:
        m = metrics[0]
        s = window_df[m]
        levels = [s.quantile(q) for q in (.33, .66, 1)]
        fig = go.Figure()
        colors = ['#d0e1f9', '#74a9cf', '#0570b0']
        for i, th in enumerate(levels):
            band = s.clip(upper=th)
            if i > 0:
                band -= levels[i - 1]
            fig.add_bar(x=s.index, y=band, marker_color=colors[i], name=f"Band {i + 1}")
        fig.update_layout(
            barmode='stack',
            title=f"Horizon Chart: {all_metric_labels[m]}",
            yaxis=dict(visible=False),
            template='plotly_white'
        )
        horizon = dcc.Graph(figure=fig)

    # Stacked Area Chart
    if 'stacked_area' in chosen and metrics:
        melt = window_df.reset_index().melt(
            id_vars=['period'], value_vars=metrics,
            var_name='Metric', value_name='Value'
        )
        melt['Metric'] = melt['Metric'].map(all_metric_labels)
        fig2 = px.area(
            melt, x='period', y='Value', color='Metric',
            title="Stacked Area Chart: Selected Metrics Over Time",
            labels={'period': 'Date', 'Value': 'Value'}
        )
        fig2.update_layout(template='plotly_white')
        stacked = dcc.Graph(figure=fig2)

    # Event Annotation Timeline
    if 'annotations' in chosen:
        ev = df_events.copy()
        ev['start'] = pd.to_datetime(ev['start'])
        ev['end']   = pd.to_datetime(ev['end'])

        window_start = window_df.index.min()
        window_end   = window_df.index.max()
        ev = ev[(ev['start'] <= window_end) & (ev['end'] >= window_start)]

        if ev.empty:
            ann = html.Div(
                "No events in this range",
                style={'textAlign': 'center', 'color': 'gray', 'marginTop': '20px'}
            )
        else:
            fig3 = px.timeline(
                ev, x_start='start', x_end='end', y='label',
                color='label',
                color_discrete_map={e['label']: e['color'] for e in events}
            )
            fig3.update_yaxes(autorange='reversed', visible=False)
            fig3.update_layout(
                title="Event Annotation Timeline",
                xaxis_title="Date",
                margin={'l': 0, 'r': 0, 't': 40, 'b': 0},
                template='plotly_white'
            )
            ann = dcc.Graph(figure=fig3)

    return horizon, stacked, ann

# --- Run Locally ---
if __name__ == '__main__':
    app.run(debug=True)
