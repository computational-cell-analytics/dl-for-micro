
Visit [Jupyter HPC of the GWDG](https://jupyter.hpc.gwdg.de/hub/spawn) and sign in with AcademicCloud.
### Launch Jupyter Desktop 
#### Option 1. For usage during HSC course
* Choose the correct **HPC Project**: Course Deep Learning for Image Analysis
* CLick on **Profile** (Top right)
* Choose the correct **Profile ID**: `dl-for-ia-2025`
<img width="695" height="428" alt="image" src="https://github.com/user-attachments/assets/9f58dde0-6518-4bfd-9e19-408fbf996a80" />

#### Option 2. For general usage 
Start a Jupyter Desktop session on HPC.  
**IMPORTANT:** In the “Advanced” section you find “Custom Container Location”. Make sure the box is ticked and enter following path:
`/mnt/vast-standard/projects/scc_umin_pape_course_dlforia25/dl-for-image-analysis.sif`  

<img width="880" height="1069" alt="Screenshot from 2025-11-05 08-11-31" src="https://github.com/user-attachments/assets/932dc72b-9ccd-4e59-8a75-5c3ec6a6c1e4" />
<img width="880" height="444" alt="Screenshot from 2025-11-05 08-12-03" src="https://github.com/user-attachments/assets/5d8c502c-2b45-4ec2-be19-631d0d903ff8" />


### Activate the working environment

Packages and modules were implemented using micromamba environments.
The current implementation requires a change to the user's `~/.bashrc`, which should be manageable for the HSC course because all users were created specifically for it. However, this implementation would need improvement before wider deployment.
The first time the server is spawned and available, we first need to invoke the bashrc once to use the Python environments:
Type following command in the terminal.
`source /root/activate_micromamba.sh`

Start a terminal (under **Activities** on the top left corner).

<img width="512" height="277" alt="image" src="https://github.com/user-attachments/assets/dc09a57f-e10a-4dde-a066-24ceb6c657d1" />

You can then get an overview about the installed environments with `micromamba env list` and activate one of the environments with `micromamba activate hsc_course`.
Once within the environment, you can work with the installed packages.

**Note: To use copy & paste from or into the Jupyter Desktop, the clipboard on the top right has to be used.**

Summary:
First time usage (only necessary once):
```
bash /root/activate_micromamba.sh
source ~/.bashrc
```
Do this to activate the python environemnt:
```
micromamba activate hsc_course
```

### Clone repository of the HSC course
In your home directory, clone the git repository of the HSC 2025 Course.
```
cd ~
git clone https://github.com/computational-cell-analytics/dl-for-micro.git
```

### Install kernel for Jupyter Lab

You can install a kernel for Jupyter Lab once you have activated an environment with:
```
python -m ipykernel install --user --name hsc_course --display-name "hsc_course"
python -m ipykernel install --user --name cellpose --display-name "cellpose"
python -m ipykernel install --user --name stardist --display-name "stardist"
```

### Start Jupyter Lab

Navigate to the cloned repository and start an instance of the Jupyter Lab with
```
jupyter lab
```
You should see the folder structure on the left side.

### Change environments

The `hsc_course` environment features packages for the work with `µsam`. Because the interplay between different software is quite complex, two other environments are used for the work with `Cellpose` and `StarDist`. You can activate them the same way as for `hsc_course`. To deactivate an environment use `micromamba deactivate`.

### Issues
The connection to the Desktop might be unstable, so that the status **Disconnected** appears in the upper right corner.
To re-establish the connection, just refresh the page, e.g. by clicking on the jupyter logo in the top left corner.
