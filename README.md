# apm-counter

This is a simple Program displaying the current APM, calculated by the average time diff of the last 12 inputs. \
The APM takes into account all keyboard and mouse presses. After a period of ideling the APM will start to decrease. The factor of APM decrease grows each idle-cycle.

![image](https://user-images.githubusercontent.com/31525324/171631271-fb5d0dc3-fed3-4647-b994-d37ff9f1134e.png)


# Run instructions:
To run create virtualenv in project folder and run the following commands.

python -m pip install -r requirements.txt
python .\main.py


To close the Application press the close button in the top right or press the "left control" + "backspace" keys.

ToDo: Add 1 click exe
