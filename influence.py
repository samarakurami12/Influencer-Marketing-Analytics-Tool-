#!/usr/bin/env python3
"""Minimal Dash app skeleton to visualize influencer KPIs."""
import os
import sqlite3
import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

DB_PATH = os.getenv("IMAT_DB", "data/influencer_analytics.db")

def load_influencer_overview():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("""
    SELECT inf.id as influencer_id, inf.handle, inf.platform,
           ms.snapshot_time, ms.followers, ms.likes, ms.comments, ms.shares
    FROM influencers inf
    JOIN posts p ON p.influencer_id = inf.id
    JOIN metrics_snapshot ms ON ms.post_id = p.id
    """, conn)
    conn.close()
    if df.empty:
        return pd.DataFrame(columns=["influencer_id","handle","platform","snapshot_time","followers","likes","comments","shares"])
    df["snapshot_time"] = pd.to_datetime(df["snapshot_time"])
    return df

app = Dash(__name__)

app.layout = html.Div([
    html.H2("Influencer Marketing Analytics - Demo Dashboard"),
    dcc.Dropdown(id="influencer-select", options=[], placeholder="Select influencer"),
    dcc.Graph(id="followers-trend"),
    dcc.Graph(id="engagement-scatter")
])

@app.callback(Output("influencer-select", "options"), Input("influencer-select", "value"))
def set_options(_):
    df = load_influencer_overview()
    options = [{"label": f"{r['handle']} ({r['platform']})", "value": r["influencer_id"]} for _, r in df.drop_duplicates("influencer_id").iterrows()]
    return options

@app.callback(
    Output("followers-trend", "figure"),
    Output("engagement-scatter", "figure"),
    Input("influencer-select", "value")
)
def update_charts(influencer_id):
    df = load_influencer_overview()
    if influencer_id is None or df.empty:
        return px.line(title="Followers Over Time"), px.scatter(title="Engagement")
    sel = df[df["influencer_id"] == influencer_id].sort_values("snapshot_time")
    followers_fig = px.line(sel, x="snapshot_time", y="followers", title="Followers Over Time")
    sel = sel.assign(engagement = (sel["likes"] + sel["comments"] + sel["shares"]) / sel["followers"])
    engagement_fig = px.scatter(sel, x="snapshot_time", y="engagement", title="Engagement Rate over Time", size="likes")
    return followers_fig, engagement_fig

if __name__ == "__main__":
    app.run_server(debug=True)
