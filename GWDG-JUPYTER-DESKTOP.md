
Visit [Jupyter HPC of the GWDG](https://jupyter.hpc.gwdg.de/hub/spawn) and sign in with AcademicCloud.

* Choose the correct **HPC Project**: Course Deep Learning for Image Analysis
* CLick on **Profile** (Top right)
* Choose the correct **Profile ID**: `dl-for-ia-2025`
<img width="695" height="428" alt="image" src="https://github.com/user-attachments/assets/9f58dde0-6518-4bfd-9e19-408fbf996a80" />


#### Activate the working environment

Packages and modules were implemented using micromamba environments.
The current implementation requires a change to the user's `~/.bashrc`, which should be manageable for the HSC course because all users were created specifically for it. However, this implementation would need improvement before wider deployment.

Start a terminal (under **Activities** on the top left corner).

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

#### Clone repository of the HSC course
In your home directory, clone the git repository of the HSC 2025 Course.
```
cd ~
git clone https://github.com/computational-cell-analytics/dl-for-micro.git
```

#### Install kernel for Jupyter Lab

You can install a kernel for Jupyter Lab once you have activated an environment with:
```
python -m ipykernel install --user --name hsc_course --display-name "hsc_course"
python -m ipykernel install --user --name cellpose --display-name "cellpose"
python -m ipykernel install --user --name stardist --display-name "stardist"
```

#### Start Jupyter Lab

Navigate to the cloned repository and start an instance of the Jupyter Lab with
```
jupyter lab
```
You should see the folder structure on the left side.

#### Change environments

The `hsc_course` environment features packages for the work with `µsam`. Because the interplay between different software is quite complex, two other environments are used for the work with `Cellpose` and `StarDist`. You can activate them the same way as for `hsc_course`. To deactivate an environment use `micromamba deactivate`.

#### Issues
The connection to the Desktop might be unstable, so that the status **Disconnected** appears in the upper right corner.
To re-establish the connection, just refresh the page, e.g. by clicking on the jupyter logo in the top left corner.
