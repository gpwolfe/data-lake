# Contribute content

## Contributor
> Contact information about the person requesting/submitting the data. Used for communication purposes.
​

**Name**:  
**Email**:  

## Dataset
> Any information necessary to help the ColabFit find and access the data, and to correctly cite relevant material. The "name" and "description" will be used when publishing to the ColabFit exchange, and should be human-readable. Author list should include full first names, unless the author is normally attributed by initials. Links should include relevant publications and online location of dataset, if available.

**Name**:  
  
​
**Authors**:  


**Links**:  
*  Publication link
*  Dataset link

**Description**:  


## Calculations  
> Details regarding how the data was computed in order to improve reproducibility. Provide as much information as possible. Input files are highly encouraged.
> Additional details might include functional, basis set, energy cutoff, k-point grid, reference energy, etc.
​

**Method**:    
**Software**:    
**Additional details**:   
**Files**:  

### Included properties
> See [the current list of ColabFit property definitions](https://materials.colabfit.org/browse/property-definitions). If you believe your data does not match one of the existing definitions, then you must submit a new property definition following [the template provided in the examples folder](https://github.com/gpwolfe/colabfit-data/blob/main/examples/example_property_definitions.py).  

|   Name            |   Units   |   Notes   |
|   ---             |   ---     |   ---     |
|   potential energy |          |           |
|   atomic forces   |           |           |
|   cauchy stress   |           |           |
  
## Configurations
> Basic information explaining the types of configurations in the dataset, and how they are organized.  
> Elements should be listed by chemical symbol


**Elements**:  
**Number of configurations**:    

### Naming convention
> If your configurations have names, please describe where their names can be found (e.g., as a field in an `ASE.Atoms.info` dictionary).
​
​
### Configuration sets
> Configuration sets are used to define a conceptual grouping over a collection of atomic configurations. Configuration sets are constructed via regex filtering on configuration names.
​

|Regex|Description|
|---|---|
|   |   |

  
### Configuration labels
> Configuration labels can be attached to your data to improve interpretability. This is done via regex matching on the configuration name.
​

| Regex | Label |
| --- | --- |
|     |     |

  
### Distribution License
>The license under which the content will be distributed (e.g. Creative Commons Zero)
