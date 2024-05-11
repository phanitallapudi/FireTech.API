import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


class EquipmentMaintainancePredictor:
    def __init__(self) -> None:
        pass

    def predict_maintenance(self, operating_hours, temperature, pressure):
        # Load data
        merged_df = pd.read_csv('merged_data.csv')

        # Features and target variable
        X = merged_df[['Operating_Hours', 'Temperature', 'Pressure']]
        y = merged_df['Maintenance_Type']

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        param_grid = {
            'n_estimators': [50, 100],
            'max_depth': [None, 10],
            'min_samples_split': [2, 5],
            'min_samples_leaf': [1, 2]
        }

        # Reduce the size of the parameter grid for faster search
        grid_search = GridSearchCV(RandomForestClassifier(random_state=42), param_grid, cv=5)
        grid_search.fit(X_train, y_train)

        # Get the best model
        best_model = grid_search.best_estimator_

        # Evaluate the best model
        y_pred = best_model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        print("Best Model Accuracy:", accuracy)

        # Make predictions (example)
        new_data = pd.DataFrame({'Operating_Hours': [operating_hours], 'Temperature': [temperature], 'Pressure': [pressure]})
        predicted_maintenance = best_model.predict(new_data)
        print("Predicted Maintenance:", predicted_maintenance)
        
        return {"predicted_maintenance": predicted_maintenance[0]}