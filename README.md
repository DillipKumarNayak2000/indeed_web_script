git clone <[repository_url](https://github.com/DillipKumarNayak2000?tab=repositories)>
cd <[project_directory](https://github.com/DillipKumarNayak2000/indeed_web_script)>

#Setup Python Environment:
# Create and activate a virtual environment
python3 -m venv venv
#source venv/bin/activate  # for Linux/Mac
venv\Scripts\activate  # for Windows

# Install required packages
pip install -r requirements.txt

#MongoDB Setup:

#Install MongoDB locally or use a cloud-based solution.
#Configure MongoDB connection details in the project.
#Run Django Server:
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
