# coco for ROS2
cd, build, source. All in one command!
Now with GUI folder selection.

<p align="center">
  <img src="https://github.com/Nopparuj-an/coco/blob/main/images/GUI.png?raw=true">
</p>

<br>

## Installation
```bash
sudo dpkg -i coco-tool.deb
```
Or right-click the `coco-tool.deb` file, select `Open With Other Application` and `Software Install`, click `Install` and enter your password.

<br>

## Usage
#### Run build
```bash
coco
```
The first time you run this command, coco will ask you to set you workspace path, simply select the folder and hit save.

<br>

#### Modify workspace path location
```bash
coco-config
```

<br>

## Building from source
In the root directory of the project, run
```bash
dpkg-deb --build debian
```
