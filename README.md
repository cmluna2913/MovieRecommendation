# Movie Recommendation
![Generic Movie App](./Images/movie.jpg)

I am taking a shot at building a movie recommendation system. I will be tackling
this as though I am building a movie recommendation system for an application.
The idea will be that this application recommends movies based on collaborative-filtering.
It will work towards recommending a user movies and streaming platform based on
ratings they have given to previous movies.

# The Data
The data comes from the movielens data <a href='https://grouplens.org/datasets/movielens/'>
    *here*
</a>. I am using the smaller dataset
consisting of about 100,000 ratings with 600 users. The including information
will be user ID, movie ID, tags, genres, and some timestamps. We will make a 
train set and a data set to build our model and then see how it does with information
it hasn't seen before.

# Approach
The surprise package for python is very useful for building recommendation systems.
We will run a variety of models:
1. Basic models in the surprise package
2. k-NN inspired models
3. Matrix Factorization models

<img src="Images/collabfilt.png" alt="Collaborative Filtering" width="200"/>

This model will be a collaborative-filtering based model. It will make recommendations
based on other user data.

# Current Conclusion
After running several models and judging based on RMSE, SVD++ is our current
best model. While SVD makes predictions based on other user ratings, SVD++ takes
this a step further by also taking into account which movies users have submitted
a rating to, regardless of the rating. After splitting our data between a train
and test set, we get an RMSE of .4911. Our movie recommender does a well enough
job in predicting which movies users will most likely enjoy.

### Quick Example
Let's take my household cat, Monkey, and have her rate a few of the movies in our
database. Taking a peek at few of the movies she enjoys, we get:
* Seven
* Usual Suspects
* Taxi Driver
* Before Sunrise
* Natural Born Killer

Taking a quick peek shows us that, for the most part, Monkey loves her crime, thriller,
and drama movies. We'll take all her ratings and generate a list of movies in an order
of movies she'd like the most to movies she'd like the list. Again, taking a look
at some of the movies she'd most likely enjoy, we get:
* Wild Tales
* Singin' in the Rain
* Lawrence of Arabia
* Rosemary's Baby
* The Hustler

After this quick peek, we see that these movies do include some of the genres
Monkey loves: crime, drama, and thriller. However, we do get some comedy and
romance thrown in, most likely influenced from the other movies Monkey decided
to rate.

# Next Steps
Since our system is recommending movies to users, I would love to be able to
give them feedback as to which streaming platform they can find their movie of
choice. I will most likely have to webscrape this information to provide the
necessary labels for each movie. 

My next approach will be to create a new column
of tags that a user gave for each movie. I will then encode this information
and the genres in order to create a new model that also compares users based on
genres they enjoy and tags they make.

I want to be able to enhance user experiences by giving them a customized
search experience. My plan is to help them narrow down movie choices by genre, years, 
streaming platform, and more.

Once all the above is said and done, I will incorporate this into the large dataset
consisting of over 27 million ratings, 58 thousand movies, and 280 thousand users.