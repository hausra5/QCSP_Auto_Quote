from classes.customer import Customer
import os
from classes.customer_TK import customer_app
from classes.quote_TK import quote_app
from write.write_quote import write_quote

class builder:
    def __init__(self, front_price,addl_price):
        # Create Customer Info Window
        self.CA = customer_app()
        self.CA.mainloop()
        self.front_price = front_price
        self.addl_price = addl_price

        # Create customer via Customer Class
        self.customer = Customer(self.CA.customer_name, self.CA.customer_email, self.CA.customer_phone,
                                 self.CA.customer_address)

        # Create directory for Customer
        self.wq = write_quote(self.customer, self.CA.df_name)

        try:
            os.makedirs(os.path.join("running_quotes",self.customer.name))
        except:
           pass

        # Start Output File with Customer Info
        self.wq.write_customer_info()

        # Open Quote Form Window and run loop
        self.QA = quote_app(customer_class=self.customer, df_name=self.CA.df_name, front=self.front_price, addl=self.addl_price)
        self.QA.mainloop()

        # Save Output and Dataframe
        self.wq.write_quote_info(self.QA)
        self.wq.write_dataframe()