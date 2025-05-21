import sys
import os
import pytest
import asyncio
import re
from mcp.client.streamable_http import streamablehttp_client
from mcp import ClientSession

@pytest.mark.asyncio
@pytest.mark.skipif(
    not (os.getenv("VOLC_APPID") and os.getenv("VOLC_TOKEN")),
    reason="需要配置VOLC_APPID和VOLC_TOKEN环境变量"
)
async def test_mcp_server_tool(monkeypatch):
    async with streamablehttp_client("http://localhost:5001/mcp") as (read, write, _):
        async with ClientSession(read, write) as session:
            await session.initialize()
            result = await session.call_tool(
                "volcengine_tts",
                arguments={
                    "text": "MCP工具端到端测试。",
                    "voice_type": "zh_female_wanqudashu_moon_bigtts",
                    "encoding": "mp3",
                    "speed_ratio": 1.0
                }
            )
            print('result:', result)
            print('dir:', dir(result))
            print('dict:', getattr(result, '__dict__', None))
            assert "合成成功" in result.content[0].text
            assert ".mp3" in result.content[0].text
            # 提取音频文件名并判断文件是否存在
            match = re.search(r"volc_tts_\d+\.mp3", result.content[0].text)
            assert match is not None
            assert os.path.exists(match.group(0))