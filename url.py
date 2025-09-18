# file: rest_api_to_excel.py
import requests
import pandas as pd

def fetch_json_and_save(api_url, excel_path='api_data.xlsx', params=None, headers=None):
    resp = requests.get(api_url, params=params, headers=headers, timeout=10)
    resp.raise_for_status()
    data = resp.json()  # usually returns list/dict

    # If API returns a list of objects (typical), convert to DataFrame directly:
    if isinstance(data, list):
        df = pd.DataFrame(data)
    elif isinstance(data, dict):
        # Many APIs return {'data': [...]} style responses
        if 'data' in data and isinstance(data['data'], list):
            df = pd.DataFrame(data['data'])
        else:
            # fallback: put the dict into single-row DataFrame
            df = pd.DataFrame([data])
    else:
        raise RuntimeError("Unexpected JSON structure")

    # Optional: select/reorder columns, clean nested columns, flatten JSON fields, etc.
    # Example: flatten nested dicts (simple one-level flatten)
    def flatten_df(dframe):
        # expand any columns where entries are dicts
        dict_cols = [c for c in dframe.columns if dframe[c].apply(lambda x: isinstance(x, dict)).any()]
        for col in dict_cols:
            expanded = pd.json_normalize(dframe[col]).add_prefix(col + '.')
            dframe = pd.concat([dframe.drop(columns=[col]), expanded], axis=1)
        return dframe

    df = flatten_df(df)
    df.to_excel(excel_path, index=False)
    print(f"Wrote API data to {excel_path}")

if __name__ == '__main__':
    api_url = 'https://jsonplaceholder.typicode.com/posts'  # example public API
    fetch_json_and_save(api_url, excel_path='api_posts.xlsx')
