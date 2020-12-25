from sklearn import datasets, linear_model
# fit the model by linear Regression
regr = linear_model.LinearRegression(fit_intercept = False)
regr.fit(Xbar, y)
# Compare two results
print('Solution by scikit-learn :', regr.coef_)
print('Solution found by (5): ',w.T)