# Roadmap & Suggested Issues

Milestone 1 — Foundation
- Create project scaffolding (README, requirements, .gitignore)  -> DONE (starter files)
- Define simplified data model -> DONE (see README)
- Implement CSV ingest pipeline (ETL) -> issue: "Add CSV ingest ETL"

Milestone 2 — Connectors
- Implement Instagram Graph API connector -> issue: "Implement Instagram API connector"
- Implement Twitter/X connector -> issue: "Implement Twitter/X connector"
- Add unit tests for connectors -> issue: "Add tests for API connectors"

Milestone 3 — Dashboard
- Build influencer overview page -> issue: "Dashboard: influencer overview"
- Add campaign comparison page -> issue: "Dashboard: campaign comparison"
- Add export CSV functionality -> issue: "Dashboard: export CSV reports"

Milestone 4 — Analytics & Recommendations
- Compute ROI per influencer (link spend -> conversions) -> issue: "Add ROI calculation"
- Content resonance analysis by post type and hour -> issue: "Content resonance analysis"
- Recommend top influencers per KPI -> issue: "Top influencer recommendation engine"

Milestone 5 — Production & Deployment
- Dockerize application -> issue: "Add Dockerfile and compose"
- Schedule ingestion (GitHub Actions) -> issue: "Schedule data ingestion via GitHub Actions"
- Configure PostgreSQL for production -> issue: "Migrate DB to Postgres"

Example issues (titles)
- "Add CSV ingest ETL"
- "Implement Instagram API connector"
- "Dashboard: influencer overview"
- "Add ROI calculation"
- "Add Dockerfile and compose"

Owners / Suggested assignees
- Data pipeline: @data-eng
- Dashboard: @frontend-dev
- Analytics: @data-scientist