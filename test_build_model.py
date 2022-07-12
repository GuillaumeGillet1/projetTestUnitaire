import build_model

def test_build_model():
    import pandas as pd 
    from sklearn.linear_model import LinearRegression
    import joblib
    X = [205.9991686803,2,0]
    y = df['price']
    model = joblib.load("regression.joblib")
    model.fit(X, y)
    expected_result = 260972.164974894 
    actual_result = model.predict(y)
    assert actual_result == expected_result