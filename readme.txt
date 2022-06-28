
##Function use to make prediction
 ## MacDeep Dili FIle
    def model_predict(X, y, model, col_name):
    y_pred = model.predict(X)
    y_pred_class = np.where(y_pred > 0.5, 1, 0)
    pred_result = pd.DataFrame()
    pred_result['id'] = y.index
    pred_result['y_true'] = y.values
    pred_result['prob_'+col_name] = y_pred
    pred_result['class_'+col_name] = y_pred_class

    result=measurements(y, y_pred_class, y_pred)
    return pred_result, result

  ##Mol2Veclr file
    def measurements(y_test, y_pred, y_pred_prob):
    acc = metrics.accuracy_score(y_test, y_pred)
    sensitivity = metrics.recall_score(y_test, y_pred)
    TN, FP, FN, TP = confusion_matrix(y_test, y_pred).ravel()
    specificity = TN/(TN+FP)
    precision = metrics.precision_score(y_test, y_pred)
    f1 = metrics.f1_score(y_test, y_pred)
    mcc = metrics.matthews_corrcoef(y_test, y_pred)
    auc = roc_auc_score(y_test, y_pred_prob)
    npv = TN/(TN+FN)
    return [TN, FP, FN, TP, acc, auc, sensitivity, specificity, precision, npv, f1, mcc]

    def model_predict(X, y, model, col_name):
    y_pred_prob = model.predict_proba(X)
    # keep probabilities for the positive outcome only
    y_pred_prob = y_pred_prob[:, 1]
    y_pred_class = np.where(y_pred_prob > 0.5, 1, 0)


##Toxicity Measurement
    ##MacDeep Dili File
    def measurements(y_test, y_pred, y_pred_prob):
    acc = metrics.accuracy_score(y_test, y_pred)
    precision = metrics.precision_score(y_test, y_pred)
    f1 = metrics.f1_score(y_test, y_pred)
    mcc = metrics.matthews_corrcoef(y_test, y_pred)
    auc = roc_auc_score(y_test, y_pred_prob)
    sensitivity = metrics.recall_score(y_test, y_pred)
    balanced_accuracy = balanced_accuracy_score(y_test, y_pred)

    TN, FP, FN, TP = confusion_matrix(y_test, y_pred).ravel()
    specificity = TN/(TN+FP)
    npv = TN/(TN+FN)
    return [TN, FP, FN, TP, acc, auc, sensitivity, specificity, precision, npv, f1, mcc, balanced_accuracy]


##Training Data

    ##MacDeep Dili File
    def dim_reduce(df, test_df, col_name1):

    X = df.iloc[:, 3:]
    y = df.loc[:, 'y_true']
    X_test = test_df.iloc[:, 3:]
    y_test = test_df.loc[:, 'y_true']

    sc = StandardScaler()
    sc.fit(X)
    X = sc.transform(X)
    X_test = sc.transform(X_test)