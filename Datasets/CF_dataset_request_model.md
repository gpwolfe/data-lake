<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <link rel="shortcut icon" href="/static/favicon.ico">

  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">

  <link href="/static/css/site.css" rel="stylesheet">
</head>
<body>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa" crossorigin="anonymous"></script>


<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
  <div class="container-fluid">
    <a class="navbar-brand" href="https://colabfit.org">
      <img style="width: 34px;" src="https://colabfit.org/images/colabfit-logo-transparent.svg" alt="ColabFit logo" />
      <span class="navbar-brand-text">ColabFit</span>
    </a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav ms-auto mb-2 mb-lg-0">
        <li class="nav-item"><a class="nav-link" href="https://colabfit.org">Home</a></li>

        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Browse
          </a>
          <ul class="dropdown-menu">
            <li><a class="dropdown-item" href="https://materials.colabfit.org/">Database</a></li>
            <li><a class="dropdown-item" href="https://colabfit.org/materials-atlas">Materials Atlas</a></li>
          </ul>
        </li>

        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Contribute
          </a>
          <ul class="dropdown-menu">
            <li><a class="dropdown-item" target=_blank href="https://contribute.colabfit.org/">Submit content</a></li>
            <li><a class="dropdown-item" target=_blank href="https://colabfit.org/request">Request content</a></li>
          </ul>
        </li>

        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Tools
          </a>
          <ul class="dropdown-menu">
            <li><a class="dropdown-item" target=_blank href="https://colabfit.github.io/colabfit-tools/html/index.html">ColabFit tools</a></li>
            <li><a class="dropdown-item" href="https://colabfit.org/data-standard">ColabFit Data Standard</a></li>
            <li><a class="dropdown-item" target=_blank href="https://github.com/openkim/kliff">KLIFF</a></li>
            <li><a class="dropdown-item" target=_blank href="https://github.com/ipcamit/kliff">KLIFF-Torch</a></li>
            <li><a class="dropdown-item" target=_blank href="https://github.com/ipcamit/colabfit-descriptor-library">Libdescriptor</a></li>
          </ul>
        </li>

        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            About
          </a>
          <ul class="dropdown-menu">
            <li><a class="dropdown-item" href="https://colabfit.org/about">About ColabFit</a></li>
            <li><a class="dropdown-item" href="https://colabfit.org/leadership">Leadership and<br>Funding</a></li>
            <li><a class="dropdown-item" href="https://colabfit.org/team">ColabFit Team</a></li>
            <li><a class="dropdown-item" href="https://colabfit.org/consortium">Consortium</a></li>
          </ul>
        </li>

        <li class="nav-item"><a class="nav-link" href="https://colabfit.org/contact">Contact</a></li>
      </ul>
    </div>
  </div>
</nav>


  <div class="container">
  <br><br>
  <div class="content">
    

<script src="https://unpkg.com/@yaireo/tagify"></script>
<script src="https://unpkg.com/@yaireo/tagify/dist/tagify.polyfills.min.js"></script>
<link href="https://unpkg.com/@yaireo/tagify/dist/tagify.css" rel="stylesheet" type="text/css" />


<h3>Contribute Content</h3>
<hr>
<br>

<form action="/contribute-upload"
      method="post"
      id="contribute_form"
      enctype="multipart/form-data">

<div class="mb-3">
  <label for="contributor-name" class="form-label">Contributor Name</label>
  <input type="text" class="form-control" id="contributor-name" name="contributor-name">
  <div class="form-text">Your name.</div>
</div>

<div class="mb-3">
  <label for="contributor-email" class="form-label">Contributor Email</label>
  <input type="email" class="form-control" id="contributor-email" name="contributor-email">
  <div class="form-text">Your email address.</div>
</div>

<div class="mb-3">
  <label for="dataset-name" class="form-label">Dataset Name</label>
  <input type="text" class="form-control" id="dataset-name" name="dataset-name">
  <div class="form-text">Name of dataset.</div>
