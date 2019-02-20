# Download-Images-With-Python

This is a simple Python script that can download images from given URL. 

# Dependencies

    atomicwrites==1.3.0
    attrs==18.2.0
    more-itertools==6.0.0
    pluggy==0.8.1
    py==1.7.0
    pytest==4.3.0
    six==1.12.0
   
# How to Use

Before runnig this script make sure you have installed python3.6, pip and virtualenv. You can download Python from https://www.python.org/downloads/ and virtualenv from https://virtualenv.pypa.io/en/stable/ . While installing python in windows, choose the advance option. So that pip will automatically install which is very important. For Linux/OSX you don't need to install python and pip. Newer version of Linux and OSX has pre-installed Python3 and Pip. 

    # Download the source code.
    1. Open the terminal(Linux/OSX). For windows you can use Poweshell. You can download Poweshell from
    https://github.com/PowerShell/PowerShell. You can also use cmd.
    
    N.B. If you want to run this script with Python IDLE, then skip this guideline, just download the
    source code & run the file test_download_images.py . Make sure all dependencies are installed.
    
    2. Write the following commands - 
        
        git clone https://github.com/raselcse07/Download-Images-With-Python   # clone the source code
        cd Download-Images-With-Python  # navigate to source folder
        virtualenv .  # create virtual environment
        source bin/activate  # activate virtual environment
        pip install -r requirements.txt
        pytest test_download_images.py
        
    Done. All images are stored in Download-Images-With-Python/Images Folder. 
    
# Update Images URL
    
    You need to change the images URL in Testcase Folder. Open the Testcase 
    folder (Download-Images-With-Python/Testcase).You will see three files 
    (images.txt, images2.txt, images3.txt). These are the test URLs. 
    Every files contain image URLs,one per line.Just remove these URLs & add your desired URLs. 
    
    *** If you want one single file that contains all URLs, then modify the 
    test_download_images.py file. Open the file test_download_images.py. 
    You will see something like - 
    
            assert main("Testcase/images.txt") == True
            assert main("Testcase/images2.txt") == True
            assert main("Testcase/images3.txt") == True
            
    Remove  assert main("Testcase/images2.txt") == True 
    & assert main("Testcase/images3.txt") == True , then save it. 
    Enlist all of your URL in Testcase/images.txt file. Now run .
