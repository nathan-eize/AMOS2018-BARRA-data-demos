# AMOS2018-BARRA-data-demos
Notebooks and code for exploring and demonstrating the BARRA reanalysis dataset for the BOM Data Workshop session at AMOS-ISCHMO 2018 conference.

## Instructions to setup environment
These notebooks require access to ~100 files from the BARRA sample data and a few non-standard python libraries. While the sample data are available to download from our BARRA public __[webpage](http://www.bom.gov.au/clim_data/rrp/BARRA_sample/)__, downloading all of the files will be frustrating. I have made the entire sample datasets available on a filesystem on NCI, and have utilised the access conda python environments available on NCI. So, if you have an NCI account you should be able to run this notebook 'out of the box'. If you do not, it may be a little complicated. But please email me and I'll be happy to help as much as I can, nathan.eizenberg@bom.gov.au .

 1. For the simplest option run these notebooks on the NCI Virtual Desktop Infrastructure (VDI) using the public conda python environments set up by Scott Wales. Instructions to get set up on the VDI and using conda envs here https://accessdev.nci.org.au/trac/wiki/User%20Guides/conda. However, you can also run these notebooks on the Raijin nodes in an interactive session.
 
 2. Then load the conda environment 'analysis3-unstable' from the terminal
    
    ```>$ module use /g/data3/hh5/public/modules```
    
    ```>$ module load conda/analysis3-unstable```
    
    Alternatively, if you are not using the NCI conda environments, you will need to create your own. I have included the __[environement.yml](https://github.com/nathan-eize/AMOS2018-BARRA-data-demos/blob/master/conda-env/environment.yml)__  and the __[spec_file.txt](https://github.com/nathan-eize/AMOS2018-BARRA-data-demos/blob/master/conda-env/spec_file.txt)__ files in this repository. You can create your own environment using the following command but please note that these conda environment files can become quite big! 
    
    ```>$ $ conda create --name <env> --file <this file>```
    
 3. Clone this repository into your working area 
    
    ```>$ git clone https://github.com/nathan-eize/AMOS2018-BARRA-data-demos.git```
    
 4. Start a python notebook client
    
    ```>$ jupyter notebook```
    
    This should start a firefox browser hosted on your localhost port.
    
 1. Note the location of th BARRA sample data ```raijin:/g/data/ma05/sample```
    
 5. Your environment is setup and you're ready to open and run this notebook!
 
## Ready-to-run exercises to explore the dataset

We've put together a couple of exercises that run off the publicly available BARRA sample dataset. After you've set up your environment and have some local copy of the sample data files you need, you should be able to run the following exercises.

### Create animation of pressure level wind vectors (script)

Create an animation of wind vectors of the BARRA_R or BARRA_TA domains, stepping through the pressure level wind fields descending from the top of the atmosphere to the surface. 

https://github.com/nathan-eize/AMOS2018-BARRA-data-demos/blob/master/plot_prs_wind.py

Usage: 
```
[nwe548@vdi-n18 tempdir]$ module use /g/data3/hh5/public/modules
[nwe548@vdi-n18 tempdir]$ module load conda/analysis3-unstable
(analysis3-18.01) [nwe548@vdi-n18 tempdir]$ python ~/code/AMOS2018-BARRA-data-demos/plot_prs_wind.py
```

### Plot an interactive timeseries of multiple parameters at a given pixel using plotly (Jupyter notebook)

This is a notebook example, so you can run it interactively (using NCI VDI) follow the instructions in the notebook https://github.com/nathan-eize/AMOS2018-BARRA-data-demos/blob/master/plot_BARRA_sample_timeseries_plotly.ipynb



