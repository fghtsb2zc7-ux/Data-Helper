# Workflows: which tool, which order

These mirror the practice exam questions. A "solid" answer names the tools in order, the key algorithm or verb at
each step, and the hand-off file between tools.

### W01 · qgis-buffer-select · order · memorize
**Q:** Ferry practice question: recreate a column chart of whale sightings within 1 km and 2 km of the Grand Manan ferry route, by month. Which steps happen in QGIS, what gets handed to R, and what does R do?
**A:** QGIS: load sightings (EPSG:4326) and the ferry route `FERYRT_L`; reproject to a metre CRS (EPSG:26920); Buffer the route by 1000 m and 2000 m; select/extract the sightings inside each buffer; export each as CSV (`1km_buffer.csv`, `2km_buffer.csv`). R: read both, `clean_names()`, `mutate(buffer = "1 km")` / `"2 km"`, `bind_rows()`, `month(event_date_standard, label = TRUE)`, `group_by(month, buffer) |> summarize(sightings = n())`, filter Jul to Nov, `geom_col(colour = "black")` with `fill = buffer`, `labs()`, `theme_bw()`, legend at bottom.
**Source:** course/assessments.md (Practice exam question: ferry); tools/r-positron/practice-exam-r-workflows.md

### W02 · qgis-raster · order · memorize
**Q:** TPM practice exam Q2: a map with red 5 km rings around facilities in areas with over 500 people, plus the raster cells with over 1000 people. List the QGIS steps in order.
**A:** Load `particulate_matter_ON.csv` as points (latitude/longitude, EPSG:4326) and the population raster. Sample raster values at the points (population per cell). Filter points with sampled value > 500. Reproject those points to a metre CRS. Buffer 5000 m and style as red rings (outline only). Show cells > 1000 with Raster Calculator (`"raster@1" > 1000`, or keep values with `* "raster@1"`) or symbology thresholds, make 0 transparent. Finish in a Print Layout with title, legend, scale bar; export.
**Source:** course/assessments.md (Full practice exam: Particulate matter); tools/qgis/sample-raster-values-at-points.md; tools/qgis/raster-calculator-threshold-filter.md; tools/qgis/buffer-points-fixed-distance.md

### W03 · r-bind-join · order · memorize
**Q:** Crab practice set: recreate crab_counts.png from `Information_stations.csv` and `Nombre_crabe_crab_number.csv`. Outline the R pipeline.
**A:** Read both with `clean_names()`; `left_join()` crab counts with the station/tow info (joins on shared `date`, `st`, `tr`, `bat`; check types match); `mutate()` a standardised count, `n_tot / dist`; `group_by()` year (`an`) and `summarize()`; plot to match the target; `ggsave()`.
**Source:** course/assessments.md (Practice set 2); datasets/rock-crab-survey.md

### W04 · qgis-joins-nearest · order · memorize
**Q:** Whale Q.1.4 and Q.1.5: distance from each sighting to the nearest traffic route, then count sightings within 5 km. Steps and the key settings?
**A:** Reproject sightings and the merged routes layer to NAD83 / UTM 20N (EPSG:26920). Processing > Join attributes by nearest (input = sightings, layer 2 = routes, max neighbours 1) → `distance` field in metres. Field Calculator `"distance" / 1000` for km. Filter `"distance_km" <= 5` and read the feature count. Graduated symbology on distance. Distance 0 means the sighting is inside a route polygon.
**Source:** course/assessments.md (Q.1.4, Q.1.5); tools/qgis/join-attributes-by-nearest.md

### W05 · r-summarise · order · memorize
**Q:** Human-wildlife R practice exam Q2: top five species in Human Wildlife Interaction incidents, then a figure of deterrent records for those species. Outline the code.
**A:** `filter(incident_type == "Human Wildlife Interaction")`; `group_by(species_common_name) |> summarize(n = n()) |> arrange(-n) |> head(5)` → top table; back on the deterrent data `filter(species_common_name %in% top5$species_common_name)`; summarise and plot; `ggsave()`.
**Source:** course/assessments.md (Practice R exam); tools/r-positron/sort-and-keep-top-n.md

### W06 · r-pivot · order · look up
**Q:** Human-wildlife Q3: mean number of animals per incident type, 2013 vs 2023, using the hint "use back-ticks around the year headers". What does the hint tell you about the shape of the data?
**A:** Years become column names after `pivot_wider(names_from = year, values_from = <mean animals>)`, so they must be back-ticked in later calculations, e.g. `mutate(change = \`2023\` - \`2013\`)`. Before that: `select()` Year, Incident Type, Sum of number of animals; `group_by(year, incident_type) |> summarize(mean_animals = mean(...))`; filter 2013 to 2023.
**Source:** tools/r-positron/pivot-longer-and-wider.md (Pitfalls); course/assessments.md

### W07 · r-lm · order · memorize
**Q:** TPM Q1: recreate a scatter with a trend line and put the slope and whether it is significantly different from zero in the subtitle. Which functions?
**A:** Summarise as the figure needs (e.g. total per year); `model <- lm(y ~ x, data)`; `summary(model)` → slope = estimate in the predictor row, p-value `Pr(>|t|)` in the same row, compare with 0.05; `ggplot() + geom_point() + geom_smooth(method = "lm")`; `labs(subtitle = "Slope = ..., p = ... (not) significant")`.
**Source:** tools/r-positron/fit-linear-regression.md; tools/r-positron/plot-scatter-with-trend-line.md

### W08 · excel-pq-cleaning · order · look up
**Q:** You are told "clean in Excel, map in QGIS". For the whale CSV, what Excel output does QGIS need, and in which format?
**A:** Power Query clean (parse dates, month column, nulls → 1), then save as CSV (E.1.1: `OBIS - North Atlantic Right Whale updated.csv`). QGIS loads it as a delimited text layer with X = `decimalLongitude`, Y = `decimalLatitude`, EPSG:4326.
**Source:** course/assessments.md (E.1.1, Q.1.1); tools/qgis/add-delimited-text-layer-csv.md
