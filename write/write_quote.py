from datetime import date
import pandas as pd
import openpyxl
from openpyxl.styles import Alignment


class write_quote:
    def __init__(self,customer_class,df_name,invoice_no, quote_app=None):
        self.customer_class = customer_class
        self.df_name = df_name
        self.invoice_no = invoice_no
        self.quote_app = quote_app

    def write_customer_info(self):
        with open('running_quotes/'+self.customer_class.name + '/' + self.df_name + '_quote', "a") as f:
            print(self.customer_class.name, '|', self.customer_class.email, '|', self.customer_class.phone, '|',
                  self.customer_class.address, file=f)
            print('-' * 30, file=f)
            print("Today's date:", date.today(), file=f)
            print('-' * 30, file=f)

    def write_quote_info(self,quote_app):
        self.quote_app = quote_app
        with open('running_quotes/'+self.customer_class.name + '/' + self.df_name + '_quote', "a") as f:
            print('-' * 30, file=f)
            print('Full Invoice Total: $', round(sum(self.quote_app.total), 2), file=f)
            print('-' * 30, file=f)
            print('Total Profit after Outsourcing: $', round(sum(self.quote_app.total_profit), 2), file=f)
            print('-' * 30, file=f)
            print('Due Date: ', self.quote_app.due_date, file=f)

    def write_dataframe(self):
        df = pd.DataFrame.from_dict(self.customer_class.running_quotes, orient='index').fillna(0)

        df.to_csv('{}/{}.csv'.format('running_quotes/'+self.customer_class.name, self.df_name))

    def write_invoice(self, quote_app, blank_template):
        self.quote_app = quote_app
        self.blank_template = blank_template
        test = pd.read_csv('{}/{}.csv'.format('running_quotes/'+self.customer_class.name, self.df_name))
        test = test.fillna('')
        xfile = openpyxl.load_workbook(blank_template)

        sheet = xfile['Invoice 2010']
        sheet['E4'] = date.today()
        sheet['E5'] = self.invoice_no
        sheet['E6'] = 'PO# ' + self.df_name
        sheet['B10'] = test.loc[0, 'customer']
        sheet['B11'] = test.loc[0, 'address']
        sheet['B12'] = test.loc[0, 'phone']
        sheet['B13'] = test.loc[0, 'email']
        sheet['B14'] = 'Due Date: ' + test.loc[0, 'due_date']

        self.location = 17
        for i in range(0, test.shape[0]):
            color_str = test.loc[i,'location_1'].astype('str')
            for location in ['location_2','location_3','location_4']:
                if test.loc[i, location] != 0:
                    color_str = color_str + '/' + test.loc[i, location].astype('str')
            sheet['B{}'.format(self.location)] = test.loc[i, 'S-XL_Q']
            sheet['C{}'.format(self.location)] = 'S-XL - ' + test.loc[i, 'shirt_style'] + ' - ' + color_str + \
                                                 ' color print ' + '(' + test.loc[i, 'description'] + ')'

            sheet['D{}'.format(self.location)] = test.loc[i, 'total_S-XL_price']
            if test.loc[i,'XXL_Q'] != 0:
                self.location += 1
                sheet['B{}'.format(self.location)] = test.loc[i, 'XXL_Q']
                sheet['C{}'.format(self.location)] = '2XL - ' + test.loc[i, 'shirt_style'] + ' - ' + color_str +\
                                                     ' color print ' + '(' + test.loc[i, 'description'] + ')'

                sheet['D{}'.format(self.location)] = test.loc[i, 'total_XXL_price']
            if test.loc[i,'XXXL_Q'] != 0:
                self.location += 1
                sheet['B{}'.format(self.location)] = test.loc[i, 'XXXL_Q']
                sheet['C{}'.format(self.location)] = '3XL - ' + test.loc[i, 'shirt_style'] + ' - ' + color_str + \
                                                     ' color print ' + '(' + test.loc[i, 'description'] + ')'

                sheet['D{}'.format(self.location)] = test.loc[i, 'total_XXXL_price']
            if test.loc[i,'XXXXL_Q'] != 0:
                self.location += 1
                sheet['B{}'.format(self.location)] = test.loc[i, 'XXXXL_Q']
                sheet['C{}'.format(self.location)] = '4XL - ' + test.loc[i, 'shirt_style'] + ' - ' + color_str + \
                                                 ' color print ' + '(' + test.loc[i, 'description'] + ')'

                sheet['D{}'.format(self.location)] = test.loc[i, 'total_XXXXL_price']
            if test.loc[i,'XXXXXL_Q'] != 0:
                self.location += 1
                sheet['B{}'.format(self.location)] = test.loc[i, 'XXXXXL_Q']
                sheet['C{}'.format(self.location)] = '5XL - ' + test.loc[i, 'shirt_style'] + ' - ' + color_str + \
                                                 ' color print ' + '(' + test.loc[i, 'description'] + ')'

                sheet['D{}'.format(self.location)] = test.loc[i, 'total_XXXXXL_price']
            self.location += 1

        sheet['C{}'.format(self.location)] = 'Setup and Screens'
        sheet['C{}'.format(self.location)].alignment = Alignment(horizontal='right')
        sheet['D{}'.format(self.location)] = 'WAIVED'
        sheet['E{}'.format(self.location)] = 'WAIVED'
        sheet['C{}'.format(self.location + 1)] = 'Tax'
        sheet['C{}'.format(self.location + 1)].alignment = Alignment(horizontal='right')
        if test['tax_total'].any():
            sheet['D{}'.format(self.location + 1)] = '-'
            sheet['E{}'.format(self.location + 1)] = test['tax_total'].sum()
        else:
            sheet['D{}'.format(self.location + 1)] = 'EXEMPT'
            sheet['E{}'.format(self.location + 1)] = 'EXEMPT'
        for i in range (self.location+2,45):
            sheet['E{}'.format(i)] = None
        test['sizes'] = test['sizes'].str.replace('{','',regex=True).str.replace('}','',regex=True).str.replace("'",'',regex=True).\
            str.replace(':',' -', regex = True)
        for i,v in enumerate(test['sizes']):
            sheet['C{}'.format(self.location + 4 + i)] = test.loc[i, 'description'] + ': ' + v
        sheet['D45'] = 'TOTAL DUE'
        sheet['D45'].alignment = Alignment(horizontal = 'right')
        sheet['E45'] = test['grand_total'].sum()

        xfile.save('{}/{}.xlsx'.format('running_quotes/' + self.customer_class.name, self.df_name))