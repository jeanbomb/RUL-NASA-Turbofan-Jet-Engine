from fastapi import FastAPI
import joblib
import numpy as np
from pydantic import BaseModel

# 初始化 FastAPI 應用
app = FastAPI()

# 載入已訓練好的 XGBoost 模型
try:
    model = joblib.load("xgboost_rul_model.pkl")
    print("? XGBoost 模型已成功載入")
except Exception as e:
    print(f"? 無法載入模型: {e}")

# 定義輸入數據格式
class RULInput(BaseModel):
    features: list[float]  # 輸入特徵數據（與訓練時的格式一致）

# 定義 API 路由
@app.post("/predict/")
async def predict_rul(data: RULInput):
    try:
        # 檢查輸入數據長度
        if len(data.features) != 38:
            return {"error": "輸入特徵數量錯誤，應該是 38 個數值"}
            
        # 轉換輸入數據為 numpy 陣列
        input_data = np.array(data.features).reshape(1, -1)
        
        # 進行預測
        prediction = model.predict(input_data)[0]
        
        return {"predicted_RUL": prediction}
    except Exception as e:
        return {"error": str(e)}
