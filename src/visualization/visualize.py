"""
visualize
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def pretty_describe(df: pd.DataFrame) -> pd.DataFrame:
    """Pretty describe a DataFrame

    Args:
        df: DataFrame

    Returns:
        Description in a DataFrame format
    """
    return pd.DataFrame(df.describe(percentiles=[.10, .25, .5, .75, .90]).T)\
        .applymap("{0:,.3f}".format)
