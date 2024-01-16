# What is it and why does it exist?

It's an easy-to-use tool for face frontalization. 
This project was created for lazy people who, like me, had a lot of problems when launching other face frontalization projects.

# Installation 

I recommend to use [Anaconda](https://www.anaconda.com/download).

To install open Anaconda Prompt, than go to the folder where you saved the lazy-face-frontalization project and paste this:
```
conda env create -f environment.yml
```

Download model ([link1](https://drive.google.com/file/d/1krOLgjW2tAPaqV-Bw4YALz0xT5zlb5HF/view) or [link2](https://drive.google.com/file/d/1bRWIrDtVRdCneMerq2aN3dAMV_NTanCW/view?usp=sharing)) and place it like ```"C:\Users\<Your_Username>\.insightface\models\inswapper_128\inswapper_128.onnx"``` (for Windows) ```"home/.insightface/models/inswapper_128/inswapper_128.onnx"``` (for Linux)

That`s it!!!

# Usage

You can run the ```demo.ipynb``` if you want to see an example of how it works OR you can place your own face images in input folder and run the ```frontalization.ipynb``` / ```frontalization.py```.
After that, the cropped frontalized faces will appear in the output folder.


# How it works?

I lied a bit when I wrote that it was face frontalization. This program just takes the face from the input image and swapp it with the  frontalized dummy face. But it doesn't matter because I think the accuracy is pretty good.

## **Note:**
- color of the output face depends on the color of the dummy.
- you can change the dummy image in ```frontalization.ipynb``` / ```frontalization.py```








