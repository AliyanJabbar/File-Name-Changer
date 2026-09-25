from pathlib import Path
import re

# Current directory
FOLDER = Path(__file__).resolve().parent

# Only image files
IMAGE_EXTENSIONS = {
    ".jpg", ".jpeg", ".png", ".webp",
    ".gif", ".bmp", ".tiff", ".svg"
}

files = [
    f for f in FOLDER.iterdir()
    if f.is_file() and f.suffix.lower() in IMAGE_EXTENSIONS
]

# Sort according to the number at the beginning of the filename
files.sort(
    key=lambda f: (
        int(re.match(r"^\d+", f.stem).group())
        if re.match(r"^\d+", f.stem)
        else float("inf")
    )
)

# Step 1: Temporary names
temp_files = []

for index, file in enumerate(files, start=1):
    temp_name = FOLDER / f"__temp_{index}{file.suffix}"
    file.rename(temp_name)
    temp_files.append(temp_name)

# Step 2: Final sequential names
for index, file in enumerate(temp_files, start=1):
    final_name = FOLDER / f"{index}{file.suffix}"
    file.rename(final_name)

print(f"Successfully renamed {len(files)} images.")