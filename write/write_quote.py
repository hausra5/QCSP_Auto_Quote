from datetime import date
import pandas as pd

class write_quote:
    def __init__(self,customer_class,df_name,quote_app=None):
        self.customer_class = customer_class
        self.df_name = df_name
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
