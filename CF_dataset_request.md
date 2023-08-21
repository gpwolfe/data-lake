# Contribute Content
  
### [Contributor][cont]

#### [Name:][name]
<!-- Enter your name -->

#### [Email:][email]
<!-- Enter your email. This will be used for correspondence about dataset submission -->
  

### [Dataset][ds]

#### [Dataset name:][dname]
<!-- Enter dataset name -->

#### [Author list:][auth]
<!-- Enter list of dataset author names as "FirstName1 LastName1, FirstName2 LastName2". Do not use initials unless author is normally attributed by initial(s) -->

#### [Links:][link]
<!-- Enter list of resources describing dataset (DOI if available). Include DOI/URL for dataset, if aleady hosted online -->
  
#### [Elements list:][elem]
<!-- List elements present in dataset using elemental symbols (e.g., Si, Al, C, etc.) -->

#### [Software:][soft]
<!-- Enter the software and version used for property calculations (e.g., VASP 5.4.1, ORCA 5.0.3) -->


#### [Method:][meth]
<!-- Enter the method(s) used for property calculations (e.g., DFT, CCSD, CCSD(T)) -->

#### [Functional:][func]
<!-- Enter the functional(s) used for property calculations (e.g., PBE, PBEsol, B3LYP, SCAN) -->

#### [Basis set:][bset]
<!-- Enter the basis set used for property calculations (e.g., cc-pVDZ, aug-cc-PVTZ) -->

#### [Property Definitions][pd]
<!-- Select a predefined property if applicable to your data. See definitions at https://github.com/colabfit/colabfit-tools/blob/development/colabfit/tools/property_definitions.py.

To select a property, replace the corresponding "[ ]" with "[x]" or "[X]".
- [X] example property

If a predefined property definition listed above does not apply to your content, you may submit new property definition files with your dataset files. Examples may be found in the file "example_property_definitions.py.-->

- [ ] potential energy
- [ ] atomic forces
- [ ] cauchy stress

#### [Configuration name key:][cokey]
<!-- A configuration’s name will be used for grouping and label application. Names will default to file names if no key is provided. In an extended XYZ file, for example, setting the Configuration Name Key to an existing key "config_name" would use the values provided by this key to name configurations -->

### [Configuration Sets][cset]
<!-- Configuration sets are used to organize and group similar Configurations with one another. These could be similar structures, similar methods, etc.

A Configuration Set’s Extended ID is constructed according to {Name}_{Short ID}. "Name" can be used to lend interpretability to an Extended ID.

Configuration Sets are constructed using regular expressions to match and group Configurations based on their name (remember that the names of Configurations are obtained from the specified "Configuration Name Key"). 

You may create as many configuration sets as needed by copying and pasting the below three entries. -->


#### [Name:][cname]
<!-- Name will be used to construct an Extended ID for the Configuration set. -->  
#### [Description:][cdesc]
<!-- Enter human-readable description of the configurations in the set -->  
#### [Regex:][creg]
<!-- Enter a regular expression for matching to configuration names (i.e., to match only the name entered above and no other configuration set names you have entered) -->  


### [Configuration Labels][clabhead]
<!-- (Optional): If necessary, more specific labels can be added to Configurations for querying purposes. Similar to the construction of Configuration Sets, regular expressions are matched against a Configuration’s name. 

You may create as many labels as needed -->

#### [Labels:][clab]
<!-- Labels to attach to the configurations matched by regex below -->  
#### [Regex:][labreg]
<!-- Regular expression for matching to configuration names (as defined in Configuration Set section above)-->


### [Distribution License][lcns]
<!-- Enter the license under which the content will be distributed (e.g. Creative Commons Zero) -->
#### [License:][lcns]

### [Comments][comm]
<!-- Enter any additional comments for the reviewer below -->



<!-- Tooltip text -->
[cont]: ## " "
[name]: ## "Name of person submitting dataset"
[email]: ## "Email of person submitting dataset. This will be used for correspondence about dataset submission"
[ds]: ## " "
[dname]: ## "A short name for your dataset"
[auth]: ## 'A list of dataset author names. Format as "FirstName1 LastName1, FirstName2 LastName2". Do not use initials unless author is normally attributed by initial(s)'
[link]: ## "A list of resources describing dataset (DOI if available). Include DOI/URL for dataset, if aleady hosted online"
[elem]: ## "List elements present in dataset using elemental symbols (e.g., Si, Al, C, etc.)"
[soft]: ## "The software and version used for property calculations (e.g., VASP 5.4.1, ORCA 5.0.3)"
[meth]: ## "The method(s) used for property calculations (e.g., DFT, CCSD, CCSD(T))"
[func]: ## "The functional(s) used for property calculations (e.g., PBE, PBEsol, B3LYP, SCAN)"
[bset]: ## "The basis set used for property calculations (e.g., cc-pVDZ, aug-cc-PVTZ)"
[cokey]: ## 'A configuration’s name will be used for grouping and label application. Names will default to file names if no key is provided. In an extended XYZ file, for example, setting the Configuration Name Key to an existing key "config_name" would use the values provided by this key to name configurations'
[pd]: ## 'Select a predefined property if applicable to your data. If a predefined property definition listed above does not apply to your content, you may submit new property definition files with your dataset files. Examples may be found in the file "example_property_definitions.py.'
[cset]: ## 'Configuration sets are used to organize and group similar Configurations with one another. These could be similar structures, similar methods, etc. A Configuration Set’s Extended ID is constructed according to {Name}_{Short ID}. "Name" can be used to lend interpretability to an Extended ID. Configuration Sets are constructed using regular expressions to match and group Configurations based on their name (remember that the names of Configurations are obtained from the specified "Configuration Name Key"). You may create as many configuration sets as needed by copying and pasting the below three entries. '
[cname]: ## "Name will be used to construct an Extended ID for the Configuration set."
[cdesc]: ## "A human-readable description of the configurations in the set"
[creg]: ## "Enter a regular expression for matching to configuration names (i.e., to match only the name entered above and no other configuration set names you have entered)"

[clabhead]: ## "(Optional): If necessary, more specific labels can be added to Configurations for querying purposes. Similar to the construction of Configuration Sets, regular expressions are matched against a Configuration’s name"
[clab]: ## "Labels to attach to the configurations matched by regex below"
[labreg]: ## "Regular expression for matching to configuration names (as defined in Configuration Set section above)"
[lcns]: ## "The license under which the content will be distributed (e.g. Creative Commons Zero)"
[comm]: ## "Any additional comments for the reviewer"