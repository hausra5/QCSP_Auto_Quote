from classes.customer import Customer
import pandas as pd

class Quote_info(Customer):
    def __init__(self,name,email, phone, address, due_date, shirt_style, shirt_price, quantity_break, location1, location2 = 0, location3 = 0,
                 location4 = 0, description = 0,override_front = 0, override_additional = 0, upcharge = 0, tax = .0725, XXL = 0, XXXL = 0, XXXXL = 0, XXXXXL = 0,
                 quantity_dict = {'S-XL':0,'XXL':0,'XXXL':0,'XXXXL':0,'XXXXXL':0}):
        super().__init__(name, email, phone, address)
        self.description = description
        self.due_date = due_date
        self.shirt_style = shirt_style
        self.location1 = location1
        self.location2 = location2
        self.location3 = location3
        self.location4 = location4
        self.override_front = override_front
        self.override_additional = override_additional
        self.upcharge = upcharge
        self.tax = tax
        self.XXL = XXL
        self.XXXL = XXXL
        self.XXXXL = XXXXL
        self.XXXXXL = XXXXXL
        self.quantity_dict = quantity_dict
        self.quantity = str(sum(quantity_dict.values()))
        self.quantity_break = str(quantity_break)
        self.shirt_price = shirt_price
        self.shirt_lizard_price_per_shirt = 1.21
        self.shirt_lizard_screen_charge = 34
        self.quote = self.run_quote()

    def run_quote(self):
        front = pd.read_csv('/Users/WordApparel/PycharmProjects/QCSP_Auto_Quote/qcsp_prices/Front_Print.csv')
        addl = pd.read_csv('/Users/WordApparel/PycharmProjects/QCSP_Auto_Quote/qcsp_prices/addl_print.csv')
        quote_dict = {}
        quote_dict['customer'] = self.name
        quote_dict['email'] = self.email
        quote_dict['phone'] = self.phone
        quote_dict['address'] = self.address
        quote_dict['due_date'] = self.due_date
        quote_dict['quantity'] = int(self.quantity)
        quote_dict['sizes'] = self.quantity_dict
        quote_dict['S-XL_price'] = self.shirt_price
        quote_dict['XXL_price'] = self.XXL
        quote_dict['XXXL_price'] = self.XXXL
        quote_dict['XXXXL_price'] = self.XXXXL
        quote_dict['XXXXXL_price'] = self.XXXXXL
        quote_dict['override_front'] = self.override_front
        quote_dict['override_additional'] = self.override_additional
        quote_dict['total upcharge'] = self.upcharge
        quote_dict['shirt_lizard_price_per_shirt'] = self.shirt_lizard_price_per_shirt
        quote_dict['shirt_lizard_screen_charge'] = self.shirt_lizard_screen_charge

        quote_dict['total_blank_cost'] = round(((quote_dict['S-XL_price']) * quote_dict['sizes']['S-XL']) +
                                              (quote_dict['XXL_price'] * quote_dict['sizes']['XXL']) +
                                              (quote_dict['XXXL_price'] * quote_dict['sizes']['XXXL']) +
                                              (quote_dict['XXXXL_price'] * quote_dict['sizes']['XXXXL']) +
                                              (quote_dict['XXXXXL_price'] * quote_dict['sizes']['XXXXXL']),2)

        def quote_dict_totals(addl2=0.0, addl3=0.0, addl4=0.0, locations=1):
            quote_dict['total_S-XL_price'] = round(
                quote_dict['front_price'] + addl2 + addl3 + addl4 + quote_dict[
                    'S-XL_price'], 2)
            quote_dict['total_XXL_price'] = round(
                quote_dict['front_price'] + addl2 + addl3 + addl4 + quote_dict[
                    'XXL_price'], 2)
            quote_dict['total_XXXL_price'] = round(
                quote_dict['front_price'] + addl2 + addl3 + addl4 + quote_dict[
                    'XXXL_price'], 2)
            quote_dict['total_XXXXL_price'] = round(
                quote_dict['front_price'] + addl2 + addl3 + addl4 + quote_dict[
                    'XXXXL_price'], 2)
            quote_dict['total_XXXXXL_price'] = round(
                quote_dict['front_price'] + addl2 + addl3 + addl4 + quote_dict[
                    'XXXXXL_price'], 2)

            quote_dict['tax_total'] = round(
                self.tax * (((quote_dict['total_S-XL_price']) * quote_dict['sizes']['S-XL']) +
                            (quote_dict['total_XXL_price'] * quote_dict['sizes']['XXL']) +
                            (quote_dict['total_XXXL_price'] * quote_dict['sizes']['XXXL']) +
                            (quote_dict['total_XXXXL_price'] * quote_dict['sizes']['XXXXL']) +
                            (quote_dict['total_XXXXXL_price'] * quote_dict['sizes']['XXXXXL'])), 2)
            quote_dict['grand_total'] = round(((quote_dict['total_S-XL_price']) * quote_dict['sizes']['S-XL']) +
                                              (quote_dict['total_XXL_price'] * quote_dict['sizes']['XXL']) +
                                              (quote_dict['total_XXXL_price'] * quote_dict['sizes']['XXXL']) +
                                              (quote_dict['total_XXXXL_price'] * quote_dict['sizes']['XXXXL']) +
                                              (quote_dict['total_XXXXXL_price'] * quote_dict['sizes']['XXXXXL']) +
                                              (quote_dict['tax_total']), 2)

            quote_dict['shirt_lizard_cost'] = round(
                ((quote_dict['quantity'] * locations) * quote_dict['shirt_lizard_price_per_shirt']) +
                ((self.location1 + self.location2 + self.location3 + self.location4) * quote_dict[
                    'shirt_lizard_screen_charge']), 2)
            quote_dict['profit'] = round(
                quote_dict['grand_total'] - quote_dict['total_blank_cost'] - quote_dict['shirt_lizard_cost'], 2)

            return quote_dict

        if self.override_front != 0:
            quote_dict['front_price'] = round(float(self.override_front + self.upcharge),2)
        else:
            quote_dict['front_price'] = round(float(front[front['Colors'] == self.location1][self.quantity_break].values[0].replace('$','')) + self.upcharge,2)

        if self.location2 != 0 and self.location3 == 0 and self.location4 == 0:
            if self.override_additional != 0:
                quote_dict['addl2'] = self.override_additional
            else:
                quote_dict['addl2'] = float(addl[addl['Colors'] == self.location2][self.quantity_break].values[0].replace('$', ''))

            quote_dict = quote_dict_totals(addl2 = quote_dict['addl2'], locations = 2)

            return quote_dict['grand_total'], quote_dict['profit'], quote_dict

        elif self.location2 != 0 and self.location3 != 0 and self.location4 == 0:
            if self.override_additional != 0:
                quote_dict['addl2'] = self.override_additional
                quote_dict['addl3'] = self.override_additional
            else:
                quote_dict['addl2'] = float(addl[addl['Colors'] == self.location2][self.quantity_break].values[0].replace('$', ''))
                quote_dict['addl3'] = float(addl[addl['Colors'] == self.location3][self.quantity_break].values[0].replace('$', ''))

            quote_dict = quote_dict_totals(addl2=quote_dict['addl2'], addl3=quote_dict['addl3'],locations=3)

            return quote_dict['grand_total'], quote_dict['profit'], quote_dict

        elif self.location2 != 0 and self.location3 != 0 and self.location4 != 0:
            if self.override_additional != 0:
                quote_dict['addl2'] = self.override_additional
                quote_dict['addl3'] = self.override_additional
                quote_dict['addl4'] = self.override_additional
            else:
                quote_dict['addl2'] = float(addl[addl['Colors'] == self.location2][self.quantity_break].values[0].replace('$', ''))
                quote_dict['addl3'] = float(addl[addl['Colors'] == self.location3][self.quantity_break].values[0].replace('$', ''))
                quote_dict['addl4'] = float(addl[addl['Colors'] == self.location4][self.quantity_break].values[0].replace('$', ''))

            quote_dict = quote_dict_totals(addl2=quote_dict['addl2'],addl3=quote_dict['addl3'],
                                           addl4=quote_dict['addl4'],locations=4)

            return quote_dict['grand_total'], quote_dict['profit'], quote_dict

        quote_dict = quote_dict_totals()

        return quote_dict['grand_total'], quote_dict['profit'], quote_dict

    def print_quote(self, actual_quote, file_name = None, dir = None):
        with open(dir+'/'+file_name, "a") as f:
            if self.description:
                print('Design: ', self.description, file = f)
            if self.location2 != 0 and self.location3 == 0 and self.location4 == 0:
                print(
                    '{} Quantity - {} - {}/{} Color Print'.format(self.quantity, self.shirt_style,
                                                                  self.location1, self.location2), file = f)

            elif self.location2 != 0 and self.location3 != 0 and self.location4 == 0:
                print(
                    '{} Quantity - {} - {}/{}/{} Color Print'.format(self.quantity, self.shirt_style,
                                                                     self.location1, self.location2,
                                                                     self.location3), file = f)

            elif self.location2 != 0 and self.location3 != 0 and self.location4 != 0:
                print(
                    '{} Quantity - {} - {}/{}/{}/{} Color Print'.format(self.quantity, self.shirt_style,
                                                                        self.location1, self.location2,
                                                                        self.location3, self.location4), file = f)
            else:
                print(
                    '{} Quantity - {} - {} Color Print'.format(self.quantity, self.shirt_style,
                                                               self.location1), file = f)

            if actual_quote['tax_total'] == 0:
                tax = 'EXEMPT'
            else:
                tax = actual_quote['tax_total']

            print(' S-XL price per shirt: $', actual_quote['total_S-XL_price'], '\n',
                  '2XL price per shirt: $', actual_quote['total_XXL_price'], '\n',
                  '3XL price per shirt: $', actual_quote['total_XXXL_price'], '\n',
                  '4XL price per shirt: $', actual_quote['total_XXXXL_price'], '\n',
                  '5XL price per shirt: $', actual_quote['total_XXXXXL_price'], '\n',
                  'Total Tax: {}'.format(tax), '\n',
                  'Grand Total Quote: $', actual_quote['grand_total'], file = f)
            print('-' * 30, file = f)