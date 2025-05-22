# server.py
import sys
#print("当前Python路径：", sys.executable)
import os
from mcp.server.fastmcp import FastMCP
from volcengine_mcp.volc_tts import VolcTTS
from dotenv import load_dotenv
from mcp.types import TextContent
from volcengine_mcp.config import get_voice_type, VOICE_LIST
from typing import Optional
import uuid

load_dotenv()

VOLC_APPID = os.getenv("VOLC_APPID")
VOLC_TOKEN = os.getenv("VOLC_TOKEN")
#print("VOLC_APPID:", VOLC_APPID)
#print("VOLC_TOKEN:", VOLC_TOKEN)
tts_client = VolcTTS(VOLC_APPID, VOLC_TOKEN)

mcp = FastMCP("VolcEngineTTS")

#print("准备注册 volcengine_tts 工具")
@mcp.tool(
    description="""
    将文本转为语音并保存为音频文件，支持所有火山引擎TTS参数。
    支持自然语言描述音色，如"青年男声""甜美女声"等。

    参数说明：
        text (str): 要合成的文本内容。
        voice_type (str, 可选): 使用的音色名称，默认为官方女声。
        encoding (str, 可选): 音频编码格式，默认为mp3。
        speed_ratio (float, 可选): 语速，1.0为正常语速。
        uid (str, 可选): 用户ID，默认uid123。
        cluster (str, 可选): 集群，默认volcano_tts。
        emotion (str, 可选): 情感标签。
        enable_emotion (bool, 可选): 是否启用情感。
        emotion_scale (float, 可选): 情感强度。
        rate (int, 可选): 采样率，默认24000。
        bitrate (int, 可选): 比特率，默认160。
        loudness_ratio (float, 可选): 响度，默认1.0。
        explicit_language (str, 可选): 明确语言。
        context_language (str, 可选): 上下文语言。
        silence_duration (float, 可选): 静音时长。
        with_timestamp (bool, 可选): 是否返回时间戳。
        extra_param (dict, 可选): 额外参数。
        output_dir (str, 可选): 音频文件保存目录，优先级高于环境变量 OUTPUT_DIR，默认当前目录。
        output_filename (str, 可选): 自定义音频文件名（无需扩展名），如不指定则自动生成唯一文件名。

    返回：
        TextContent，包含合成成功提示和音频文件路径。

    English:
    Convert text to speech with a given voice and save the output audio file to a given directory.
    Directory is optional, if not provided, the output file will be saved to the current working directory.

    Args:
        text (str): The text to convert to speech.
        voice_type (str, optional): The name of the voice to use.
        encoding (str, optional): Output audio encoding, default is mp3.
        speed_ratio (float, optional): Speed of the generated audio. 1.0 is normal speed.
        uid (str, optional): User ID, default is uid123.
        cluster (str, optional): Cluster, default is volcano_tts.
        emotion (str, optional): Emotion tag.
        enable_emotion (bool, optional): Whether to enable emotion.
        emotion_scale (float, optional): Emotion intensity.
        rate (int, optional): Sampling rate, default is 24000.
        bitrate (int, optional): Bitrate, default is 160.
        loudness_ratio (float, optional): Loudness, default is 1.0.
        explicit_language (str, optional): Explicit language.
        context_language (str, optional): Context language.
        silence_duration (float, optional): Silence duration.
        with_timestamp (bool, optional): Whether to return timestamp.
        extra_param (dict, optional): Extra parameters.
        output_dir (str, optional): Directory to save the output audio file. Priority: argument > env OUTPUT_DIR > current dir.
        output_filename (str, optional): Custom audio file name (no extension needed). If not specified, a unique file name will be generated.

    Returns:
        Text content with the path to the output file and name of the voice used.
    """
)
def volcengine_tts(
    text: str,
    voice_type: Optional[str] = "zh_female_wanqudashu_moon_bigtts",
    encoding: Optional[str] = "mp3",
    speed_ratio: Optional[float] = 1.0,
    uid: Optional[str] = None,
    cluster: Optional[str] = "volcano_tts",
    emotion: Optional[str] = None,
    enable_emotion: Optional[bool] = None,
    emotion_scale: Optional[float] = None,
    rate: Optional[int] = 24000,
    bitrate: Optional[int] = 160,
    loudness_ratio: Optional[float] = 1.0,
    explicit_language: Optional[str] = None,
    context_language: Optional[str] = None,
    silence_duration: Optional[float] = None,
    with_timestamp: Optional[bool] = None,
    extra_param: Optional[dict] = None,
    output_dir: Optional[str] = None,
    output_filename: Optional[str] = None
) -> TextContent:
    """调用火山引擎语音合成，将文本转为语音mp3，返回音频文件路径"""
    # 类型安全：所有 int 类型参数都强制转为 int
    if rate is not None:
        rate = int(rate)
    if bitrate is not None:
        bitrate = int(bitrate)
    # 使用config.py的get_voice_type进行音色解析
    #print("volcengine_tts 被调用")
    #print(f"调用 synthesize, text={text}, voice_type={voice_type}")
    voice_type = get_voice_type(voice_type)
    #print('映射后voice_type:', voice_type)
    if not uid or uid is None:
        uid = str(uuid.uuid4())
    audio_bytes = tts_client.synthesize(
        text,
        voice_type=voice_type,
        encoding=encoding,
        speed_ratio=speed_ratio,
        uid=uid,
        cluster=cluster,
        emotion=emotion,
        enable_emotion=enable_emotion,
        emotion_scale=emotion_scale,
        rate=rate,
        bitrate=bitrate,
        loudness_ratio=loudness_ratio,
        explicit_language=explicit_language,
        context_language=context_language,
        silence_duration=silence_duration,
        with_timestamp=with_timestamp,
        extra_param=extra_param
    )
    # 优先用参数，其次用环境变量，最后用当前目录
    if not output_dir:
        output_dir = os.getenv("OUTPUT_DIR", os.getcwd())
    os.makedirs(output_dir, exist_ok=True)
    import time
    if output_filename:
        filename = output_filename
        if not filename.endswith(f".{encoding}"):
            filename += f".{encoding}"
    else:
        filename = f"volc_tts_{int(time.time())}_{uuid.uuid4().hex[:8]}.{encoding}"
    out_path = os.path.join(output_dir, filename)
    with open(out_path, "wb") as f:
        f.write(audio_bytes)
    return TextContent(
        type="text",
        text=f"合成成功，音频文件路径：{out_path}"
    )

@mcp.tool(
    description="""
    获取所有可用的火山引擎TTS音色列表。
    返回：
        List[dict]，每个元素包含音色的scene、desc、voice_type、lang、emotions、keywords等信息。
    """
)
def list_voice() -> list:
    """返回所有可用音色信息列表"""
    return VOICE_LIST

def main():
    mcp.run()
#print("准备启动 MCP 服务")
if __name__ == "__main__":
    #mcp.run(transport="streamable-http")
    main()
    #print("MCP 服务已启动")
