"""GA4 Data API client — OAuth-based helpers for monthly reporting."""
from typing import Optional
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    DateRange, Dimension, Metric, OrderBy, RunReportRequest,
)
from google.oauth2.credentials import Credentials

SCOPE = "https://www.googleapis.com/auth/analytics.readonly"


def make_client(client_id: str, client_secret: str, refresh_token: str) -> BetaAnalyticsDataClient:
    creds = Credentials(
        token=None,
        refresh_token=refresh_token,
        client_id=client_id,
        client_secret=client_secret,
        token_uri="https://oauth2.googleapis.com/token",
        scopes=[SCOPE],
    )
    return BetaAnalyticsDataClient(credentials=creds)


def run(
    client: BetaAnalyticsDataClient,
    property_id: str,
    start: str,
    end: str,
    dimensions: list,
    metrics: list,
    order_by: Optional[str] = None,
    limit: Optional[int] = None,
):
    """Run a GA4 report. start/end as YYYY-MM-DD."""
    order_bys = []
    if order_by:
        order_bys = [OrderBy(metric=OrderBy.MetricOrderBy(metric_name=order_by), desc=True)]
    req = RunReportRequest(
        property=f"properties/{property_id}",
        dimensions=[Dimension(name=d) for d in dimensions],
        metrics=[Metric(name=m) for m in metrics],
        date_ranges=[DateRange(start_date=start, end_date=end)],
        order_bys=order_bys,
        limit=limit,
    )
    return client.run_report(req)


def to_rows(response) -> list:
    """Flatten a GA4 response into list of dicts."""
    dims = [h.name for h in response.dimension_headers]
    mets = [h.name for h in response.metric_headers]
    out = []
    for row in response.rows:
        record = {}
        for i, d in enumerate(dims):
            record[d] = row.dimension_values[i].value
        for i, m in enumerate(mets):
            v = row.metric_values[i].value
            try:
                record[m] = float(v) if "." in v else int(v)
            except ValueError:
                record[m] = v
        out.append(record)
    return out
