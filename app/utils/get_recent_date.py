from datetime import date, timedelta

def get_recent_date(day: int, last_week: bool = False) -> str:
    target_date = date.today()
    while target_date.weekday() != day:
        target_date = target_date - timedelta(days=1)
    if last_week:
        target_date = target_date - timedelta(days=7)

    return target_date.strftime("%Y%m%d")
