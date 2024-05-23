# Thermodynamic Data Excel File

<p style="font-size: 1.2em;">The Excel file databank contains various thermodynamic data relevant for subsurface hydrogen storage. 
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

- Pressure ($p$) in MPa
- Temperature ($T$) in K
- Salt concentration ($c_\mathrm{salt}$) in moles of salt per kg of H<sub>2</sub>O
- Salt concentration ($M_\mathrm{salt}$) in moles of salt per L of H<sub>2</sub>O
- Uncertainty in a computed quantity ($\sigma$) in the same unit as the quantity
- Density ($\rho$) in kg/m<sup>3</sup>
- Compressibility ($Z$) in dimensionless units
- Thermodynamic Factor ($\Gamma$) in dimensionless units
- Interfacial Tension ($\gamma$) in N/m
- Viscosity ($\eta$) in mPas or $\mu$Pas
- Self-diffusivity ($D_\mathrm{self}$) in m<sup>2</sup>/s
- Maxwell Stefan diffusivity ($D^\text{MS}$) in units 
- Fick diffusivity ($D^\mathrm{Fick}$)
- Excess Chemical Potential ($\frac{\mu^\mathrm{Ex}}{k_{B}T}$) in dimensionless units
- Solubility in liquid phase ($s$) in moles per gas per kg of H<sub>2</sub>O
- Solubility in liquid phase as mole fraction ($x$) in dimensionless units
- Solubility in gas phase as mole fraction ($y$) in dimensionless units
- Fugacity coefficient ($\phi$) in dimensionless units

## Sheet Descriptions

### <span style="color: #4CAF50;">1. IFT H<sub>2</sub>-Brine</span>
- **Properties**: 
    - $\large \gamma(p,T,c_\mathrm{NaCl})$ of H<sub>2</sub>-NaCl Brine systems computed from MD simulations (Ref. [6]).
- **Range of data**: 
    - $\large p \in [0.1, 60]$
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




## References 

- [1] A. P. Thompson, H. M. Aktulga, R. Berger, D. S. Bolintineanu, W. M. Brown, P. S. Crozier, P. J. in 't Veld, A. Kohlmeyer, S. G. Moore, T. D. Nguyen, R. Shan, M. J. Stevens, J. Tranchida, C. Trott, S. J. Plimpton, "LAMMPS - a flexible simulation tool for particle-based materials modeling at the atomic, meso, and continuum scales," _Computer Physics Communications_, 271 (2022) 10817. 
- [2] Seyed Hossein Jamali, Ludger Wolff, Tim M. Becker, Mariëtte de Groen, Mahinder Ramdin, Remco Hartkamp, André Bardow, Thijs J. H. Vlugt, and Othonas A. Moultos, "OCTP: A Tool for On-the-Fly Calculation of Transport Properties of Fluids with the Order-n Algorithm in LAMMPS," _Journal of Chemical Information and Modeling_, 2019, 59 (4), 1290-1294. DOI: [10.1021/acs.jcim.8b00939](https://doi.org/10.1021/acs.jcim.8b00939)
- [3] Remco Hens, Ahmadreza Rahbari, Sebastián Caro-Ortiz, Noura Dawass, Máté Erdős, Ali Poursaeidesfahani, Hirad S. Salehi, Alper T. Celebi, Mahinder Ramdin, Othonas A. Moultos, David Dubbelda m, and Thijs J. H. Vlugt, "Brick-CFCMC: Open Source Software for Monte Carlo Simulations of Phase and Reaction Equilibria Using the Continuous Fractional Component Method," _Journal of Chemical Information and Modeling_, 2020, 60 (6), 2678-2682. DOI: [10.1021/acs.jcim.0c00334](https://doi.org/10.1021/acs.jcim.0c00334)
- [4] H. Mert Polat, Hirad S. Salehi, Remco Hens, Dominika O. Wasik, Ahmadreza Rahbari, Frédérick de Meyer, Céline Houriez, Christophe Coquelet, Sofia Calero, David Dubbeldam, Othonas A. Moultos, and Thijs J. H. Vlugt, "New Features of the Open Source Monte Carlo Software Brick-CFCMC: Thermodynamic Integration and Hybrid Trial Moves," _Journal of Chemical Information and Modeling_, 2021, 61 (8), 3752-3757. DOI: [10.1021/acs.jcim.1c00652](https://doi.org/10.1021/acs.jcim.1c00652)
- [5] Rahbari, A., Hens, R., Ramdin, M., Moultos, O. A., Dubbeldam, D., & Vlugt, T. J. H. (2021). "Recent advances in the continuous fractional component Monte Carlo methodology," _Molecular Simulation_, 47(10–11), 804–823. DOI: [10.1080/08927022.2020.1828585](https://doi.org/10.1080/08927022.2020.1828585)
- [6] W. A. van Rooijen, P. Habibi, K. Xu, P. Dey, T. J. H. Vlugt, H. Hajibeygi, and O. A. Moultos, "Interfacial Tensions, Solubilities, and Transport Properties of the H2/H2O/NaCl System: A Molecular Simulation Study," *Journal of Chemical & Engineering Data*, 2024, 69 (2), 307-319. DOI: [10.1021/acs.jced.2c00707](https://doi.org/10.1021/acs.jced.2c00707)
- [7] Thejas Hulikal Chakrapani, Hadi Hajibeygi, Othonas A. Moultos, and Thijs J. H. Vlugt, "Calculating Thermodynamic Factors for Diffusion Using the Continuous Fractional Component Monte Carlo Method," _Journal of Chemical Theory and Computation_, 2024, 20 (1), 333-347. DOI: [10.1021/acs.jctc.3c01144](https://doi.org/10.1021/acs.jctc.3c01144)
- [8] Lemmon, E. W.; Bell, I. H.; Huber, M. L.; McLinden, M. O. "NIST Standard Reference Database 23: Reference Fluid Thermodynamic and Transport Properties-REFPROP, Version 10.0," National Institute of Standards and Technology, 2018. [https://www.nist.gov/srd/refprop](https://www.nist.gov/srd/refprop).


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

