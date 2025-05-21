import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from volcengine_mcp.volc_tts import VolcTTS

@pytest.mark.skipif(
    not (os.getenv("VOLC_APPID") and os.getenv("VOLC_TOKEN")),
    reason="需要配置VOLC_APPID和VOLC_TOKEN环境变量"
)
def test_synthesize_basic():
    appid = os.getenv("VOLC_APPID")
    token = os.getenv("VOLC_TOKEN")
    tts = VolcTTS(appid, token)
    text = "你好，欢迎使用火山引擎语音合成测试。"
    audio = tts.synthesize(text)
    assert isinstance(audio, bytes)
    assert len(audio) > 1000
    # 可选：保存音频文件，人工试听
    with open("test_output.mp3", "wb") as f:
        f.write(audio)