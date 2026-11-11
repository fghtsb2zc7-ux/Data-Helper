# results/

One sub-folder per question, created by `agent/new_job.sh`, named `NN-short-name` (e.g. `03-crab-counts`).

| Inside a job folder | What |
|---|---|
| `inputs/` | copies of the files you supplied; the target image is also saved as `target.<ext>` |
| `work/` | intermediate and hand-off files (cleaned CSVs, GeoPackages, step scripts, `r.log`, `qgis.log`) |
| `screenshots/` | numbered progress screenshots (`01-…png`, `02-…png`, …) |
| `final/` | the finished graph/map (`.png`), the final R script (`<name>.R`) and/or QGIS project (`.qgz`) / workbook (`.xlsx`), and `comparison.png` (target vs result) |
| `REPORT.md` | target specification, plan, steps with the course procedures used, assumptions, web lookups, remaining differences |