</div>

<div class="mb-3">
  <label for="dataset-authors" class="form-label">Dataset Authors</label>
  <input type="text" class="form-control" id="dataset-authors" name="dataset-authors">
  <div class="form-text">Authors of dataset.</div>
</div>

<div class="mb-3">
  <label for="dataset-links" class="form-label">Dataset External Links</label>
  <textarea class="form-control" id="dataset-links" name="dataset-links"></textarea>
  <div class="form-text">Links to resources describing dataset.</div>
</div>

<div class="mb-3">
  <label for="elements" class="form-label">Elements</label>
  <input type="text" class="form-control" id="elements" name="elements">
  <div class="form-text">Elements present in the dataset. Only element symbols are allowed (e.g., Si, Al, C, etc.).</div>
</div>

<br>
<div class="mb-3">
  <label for="configuration-files" class="form-label">Select Data File(s) to upload</label>
  <br>
  <a href="#" class="font-weight-light" style="font-size: 0.8em" data-bs-toggle="modal" data-bs-target="#help-configuration-files">click for help</a>
<div class="modal modal-xl fade" id="help-configuration-files" tabindex="-1" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-body">
        Files should contain paired configurational-property data. Data are expected to possess a key-value structure, e.g., those found in the header of extended XYZ files, JSON, HDF5 groups, general serialized Python dictionaries, etc. Although ColabFit can accept any of these file formats, there should be a consistent formatting if multiple files are to be uploaded.
       </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
      </div>
    </div>
  </div>
</div>
  <input class="form-control" type="file" id="configuration-files" name="configuration-files" multiple="multiple">
  <div class="form-text">Attach data files here. Multiple files may be selected.</div>
</div>

<div class="mb-3">
  <label for="configuration-name-key" class="form-label">Configuration Name Key</label>
  <br>
  <a href="#" class="font-weight-light" style="font-size: 0.8em" data-bs-toggle="modal" data-bs-target="#help-configuration-name-key">click for help</a>
<div class="modal modal-xl fade" id="help-configuration-name-key" tabindex="-1" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-body">
        A Configuration’s name will be used for grouping and label application. Names will default to file names if no key is provided. In the example (extended XYZ), setting the Configuration Name Key to "config_name" would provide the configurations with names of "example1" and "example2".
        <img style="width: 900px" src="/static/images/contribute-help/help-configuration-name-key.png">
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
      </div>
    </div>
  </div>
</div>
  <input type="text" class="form-control" id="configuration-name-key" name="configuration-name-key">
  <div class="form-text">Key from which a Configuration will obtain its name value.</div>
</div>

<br>
<div class="mb-3">
  <label for="property-definitions" class="form-label">Choose Property Definitions</label>
  <select id="property-definitions"
          name="property-definitions"
          class="form-select" multiple="multiple" style="min-height: 7em">
    <option value="" selected>(none)</option>
    <option>potential-energy</option>
    <option>atomic-forces</option>
    <option>cauchy-stress</option>
  </select>
  <div class="form-text">
    Choose pre-defined Property Definitions that apply to your content. Multiple entries may be selected by Ctrl-Click (Windows) or Cmd-Click (macOS).
    <br>
    Select a predefined property if applicable to your data. See definitions at <a href="https://github.com/colabfit/colabfit-tools/blob/development/colabfit/tools/property_definitions.py" target=_blank>https://github.com/colabfit/colabfit-tools/blob/development/colabfit/tools/property_definitions.py</a>.
  </div>
</div>

<br>
<div class="mb-3">
  <label for="property-definition-files" class="form-label">Select Property Definition Files to upload</label>
  <br>
  <a href="#" class="font-weight-light" style="font-size: 0.8em" data-bs-toggle="modal" data-bs-target="#help-property-definition-files">click for help</a>
