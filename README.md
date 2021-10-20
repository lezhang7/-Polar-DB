# Polar-DB based Educational Administration System

### More information about this project please refer to [here]:https://zhangle.netlify.app/project/database-system/

## Code Structure
```
|__ UI/ --> all UI design and main function
    |__ __init__.py 
    |__ admin.py --> log in UI
    |__ department.py --> department settings for teacher account
    |__ icon.py -->  icons for all operations
    |__ login.py --> main file for launch the system
    |__ main_window.py --> main console file when login sucessfully
    |__ teacher.py --> login UI for teacher account(student account can't access this interface)
|__ img/ --> all images for the system
|__ main.py PolarDB connection settings
```

## Getting Started
install with  `pip install -r requirements.txt` 
run with `python login_ui.py`

<!-- login_ui.py是主文件，子界面teacher,student,courses以类的形式存在该程序内 
main_window.py是主界面的设计文件，包括了主界面的
几个.ui程序，是根据qtdesigner设计时生成的ui界面，通过Pyqt5转换成对应的.py文件 -->

