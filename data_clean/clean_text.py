import re
from shutil import which

input_files = [
    "data_raw/les_miserables_en.txt",
    "data_raw/monte_cristo_en.txt"
]

output_file = "data_clean/books_clean.txt"

with open(output_file, "w", encoding="utf-8") as out:
    for file in input_files:
        with open(file, "r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                line = line.lower()
                line = re.sub(r"[^a-z\s]", " ", line)
                line = re.sub(r"\s+", " ", line)
                out.write(line.strip() + "\n")
