
Visit [Jupyter HPC of the GWDG](https://jupyter.hpc.gwdg.de/hub/spawn) and sign in with AcademicCloud.

* Choose the correct **HPC Project**
* **HPC Type**: Desktop
* **Desktop Environment**: Gnome
* **HPC Device**: GPU
* Open the **Advanced** Tab and select your computing resources
* Provide a **Custom Container location** to your downloaded singularity file (.sif)

#### Activate the working environment

Packages and modules were implemented using micromamba environments.
The current implementation requires a change to the user's `~/.bashrc`, which should be manageable for the HSC course because all users were created specifically for it. However, this implementation would need improvement before wider deployment.

Start a terminal (under **Activities**).
To source the environment, you can execute the bash script `/root/activate_micromamba.sh`.
You may have to source your `~/.bashrc` so that the changes take effect.
You can then get an overview about the installed environments with `micromamba env list` and activate one of the environments with `micromamba activate hsc_course`.
Once within the environment, you can work with the installed packages.

Summary:
```
bash /root/activate_micromamba.sh
source ~/.bashrc
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
python -m ipykernel install --user --name <micromamba_env> --display-name "display_name"
```
e.g. for the `hsc_course` environment:
```
python -m ipykernel install --user --name hsc_course --display-name "Python hsc_course2025"
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
