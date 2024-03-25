import os

def load_inventory_and_ping():
    # Execute shell commands
    os.system("docker-compose up -d")
    os.system("docker-compose ps")
    # Set the environment variable ANSIBLE_CONFIG
    os.environ['ANSIBLE_CONFIG'] = f"{os.getcwd()}/ansible.cfg"
    # Run ansible commands
    os.system("ansible all:localhost --list-hosts")
    os.system("ansible all:localhost -m ping")

if __name__ == "__main__":
    load_inventory_and_ping()
