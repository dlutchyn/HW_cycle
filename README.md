<h1>Best Financial Portfolio Creator</h1>

<h2> About the project</h2>
This project is created for those people who want to generate a passive income
or invest their money into world currencies, corporations and stocks. Based on your preferaces and 
collected/analyzed data, Financial Portfolio Creator generates you a most reliable and profitable 
collection of stocks for you to invest in. Using this program, you will get a stable yearly income.

## Wiki content

1. [Опис проблеми](https://github.com/dlutchyn/HW_cycle/wiki/%D0%9E%D0%BF%D0%B8%D1%81-%D0%BF%D1%80%D0%BE%D0%B1%D0%BB%D0%B5%D0%BC%D0%B8)
2. [Web blog analysis](https://github.com/dlutchyn/HW_cycle/wiki/Web-blog-analysis-(%D1%80%D0%B5%D1%84%D0%B5%D1%80%D0%B0%D1%82%D0%B8)
3. [ДЗ-2](https://github.com/dlutchyn/HW_cycle/wiki/%D0%94%D0%B7---2)
4. [ДЗ-3](https://github.com/dlutchyn/HW_cycle/wiki/%D0%94%D0%B7---3)
5. [ДЗ-4]()
6. [ДЗ-5](https://github.com/dlutchyn/HW_cycle/wiki/%D0%94%D0%B7---5)

## Table of content

1. [Instalation and requirements](#instalation-and-requirements)
2. [Program exploitation](#program-exploitation)
3. [Input and Output data](#input-and-output-data)
4. [Project Structure](#project-structure)

## Instalation and requirements

<h3> - Download the project</h3>
You can clone this project from repository executing this command for your local git repository

```python 
$ git clone https://github.com/dlutchyn/HW_cycle
```
or you can manually download the Zip of this project to your pc.

<h3> - Installing requirements</h3>
One way to install requirements for this project is to get them from requirements.txt
You need to execute this command in Terminal (you need to execute it from the root directory of the project):

```python
pip install -r requirements.txt
```
Another way to install all requirements is to execute the following command:

```python 
pip install pandas, matplotlib, flask, yfinance, numpy
```
<h3> - Run the program</h3>
Write:

```python
python flask_app.py
```

## Program exploitation
<h3> - Welcome page</h3>

![](/static/images/welcome.png)

Start creating your financial portfolio

<h3> - Creating portfolio</h3>

![](/static/images/stock.png)

- Select stocks you would like to invest in
- After that type in the number of stocks you are ready to invest (the size of your portfolio)
- Type in the number of days you want the analysis to be held on 
(the more, the more accurate the analysis will be)
- Submit

<h3> - Results</h3>

![](/static/images/result.png)

View your results

## Input and Output data
The input data is the number of stocks you are willing to invest in (the size of your financial portfolio)
and the numer of days you want to have an analysis for (the more days, the more accurate the analysis will be)
You also check the boxex of the preferable stocks for investing.

## Project Structure
<h3>Modules</h3>

* getter_data.py - module that gets stock data from the csv files 
* processor.py - module that processes all information about stocks from yfinance and analyzes it
* stock_plotting.py - module that plots graphics with analyzed information

<h3>Structures</h3>

* arrays.py - module with implemented Array ADT
* stock_adt.py - module with implemented Stock ADT
* stock_analyzer.py - module with implemented StockAnalyzer ADT

<h3>External Libraries</h3>

* yfinance
* numpy
* pandas
* flask
* matplotlib


