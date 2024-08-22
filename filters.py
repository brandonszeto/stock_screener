def filter_bids(df, threshold=0):
    return df[df['bid'] > threshold]

def filter_open_interest(df, threshold=100):
    return df[df['openInterest'] > threshold]

def apply_filters(df, bid_threshold=0,
                  open_interest_threshold=100):
    df_filtered = filter_bids(df, bid_threshold)
    df_filtered = filter_open_interest(df_filtered, open_interest_threshold)
    return df_filtered
