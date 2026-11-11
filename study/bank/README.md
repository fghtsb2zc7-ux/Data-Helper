# Question bank (exam sprint edition, 2026-10-25)

Read-only during a study session. Every question is tied to a **topic key** (the unit the review schedule tracks)
and to the repo file that holds the answer, so feedback can always say "where it lives".

| File | What |
|---|---|
| `traps.md` | Data-quality traps from the practice and course datasets |
| `workflows.md` | "Which tool, which order" for the practice exam questions |
| `excel.md` | Power Query, formulas, PivotTables, dropdowns |
| `qgis.md` | CRS, buffers, joins, counts, rasters, print layout |
| `r.md` | tidyverse + janitor: read, dates, filter, summarise, joins, pivots, lm, ggplot |
| `drills.md` | Hands-on tasks in the real apps and timed mock sections |

## Format of one question

```
### <id> · <topic key> · <type> · <memorize | look up>
**Q:** the scenario, as it will be asked
**A:** the model answer (what "solid" needs to contain)
**Source:** repo path(s)
```

Types: `scenario`, `bug`, `fill`, `order` (which tool / which order), `trap`, `drill`.
"memorize" = worth holding in your head for the exam; "look up" = know that it exists and where it is.

Grading rule for the coach: **solid** = contains the key idea of A (wording can differ); **shaky** = right direction
but a key step, argument or value missing; **blank** = no answer, "don't know", or the key idea is missing.

## Topic keys

| Key | Tool | Covers |
|---|---|---|
| `excel-pq-cleaning` | Excel | Power Query import, nulls, replace values, data types |
| `excel-dates` | Excel | Parse dates, extract year/month |
| `excel-if-ifs` | Excel | IF, IFS, nested conditions |
| `excel-pivots` | Excel | PivotTables/Charts, count vs sum, sorting by value, blanks |
| `excel-dropdown-countif` | Excel | UNIQUE, Data Validation list, COUNTIF/SUMIF |
| `qgis-load-crs` | QGIS | Delimited text layers, CRS, reprojecting before distances |
| `qgis-buffer-select` | QGIS | Buffers, selecting/extracting points inside, exporting |
| `qgis-joins-nearest` | QGIS | Join by nearest, join by location, distance fields |
| `qgis-merge-export` | QGIS | Merge vector layers, save selected features |
| `qgis-count-symbology` | QGIS | Count points in polygon, categorized/graduated styles |
| `qgis-field-calculator` | QGIS | Field Calculator IF/CASE, type changes, km conversion |
| `qgis-raster` | QGIS | Sample raster values, raster calculator thresholds |
| `qgis-print-layout` | QGIS | Print layout elements, export |
| `r-read-clean` | R | read_csv, clean_names, encodings, column names |
| `r-dates` | R | ymd/mdy, month(label = TRUE), year() |
| `r-filter` | R | filter, exact vs pattern match, %in%, NA |
| `r-summarise` | R | group_by + summarize, n() vs sum(), top-n |
| `r-bind-join` | R | bind_rows with labels, left_join keys and types, duplicates |
| `r-pivot` | R | pivot_longer / pivot_wider, backticks |
| `r-lm` | R | lm, summary, slope and p-value in a subtitle |
| `r-ggplot` | R | geom_col/line/point, fill vs colour, stacking, facets, labs, themes, ggsave |
| `traps-general` | All | Encodings, leading zeros, truncated files, effort bias |
