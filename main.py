from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import joblib
import numpy as np
from pydantic import BaseModel
import os

app = FastAPI()

# 🔥 啟用 CORS，允許前端請求 API 🔥
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允許所有網址（正式環境請改成指定網域）
    allow_credentials=True,
    allow_methods=["*"],  # 允許所有 HTTP 方法
    allow_headers=["*"],  # 允許所有請求標頭
)

# 載入 XGBoost 模型
try:
    model = joblib.load("xgboost_rul_model.pkl")
    print("✅ XGBoost 模型已成功載入")
except Exception as e:
    print(f"❌ 無法載入模型: {e}")

# 定義輸入數據格式
class RULInput(BaseModel):
    features: list[float]

@app.get("/")
async def root():
    return {"message": "API 部署成功！請使用 /predict/ 來進行預測"}

@app.post("/predict/")
async def predict_rul(data: RULInput):
    try:
        if len(data.features) != 38:
            return {"error": "輸入特徵數量錯誤，應該是 38 個數值"}
        
        input_data = np.array(data.features).reshape(1, -1)
        prediction = model.predict(input_data)[0]
        return {"predicted_RUL": prediction}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 10000)))  # 預設 10000，但 Render 會改成它的 PORT
