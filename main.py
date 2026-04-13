from data_loader import load_data
from analyzer import analyze
from config import MIN_CONFIDENCE

def main():
    file_path = "data.csv"

    df = load_data(file_path)

    results = analyze(df, MIN_CONFIDENCE)

    print("\n📊 HORÁRIOS COM PADRÃO FORTE:\n")

    for r in results:
        print(f"{r['time']} -> {r['direction']} | {r['confidence']}% | {r['samples']} velas")

if __name__ == "__main__":
    main()
