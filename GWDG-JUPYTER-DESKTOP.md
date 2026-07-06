# Starting the GWDG Jupyter Desktop for the Course

Go to https://jupyter.hpc.gwdg.de/?profile=dl-for-ia-2026 and sign in with Single Sign On (SSO).

For more details check out https://docs.google.com/document/d/1PJAcQyaiizerRujCnRsDOKV_ZFOAYT78nDWWX5B9t18/edit?tab=t.0.

## Starting the GWDG Jupyter Desktop with your Own Account

**This section is only relevant after the course, if you want to use the GWDG resources.**

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

### Pre-staged bioimage.io model (nucleus segmentation)

The compute nodes have restricted internet, so the online download of the bioimage.io model
in `nucleus_segmentation/bioimageio/pretrained_segmentation.ipynb`
(`bioimageio.load_model_description("affable-shark")`) can fail.

As a failsafe, the model is pre-staged as a self-contained zip in the shared project space:
```
/mnt/vast-standard/projects/scc_umin_pape_course_dlforia26/models/affable-shark.zip
```
The notebook loads this copy automatically when it exists (falling back to the online download
otherwise). To point it at a different location without editing the notebook, set the env var
`BIOIMAGEIO_MODEL_ZIP=/path/to/affable-shark.zip`.

To refresh the model, re-create the zip on a machine with internet
(`bioimageio package affable-shark ./affable-shark.zip`) and copy it back to the path above.

### Issues
The connection to the Desktop might be unstable, so that the status **Disconnected** appears in the upper right corner.
To re-establish the connection, just refresh the page, e.g. by clicking on the jupyter logo in the top left corner.
