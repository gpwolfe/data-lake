# ColabFit-Data
A repository to request ingestion of datasets to ColabFit
  
## Instructions  
  
### For datasets stored on local machine(s)

**Prepare your dataset**
  
* Create a folder to contain all your dataset files and ONLY your dataset files
* Give this folder the name of your dataset, replacing spaces with underscores `_`
* Move your dataset files (and ONLY your dataset files) into this folder

**Fill out the dataset information spreadsheet**
  
* Download the [informational Excel spreadsheet template by following this link](https://github.com/gpwolfe/colabfit-data/blob/main/CF_dataset_request_template.xltx) and choosing "Download raw file" (on far right of activity bar)
* Open template file with Excel
* `Save as` &rarr; choose `File Format: Excel Workbook (.xlsx)`
    * Choose your dataset folder as the save location
* Rename the Excel file. Include the short name for your dataset and your last name in the file name  
  * Example: `Dataset_name_Your-name.xlsx` &rarr; `C_allotrope_bixby_2022_Bixby.xlsx`
* Fill out the Excel template


**Submit a Pull Request**
  
*Create a new branch*
* Select the [Branches page](https://github.com/gpwolfe/colabfit/branches)
* Click the `New branch` button
* Enter a meaningful name for your new branch (i.e., the name of your dataset)
* Leave `main` as the Source branch
* Click `Create new branch`
* Select your new branch from branch list (you may need to refresh the page)
* Navigate to the [Datasets](https://github.com/gpwolfe/colabfit-data/tree/main/Datasets)
* Select `Add file` &rarr; `Upload files` from the right side of the activity bar
* Using your mouse, drag your entire dataset folder (containing all dataset files and your Excel file) 
  * Note: You must drag your files from your file explorer application onto the GitHub pane. The `choose your files` button will not allow you to upload a folder.
* Add a commit message to the field containing `Add files via upload`
* Click on `Commit changes`. Leave `Commit directly to the your_branch branch` selected.
* Click on `Compare & pull request`
* Read through the Pull Request checklist and ensure you are prepared to submit
* Click `Create pull request`
  
### For datasets hosted online
  
#### Preferred: Submit an Issue using Excel template
*Download Excel template file:*
* Select [CF_excel_dataset_template.xlsx](https://github.com/gpwolfe/colabfit-data/blob/main/CF_dataset_request_template.xltx)
* Choose "Download raw file" (on far right of activity bar)

*Edit template and save as a new xlsx file:* 
* Open template file
* `Save as` &rarr; choose `File Format: Excel Workbook (.xlsx)`
* Rename the Excel file. Include the short name for your dataset and your last name in the file name  
  * Example: `Dataset_name_Your-name.xlsx` &rarr; `C_allotrope_bixby_2022_Bixby.xlsx`
* Fill out the Excel template

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
    
