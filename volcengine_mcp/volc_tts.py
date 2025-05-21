import requests
import base64
import uuid
import json
import os
import logging

class VolcTTS:
    def __init__(self, appid, token):
        self.appid = appid
        self.token = token
        self.url = "https://openspeech.bytedance.com/api/v1/tts"

    def synthesize(
        self,
        text,
        voice_type="zh_female_wanqudashu_moon_bigtts",
        encoding="mp3",
        speed_ratio=1.0,
        uid=None,
        cluster="volcano_tts",
        emotion=None,
        enable_emotion=None,
        emotion_scale=None,
        rate=24000,
        bitrate=160,
        loudness_ratio=1.0,
        explicit_language=None,
        context_language=None,
        silence_duration=None,
        with_timestamp=None,
        extra_param=None,
    ):
        reqid = str(uuid.uuid4())
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer;{self.token}",
        }
        audio_config = {
            "voice_type": voice_type,
            "encoding": encoding,
            "speed_ratio": speed_ratio,
            "rate": rate,
            "bitrate": bitrate,
            "loudness_ratio": loudness_ratio,
        }
        if emotion is not None:
            audio_config["emotion"] = emotion
        if enable_emotion is not None:
            audio_config["enable_emotion"] = enable_emotion
        if emotion_scale is not None:
            audio_config["emotion_scale"] = emotion_scale
        if explicit_language is not None:
            audio_config["explicit_language"] = explicit_language
        if context_language is not None:
            audio_config["context_language"] = context_language
        if silence_duration is not None:
            audio_config["silence_duration"] = silence_duration

        body = {
            "app": {
                "appid": self.appid,
                "token": self.token,
                "cluster": cluster,
            },
            "user": {
                "uid": uid,
            },
            "audio": audio_config,
            "request": {
                "reqid": reqid,
                "text": text,
                "operation": "query",
            },
        }
        if with_timestamp is not None:
            body["request"]["with_timestamp"] = with_timestamp
        if extra_param is not None:
            body["request"]["extra_param"] = extra_param

        resp = requests.post(self.url, headers=headers, data=json.dumps(body))
        #print('请求body:', json.dumps(body, ensure_ascii=False))
        logging.basicConfig(filename='tts_debug.log', level=logging.INFO)
        #logging.info('请求body: %s', json.dumps(body, ensure_ascii=False))
        try:
            resp.raise_for_status()
        except Exception as e:
            #print('接口返回内容:', resp.text)
            raise
        #print('接口返回内容:', resp.text)
        result = resp.json()
        if result.get("code") == 3000:
            audio_base64 = result["data"]
            audio_bytes = base64.b64decode(audio_base64)
            return audio_bytes
        else:
            raise Exception(f"TTS Error: {result.get('message', 'Unknown error')}, code: {result.get('code')}") 