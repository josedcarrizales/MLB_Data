from mlb_api.pipelines.awards import fetch_awards

if __name__ == "__main__":
    df = fetch_awards()
    print(df)