import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_dummy_maintenance_data(num_records=500, num_equipment=50):
    np.random.seed(0)
    
    # Generate dummy historical maintenance data
    start_date = datetime(2018, 1, 1)
    end_date = datetime(2022, 1, 1)
    dates = [start_date + timedelta(days=np.random.randint((end_date - start_date).days)) for _ in range(num_records)]
    equipment_ids = np.random.randint(1, num_equipment + 1, size=num_records)
    
    maintenance_actions = []
    maintenance_costs = []
    operating_hours = []
    
    for _ in range(num_records):
        maintenance_type = np.random.choice(['Servicing', 'Replacement', 'Breakdown'], p=[0.4, 0.4, 0.2])
        if maintenance_type == 'Servicing':
            cost = np.random.randint(100, 500)
            hours = np.random.randint(1000, 2000)
        elif maintenance_type == 'Replacement':
            cost = np.random.randint(500, 800)
            hours = np.random.randint(2000, 4000)
        else:  # Breakdown
            cost = np.random.randint(800, 1200)
            hours = np.random.randint(4000, 6000)
        
        maintenance_actions.append(maintenance_type)
        maintenance_costs.append(cost)
        operating_hours.append(hours)
    
    maintenance_df = pd.DataFrame({
        'Date': dates,
        'Equipment_ID': equipment_ids,
        'Maintenance_Type': maintenance_actions,
        'Maintenance_Cost': maintenance_costs,
        'Operating_Hours': operating_hours
    })
    
    return maintenance_df

def generate_dummy_performance_data(num_equipment=500):
    np.random.seed(0)
    
    # Generate dummy current performance metrics data
    operating_hours = np.random.randint(1, 5000, size=num_equipment)
    temperatures = np.random.uniform(50, 100, size=num_equipment)
    pressures = np.random.uniform(20, 40, size=num_equipment)
    
    performance_df = pd.DataFrame({
        'Equipment_ID': range(1, num_equipment + 1),
        'Temperature': temperatures,
        'Pressure': pressures
    })
    
    return performance_df

# Generate and save dummy data

# Read the generated CSV files
maintenance_df = generate_dummy_maintenance_data()
performance_df = generate_dummy_performance_data()

# Merge maintenance and performance data based on Equipment_ID
merged_data = pd.merge(maintenance_df, performance_df, on='Equipment_ID')

# Save the merged data to a new CSV file
merged_data.to_csv('merged_dataq.csv', index=False)
print("Merged data saved to CSV file: merged_data.csv")
