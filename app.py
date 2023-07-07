from flask import Flask,render_template,request,jsonify
from credit_card_default_pdn.pipeline.prediction_pipeline import PredictPipline,CustomData
from credit_card_default_pdn.logging.logger import logging


application = Flask(__name__)
app = application


@app.route("/",methods = ["GET","POST"])
def predict_datapoint():
    if request.method == "GET":
        return render_template("form2.html")

    else:
        data = CustomData(
            LIMIT_BAL = int(request.form.get("LIMIT_BAL")),
            SEX = int(request.form.get("SEX")),
            EDUCATION = int(request.form.get("EDUCATION")),
            MARRIAGE = int(request.form.get("MARRIAGE")),
            AGE = int(request.form.get("AGE")),
            PAY_0 = int(request.form.get("PAY_0")),
            PAY_2 = int(request.form.get("PAY_2")),
            PAY_3 = int(request.form.get("PAY_3")),
            PAY_4 = int(request.form.get("PAY_4")),
            PAY_5 = int(request.form.get("PAY_5")),
            PAY_6 = int(request.form.get("PAY_6")),
            BILL_AMT1 = int(request.form.get("BILL_AMT1")),
            BILL_AMT2 = int(request.form.get("BILL_AMT2")),
            BILL_AMT3 = int(request.form.get("BILL_AMT3")),
            BILL_AMT4 = int(request.form.get("BILL_AMT4")),
            BILL_AMT5 = int(request.form.get("BILL_AMT5")),
            BILL_AMT6 = int(request.form.get("BILL_AMT6")),
            PAY_AMT1 = int(request.form.get("PAY_AMT1")),
            PAY_AMT2 = int(request.form.get("PAY_AMT2")),
            PAY_AMT3 = int(request.form.get("PAY_AMT3")),
            PAY_AMT4 = int(request.form.get("PAY_AMT4")),
            PAY_AMT5 = int(request.form.get("PAY_AMT5")),
            PAY_AMT6 = int(request.form.get("PAY_AMT6")),
            )
        

        final_data = data.get_data_as_data_frame()
        predict_pipline = PredictPipline()
        pred = predict_pipline.predict(final_data)

        # if pred == 0:
        #        output = 'Not Default'
        # else:
        #        output = 'Default'

        # return render_template('form2.html', prediction_text = 'Credit Card Default Status for account {} : {}'.format( output))

        result = pred

        if result == 1:
            return render_template("form2.html",final_result = "The Credit Card Holder Will Be Defaulter in Next Month:{}".format(result))
        elif result == 0:
            return render_template("form2.html",final_result = "The Credit Card Holder Will Not Be Defaulter in Next Month:{}".format(result))


if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)