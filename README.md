# Predictive Maintenance API (RUL Prediction)

## 📌 專案簡介
本專案針對工業設備的預測性維護（Predictive Maintenance），利用機器學習與深度學習技術來預測設備的剩餘使用壽命（RUL）。使用 XGBoost、隨機森林（Random Forest）、卷積神經網絡（CNN） 進行模型訓練，最終 XGBoost 表現最佳。

## 📂 數據集
- NASA CMaps (https://www.kaggle.com/datasets/behrad3d/nasa-cmaps)
- 數據包含多個感測器讀數，可用於分析設備的健康狀況

## 🚀 技術與工具
- **Python**
- **機器學習模型: XGBoost, Random Forest** 
- **深度學習模型: CNN (TensorFlow/Keras)**
- **NumPy & Pandas** - 數據處理
- **Joblib** - 儲存與載入模型

## 📂 專案結構
```
📁 predictive-maintenance-api
│── main.py               # FastAPI 伺服器
│── xgboost_rul_model.pkl # 訓練好的模型
│── requirements.txt      # 依賴套件清單
└── README.md             # 專案說明文件
```

## 🔧 安裝與執行
### 1️⃣ 安裝依賴
```bash
pip install -r requirements.txt
```

### 2️⃣  啟動 FastAPI 伺服器
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

## 🚀 未來改進
✅ 提供更精準的特徵工程  
✅ 增加前端可視化介面  
✅ 優化 CNN 模型表現
