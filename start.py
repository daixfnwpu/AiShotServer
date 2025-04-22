import subprocess

# Define the IP address and port
#ip_address = '192.168.3.116'
ip_address = '0.0.0.0'
port = '8080'

# Command to run the Django development server
command = f'python manage.py runserver {ip_address}:{port}'

# Run the command using subprocess
subprocess.run(command, shell=True)