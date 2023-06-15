import pyodbc
from flask import Flask,jsonify,request,render_template
import sqlite3

app = Flask(__name__)


def idgenerator(tab):  
    conn = sqlite3.connect()
    cur = conn.cursor()
    idval = ''
    if tab=='CUSTOMER':
        idval = 'CUSID'
    if tab=='PRODUCT':
        idval = 'PROID'
    if tab=='ORDER':
        idval = 'ORDID'
    if tab=='SUPPLIER':
        idval = 'SUPID'
    print(tab,idval)
    cur.execute(f"SELECT {idval} FROM {tab}")
    new = cur.fetchall()
    cud = str(new[len(new)-1][0])
    for i in range(len(str(cud))):
        if cud[i].isnumeric():
            f = i
            break
    myint = cud[f:]
    myint = int(myint)+1
    return idval[0:3]+str(myint)



# server='DESKTOP-RCL2SU1\SQLEXPRESS'
# database='newims'
# driver='{sql server}'

# connection_string = f'DRIVER={driver};SERVER={server};DATABASE={database};trusted_connection=yes'

# conn = pyodbc.connect(connection_string)


# cn = conn.cursor()

#customer_name = 'RTF'
#customer_addr = 'HYD'
#customer_email = 'rtf@gmail.com'

#cn.execute('select * from customer')
#print(cn.fetchall)

#cn.execute(f"insert into customer(CUSTOMER_NAME,CUSTOMER_ADDR,CUSTOMER_EMAIL) VALUES ('{customer_name}','{customer_addr}','{customer_email}')")
#conn.commit()


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/customer/show')
def CUSTOMER_show():
    cn = conn.cursor()
    cn.execute("SELECT * FROM CUSTOMER")
    data = []
    for i in cn.fetchall():
        CUSTOMER = {}
        CUSTOMER['CUSTOMER_ID'] = i[0]
        CUSTOMER['CUSTOMER_NAME'] = i[1]
        CUSTOMER['CUSTOMER_ADDR'] = i[2]
        CUSTOMER['CUSTOMER_EMAIL'] = i[3]
        data.append(CUSTOMER)
    return render_template('showcustomer.html', data=data)

@app.route('/supplier/show')
def SUPPLIER_show():
    cn = conn.cursor()
    cn.execute("SELECT * FROM SUPPLIER")
    data = []
    for i in cn.fetchall():
        SUPPLIER = {}
        SUPPLIER['SUPPLIER_ID'] = i[0]
        SUPPLIER['SUPPLIER_NAME'] = i[1]
        SUPPLIER['SUPPLIER_ADDR'] = i[2]
        SUPPLIER['SUPPLIER_EMAIL'] = i[3]
        data.append(SUPPLIER)
    return render_template('showsupplier.html', data=data)

@app.route('/product/show')
def product_show():
    cn = conn.cursor()
    cn.execute("select * from PRODUCT")
    data = []
    for i in cn.fetchall():
        PRODUCT = {}
        PRODUCT['PRODUCT_ID']=i[0]
        PRODUCT['PRODUCT_NAME'] = i[1]
        PRODUCT['PRODUCT_STOCK'] = i[2]
        PRODUCT['PRODUCT_PRICE'] = i[3]
        PRODUCT['PRODUCT_SUPPLIERID'] = i[4]
        data.append(PRODUCT)
    return render_template('showproduct.html',data = data)

@app.route('/orders/show')
def orders_show():
    cn = conn.cursor()
    cn.execute("select * from orders")
    data = []
    for i in cn.fetchall():
        orders = {}
        orders['ORDER_ID']=i[0]
        orders['PRODUCT_ID'] = i[1]
        orders['CUSTOMER_ID'] = i[2]
        orders['QUANTITY'] = i[3]
        data.append(orders)
    return render_template('showorders.html',data = data)



if __name__=='__main__':
    app.run(host='0.0.0.0',debug=False,port=6000)