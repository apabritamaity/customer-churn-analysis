from data_loader import load_data
from preprocessing import preprocess
from feature_engineering import engineer_features
class TrainingPipeline:

    def __init__(self):
        self.load_data = load_data
        self.preprocess = preprocess
        self.engineer_features = engineer_features 
        
    def run(self):
        data = self.load_data()
        print(f"data loaded successfully.\nShape={data.shape}")

        data = self.preprocess(data)
        print(f"\ndata preprocessing has been successful")
        print(data.shape)

        X_train, y_train = self.engineer_features(data)
        print(X_train.shape, y_train.shape)
        print(X_train.head())

        # model = self.train(data)
        # metrics = self.evaluate(model)
        # self.export(model, metrics)