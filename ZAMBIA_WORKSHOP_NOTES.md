# Zambia Workshop Preparation Notes (24–29 Nov)

Branch: `zambia-workshop`, created from `main`. The East Africa configuration on
`main` is untouched.

Countries: the participating NMHSs, **Zambia (host), Angola, Botswana, Kenya,
Malawi, Mozambique, Nigeria, Rwanda, Tanzania and Zimbabwe**. All four
notebooks keep their existing workflow; the dropdowns list these ten countries
and default to **Zimbabwe**.

Zambia, Angola, Kenya, Tanzania, Rwanda and Nigeria were added, and the DRC
removed, once the participant list was confirmed. Kenya and Tanzania reuse the bbox, capital and
rainfall event from the East Africa (`workshop-2`) branch; both events fall
inside this branch's window.

## 1. Selected date ranges

| Notebook | Period | Why |
|---|---|---|
| 01 Ground QC, 02 Rainfall Skill Explorer | **2023-07-01 → 2025-06-30** | Two full austral hydrological years (Jul–Jun) |
| 02 Case studies | Event windows (below) | All inside the main period |
| 03 Temperature & PET | **2023-10-01 → 2023-10-31** (comparison window **2023-10-25 → 2023-10-29**) | Late-Oct 2023 heatwave |
| 03 Step 7 / 04 AEZ long-term | Unchanged | Climatology, not event driven |

### Reasoning

* Southern Africa's main rainy season runs from **November to March**. A July–June
  window keeps each season whole and starts and ends in the dry season.
* The two seasons give a **drought-versus-flood contrast**:
  * **2023/24** was a severe El Niño season. Zimbabwe, Zambia, Malawi, Mozambique
    and Botswana got less than 20% of normal February rainfall, and Zimbabwe,
    Zambia and Malawi declared national disasters.
  * **2024/25** was wet, with Cyclone Chido and the Gaborone, Kigali and Mokwa floods.

  This is directly relevant to a Zambia-hosted workshop.
* Every country gets a well-documented event inside the window. An earlier
  2021–2023 window had no comparable Zimbabwe or Botswana events.
* The window is 731 days long, the same as the East Africa window.

### IMERG V06 → V07 (code change)

GEE's `NASA/GPM_L3/IMERG_V06` collection ends on **2024-06-02** and is deprecated,
so it can't cover this window. On this branch, Notebook 02 now pulls
`NASA/GPM_L3/IMERG_V07`. The units are the same (half-hourly mm/hr, ×0.5 to get
mm), the band is now `precipitation`, and the result is still saved as
`precipitationCal`, so nothing downstream changes. V07 permanent products run
to 2025-09-30.

## 2. Events investigated

### Rainfall (Notebook 02 `EVENTS`, 30 km radius)

