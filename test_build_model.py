import build_model

def testSuperieurZero():
    import pandas as pd 
    from sklearn.linear_model import LinearRegression
    import joblib
    X = [[1,1,0]]
    model = joblib.load("regression.joblib")
    actual_result = model.predict(X)
    assert actual_result > 0

def testValeurTaille():
    import pandas as pd 
    from sklearn.linear_model import LinearRegression
    import joblib
    X = [[200,2,0]]
    X2 = [[100,2,0]]
    model = joblib.load("regression.joblib")
    actual_result = model.predict(X)
    actual_result2 = model.predict(X2)
    assert actual_result > actual_result2