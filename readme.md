Screen Printing Quote Generator
===================

Python application that will store Customer information and generate quotes with multiple input parameters to tweak pricing. 

### Setup

All you need to install is pandas in order for the program to work.

```bash
pip install pandas
```

#### Generation

The easiest option is to clone the repository and open in PyCharm.  There is a shared run configuration that will execute the flow for you.

All you need to do is run the main file. 

```bash
main.py
```
After running, the user inputted information is saved as a Dataframe and a text file is generated
with the full customer and quote information. Also included are grand totals and profit margin after outsourcing.

#### Input parameters
The first window that is displayed is the Customer Information. The only two required
inputs are the <code>Customer Name</code> and <code>Name for DataFrame</code>.

The second window that is displayed is where each quote is entered.
Here you can enter as many quotes as you want. The input formatting required is prefilled
and resets after each submit. Once finished inputting each quote, click <code>Exit</code> to finish.

