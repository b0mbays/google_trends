from pytrends.request import TrendReq
from typing import List

def get_top_trends(country_code: str, count: int = 5) -> List[str]:
    pytrends = TrendReq(hl='en-GB', tz=360)
    trending_searches_df = pytrends.trending_searches(pn=country_code)
    return trending_searches_df.head(count)[0].tolist()