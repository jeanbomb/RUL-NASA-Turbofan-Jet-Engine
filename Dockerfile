# 使用官方 Python 3.8 映像
FROM python:3.8-slim

# 設定工作目錄
WORKDIR /app

# 複製當前目錄所有檔案到容器內的 /app 資料夾
COPY . /app

# 安裝應用所需的依賴
RUN pip install --no-cache-dir -r requirements.txt

# 設定容器啟動命令
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
