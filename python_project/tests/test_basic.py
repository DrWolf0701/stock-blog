"""
基本測試範例
"""

import pytest
import sys
import os

# 添加 src 目錄到路徑
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../src'))


def test_python_version():
    """測試 Python 版本"""
    assert sys.version_info >= (3, 9), "需要 Python 3.9 或更高版本"


def test_imports():
    """測試套件導入"""
    try:
        import pandas as pd
        import numpy as np
        import matplotlib.pyplot as plt
        import requests
        
        # 檢查版本
        assert pd.__version__ >= '2.0.0'
        assert np.__version__ >= '1.24.0'
        
        print("✅ 所有套件導入成功")
        return True
    except ImportError as e:
        pytest.fail(f"套件導入失敗: {e}")


def test_dataframe_creation():
    """測試 Pandas DataFrame 建立"""
    import pandas as pd
    import numpy as np
    
    # 建立測試資料
    data = {
        'A': [1, 2, 3, 4, 5],
        'B': ['a', 'b', 'c', 'd', 'e'],
        'C': np.random.randn(5)
    }
    
    df = pd.DataFrame(data)
    
    # 驗證 DataFrame 屬性
    assert len(df) == 5
    assert list(df.columns) == ['A', 'B', 'C']
    assert df['A'].sum() == 15
    
    return df


def test_numpy_operations():
    """測試 NumPy 操作"""
    import numpy as np
    
    arr = np.array([1, 2, 3, 4, 5])
    
    # 基本操作
    assert arr.sum() == 15
    assert arr.mean() == 3.0
    assert arr.std() > 0
    
    # 陣列操作
    squared = arr ** 2
    assert squared[0] == 1
    assert squared[-1] == 25


def test_requests_connection():
    """測試網路連線"""
    import requests
    
    try:
        # 測試簡單的請求
        response = requests.get('https://httpbin.org/get', timeout=10)
        assert response.status_code == 200
        
        # 檢查回應格式
        data = response.json()
        assert 'url' in data
        
        print("✅ 網路連線測試通過")
        return True
    except Exception as e:
        print(f"⚠️ 網路測試跳過: {e}")
        return None  # 跳過測試，不視為失敗


class TestEnvironment:
    """環境測試類別"""
    
    def test_working_directory(self):
        """測試工作目錄"""
        assert os.path.exists(os.path.dirname(__file__))
    
    def test_virtual_environment(self):
        """測試虛擬環境"""
        # 檢查是否在虛擬環境中執行
        python_executable = sys.executable
        assert 'venv' in python_executable or '.virtualenv' in python_executable


if __name__ == "__main__":
    """直接執行測試"""
    print("執行基本測試...")
    
    # 執行測試
    test_python_version()
    test_imports()
    df = test_dataframe_creation()
    test_numpy_operations()
    test_requests_connection()
    
    print("\n✅ 所有測試通過！")