from flask import Flask, render_template, request
from flask_cors import CORS
import os
import numpy as np
from src.mlProject.pipeline.prediction import PredictionPipeline
from src.mlProject.utils.common import display_section_heading
from dotenv import load_dotenv


load_dotenv()

MLFLOW_TRACKING_URI = os.getenv('MLFLOW_TRACKING_URI')
MLFLOW_TRACKING_USERNAME = os.getenv('MLFLOW_TRACKING_USERNAME')
MLFLOW_TRACKING_PASSWORD = os.getenv('MLFLOW_TRACKING_PASSWORD')


app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def homepage():
    
    return render_template("index.html")

@app.route('/train', methods=['GET'])
def training():
    os.environ["MLFLOW_TRACKING_URI"] = MLFLOW_TRACKING_URI
    os.environ["MLFLOW_TRACKING_USERNAME"] = MLFLOW_TRACKING_USERNAME
    os.environ["MLFLOW_TRACKING_PASSWORD"] = MLFLOW_TRACKING_PASSWORD
    
    os.system("python main.py")
    
    return "Training Successful!"

@app.route('/predict', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        
        terminal_width = os.get_terminal_size().columns
        
        def your_endpoint():
            if request.form:
                form_data = request.form.to_dict()
                print('\033[31m' + '-'*terminal_width + f'\nForm Data: {form_data}\n' + '-'*terminal_width + '\033[0m')
                return form_data

            elif request.json:
                json_data = request.json
                print('\033[31m' + '-'*terminal_width + f'\nJSON Data: {json_data}\n' + '-'*terminal_width + '\033[0m')
                return json_data

            else:
                print('Error')
                return 400
            
        request_data = your_endpoint()

        try:
            age = str(request_data['age'])
            gender = str(request_data['gender'])
            family_diabetes = str(request_data['family_diabetes'])
            highbp = str(request_data['highbp'])
            physicallyactive = str(request_data['physicallyactive'])
            bmi = float(request_data['bmi'])
            smoking = str(request_data['smoking'])
            alcohol = str(request_data['alcohol'])
            sleep = float(request_data['sleep'])
            soundsleep = float(request_data['soundsleep'])
            regularmedicine = str(request_data['regularmedicine'])
            junkfood = str(request_data['junkfood'])
            stress = str(request_data['stress'])
            bplevel = str(request_data['bplevel'])
            pregancies = float(request_data['pregancies'])
            pdiabetes = str(request_data['pdiabetes'])
            uriationfreq = str(request_data['uriationfreq'])
            
            # age = str(request.form['age'])  
            # gender = str(request.form['gender'])
            # family_diabetes = str(request.form['family_diabetes'])
            # highbp = str(request.form['highbp'])
            # physicallyactive = str(request.form['physicallyactive'])
            # bmi = float(request.form['bmi'])
            # smoking = str(request.form['smoking'])
            # alcohol = str(request.form['alcohol'])
            # sleep = float(request.form['sleep'])
            # soundsleep = float(request.form['soundsleep'])
            # regularmedicine = str(request.form['regularmedicine'])
            # junkfood = str(request.form['junkfood'])
            # stress = str(request.form['stress'])
            # bplevel = str(request.form['bplevel'])
            # pregancies = float(request.form['pregancies'])
            # pdiabetes = str(request.form['pdiabetes'])
            # uriationfreq = str(request.form['uriationfreq'])

            feature_mappings = {
                'Age': {'less than 40': 0, '40-49': 1, '50-59': 2, '60 or older': 3},
                'Gender': {'male': 0, 'female': 1},
                'Family_Diabetes': {'no': 0, 'yes': 1},
                'highBP': {'no': 0, 'yes': 1},
                'PhysicallyActive': {'none': 0, 'less than half an hr': 1, 'more than half an hr': 2, 'one hr or more': 3},
                'Smoking': {'no': 0, 'yes': 1},
                'Alcohol': {'no': 0, 'yes': 1},
                'RegularMedicine': {'no': 0, 'yes': 1},
                'JunkFood': {'occasionally': 0, 'very often': 1, 'often': 2, 'always': 3},
                'Stress': {'sometimes': 0, 'not at all': 1, 'very often': 2, 'always': 3},
                'BPLevel': {'high': 0, 'normal': 1, 'low': 2},
                'Pdiabetes': {'no': 0, 'yes': 1},
                'UriationFreq': {'not much': 0, 'quite often': 1}
            }

            # Mapping values for all the categorical features
            age_mapped = float(feature_mappings['Age'][age])
            gender_mapped = float(feature_mappings['Gender'][gender])
            family_diabetes_mapped = float(feature_mappings['Family_Diabetes'][family_diabetes])
            highbp_mapped = float(feature_mappings['highBP'][highbp])
            physicallyactive_mapped = float(feature_mappings['PhysicallyActive'][physicallyactive])
            smoking_mapped = float(feature_mappings['Smoking'][smoking])
            alcohol_mapped = float(feature_mappings['Alcohol'][alcohol])
            regularmedicine_mapped = float(feature_mappings['RegularMedicine'][regularmedicine])
            junkfood_mapped = float(feature_mappings['JunkFood'][junkfood])
            stress_mapped = float(feature_mappings['Stress'][stress])
            bplevel_mapped = float(feature_mappings['BPLevel'][bplevel])
            pdiabetes_mapped = float(feature_mappings['Pdiabetes'][pdiabetes])
            uriationfreq_mapped = float(feature_mappings['UriationFreq'][uriationfreq])
            
            data = [
                age_mapped, 
                gender_mapped, 
                family_diabetes_mapped, 
                highbp_mapped, 
                physicallyactive_mapped,
                bmi, 
                smoking_mapped, 
                alcohol_mapped, 
                sleep, 
                soundsleep, 
                regularmedicine_mapped, 
                junkfood_mapped, 
                stress_mapped, 
                bplevel_mapped, 
                pregancies, 
                pdiabetes_mapped, 
                uriationfreq_mapped
            ]
            
            data = np.array(data).reshape(1,-1)            
            obj = PredictionPipeline()
            predict = obj.predict(data)
            
            if predict == 1:
                result = "คุณมีความเสี่ยงเป็นโรคเบาหวาน"
            else:
                result = "คุณไม่มีความเสี่ยงเป็นโรคเบาหวาน"
            
            print('\033[33m' + '-'*terminal_width + f'\nTransformed Data: {data}\n' + '-'*terminal_width + '\033[0m')
            print('\033[32m' + '-'*terminal_width + f'\nPredict: {predict}\n' + '-'*terminal_width + '\033[0m')

            display_section_heading(
                title="result",
                content=result,
                symbol="=",
                title_case='upper', 
                color='\033[34m',  # Blue color
                alignment="center",
                bold=True
            )
            
            return render_template('predict.html', result=result)

        except Exception as e:
            print('='*terminal_width)
            print('The Exception Message is:', e)
            print('='*terminal_width)
            
            return 'Something is wrong!!!'

    else:
        
        return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)