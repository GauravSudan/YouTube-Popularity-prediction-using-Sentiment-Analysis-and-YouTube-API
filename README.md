CLASSIFY AND PREDICT VIDEO POPULARITY      
ON YOUTUBE
									-By Gaurav Sudan


1.	ABSTRACT
Classifying the category of any online content and predicting its popularity is an important task for a wide range of systems, from advertising to recommendation systems or making profit and earn money from online content. We here present a system for categorising a video into three broad categories namely ‘Health and Fitness’, ‘Travel and Education’ and ‘Personality Development’, and then we predict the future popularity of video using regression method based on views from the past. We prove the results of our system against a dataset containing views of 1500 videos on YouTube with a mean error of 0.8.

2.	INTRODUCTION
Having a look at their contents, you could probably categorise a video into a particular category in a few seconds that this video or channel on YouTube is about video games, Soccer, Health or News. But how to determine this algorithmically? And how to do this at a large scale of data? These are in short the challenges this system tackles. YouTube is placing the concept of channel at the core of its strategy to develop content and audience. A channel can be viewed as a living set of videos which share a common property: they are from the same person or organization, they are about the same topic, they are related to the same event, etc. A channel has a live feed of events, in which videos may be published, and users may subscribe to them. Channels are engaging creators and curators, by gathering an audience for them. Channels are engaging users, by recommending them videos about things they like. With channels playing such a central role, categorising videos into different categories and predicting content popularity is of great importance to support and drive the design and management of various services. For example, in online marketing, the information about the expected future popularity of a certain type of content can be useful for planning advertising campaigns and estimating costs. Accurately predicting content popularity is also key to support effective information services. Popularity prediction can help identifying possible bottlenecks due to poor recommendation and search engines and improving the quality of such services by extending current result ranking strategies to take the estimated future popularity.

Our challenge in building an accurate data classifier and popularity predictor is the lack of manually labelled training data, which can be prohibitively expensive to collect. Our system uses keyword matching technique to classify the videos into their respective categories and then use regression method to predict the future popularity. Our system is tested on a dataset consisting of videos of around 1500 videos of more than 150 channels worldwide. The channels were selected based on their average daily views (Categorised as daily views less than 2000, daily views less than 5000 and so on) over a period of one year (2nd September 2016 to 1st September 2017). The experimental method generated results with a relative mean percentage error of 0.8%.

3.	LITERATURE REVIEW

•	Keyword Matching

To classify the video, our system breaks the title of keyword into various keywords. For example, a video titled “How to lose weight in 30 days”, will be broken into set of separate keywords like “How” , ” to” , ”lose” , ”weight” , ”in” ,  “30” , “days”. Then our system will ignore the connecting words like “to”, “in”. Then it will also ignore the numeric word i.e. “30” and word like “days”.

Thus the remaining keywords would be just “lose” and “weight”. Then our system will match these words with its own database, and the category to which it will belong would be known to us.

•	Predicting future popularity of video

In order to predict the future popularity, our system will ask the user to specify the number of average daily views that the user’s channel receives. The various daily view categories covered by our system are less than 2000, less than 5000, less than 10000, less than 20000 and less than 50000. Then after selecting the appropriate category, the user is asked to enter “Date of video released” and “Prediction date”. The Prediction date is the date upto which, the user wants to know the number of views his/her video would achieve. Then using the regression model on the training dataset belonging to time period 2nd September 2016 to 1st September 2017, our system can predict the views achieved by the system video in future upto a relative mean percentage error of 0.8%.

Working Algorithm of the system 
Step 1.  Enter video title.
Step 2.  Enter release date.
Step 3.  Enter prediction date.
Step 4.  End

#Example 1
Title : “How to lose weight in 30 days”
Release Date = 2/12/2016
Prediction Date = 2/3/2017




Results:
The following video “How to lose weight in 30 days” belongs to Health and Fitness blog.
Total Views from 2/12/2016 to 2/3/2017 = 2,53,648

 
		    Fig. Views between Released and Predictive date

 

4.	OVERVIEW DIAGRAM


 


Phase 1
In phase 1, the user enters the title of his/her video.

