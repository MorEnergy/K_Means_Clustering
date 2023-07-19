# K_Means_Clustering

This repository contains an example of implementing the K-means clustering algorithm in Python using scikit-learn. The code demonstrates how to cluster data points and visualise the clustering results.

## Table of Contents
- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Requirements](#Requirements)
- [Contributing](#contributing)
- [License](#license)

## Description
In this example, we generate a sample dataset using scikit-learn. We then preprocess the data as necessary. Next, we use the silhouette score to determine the optimal number of clusters. The silhouette score measures the compactness of clusters and the separation between different clusters, with higher scores indicating better clustering.

We iterate over different values of k (number of clusters) and calculate the silhouette score for each clustering solution. We select the number of clusters with the highest silhouette score as the optimal number of clusters.

After determining the optimal number of clusters, we create a K-means clustering object with the selected number of clusters and fit the model to the data. We obtain the cluster labels and centroids. We then visualise the clustering results by plotting the data points colored according to their assigned clusters, with centroids indicated by red crosses.

Finally, we evaluate the clustering results using the silhouette score and print the optimal number of clusters and the calculated silhouette score.

## Installation

1. Clone the repository:

        git clone https://github.com/MorEnergy/K_Means_Clustering.git

2. Install the required packages by running:

        pip install -r requirements.txt

## Usage

1. Run the 'K_Means_Clustering.py' script:

        python k_means_clustering.py
   
The script will generate sample data, preprocess it, determine the optimal number of clusters, perform the clustering, and display the results.

2. Adjust the parameters and customise the code as needed for your own dataset.

## Requirements

The code is implemented in Python 3 and requires the following packages:

- numpy
- matplotlib
- scikit-learn
  
For the detailed list of dependencies, refer to the requirements.txt file.

## Contributing
Contributions are welcome! If you have any suggestions, enhancements, or bug fixes, please open an issue or submit a pull request.

## License
This project is licensed under the [MIT License](LICENSE).
