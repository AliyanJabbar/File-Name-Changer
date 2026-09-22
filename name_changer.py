from pathlib import Path

PREFIX = "the_makeup_book_"

IMAGE_EXTENSIONS = {
    ".jpg",
    ".jpeg",
    ".png",
    ".webp",
    ".gif",
    ".bmp",
    ".tiff",
    ".tif",
}

current_directory = Path.cwd()

for image in current_directory.iterdir():
    if not image.is_file():
        continue

    if image.suffix.lower() not in IMAGE_EXTENSIONS:
        continue

    # Skip files that already have the prefix
    if image.name.startswith(PREFIX):
        continue

    new_name = f"{PREFIX}{image.name}"
    new_path = image.with_name(new_name)

    # Avoid accidentally overwriting an existing file
    if new_path.exists():
        print(f"Skipped: {image.name} → {new_name} (already exists)")
        continue

    image.rename(new_path)
    print(f"Renamed: {image.name} → {new_name}")

print("\nDone!")