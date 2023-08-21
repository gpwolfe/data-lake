# Contribute Content
  
### Contributor

#### Name:
<!-- Enter your name -->

#### Email:
<!-- Enter your email. This will be used for correspondence about dataset submission -->
  

### Dataset

#### Dataset name:
<!-- Enter dataset name -->

#### Author list:
<!-- Enter list of dataset author names as "FirstName1 LastName1, FirstName2 LastName2". Do not use initials unless author is normally attributed by initial(s) -->

#### Links:
<!-- Enter list of resources describing dataset (DOI if available). Include DOI/URL for dataset, if aleady hosted online -->
  
#### Elements list:
<!-- List elements present in dataset using elemental symbols (e.g., Si, Al, C, etc.) -->

#### Software:
<!-- Enter the software and version used for property calculations (e.g., VASP 5.4.1, ORCA 5.0.3) -->


#### Method:
<!-- Enter the method used for property calculations (e.g., DFT, CCSD, CCSD(T)) -->

#### Functional:
<!-- Enter the functional used for property calculations (e.g., PBE, PBEsol, B3LYP, SCAN) -->

#### Basis set:
<!-- Enter the basis set used for property calculations (e.g., cc-pVDZ, aug-cc-PVTZ) -->

#### Configuration name key:
<!-- A configuration’s name will be used for grouping and label application. Names will default to file names if no key is provided. In an extended XYZ file, for example, setting the Configuration Name Key to an existing key "config_name" would use the values provided by this key to name configurations -->


#### Property Definitions
<!-- Select a predefined property if applicable to your data. See definitions at https://github.com/colabfit/colabfit-tools/blob/development/colabfit/tools/property_definitions.py.

To select a property, replace the corresponding "[ ]" with "[x]" or "[X]".
- [X] example property

If a predefined property definition listed above does not apply to your content, you may submit new property definition files with your dataset files. Examples may be found in the file "example_property_definitions.py.-->

- [ ] potential energy
- [ ] atomic forces
- [ ] cauchy stress


### Configuration Sets
<!-- Configuration sets are used to organize and group similar Configurations with one another. These could be similar structures, similar methods, etc.

A Configuration Set’s Extended ID is constructed according to {Name}_{Short ID}. "Name" can be used to lend interpretability to an Extended ID.

Configuration Sets are constructed using regular expressions to match and group Configurations based on their name (remember that the names of Configurations are obtained from the specified "Configuration Name Key"). 

You may create as many configuration sets as needed. -->


#### Name:  
<!-- Enter name used to construct an Extended ID for the Configuration set. -->  
#### Description:  
<!-- Enter human-readable description of the configurations in the set -->  
#### Regex:  
<!-- Enter a regular expression for matching to configuration names -->  


### Configuration Labels
<!-- If necessary, more specific labels can be added to Configurations for querying purposes. Similar to the construction of Configuration Sets, regular expressions are matched against a Configuration’s name. 

You may create as many labels as needed -->

#### Labels: 
<!-- Labels to attach to the matching configurations -->  
#### Regex: 
<!-- Regular expression for matching to configuration names -->


### Distribution License
<!-- Enter the license under which the content will be distributed (e.g. Creative Commons Zero) -->
#### License:

### Comments
<!-- Enter any additional comments for the reviewer below -->