import pyodbc
from flask import Flask,jsonify,request,render_template
app = Flask(__name__)

server='DESKTOP-RCL2SU1\SQLEXPRESS'
database='newims'
driver='{sql server}'

connection_string = f'DRIVER={driver};SERVER={server};DATABASE={database};trusted_connection=yes'

conn = pyodbc.connect(connection_string)


cn = conn.cursor()

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


@app.route('/customer/add', methods=['GET', 'POST'])
def addcustomer():
    if request.method == 'POST':
        cn = conn.cursor()
        customername = request.form.get('customer_name')
        customeraddr = request.form.get('customer_addr')
        customeremail = request.form.get('customer_email')
        cn.execute(f"INSERT INTO customer (customer_name, customer_addr, customer_email) VALUES ('{customername}', '{customeraddr}', '{customeremail}')")
        conn.commit()
        print('Data has been inserted')
        return jsonify({'message': 'successful'})
    else:
        return render_template('addcustomer.html')

@app.route('/customer/update', methods=['GET', 'POST'])
def updatecustomer():
    if request.method == 'POST':
        cn = conn.cursor()
        customerid = request.form.get('customer_id')
        change = request.form.get('change')
        newvalue = request.form.get('newvalue')
        print (customerid)
        print(change)
        print(newvalue)
        cn.execute(f"update customer set {change} = '{newvalue}' where customer_id= '{customerid}'")
        conn.commit()
        print('Data has been updated')
        return jsonify({'message': 'successful'})
    else:
        return render_template('updatecustomer.html')


@app.route('/customer/delete', methods=['GET', 'POST'])
def deletecustomer():
    if request.method == 'POST':
        cn = conn.cursor()
        customerid = request.form.get('customer_id')
        cn.execute(f"DELETE FROM customer WHERE customer_id = '{customerid}'")
        conn.commit()
        print('Data has been deleted')
        return jsonify({'message': 'successful'})
    else:
        return render_template('deletecustomer.html')

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

@app.route('/supplier/add', methods=['GET', 'POST'])
def addsupplier():
    if request.method == 'POST':
        cn = conn.cursor()
        suppliername = request.form.get('supplier_name')
        supplieraddr = request.form.get('supplier_addr')
        supplieremail = request.form.get('supplier_email')
        cn.execute(f"INSERT INTO supplier (supplier_name, supplier_addr, supplier_email) VALUES ('{suppliername}', '{supplieraddr}', '{supplieremail}')")
        conn.commit()
        print('Data has been inserted')
        return jsonify({'message': 'successful'})
    else:
        return render_template('addsupplier.html')

@app.route('/supplier/update', methods=['GET', 'POST'])
def updatesupplier():
    if request.method == 'POST':
        cn = conn.cursor()
        supplierid = request.form.get('supplier_id')
        change = request.form.get('change')
        newvalue = request.form.get('newvalue')
        print (supplierid)
        print(change)
        print(newvalue)
        cn.execute(f"update supplier set {change} = '{newvalue}' where supplier_id= '{supplierid}'")
        conn.commit()
        print('Data has been updated')
        return jsonify({'message': 'successful'})
    else:
        return render_template('updatesupplier.html')


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


@app.route('/product/add', methods=['GET', 'POST'])
def addproduct():
    if request.method == 'POST':
        cn = conn.cursor()
        productname = request.form.get('product_name')
        productstock = request.form.get('product_stock')
        productprice = request.form.get('product_price')
        productsupplierid = request.form.get('product_supplierid')
        cn.execute(f"INSERT INTO PRODUCT(PRODUCT_NAME,STOCK,PRICE,SUPPLIER_ID) VALUES ('{productname}',{productstock}, {productprice}, '{productsupplierid}')")
        conn.commit()
        print('Data has been inserted')
        return jsonify({'message': 'successful'})
    else:
        return render_template('addproduct.html')


@app.route('/product/update', methods=['GET', 'POST'])
def updateproduct():
    if request.method == 'POST':
        cn = conn.cursor()
        productid = request.form.get('product_id')
        change = request.form.get('change')
        newvalue = request.form.get('newvalue')
        print(productid)
        print(change)
        print(newvalue)
        
        # Sanitize user input to prevent SQL injection
        valid_columns = ['product_name', 'stock', 'price', 'supplierid']
        if change not in valid_columns:
            return jsonify({'error': 'Invalid column name'})
        
        # Prepare the SQL query using parameterized query
        query = f"UPDATE product SET {change} = ? WHERE product_id = ?"
        cn.execute(query, (newvalue, productid))
        conn.commit()
        
        print('Data has been updated')
        return jsonify({'message': 'successful'})
    else:
        return render_template('updateproduct.html')



@app.route('/product/delete', methods=['GET', 'POST'])
def deleteproduct():
    if request.method == 'POST':
        cn = conn.cursor()
        productid = request.form.get('product_id')
        cn.execute(f"DELETE FROM PRODUCT WHERE product_id = '{productid}'")
        conn.commit()
        print('Data has been deleted')
        return jsonify({'message': 'successful'})
    else:
        return render_template('deleteproduct.html')


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


@app.route('/orders/add', methods=['GET', 'POST'])
def addorders():
    if request.method == 'POST':
        cn = conn.cursor()
        ordersproductid = request.form.get('product_id')
        orderscustomerid = request.form.get('customer_id')
        ordersquantity = request.form.get('quantity')
        cn.execute(f"INSERT INTO ORDERS(PRODUCT_ID,CUSTOMER_ID,QUANTITY) VALUES ('{ordersproductid}','{orderscustomerid}',{ordersquantity})")
        conn.commit()
        print('Data has been inserted')
        return jsonify({'message': 'successful'})
    else:
        return render_template('addorders.html')


@app.route('/orders/update', methods=['GET', 'POST'])
def updateorders():
    if request.method == 'POST':
        cn = conn.cursor()
        ordersid = request.form.get('order_id')
        change = request.form.get('change')
        newvalue = request.form.get('newvalue')
        print (ordersid)
        print(change)
        print(newvalue)
        cn.execute(f"update orders set {change} = '{newvalue}' where order_id= '{ordersid}'")
        conn.commit()
        print('Data has been updated')
        return jsonify({'message': 'successful'})
    else:
        return render_template('updateorders.html')


@app.route('/orders/delete', methods=['GET', 'POST'])
def delete_orders():
    if request.method == 'POST':
        cn = conn.cursor()
        orders_id = request.form.get('ORDER_ID')
        try:
            cn.execute(f"DELETE FROM ORDERS WHERE ORDER_ID = '{orders_id}'")
            conn.commit()
            print('Data has been deleted')
            return jsonify({'message': 'successful'})
        except Exception as e:
            print('Error occurred:', str(e))
            return jsonify({'message': 'error'})

    else:
        return render_template('deleteorders.html')



if __name__=='__main__':
    app.run()







