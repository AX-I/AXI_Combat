# AXI_Combat
AXI Combat is a networked multiplayer game built on the AXI Visualizer 3D engine.

http://axi.x10.mx/Combat

![Combat Teaser](https://agentxindustries.neocities.org/Combat/DOF_Screenshot%202020%20May%2014%2006-29-01.png)

AXI Combat is released under the GNU General Public License v3 or above.

## Releases
Binaries for Windows, Mac OSX, and Ubuntu Linux are available via the main page http://axi.x10.mx/Combat

## Building from source

### Windows
Download Python >= 3.6
```
python -m pip install numpy numexpr pillow pyautogui opencv-python pyaudio requests pywin32
```
Download PyOpenCL from https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyopencl
```
python -m pip install pyopencl-win_amd64.whl
```

### Mac OSX
Download Python >= 3.6
```
python -m pip install pyopencl numpy numexpr pillow pyautogui opencv-python pyaudio tkmacosx
```

### Ubuntu Linux
After installing Ubuntu 18.04.1 LTS:
```
sudo apt update
sudo apt install python3-pip tk8.6-dev python3-tk python3-pil.imagetk
pip3 install numpy numexpr
pip3 install pyopencl xlib opencv-python
sudo apt install libasound-dev portaudio19-dev
pip3 install pyaudio
```
Drivers might be troublesome
```
sudo add-apt-repository ppa:intel-opencl/intel-opencl
sudo apt update
sudo apt install intel-opencl-icd

sudo add-apt-repository ppa:graphics-drivers/ppa
sudo apt install nvidia-opencl-icd-384
```

