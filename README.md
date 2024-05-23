# Thermodynamic Data Excel File

<p style="font-size: 1.2em;">The Excel file dataBank.xlsx contains various thermodynamic data relevant for subsurface hydrogen storage. 
These thermodynamic data are computed from Molecular Dynamics (MD) and Monte Carlo (MC) simulations using the open-source softwares 
LAMMPS (Refs. [1] and [2] ) and Brick CFCMC (Refs. [4]-[6]).The applicability of the data is not restricted to subsurface hydrogen storage only. 
Where available, the computed thermodynamic properties are compared with the thermodynamic database REFPROP (Ref. [8]).

## Table of Contents

1. [Sheet Descriptions](#sheet-descriptions)
2. [Notations and Units](#Notations-and-Units)
3. [Python Script for Data Extraction](#python-script-for-data-extraction)
4. [References](#references)
5. [Usage Instructions](#usage-instructions)

## Notations and Units

- $\large p$ : Pressure [MPa]
- $\large T$ : Temperature [K]
- $\large c_\mathrm{salt}$ : Salt concentration [moles of salt per kg of H<sub>2</sub>O]
- $\large M_\mathrm{salt}$ : Salt concentration [moles of salt per L of H<sub>2</sub>O]
- $\large \sigma_{A}$ : Statistical uncertainty in the computation of the thermodynamic property $A$ in units same as $A$
- $\large \rho$ : Density [kg/m<sup>3</sup>]
- $\large Z$ : Compressibility []
- $\large \Gamma$ : Thermodynamic Factor []
- $\large \gamma$ : Interfacial Tension [N/m]
- $\large \eta$ : Viscosity [Pas]
- $\large D^\mathrm{self}_{i}$ : Self-diffusivity of species $i$ [m<sup>2</sup>/s]
- $\large D^\text{MS}_{ij}$ : Maxwell-Stefan diffusivity of a mixture of $i$ and $j$ [m<sup>2</sup>/s]
- $\large D^\mathrm{Fick}_{ij}$ : Fick diffusivity of a mixture of $i$ and $j$ [m<sup>2</sup>/s]
- $\large \frac{\mu^\mathrm{Ex}}{k_{B}T}$ : Excess Chemical Potential of specie $i$ expressed in units of $k_{B}T$ where $k_{B}$ is Boltzmann constant []
- $\large s_{i}$ : Solubility of specie $i$ in the liquid phase [moles per gas per kg of H<sub>2</sub>O]
- $\large x_{i}$ : Solubility of specie $i$ in liquid phase expressed as a mole fraction []
- $\large y_{i}$ : Solubility of specie $i$ in gas phase expressed as a mole fraction []
- $\large \phi_{i}$ : Fugacity coefficient of species $i$ in the gas-phase []
- $\large \mathrm{mf}_{i}$ : Mole fraction of species $i$ in a mixture 

## Sheet Descriptions

### <span style="color: #4CAF50;">1. IFT H<sub>2</sub>-Brine</span>
- **Properties**: 
    - $\large \gamma(p,T,c_\mathrm{NaCl})$ of H<sub>2</sub>-NaCl Brine systems computed from MD simulations (Ref. [6]).
- **Range of data**: 
    - $\large p \in [0.1, 60]$ MPa
    - $\large T \in [298, 373]$ K
    - $\large c_\mathrm{NaCl} \in [0,5]$ mol of NaCl per kg of H<sub>2</sub>O
- **Description**: Mixtures considered here contain gaseous and liquid phases dominated by H<sub>2</sub> and H<sub>2</sub>O, respectively.

### <span style="color: #4CAF50;">2. Mixture properties H<sub>2</sub>-Brine
- **Properties**: 
    - $\large \rho(p,T,c_\mathrm{NaCl})$ of H<sub>2</sub>-NaCl Brine systems computed from MD simulations (Ref. [6]).
- **Range of data**: 
    - $\large p \in [0.1, 100]$
    - $\large T \in [298, 723]$ K
    - $\large c_\mathrm{NaCl} \in [0,6]$ mol of NaCl per kg of H<sub>2</sub>O
- **Description**: Data reported are for liquid-phase mixtures.

### <span style="color: #4CAF50;">3. Transport properties of H<sub>2</sub>-Brine
- **Properties**: 
    - $\large \eta(p,T,c_\mathrm{NaCl})$ of NaCl Brine systems computed from MD simulations (Ref. [6]).
    - $\Large D^\mathrm{self}_\mathrm{H_2}$ in NaCl Brine systems computed from MD simulations (Ref. [6]).
- **Range of data**: 
    - $\large p \in [0.1, 100]$
    - $\large T \in [298, 723]$ K
    - $\large c_\mathrm{NaCl} \in [0,6]$ mol of NaCl per kg of H<sub>2</sub>O
- **Description**: Data reported are for liquid-phase mixtures.

### <span style="color: #4CAF50;">4. VLE H<sub>2</sub>-Brine
- **Properties**: 
    - $\large \rho(p,T,c_\mathrm{NaCl})$ of H<sub>2</sub>NaCl Brine systems computed from CFCMC simulations (Ref. [6]).
    - $\large \mu^\mathrm{Ex}/k_{B}T(p,T,c_\mathrm{NaCl})$ of H<sub>2</sub> in H<sub>2</sub>-Brine systems computed from CFCMC simulations (Ref. [6])
    - $\large s_\mathrm{H_{2}}, x_\mathrm{H_{2}}(p,T,c_\mathrm{NaCl})$ in NaCl Brine systems computed from CFCMC simulations (Ref. [6])
- **Range of data**: 
    - $\large p \in [0.1, 100]$
    - $\large T \in [298, 363]$ K
    - $\large c_\mathrm{NaCl} \in [0,6]$ mol of NaCl per kg of H<sub>2</sub>O
- **Description**: Data reported are for liquid-phase mixtures.

### <span style="color: #4CAF50;">5. Mixture properties H<sub>2</sub>-CO<sub>2</sub> 
- **Properties**: 
    - $\large \rho(p,T,\mathrm{mf}_\mathrm{H_2})$ of H<sub>2</sub>-CO<sub>2</sub> mixtures computed from MD simulations (Ref. [6]).
    - $\large \Gamma(p,T,\mathrm{mf}_\mathrm{H_2})$ of H<sub>2</sub>-CO<sub>2</sub> mixtures computed from MD simulations (Ref. [6]).
    - $\large Z(p,T,\mathrm{mf}_\mathrm{H_2})$ of H<sub>2</sub>-CO<sub>2</sub> mixtures taken from MD simulations (Ref. [8]).
    - $\large Z(p,T,\mathrm{mf}_\mathrm{H_2})$ of H<sub>2</sub>-CO<sub>2</sub> mixtures taken from REFPROP database (Ref. [9]).
- **Range of data**: 
    - $\large p \in [5, 50]$ MPa
    - $\large T \in [323.15, 423.15]$ K
    - $\large \mathrm{mf}_\mathrm{H_2} \in [0,1]$ 
- **Description**: Values of $\Gamma$ are computed from the Gibbs free energies taken from the REFPROP database (Ref. [9]).

### <span style="color: #4CAF50;">5. Transport properties H<sub>2</sub>-CO<sub>2</sub> 
- **Properties**: 
    - $\large \eta(p,T,\mathrm{mf}_\mathrm{H_2})$ of H<sub>2</sub>-CO<sub>2</sub> mixtures computed from MD simulations (Ref. [8]).
    - $\large \eta(p,T,\mathrm{mf}_\mathrm{H_2})$ of H<sub>2</sub>-CO<sub>2</sub> mixtures taken from REFPROP database (Ref. [8]).
    - $\large D_\mathrm{H_2}^\mathrm{self}(p,T,\mathrm{mf}_\mathrm{H_2})$ of H<sub>2</sub>-CO<sub>2</sub> mixtures taken from MD simulations (Ref. [8]).
    - $\large D_\mathrm{CO_2}^\mathrm{self}(p,T,\mathrm{mf}_\mathrm{H_2})$ of H<sub>2</sub>-CO<sub>2</sub> mixtures taken from MD simulations (Ref. [8]).
    - $\large D^\mathrm{MS}(p,T,\mathrm{mf}_\mathrm{H_2})$ of H<sub>2</sub>-CO<sub>2</sub> mixtures taken from MD simulations (Ref. [8]).
    - $\large D^\mathrm{Fick}(p,T,\mathrm{mf}_\mathrm{H_2})$ of H<sub>2</sub>-CO<sub>2</sub> mixtures taken from MD simulations (Ref. [8]).
- **Range of data**: 
    - $\large p \in [5, 50]$ MPa
    - $\large T \in [323.15, 423.15]$ K
    - $\large \mathrm{mf}_\mathrm{H_2} \in [0,1]$ 
- **Description**: 

### <span style="color: #4CAF50;">6. VLE H<sub>2</sub>-CO<sub>2</sub>-Brine
- **Properties**: 
    - $\large x_\mathrm{H_{2}}(p,T,c_\mathrm{NaCl})$ in liquid phase computed from CFCMC simulations (Ref. [8])
    - $\large x_\mathrm{CO_{2}}(p,T,c_\mathrm{NaCl})$ in liquid phase computed from CFCMC simulations (Ref. [8])
    - $\large x_\mathrm{H_{2}O}(p,T,c_\mathrm{NaCl})$ in liquid phase computed from CFCMC simulations (Ref. [8])
    - $\large y_\mathrm{H_{2}}(p,T,c_\mathrm{NaCl})$ in gas-phase computed from CFCMC simulations (Ref. [8])
    - $\large y_\mathrm{CO_{2}}(p,T,c_\mathrm{NaCl})$ in gas-phase computed from CFCMC simulations (Ref. [8])
    - $\large y_\mathrm{H_{2}O}(p,T,c_\mathrm{NaCl})$ in gas-phase computed from CFCMC simulations (Ref. [8])
    - $\large \phi_\mathrm{H_{2}}(p,T,c_\mathrm{NaCl})$ in gas-phase computed from CFCMC simulations (Ref. [8])
    - $\large \phi_\mathrm{CO_{2}}(p,T,c_\mathrm{NaCl})$ in gas-phase computed from CFCMC simulations (Ref. [8])
    - $\large \phi_\mathrm{H_{2}O}(p,T,c_\mathrm{NaCl})$ in gas-phase computed from CFCMC simulations (Ref. [8])
    - $\large \phi_\mathrm{H_{2}}(p,T,c_\mathrm{NaCl})$ in gas-phase computed from REFPROP simulations (Ref. [8])
    - $\large \phi_\mathrm{CO_{2}}(p,T,c_\mathrm{NaCl})$ in gas-phase computed from REFPROP simulations (Ref. [8])
    - $\large \phi_\mathrm{H_{2}O}(p,T,c_\mathrm{NaCl})$ in gas-phase computed from REFPROP simulations (Ref. [8])
- **Range of data**: 
    - $\large p \in [5, 50]$ MPa
    - $\large T \in [323.15, 423.15]$ K
    - $\large c_\mathrm{NaCl} \in [0,2]$ mol of NaCl per kg of H<sub>2</sub>O
- **Description**: 
    - VLE in H<sub>2</sub>-CO<sub>2</sub>-H<sub>2</sub>O mixtures is calculated for a single mixture composition of [0.25, 0.25, 0.5]
    - VLE for binary mixtures of H<sub>2</sub>-H<sub>2</sub>O and CO<sub>2</sub>-H<sub>2</sub>O mixtures are also tabulated in the excel sheet
    - The liquid phase is predominantly NaCl brine.
    - The gas phase consists mainly of H<sub>2</sub>, CO<sub>2</sub>, or a mixture of H<sub>2</sub> and CO<sub>2</sub>.
      
## References 

- [1] A. P. Thompson, H. M. Aktulga, R. Berger, D. S. Bolintineanu, W. M. Brown, P. S. Crozier, P. J. in 't Veld, A. Kohlmeyer, S. G. Moore, T. D. Nguyen, R. Shan, M. J. Stevens, J. Tranchida, C. Trott, S. J. Plimpton, "LAMMPS - a flexible simulation tool for particle-based materials modeling at the atomic, meso, and continuum scales," _Computer Physics Communications_, 271 (2022) 10817. 
- [2] Seyed Hossein Jamali, Ludger Wolff, Tim M. Becker, Mariëtte de Groen, Mahinder Ramdin, Remco Hartkamp, André Bardow, Thijs J. H. Vlugt, and Othonas A. Moultos, "OCTP: A Tool for On-the-Fly Calculation of Transport Properties of Fluids with the Order-n Algorithm in LAMMPS," _Journal of Chemical Information and Modeling_, 2019, 59 (4), 1290-1294. DOI: [10.1021/acs.jcim.8b00939](https://doi.org/10.1021/acs.jcim.8b00939)
- [3] Remco Hens, Ahmadreza Rahbari, Sebastián Caro-Ortiz, Noura Dawass, Máté Erdős, Ali Poursaeidesfahani, Hirad S. Salehi, Alper T. Celebi, Mahinder Ramdin, Othonas A. Moultos, David Dubbeldam, and Thijs J. H. Vlugt, "Brick-CFCMC: Open Source Software for Monte Carlo Simulations of Phase and Reaction Equilibria Using the Continuous Fractional Component Method," _Journal of Chemical Information and Modeling_, 2020, 60 (6), 2678-2682. DOI: [10.1021/acs.jcim.0c00334](https://doi.org/10.1021/acs.jcim.0c00334)
- [4] H. Mert Polat, Hirad S. Salehi, Remco Hens, Dominika O. Wasik, Ahmadreza Rahbari, Frédérick de Meyer, Céline Houriez, Christophe Coquelet, Sofia Calero, David Dubbeldam, Othonas A. Moultos, and Thijs J. H. Vlugt, "New Features of the Open Source Monte Carlo Software Brick-CFCMC: Thermodynamic Integration and Hybrid Trial Moves," _Journal of Chemical Information and Modeling_, 2021, 61 (8), 3752-3757. DOI: [10.1021/acs.jcim.1c00652](https://doi.org/10.1021/acs.jcim.1c00652)
- [5] Rahbari, A., Hens, R., Ramdin, M., Moultos, O. A., Dubbeldam, D., & Vlugt, T. J. H. (2021). "Recent advances in the continuous fractional component Monte Carlo methodology," _Molecular Simulation_, 47(10–11), 804–823. DOI: [10.1080/08927022.2020.1828585](https://doi.org/10.1080/08927022.2020.1828585)
- [6] W. A. van Rooijen, P. Habibi, K. Xu, P. Dey, T. J. H. Vlugt, H. Hajibeygi, and O. A. Moultos, "Interfacial Tensions, Solubilities, and Transport Properties of the H2/H2O/NaCl System: A Molecular Simulation Study," _Journal of Chemical & Engineering Data_, 2024, 69 (2), 307-319. DOI: [10.1021/acs.jced.2c00707](https://doi.org/10.1021/acs.jced.2c00707)
- [7] Thejas Hulikal Chakrapani, Hadi Hajibeygi, Othonas A. Moultos, and Thijs J. H. Vlugt, "Calculating Thermodynamic Factors for Diffusion Using the Continuous Fractional Component Monte Carlo Method," _Journal of Chemical Theory and Computation_, 2024, 20 (1), 333-347. DOI: [10.1021/acs.jctc.3c01144](https://doi.org/10.1021/acs.jctc.3c01144)
- [8] Thejas Hulikal Chakrapani, Hadi Hajibeygi, O. A. Moultos, and Thijs. J. H. Vlugt, "Mutual diffusivities of mixtures of carbon dioxide and hydrogen and their solubilities in brine: Insight from molecular simulations," Accepted for Publication in _Industrial & Engineering Chemistry Research_, 2024 
- [9] Lemmon, E. W., Bell, I. H., Huber, M. L., McLinden, M. O. "NIST Standard Reference Database 23: Reference Fluid Thermodynamic and Transport Properties-REFPROP, Version 10.0," National Institute of Standards and Technology, 2018. [https://www.nist.gov/srd/refprop](https://www.nist.gov/srd/refprop).

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
   - Install the required library using:
     ```sh
     pip install pandas
     ```

2. **Running the Script**:
   - Place the Python script (`extract_data.py`) in the same directory as the Excel file (`databank.xlsx`).
   - Modify the script parameters if necessary to match your specific file and data requirements.
   - Run the script using:
     ```sh
     python extract_data.py
     ```

3. **Output**:
   - The script will prompt you to select sheets and columns and then output the extracted data to a new file or display it as specified.

### Script Example

```python
import pandas as pd

def get_sheet_names(file_path):
    """
    Get all sheet names from the Excel file.
    
    :param file_path: Path to the Excel file.
    :return: List of sheet names.
    """
    try:
        excel_file = pd.ExcelFile(file_path)
        return excel_file.sheet_names
    except Exception as e:
        print(f"An error occurred while fetching sheet names: {e}")
        return []

def get_available_columns(file_path, sheet_name):
    """
    Get the available columns from the specified sheet in the Excel file.
    
    :param file_path: Path to the Excel file.
    :param sheet_name: Name of the sheet to read data from.
    :return: List of column names.
    """
    try:
        df = pd.read_excel(file_path, sheet_name=sheet_name, nrows=0)  # Read only the header row
        return list(df.columns)
    except Exception as e:
        print(f"An error occurred while fetching columns: {e}")
        return []

def import_selected_columns(file_path, sheet_name, columns):
    """
    Import selected columns from an Excel sheet.
    
    :param file_path: Path to the Excel file.
    :param sheet_name: Name of the sheet to read data from.
    :param columns: List of columns to import.
    :return: DataFrame containing the selected columns.
    """
    try:
        data = pd.read_excel(file_path, sheet_name=sheet_name, usecols=columns)
        return data
    except Exception as e:
        print(f"An error occurred while importing data: {e}")
        return None

def export_data(data, file_name, file_format):
    """
    Export the DataFrame to the specified file format.
    
    :param data: DataFrame to be exported.
    :param file_name: Name of the output file.
    :param file_format: Format of the output file ('xlsx', 'csv', or 'dat').
    """
    try:
        if file_format == 'xlsx':
            data.to_excel(f"{file_name}.xlsx", index=False)
        elif file_format == 'csv':
            data.to_csv(f"{file_name}.csv", index=False)
        elif file_format == 'dat':
            data.to_csv(f"{file_name}.dat", index=False, sep='\t')
        print(f"Data exported successfully to {file_name}.{file_format}")
    except Exception as e:
        print(f"An error occurred while exporting data: {e}")

def main():
    # Known file path
    file_path = "databank.xlsx"  # Change this to your file path

    # Get all sheet names
    sheet_names = get_sheet_names(file_path)

    if not sheet_names:
        print("No sheets found or unable to read the file.")
        return

    # Display available sheet names
    print("Available sheet names:")
    for idx, sheet in enumerate(sheet_names):
        print(f"{idx + 1}. {sheet}")

    # User input for sheet name
    while True:
        try:
            sheet_idx = int(input("Enter the number corresponding to the sheet name you want to use: ")) - 1
            if sheet_idx < 0 or sheet_idx >= len(sheet_names):
                print(f"Invalid selection. Please enter a number between 1 and {len(sheet_names)}.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    sheet_name = sheet_names[sheet_idx]

    # Get available columns
    available_columns = get_available_columns(file_path, sheet_name)

    if not available_columns:
        print("No columns found or unable to read the sheet.")
        return

    print("Available columns:")
    for idx, col in enumerate(available_columns):
        print(f"{idx + 1}. {col}")

    # User input for columns to import
    while True:
        try:
            column_indices = input("Enter the numbers corresponding to the columns you want to import, separated by commas: ").split(',')
            column_indices = [int(idx.strip()) - 1 for idx in column_indices]
            if any(idx < 0 or idx >= len(available_columns) for idx in column_indices):
                print(f"Invalid selection. Please enter numbers between 1 and {len(available_columns)}.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter valid numbers.")

    columns = [available_columns[idx] for idx in column_indices]

    # Import the selected columns
    data = import_selected_columns(file_path, sheet_name, columns)

    # Display the imported data
    if data is not None:
        print("Imported Data:")
        print(data)
    else:
        print("Failed to import data.")
        return

    # User input for export format
    while True:
        export_format = input("Enter the export format (xlsx, csv, dat): ").strip().lower()
        if export_format in ['xlsx', 'csv', 'dat']:
            break
        else:
            print("Invalid format. Please enter 'xlsx', 'csv', or 'dat'.")

    # User input for export file name
    file_name = input("Enter the name for the output file (without extension): ").strip()

    # Export data
    export_data(data, file_name, export_format)

if __name__ == "__main__":
    main()
