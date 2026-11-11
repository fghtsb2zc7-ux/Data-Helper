# Traps

### T01 · excel-pq-cleaning · trap · memorize
**Q:** In the right whale CSV, some rows have a blank `individualCount`, but the row is still a sighting. You build a PivotTable of total whales per year. What is wrong with your totals, and what does Practice set 1 tell you to do?
**A:** Blank/null `individualCount` means a whale was seen but the number wasn't recorded, so those sightings add 0 and totals are too low. E.1.1 says assume a single whale: replace nulls with 1 in Power Query (Replace Values) before summarising.
**Source:** datasets/obis-north-atlantic-right-whale.md (issue 1); course/assessments.md (E.1.1)

### T02 · excel-if-ifs · trap · memorize
**Q:** Some whale records have negative `bathymetry` values. What does a negative value mean here, and what two things does the practice set do with it (one in Excel, one in QGIS)?
**A:** Negative bathymetry = the point is on land. Excel E.1.2: a `corrected_depth` column `=IF([@bathymetry]<0, 0, [@bathymetry])` (or fix via the column filter). QGIS Q.1.1: Field Calculator text field `IF("bathymetry" < 0, 'On land', 'On Water')` and symbolise by it.
**Source:** datasets/obis-north-atlantic-right-whale.md (issue 3)

### T03 · r-summarise · trap · memorize
**Q:** Two questions: "number of sighting records per year" and "number of whales per year". You use the same code for both. Why is one of them wrong, and what is the difference in R and in a PivotTable?
**A:** Records = count of rows (`n()` in R, Count of `id` in a PivotTable). Whales = sum of the count column (`sum(individual_count, na.rm = TRUE)`, Sum of `individualCount`). The exercises deliberately ask for both (E.1.4, R.1.3 vs R.1.4).
**Source:** datasets/obis-north-atlantic-right-whale.md (issue 2); tools/r-positron/group-and-summarize.md

### T04 · qgis-load-crs · trap · memorize
**Q:** You load sightings as EPSG:4326 and run Join attributes by nearest against the vessel routes. The distances come out like 0.013. What went wrong and how do you fix it?
**A:** EPSG:4326 is in degrees, so the distance is in degrees. Reproject both layers to a metre CRS first (the course uses NAD83 / UTM zone 20N, EPSG:26920, for the Bay of Fundy; UTM 17N EPSG:26917 for southern Ontario), then rerun. Divide by 1000 for km.
**Source:** datasets/vessel-traffic-routes.md (issue 1); tools/qgis/join-attributes-by-nearest.md (Pitfalls)

### T05 · r-filter · trap · memorize
**Q:** Human-wildlife practice exam Q1: "Remove species listed as Unknown, but keep names like 'unknown duck'." You write `filter(!str_detect(species_common_name, "nknown"))`. What happens, and what should you write?
**A:** Pattern matching also removes "unknown duck", "unknown mollusk", etc. Use exact equality: `filter(species_common_name != "Unknown")`.
**Source:** datasets/human-wildlife-coexistence.md (issue 1)

### T06 · r-summarise · trap · look up
**Q:** In the human-wildlife animals-involved file, you count incidents per year with `n()` and get more than the incidents file says. Why?
**A:** The animals file has one row per species per incident, so incident numbers repeat. Count incidents with `n_distinct(incident_number)` when the question is about incidents.
**Source:** datasets/human-wildlife-coexistence.md (issue 3)

### T07 · r-bind-join · trap · memorize
**Q:** Crab practice set: you plot total crabs per year straight from `n_tot`. The figure looks wrong compared with crab_counts.png. What did the question warn you about?
**A:** Counts must be corrected for tow length: longer tows catch more crabs. Join the tow info (`dist`) to the crab counts, then divide, e.g. `mutate(crabs_per_m = n_tot / dist)`, before summarising.
**Source:** datasets/rock-crab-survey.md (issue 2); tools/r-positron/practice-exam-r-workflows.md

