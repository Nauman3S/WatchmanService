<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="watchmanservice.png" alt="Project logo"></a>
</p>

<h3 align="center">Watchman Service</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()


</div>

---


<p align="center"> Watchman Service
    <br> 
</p>

## 📝 Table of Contents

- [📝 Table of Contents](#-table-of-contents)
- [🧐 About <a name = "about"></a>](#-about-)
- [Getting Started <a name = "getting_started"></a>](#getting-started-)
  - [RPiClient Installation <a name = "Installation"></a>](#rpiclient-installation-)
    - [Auto Installer](#auto-installer)
- [Config Details <a name = "config"></a>](#config-details-)
  - [Config Variables](#config-variables)
- [Usage <a name = "usage"></a>](#usage-)
- [⛏️ Built Using <a name = "built_using"></a>](#️-built-using-)
- [✍️ Authors <a name = "authors"></a>](#️-authors-)


## 🧐 About <a name = "about"></a>

This repo contain files and detailed instructions on running the Watchman Service


## Getting Started <a name = "getting_started"></a>



### RPiClient Installation <a name = "Installation"></a>


#### Auto Installer
To install and Run RPi Client Automatically just run the following command on your Raspberry Pi terminal

- ```curl -sSL  https://raw.githubusercontent.com/Nauman3S/WatchmanService/main/installer.sh  | bash```

After the installer completes the process restart your raspberry pi.



## Config Details <a name = "config"></a>


### Config Variables


```http
Configure variables in varibales.py file
```

| Variable | Description | 
| :---  | :--- |
| `GUI_APP_PATH` | **Required**. *Complete path to your GUI App*  |
| `GUI_APP_WINDOW_NAME` | **Required**.  *Window name shown on the title bar of the app.*|
| `TERMINAL_NAME` | **Required**.  *Name of the terminal*|
| `FILEMANAGER_NAME` | **Required**.  *Name of the filemanager*|

-   Note: The variables.py is pre-configured for Ubuntu MATE but you will have to counter-check the paths and names before running the program.
## Usage <a name = "usage"></a>

1.  Run installer script on your Raspberry Pi.
2.  Configure the varibles.py file based on your program names.
3.  To stop running the Watchman Service automatically on boot, in the /boot partition of your SD Card, open the file named WatchmanService.conf and replace ``RUN_ON_BOOT=1`` with ``RUN_ON_BOOT=0``

## ⛏️ Built Using <a name = "built_using"></a>

- [Python](https://www.python.org/) - For programming the Watchman Service
  

## ✍️ Authors <a name = "authors"></a>

- [@Nauman3S](https://github.com/Nauman3S) - Development and Deployment
