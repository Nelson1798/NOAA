"""Extract One Acre Fund Malawi 2023/24 farms (GROW-Africa) near the notebook's Lilongwe point.
Ships only planting date, yield and distance (km, rounded) -- no coordinates, no IDs."""
import sys
import numpy as np, pandas as pd
src, out = sys.argv[1], sys.argv[2]
d = pd.read_parquet(src)
col = [c for c in d.columns if "source" in c.lower()][0]
o = d[d[col].astype(str).str.contains("acre|oaf", case=False) & d.country.eq("Malawi")
      & d.plant_date.notna() & d.yield_t_ha.notna() & d.lat.notna() & d.lon.notna()].copy()
o["planting_date"] = pd.to_datetime(o.plant_date)
lat, lon = -13.98, 33.78          # locations.csv requested location, "Lilongwe area"
p1, p2, dl = np.radians(lat), np.radians(o.lat), np.radians(o.lon - lon)   # haversine, km
o["distance_km"] = 2 * 6371 * np.arcsin(np.sqrt(np.sin((p2 - p1) / 2) ** 2 + np.cos(p1) * np.cos(p2) * np.sin(dl / 2) ** 2))
x = o[o.planting_date.between("2023-09-01", "2024-02-29") & o.distance_km.le(100)].copy()   # filter unrounded
x["distance_km"] = x.distance_km.round(1)
x = x[["planting_date", "yield_t_ha", "distance_km"]].sort_values(["planting_date", "distance_km", "yield_t_ha"])
x["yield_t_ha"] = x.yield_t_ha.round(2)
x.to_csv(out, index=False, date_format="%Y-%m-%d")
print(len(x), "farms;", int(x.distance_km.le(50).sum()), "within 50 km; min", x.distance_km.min(), "km ->", out)
