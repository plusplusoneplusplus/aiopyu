"""
Utility methods related to TIME
"""
from datetime import datetime, timedelta
from typing import Any
import pandas as pd

def to_datetime(i : Any) -> datetime:
    """
    Parse anything into the datetime
    """
    if isinstance(i, datetime):
        return i
    elif isinstance(i, str):
        if i.lower() == 'now':
            return datetime.utcnow()

        return pd.to_datetime(i)
    else:
        assert False, f"Not supported: {i}"

def to_timedelta(i : Any) -> timedelta:
    """
    Parse anything into the timedelta
    """
    if isinstance(i, timedelta):
        return i
    elif isinstance(i, str):
        #
        # parse...
        #

        return pd.to_timedelta(i)
    else:
        assert False, f"Not supported: {i}"
