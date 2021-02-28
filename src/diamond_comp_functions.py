import pandas as pd

def diamond_submission(model, train_data, train_pred, test_data, file_name, expected_rows=13485, file_path="../data/"):
    '''
    For use in the kagggle diamond competition.
    Given a model, train and test data, a file name, expected rows and file path, creates csv file ready
    for submission
    
    Takes: a model, train and test data, a file name, expected rows and file path
    Returns: csv file for submission
    '''
    
    # retraining the model with all of the data
    model.fit(train_data, train_pred)
    
    # making final prediction
    y_final_pred = model.predict(test_data)
    
    # creating submission dataframe
    subm_df = pd.DataFrame(y_final_pred, columns = ['price'])

    subm_df['id'] = subm_df.index

    subm_df = subm_df[['id', 'price']]
    
    # checking if number of rows matches expectation and creating csv
    if subm_df.shape[0] == expected_rows:
        subm_df.to_csv(file_path+f'{file_name}.csv', index=False)
        return f"{file_name}.csv has been created in {file_path}"
    else:
        return f"Unexpected number of columns. Received {subm_df.shape[0]}, expected {expected_rows}"