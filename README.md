                                                                            ##
                                     ####                                   ##
                                    ## ##  ###  ## ##  ### ##  ###  ## ### #####   ###  ## ###
                                    ##    ## ##  ## ##  ## ## ## ##  ### #  ##    ## ##  ### #
                                    ##    ## ##  ## ##   ###  #####  ##     ##    #####  ##
                                    ## ## ## ##  ## ##   ###  ##     ##     ## ## ##     ##
                                     ###   ###   ## ##    #    #### ####     ###   #### ####

# Introduction
Python code to convert the pdf to high quality image and attach associated metadata.

# Folder architecture
                                                      C:.
                                                      │   converter.py
                                                      │   LICENSE
                                                      │   README.md
                                                      │   requirements.txt
                                                      │
                                                      ├───Dump
                                                      ├───Input
                                                      │       0bbe4645-247e-40ee-9f9a-945f5ac1e582.json
                                                      │       0bbe4645-247e-40ee-9f9a-945f5ac1e582.pdf
                                                      │
                                                      ├───Output
                                                      └───poppler
# How to use?
Put all the pdf with json data(need to attach as meta data) in Input folder.

- To convert pdf to image and attach metadata run
        ```
        python converter.py -d 1
        ```
- To attach the metadata on png run
        ```
        python coverter.py -i 1
        ```
- For help run
        ```
        python converter -h
        ```
- All raw data will be shifted to **Dump** folder and processed data to **Output** folder

# Author
Ashish Kumar

For any clarification on code, please feel free to drop an email to **Ashish.Kashyap@csscorp.com**

Made with ❤️ in Ranchi, India

# License

Copyright (c) 2020 Ashish Kumar
