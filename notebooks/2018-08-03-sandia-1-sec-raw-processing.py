from pathlib import Path
from itertools import chain
import pandas as pd


def sandia2parquet(csvPaths, outputPath):
    """Combine Sandia raw files and save DataFrame in Parquet."""
    df = pd.concat(pd.read_csv(p, parse_dates=[[0, 1]], index_col=0) for p in csvPaths)
    df.drop_duplicates(inplace=True)
    df.sort_index(inplace=True) # ensure datetime is increasing
    df.to_parquet(outputPath)
    return outputPath

# Original Files
SANDIA = Path("/Volumes/Sandia")
DATA1 = SANDIA / "Sandia chamber data613626"
DATA2 = SANDIA / "Sandia chamberdata711"
DATA3 = SANDIA / "Sandia Chamber Data 711725"

# List Dry files
# Parent folder name irregular, sort each list separately then combine
PATTERN = "Dry_*.csv"
DRY_FILES = list(chain.from_iterable([
    sorted(DATA1.glob(PATTERN)),
    sorted(DATA2.glob(PATTERN)),
    sorted(DATA3.glob(PATTERN)),
]))

# List of Humid files
PATTERN = "Humid_*.csv"
HUMID_FILES = list(chain.from_iterable([
    sorted(DATA1.glob(PATTERN)),
    sorted(DATA2.glob(PATTERN)),
    sorted(DATA3.glob(PATTERN)),
]))

# Output files
DRY_PARQUET = Path("../data/dry-0613-0724-2018.parquet")
HUMID_PARQUET = Path("../data/humid-0613-0724-2018.parquet")

# Process raw files if parquet files don't exist
if not DRY_PARQUET.exists():
    sandia2parquet(DRY_FILES, DRY_PARQUET)
dry = pd.read_parquet(DRY_PARQUET)
if not HUMID_PARQUET.exists():
    sandia2parquet(HUMID_FILES, HUMID_PARQUET)
humid = pd.read_parquet(HUMID_PARQUET)