<div class="modal modal-xl fade" id="help-property-definition-files" tabindex="-1" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-body">
         If a new property needs to be defined, please upload a file formatted similarly to the example. Red text denotes the standardization that should be present in all definitions, while green text denotes user-entered information. See predefined properties for further examples: <a href="https://github.com/colabfit/colabfit-tools/blob/development/colabfit/tools/property_definitions.py" target=_blank>https://github.com/colabfit/colabfit-tools/blob/development/colabfit/tools/property_definitions.py</a>.
        <img style="width: 700px" src="/static/images/contribute-help/help-property-definition-files.png">
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
      </div>
    </div>
  </div>
</div>
  <input class="form-control" type="file" id="property-definition-files" name="property-definition-files" multiple="multiple">
  <div class="form-text">If a predefined Property Definition listed above does not apply to your content, you may submit new Property Definition Files here. Multiple files may be selected.</div>
</div>

<br>
<hr>
<h5>Property mappings</h5>
<a href="#" class="font-weight-light" style="font-size: 0.8em" data-bs-toggle="modal" data-bs-target="#help-modal-property-mappings">click for help</a>
<div class="modal modal-xl fade" id="help-modal-property-mappings" tabindex="-1" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-body">
        For reference, a piece of the "potential-energy" property definition and an example XYZ file are shown below.
        <img style="width: 900px" src="/static/images/contribute-help/help-modal-property-mappings.png">
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
      </div>
    </div>
  </div>
</div>
<div id="form-container-property-mappings"></div>
<button type="button" class="btn btn-sm btn-info text-light float-end" onclick="add_to_form_container_property_mappings();">Add Another Map</button>


<br><br><br><hr>
<h5>Property settings</h5>
<a href="#" class="font-weight-light" style="font-size: 0.8em" data-bs-toggle="modal" data-bs-target="#help-property-setting">click for help</a>
<div class="modal modal-xl fade" id="help-property-setting" tabindex="-1" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-body">
        <h4>Property Setting Subkeys</h4>
        If settings are stored within the data file(s) using key-value pairs, e.g., within an XYZ header, one can add a "Setting Subkey" to allow for automatic extraction of these settings. In the below example, "some_prop_setting" should be entered as the "Property setting key". If one would like the setting to be entered into the database using a more descriptive name, a user-specified "Property setting name" can be specified, otherwise it will default to the value entered in "Property setting key".
        <img style="width: 900px" src="/static/images/contribute-help/help-property-setting.png">
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
      </div>
    </div>
  </div>
</div>
<div id="form-container-property-settings"></div>
<button type="button" class="btn btn-sm btn-info text-light float-end" onclick="add_to_form_container_property_settings();">Add Another Settings</button>

<br><br><br><hr>
<h5>Configuration sets</h5>
<a href="#" class="font-weight-light" style="font-size: 0.8em" data-bs-toggle="modal" data-bs-target="#help-configuration-sets">click for help</a>
<div class="modal modal-xl fade" id="help-configuration-sets" tabindex="-1" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-body">
        Configuration sets are used to organize and group similar Configurations with one another. These could be similar structures, data splits for ML applications, etc.
        <br><br>
        A Configuration Set’s Extended ID is constructed according to {Name}_{Short ID}. "Name" can be used to lend interpretability to an Extended ID.
        <br><br>
        Configuration Sets are constructed using regular expressions to match and group Configurations based on their name (remember that the names of Configurations are obtained from the specified "Configuration Name Key").
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
      </div>
    </div>
  </div>
</div>
<div id="form-container-configuration-sets"></div>
<button type="button" class="btn btn-sm btn-info text-light float-end" onclick="add_to_form_container_configuration_sets();">Add Another Set</button>

<br><br><br><hr>
<h5>Configuration labels</h5>
<a href="#" class="font-weight-light" style="font-size: 0.8em" data-bs-toggle="modal" data-bs-target="#help-configuration-labels">click for help</a>
<div class="modal modal-xl fade" id="help-configuration-labels" tabindex="-1" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-body">
        If necessary, more specific labels can be added to Configurations for querying purposes. Similar to the construction of Configuration Sets, regular expressions are matched against a Configuration’s name.
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
      </div>
    </div>
  </div>
