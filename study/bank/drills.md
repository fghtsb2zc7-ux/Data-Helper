# Hands-on drills and timed mocks

Drills run in the real apps. Copy inputs into `study/drills/<date>-<drill id>/` first (never work on
`sources/files/` directly, and never write to `results/`, which belongs to the chart agent).

How the coach checks a drill:
- **R**: the learner saves `drill.R` in the drill folder. Run it with `agent/r/run_r.sh <drill folder>/drill.R`; check
  it runs clean, uses only tidyverse + janitor, and writes the asked PNG/CSV. Look at the PNG.
- **Chart vs target**: `agent/py.sh agent/compare.py <your.png> <target.png>` gives a side-by-side; then look at it
  (titles, axes, colours, legend, facets).
- **Excel / QGIS**: ask for a screenshot (or take one with `agent/screenshot.sh <drill folder>/screenshots/x.png`)
  and check the visible result against the model answer.

### D01 · r-ggplot · drill · 15 min
**Task:** Practice set 1 R.1.4: yearly number of sighting records as a purple line with points, axis labels, a title,
`theme_bw()`. Data: `sources/files/Practice sets/OBIS - North Atlantic Right Whale reduced.csv`.
**Check:** `group_by(year) |> summarize(sightings = n())`; `geom_line(colour = "purple") + geom_point(colour = "purple")`; labels; theme_bw.
**Source:** tools/r-positron/plot-line-chart.md; course-pages/practice-1-north-atlantic-right-whale.md

### D02 · r-ggplot · drill · 15 min
**Task:** R.1.6: monthly sightings split Individual vs Group as stacked columns; export PNG and CSV.
**Check:** ifelse on `individual_count >= 2`; `group_by(month, group_type) |> summarize(n = n())`; `fill = group_type`; `ggsave()` and `write_csv()`.
**Source:** tools/r-positron/classify-with-ifelse.md; tools/r-positron/save-plot-png-and-csv.md

### D03 · r-bind-join · drill · 25 min
**Task:** Practice set 2: recreate `sources/files/Practice sets/Practice set #2/crab_counts.png`.
**Check:** compare with the target; the chart agent's solved version is in `results/01-crab-counts/final/` (look only after the attempt).
**Source:** datasets/rock-crab-survey.md; results/01-crab-counts/REPORT.md

### D04 · excel-pivots · drill · 15 min
**Task:** E.1.3 in Excel: PivotTable of sighting records by `institutionCode`, remove blanks and institutions with < 10 records, sort by count, PivotChart.
**Check:** screenshot shows no "(blank)", all counts >= 10, sorted by value not label.
**Source:** tools/excel/create-pivottable-summarize-filter-sort.md; tools/excel/create-pivotchart-from-pivottable.md

### D05 · qgis-buffer-select · drill · 25 min
**Task:** Ferry question, QGIS half: 1 km and 2 km buffers around the ferry route, export the sightings inside each as CSV.
**Check:** both layers reprojected to EPSG:26920 before buffering; two CSVs with `eventDate_standard`; 2 km count >= 1 km count. Then do the R half (W01) and compare with `sources/files/Practice Questions/ferry.png`.
**Source:** course/assessments.md (ferry); tools/qgis/buffer-points-fixed-distance.md

## Timed mocks

| Mock | Section | Time | Material |
|---|---|---|---|
| M1 | Whale R.1.1 to R.1.6 | 45 min | course-pages/practice-1-north-atlantic-right-whale.md (answers in "Get help") |
| M2 | Whale E.1.1 to E.1.7 | 45 min | same page |
| M3 | Whale Q.1.1 to Q.1.6 | 60 min | same page |
| M4 | Human-wildlife Q1 to Q3 | 60 min | sources/files/Practice Questions/ENVRSUST 9014 R Practice Exam.pdf |
| M5 | Particulate matter Q1 to Q3 | 90 min | sources/files/ENVRSUST 9014 - Practice Exam - Particulate Matter 2026 updated.pdf |

During a mock the coach stays quiet except for time checks every 15 minutes, then grades each question
solid / shaky / blank against the model answers and logs the topic keys.
