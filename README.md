# AMOS2018-BARRA-data-demos
Notebooks and code for exploring and demonstrating the BARRA reanalysis dataset for the BOM Data Workshop session at AMOS-ISCHMO 2018 conference

## Instructions to setup environment
These notebooks require access to ~100 files from the BARRA sample data and a few non-standard python libraries. While the sample data are available to download from our BARRA public __[webpage](http://www.bom.gov.au/clim_data/rrp/BARRA_sample/)__, downloading all of the files will be frustrating. I have made the entire sample datasets available on a filesystem on NCI, and have utilised the access conda python environments available on NCI. So, if you have an NCI account you should be able to run this notebook 'out of the box'. If you do not, it may be a little complicated. But please email me and I'll be happy to help as much as I can, nathan.eizenberg@bom.gov.au .

 1. For the simplest option run these notebooks on the NCI Virtual Desktop Infrastructure (VDI) using the public conda python environments set up by Scott Wales. Instructions to get on the VDI and using conda envs here https://accessdev.nci.org.au/trac/wiki/User%20Guides/conda
 2. Then load the conda environment 'analysis3-unstable' from the terminal
    
    ```>$ module use /g/data3/hh5/public/modules```
    
    ```>$ module load conda/analysis3-unstable```
 3. Clone this repository into your working area 
    
    ```>$ git clone https://github.com/nathan-eize/AMOS2018-BARRA-data-demos.git```
 4. Start a python notebook client
    
    ```>$ jupyter notebook```
    
    This should start a firefox browser hosted on your localhost port 
 5. Your environment is setup and you're ready to open and run these notebooks!