</div>
<div id="form-container-configuration-labels"></div>
<button type="button" class="btn btn-sm btn-info text-light float-end" onclick="add_to_form_container_configuration_labels();">Add Another Regex</button>


<br><br><br><hr>
<script>
  function toggle_license_custom_choice_area() {
    e_select = document.getElementById('license');
    e_help = document.getElementById('license-custom-choice-area');
    if( e_select.value == "custom" ) {
      e_help.style.removeProperty('display'); // display with default value
    } else {
      e_help.style.display = "none";
    }
  }
</script>
<div class="form-group">
  <label for="license"><h5>Distribution License</h5></label>
  <select class="form-control" id="license" name="license" onchange="toggle_license_custom_choice_area();" required>
    <option selected disabled value="">Click here to choose a license</option>
    <option value="cc0">Creative Commons Zero</option>
    <option value="custom">Other</option>
  </select>
  <p class="form-text text-muted">The license under which the content will be distributed.</p>

  <div id="license-custom-choice-area" style="display:none">

    <div class="mb-3">
      <label for="license-notes" class="form-label">License Explanatory Details</label>
      <textarea rows=5 class="form-control" id="dataset-links" name="license-notes"></textarea>
      <div class="form-text">Please state your license terms as a valid <a target=_blank href="https://spdx.org/licenses/">SPDX License Expression</a> and the rationale for the license selection.</div>
    </div>

    <div id="license-custom-choice-help" class="card border-danger mt-3 mb-3">
      <div class="card-body">
        <p class="card-text">
          The preferred license for uploading content to ColabFit is the <i><a target=_blank href="https://spdx.org/licenses/CC0-1.0.html">Creative Commons Zero v1.0 Universal</a></i> (CC0-1.0). Alternatively, select "Other" and provide an explanation with a valid SPDX License Expression (see the <a target=_blank href="https://spdx.org/licenses/">SPDX License List</a>) for more information, or <a href="mailto:support@colabfit.org">contact support@colabfit.org</a>.
        </p>
      </div>
    </div>

  </div> <!-- license-custom-choice-area -->

</div>

<script>
  toggle_license_custom_choice_area();
</script>

<div class="form-check">
  <input class="form-check-input" type="checkbox" id="license-attestation" name="license-attestation" value="yes" required>
  <label class="form-check-label" for="license-attestation">
    By checking this box, I attest that I own or am acting within the bounds of the license under which I acquired this data and possess the right to upload this data under the license specified above.
  </label>
</div>


<br><hr>
<div class="mb-3">
  <label for="comments" class="form-label"><h5>Comments</h5></label>
  <textarea class="form-control" id="comments" name="comments" rows=6></textarea>
  <div class="form-text">You may include any comments for the reviewer.</div>
</div>


<script>
const periodic_table_elements = [
"H",
"He",
"Li",
"Be",
"B",
"C",
"N",
"O",
"F",
"Ne",
"Na",
"Mg",
"Al",
"Si",
"P",
"S",
"Cl",
"Ar",
"K",
"Ca",
"Sc",
"Ti",
"V",
"Cr",
"Mn",
"Fe",
"Co",
"Ni",
"Cu",
"Zn",
"Ga",
"Ge",
"As",
"Se",
"Br",
"Kr",
"Rb",
"Sr",
"Y",
"Zr",
"Nb",
"Mo",
"Tc",
"Ru",
"Rh",
"Pd",
"Ag",
"Cd",
"In",
"Sn",
"Sb",
"Te",
"I",
"Xe",
"Cs",
"Ba",
"La",
"Ce",
"Pr",
"Nd",
"Pm",
"Sm",
"Eu",
"Gd",
"Tb",
"Dy",
"Ho",
"Er",
"Tm",
"Yb",
"Lu",
"Hf",
"Ta",
"W",
"Re",
"Os",
"Ir",
"Pt",
"Au",
"Hg",
"Tl",
"Pb",
"Bi",
"Po",
"At",
"Rn",
"Fr",
"Ra",
"Ac",
"Th",
"Pa",
"U",
"Np",
"Pu",
"Am",
"Cm",
"Bk",
"Cf",
"Es",
"Fm",
"Md",
"No",
"Lr",
"Rf",
"Db",
"Sg",
"Bh",
"Hs",
"Mt",
"Ds",
"Rg",
"Cn",
"Nh",
"Fl",
"Mc",
"Lv",
"Ts",
"Og"
]
</script>

