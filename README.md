# coco for ROS2
cd, build, source. All in one command!
Now with GUI folder selection.

<p align="center">
  <img src="https://github.com/Nopparuj-an/coco/blob/main/images/demo.gif?raw=true">
</p>

<br>

## Installation
1. Download the file from the release tab.
2. Run installer by right-click the `coco-tool.deb` file, select `Open With Other Application` and `Software Install`, click `Install` and enter your password.

If you prefer to install via terminal, run
```bash
sudo dpkg -i coco-tool.deb
```
3. Add `source coco-source` to your .bashrc file

Or run this command to add it automatically
```bash
echo "source coco-source" >> ~/.bashrc
```

<br>

## Usage
#### Run build
```bash
coco
```

<p align="center">
  <img src="https://github.com/Nopparuj-an/coco/blob/main/images/GUI.png?raw=true">
</p>

The first time you run this command, coco will ask you to set you workspace path, simply select the folder and hit save.

<br>

#### Modify workspace path location
```bash
coco-config
```

<br>

## Uninstallation
```bash
sudo apt remove coco-tool
```

<br>

## Building from source
In the root directory of the project, run
```bash
dpkg-deb --build debian
```
