"""A made up project: moving a retailer's customer data to a new CRM. Everything here is invented."""
from datetime import date

PROJECT = dict(name="CRM Migration for a Retail Client", start=date(2026, 9, 7), status_date=date(2026, 10, 19),
               pm="Project Manager", budget_total=480000.0, currency="DKK")

# id, name, owner, working days, depends on, percent complete
TASKS = [
    ("T1", "Kick-off and scope sign-off", "PM", 3, [], 100),
    ("T2", "Map customer fields", "Analyst", 8, ["T1"], 100),
    ("T3", "Build load scripts", "Engineer", 10, ["T2"], 80),
    ("T4", "Clean duplicate customers", "Analyst", 7, ["T2"], 60),
    ("T5", "Trial migration", "Engineer", 4, ["T3", "T4"], 0),
    ("T6", "User acceptance testing", "Client", 6, ["T5"], 0),
    ("T7", "Train key users", "Analyst", 4, ["T5"], 0),
    ("T8", "Go or no-go meeting", "PM", 1, ["T6", "T7"], 0),
    ("T9", "Cutover weekend", "Engineer", 2, ["T8"], 0),
    ("T10", "Hypercare", "Engineer", 10, ["T9"], 0),
]

# line, planned, actual to date, estimate to complete
BUDGET = [
    ("Discovery and mapping", 60000.0, 61500.0, 0.0),
    ("Engineering", 190000.0, 118000.0, 99000.0),
    ("Data cleansing", 70000.0, 47000.0, 36000.0),
    ("Testing and training", 80000.0, 0.0, 91000.0),
    ("Project management", 60000.0, 31000.0, 33000.0),
    ("Contingency", 20000.0, 0.0, 20000.0),
]

# id, description, probability 1-5, impact 1-5, owner, mitigation, last review
RISKS = [
    ("R1", "Duplicate customers exceed estimate and delay the trial", 4, 4, "Analyst", "Match rules agreed early, weekly count", date(2026, 10, 12)),
    ("R2", "Client users unavailable for acceptance testing", 3, 5, "PM", "Book testers now, name a backup", date(2026, 9, 28)),
    ("R3", "Old export format changes without notice", 2, 3, "Engineer", "Freeze export, add a schema check", date(2026, 10, 5)),
    ("R4", "Cutover weekend clashes with a sales campaign", 2, 4, "PM", "Agree the date with the client marketing lead", date(2026, 9, 14)),
    ("R5", "Personal data copied to a test system", 2, 5, "Engineer", "Mask names and emails in test", date(2026, 10, 15)),
]

# id, description, raised, owner, status
ISSUES = [
    ("I1", "Address field has two formats in the old system", date(2026, 9, 21), "Analyst", "open"),
    ("I2", "Test environment not ready for the trial", date(2026, 10, 14), "Engineer", "open"),
    ("I3", "Client has not named a UAT lead", date(2026, 10, 1), "Client", "open"),
    ("I4", "Scope question on loyalty points", date(2026, 9, 10), "PM", "closed"),
]

# person, role, then percent allocation for 6 weeks starting 2026-10-19
RESOURCES = [
    ("Analyst", "Business analyst", [60, 100, 100, 80, 80, 40]),
    ("Engineer", "Data engineer", [100, 100, 120, 100, 100, 100]),
    ("PM", "Project manager", [50, 50, 60, 60, 80, 80]),
]
RESOURCE_START = date(2026, 10, 19)

# stakeholder, interest, influence, how often, channel
STAKEHOLDERS = [
    ("Client sponsor", "high", "high", "weekly", "status report and call"),
    ("Client marketing lead", "medium", "high", "every two weeks", "email and meeting"),
    ("Client IT contact", "high", "medium", "twice a week", "stand-up"),
    ("Project team", "high", "medium", "daily", "stand-up"),
]
