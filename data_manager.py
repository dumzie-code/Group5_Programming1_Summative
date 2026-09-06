import json

def load_data():
    """
    Reads patients, doctors, and appointments from their respective JSON files.
    Returns empty lists if any file is missing to prevent application crashes.
    """
    # 1. Read patients.json
    try:
        with open('patients.json', 'r') as f:
            patients = json.load(f)
    except FileNotFoundError:
        patients = []

    # 2. Read doctors.json
    try:
        with open('doctors.json', 'r') as f:
            doctors = json.load(f)
    except FileNotFoundError:
        doctors = []

    # 3. Read appointments.json
    try:
        with open('appointments.json', 'r') as f:
            appointments = json.load(f)
    except FileNotFoundError:
        appointments = []

    return patients, doctors, appointments