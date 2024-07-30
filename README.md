# AXI_Combat
AXI Combat is a networked multiplayer game built on the AXI Visualizer 3D engine.

![Combat Teaser](https://agentxindustries.neocities.org/Combat/AXICombat.jpg)

AXI Combat is released under the GNU General Public License v3 or above.

## Releases
Binaries for Windows, Mac OSX, and Ubuntu Linux are available via the main page https://axi.x10.mx/Combat

## Building from source

You'll need to run `git clone --recursive` to include the core source code submodule (https://github.com/AX-I/Combat_Core).

### Windows, Mac OSX
Download Python >= 3.8
```
python -m pip install -r requirements.txt
```

### Ubuntu Linux
After clean installation:
```
sudo apt update
sudo apt install python3-pip tk8.6-dev python3-tk python3-pil.imagetk
sudo apt install libasound-dev portaudio19-dev
pip3 install xlib
pip3 install -r requirements.txt
```

Drivers might be troublesome
```
sudo add-apt-repository ppa:intel-opencl/intel-opencl
sudo apt update
sudo apt install intel-opencl-icd

sudo add-apt-repository ppa:graphics-drivers/ppa
sudo apt install nvidia-opencl-icd-384
```

