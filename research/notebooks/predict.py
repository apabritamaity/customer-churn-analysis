class ChurnPredictor:

    def __init__(self, model, threshold):
        self.model = model
        self.threshold = threshold

    def predict(self, X):

        prob = self.model.predict_proba(X)[:,1]

        return (prob >= self.threshold).astype(int)

    def predict_proba(self, X):

        return self.model.predict_proba(X)