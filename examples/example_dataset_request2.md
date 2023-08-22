# Contribute content
​
## Contributor
> Contact information about the person requesting/uploading the data. Used for communication purposes.
​

**Name**: Josh Vita  
**Email**: vita1@llnl.gov  
​
## Dataset
> Any information necessary to help the ColabFit find and access the data, and to correctly cite relevant material. The "name" and "description" will be used when publishing to the ColabFit exchange, and should be human-readable.

**Name**:  
InP_JPCA2020  
​  
**Authors**:  
Mary Alice Cusentino, Mitchell A. Wood, Aidan P. Thompson  

**Links**:  
* https://pubs.acs.org/doi/10.1021/acs.jpca.0c02450  
* https://github.com/FitSNAP/FitSNAP/tree/master/examples/InP_JPCA2020

**Description**:  
This data set was used to generate a multi-element linear SNAP potential for InP as published in Cusentino, M.A. et. al, J. Chem. Phys. (2020). Intended to produce an interatomic potential for indium phosphide capable of capturing high-energy defects that result from radiation damage cascades.
​
## Calculations  
> Details regarding how the data was computed in order to improve reproducibility. Provide as much information as possible. Input files are highly encouraged.
​

**Method**: DFT  
**Software**: VASP  
**Additional details**: LDA XC-functional, PAW pseudopotential, Monkhorst-Pack k-point grid with spacings of 0.17 or 0.72 $Ang^{-1}$ depending upon system size, 500 eV plane wave cutoff.  
**Files**: VASP INCAR files are provided for each atomic configuration.  
​
### Included properties
> See [the current list of ColabFit property definitions](https://materials.colabfit.org/browse/property-definitions). If you believe your data does not match one of the existing definitions, then you must submit a new property definition following [the template provided in the examples folder](https://github.com/gpwolfe/colabfit-data/blob/main/examples/example_property_definitions.py).  

|Name|Units|Notes|
| --- | --- | --- |
| potential energy | eV | Reported relative to ground state structure, so they have all been shifted by subtracting off 3.48 eV/atom
| atomic forces | eV/Ang | |
| cauchy stress | GPA | Stored as full (3,3) stress tensor
## Configurations
> Basic information explaining the types of configurations in the dataset, and how they are organized.  


**Elements**: In, P  
**Number of configurations**: 1894  
​
### Naming convention
> If your configurations have names, please describe where their names can be found (e.g., as a field in an `ASE.Atoms.info` dictionary).
​
Each configuration is stored as a JSON file under `JSON/<group_name>/<config_name>`.  
The full file path can be taken as the name of the configuration.
​
### Configuration sets
> Configuration sets are used to define a conceptual grouping over a collection of atomic configurations. Configuration sets are constructed via regex filtering on configuration names.
​

|Regex|Description|
|---|---|
|^Bulk| Ground state configuration for bulk zincblende|
|^EOS| Bulk zincblende with uniform expansion and compression
|^Shear | Bulk zincblende with random cell shape modifications
|^Strain | Uniaxially strained bulk zinc blende
|^a(In|P) | Antisite defects in InP
|^aa$ | Diantisite defects
|^i(In\|P) | Interstitial defects in InP
|^vP | Vacancy defects in InP
|^vv | Divacancy defects in InP
### Configuration labels
> Configuration labels can be attached to your data to improve interpretability. This is done via regex matching on the configuration name.
​

| Regex | Label |
| --- | --- |
|^Bulk\|EOS\|Shear\|Strain | zincblende
| ^EOS | eos| 
| ^Shear\|Strain | strain
| ^a(In\|P) | antisite
| ^aa | diantisite
| ^i(In\|P) | interstitial
| ^v(In\|P\|v) | vacancy