Phase 2
In phase 2, the system breaks the title into keywords. If the match is found, the system identifies the category of the video and moves to phase 3, else the system calls the “EXPAND_DATABASE” function so as to update its database for any future reference.


Phase 3
In phase 3, the system ask user to enter the “Release Date” and “Prediction Date” of the video.

Phase 4
In phase 4, the system predicts the number of views that the video might achieve in future.



5.	IMPLEMENTATION

This system will work for all users who have a video with a proper title that the user is willing to publish on online platforms like YouTube. This system would help them to know the approximate views that the video might achieve in the near future.

5.1   Collecting the Title of the video

There are two ways in which our system can collect the Title of the video:

1.	Directly from YouTube

In this case, it is assumed that the user has an active YouTube channel. If so, the user must have a YouTube API key, that would allow our system to extract all the details required by our system from the YouTube.
	     
	     The User need to enter the title of the video and his API key as

“—serach=”SOME_RANDOM_VIDEO_TITLE” –key=”YOUTUBE API KEY” 

through command line. For example:

“--search="Kwality Walls Ice Cream Sandwich Chocolate and Vanilla " --key=AIzaSyBxfwXiIAh3iLAzfK6eRcxisKcQEHLrsW0”

After this, the system retrieves the title, channel name and all the related information that will be required further in the program.


2.	Entering the title manually

In this method, the user can enter the title of video manually without the need of YouTube API. With the help of this method, the user can know the popularity of any video that might be in planning stage, just by entering the title of video. This feature of system aims to help those users also that may or may not have an active YouTube channel or those who are planning to make a video and have a rough idea in their mind about what the title of video might be.

#ALGO 2:
Step 1.     Retrieve video’s title from the user.
	Step 2.     Pass the video’s title to the keyword_matching method.
	Step 3.     End.



5.2   Retrieving the keywords from the title of video

This method is used to retrieve the keywords from the title of the video.  After Phase 1, the video title retrieved will be appended in a list and will be broken into separate words. 

#ALGO 3
	Step 1.	   Append the Title of video to an empty dictionary.
	Step 2.	   Repeat step 3 till count less than length of video’s title.
	Step 3.    If character is not equal to blank space (“  “), then
			Set word equal to word + character.
		    Else, append word to keyword_list
	Step 4.    End of step 2 and 3.

For example, a video titled “How to lose weight in 30 days”, will be broken into set of separate keywords like “How” , ” to” , ”lose” , ”weight” , ”in” ,  “30” , “days”. But in this case there are several words like “to” , ”in” , “days” etc. that cannot be used as keywords. This is because these type of words are called connectors that are used to connect words together and furthermore they are not unique, thus are method will ignore all those words and will consider only unique words like “lose” and “weight” as keywords to identify the category of the video.




#ALGO 4
Step 1.  Repeat step 2 till count less than length of title.
Step 2.  If keyword is not equal to ‘and’ & keyword is not equal to ‘or’ ……..& keyword is not equal to ‘day’, then append keyword to keyword_database.
Step 3.  End of step 1 and 2.

5.3	Expanding Database

Let us suppose the user entered a title that does not match our database.  For this purpose, our system has a self-learning feature by which it will automatically update its database so as to easily categorise the video in future.
	


#ALGO 5

Step 1.  If Match_Count is equal to 0, then display “NO CATEGORY FOUND")
Step 2.  If user wants to expand database, then call Expand_Database method.
Step 3.  Call the view_prediction method after step 2.
Step 4.   End.






Expand_Database method.


Step 1.  Open Keyword_Database in append mode.
Step 2.  If keyword is not equal to ‘and’ & keyword is not equal to ‘or’ ……..& keyword is not equal to ‘day’, then append keyword to Keyword_Database.
Step 3.  Display “DATABASE UPDATED SUCCUSSFULLY”
Step 4.  End.
 


5.4	  Getting Dates from the user

This method is used to retrieve “Release date” and “Predicting date”.  Release date is a date on which the user has released his video on YouTube. Predicting date is the date till which the user wants to know how much popularity his video would gain. By calculating the number of days between the two dates and by applying regression model on the calculated number of days, our system will predict how much popularity the video would gain provided the user has selected the correct “daily average views” category. 

