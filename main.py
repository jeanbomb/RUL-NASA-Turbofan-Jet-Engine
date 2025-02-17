from fastapi import FastAPI
import joblib
import numpy as np
from pydantic import BaseModel

# ��l�� FastAPI ����
app = FastAPI()

# ���J�w�V�m�n�� XGBoost �ҫ�
try:
    model = joblib.load("xgboost_rul_model.pkl")
    print("? XGBoost �ҫ��w���\���J")
except Exception as e:
    print(f"? �L�k���J�ҫ�: {e}")

# �w�q��J�ƾڮ榡
class RULInput(BaseModel):
    features: list[float]  # ��J�S�x�ƾڡ]�P�V�m�ɪ��榡�@�P�^

# �w�q API ����
@app.post("/predict/")
async def predict_rul(data: RULInput):
    try:
        # �ˬd��J�ƾڪ���
        if len(data.features) != 38:
            return {"error": "��J�S�x�ƶq���~�A���ӬO 38 �Ӽƭ�"}
            
        # �ഫ��J�ƾڬ� numpy �}�C
        input_data = np.array(data.features).reshape(1, -1)
        
        # �i��w��
        prediction = model.predict(input_data)[0]
        
        return {"predicted_RUL": prediction}
    except Exception as e:
        return {"error": str(e)}
