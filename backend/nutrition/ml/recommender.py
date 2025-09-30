import os, joblib, pandas as pd

HERE = os.path.dirname(__file__)
MODEL_PATH = os.path.join(HERE, "digestwell_model.pkl")

_BUNDLE = joblib.load(MODEL_PATH)
_PIPE = _BUNDLE["pipeline"]
_FEATURES = _BUNDLE["features"]
_CONDITION = _BUNDLE.get("condition", "IBS")

def rank_candidates(candidates_df: pd.DataFrame, banned_ids=None) -> pd.DataFrame:
    banned_ids = set(banned_ids or [])
    df = candidates_df.copy()
    if "recipe_id" in df.columns:
        df = df[~df["recipe_id"].isin(banned_ids)]
    probs = _PIPE.predict_proba(df[_FEATURES])[:, 1]
    df["suitability"] = probs
    return df.sort_values("suitability", ascending=False)

def model_info():
    return {"condition": _CONDITION, "features": _FEATURES}