| Country | Event | Peak | Window | Point | Evidence |
|---|---|---|---|---|---|
| Zimbabwe | El Niño mid-season **drought** | Feb 2024 | 02-01 → 02-29 | Harare (-17.83, 31.05) | <20% of normal Feb rain; national disaster 3 Apr 2024; 2.7 M people needing food aid ([WWA](https://www.worldweatherattribution.org/?p=2673), [AP](https://www.nbcnews.com/news/world/zimbabwe-el-nino-africa-drought-disaster-humanitarian-aid-rcna146347)) |
| Malawi | Nkhotakota floods | 26–27 Feb 2024 | 02-23 → 03-02 | Nkhotakota (-12.93, 34.30) | ~80,000 affected, 8 deaths ([Save the Children](https://resourcecentre.savethechildren.net/document/2024-save-the-children-malawi-nkhotakota-floods-situation-report), [IFRC](https://go-api.ifrc.org/api/downloadfile/87312/MDRMW020dfr)) |
| Mozambique | Tropical Cyclone Chido | 15 Dec 2024 | 12-12 → 12-19 | Mecúfi, Cabo Delgado (-13.28, 40.57) | ~260 km/h winds, ~250 mm in a day; 94–120 deaths; ~110,000 homes destroyed ([Al Jazeera](https://www.aljazeera.com/amp/news/2024/12/19/cyclone-chido-death-toll-in-mozambique-rises-to-73)) |
| Botswana | Gaborone floods | 16–20 Feb 2025 | 02-15 → 02-22 | Gaborone (-24.65, 25.91) | ≥9 deaths, 5,000+ displaced; ~40-yr return period ([WWA](https://www.worldweatherattribution.org/increasing-extreme-rainfall-and-rapid-urbanisation-major-drivers-behind-gaborones-deadly-floods/)) |
| Zambia | El Niño **drought** | Feb 2024 | 02-01 → 02-29 | Lusaka (-15.39, 28.32) | National disaster declared 29 Feb 2024; 84 of 116 districts affected ([Al Jazeera](https://www.aljazeera.com/news/2024/2/29/zambia-declares-national-disaster-after-drought-devastates-agriculture), [UN Zambia](https://zambia.un.org/en/node/271472)) |
| Angola | El Niño rainfall **deficit**, southern Angola | Mar 2024 | 03-01 → 03-31 | Ondjiva, Cunene (-17.07, 15.73) | Season rainfall 75–90% of average in Cunene/Huíla; dry March cut harvest prospects ([FEWS NET via ReliefWeb](https://reliefweb.int/report/angola/angola-key-message-update-dry-march-reduces-harvest-prospects-southern-angola-march-2024), [ReliefWeb drought page](https://reliefweb.int/disaster/dr-2024-000095-ago)) |
| Kenya | Garissa / Tana River floods | 20 Nov 2023 | 11-16 → 11-25 | Garissa (-0.46, 39.66) | Reused from the `workshop-2` branch. A routed river flood, so local rainfall totals are modest |
| Tanzania | Dar es Salaam floods | 4 Dec 2023 | 12-01 → 12-10 | Dar es Salaam (-6.79, 39.21) | Reused from the `workshop-2` branch |
| Rwanda | Kigali floods, long rains | 10–13 Apr 2025 | 04-08 → 04-15 | Kigali (-1.94, 30.06) | MINEMA: 52 deaths from rain-induced disasters, 1–16 Apr 2025 ([AllAfrica](https://allafrica.com/stories/202504180192.html), [AllAfrica](https://allafrica.com/stories/202504140532.html)) |
| Nigeria | Mokwa flash flood, Niger State | night of 28–29 May 2025 | 05-25 → 06-01 | Mokwa (9.30, 5.05) | ≥151 deaths by 31 May (AP); many missing; no official rainfall total published ([PBS/AP](https://www.pbs.org/newshour/amp/world/death-toll-rises-to-151-after-flooding-in-north-central-nigeria), [Wikipedia](https://en.wikipedia.org/wiki/2025_Mokwa_flood)) |

The Zimbabwe and Zambia cases are deliberately **droughts**: they test whether
the products agree on near-zero rain, not on a flood peak. The Angola case is a
moderate deficit, so compare against climatology rather than expecting zero.

No well-documented Angola flood fell inside the window: the Luanda/Benguela
floods found were April 2021 and April 2026. Rwanda's deadliest recent floods
(2–3 May 2023, 130+ deaths) also fall just before the window.

Considered but not used: Cyclone Freddy in Malawi/Mozambique (March 2023). It is
a strong event but falls before the chosen window.

### Heat (Notebook 03 `HEAT_EVENTS`)

**Late-October 2023 El Niño heatwave.** Botswana's Department of Meteorological
Services issued a nationwide heatwave warning with forecast maxima of 39–42 °C
until at least 27–30 Oct 2023 ([Crisis24](https://crisis24.garda.com/alerts/2023/10/botswana-namibia-heatwave-forecast-across-much-of-both-countries-through-at-least-oct-30)).
Regional outlooks gave 35–40 °C, 2–8 °C above average, across Botswana,
Zimbabwe and Mozambique. Zimbabwe, Malawi, Mozambique, Botswana, **Zambia
and Angola** use this event. The evidence is Botswana-centred, so check the
Zambia and Angola anomaly in ERA5 before presenting it.

**Kenya, Tanzania, Rwanda and Nigeria** use the notebook's default **March
2024** event (month 2024-03-01 → 03-31, window 03-01 → 03-05), as on the East
Africa branch. No country-specific heat event was researched for these four.
For Nigeria, a Feb–Apr 2024 West African heat episode would be a better fit if
one is documented in time.

## 3. Datasets

Same products as the existing workflow:

* **Ground:** TAHMO (default), GHCN-Daily, or custom national met-service CSVs.
* **Rainfall:** CHIRPS pentad, TAMSAT (PERSIANN-CDR fallback), **IMERG V07**,
  ERA5-Land.
* **Temperature:** ERA5 / ERA5-Land, CBAM.
* **Region:** OSM country polygon (Notebook 01) and the bboxes below
  (Notebooks 02–04).

| Country | bbox [lon_min, lat_min, lon_max, lat_max] | Capital |
|---|---|---|
| Zimbabwe | [25.2, -22.5, 33.1, -15.6] | Harare |
| Malawi | [32.6, -17.2, 36.0, -9.3] | Lilongwe |
| Mozambique | [30.2, -26.9, 41.0, -10.4] | Maputo |
| Botswana | [19.9, -27.0, 29.4, -17.7] | Gaborone |
| Zambia | [21.9, -18.1, 33.7, -8.2] | Lusaka |
| Angola | [11.6, -18.1, 24.1, -4.3] (includes Cabinda) | Luanda |
| Kenya | [33.9, -4.7, 41.9, 5.1] | Nairobi |
| Tanzania | [29.0, -12.0, 41.0, -1.0] | Dodoma |
| Rwanda | [28.8, -2.9, 30.9, -1.0] | Kigali |
| Nigeria | [2.6, 4.2, 14.7, 13.9] | Abuja |

### GHCN coverage (checked against NOAA's public archive)

PRCP days out of 731 in the window:

| Country | GHCN stations | With any PRCP | Best station |
|---|---|---|---|
| Mozambique | 19 | 9 | 265 |
| Botswana | 21 | 5 | 192 |
| Malawi | 20 | 2 | 182 |
| Zimbabwe | 20 | 3 | 129 |

GHCN and TAHMO coverage has **not yet been checked** for the six added
countries (Zambia, Angola, Kenya, Tanzania, Rwanda, Nigeria).

**GHCN cannot carry the station QC on its own for any of these countries.**
The 2021–2023 window is no better (Zimbabwe has no GHCN rainfall at all).
Ground data needs to come from **TAHMO** or from **national met services**
via the `custom` upload.

## 4. Assumptions and limitations

* **TAHMO coverage** (stations in TAHMO's metadata, Oct 2026): Malawi 30,
  Zimbabwe 19, Mozambique 19, Botswana 0. For Botswana use GHCN or a
  `"custom"` national export; GHCN alone is too sparse (see above).
* **CBAM availability** was confirmed only for Zimbabwe, Malawi, Mozambique
  and Botswana.
  Check the six added countries in the TomorrowNow GAP API before the session.
* **Rwanda** is small (about 2° × 2°), so ERA5 and IMERG have only a handful of
  pixels over the country.
* **PERSIANN-CDR** (the TAMSAT fallback) is released with a delay of a few
  months. Check that it reaches June 2025 when you run it.
* **Notebook 04** was empty on `main`. The populated version from `tahmo-work`
  was brought in, and its crop list is unchanged (maize, sorghum, cassava and
  groundnut matter most in these countries).
* **Saved cell outputs** are from earlier East Africa runs. Re-run in Colab to
  regenerate them. Cached files go to `Datasets/<Country>/` on the Shared Drive.
