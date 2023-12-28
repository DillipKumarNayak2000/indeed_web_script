import numpy as np
from .database import job_data
# Retrieve salary data for Python developers from MongoDB
python_dev_salaries = [job['salary'] for job in job_data if 'Python Developer' in job['title']]

# Convert salaries to numeric values (cleaning data if necessary)
numeric_salaries = [float(salary.replace('$', '').replace(',', '')) for salary in python_dev_salaries]

# Calculate average salary
average_salary = np.mean(numeric_salaries)
