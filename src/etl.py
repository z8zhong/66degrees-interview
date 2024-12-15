import kagglehub
import pandas as pd
import sqlite3

class etl():
    def __init__(self):
        self.df = pd.DataFrame()
        self.df_customer = pd.DataFrame()
        self.df_payment = pd.DataFrame()
        self.df_invoice = pd.DataFrame()

    def extract(self):
        path = kagglehub.dataset_download("aungpyaeap/supermarket-sales")
        self.df = pd.read_csv(path + '/supermarket_sales - Sheet1.csv')
        print("data is successfully extracted")


    def transform(self):
        self.df.columns = self.df.columns.str.lower().str.replace(' ', '_')
        self.df['tax'] = self.df['tax_5%']
        self.df['gross_margin'] = self.df['gross_margin_percentage']
        self.df['invoice_date'] = self.df['date']
        self.df['invoice_time'] = self.df['time']
        self.df['customer_id'] = range(1, len(self.df) + 1)

        self.df_customer = self.df[['customer_id', 'customer_type', 'gender']].reset_index(drop=True)

        self.df_payment = self.df[['payment']].drop_duplicates().reset_index(drop=True)
        self.df_payment['payment_id'] = range(1, len(self.df_payment) + 1)

        self.df_invoice = self.df.merge(self.df_payment, on=['payment'])

        self.df_invoice = self.df_invoice[['invoice_id', 'customer_id', 'payment_id', 'product_line', 'unit_price',
                                           'quantity', 'tax', 'total', 'date', 'time', 'payment', 'cogs', 'gross_margin',
                                           'gross_income', 'rating']]

        print("data is successfully transformed")

    def load(self):
        database_file = "db/supermarket.db"
        conn = sqlite3.connect(database_file)

        self.df_customer.to_sql('customer', conn, index=False, if_exists='replace')
        self.df_payment.to_sql('payment', conn, index=False, if_exists='replace')
        self.df_invoice.to_sql('invoice', conn, index=False, if_exists='replace')

        print("data is successfully loaded")


if __name__ == "__main__":
    etl = etl()
    etl.extract()
    etl.transform()
    etl.load()
