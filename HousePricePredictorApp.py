import joblib
import matplotlib.pyplot as mp
import caster as cs


def HousePricePrediction(age, no_of_rooms,no_of_Brooms,area_population,cuerrnt_year):
    model = joblib.load('House_price_predictor.joblib')

    pred = model.predict([[600,age,no_of_rooms,no_of_Brooms,area_population]])
    return(cs.convert_val(pred))

def plot_graph(age, no_of_rooms,no_of_Brooms,area_population,cuerrnt_year):
    price=[]
    year=[]

    model = joblib.load('House_price_predictor.joblib')

    for i in range (1,6):
        val = (float(model.predict([[600,age+i,no_of_rooms,no_of_Brooms,area_population]])))/1000
        price.append(val)

    for i in range(0,5):
        year.append(str(cuerrnt_year+i))
    print(year)
    print(price)

    mp.plot(year,price)
    mp.show()

    