#ALGO 6
	
	Step 1.  Retrieve release_date and prediction_date from the user.
	Step 2.  Set day1 equals release_date - initial_date.
	Step 3.  Set day2 equals prediction_date - initial_date.
	Step 4.  If day1 is greater than 360, 
then set temp = int(day1/360) and set day1=day1-temp*366
	Step 5.  If day2 is greater than 360, 
                                    then set temp = int(day2/360) and set day2=day2-temp*366
	Step 6.  End. 

6.	DATASET


In order to train our model, we collected the data of YouTube channels under several categories. These categories were based on average daily total number of views and were categorized as average views less than 2000, average views less than 5000 and so on.

The data for channels was collected for one year from 2nd Sept. 2016 to 1st Sept. 2017. The model was trained on data set of one channel of each category and was tested on 10 channels of each category. Further the model was also tested on similar data of 450 channels. 



7.	POPULARITY PREDICTION MODELS

The dataset of 450 random channels was tested on different regression models, and the results were as follows:

7.1 Linear Regression Model

Linear regression attempts to model the relationship between two variables by fitting a linear equation to observed data. One variable is considered to be an explanatory variable, and the other is considered to be a dependent variable. A linear regression line has an equation of the form 
Y = a + bX
where X is the explanatory variable and Y is the dependent variable. The slope of the line is b, and a is the intercept (the value of Y when X = 0). The values of a and b can be calculated as

			 

		 
				Fig. Linear Regression Model

The Linear Regression Model was trained using a dataset of any random channel out of the database that falls under a particular category and was tested on dataset of other channels of the same category. The results obtained were as follows:

#ALGO 11
Step 1. Import LinearRegression method from sklearn. .linear_model library.               
Step 2. Set regressor = LinearRegression().
Step 3. Call fit method and pass Date and Daily_Views as arguments.
Step 4. End.
    

		 
			Fig. Linear Regression Model Results

The Linear Regression model gave an accuracy of 10% with variation of about 29%.

7.2	Support Vector Regression Model

 The Support Vector Regression (SVR) uses the same principles as the SVM for classification, with only a few minor differences. First of all, because output is a real number it becomes very difficult to predict the information at hand, which has infinite possibilities. In the case of regression, a margin of tolerance (epsilon) is set in approximation to the SVM which would have already requested from the problem. But besides this fact, there is also a more complicated reason, the algorithm is more complicated therefore to be taken in consideration. However, the main idea is always the same: to minimize error, individualizing the hyperplane which maximizes the margin, keeping in mind that part of the error is tolerated. 
 

 














Non Linear SVR
	 



The Non-Linear SVR Model was trained using a dataset of any random channel out of the database that falls under a particular category and was tested on dataset of other channels of the same category. The results obtained were as follows:

#ALGO 12

Step 1. Import SVR method from sklearn.svm library.               
Step 2. Set regressor = SVR(kernel = 'rbf').
Step 3. Call fit method and pass Date and Daily_Views as arguments.
Step 4. End.


     
	Fig. SVR Model Results

The Linear Regression model gave an accuracy of 65% with variation of about 8%.




7.3	  Decision Tree Model

Decision tree builds regression or classification models in the form of a tree structure. It breaks down a dataset into smaller and smaller subsets while at the same time an associated decision tree is incrementally developed. The final result is a tree with decision nodes and leaf nodes. A decision node (e.g., Outlook) has two or more branches (e.g., Sunny, Overcast and Rainy), each representing values for the attribute tested. Leaf node (e.g., Hours Played) represents a decision on the numerical target. The topmost decision node in a tree which corresponds to the best predictor called root node. Decision trees can handle both categorical and numerical data.
	 
Fig. Example of D.T.

The Decision Tree Model was trained using a dataset of any random channel out of the database that falls under a particular category and was tested on dataset of other channels of the same category. The results obtained were as follows:


#ALGO 13