<script>
function tagify_element( id ) {
  let e = document.getElementById(id);
  new Tagify(e, {
    delimiters: '\\|',
    originalInputValueFormat: valuesArr => valuesArr.map(item => item.value).join('|')
  });
}

function tagify_element_restricted_to_periodic_table( id ) {
  let e = document.getElementById(id);
  new Tagify(e, {
    delimiters: '\\|',
    originalInputValueFormat: valuesArr => valuesArr.map(item => item.value).join('|'),
    enforceWhitelist: true,
    whitelist : periodic_table_elements,
    dropdown: {
      caseSensitive: true,
    },
  });
}

let form_container_property_mappings_count = 0;
let form_container_property_settings_count = 0;
let form_container_configuration_sets_count = 0;
let form_container_configuration_labels_count = 0;

let form_container_property_mappings_subkey_count = {};
let form_container_property_settings_subkey_count = {};

function add_to_form_container_property_mappings_subkey(form_container_property_mappings_count,
                                                        form_container_property_mappings_subkey_count) {

  form_container_property_mappings_subkey_count[form_container_property_mappings_count] ??= 0;
  form_container_property_mappings_subkey_count[form_container_property_mappings_count] += 1;
  let subkey_count = form_container_property_mappings_subkey_count[form_container_property_mappings_count];

  tmpl = `
<div class="card bg-light" style="margin-bottom: 1em">
  <div class="card-body">

    <div class="mb-3 row">
      <label for="property-map-${form_container_property_mappings_count}-${subkey_count}-property-definition-key" class="col-sm-2 col-form-label">Property Definition key</label>
      <div class="col-sm-10">
        <input type="text" class="form-control" id="property-map-${form_container_property_mappings_count}-${subkey_count}-property-definition-key" name="property-map[${form_container_property_mappings_count}][${subkey_count}][property-definition-key]">
      </div>
      <div class="form-text">Field name from the property definition</div>
    </div>

    <div class="mb-3 row">
      <label for="property-map-${form_container_property_mappings_count}-${subkey_count}-ase-field" class="col-sm-2 col-form-label">Configuration key</label>
      <div class="col-sm-10">
        <input type="text" class="form-control" id="property-map-${form_container_property_mappings_count}-${subkey_count}-ase-field" name="property-map[${form_container_property_mappings_count}][${subkey_count}][ase-field]">
      </div>
      <div class="form-text">Key where property field data is stored on Configuration</div>
    </div>

    <div class="mb-3 row">
      <label for="property-map-${form_container_property_mappings_count}-${subkey_count}-units" class="col-sm-2 col-form-label">Units</label>
      <div class="col-sm-10">
        <input type="text" class="form-control" id="property-map-${form_container_property_mappings_count}-${subkey_count}-units" name="property-map[${form_container_property_mappings_count}][${subkey_count}][units]">
      </div>
      <div class="form-text">Units for property data (e.g., eV, eV/Ang, GPa, etc.)</div>
    </div>

  </div>
</div>
  `;

  e = document.getElementById(`form-container-property-mappings-${form_container_property_mappings_count}-subkeys`);
  e.insertAdjacentHTML('beforeend', tmpl);

  update_options_for_all_property_setting_property_max_index_select();
}


