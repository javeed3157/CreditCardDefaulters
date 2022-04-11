from flask import Flask, request, render_template
from flask import Response, send_file
import os
from flask_cors import CORS, cross_origin
from prediction_Validation_Insertion import pred_validation
from trainingModel import trainModel
from training_Validation_Insertion import train_validation
from predictFromModel import prediction
os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)

@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRouteClient():
    try:
        if request.form is not None:
            path = request.form['filepath']
            pred_val = pred_validation(path)
            pred_val.prediction_validation()
            pred = prediction(path)
            path = pred.predictionFromModel()
            return send_file('Prediction_Output_File/Predictions.csv', mimetype='text/csv',attachment_filename='Predictions.csv', as_attachment=True)
            # return Response("Prediction File created ")
    except ValueError:
        return Response("Error Occurred! %s" %ValueError)
    except KeyError:
        return Response("Error Occurred! %s" %KeyError)
    except Exception as e:
        return Response("Error Occurred! %s" %e)

@app.route("/train", methods=['POST'])
@cross_origin()
def trainRouteClient():
    try:
        if request.form is not None:
            path = request.form['filepath']
            train_valObj = train_validation(path)
            train_valObj.train_validation()
            trainModelObj = trainModel()
            trainModelObj.trainingModel()
    except ValueError:
        return Response("Error Occurred! %s" % ValueError)
    except KeyError:
        return Response("Error Occurred! %s" % KeyError)
    except Exception as e:
        return Response("Error Occurred! %s" % e)
    return Response("Training successfull!!")

@app.route("/download", methods=['POST'])
@cross_origin()
def downloadFile():
    try:
        if(os.path.isfile("D:\creditCardDefaulters\Prediction_Output_File\Predictions.csv")):
            csv_path = "D:\creditCardDefaulters\Prediction_Output_File\Predictions.csv"
            csv_file = "Predictions.csv"
            return send_file(csv_path,as_attachment=True,attachment_filename=csv_file)
    except Exception as e:
        return Response

if __name__ == "__main__":
    app.run(debug=True)