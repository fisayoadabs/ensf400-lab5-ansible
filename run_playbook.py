import json
from ansible_runner import run

def run_hello_playbook():
    result = run(
        private_data_dir="./", 
        playbook="hello.yml"
    )
    
    # Convert the generator object to a list and take only the first 10 events
    events_list = list(result.events)[:10]
    
    # Create a dictionary containing relevant attributes
    result_dict = {
        "status": result.status,
        "events": events_list,
        # Add other relevant attributes as needed
    }
    
    # Convert the dictionary to JSON format
    result_json = json.dumps(result_dict)
    print(result_json)

if __name__ == "__main__":
    run_hello_playbook()
