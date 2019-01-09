import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from date import date_fun


def healthfitness_fun():
    X=[]    #X=dates
    Y=[]    #Y=views
    def get_data(filename):
        with open(filename,'r') as csvfile:
            csvFileReader = csv.reader(csvfile)
            next(csvFileReader)                     #to skip 1st row ie header row
            for row in csvFileReader:                   #for iteration of each rows
            #X.append(int(row[0].replace("-","")))
            #X.append(int(row[0].split('-')[0]))
                X.append(int(row[1]))
                if(c==1):
                    Y.append(float(row[2]))
                if(c==2):
                    Y.append(float(row[3]))
                if(c==3):
                    Y.append(float(row[4]))
                if(c==4):
                    Y.append(float(row[5]))
                if(c==5):
                    Y.append(float(row[6]))
                if(c==6):
                    Y.append(float(row[7]))
                if(c==7):
                    Y.append(float(row[8]))
        return 
    c=0
    print("ENTER AVERAGE DAILY VIEWS")
    print("\n1.DAILY VIEWS LESS THAN 1,000")
    print("\n2.DAILY VIEWS LESS THAN 2,000")
    print("\n3.DAILY VIEWS LESS THAN 5,000")
    print("\n4.DAILY VIEWS LESS THAN 10,000")
    print("\n5.DAILY VIEWS LESS THAN 20,000")
    print("\n6.DAILY VIEWS LESS THAN 50,000")
    print("\n7.DAILY VIEWS LESS THAN 1,00,000")
    c=int(input("ENTER YOUR CHOICE:"))
    get_data('healthfitness.csv')
    

    from sklearn.cross_validation import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.25)

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
    
    
    from sklearn.tree import DecisionTreeRegressor                
    regressor = DecisionTreeRegressor(random_state = 0)
    regressor.fit(X1, Y1)
    
    
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
    for i in range(day1,day2+1):
        y_pred1 = sc_y.inverse_transform(regressor.predict(sc_X.transform(np.array([[i]]))))
        totalviews+=y_pred1
    totalviews=totalviews*1.85
    print("Total views till prediction date = ",totalviews)
    print("Total earning till prediction date = ",(totalviews/1000)*7.6)
    print("\n------------------------------------------------------------")
    
    
    
    """#Visualising the train set result
    plt.scatter(X,Y, color = 'red')        
    plt.plot(X, regressor.predict(X), color = 'blue')   #For line(PREDICTED)
    plt.title('YOUTUBE API VIEWS/DAY')
    plt.xlabel('Dates')
    plt.ylabel('Views/day')
    plt.show()
    """
    
    # Visualising the SVR results (for higher resolution and smoother curve)
    """
    X_grid = np.arange(min(X1), max(X1), 0.01) # choice of 0.01 instead of 0.1 step because the data is feature scaled
    X_grid = X_grid.reshape((len(X_grid), 1))
    plt.scatter(X1, Y1, color = 'red')
    plt.plot(X_grid, regressor.predict(X_grid), color = 'blue')
    plt.title('HEALTH AND FITNESS')
    plt.xlabel('Dates')
    plt.ylabel('Views/day')
    plt.show()
    
healthfitness_fun()
    """