import pandas as pd
import mplfinance as mpf

# Sample candle data with 26 data points
data = {
    'Date': [
        '2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04', '2022-01-05', '2022-01-06',
        '2022-01-07', '2022-01-08', '2022-01-09', '2022-01-10', '2022-01-11', '2022-01-12',
        '2022-01-13', '2022-01-14', '2022-01-15', '2022-01-16', '2022-01-17', '2022-01-18',
        '2022-01-19', '2022-01-20', '2022-01-21', '2022-01-22', '2022-01-23', '2022-01-24',
        '2022-01-25', '2022-01-26'
    ],
    'Open': [
        101, 100, 102, 103, 105, 108,110, 108, 111, 112, 115, 118,120, 118, 122, 124, 125, 122,128, 126, 130, 129, 132, 134,136, 135
    ],
    'Close': [
        100, 98, 103, 106, 108, 107,109, 110, 114, 116, 118, 119,117, 121, 123, 125, 124, 127,130, 128, 133, 131, 133, 135,137, 136
    ],
    'High': [
        105, 108, 104, 108, 110, 110,112, 112, 115, 118, 120, 122,121, 125, 127, 128, 126, 129,134, 132, 137, 135, 137, 140,141, 139
    ],
    'Low': [
        99, 96, 101, 98, 105, 106,107, 109, 112, 113, 116, 117,116, 120, 122, 124, 123, 126,129, 127, 132, 130, 132, 134,136, 135
    ]
}

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)  # Set 'Date' as the index

# Function to detect the specified candle patterns
def detect_candle_patterns(df):
    patterns = []
    for i in range(1, len(df)):
        if (df['Close'][i - 1] == df['Open'][i]) and (df['Open'][i - 1] > df['Close'][i - 1]) and (df['Open'][i] > df['Close'][i]):
            patterns.append((df.index[i], "Case 1"))
        elif (df['Close'][i - 1] == df['Open'][i]) and (df['Close'][i] > df['Open'][i]) and (df['Close'][i - 1] > df['Open'][i - 1]):
            patterns.append((df.index[i], "Case 2"))
    print(patterns)
    return patterns

candle_patterns = detect_candle_patterns(df)

# Convert the patterns to a list of dictionaries
pattern_data = [{'date': date, 'pattern': pattern} for date, pattern in candle_patterns]

# Create a custom axis
apd = mpf.make_addplot(df[['Open', 'Close', 'High', 'Low']], type='candle')

# Visualize the candlestick chart with matched patterns using mplfinance
mpf.plot(df, type='candle', style='yahoo', title='Candlestick Chart with Matched Patterns', addplot=apd)
