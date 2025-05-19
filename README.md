# Predictive Maintenance API (RUL Prediction)  

[日本語](#日本語) | [中文](#中文)

---

## <a name="日本語"></a>日本語

[↑ 頁首へ](#predictive-maintenance-api-rul-prediction)

### 📌 プロジェクト概要
本プロジェクトは産業機器の予知保全（Predictive Maintenance）を目的とし、機械学習と深層学習を用いて残存耐用年数（RUL）を予測します。XGBoost、ランダムフォレスト、CNN（畳み込みニューラルネットワーク）を利用してモデルを構築しています。

### 📂 データセット
- NASA CMaps (https://www.kaggle.com/datasets/behrad3d/nasa-cmaps)
- 複数のセンサーからのデータが含まれており、機器の健全性分析に使用します

### 🚀 技術・ツール
- **Python**
- **機械学習モデル：XGBoost、ランダムフォレスト**
- **深層学習モデル：CNN (TensorFlow/Keras)**
- **NumPy & Pandas** - データ処理
- **Joblib** - モデルの保存と読み込み

### 📂 プロジェクト構成
```
predictive-maintenance-api
│── main.py               # FastAPI サーバー
│── xgboost_rul_model.pkl # 学習済みモデル
│── requirements.txt      # 依存パッケージ
└── README.md             # プロジェクト説明書
```

### 🔧 インストール＆実行

#### 1️⃣ 依存パッケージのインストール
```bash
pip install -r requirements.txt
```

#### 2️⃣ FastAPI サーバーの起動
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

### 🚀 今後の改善
- ✅ より高精度な特徴量エンジニアリングの提供
- ✅ フロントエンド可視化インターフェースの追加
- ✅ CNN モデルの最適化

---

[↑ 頁首へ](#predictive-maintenance-api-rul-prediction)

---

## <a name="中文"></a>中文版

[↑ 回到頁首](#predictive-maintenance-api-rul-prediction)

### 📌 專案簡介
本專案針對工業設備的預測性維護（Predictive Maintenance），利用機器學習與深度學習技術來預測設備的剩餘使用壽命（RUL）。使用 XGBoost、隨機森林（Random Forest）、卷積神經網絡（CNN）進行模型訓練。

### 📂 數據集
- NASA CMaps (https://www.kaggle.com/datasets/behrad3d/nasa-cmaps)
- 數據包含多個感測器讀數，可用於分析設備的健康狀況

### 🚀 技術與工具
- **Python**
- **機器學習模型: XGBoost, Random Forest**
- **深度學習模型: CNN (TensorFlow/Keras)**
- **NumPy & Pandas** - 數據處理
- **Joblib** - 儲存與載入模型

### 📂 專案結構
```
predictive-maintenance-api
│── main.py               # FastAPI 伺服器
│── xgboost_rul_model.pkl # 訓練好的模型
│── requirements.txt      # 依賴套件清單
└── README.md             # 專案說明文件
```

### 🔧 安裝與執行

#### 1️⃣ 安裝依賴
```bash
pip install -r requirements.txt
```

#### 2️⃣  啟動 FastAPI 伺服器
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

### 🚀 未來改進
- ✅ 提供更精準的特徵工程  
- ✅ 增加前端可視化介面  
- ✅ 優化 CNN 模型表現  

---

[↑ 回到頁首](#predictive-maintenance-api-rul-prediction)