Step 1. Import DecisionTreeRegressor method from sklearn.tree library.               
Step 2. Set regressor = DecisionTreeRegressor(random_state = 0)
Step 3. Call fit method and pass Date and Daily_Views as arguments.
Step 4. End
 
	Fig. D.T. Model Results
The Decision Tree model gave an accuracy of 97% with variation of about 3%.

7.4	Models at a glance


MODEL	ACCURACY( in %)	VARIATION (in %)
LINEAR REGRESSION	10	29
SVR	65	8
DECISION TREE	97	3

Thus because of best accuracy and least variation, we chose Decision Tree Model for our system.




8.	  Proposed methodology for predicting popularity

After the user has correctly entered all the required details, our system will categorize the video under which category it falls and by using Decision tree prediction model, the system will predict the number of use the video will achieve in future. 






#ALGO 7

Step 1. Import DecisionTreeRegressor method from sklearn.tree library.               
Step 2. Set regressor = DecisionTreeRegressor(random_state = 0)
Step 3. Call fit method and pass Date and Daily_Views as arguments.
Step 4. Set total_views=0
Step 5. Repeat steps 6 and 7 till count is in range of day1 and day2.
Step 6. Set Predicted_value = sc_y.inverse_transform
(regressor.predict(sc_X.transform(np.array([[i]]))))
       	Step 7. Set total_views= total_views + Predicted_value
	Step 8. End of step 5.
	Step 9. Print total_views.
	Step 10. End.

8.1   Predicting popularity for videos related to Health and       Fitness
This method is used to predict the popularity of the videos that are related to health and fitness blogs. 

#ALGO 8

Step 1. Import DecisionTreeRegressor method from sklearn.tree library.               
Step 2. Set regressor = DecisionTreeRegressor(random_state = 0)
Step 3. Call fit method and pass Date and Daily_Views as arguments.
Step 4. End.
 
 






8.2  Predicting popularity for videos related to Travel blog

This method is used to predict the popularity of the videos that are related to travel blogs. 
 
#ALGO 9
Step 1. Import DecisionTreeRegressor method from sklearn.tree library.               
Step 2. Set regressor = DecisionTreeRegressor(random_state = 0)
Step 3. Call fit method and pass Date and Daily_Views as arguments.
Step 4. End.
 



8.3 Predicting popularity for videos related to Education and Personality Development

This method is used to predict the popularity of the videos that are related to Education and Personality Development blogs.  

#ALGO 10
Step 1. Import DecisionTreeRegressor method from sklearn.tree library.               
Step 2. Set regressor = DecisionTreeRegressor(random_state = 0)
Step 3. Call fit method and pass Date and Daily_Views as arguments.
Step 4. End.


. 







9.	PERFORMANCE ANALYSIS

To measure the accuracy of the number of views calculated by our system in future, we tested our model on different datasets, and the relative mean error was calculated to evaluate our model as:		
	 
	Where Av is the actual views from 2nd Sept. 2016 to 1st Sept. 2017
	            Cv is the views calculated by our system.

This related error was calculated to be 0.8% by our system. 

10.	 CONCLUSION AND FUTURE WORK

With the help of our system, we can predict the number of views that any online video would achieve in future. This can be utilised for a wide range of systems, from advertising to recommendation systems or making profit and earn money from online content or to simply inspire new talents to make more and more videos to show their talent to the outer world

As we know that no system is perfect, and so not our system is. Our system uses only keyword matching technique for categorising our video, thus it may sometimes misjudge wrong keyword into wrong category. To improve this, we can add object recognition from an image or video to effectively identify objects in our model and easily and effectively categorise the video.










11.	 REFERRENCES

      10.1   Classifying YouTube Channels: a Practical System
[Vincent Simonet Google, Paris (France)]

11.1	Improving Video Classification via YouTube Video Co-Watch Data 

[John R. Zhang ( Dept. Computer Science ,Columbia University),John R. Zhang(Dept. Computer Science Columbia University New York, USA),Yang Song(Google, Inc.)

      10.3    Using Early View Patterns to Predict the Popularity of YouTube Videos

(Henrique Pinto, Jussara M. Almeida, Marcos A. Gonçalves,Computer Science Department Universidade Federal de Minas Gerais, Brazil)

