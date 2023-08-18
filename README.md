# ColabFit-Data
A repository to request ingestion of datasets to ColabFit
  
# Instructions  
  
## For datasets stored on local machine(s)

**Prepare your dataset**
  
* Create a folder to contain all your dataset files and ONLY your dataset files
* Give this folder the name of your dataset, replacing spaces with underscores &rarr; `_`
* Move your dataset files (and ONLY your dataset files) into this folder

**Fill out the dataset information spreadsheet**
  
* [Follow this link](https://github.com/gpwolfe/colabfit-data/blob/main/CF_dataset_request_template.xltx) and choose "Download raw file" (on far right of activity bar) to get the Excel template for dataset information
* Save the template as a new spreadsheet
  * Open template file with Excel
  * Go to `Save as` and choose `File Format: Excel Workbook (.xlsx)`
  * Choose your dataset folder as the save location
  * Rename the Excel file. Include the short name for your dataset and your last name in the file name  
    * Example: `Dataset_name_Your-name.xlsx` &rarr; `C_allotrope_bixby_2022_Bixby.xlsx`
* Fill out the Excel template and save your file

**Fork the colabfit-data repository**
  
* Click on the `Fork` dropdown menu near the upper right-hand side of the page
* Select `Create new fork`
* Leave `Copy the main branch only` selected
* Click on `Create fork`
  
**Create a new branch**
* Select the [Branches page](https://github.com/gpwolfe/colabfit/branches)
* Click the `New branch` button
* Enter a meaningful name for your new branch (i.e., the name of your dataset)
* Leave `main` as the source branch
* Click `Create new branch`
* Select your new branch from the branch list (you may need to refresh the page to see your branch)
  
**Upload your dataset**
* Navigate to the [Datasets](https://github.com/gpwolfe/colabfit-data/tree/main/Datasets) folder
* Select `Add file` &rarr; `Upload files` from the right side of the activity bar
* Using your mouse, drag your **entire dataset folder** (containing all dataset files and your Excel file) onto the GitHub pane
  * Note: You must drag your files from your file explorer application onto the GitHub pane. The `choose your files` button will not allow you to upload a folder.
* Add a commit message to the field containing `Add files via upload`
* Click on `Commit changes`. Leave `Commit directly to the your_branch branch` selected.

**Submit a pull request**
* Click on `Compare & pull request`
* Read through the Pull Request checklist and ensure you are prepared to submit
* Click `Create pull request`
  
## For datasets hosted online
  
#### Preferred: Submit an Issue using Excel template
  
**Fill out the dataset information spreadsheet**
  
* [Follow this link](https://github.com/gpwolfe/colabfit-data/blob/main/CF_dataset_request_template.xltx) and choose "Download raw file" (on far right of activity bar) to get the Excel template for dataset information
* Save the template as a new spreadsheet
  * Open template file with Excel
  * Go to `Save as` and choose `File Format: Excel Workbook (.xlsx)`
  * Choose your dataset folder as the save location
  * Rename the Excel file. Include the short name for your dataset and your last name in the file name  
    * Example: `Dataset_name_Your-name.xlsx` &rarr; `C_allotrope_bixby_2022_Bixby.xlsx`
* Fill out the Excel template and save your file
  
*Submit a GutHub Issue* 
* Click on `Issues`, above
* Click on `New Issue`
* Select `Submit Dataset Excel` &rarr; `Get Started`
* Add a title with your name and your dataset name
* Attach your Excel file by dragging and dropping or selecting from your computer
* Click `Submit new issue`
  
### Alternatively: Fill out and submit non-Excel Issue template
  
* Open new issue, selecting `Submit Dataset Without Excel`
* Fill out Issue template
* Click `Submit new issue`
    
