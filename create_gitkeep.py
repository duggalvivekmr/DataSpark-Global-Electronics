import os
folders = [
    "data/raw",
    "data/clean",
    "notebooks",
    "sql",
    "dashboard",
    "media",
    "reports",
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)
    with open(os.path.join(folder, ".gitkeep"), "w") as f:pass

print("Palceholder files created.")
