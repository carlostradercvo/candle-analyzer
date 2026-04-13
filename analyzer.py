def analyze(df, min_confidence=0.9):
    results = []

    grouped = df.groupby('hour_min')

    for time, group in grouped:
        total = len(group)

        green_count = len(group[group['color'] == 'green'])
        red_count = len(group[group['color'] == 'red'])

        green_pct = green_count / total
        red_pct = red_count / total

        if green_pct >= min_confidence:
            results.append({
                'time': time,
                'direction': 'CALL',
                'confidence': round(green_pct * 100, 2),
                'samples': total
            })

        elif red_pct >= min_confidence:
            results.append({
                'time': time,
                'direction': 'PUT',
                'confidence': round(red_pct * 100, 2),
                'samples': total
            })

    return sorted(results, key=lambda x: x['confidence'], reverse=True)
