# Youtube-Video-Face-Extraction-using-python

<img src="https://www.google.com/imgres?imgurl=https%3A%2F%2Fwww.logo.wine%2Fa%2Flogo%2FYouTube%2FYouTube-Icon-Full-Color-Logo.wine.svg&imgrefurl=https%3A%2F%2Fwww.logo.wine%2Flogo%2FYouTube&tbnid=zm4mFmL-l08cyM&vet=12ahUKEwiLl-Hs8Jb9AhWU0TgGHSjzCe0QMygIegUIARDvAQ..i&docid=-WouIiroWvqmWM&w=1200&h=800&q=youtube%20logo&ved=2ahUKEwiLl-Hs8Jb9AhWU0TgGHSjzCe0QMygIegUIARDvAQ" width="500px" height="300px" alt="architecture.jpg" align=center />

## Instructions to Run the Code:

To run this code, you will need to have Python installed on your system and create a Python virtual environment. Here are the steps to follow:
Install Python virtual environment using pip by running the following command:

> pip install virtualenv

 If you already have virtualenv installed, you can skip this step.
Verify that pip is installed correctly by running the pip command and checking for any errors.

Change to the directory where you want to run the code.
Create a new virtual environment using the following command:

virtualenv Youtube

 If you get an error that "virtualenv" is not recognized as the name of a command, you will need to set the environment path as follows:

>Open the start menu and search for "environment variables".
- Click on "Edit the system environment variables".
- Click on the "Environment Variables" button.
- Under "System Variables", find the "Path" variable and click "Edit".
- Click "New" and enter the full path to the directory containing virtualenv.exe. For example, "C:\Users\USERNAME\AppData\Roaming\Python\Python39\Scripts".
- Click "OK" to save the changes.
- Once you have set the path variable, you can run the "virtualenv" command again to create the virtual environment.

Activate the virtual environment by running the following command:
Copy code
.\Youtube\Scripts\activate

Install two Python libraries required to run the code by running the following commands:
Copy code

> pip install opencv-python pip install pytube

Once both modules are installed, you can run the Python code using the following command:
Copy code

> python .\yt_face

 Please note that the code may take a while to execute, especially for longer videos.

After successful execution, you will be able to see frames and faces stored in their respective folders. Please note that larger videos may generate a large number of frames and faces.
