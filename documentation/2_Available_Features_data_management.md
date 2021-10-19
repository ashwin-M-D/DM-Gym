# DM-Gym: Available Features - Data Management

The package has a lot of features which include but not limited to creation of environments. Some of the data management features are explained below.

## Sample / Synthetic Datasets generation

This feature can be used to randomly generate datasets for the different environments in this package. It is done as follows.

#### Clustering Datasets

First create an object of the class and set parameters.

```python
from dm_gym.utils.data_gen import *

### For Clustering type dataset
datagen = data_gen_clustering()
datagen.param_init(n=<num_features>, k=<num_clusters>, num_records=<num_records>,
                   parameter_means=[], parameter_sd=[])
```

The param_init() function returns error, error_code, parameter_means and parameter_sd. This is for debug processes. If there are no errors, the error code is 0 and error is an empty string.

The parameters are explained below:

1. n: the number of features required in the dataset. //required

2. k: the number of clusters you want in the dataset. //required

3. num_records: the number of records required in the dataset //required

4. parameter_means: the mean of the features for each cluster //optional
   This is basically a 2d-array. Randomly selected of not specified.

5. parameter_sd: the standard deviation of the features for each cluster //optional
   This is basically a 2d-array. Defaults to all 1 if not specified

   ```python
   ### Example of parameters
   n = 5 ## Five features
   k = 3 ## Three clusters
   
   parameter_means = [[ftr-1-means], [ftr-2-means], [ftr-3-means],
                      [ftr-4-means], [ftr-5-means]] ## is n x k matrix
   
   parameter_means = [[1,5,9], [1,6,4], [1,7,3], [2,2,2], [7,8,9]]
   ## So the centroids would equate to (1,1,1,2,7) (5,6,7,2,8) (9,4,3,2,9)
   
   parameter_sd = [[ftr-1-std], [ftr-2-std], [ftr-3-std],
                      [ftr-4-std], [ftr-5-std]] ## is n x k matrix 
   
   parameter_sd = [[1,1,1], [1,1,1], [1,1,1], [1,1,1], [1,1,1]] 
   ## This is the default value for parameter_sd given n=5 and k=3
   ```


After the parameters are specified, the data can be generated as follows:

```python
### Generate data
data = datagen.gen_data()
```

The output is a pandas dataframe which tries to be as close to the specifications as possible.

#### Classification datasets

First create an object of the class and set parameters similar to clustering.

```python
from dm_gym.utils.data_gen import *

### For Classification type dataset
datagen = data_gen_clustering()
datagen.param_init(n=<num_features>, k=<num_classes>, num_records=<num_records>,
                   parameter_means=[], parameter_sd=[])
```

The param_init() function returns error, error_code, parameter_means and parameter_sd. This is for debug processes. If there are no errors, the error code is 0 and error is an empty string.

The parameters are explained below:

1. n: the number of features required in the dataset. //required

2. k: the number of classes you want in the dataset. //required

3. num_records: the number of records required in the dataset //required

4. parameter_means: the mean of the features for each class //optional
   This is basically a 2d-array. Randomly selected of not specified.

5. parameter_sd: the standard deviation of the features for each class //optional
   This is basically a 2d-array. Defaults to all 1 if not specified

   ```python
   ### Example of parameters
   n = 5 ## Five features
   k = 3 ## Three classes
   
   parameter_means = [[ftr-1-means], [ftr-2-means], [ftr-3-means],
                      [ftr-4-means], [ftr-5-means]] ## is n x k matrix
   
   parameter_means = [[1,5,9], [1,6,4], [1,7,3], [2,2,2], [7,8,9]]
   ## So the centroids would equate to (1,1,1,2,7) (5,6,7,2,8) (9,4,3,2,9)
   
   parameter_sd = [[ftr-1-std], [ftr-2-std], [ftr-3-std],
                      [ftr-4-std], [ftr-5-std]] ## is n x k matrix 
   
   parameter_sd = [[1,1,1], [1,1,1], [1,1,1], [1,1,1], [1,1,1]] 
   ## This is the default value for parameter_sd given n=5 and k=3
   ```

After the parameters are specified, the data can be generated as follows:

```python
### Generate data
data, target = datagen.gen_data()
```

The output is a pandas dataframe which contains the features and the target is a list which contains the labels for the classifier in the order of the data itself.

## Baseline Algorithms for testing

Certain baseline algorithms are also integrated into the package so that you can quickly compare the performance of your RL model with classical data mining techniques.

#### For Clustering

To generate the model, run the following:

```python
## Mean Shift Algorithm (Scikit-learn)
final_data, centroids = datagen.gen_model(data=data)

## K-Means Clustering Algorithm (Scikit-learn)
final_data, centroids = datagen.gen_model_Kmeans(data=data,k=k)
### if you generated the data using datagen, then you need not specify k. Otherwies, the value of k is required.
### If k is not specified, it defaults to 2.
```

The parameters are self explanatory.

The Outputs are as follows:

1. final_data: is a dataset which contains the original data along with an additional column called "Class" which contains a label stating which cluster it belongs to.
2. centroids: is a 2d python list which contains tuples of the centroids of the clusters. The order is the same as the label itself. 

The labels start from 0 to k-1 both inclusive in the case of k means. In case of mean shift algorithm, it is possible that it may identify more or less clusters than the value of k.

#### For Classification

To generate the model, run the following:

```python
## Logistic regression (Scikit-learn)
final_data, training_accuracy, classifier = datagen.gen_model(data=data, target=target)
```

The parameters are self explanatory.

The Outputs are as follows:

1. final_data: is a dataset which contains the original data along with a column called "target" which contains the target values and an additional column called "prediction" which contains a label stating which class it was predicted to be in.
2. training_accuracy: is a value between 0 and 1 which tells us the accuracy of the trained model on the training dataset
3. classifier: This is the sklearn logistic regression classifier returned after being fitted with the data. This can be used for further exploration if required.