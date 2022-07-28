import tkinter as tk
from tkinter import ttk
from classes.quote import Quote_info

class quote_app(tk.Tk):
    def __init__(self, count = 1, total = [], total_profit = [], df_name = None,
                customer_class = None, due_date = None, shirt_style = None, quantity_break = None,
                s_xl_q = None, xxl_q = None, xxxl_q = None, xxxxl_q = None, xxxxxl_q = None,
                location1 = None, location2 = None, location3 = None, location4 = None,
                description = None, override_front = None, override_addl = None, upcharge = None, tax = None,
                s_xl_blank = None, xxl_blank = None, xxxl_blank = None, xxxxl_blank = None, xxxxxl_blank = None,
                quote_name = None):
        super().__init__()

        self.title('Queen City Quote Form')
        self.geometry("700x700")
        self.resizable(True, True)
        self.count = count
        self.total = total
        self.total_profit = total_profit
        self.df_name = df_name
        self.customer_class = customer_class
        self.due_date = due_date
        self.shirt_style = shirt_style
        self.quantity_break = quantity_break
        self.s_xl_q = s_xl_q
        self.xxl_q = xxl_q
        self.xxxl_q = xxxl_q
        self.xxxxl_q = xxxxl_q
        self.xxxxxl_q = xxxxxl_q
        self.location1 = location1
        self.location2 = location2
        self.location3 = location3
        self.location4 = location4
        self.description = description
        self.override_front = override_front
        self.override_addl = override_addl
        self.upcharge = upcharge
        self.tax = tax
        self.s_xl_blank = s_xl_blank
        self.xxl_blank = xxl_blank
        self.xxxl_blank = xxxl_blank
        self.xxxxl_blank = xxxxl_blank
        self.xxxxxl_blank = xxxxxl_blank
        self.quote_name = quote_name

        self.create_quote_widgets()

    def create_quote_widgets(self):
        self.quote_count = tk.Label(self, text='Quote #{}'.format(self.count), font=('calibre', 16, 'bold'))
        self.quote_count.grid(row=0, column=0)

        self.due_date_qa = tk.StringVar()
        due_date_label = tk.Label(self, text='Due Date', font=('calibre', 12, 'bold'))
        due_date_label.grid(row=1, column=0)
        due_date_entry = tk.Entry(self, textvariable=self.due_date_qa, font=('calibre', 12, 'normal'), width=27)
        due_date_entry.grid(row=1, column=1)

        self.shirt_style = tk.StringVar()
        shirt_style_label = tk.Label(self, text='Shirt Style', font=('calibre', 12, 'bold'))
        shirt_style_label.grid(row=2, column=0)
        shirt_style_entry = tk.Entry(self, textvariable=self.shirt_style, font=('calibre', 12, 'normal'), width=27)
        shirt_style_entry.grid(row=2, column=1)

        self.quantity_break = tk.StringVar()
        quantity_break_label = tk.Label(self, text='Quantity Break', font=('calibre', 12, 'bold'))
        quantity_break_label.grid(row=3, column=0)
        quantity_break_entry = ttk.Combobox(self, textvariable=self.quantity_break, font=('calibre', 12, 'bold'),
                                            width=27)
        quantity_break_entry['values'] = [12, 24, 72, 144, 288, 500, 1000, 2000]
        quantity_break_entry['state'] = 'readonly'
        quantity_break_entry.grid(row=3, column=1)

        self.s_xl_q = tk.StringVar()
        s_xl_q_label = tk.Label(self, text='S-XL Quantity', font=('calibre', 12, 'bold'))
        s_xl_q_label.grid(row=4, column=0)
        s_xl_q_entry = tk.Entry(self, textvariable=self.s_xl_q, font=('calibre', 12, 'normal'), width=27)
        s_xl_q_entry.grid(row=4, column=1)

        self.xxl_q = tk.StringVar()
        xxl_q_label = tk.Label(self, text='2XL Quantity', font=('calibre', 12, 'bold'))
        xxl_q_label.grid(row=5, column=0)
        xxl_q_entry = tk.Entry(self, textvariable=self.xxl_q, font=('calibre', 12, 'normal'), width=27)
        xxl_q_entry.grid(row=5, column=1)

        self.xxxl_q = tk.StringVar()
        xxxl_q_label = tk.Label(self, text='3XL Quantity', font=('calibre', 12, 'bold'))
        xxxl_q_label.grid(row=6, column=0)
        xxxl_q_entry = tk.Entry(self, textvariable=self.xxxl_q, font=('calibre', 12, 'normal'), width=27)
        xxxl_q_entry.grid(row=6, column=1)

        self.xxxxl_q = tk.StringVar()
        xxxxl_q_label = tk.Label(self, text='4XL Quantity', font=('calibre', 12, 'bold'))
        xxxxl_q_label.grid(row=7, column=0)
        xxxxl_q_entry = tk.Entry(self, textvariable=self.xxxxl_q, font=('calibre', 12, 'normal'), width=27)
        xxxxl_q_entry.grid(row=7, column=1)

        self.xxxxxl_q = tk.StringVar()
        xxxxxl_q_label = tk.Label(self, text='5XL Quantity', font=('calibre', 12, 'bold'))
        xxxxxl_q_label.grid(row=8, column=0)
        xxxxxl_q_entry = tk.Entry(self, textvariable=self.xxxxxl_q, font=('calibre', 12, 'normal'), width=27)
        xxxxxl_q_entry.grid(row=8, column=1)

        self.location1 = tk.StringVar()
        location1_label = tk.Label(self, text='Location 1 Colors', font=('calibre', 12, 'bold'))
        location1_label.grid(row=9, column=0)
        location1_entry = ttk.Combobox(self, textvariable=self.location1, font=('calibre', 12, 'bold'), width=27)
        location1_entry['values'] = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        location1_entry['state'] = 'readonly'
        location1_entry.grid(row=9, column=1)

        self.location2 = tk.StringVar()
        location2_label = tk.Label(self, text='Location 2 Colors', font=('calibre', 12, 'bold'))
        location2_label.grid(row=10, column=0)
        location2_entry = ttk.Combobox(self, textvariable=self.location2, font=('calibre', 12, 'bold'), width=27)
        location2_entry['values'] = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        location2_entry['state'] = 'readonly'
        location2_entry.grid(row=10, column=1)

        self.location3 = tk.StringVar()
        location3_label = tk.Label(self, text='Location 3 Colors', font=('calibre', 12, 'bold'))
        location3_label.grid(row=11, column=0)
        location3_entry = ttk.Combobox(self, textvariable=self.location3, font=('calibre', 12, 'bold'), width=27)
        location3_entry['values'] = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        location3_entry['state'] = 'readonly'
        location3_entry.grid(row=11, column=1)

        self.location4 = tk.StringVar()
        location4_label = tk.Label(self, text='Location 4 Colors', font=('calibre', 12, 'bold'))
        location4_label.grid(row=12, column=0)
        location4_entry = ttk.Combobox(self, textvariable=self.location4, font=('calibre', 12, 'bold'), width=27)
        location4_entry['values'] = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        location4_entry['state'] = 'readonly'
        location4_entry.grid(row=12, column=1)

        self.description = tk.StringVar()
        description_label = tk.Label(self, text='Design Description', font=('calibre', 12, 'bold'))
        description_label.grid(row=13, column=0)
        description_entry = tk.Entry(self, textvariable=self.description, font=('calibre', 12, 'normal'), width=27)
        description_entry.grid(row=13, column=1)

        self.override_front = tk.StringVar()
        override_front_label = tk.Label(self, text='Override Front Price', font=('calibre', 12, 'bold'))
        override_front_label.grid(row=14, column=0)
        override_front_entry = tk.Entry(self, textvariable=self.override_front, font=('calibre', 12, 'normal'), width=27)
        override_front_entry.grid(row=14, column=1)

        self.override_addl = tk.StringVar()
        override_addl_label = tk.Label(self, text='Override Additional Location Price', font=('calibre', 12, 'bold'))
        override_addl_label.grid(row=15, column=0)
        override_addl_entry = tk.Entry(self, textvariable=self.override_addl, font=('calibre', 12, 'normal'), width=27)
        override_addl_entry.grid(row=15, column=1)

        self.upcharge = tk.StringVar()
        upcharge_label = tk.Label(self, text='Flat Upcharge Price', font=('calibre', 12, 'bold'))
        upcharge_label.grid(row=16, column=0)
        upcharge_entry = tk.Entry(self, textvariable=self.upcharge, font=('calibre', 12, 'normal'), width=27)
        upcharge_entry.grid(row=16, column=1)

        self.tax = tk.StringVar()
        tax_label = tk.Label(self, text='Tax Price (NC = .0725)', font=('calibre', 12, 'bold'))
        tax_label.grid(row=17, column=0)
        tax_entry = tk.Entry(self, textvariable=self.tax, font=('calibre', 12, 'normal'), width=27)
        tax_entry.grid(row=17, column=1)

        self.s_xl_blank = tk.StringVar()
        s_xl_blank_label = tk.Label(self, text='S-XL Blank Price', font=('calibre', 12, 'bold'))
        s_xl_blank_label.grid(row=18, column=0)
        s_xl_blank_entry = tk.Entry(self, textvariable=self.s_xl_blank, font=('calibre', 12, 'normal'), width=27)
        s_xl_blank_entry.grid(row=18, column=1)

        self.xxl_blank = tk.StringVar()
        xxl_blank_label = tk.Label(self, text='2XL Blank Price', font=('calibre', 12, 'bold'))
        xxl_blank_label.grid(row=19, column=0)
        xxl_blank_entry = tk.Entry(self, textvariable=self.xxl_blank, font=('calibre', 12, 'normal'), width=27)
        xxl_blank_entry.grid(row=19, column=1)

        self.xxxl_blank = tk.StringVar()
        xxxl_blank_label = tk.Label(self, text='3XL Blank Price', font=('calibre', 12, 'bold'))
        xxxl_blank_label.grid(row=20, column=0)
        xxxl_blank_entry = tk.Entry(self, textvariable=self.xxxl_blank, font=('calibre', 12, 'normal'), width=27)
        xxxl_blank_entry.grid(row=20, column=1)

        self.xxxxl_blank = tk.StringVar()
        xxxxl_blank_label = tk.Label(self, text='4XL Blank Price', font=('calibre', 12, 'bold'))
        xxxxl_blank_label.grid(row=21, column=0)
        xxxxl_blank_entry = tk.Entry(self, textvariable=self.xxxxl_blank, font=('calibre', 12, 'normal'), width=27)
        xxxxl_blank_entry.grid(row=21, column=1)

        self.xxxxxl_blank = tk.StringVar()
        xxxxxl_blank_label = tk.Label(self, text='5XL Blank Price', font=('calibre', 12, 'bold'))
        xxxxxl_blank_label.grid(row=22, column=0)
        xxxxxl_blank_entry = tk.Entry(self, textvariable=self.xxxxxl_blank, font=('calibre', 12, 'normal'), width=27)
        xxxxxl_blank_entry.grid(row=22, column=1)

        self.quote_name = tk.StringVar()
        quote_name_label = tk.Label(self, text='Quote Name', font=('calibre', 12, 'bold'))
        quote_name_label.grid(row=23, column=0)
        quote_name_entry = tk.Entry(self, textvariable=self.quote_name, font=('calibre', 12, 'normal'), width=27)
        quote_name_entry.grid(row=23, column=1)

        sub_btn = tk.Button(self, text='Submit', command=self.submit, width=10, padx=5, pady=5, height=1)
        sub_btn.grid(row=24, column=1)
        exit_button = tk.Button(self, text="Exit", command=self.destroy, width=10, padx=5, pady=5, height=1)
        exit_button.grid(row=25, column=1)

        self.set_variables()

    def submit(self):
        self.count += 1
        self.due_date = self.due_date_qa.get()

        quantity_dict_auto = {'S-XL': int(self.s_xl_q.get()), 'XXL': int(self.xxl_q.get()),
                              'XXXL': int(self.xxxl_q.get()),
                              'XXXXL': int(self.xxxxl_q.get()), 'XXXXXL': int(self.xxxxxl_q.get())}

        quote_info = Quote_info(name=self.customer_class.name, email=self.customer_class.email,
                                phone=self.customer_class.phone, address=self.customer_class.address,
                                due_date=self.due_date, shirt_style=self.shirt_style.get(),
                                shirt_price=float(self.s_xl_blank.get()),
                                quantity_break=int(self.quantity_break.get()),
                                location1=int(self.location1.get()), location2=int(self.location2.get()),
                                location3=int(self.location3.get()), location4=int(self.location4.get()),
                                description=self.description.get(), override_front=float(self.override_front.get()),
                                override_additional=float(self.override_addl.get()),
                                upcharge=float(self.upcharge.get()),
                                tax=float(self.tax.get()), XXL=float(self.xxl_blank.get()),
                                XXXL=float(self.xxxl_blank.get()), XXXXL=float(self.xxxxl_blank.get()),
                                XXXXXL=float(self.xxxxxl_blank.get()), quantity_dict=quantity_dict_auto)

        grand_total, profit, actual_quote = quote_info.run_quote()
        quote_info.print_quote(actual_quote, file_name=self.df_name + '_quote',
                               dir='running_quotes/' + self.customer_class.name)
        self.total.append(grand_total)
        self.total_profit.append(profit)
        self.customer_class.add_quote(self.quote_name.get(), actual_quote)
        self.set_variables()
        self.quote_count.config(text="Quote #{}".format(self.count))

    def set_variables(self):
        self.shirt_style.set("")
        self.quantity_break.set("72")
        self.s_xl_q.set("72")
        self.xxl_q.set("0")
        self.xxxl_q.set("0")
        self.xxxxl_q.set("0")
        self.xxxxxl_q.set("0")
        self.location1.set("1")
        self.location2.set("0")
        self.location3.set("0")
        self.location4.set("0")
        self.description.set("")
        self.override_front.set("0")
        self.override_addl.set("0")
        self.upcharge.set("0")
        self.tax.set("0")
        self.s_xl_blank.set("0.00")
        self.xxl_blank.set("0.00")
        self.xxxl_blank.set("0.00")
        self.xxxxl_blank.set("0.00")
        self.xxxxxl_blank.set("0.00")
        self.quote_name.set("")