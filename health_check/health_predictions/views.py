from django.shortcuts import render,HttpResponse
from joblib import load
from rest_framework.views import APIView
import json
model_diabetes = load('./savedModels/diabetesModel.joblib')
model_heart = load('./savedModels/heartModel.joblib')
model_parkinsons = load('./savedModels/parkinsonsModel.joblib')
# Create your views here.

class DiabetesView(APIView):
     def post(self,request):
          
          Pregnancies = request.data['Pregnancies']
          Glucose = request.data['Glucose']
          BloodPressure = request.data['BloodPressure']
          SkinThickness = request.data['SkinThickness']
          Insulin = request.data['Insulin']
          bmi = request.data['bmi']
          DiabetesPedigreeFunction = request.data['DiabetesPedigreeFunction']
          Age = request.data['Age']
          
          diabetes_pred = model_diabetes.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,bmi,DiabetesPedigreeFunction,Age]])
          
          if diabetes_pred[0]==0:
               diabetes_pred = 'non Diabetic'
          else:
               diabetes_pred = 'Diabetic'
               
          return HttpResponse(json.dumps({'result': diabetes_pred}))
     

class HeartView(APIView):
     def post(self,request):
          
          Age = request.data['Age']
          Sex = request.data['Sex']
          ChestPainType = request.data['ChestPainType']
          RestingBP = request.data['RestingBP']
          SerumCholestrol = request.data['SerumCholestrol']
          FastingBP = request.data['FastingBP']
          RestingElectrocardiograph = request.data['RestingElectrocardiograph']
          MaxHeartRate = request.data['MaxHeartRate']
          ExerciseAngina = request.data['ExerciseAngina']
          STdepressionByexercise = request.data['STdepressionByexercise']
          SlopeSTPeaksegment = request.data['SlopeSTPeaksegment']
          MajorVesselsColored = request.data['MajorVesselsColored']
          Thal = request.data['Thal']
          
          heart_pred = model_heart.predict([[Age,Sex,ChestPainType,RestingBP,SerumCholestrol,FastingBP,RestingElectrocardiograph,MaxHeartRate,ExerciseAngina,STdepressionByexercise,SlopeSTPeaksegment,MajorVesselsColored,Thal]])
          
          if heart_pred[0]==0:
               heart_pred = 'No Heart disease present'
          else:
               heart_pred = 'Heart disease present'
               
          return HttpResponse(json.dumps({'result': heart_pred}))
     
     