function add_to_form_container_property_settings_subkey(form_container_property_settings_count,
                                                        form_container_property_settings_subkey_count) {

  form_container_property_settings_subkey_count[form_container_property_settings_count] ??= 0;
  form_container_property_settings_subkey_count[form_container_property_settings_count] += 1;
  var subkey_count = form_container_property_settings_subkey_count[form_container_property_settings_count];

  tmpl = `
<div class="card bg-light" style="margin-bottom: 1em">
  <div class="card-body">

    <div class="mb-3 row">
      <label for="property-setting-${form_container_property_settings_count}-${subkey_count}-property-setting-name" class="col-sm-2 col-form-label">Property setting name</label>
      <div class="col-sm-10">
        <input type="text" class="form-control" id="property-setting-${form_container_property_settings_count}-${subkey_count}-property-setting-name" name="property-setting[${form_container_property_settings_count}][${subkey_count}][property-setting-name]">
      </div>
      <div class="form-text">Name for the property setting</div>
    </div>

    <div class="mb-3 row">
      <label for="property-setting-${form_container_property_settings_count}-${subkey_count}-property-setting-key" class="col-sm-2 col-form-label">Property setting key</label>
      <div class="col-sm-10">
        <input type="text" class="form-control" id="property-setting-${form_container_property_settings_count}-${subkey_count}-property-setting-key" name="property-setting[${form_container_property_settings_count}][${subkey_count}][property-setting-key]">
      </div>
      <div class="form-text">Key where property setting data is stored on Configuration</div>
    </div>

    <div class="mb-3 row">
      <label for="property-setting-${form_container_property_settings_count}-${subkey_count}-units" class="col-sm-2 col-form-label">Units</label>
      <div class="col-sm-10">
        <input type="text" class="form-control" id="property-setting-${form_container_property_settings_count}-${subkey_count}-units" name="property-setting[${form_container_property_settings_count}][${subkey_count}][units]">
      </div>
      <div class="form-text">Units for property setting data (e.g., eV, eV/Ang, GPa, etc.)</div>
    </div>

  </div>
</div>
  `;

  e = document.getElementById(`form-container-property-settings-${form_container_property_settings_count}-subkeys`);
  e.insertAdjacentHTML('beforeend', tmpl);
}


function add_to_form_container_property_mappings() {
  form_container_property_mappings_count += 1;
  tmpl = `
<div class="card" style="margin-bottom: 1em">
  <div class="card-body">
  <div style="font-size: 130%; font-weight: bold;">Map ${form_container_property_mappings_count}</div>

  <div class="mb-3 row">
    <label for="property-map-${form_container_property_mappings_count}-property-definition-short-name" class="col-sm-2 col-form-label">Property Definition Short Name</label>
    <div class="col-sm-10">
      <input type="text" class="form-control" id="property-map-${form_container_property_mappings_count}-property-definition-short-name" name="property-map[${form_container_property_mappings_count}][property-definition-short-name]">
    </div>
  </div>

<div id="form-container-property-mappings-${form_container_property_mappings_count}-subkeys"></div>
<button type="button" class="btn btn-sm btn-success float-end"
        onclick="add_to_form_container_property_mappings_subkey(${form_container_property_mappings_count},form_container_property_mappings_subkey_count);">Add Another Map Subkey</button>

  </div>
</div>
  `;
  e = document.getElementById('form-container-property-mappings');
  e.insertAdjacentHTML('beforeend', tmpl);

  add_to_form_container_property_mappings_subkey( form_container_property_mappings_count, form_container_property_mappings_subkey_count );
}


