# Madagascar Preparation Notes

Branch: `madagascar-work` (kept separate from `main` so the East Africa
configuration is untouched; merge only after review).

All four notebooks keep their existing workflow and country dropdown. On this
branch, **Madagascar is the default country**, and every country-keyed lookup
(bounding boxes, capitals, events, heat-event window) has a Madagascar entry.
The other countries still behave exactly as on `main`.

## 1. Selected date ranges

| Notebook | Period | Why |
|---|---|---|
| 01 Ground QC, 02 Rainfall Skill Explorer | **2021-07-01 → 2023-06-30** | Two full austral hydrological years (Jul–Jun) |
| 02 Case studies | Event windows (below) | Inside the main period |
| 03 Temperature & PET | **2023-10-01 → 2023-10-31** (product comparison window **2023-10-10 → 2023-10-14**) | October 2023 heatwave |
| 03 Step 7 / 04 AEZ long-term | Unchanged (ERA5 monthly LT_START–LT_END) | Climatology, not event driven |

### Reasoning

The Ethiopia work used a calendar-year window (2022-01-01 → 2023-12-31) built
around a JJAS/kiremt flash flood. That doesn't carry over to Madagascar:

* Madagascar has a **single austral rainy season, November to April**, with the
  cyclone peak in January to March. A January start would cut the 2021/22 season
  in half (missing its November–December onset), and a December end would leave
  the 2023/24 season incomplete. A July–June window keeps every season whole and
  starts and ends in the dry season.
* The two seasons chosen are the most event-dense in recent Malagasy records.
  Every rainfall case study below falls inside them.
* The window is 730 days long, the same as the Ethiopia window, so compute cost
  and the pentad count for skill scoring are comparable. GHCN downloads cover three
  calendar years (2021–2023) instead of two.

Notebook 02 still adopts Notebook 1's dates automatically
(`Resolved_Ground_Source.json`). Both now default to the same window.

## 2. Events investigated

### Rainfall and floods (Notebook 02 `EVENTS`, 30 km radius)

| Event | Peak date | Window | Point | Evidence |
|---|---|---|---|---|
| **Cyclone Batsirai** (primary case study) | 2022-02-05 | 02-02 → 02-09 | Mananjary (-21.23, 48.34) | Cat-3-equivalent landfall ~14 km from Mananjary, 165 km/h sustained; ≥120 deaths; ~6,000 buildings flooded ([WMO](https://wmo.int/node/14603), [NASA EO](https://earthobservatory.nasa.gov/images/149454/cyclone-batsirai-floods-madagascar)) |
| Antananarivo floods / TS Ana | 2022-01-18 | 01-15 → 01-25 | Antananarivo (-18.88, 47.51) | Up to 226 mm overnight 17–18 Jan; 34 deaths in the capital, 41 in Madagascar from Ana ([summary](https://en.wikipedia.org/wiki/2022_Antananarivo_floods)) |
| Cyclone Emnati | 2022-02-22 | 02-19 → 02-26 | Manakara (-22.15, 48.00) | Landfall Manakara Atsimo, 135 km/h; fifth system in six weeks ([NASA EO](https://earthobservatory.nasa.gov/images/149494/storm-ravaged-madagascar-faces-another-storm), [ReliefWeb](https://reliefweb.int/disaster/tc-2022-000175-mdg)) |
| Cyclone Freddy (1st landfall) | 2023-02-21 | 02-18 → 02-25 | Mananjary (-21.23, 48.34) | Landfall north of Mananjary, 150 km/h; passed the SE coast again 5 Mar 2023 ([WMO](https://wmo.int/node/21162)) |

Also noted but **not configured as a case study**: Cyclone Cheneso (landfall
19 Jan 2023, then stalled off the west coast with torrential rain; 33 deaths).
Its rain was spread along the west coast rather than at one point, so it doesn't
suit the notebook's single point and 30 km radius design.

### Heat (Notebook 03 `HEAT_EVENTS`)

**October 2023 heatwave.** It was the warmest month in Madagascar since 1950,
with temperatures normally only reached in December–January. The hottest 7-day
Tmax ran 10–16 Oct and the hottest 7-day Tmin 13–19 Oct, centred on the
Antananarivo highlands ([World Weather Attribution](https://www.worldweatherattribution.org/?p=2314)).
This replaces the East African March 2024 heatwave for Madagascar only: the
notebook picks it via `HEAT_EVENTS[Country]`, and every other country still uses
March 2024. The 5-day CBAM/ERA5 comparison window (10–14 Oct) sits inside the
peak Tmax week.

## 3. Datasets

Same products as the Ethiopia workflow, no new sources:

* **Ground:** TAHMO (default, unchanged), GHCN-Daily, or custom national
  (Direction Générale de la Météorologie) CSVs.
* **Satellite / reanalysis:** CHIRPS pentad, TAMSAT (PERSIANN-CDR fallback), IMERG,
  ERA5-Land (rainfall); ERA5 / ERA5-Land and CBAM (temperature, PET).
* **Region:** OSM Nominatim country polygon (Notebook 01 keeps the largest ring,
  i.e. the main island) and bbox `[43.0, -25.7, 50.6, -11.9]` (Notebooks 02–04).

GHCN coverage was checked against NOAA's public archive: 25 Madagascar stations
fall in the bbox. The best have 200–550 PRCP days out of 730 in the window
(Toamasina 548, Sainte Marie 425, Fascene/Nosy Be 357, Taolagnaro 334,
Sambava 297, Fianarantsoa 289, Antananarivo/Ivato 257). 8 have none.
About 10 stations have Oct 2023 TMAX/TAVG.

## 4. Assumptions and limitations

* **TAHMO coverage in Madagascar was not verified.** If Step 4a of Notebook 01
  reports 0 stations, set `Ground_data_source = "GHCN"` (or `"custom"`), as the
  notebook itself prompts.
* **GHCN is patchy** (see above). Expect lower pentad completeness and fewer
  "High confidence" stations than in Kenya. National DGM data via the `custom`
  path would strengthen the analysis considerably.
* **Mayotte station** `MFM00067005` (French territory) falls inside the
  Madagascar bbox. Notebook 01 excludes it (polygon filter), but Notebook 02's
  bbox-based GHCN comparison will include it.
* **The bbox is mostly ocean.** CHIRPS is land-only. IMERG/ERA5 ocean pixels sit
  far from any station, so they don't affect station scoring but do appear in maps.
* **Cyclone rainfall:** cyclone rain bands are tight, so 30 km event-radius totals
  are sensitive to the exact landfall point.
* **Heat-stress threshold** (Tmax > 32 °C) was kept from the East Africa setup.
  It is rarely exceeded on the Antananarivo highlands (~1,300 m), so stress maps
  will mainly highlight the west and south-west lowlands.
* **CBAM coverage of Madagascar** isn't documented here. Notebook 03 already falls
  back to ERA5 if the CBAM fetch returns nothing.
* **Notebook 04** was empty on `main`, so the populated version from
  `tahmo-work` was brought onto this branch before adding Madagascar. Its crop
  list is unchanged. Rice, the national staple, may need adding or checking.
* **Saved cell outputs** in the notebooks are from earlier (Kenya) runs. Re-run
  in Colab to regenerate Madagascar outputs; cached files are written under
  `Datasets/Madagascar/` on the Shared Drive.
