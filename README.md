---

## 项目简介

本项目旨在将火山引擎TTS官方API封装为标准MCP协议工具，支持在 Cursor、Claude 等平台通过自然语言参数调用，实现一键语音合成。适用于需要自定义音色、参数映射、自动化批量语音生成的开发者场景。

---

# doubao_tts_mcp 使用说明

## 快速开始

### 0. 克隆项目代码

```bash
git clone https://github.com/你的用户名/doubao_tts_mcp.git
cd doubao_tts_mcp
```

## Python环境准备

- 本项目需 Python 3.8 及以上版本。
- 推荐使用 [Python官网](https://www.python.org/downloads/) 下载并安装最新版。
- 安装完成后，命令行输入 `python --version` 或 `python3 --version` 检查版本。
- 建议使用虚拟环境：
  ```bash
  python -m venv .venv
  source .venv/bin/activate  # Linux/macOS
  .venv\Scripts\activate    # Windows
  ```

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 安装本地包（支持命令行调用）

```bash
pip install -e .
```

### 3. 配置环境变量

可在 `.env` 或 `mcp.json` 的 `env` 字段中设置：
（获取方式：https://console.volcengine.com/speech/service/10007）
- VOLC_APPID
- VOLC_TOKEN
- PORT（如需自定义端口）
- OUTPUT_DIR（音频输出目录）

### 4. 命令行启动服务

```bash
doubao-tts-mcp
```

### 5. cursor mcp.json 配置示例

```json
{
  "mcpServers": {
    "doubao_tts_mcp": {
      "command": "doubao-tts-mcp",
      "args": [],
      "env": {
        "VOLC_APPID": "你的appid",
        "VOLC_TOKEN": "你的token",
        "PORT": "5001",
        "OUTPUT_DIR": "D:/doubao_tts_mcp/output"
      }
    }
  }
}
```

### 6. 在 Cursor/Claude 等平台使用

- 平台会自动读取 mcp.json 并用命令行方式启动 MCP 服务。
- 在 MCP 面板填写参数即可一键合成音频。
- 合成结果会返回音频文件的绝对路径，文件保存在指定目录下。

### 7. 常见问题

- **Q：如何让 MCP 工具支持命令行调用？**
  - A：请确保 pyproject.toml 配置了 entry_points，并用 pip install -e . 安装本地包。
- **Q：比特率及采样率无法调整？**
  - A：由于 MCP 工具 schema 类型校验限制，bitrate 和 rate 参数暂不可用，建议用默认值。
- **Q：音色、情感、语速等参数如何填写？**
  - A：支持自然语言关键词（如"少女""萝莉"），会自动智能映射到官方音色。

---

## 示例调用

```json
{
  "text": "测试声音参数",
  "voice_type": "少女",
  "speed_ratio": 0.8,
  "emotion": "happy",
  "output_filename": "少女音色测试"
}
```

---

如需开发细节、扩展说明，请参考 doubao-tts-api-with-mcp-flow.md。

## 参考
- [火山引擎语音合成API文档](https://www.volcengine.com/docs/6561/1257584)
- [Model Context Protocol Python SDK](https://github.com/modelcontextprotocol/python-sdk) 