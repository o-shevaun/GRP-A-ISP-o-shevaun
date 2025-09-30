import json, pandas as pd
from django.http import JsonResponse, HttpResponseBadRequest
from .ml.recommender import rank_candidates, model_info

def score_recipes(request):
    if request.method != "POST":
        return HttpResponseBadRequest("POST JSON only")
    try:
        payload = json.loads(request.body.decode("utf-8"))
    except Exception:
        return HttpResponseBadRequest("Invalid JSON")
    cand = payload.get("candidates", [])
    if not cand:
        return HttpResponseBadRequest("Missing candidates")
    df = pd.DataFrame(cand)
    ranked = rank_candidates(df, banned_ids=payload.get("banned_ids", []))
    return JsonResponse({"model": model_info(), "results": ranked.to_dict(orient="records")})
