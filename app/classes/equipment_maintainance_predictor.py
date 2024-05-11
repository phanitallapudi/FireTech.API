import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.metrics import accuracy_score


class EquipmentMaintainancePredictor:
    def __init__(self) -> None:
        pass

    def predict_maintenance_type_cost(self, equipment_id, operating_hours, temperature, pressure):
        # Load data
        merged_df = pd.read_csv('merged_data.csv')

        # Filter data for the specified equipment ID
        equipment_data = merged_df[merged_df['Equipment_ID'] == equipment_id]

        # Features and target variable
        X = equipment_data[['Operating_Hours', 'Temperature', 'Pressure']]
        y_type  = equipment_data['Maintenance_Type']
        y_cost = equipment_data['Maintenance_Cost']

        # Check for class imbalance
        class_counts = y_type.value_counts()
        min_class_count = class_counts.min()

        # Determine the maximum number of splits in cross-validation
        max_splits = min(5, min_class_count)  # Adjust as needed

        X_train_type, X_test_type, y_train_type, y_test_type = train_test_split(X, y_type, test_size=0.2, random_state=42)

        param_grid = {
            'n_estimators': [50, 100],
            'max_depth': [None, 10],
            'min_samples_split': [2, 5],
            'min_samples_leaf': [1, 2]
        }

        grid_search_type = GridSearchCV(RandomForestClassifier(random_state=42), param_grid, cv=max_splits)
        grid_search_type.fit(X_train_type, y_train_type)

        best_model_type = grid_search_type.best_estimator_

        # Split the dataset for maintenance cost prediction
        X_train_cost, X_test_cost, y_train_cost, y_test_cost = train_test_split(X, y_cost, test_size=0.2, random_state=42)

        # Train model for maintenance cost prediction
        param_grid_cost = {
            'n_estimators': [50, 100],
            'max_depth': [None, 10],
            'min_samples_split': [2, 5],
            'min_samples_leaf': [1, 2]
        }

        grid_search_cost = GridSearchCV(RandomForestRegressor(random_state=42), param_grid_cost, cv=max_splits)
        grid_search_cost.fit(X_train_cost, y_train_cost)

        best_model_cost = grid_search_cost.best_estimator_

        # Make predictions
        new_data = pd.DataFrame({'Operating_Hours': [operating_hours], 'Temperature': [temperature], 'Pressure': [pressure]})
        predicted_maintenance_type = best_model_type.predict(new_data)
        predicted_maintenance_cost = best_model_cost.predict(new_data)

        print("Predicted Maintenance Type:", predicted_maintenance_type)
        print("Predicted Maintenance Cost:", predicted_maintenance_cost)

        return {"predicted_maintenance_type": predicted_maintenance_type[0], "predicted_maintenance_cost": predicted_maintenance_cost[0]}