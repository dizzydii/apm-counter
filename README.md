# apm-counter

This is a simple Program displaying the current APM, inspired by the Starcraft 2 APM display. \
The APM takes into account all keyboard and mouse presses. After a period of ideling the APM will start to decrease. The factor of APM decrease grows each idle-cycle.

![image](https://user-images.githubusercontent.com/31525324/171631271-fb5d0dc3-fed3-4647-b994-d37ff9f1134e.png)


# Run instructions:
## Windows
Just run the "Apm Counter.exe". \
Windows might warn you with the following message:\
> Microsoft Defender SmartScreen prevented an unrecognized app from starting. Running this app might put your PC at risk.
Click on "more info" and then on "run anyways". \

If you distrust the exe feel free to build the exe yourself.
## Python
To run create virtualenv in project folder and run the following commands. \
`python -m pip install -r requirements.txt` \
`python .\main.py` 

To close the Application press the close button in the top right or press the "left control" + "backspace" keys.

# Build your own exe 
Run the folowing line in a terminal in the same directory as the main file. \
`pip install pyinstaller` \
`pyinstaller main.py -F -n "Apm Counter" --paths .\venv\Lib\site-packages --noconsole`


# Build with icon
`pyinstaller main.py -F -n "Apm Counter" -i "keyboard.ico" --paths .\venv\Lib\site-packages --noconsole --specpath .\assets\build --distpath .\assets\dist`
