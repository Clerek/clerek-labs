import os
import secrets
import shutil
from pathlib import Path

# =====================================
# CONFIGURATION
# =====================================

# Use direct path to your .bin directory: 
#ROOT = Path(r"REPLACE WITH PATH TO YOUR AMIIBO BIN FOLDER")

# Use the directory where the script is located: 
ROOT = Path(__file__).resolve().parent

# The number of copies you want:
COUNT = 50

# =====================================
# VALIDATION
# =====================================

if not ROOT.is_dir():
    raise SystemExit(f"Directory not found: {ROOT}")

# =====================================
# DISCOVER ORIGINAL AMIIBO
# =====================================

files = []

for directory, folders, filenames in os.walk(ROOT):
    directory = Path(directory)

    bin_names = {
        Path(name).stem.casefold()
        for name in filenames
        if Path(name).suffix.lower() == ".bin"
    }

    # Skip previously generated amiibo folders
    folders[:] = [
        folder for folder in folders
        if folder.casefold() not in bin_names
    ]

    for filename in filenames:
        if Path(filename).suffix.lower() == ".bin":
            files.append(directory / filename)

# =====================================
# GENERATE AMIIBO COPIES
# =====================================

created = 0
skipped = 0
processed = 0
invalid = 0

print(f"Found {len(files)} original amiibo files.\n")

for source in files:

    original = source.read_bytes()

    # Validate amiibo file size
    if len(original) != 540:
        print(f"Skipping {source.name}: invalid file size.")
        invalid += 1
        continue

    name = source.stem
    destination = source.parent / name

    # Create matching folder
    destination.mkdir(exist_ok=True)

    # Preserve original inside matching folder
    original_copy = destination / source.name

    if not original_copy.exists():
        shutil.copy2(source, original_copy)

    new_copies = 0

    for i in range(1, COUNT + 1):

        output = destination / f"{name} - {i:02d}.bin"

        # Preserve existing copies
        if output.exists():
            skipped += 1
            continue

        data = bytearray(original)

        # Randomize UID
        for offset in (1, 2, 4, 5, 6, 7):
            data[offset] = secrets.randbelow(256)

        # Recalculate UID check bytes
        data[3] = 0x88 ^ data[0] ^ data[1] ^ data[2]
        data[8] = data[4] ^ data[5] ^ data[6] ^ data[7]

        # Save randomized amiibo
        output.write_bytes(data)

        created += 1
        new_copies += 1

    processed += 1
    print(f"{name}: {new_copies} new copies created")

# =====================================
# SUMMARY
# =====================================

print("\n" + "=" * 45)
print(" COMPLETE")
print("=" * 45)
print(f"Original amiibo processed: {processed:,}")
print(f"New copies generated:      {created:,}")
print(f"Existing copies skipped:   {skipped:,}")
print(f"Invalid files skipped:     {invalid:,}")
print(f"Target copies per amiibo:  {COUNT:,}")
print("Original files preserved:  Yes")
