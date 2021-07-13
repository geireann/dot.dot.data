# Data Deliverable Report - dot dot data
**Team members**: Dhiraj, Khosrow, Amin, Jimmy and Geireann

## Table of Contents
  - [Step 1](#step-1)
  - [Step 2](#step-2)
  - [Step 3](#step-3)
  - [Step 4](#step-4)
  - [Step 5](#step-5)
    - [Who are the major stakeholders of your project?](#who-are-the-major-stakeholders-of-your-project)
    - [How could an individual or particular community's privacy be affected by the aggregation or analysis of your data?](#how-could-an-individual-or-particular-communitys-privacy-be-affected-by-the-aggregation-or-analysis-of-your-data)
    - [What ethical problems could you see arising in the course of the project?](#what-ethical-problems-could-you-see-arising-in-the-course-of-the-project)
    - [Underlying socio-historical biases](#underlying-socio-historical-biases)
  - [Step 6](#step-6)
  - [FORM](#form)


***

## Step 1

1. Your data collection description goes here (at most around 200 words)

2. Your data commentary goes here (at most around 200 words)

***

## Step 2

Your data schema description goes here (at most around 300 words)

-**Data types/assumption of data types**<br>
We think the following attributes would matter the most:  

  **The name of he game (eg. A vs B):**<br>
    Game (PRIMARY ID) - VARCHAR  
  **The name of the white player:**<br>
    White player name (ID) - VARCHAR  
  **The name of the black player:**<br>
    Black player name (ID) - VARCHAR  
  **The ELO rating of the white player:**<br>
    White player ELO rating - INT  
  **The ELO rating of the black player:**<br>
    Black player ELO rating - INT  
  **The date of the game:**<br>
    Date (year+month+day) - INT  
  **The opening used by the white player:**<br>
    Move sequence (opening) - VARCHAR  

-**Keys/cross-references**<br>
  The primary key we will be using will be Game. We will also use Date and Move sequence when joining daa to make sure our data is unique.  

-**Required/Optional fields**<br>
  The Game, White player name, Black player name, White player ELO rating, Black player ELO rating, and Date would be required fields. The Move sequence would be optional. We would be using the data of the openings when we can to analyze the effect of it on the winning/losing of specific players.  
***

## Step 3

1. Your observation of the data prior to cleaning the data goes here (limit: 250 words)
2. Your data cleaning process and outcome goes here (at most around 250 words)

***

## Step 4

Your train-test data descriptions goes here (at most around 250 words)

***

## Step 5

### Who are the major stakeholders of your project?
The major stakeholders in our project are chess players, in particular chess players who are ranked above 2650 in the Elo system. Since we are primarly evaluating the games that have been played, in order to limit the scope of our project to something realistic we decided to set a lower boundary for chess players that we would include in our database. As a result, our project primarily handles data with regards to the chess games and which moves are played, but also additional information on the player, such as the age that they became the grandmaster, or their previous record. The major stakeholders in this project are as follows:
- **Chess players**: The players are the primary stakeholders in our dataset, they are the group that we are evaluating and therefore are most impacted by it. This group is two-fold, we are evaluating grand masters as to learn from their opening moves and to find out if it is possible to make predictions based on factors that determine the data, but this project is also useful for amatuer chess players like us, who want to learn what opening moves we can do, or how we should play in order to improve our ability when playing chess. 
- **International chess bodies**: Data availability in chess is strongly linked to how accessible the sport is to the general public. With websites such as chess.com, and lichess.com become more popular, international chess bodies are a relevant stakeholder in determining how games are decided. 
- **Websites that host chess games**: Websites such as lichess.com and chess.com have significantly contributed to the accessibility of chess and also make such an analysis possible. 
- **Chess betting sites**: Though this is not a significant stakeholder, we must be mindful of the fact that there is betting in chess, and a prediction system like ours could be used for such purposes, which we do not intent it to be used for. 

### How could an individual or particular community's privacy be affected by the aggregation or analysis of your data? 
Although this data, in particular the chess moves that are played, are [public domain](https://chess24.com/en/read/news/us-judge-agrees-with-chess24-on-chess-moves), we must recognise that the information that we are keeping on players and the moves that they play, can be used maliciously, and therefore will not use the data for those reasons. Since our data involves keeping track of how individuals are named, and the way that they play, we need to be careful about how we publish the data. Ideally, in our analysis of the players we can make the names use anonymous as to not potential be swayed by who the player is, but instead how the important variables going into the game inpact the outcome. 


### What ethical problems could you see arising in the course of the project?
Although one may think that there are relatively few ethical problems arising from the project, due to the nature of chess, but that is in fact not the case. The most significant ethical problem has to do with the gender imbalance that exists in our data, but there are also geographical boundaries for chess players, as well as some that discriminate based on age. 

- **Gender in Chess**<br>
Since we decided to only evaluate players who are ranked above 2650, this also means that we only have one female identifying member in our dataset ([Source](ratings.fide.com/top.phtml?list=women)). Although gender identity and sex do not impact chess performance, women have been historically underepresented in chess as the are fewer female chess players to begin with ([Source](https://journals.sagepub.com/doi/full/10.1177/0956797620924051)). 

- **Age & Elo Ratings**<br>
Another point that we need to consider is the ranking system that we are using: Elo. Although Elo is universally accepted, evidence has suggested that the rating understimates younger or inexperienced players and that their Elo ratings fall behind their actual performance. This understimarion is relevent to the gender comparison, as female identifying chess players are generally much younger (Mean = 21.6, Standard Deviation = 13.5) than their male counterparts (Mean = 36.8, Standard Deviation = 18.8)([Source](https://journals.sagepub.com/doi/full/10.1177/0956797620924051)). 

### Underlying socio-historical biases
Seperating our analysis for men and women would be a possible approach, but they compete against each other too often for that to be an option. Chess datasets, and games between women and men have been used in the past to arive at the conclusion that there exists a difference in ability as a result of gender. These predictions are dangerous and seriously disincentivize females to participate which further contributes to the problem. The reason for the statistical differences between genders is because of the historical discrimination of women in chess. 

Another part of our analysis has to do with how AI, and statistical analysis of chess games has in fact benefited chess players and the chess community. Historically, in order to really develop as a chess player we needed access to resources, a trainer, and the resources available to be taught how to play chess. Now, with the vast extent of historical resources available to chess players, and due to the fact that we have automated teachers that allow you to analyse games, and learn what the next best move would be, chess has become a much more accessible sport ([Source](https://towardsdatascience.com/how-22-years-of-ai-superiority-changed-chess-76eddd061cb0)).  


***

## Step 6


Your team report goes here

## FORM
Form link: https://forms.gle/sGYpbdHEhnBpo6tg7