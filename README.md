# Frequalizer - Multi-usage Equalizer

## Table of Contents

- [Introduction](#Description)
- [Quick Preview](#quick-preview)
- [Project Structure](#project-structure)
- [How to Run The Project](#run-the-project)
- [Team](#team)


### Description
Signal equalizer is a basic tool in the music and speech industry. It also serves in several biomedical
applications like hearing aid abnormalities detection.

This is a web application that can open a signal and allow the user to change the magnitude of some
frequency components via sliders and reconstruct back the signal.


The application is able to work in different modes:
1. **Uniform Range Mode**: where the total frequency range of the input signal is divided uniformly into 8 equal
ranges of frequencies, each is controlled by one slider in the UI.

2. **Vocals Mode**: where each slider can control the magnitude of specific vocals. It manipulates the speech specific vocals which are composed of different frequency components/ranges.

3. **Musical Instruments Mode**: where each slider can control the magnitude of a specific musical instrument in
the input music signal.

4. **Biological Signal Abnormalities Mode**: where each slider can control the magnitude of a specific abnormality (e.g.
ECG arrhythmia) in the input biological signal.

5. **Voice Tone Changer Mode**: where you can change the tone of a person to be more masculine or more feminine according to the slider in the UI.

### Quick Preview

#### Uniform Range Mode
![](./uploads/readme%data/basic.gif)
#### Vocals Mode
![](./uploads/readme%data/vocals.gif)
#### Musical Instruments Mode
![](./uploads/readme%data/mosica.gif)
#### Biological Signal Abnormalities Mode (ECG Arrhythmia)
![](./uploads/readme%data/medical.gif)
#### Voice Tone Changer Mode
![](./uploads/readme%data/tone.gif)


### Project Structure
The Web Application is built using:
- UI:
  - Streamlit (Python)
  - ReactJS (JavaScript)
  - CSS
- Processing:
  - Streamlit (Python)

This Application is built using streamlit framework, which enables python processing and building user interfacing using
python only. CSS is added to improve the overall UI, while integrating ReactJS components like the sliders and buttons to
have better UI performance and design.

````
master
├─ Data (Sliders' Ranges Data)
├─ Notebooks (Raw Python Processing & Wav files)
│  └─  data
├─ Processing (Application Processing Class)
├─ state_managment (Application State Mangement Class)
├─ Styles (CSS Files)
├─ UI (UI Classes)
│  ├─  Views (Graphs, SLiders, Spectrograms)
│  └─  Widgets (SlidersWidgets, Speed Control, Upload)
│      └─  builds (React Components Builds)
├─ uploads (Produced files)
├─ gitignore
├─ gitattributtes
├─ app.py (main driver file)
├─ requirements.txt (project dependencies)
└─ README.md
````


### Run The Project

1. Install Python3 in your computer
``` 
Download it from www.python.org/downloads/
```

2. Install the project dependencies
```shell
pip install requirements.txt
```

3. Start Application
```shell
streamlit run app.py
```

4. Visit http://localhost:8501

### Team

First Semester - Biomedical Digital Signal Processing (SBE3110) class project created by:

| Team Members' Names                                  | Section | B.N. |
|------------------------------------------------------|:-------:|:----:|
| [Ibrahim Mohamed](https://github.com/1brahimmohamed) |    1    |  2   |
| [Kamel Mohamed](https://github.com/KamelMoohamed)    |    2    |  10  |
| [Ahmed El Sarta](https://github.com/ahmed-elsarta)   |    1    |  8   |
| [Saeed El Sayed](https://github.com/saeedelsayed)    |    1    |  42  |

### Submitted to:
- Dr. Tamer Basha & Eng. Abdallah Darwish
All rights reserved © 2022 to Team 1 - Systems & Biomedical Engineering, Cairo University (Class 2024)