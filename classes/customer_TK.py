import tkinter as tk

class customer_app(tk.Tk):
    def __init__(self, customer_name = None, customer_email = None, customer_phone = None,
                 customer_address = None, df_name = None, invoice_no = None):
        super().__init__()

        self.title('Queen City Quote Form - Customer Info')
        self.geometry("400x400")
        self.resizable(True, True)
        self.customer_name = customer_name
        self.customer_email = customer_email
        self.customer_phone = customer_phone
        self.customer_address = customer_address
        self.df_name = df_name
        self.invoice_no = invoice_no

        self.create_customer_widgets()

    def create_customer_widgets(self):
        # Create Customer Labels + Entries + Grid
        cust_info = tk.Label(self, text='Customer Information', font=('calibre', 16, 'bold'))
        cust_info.grid(row=0, column=0)

        self.name = tk.StringVar()
        customer_name_label = tk.Label(self, text='Customer Name (required)', font=('calibre', 12, 'bold'))
        customer_name_label.grid(row=1, column=0)
        customer_name_entry = tk.Entry(self, textvariable=self.name, font=('calibre', 12, 'normal'))
        customer_name_entry.grid(row=1, column=1)

        self.email = tk.StringVar()
        customer_email_label = tk.Label(self, text='Customer E-Mail', font=('calibre', 12, 'bold'))
        customer_email_label.grid(row=2, column=0)
        customer_email_entry = tk.Entry(self, textvariable=self.email, font=('calibre', 12, 'normal'))
        customer_email_entry.grid(row=2, column=1)

        self.phone = tk.StringVar()
        customer_phone_label = tk.Label(self, text='Customer Phone Number', font=('calibre', 12, 'bold'))
        customer_phone_label.grid(row=3, column=0)
        customer_phone_entry = tk.Entry(self, textvariable=self.phone, font=('calibre', 12, 'normal'))
        customer_phone_entry.grid(row=3, column=1)

        self.address = tk.StringVar()
        customer_address_label = tk.Label(self, text='Customer Address', font=('calibre', 12, 'bold'))
        customer_address_label.grid(row=4, column=0)
        customer_address_entry = tk.Entry(self, textvariable=self.address, font=('calibre', 12, 'normal'))
        customer_address_entry.grid(row=4, column=1)

        self.cust_df_name = tk.StringVar()
        name_for_df_label = tk.Label(self, text='Name for DataFrame (required)', font=('calibre', 12, 'bold'))
        name_for_df_label.grid(row=5, column=0)
        name_for_df_entry = tk.Entry(self, textvariable=self.cust_df_name, font=('calibre', 12, 'normal'))
        name_for_df_entry.grid(row=5, column=1)

        self.invoice_no = tk.StringVar()
        name_for_df_label = tk.Label(self, text='Invoice Number', font=('calibre', 12, 'bold'))
        name_for_df_label.grid(row=6, column=0)
        name_for_df_entry = tk.Entry(self, textvariable=self.invoice_no, font=('calibre', 12, 'normal'))
        name_for_df_entry.grid(row=6, column=1)

        cus_sub_btn = tk.Button(self, text='Submit', command=self.customer_submit, width=10, padx=5, pady=5, height=1)
        cus_sub_btn.grid(row=7, column=1)

    def customer_submit(self):
        self.customer_name = self.name.get()
        self.customer_email = self.email.get()
        self.customer_phone = self.phone.get()
        self.customer_address = self.address.get()
        self.df_name = self.cust_df_name.get()
        self.invoice_no = self.invoice_no.get()
        self.destroy()