function update_options_for_all_property_setting_property_max_index_select() {
  for (const c_property_settings_count_n of Array(form_container_property_settings_count).keys()) {
    let property_settings_count_n = c_property_settings_count_n + 1;
    let e_select = document.getElementById(`property-setting-${property_settings_count_n}-property-map-index`);

    if( !e_select ) {
      return;
    }

    let e_selected_options = e_select.selectedOptions;
    let e_selected_options_values = [];
    for (const o of e_selected_options) {
      e_selected_options_values.push( Number(o.value) );
    }
    let tmpl = "";

    for (const ci of Array(form_container_property_mappings_count).keys()) {
      let i = ci + 1;

      let selected_str = "";
      if( e_selected_options_values.includes( i ) ) {
        selected_str = 'selected="selected"';
      }
      tmpl += `<option value="${i}" ${selected_str}>Map ${i}</option>`;
    }

    e_select.innerHTML = tmpl;
  }
}


function add_to_form_container_property_settings() {
  form_container_property_settings_count += 1;
  tmpl = `
<div class="card" style="margin-bottom: 1em">
  <div class="card-body">
  <div style="font-size: 130%; font-weight: bold;">Setting ${form_container_property_settings_count}</div>

    <div class="mb-3 row">
      <label for="property-setting-${form_container_property_settings_count}-property-map-index" class="col-sm-2 col-form-label">Property Map(s)</label>
      <div class="col-sm-10">
        <select id="property-setting-${form_container_property_settings_count}-property-map-index"
                name="property-setting[${form_container_property_settings_count}][property-map-index]"
                class="form-select" multiple="multiple">
        </select>
        <div class="form-text">Multiple entries may be selected by Ctrl-Click (Windows) or Cmd-Click (macOS).</div>
      </div>
    </div>

    <div class="mb-3 row">
      <label for="property-setting-${form_container_property_settings_count}-method" class="col-sm-2 col-form-label">Method</label>
      <div class="col-sm-10">
        <input type="text" class="form-control" id="property-setting-${form_container_property_settings_count}-method" name="property-setting[${form_container_property_settings_count}][method]">
      </div>
      <div class="form-text">Method used for calculation (e.g., VASP, CASTEP, experiment, etc.)</div>
    </div>

    <div class="mb-3 row">
      <label for="property-setting-${form_container_property_settings_count}-description" class="col-sm-2 col-form-label">Description</label>
      <div class="col-sm-10">
        <input type="text" class="form-control" id="property-setting-${form_container_property_settings_count}-description" name="property-setting[${form_container_property_settings_count}][description]">
      </div>
      <div class="form-text">Human-readable description of the calculation</div>
    </div>

    <div class="mb-3 row">
      <label for="property-setting-${form_container_property_settings_count}-labels" class="col-sm-2 col-form-label">Labels</label>
      <div class="col-sm-10">
        <input type="text" class="form-control" id="property-setting-${form_container_property_settings_count}-labels" name="property-setting[${form_container_property_settings_count}][labels]">
      </div>
      <div class="form-text">Labels to apply to property settings to improve future queries</div>
    </div>

    <div class="mb-3">
      <label for="property-setting-${form_container_property_settings_count}-files" class="form-label">Additional files</label>
      <input class="form-control" type="file" id="property-setting-${form_container_property_settings_count}-files" name="property-setting-${form_container_property_settings_count}-files" multiple="multiple">
      <div class="form-text">Attach files (e.g., program input, scripts, etc.) here. Multiple files may be selected.</div>
    </div>

    <div id="form-container-property-settings-${form_container_property_settings_count}-subkeys"></div>
    <button type="button" class="btn btn-sm btn-success float-end"
            onclick="add_to_form_container_property_settings_subkey(${form_container_property_settings_count},form_container_property_settings_subkey_count);">Add Setting Subkey</button>
  </div>
</div>
  `;
  e = document.getElementById('form-container-property-settings');
  e.insertAdjacentHTML('beforeend', tmpl);
  tagify_element(`property-setting-${form_container_property_settings_count}-labels`);

  // add_to_form_container_property_settings_subkey( form_container_property_settings_count, form_container_property_settings_subkey_count );

  update_options_for_all_property_setting_property_max_index_select();
}


