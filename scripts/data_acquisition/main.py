
import kagglehub
from kagglehub import KaggleDatasetAdapter

# Set the path to the file you'd like to load
file_path = "global_climate_energy_2020_2024.csv"

# Load the latest version
df = kagglehub.load_dataset(
  KaggleDatasetAdapter.PANDAS,
  "emirhanakku/climate-and-energy-consumption-dataset-20202024",
  file_path,
)
