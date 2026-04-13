import pandas as pd

def load_data(path):
    df = pd.read_csv(path)

    df['time'] = pd.to_datetime(df['time'])
    df['hour_min'] = df['time'].dt.strftime('%H:%M')

    df['color'] = df.apply(lambda row: 'green' if row['close'] > row['open'] else 'red', axis=1)

    return df
