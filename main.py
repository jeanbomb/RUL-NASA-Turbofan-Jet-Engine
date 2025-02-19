from fastapi import FastAPI
import joblib
import numpy as np
from pydantic import BaseModel
from typing import List

# 初始化 FastAPI 應用
app = FastAPI()

# 嘗試載入已訓練好的 XGBoost 模型
try:
    model = joblib.load("xgboost_rul_model.pkl")
    print("✅ XGBoost 模型已成功載入")
except Exception as e:
    model = None
    print(f"❌ 無法載入模型: {e}")

# 定義輸入數據格式
class RULInput(BaseModel):
    features: List[float]  # 確保輸入是數值列表

# 定義 API 路由
@app.get("/")
async def root():
    return {"message": "API 部署成功！請使用 /predict/ 來進行預測"}

@app.post("/predict/")
async def predict_rul(data: RULInput):
    if model is None:
        return {"error": "模型未載入，請檢查模型檔案是否存在"}

    if len(data.features) != 38:
        return {"error": "輸入特徵數量錯誤，應該是 38 個數值"}
    
    try:
        input_data = np.array(data.features).reshape(1, -1)
        prediction = model.predict(input_data)[0]
        return {"predicted_RUL": float(prediction)}
    except Exception as e:
        return {"error": str(e)}
