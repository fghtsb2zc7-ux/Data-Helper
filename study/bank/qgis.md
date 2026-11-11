# QGIS

### Q01 · qgis-load-crs · order · memorize
**Q:** Load the whale CSV as points. Menu path, which fields go to X and Y, and which CRS?
**A:** Layer > Add Layer > Add Delimited Text Layer; Point coordinates; X = `decimalLongitude`, Y = `decimalLatitude`; CRS EPSG:4326 (WGS 84).
**Source:** tools/qgis/add-delimited-text-layer-csv.md; datasets/obis-north-atlantic-right-whale.md (issue 8)

### Q02 · qgis-buffer-select · bug · memorize
**Q:** You buffer PWQMN stations by 500 and the buffers cover all of Ontario. What happened?
**A:** The layer was still in EPSG:4326, so 500 = 500 degrees. Reproject (Vector general > Reproject layer) to EPSG:26917 (UTM 17N) and buffer 500 metres.
**Source:** tools/qgis/buffer-points-fixed-distance.md (Pitfalls)

### Q03 · qgis-merge-export · order · look up
**Q:** Q.1.2: combine `TSSLPT_A.shp` and `TSEZNE_A.shp` into one layer, then keep only the Bay of Fundy routes as their own layer. Steps? There's a warning you can ignore; which?
**A:** Vector > Data Management Tools > Merge Vector Layers (both inputs). Select the Bay of Fundy features, then right-click > Export > Save Selected Features As (set path with `...`). The field-length warning can be ignored.
**Source:** tools/qgis/merge-vector-layers.md; datasets/vessel-traffic-routes.md (issues 2 and 3)

### Q04 · qgis-count-symbology · scenario · look up
**Q:** Q.1.3: show how many sightings fall in each route polygon, and compare May with August. Which algorithm, what's the new field called, and how do you get the two months?
**A:** Vector analysis > Count points in polygon (polygons = routes, points = sightings) → `NUMPOINTS`. Filter the sightings to May (and separately August) before counting, making two count layers; style Graduated on `NUMPOINTS`.
**Source:** tools/qgis/count-points-in-polygon.md; course/assessments.md (Q.1.3)

### Q05 · qgis-field-calculator · fill · memorize
**Q:** Field Calculator: create a text field that says 'On land' when bathymetry is below zero, otherwise 'On Water'. Write the expression. Mind the quotes.
**A:** `IF("bathymetry" < 0, 'On land', 'On Water')`. Double quotes = field names, single quotes = text values.
**Source:** course/assessments.md (Q.1.1); tools/qgis/field-calculator-if-statement.md

### Q06 · qgis-joins-nearest · scenario · look up
**Q:** You run Join attributes by nearest and leave "Layer 2 fields to copy" empty, expecting no extra columns. What do you get?
**A:** Empty means copy ALL layer-2 fields, plus `n`, `distance`, `feature_x/y`, `nearest_x/y`.
**Source:** tools/qgis/join-attributes-by-nearest.md (Pitfalls)

### Q07 · qgis-raster · fill · memorize
**Q:** Raster Calculator: one expression that gives 1/0 for cells above 0.5, and one that keeps the original values above 0.5 (0 elsewhere), for layer "Carcinus maenas".
**A:** `"Carcinus maenas@1" > 0.5` and `("Carcinus maenas@1" > 0.5) * "Carcinus maenas@1"`. Then restyle as Singleband pseudocolor and make 0 transparent.
**Source:** tools/qgis/raster-calculator-threshold-filter.md

### Q08 · qgis-raster · scenario · look up
**Q:** You run Sample raster values with prefix `pop`. What's the new column called, and why might some points get NULL?
**A:** `pop1` (prefix + band number). Points outside the raster extent get NULL; keep layers in matching CRSs.
**Source:** tools/qgis/sample-raster-values-at-points.md

### Q09 · qgis-print-layout · order · memorize
**Q:** Q.1.6 print layout: list the items the map needs and how you finish.
**A:** Project > New Print Layout; Add Map; title (Add Label); Add Legend (remove unneeded layers); Add Scale Bar (north arrow if asked); Layout > Export as Image/PDF; save the project and layers.
**Source:** tools/qgis/print-layout-checklist.md; tools/qgis/print-layout-map-export.md
