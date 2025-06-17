import os
import time
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = REPO_ROOT / "datasets"
README_FILE = REPO_ROOT / "README.md"

table_header = (
    "| Name of Dataset | Last Updated | Number of Data Points | Properties | Cite | DOI |\n"
    "|-----------------|--------------|------------------------|------------|------|-----|\n"
)

def get_file_info(filepath):
    stat = filepath.stat()
    last_updated = time.strftime('%Y-%m-%d', time.localtime(stat.st_mtime))
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            num_lines = sum(1 for _ in f)
    except:
        num_lines = "N/A"
    return filepath.name, last_updated, num_lines

def main():
    rows = []
    for file in DATA_DIR.glob("*"):
        if file.is_file():
            name, last_updated, num_points = get_file_info(file)
            row = f"| {name} | {last_updated} | {num_points} | - | - | - |"
            rows.append(row)

    full_table = "# Dataset Catalog\n\n" + table_header + "\n".join(rows) + "\n"

    with open(README_FILE, 'w', encoding='utf-8') as f:
        f.write(full_table)

if __name__ == "__main__":
    main()
