from builder.builder import builder

front_prices = 'qcsp_prices/Front_Print.csv'
addl_prices = 'qcsp_prices/addl_print.csv'
qcsp_template = 'qcsp_prices/blank_template.xlsx'

if __name__ == '__main__':
    builder(front_price=front_prices, addl_price=addl_prices, blank_template = qcsp_template)