function add_to_form_container_configuration_sets() {
  form_container_configuration_sets_count += 1;
  tmpl = `
<div class="card" style="margin-bottom: 1em">
  <div class="card-body">

    <div class="mb-3 row">
      <label for="configuration-set-${form_container_configuration_sets_count}-name" class="col-sm-2 col-form-label">Name</label>
      <div class="col-sm-10">
        <input type="text" class="form-control" id="configuration-set-${form_container_configuration_sets_count}-name" name="configuration-set[${form_container_configuration_sets_count}][name]">
      </div>
      <div class="form-text">Name used to construct an Extended ID for the Configuration set.</div>
    </div>

    <div class="mb-3 row">
      <label for="configuration-set-${form_container_configuration_sets_count}-description" class="col-sm-2 col-form-label">Description</label>
      <div class="col-sm-10">
        <input type="text" class="form-control" id="configuration-set-${form_container_configuration_sets_count}-description" name="configuration-set[${form_container_configuration_sets_count}][description]">
      </div>
      <div class="form-text">Human-readable description of the configurations in the set</div>
    </div>

    <div class="mb-3 row">
      <label for="configuration-set-${form_container_configuration_sets_count}-regex" class="col-sm-2 col-form-label">Regex</label>
      <div class="col-sm-10">
        <input type="text" class="form-control" id="configuration-set-${form_container_configuration_sets_count}-regex" name="configuration-set[${form_container_configuration_sets_count}][regex]">
      </div>
      <div class="form-text">Regular expression for matching to configuration names</div>
    </div>

  </div>
</div>
  `;
  e = document.getElementById('form-container-configuration-sets');
  e.insertAdjacentHTML('beforeend', tmpl);
}


function add_to_form_container_configuration_labels() {
  form_container_configuration_labels_count += 1;
  tmpl = `
<div class="card" style="margin-bottom: 1em">
  <div class="card-body">

    <div class="mb-3 row">
      <label for="configuration-label-${form_container_configuration_labels_count}-description" class="col-sm-2 col-form-label">Labels</label>
      <div class="col-sm-10">
        <input type="text" class="form-control" id="configuration-label-${form_container_configuration_labels_count}-labels" name="configuration-label[${form_container_configuration_labels_count}][labels]">
      </div>
      <div class="form-text">Labels to attach to the matching configurations</div>
    </div>

    <div class="mb-3 row">
      <label for="configuration-label-${form_container_configuration_labels_count}-regex" class="col-sm-2 col-form-label">Regex</label>
      <div class="col-sm-10">
        <input type="text" class="form-control" id="configuration-label-${form_container_configuration_labels_count}-regex" name="configuration-label[${form_container_configuration_labels_count}][regex]">
      </div>
      <div class="form-text">Regular expression for matching to configuration names</div>
    </div>

  </div>
</div>
  `;
  e = document.getElementById('form-container-configuration-labels');
  e.insertAdjacentHTML('beforeend', tmpl);
  tagify_element(`configuration-label-${form_container_configuration_labels_count}-labels`);
}
</script>

<br><br><br><hr>
<button type="button"
        id="contribute_form_submit_button"
        class="btn btn-primary">Submit</button>
</form>


<script>
window.addEventListener("DOMContentLoaded", function () {
  document.getElementById("contribute_form_submit_button").addEventListener("click", function () {
    let form = document.getElementById("contribute_form");
    if( form.checkValidity() ) {
      form.submit();
    } else {
      form.reportValidity();
    }
  });

  add_to_form_container_property_mappings();
  add_to_form_container_property_settings();
  add_to_form_container_configuration_sets();
  add_to_form_container_configuration_labels();

  tagify_element('dataset-authors');
  tagify_element('dataset-links');
  tagify_element_restricted_to_periodic_table('elements');
});
</script>


<br><br><br><br><br>

  </div>

  </div>

</body>
</html>