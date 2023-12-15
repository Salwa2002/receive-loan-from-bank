import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException, Query
from prometheus_client import Counter, make_asgi_app
import uvicorn
approved_counter = Counter("approved", "Counter for approved loans")
rejected_counter = Counter("rejected", "Counter for rejected loans")

app = FastAPI()
metrics_app = make_asgi_app()
app.mount("/metrics", metrics_app)

@app.get("/loan_approval")
def prediction_api(
    checking_account: int,
    duration: int,
    credit_history: int,
    purpose: int,
    credit_amount: int,
    savings_account: int,
    employment: int,
    installment_rate: int,
    personal_status: int,
    other_debtors: int,
    residence_duration: int,
    property: int,
    age: int,
    other_installment_plans: int,
    housing: int,
    existing_credits: int,
    job: int,
    num_people_liable: int,
    telephone: int,
    foreign_worker: int
):
    # Charger le modèle formé
    loan_model = joblib.load("./model/SVC_model.joblib")

    # Créer une DataFrame avec les données d'entrée
    data = pd.DataFrame({
        'checking_account': [checking_account],
        'duration': [duration],
        'credit_history': [credit_history],
        'purpose': [purpose],
        'credit_amount': [credit_amount],
        'savings_account': [savings_account],
        'employment': [employment],
        'installment_rate': [installment_rate],
        'personal_status': [personal_status],
        'other_debtors': [other_debtors],
        'residence_duration': [residence_duration],
        'property': [property],
        'age': [age],
        'other_installment_plans': [other_installment_plans],
        'housing': [housing],
        'existing_credits': [existing_credits],
        'job': [job],
        'num_people_liable': [num_people_liable],
        'telephone': [telephone],
        'foreign_worker': [foreign_worker]
    })

    # Faire la prédiction
    prediction = loan_model.predict(data)[0]

    # Mettre à jour les compteurs Prometheus
    if prediction == 1:
        approved_counter.inc()
    else:
        rejected_counter.inc()

    # Retourner le résultat en format JSON
    return {"loan_approval": bool(prediction)}

if __name__ == "__main__":
    
    uvicorn.run(app, host="127.0.0.1",port=5000)