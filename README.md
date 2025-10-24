# Influencer-Marketing-Analytics-Tool-


Project overview
----------------
A tool to track and measure influencer marketing campaigns by collecting post- and account-level metrics (followers, likes, comments, shares, reach, conversions) and presenting them in an interactive dashboard so teams can evaluate ROI and identify top-performing influencers and content.

Goals
- Identify and track key influencers in a niche.
- Collect post and profile metrics on a schedule.
- Normalize and store historical metrics for trend analysis.
- Provide a dashboard with KPI views, campaign pages, and influencer comparisons.
- Produce recommendations for future influencer collaborations.

Features (starter)
- Data ingestion pipeline: fetch social metrics from APIs (or CSV/CSV exports).
- SQLite (or PostgreSQL) storage of normalized metrics and campaign metadata.
- Small ETL scripts to compute engagement rate, follower growth, conversion rate.
- Dash/Plotly web dashboard to visualize influencer performance and campaign ROI.
- Exportable CSV reports for stakeholders.

Recommended tech stack
- Language: Python 3.10+
- Data: pandas, SQLAlchemy, sqlite3 (dev) / PostgreSQL (prod)
- APIs: platform SDKs or HTTP requests (Instagram Graph API, Twitter/X API, TikTok scraping / official endpoints)
- Dashboard: Dash (Plotly) or Streamlit
- Scheduling: cron / GitHub Actions / Prefect / Airflow (for production)
- Optional: Docker for reproducible environments

Quickstart
1. Clone repo
2. Create a Python venv and install dependencies:
   - python -m venv venv
   - source venv/bin/activate
   - pip install -r requirements.txt
3. Add API credentials to a .env file (or a secure secrets manager)
4. Run the data fetch script to populate the database:
   - python src/data_pipeline/fetch_influencer_data.py
5. Start the dashboard:
   - python src/dashboard/app.py
6. Open http://localhost:8050

Data sources and permissions
- Use official platform APIs where possible (Instagram Graph API, Twitter/X, YouTube Data API, TikTok for Business).
- For platforms without accessible APIs, accept CSV exports or use approved scraping methods — always respect terms of service.
- Store API keys in environment variables or a secrets manager.

Data model (simplified)
- influencers: id, handle, platform, name, category, first_seen
- posts: id, influencer_id, platform_post_id, timestamp, text, media_type, campaign_id
- metrics_snapshot: id, post_id, followers, likes, comments, shares, reach, impressions, conversions, snapshot_time
- campaigns: id, name, start_date, end_date, budget, goal

Suggested metrics to compute
- Engagement rate = (likes + comments + shares) / followers
- Follower growth rate (period over period)
- Conversion per 1k impressions
- Cost per conversion (if spend data available)

Development tasks / milestones
- M1: Project scaffolding, README, data model, simple ETL (CSV ingest)
- M2: API connectors for 1–2 platforms, schedule ingestion
- M3: Dashboard: influencer overview, campaign overview, per-post drilldown
- M4: Analytics: cohort analysis, attribution (UTM) linking, recommendations
- M5: Deployment: Dockerize, CI, scheduled ingestion (GitHub Actions)

Contributing
- Create a branch per feature: feature/<short-description>
- Open PRs against main, add unit tests for ETL and critical functions

License
- Add a license as required (MIT recommended for teaching projects)
