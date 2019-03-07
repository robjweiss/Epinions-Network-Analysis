# Epinions-Network-Analysis
A graph theory application that looks at trust among reviewers on Epinions.com

## Data
| epinions_small.csv  |
|:-------------------:|
| 0, 1, -1            |
| 5, 20, 1            |
| 5, 50, 1            |
| ...                 |

* The data is in a CSV format and comes from Epinions.com
* This data represents relationships between reviewers and wether they trust or distrust one another
* The first two numbers represent nodes in the network (reviewers)
* The final number represents the edge connecting these nodes
* A final value of `1` indicates trust and a value of `-1` indicates distrust

## Results
![Alt text](/output/output.png?raw=true "Analysis Results")

* Triangles in the above output represents the number of triads in the network, that is relationships among 3 reviewers
* There are three types of triads that appear in this network:

| Type  | Relationship                  |
|:-----:|:-----------------------------:|
| TTT   | Trust - Trust - Trust         |
| TTD   | Trust - Trust - Distrust      |
| TDD   | Trust - Distrust - Distrust   | 
| DDD   | Distrust - Distrust - Distrust|

## Analysis
The expected and actual distirubtions of triad types differ a bit. The main cause of this can likely be attributed to the fact that the expected distribution assumes that trust and distrust are randomly distributed among reviewers. In reality it is possible that a certain reviewer consistently writes distrustful reviews. It is also likely that reviewers communicate in reality, as a result they could develop biases toward one another.

## Requirements
* [NetworkX 2.2](https://networkx.github.io/)