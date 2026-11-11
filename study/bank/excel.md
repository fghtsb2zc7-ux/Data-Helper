# Excel

### E01 · excel-dates · scenario · look up
**Q:** The whale `eventDate` column mixes `2011-10-12 0:00`, `1/28/2009` and `Apr-64`, and its header icon shows ABC. How do you get one usable date column in Power Query, and what happens to `Apr-64`?
**A:** Select `eventDate`, then Add Column > From Date & Time > Date > Parse. A new date-typed `Parse` column is added. Month-year values become the 1st of that month.
**Source:** tools/excel/parse-inconsistent-dates-power-query.md; datasets/obis-north-atlantic-right-whale.md (issue 4)

### E02 · excel-dates · fill · look up
**Q:** In Power Query you need a month column from `eventDate_standard`. Finish the menu path: Add Column > ... and name the two Month options that give a number vs a name.
**A:** Add Column > From Date & Time > Date > Month > Month (number) or Name of Month (text).
**Source:** tools/excel/extract-date-parts-power-query.md

### E03 · excel-if-ifs · fill · memorize
**Q:** E.1.6: classify sightings as "Only 1", "Between 2 and 10", "More than 10". Finish: `=IFS([@individualCount]>10, "More than 10", ...)`. Why does the order of the conditions matter?
**A:** `=IFS([@individualCount]>10, "More than 10", [@individualCount]>1, "Between 2 and 10", [@individualCount]=1, "Only 1")`. IFS returns the first true condition, so the >10 test must come before >1 or everything above 1 lands in "Between 2 and 10".
**Source:** course/assessments.md (E.1.6); tools/excel/ifs-categorize-numeric-thresholds.md

### E04 · excel-pivots · scenario · memorize
**Q:** You rank institutions in a PivotTable using Sort A to Z, but the biggest isn't at the bottom. Why, and what do you use instead?
**A:** A to Z sorts the labels alphabetically. Use Row Labels dropdown > More Sort Options > Ascending/Descending by "Sum of …" (or "Count of …").
**Source:** tools/excel/create-pivottable-summarize-filter-sort.md (Pitfalls)

### E05 · excel-pivots · scenario · look up
**Q:** E.1.3 asks how many sightings have no institution. Where does that show up in the PivotTable, and how do you then remove it plus institutions with fewer than 10 sightings?
**A:** As a "(blank)" row in Row Labels. Remove it via the Row Labels filter (untick "(blank)") and use a Value Filter (Count of … less than 10 → exclude, or "greater than or equal to 10").
**Source:** tools/excel/create-pivottable-summarize-filter-sort.md; course/assessments.md (E.1.3)

### E06 · excel-pivots · scenario · memorize
**Q:** E.1.4 asks you to switch a chart from "sum of individualCount per year" to "number of sightings per year". What exactly do you change in the PivotTable?
**A:** Value Field Settings on the values field: change Sum to Count (or put `id` in Values as Count). Sum = whales, Count = records.
**Source:** course/assessments.md (E.1.4); datasets/obis-north-atlantic-right-whale.md (issue 2)

### E07 · excel-dropdown-countif · order · memorize
**Q:** E.1.7: a cell where you pick an institution from a dropdown and another cell shows its number of sightings. Three steps?
**A:** (1) `=UNIQUE(range)` of institution codes on a separate sheet; (2) Data > Data Validation > Allow: List, Source = that unique range; (3) `=COUNTIF(institution_column, dropdown_cell)` in the result cell.
**Source:** tools/excel/unique-distinct-values-formula.md; tools/excel/data-validation-dropdown-list.md; tools/excel/countif-sumif-max-min-formulas.md

### E08 · excel-pq-cleaning · scenario · look up
**Q:** A PWQMN station ID like `03007703502` shows up in Excel as `3.0077E+09`. What happened and how do you stop it?
**A:** Excel/Power Query typed the ID as a number, dropping the leading zero and showing scientific notation. Set the column type to Text in Power Query (Transform > Data Type: Text) before loading.
**Source:** datasets/pwqmn.md (issue 1); datasets/id-columns-leading-zeros.md; tools/excel/check-and-fix-data-types-power-query.md
