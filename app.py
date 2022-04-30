from flask import Flask, render_template, request
import numpy as np
import pickle
import pandas as pd


app = Flask(__name__, template_folder='Templates')
model = pickle.load(open('model.pkl', 'rb'))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    temperature = request.form.get('temperature')
    fuel_price = request.form.get('fuel_price')
    Cpi = request.form.get('CPI')
    Unemployment = request.form.get('Unemployment')
    Day= request.form.get('Day')
    Month=request.form.get('Month')
    Holiday=request.form.get('Holiday')
    store= int(request.form.get('store'))
    print('store:', store)
    S = np.zeros(44)
    for i in range(1,45): 
          if (i==store):
            S[i-1]= 1 
    print('S=', S)
    arr1 = np.array([temperature, fuel_price, Cpi, Unemployment,Day, Month, Holiday ])
    final_arr= np.concatenate((arr1,S))
    final_arr = final_arr.astype(np.float64)
    print(final_arr)
    pred = model.predict([final_arr])
    output= abs(round(pred[0],2))
    return render_template('index.html', data=output)


if __name__ == '__main__':
    app.run(debug=True)