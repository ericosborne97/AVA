# 🚀 AVA – Autonomous Vehicular Assistant

![Perseverance rover inspiration](https://assets.science.nasa.gov/dynamicimage/assets/science/psd/mars/downloadable_items/4/5/45799_PIA24487.png "NASA/JPL-Caltech – Perseverance rover")

> **Drive like a Martian.**  
> **AVA** is a lightweight Python GUI for **eight-motor rovers** – record paths, steer each wheel, and run fully autonomous drives, all from a slick Tkinter interface.

---

## ✨  Key Features
- **Dual-axis control** – four drive motors + four steering motors (Ackermann-style, just like *Perseverance*)  
- **Path recorder & replay** – teach AVA a route once, let it handle it next time  
- **Autonomous navigation** – optional AI layer for obstacle detection & course correction  
- **Live telemetry** – speed, heading, battery, and sensor panes updated in real-time  
- **Tkinter-Designer GUI** – layouts built with [Tkinter-Designer](https://github.com/ParthJadhav/Tkinter-Designer) for easy tweaking  

---

## 🛠️  Quick Start
```bash
# clone and install
git clone https://github.com/your-username/ava.git
cd ava
pip install -r requirements.txt
python main.py
