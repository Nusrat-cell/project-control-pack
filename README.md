# Project Control Pack

A small toolkit that does the paperwork a project coordinator keeps for a project manager: the plan with dependencies and critical path, the budget with a forecast, the risk and issue logs, the resource plan, and a one-page weekly status report. It reads one project definition and writes a markdown report and an Excel workbook.

The project in it is made up: moving a retailer's customer data to a new CRM. All names, dates and amounts are invented.

## What it does

1. **Plan and schedule.** Working days only, dependencies between tasks, a forward and backward pass for slack and the critical path. A dependency cycle or an unknown task id stops the run with a clear message.
2. **Forecast.** Re-plans the work that is left from the status date and reports the slip in working days against the baseline.
3. **Budget control.** Planned, actual, estimate to complete, forecast at completion and variance per line. Lines more than 10 percent over are flagged.
4. **Risks and issues.** Probability times impact gives a score and a rating. Reviews are due every 14 days and overdue ones are listed. Open issues older than 14 days are marked as needing a decision.
5. **Resources.** Weekly allocation per person and over-allocation above 100 percent.
6. **Stakeholders.** Interest, influence and how often each one is updated.
7. **Status report.** A red, amber or green rating from explicit rules, the late tasks, the decisions needed this week and the top risks.

## Run it

```
python -m pcp demo
python -m pytest -q
```

## Result on the sample project

|Measure|Result|
|-|-|
|Baseline finish|5 Nov 2026|
|Forecast finish|23 Nov 2026 (12 working days late)|
|Critical path|T1, T2, T3, T5, T6, T8, T9, T10|
|Forecast cost|536.500 DKK against 480.000 DKK (11.8 percent over)|
|Late tasks|4 of 10|
|High risks|2, with 2 reviews overdue|
|Over-allocation|1 person, 1 week|
|Overall status|Red|

## Rules for the status colour

* Red: slip above 10 working days, budget more than 10 percent over, or two or more high risks.
* Amber: any slip, any overspend, or an overdue risk review.
* Green: none of the above.

## What this is not

* The data is invented and there is no connection to Jira, Asana, Microsoft Project or a finance system.
* Progress is entered by hand as a percentage per task. A real project would take it from the team's tool.
* There are no charts and no Gantt picture, only the workbook and the report.
