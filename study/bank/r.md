# R (tidyverse + janitor)

### R01 · r-read-clean · bug · memorize
**Q:** `whales <- read_csv("OBIS - North Atlantic Right Whale reduced.csv")` then `whales |> filter(individual_count > 1)` gives "object 'individual_count' not found". Why?
**A:** The raw header is `individualCount`; snake_case names only exist after `clean_names()`. Add `|> clean_names()` to the read (and load `library(janitor)`).
**Source:** tools/r-positron/read-csv-and-clean-column-names.md; datasets/obis-north-atlantic-right-whale.md (issue 10)

### R02 · r-dates · fill · memorize
**Q:** R.1.1: add a labelled month (Jan, Feb…) from `event_date_standard`. One line.
**A:** `mutate(month = month(event_date_standard, label = TRUE))`.
**Source:** tools/r-positron/parse-dates-and-extract-month.md

### R03 · r-dates · scenario · look up
**Q:** PWQMN `collected` looks like `07/14/2024`; the human-wildlife animals file has `2015-06-03`. Which lubridate function for each?
**A:** `mdy()` for MM/DD/YYYY, `ymd()` for ISO. Then `year()` / `month(label = TRUE)`.
**Source:** datasets/pwqmn.md (issue 5); datasets/human-wildlife-coexistence.md (issue 2)

### R04 · r-summarise · fill · memorize
**Q:** R.1.3: sum of whale counts per month, ignoring missing values. Fill in: `whales |> group_by(month) |> summarize(...)`.
**A:** `summarize(total = sum(individual_count, na.rm = TRUE))`.
**Source:** tools/r-positron/group-and-summarize.md

### R05 · r-ggplot · bug · memorize
**Q:** You want all columns blue and write `geom_col(aes(fill = "blue"))`. The bars come out salmon with a legend saying "blue". Why?
**A:** Inside `aes()` "blue" is treated as a data value (a category), not a colour. Fixed colours go outside: `geom_col(fill = "blue")`.
**Source:** tools/r-positron/plot-column-chart.md (step 5)

### R06 · r-ggplot · scenario · memorize
**Q:** In a column chart, what's the difference between `fill = buffer` inside `aes()` and `colour = "black"` in `geom_col()`?
**A:** `fill` inside aes maps a variable to the bar fill (stacks and adds a legend); `colour` outside aes sets a fixed outline for every bar.
**Source:** course/assessments.md (ferry code); tools/r-positron/plot-column-chart.md

### R07 · r-bind-join · scenario · memorize
**Q:** You have `1km_buffer.csv` and `2km_buffer.csv` with the same columns. Why does the course `mutate(buffer = "1 km")` each before `bind_rows()`?
**A:** After stacking, nothing would show which file a row came from. The constant label column lets you group and fill by buffer.
**Source:** tools/r-positron/bind-rows.md; tools/r-positron/create-columns-with-mutate.md

### R08 · r-bind-join · scenario · look up
**Q:** After a `left_join()` your row count went up from 112,392 to 112,450 and R warned about many-to-many. What happened and the fix?
**A:** The lookup table has duplicate keys (STATION appears twice), so matched rows duplicate. `distinct(station, .keep_all = TRUE)` on the lookup before joining; compare `nrow()` before and after.
**Source:** datasets/pwqmn.md (issue 2); tools/r-positron/find-duplicates-and-keep-distinct.md

### R09 · r-summarise · fill · memorize
**Q:** R.1.5: the top five institutions by whales seen. Fill the pipe: `group_by(institution_code) |> summarize(whales = sum(individual_count, na.rm = TRUE)) |> ...`
**A:** `arrange(-whales) |> head(5)`. Then use `filter(institution_code %in% top5$institution_code)` on the detailed data.
**Source:** tools/r-positron/sort-and-keep-top-n.md

### R10 · r-filter · scenario · memorize
**Q:** R.1.6 splits sightings into "Individual" (1) and "Group" (2 or more). Write the mutate.
**A:** `mutate(group_type = ifelse(individual_count >= 2, "Group", "Individual"))`.
**Source:** tools/r-positron/classify-with-ifelse.md

### R11 · r-lm · scenario · memorize
**Q:** In `summary(lm(quantity ~ year, data))`, where is the slope and how do you decide if it differs from zero?
**A:** The `Estimate` in the `year` row is the slope; its `Pr(>|t|)` is the p-value. p < 0.05 = significantly different from zero.
**Source:** tools/r-positron/fit-linear-regression.md

### R12 · r-ggplot · fill · memorize
**Q:** Save the last plot as a 15 × 10 cm PNG and the summary table as CSV.
**A:** `ggsave("name.png", width = 15, height = 10, units = "cm")` and `write_csv(summary_table, "name.csv")`.
**Source:** tools/r-positron/save-plot-png-and-csv.md

### R13 · r-ggplot · scenario · look up
**Q:** R.1.5 wants yearly sums per institution as columns, one panel per institution. Which ggplot addition gives the panels?
**A:** `facet_wrap(~ institution_code)` (plus `fill = institution_code` for colour).
**Source:** tools/r-positron/customize-plot-labels-themes-facets.md

### R14 · r-pivot · fill · look up
**Q:** Stack columns `Bin1` to `Bin8` into two columns `range` and `percent`.
**A:** `pivot_longer(cols = Bin1:Bin8, names_to = "range", values_to = "percent")`. All stacked columns must share a type (convert text bins with `as.numeric()` first).
**Source:** tools/r-positron/pivot-longer-and-wider.md
