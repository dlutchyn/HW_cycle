<h1>Best Financial Portfolio Creator</h1>

<h2> About the project</h2>
This project is created for those people who want to generate a passive income
or invest their money into world currencies, corporations and stocks. Based on your preferaces and 
collected/analyzed data, Financial Portfolio Creator generates you a most reliable and profitable 
collection of stocks for you to invest in. Using this program, you will get a stable yearly income.

<h2>Table of content</h2>
[Go to Input and Output data section](#input-and-output-data)

<h2>Instalation and requirements</h2>

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

<h2>Program exploitation</h2>
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

<h2># Input and Output data</h2>
The input data is the number of stocks you are willing to invest in (the size of your financial portfolio)
and the numer of days you want to have an analysis for (the more days, the more accurate the analysis will be)
You also check the boxex of the preferable stocks for investing.

<h2>Project Structure</h2>
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


