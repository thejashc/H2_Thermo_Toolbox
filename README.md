# Thermodynamic Data Excel File

<p style="font-size: 1.2em;">This Excel file contains comprehensive thermodynamic data for various mixtures as a function of pressure, temperature, and salt concentration. It also includes comparisons with established thermodynamic databases.</p>

## Table of Contents

1. [Sheet Descriptions](#sheet-descriptions)
2. [Data Description](#data-description)
3. [Python Script for Data Extraction](#python-script-for-data-extraction)
4. [References](#references)
5. [Usage Instructions](#usage-instructions)

## Sheet Descriptions

### <span style="color: #4CAF50;">1. IFT H2-Brine</span>
- **Properties**: Interfacial Tensions (IFTs) of H2-NaCl Brine systems as functions of temperature, pressure, and NaCl salt concentration.
- **Description**: IFTs computed from MD simulations performed in the _NVT_ ensemble. Details are provided in Ref. [1]. 
- **Reference**: 
    - [1] W. A. van Rooijen, P. Habibi, K. Xu, P. Dey, T. J. H. Vlugt, H. Hajibeygi, and O. A. Moultos, "Interfacial Tensions, Solubilities, and Transport Properties of the H2/H2O/NaCl System: A Molecular Simulation Study," *Journal of Chemical & Engineering Data*, 2024, 69 (2), 307-319. DOI: [10.1021/acs.jced.2c00707](https://doi.org/10.1021/acs.jced.2c00707) 

### <span style="color: #4CAF50;">1. H2 Self-Diffusion in H2O</span>
- **Description**: Contains data on the infinite dilution self-diffusion coefficient of hydrogen (H2) in water (H2O).
- **Properties**: Self-diffusion coefficients as a function of temperature and pressure.
- **References**: Relevant literature and databases used for data collection.

### <span style="color: #4CAF50;">2. H2-CO2 Mix & Transport</span>
- **Description**: Provides mixture and transport properties of hydrogen (H2) and carbon dioxide (CO2).
- **Properties**: Viscosity, thermal conductivity, and diffusivity data for various temperatures and pressures.
- **References**: Relevant literature and databases used for data collection.

### <span style="color: #4CAF50;">3. [Other Sheets]</span>
- **Description**: [Brief description of other sheets in your file]
- **Properties**: [List of properties covered]
- **References**: [Sources of data]

## Data Description

<p style="font-size: 1.1em;">
- <b>Pressure (P)</b>: Measured in [units, e.g., Pascals (Pa) or atmospheres (atm)].<br>
- <b>Temperature (T)</b>: Measured in degrees Celsius (°C) or Kelvin (K).<br>
- <b>Salt Concentration</b>: Measured in [units, e.g., molarity (M) or percentage (%)].<br>
- <b>Mixtures</b>: Detailed data on various binary and ternary mixtures.<br>
- <b>Comparison</b>: Comparison data with recognized thermodynamic databases such as [Name of Database].
</p>

## Python Script for Data Extraction

<p style="font-size: 1.1em;">A Python script is available to help users extract data from this Excel file efficiently. The script allows users to:</p>

<ul>
  <li>Select specific sheets and columns of interest.</li>
  <li>Filter data based on specified criteria (e.g., temperature, pressure).</li>
  <li>Export filtered data for further analysis.</li>
</ul>

### How to Use the Python Script

1. **Setup**:
   - Ensure you have Python installed on your system.
   - Install required libraries using `pip install -r requirements.txt`.

2. **Running the Script**:
   - Place the Python script (`extract_data.py`) in the same directory as the Excel file.
   - Modify the script parameters to select the desired data.
   - Run the script using `python extract_data.py`.

3. **Output**:
   - The script will output the extracted data to a new file or display it as specified.

### Script Example

```python
import pandas as pd

# Load the Excel file
file_path = 'thermodynamic_data.xlsx'
sheet_name = 'H2 Self-Diffusion in H2O'

# Read the data from the specified sheet
data = pd.read_excel(file_path, sheet_name=sheet_name)

# Display the first few rows of the data
print(data.head())

