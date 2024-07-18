# Jetson_Nano_Power_Statistics
This repository contains power statistics of NVIDIA's Jetson Nano while training face recognition model and also inferencing. I used the jtop library to collect the data and to control the active CPU cores, CPU frequency and GPU frequency I edited the nvpmodel.conf file found at /etc/nvpmodel.conf. I have also added a file named stats.py which contains the code I wrote which collects the data and saves it. When you run stats.py it will ask you to enter a filename you want to save the data to. It will create that file for you with the name you entered.


The face recognition model used can be found here https://github.com/ageitgey/face_recognition. The dataset that was used to train this model contained approximately 4000 images.


By default Jetson Nano comes with two power modes called MAXN and 5W. You can check their details here https://docs.nvidia.com/jetson/archives/l4t-archived/l4t-3275/index.html#page/Tegra%20Linux%20Driver%20Package%20Development%20Guide/power_management_nano.html. I added 3 more modes: CPU1GPU0 (1 CPU core active and GPU frequency set to minimum), CPU1GPU1(1 CPU core active and GPU frequency set to maximum) and CPU4GPU0 (All CPU cores active and GPU frequency set to minimum). The MAXN mode has all CPU cores active and GPU frequency at maximum. 5W mode has 2 CPU cores active and GPU frequency is a bit reduced.


During the inferencing part I noticed that when my face was being detected there was a reduction in the FPS. Therefore, I have collected statistics which takes this into account by first hiding my face and collecting data then running the inferencing part again with my face always in view of the webcam.


This study was conducted to see if we can save power on resource constrained devices by switching off CPU cores or reducing GPU frequency without having much of an effect on machine learning training and inferencing performance. 
