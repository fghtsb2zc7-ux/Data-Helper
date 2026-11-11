# study/ — the ENVRSUST 9014 study coach

The study coach is the second agent in this folder. It quizzes you on the course material in this repo, grades
each answer straight away, points you to the file that has the answer, and brings weak topics back on a spaced
schedule. Its method comes from the ADHD Study Coach plugin; its workflow is the `study-9014` skill
(`.claude/skills/study-9014/SKILL.md`).

Start it in Claude Code in the Data Repo folder by saying, for example, "quiz me", "exam sprint",
"let's study QGIS buffers", "mock exam M1", "I'm done for today" or "how am I doing".

| Path | What |
|---|---|
| `bank/` | Question bank (traps, workflows, Excel, QGIS, R, drills and mock exams), each with a model answer and source path |
| `tools/coach.py` | Progress helper: status, what's next, grading and rescheduling, session log |
| `state/` | Your progress, in the plugin's file formats (created on first use) |
| `state/notes/ENVRSUST 9014/` | Reflection notes, the exam cheat sheet, optional Anki decks |
| `drills/` | Scratch folders for hands-on drills |

It never writes to the knowledge base or to `results/` (the chart agent's folder).
