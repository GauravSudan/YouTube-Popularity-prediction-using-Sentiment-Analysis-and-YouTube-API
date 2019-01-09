import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from date import date_fun


def food_fun():
    
    X=[]    #X=dates
    Y=[]    #Y=views
    dataset = pd.read_csv('food.csv')
#TO GET DATA IN dates n views
    def get_data(filename):
        with open(filename,'r') as csvfile:
            csvFileReader = csv.reader(csvfile)
            next(csvFileReader)                     #to skip 1st row ie header row
            for row in csvFileReader:                   #for iteration of each rows
            #X.append(int(row[0].replace("-","")))
            #X.append(int(row[0].split('-')[0]))
                X.append(int(row[1]))
                Y.append(float(row[2]))
        return

    get_data('food.csv')


    from sklearn.cross_validation import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.3)

    X_train=np.reshape(X_train,(len(X_train),1))
    y_train=np.reshape(y_train,(len(y_train),1))
    X_test=np.reshape(X_test,(len(X_test),1))
    y_test=np.reshape(y_test,(len(y_test),1))


#X_poly=np.reshape(y_test,(len(y_test),1))
    X=np.reshape(X,(len(X),1))
    Y=np.reshape(Y,(len(Y),1))

#######################################################################################
#MODEL HERE


# Feature Scaling
    from sklearn.preprocessing import StandardScaler
    sc_X = StandardScaler()
    sc_y = StandardScaler()
    X1 = sc_X.fit_transform(X_train)
    Y1 = sc_y.fit_transform(y_train)
    
    # Fitting SVR to the dataset
    from sklearn.svm import SVR
    regressor = SVR(kernel = 'rbf')
    regressor.fit(X1,Y1)
    
    
    #APPLY KFOLD METHOD
    from sklearn.model_selection import cross_val_score
    accuracies = cross_val_score(estimator = regressor, X=X1 , y=Y1,cv = 10)
    accuracies.mean()
    accuracies.std()
    
    #print(accuracies.mean())
    #print(accuracies.std())
    
    
    #######################################################################################
       #Calculating views till a particular day
    days=[]
    days=date_fun()
    day1=days[0]
    day2=days[1]
    #print(day1)
    #print(day2)
    totalviews=0
    #daycount=1
    #xday=[]
    #yviews=[]
    for i in range(day1,day2+1):
        
        y_pred1 = sc_y.inverse_transform(regressor.predict(sc_X.transform(np.array([[i]]))))
        #xday.append(daycount)
        #yviews.append(y_pred1)
        #daycount+=1
        totalviews+=y_pred1
    print("Total views till prediction date = ",totalviews)
    print("\n------------------------------------------------------------")
    print("\n------------------------------------------------------------")
    print("\n------------------------------------------------------------")
    
    #print(xday)
    #print(yviews)
    
    
    """plt.scatter(xday,yviews, color = 'red')        
    #plt.plot(X, regressor.predict(X), color = 'blue')   #For line(PREDICTED)
    plt.title('YOUTUBE API VIEWS/DAY')
    plt.xlabel('Dates')
    plt.ylabel('Views/day')
    plt.show()
    
    #Visualising the train set result
    plt.scatter(X,Y, color = 'red')        
    plt.plot(X, regressor.predict(X), color = 'blue')   #For line(PREDICTED)
    plt.title('YOUTUBE API VIEWS/DAY')
    plt.xlabel('Dates')
    plt.ylabel('Views/day')
    plt.show()
    """
    """
    # Visualising the SVR results (for higher resolution and smoother curve)
    X_grid = np.arange(min(X1), max(X1), 0.01) # choice of 0.01 instead of 0.1 step because the data is feature scaled
    X_grid = X_grid.reshape((len(X_grid), 1))
    plt.scatter(X1, Y1, color = 'red')
    plt.plot(X_grid, regressor.predict(X_grid), color = 'blue')
    plt.title('ICE-CREAM BRAND')
    plt.xlabel('Dates')
    plt.ylabel('Views/day')
    plt.show()
    """
#food_fun()