### T08 · r-bind-join · trap · look up
**Q:** You `left_join()` the crab counts to the station info without `by =`. Which columns does R join on, and what should you check first?
**A:** All shared column names: `date`, `st`, `tr`, `bat`. Check they have the same type in both files (e.g. `date` and `st`) or the join fails or matches nothing.
**Source:** datasets/rock-crab-survey.md (issue 3); tools/r-positron/practice-exam-r-workflows.md (Pitfalls)

### T09 · r-read-clean · trap · look up
**Q:** In `particulate_matter_ON.csv`, the estimation method column header prints as `Estimation_Method / M�thode_d�estimation`. What is going on, and name one fix.
**A:** The file isn't UTF-8, so the French accents are mis-decoded. Read with `read_csv(..., locale = locale(encoding = "latin1"))`, or just `clean_names()` / rename by position.
**Source:** datasets/tpm-practice-exam.md (column table)

### T10 · r-summarise · trap · memorize
**Q:** TPM data: Bunge Hamilton has two rows for 2024 (3.794 t and 26.130 t). You plot a trend per facility straight from the rows. What's the problem?
**A:** Rows are separate release reports for the same facility-year. Sum per facility and year (`group_by(npri_id, year) |> summarize(total = sum(quantity))`) before plotting. Also trim trailing spaces in `Company_Name` (false duplicates).
**Source:** datasets/tpm-practice-exam.md (issues 1 and 3)

### T11 · qgis-raster · trap · memorize
**Q:** The TPM population raster `can_ppp_2020_1km_Aggregated` — what does one cell value mean, and why does that matter for the question "facilities in areas with over 500 people"?
**A:** Each cell is the estimated number of people living in that ~1 km cell (a count, not a density). So "over 500 people" = sampled cell value > 500; no area division needed.
**Source:** datasets/tpm-practice-exam.md (issue 4)

### T12 · traps-general · trap · look up
**Q:** You open the full NPRI Releases CSV in Excel and summarise. Why might your totals be too low?
**A:** The NPRI Releases file is truncated at Excel's row limit (1,048,575 rows), so later rows are missing. Use Power Query/R, or a filtered file.
**Source:** README.md (Known data traps); datasets/npri-file-schemas.md

### T13 · r-bind-join · trap · look up
**Q:** You join PWQMN 2024 measurements to stations in R and about half the rows don't match. What's the likely cause, and how do you check?
**A:** Station IDs lost a leading zero in one file (`03007703502` vs `3007703502`), and keys have different types. Make both keys text and pad (or both numeric), and check unmatched rows with `anti_join()`. Also STATION isn't unique (duplicates add rows): `distinct(station, .keep_all = TRUE)` first.
**Source:** datasets/pwqmn.md (issues 1 and 2); datasets/id-columns-leading-zeros.md

### T14 · traps-general · scenario · memorize
**Q:** Your whale sightings by month peak in summer. A classmate concludes whales are mostly present in summer. What would you say (the practice set asks you to discuss this)?
**A:** Counts reflect observation effort (more surveys in summer, good weather), not only whale presence. Monthly totals can't separate the two without effort data.
**Source:** datasets/obis-north-atlantic-right-whale.md (issue 7); course/assessments.md (E.1.5)

### T15 · qgis-joins-nearest · scenario · memorize
**Q:** After Q.1.5 you find 40 sightings within 5 km of a shipping route. Does that show vessels were near whales? Why or why not?
**A:** No: proximity to a mapped route doesn't show a vessel was there at the time of the sighting. It's distance to a route, not to a ship.
**Source:** datasets/vessel-traffic-routes.md (issue 4)

### T16 · r-ggplot · trap · look up
**Q:** Basking shark temperature bins plot in the order ">18", "0-2", "10-12"… instead of coldest to warmest. Why, and how is it fixed?
**A:** Text categories plot alphabetically. Set the order with `factor(column, levels = c(...))` (or `fct_reorder` when ordering by a value).
**Source:** datasets/class-2-basking-shark-tag-data.md (issue 5); tools/r-positron/order-categories-with-factor-and-reorder.md
