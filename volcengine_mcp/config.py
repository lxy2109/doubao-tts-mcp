# volcengine_mcp/config.py
# 火山引擎TTS音色映射配置（自动生成，结构化）

VOICE_LIST = [
    # ====== 多情感 ======
    {"scene": "多情感", "desc": "北京小爷（多情感）", "voice_type": "zh_male_beijingxiaoye_emo_v2_mars_bigtts", "lang": "中文", "emotions": ["angry", "surprised", "fear", "excited", "coldness", "neutral"], "keywords": ["北京小爷", "多情感", "男声", "情感", "中文"]},
    {"scene": "多情感", "desc": "柔美女友（多情感）", "voice_type": "zh_female_roumeinvyou_emo_v2_mars_bigtts", "lang": "中文", "emotions": ["happy", "sad", "angry", "surprised", "fear", "hate", "excited", "coldness", "neutral"], "keywords": ["柔美女友", "多情感", "女声", "女友", "情感", "中文"]},
    {"scene": "多情感", "desc": "阳光青年（多情感）", "voice_type": "zh_male_yangguangqingnian_emo_v2_mars_bigtts", "lang": "中文", "emotions": ["happy", "sad", "angry", "fear", "excited", "coldness", "neutral"], "keywords": ["阳光青年", "多情感", "男声", "青年", "情感", "中文"]},
    {"scene": "多情感", "desc": "魅力女友（多情感）", "voice_type": "zh_female_meilinvyou_emo_v2_mars_bigtts", "lang": "中文", "emotions": ["sad", "fear", "neutral"], "keywords": ["魅力女友", "多情感", "女声", "女友", "情感", "中文"]},
    {"scene": "多情感", "desc": "爽快思思（多情感）", "voice_type": "zh_female_shuangkuaisisi_emo_v2_mars_bigtts", "lang": "中文, 美式英语", "emotions": ["happy", "sad", "angry", "surprised", "excited", "coldness", "neutral"], "keywords": ["爽快思思", "多情感", "女声", "思思", "情感", "中文", "美式英语"]},
    # ====== 通用场景 ======
    {"scene": "通用场景", "desc": "灿灿/Shiny", "voice_type": "zh_female_cancan_mars_bigtts", "lang": "中文, 美式英语", "emotions": [], "keywords": ["灿灿", "Shiny", "通用场景", "女声", "中文", "美式英语"]},
    {"scene": "通用场景", "desc": "清新女声", "voice_type": "zh_female_qingxinnvsheng_mars_bigtts", "lang": "中文", "emotions": [], "keywords": ["清新女声", "通用场景", "女声", "中文"]},
    {"scene": "通用场景", "desc": "爽快思思/Skye", "voice_type": "zh_female_shuangkuaisisi_moon_bigtts", "lang": "中文, 美式英语", "emotions": [], "keywords": ["爽快思思", "Skye", "通用场景", "女声", "思思", "中文", "美式英语"]},
    {"scene": "通用场景", "desc": "温暖阿虎/Alvin", "voice_type": "zh_male_wennuanahu_moon_bigtts", "lang": "中文, 美式英语", "emotions": [], "keywords": ["温暖阿虎", "Alvin", "通用场景", "男声", "阿虎", "中文", "美式英语"]},
    {"scene": "通用场景", "desc": "少年梓辛/Brayan", "voice_type": "zh_male_shaonianzixin_moon_bigtts", "lang": "中文, 美式英语", "emotions": [], "keywords": ["少年梓辛", "Brayan", "通用场景", "男声", "梓辛", "中文", "美式英语"]},
    {"scene": "通用场景", "desc": "知性女声", "voice_type": "zh_female_zhixingnvsheng_mars_bigtts", "lang": "中文", "emotions": [], "keywords": ["知性女声", "通用场景", "女声", "中文"]},
    {"scene": "通用场景", "desc": "清爽男大", "voice_type": "zh_male_qingshuangnanda_mars_bigtts", "lang": "中文", "emotions": [], "keywords": ["清爽男大", "通用场景", "男声", "中文"]},
    {"scene": "通用场景", "desc": "邻家女孩", "voice_type": "zh_female_linjianvhai_moon_bigtts", "lang": "中文", "emotions": [], "keywords": ["邻家女孩", "通用场景", "女声", "中文"]},
    {"scene": "通用场景", "desc": "渊博小叔", "voice_type": "zh_male_yuanboxiaoshu_moon_bigtts", "lang": "中文", "emotions": [], "keywords": ["渊博小叔", "通用场景", "男声", "中文"]},
    {"scene": "通用场景", "desc": "阳光青年", "voice_type": "zh_male_yangguangqingnian_moon_bigtts", "lang": "中文", "emotions": [], "keywords": ["阳光青年", "通用场景", "男声", "青年", "中文"]},
    {"scene": "通用场景", "desc": "甜美小源", "voice_type": "zh_female_tianmeixiaoyuan_moon_bigtts", "lang": "中文", "emotions": [], "keywords": ["甜美小源", "通用场景", "女声", "小源", "中文"]},
    {"scene": "通用场景", "desc": "清澈梓梓", "voice_type": "zh_female_qingchezizi_moon_bigtts", "lang": "中文", "emotions": [], "keywords": ["清澈梓梓", "通用场景", "女声", "梓梓", "中文"]},
    {"scene": "通用场景", "desc": "解说小明", "voice_type": "zh_male_jieshuoxiaoming_moon_bigtts", "lang": "中文", "emotions": [], "keywords": ["解说小明", "通用场景", "男声", "小明", "中文"]},
    {"scene": "通用场景", "desc": "开朗姐姐", "voice_type": "zh_female_kailangjiejie_moon_bigtts", "lang": "中文", "emotions": [], "keywords": ["开朗姐姐", "通用场景", "女声", "姐姐", "中文"]},
    {"scene": "通用场景", "desc": "邻家男孩", "voice_type": "zh_male_linjiananhai_moon_bigtts", "lang": "中文", "emotions": [], "keywords": ["邻家男孩", "通用场景", "男声", "中文"]},
    {"scene": "通用场景", "desc": "甜美悦悦", "voice_type": "zh_female_tianmeiyueyue_moon_bigtts", "lang": "中文", "emotions": [], "keywords": ["甜美悦悦", "通用场景", "女声", "悦悦", "中文"]},
    {"scene": "通用场景", "desc": "心灵鸡汤", "voice_type": "zh_female_xinlingjitang_moon_bigtts", "lang": "中文", "emotions": [], "keywords": ["心灵鸡汤", "通用场景", "女声", "中文"]},
    {"scene": "通用场景", "desc": "知性温婉", "voice_type": "ICL_zh_female_zhixingwenwan_tob", "lang": "中文", "emotions": [], "keywords": ["知性温婉", "通用场景", "女声", "中文"]},
    {"scene": "通用场景", "desc": "暖心体贴", "voice_type": "ICL_zh_male_nuanxintitie_tob", "lang": "中文", "emotions": [], "keywords": ["暖心体贴", "通用场景", "男声", "中文"]},
    {"scene": "通用场景", "desc": "温柔文雅", "voice_type": "ICL_zh_female_wenrouwenya_tob", "lang": "中文", "emotions": [], "keywords": ["温柔文雅", "通用场景", "女声", "中文"]},
    {"scene": "通用场景", "desc": "开朗轻快", "voice_type": "ICL_zh_male_kailangqingkuai_tob", "lang": "中文", "emotions": [], "keywords": ["开朗轻快", "通用场景", "男声", "中文"]},
    {"scene": "通用场景", "desc": "活泼爽朗", "voice_type": "ICL_zh_male_huoposhuanglang_tob", "lang": "中文", "emotions": [], "keywords": ["活泼爽朗", "通用场景", "男声", "中文"]},
    {"scene": "通用场景", "desc": "率真小伙", "voice_type": "ICL_zh_male_shuaizhenxiaohuo_tob", "lang": "中文", "emotions": [], "keywords": ["率真小伙", "通用场景", "男声", "中文"]},
    {"scene": "通用场景", "desc": "温柔小哥", "voice_type": "zh_male_wenrouxiaoge_mars_bigtts", "lang": "中文", "emotions": [], "keywords": ["温柔小哥", "通用场景", "男声", "中文"]},
    # ====== 多语种 ======
    {"scene": "多语种", "desc": "Smith", "voice_type": "en_male_smith_mars_bigtts", "lang": "英式英语", "emotions": [], "keywords": ["Smith", "多语种", "男声", "英语", "英式英语"]},
    {"scene": "多语种", "desc": "Anna", "voice_type": "en_female_anna_mars_bigtts", "lang": "英式英语", "emotions": [], "keywords": ["Anna", "多语种", "女声", "英语", "英式英语"]},
    {"scene": "多语种", "desc": "Adam", "voice_type": "en_male_adam_mars_bigtts", "lang": "美式英语", "emotions": [], "keywords": ["Adam", "多语种", "男声", "英语", "美式英语"]},
    {"scene": "多语种", "desc": "Sarah", "voice_type": "en_female_sarah_mars_bigtts", "lang": "澳洲英语", "emotions": [], "keywords": ["Sarah", "多语种", "女声", "英语", "澳洲英语"]},
    {"scene": "多语种", "desc": "Dryw", "voice_type": "en_male_dryw_mars_bigtts", "lang": "澳洲英语", "emotions": [], "keywords": ["Dryw", "多语种", "男声", "英语", "澳洲英语"]},
    {"scene": "多语种", "desc": "かずね（和音）/Javier or Álvaro", "voice_type": "multi_male_jingqiangkanye_moon_bigtts", "lang": "日语, 西语", "emotions": [], "keywords": ["かずね", "和音", "Javier", "Álvaro", "多语种", "男声", "日语", "西语"]},
    {"scene": "多语种", "desc": "はるこ（晴子）/Esmeralda", "voice_type": "multi_female_shuangkuaisisi_moon_bigtts", "lang": "日语, 西语", "emotions": [], "keywords": ["はるこ", "晴子", "Esmeralda", "多语种", "女声", "日语", "西语"]},
    {"scene": "多语种", "desc": "ひろし（広志）/Roberto", "voice_type": "multi_male_wanqudashu_moon_bigtts", "lang": "日语, 西语", "emotions": [], "keywords": ["ひろし", "広志", "Roberto", "多语种", "男声", "日语", "西语"]},
    {"scene": "多语种", "desc": "あけみ（朱美）", "voice_type": "multi_female_gaolengyujie_moon_bigtts", "lang": "日语", "emotions": [], "keywords": ["あけみ", "朱美", "多语种", "女声", "日语"]},
    {"scene": "多语种", "desc": "Amanda", "voice_type": "en_female_amanda_mars_bigtts", "lang": "美式英语", "emotions": [], "keywords": ["Amanda", "多语种", "女声", "英语", "美式英语"]},
    {"scene": "多语种", "desc": "Jackson", "voice_type": "en_male_jackson_mars_bigtts", "lang": "美式英语", "emotions": [], "keywords": ["Jackson", "多语种", "男声", "英语", "美式英语"]},
    # ====== 趣味口音 ======
    {"scene": "趣味口音", "desc": "京腔侃爷/Harmony", "voice_type": "zh_male_jingqiangkanye_moon_bigtts", "lang": "中文-北京口音, 英文", "emotions": [], "keywords": ["京腔侃爷", "Harmony", "趣味口音", "男声", "北京口音", "英文"]},
    {"scene": "趣味口音", "desc": "湾湾小何", "voice_type": "zh_female_wanwanxiaohe_moon_bigtts", "lang": "中文-台湾口音", "emotions": [], "keywords": ["湾湾小何", "趣味口音", "女声", "台湾口音"]},
    {"scene": "趣味口音", "desc": "湾区大叔", "voice_type": "zh_female_wanqudashu_moon_bigtts", "lang": "中文-广东口音", "emotions": [], "keywords": ["湾区大叔", "趣味口音", "女声", "广东口音"]},
    {"scene": "趣味口音", "desc": "呆萌川妹", "voice_type": "zh_female_daimengchuanmei_moon_bigtts", "lang": "中文-四川口音", "emotions": [], "keywords": ["呆萌川妹", "趣味口音", "女声", "四川口音"]},
    {"scene": "趣味口音", "desc": "广州德哥", "voice_type": "zh_male_guozhoudege_moon_bigtts", "lang": "中文-广东口音", "emotions": [], "keywords": ["广州德哥", "趣味口音", "男声", "广东口音"]},
    {"scene": "趣味口音", "desc": "北京小爷", "voice_type": "zh_male_beijingxiaoye_moon_bigtts", "lang": "中文-北京口音", "emotions": [], "keywords": ["北京小爷", "趣味口音", "男声", "北京口音"]},
    {"scene": "趣味口音", "desc": "浩宇小哥", "voice_type": "zh_male_haoyuxiaoge_moon_bigtts", "lang": "中文-青岛口音", "emotions": [], "keywords": ["浩宇小哥", "趣味口音", "男声", "青岛口音"]},
    {"scene": "趣味口音", "desc": "广西远舟", "voice_type": "zh_male_guangxiyuanzhou_moon_bigtts", "lang": "中文-广西口音", "emotions": [], "keywords": ["广西远舟", "趣味口音", "男声", "广西口音"]},
    {"scene": "趣味口音", "desc": "妹抖洁儿", "voice_type": "zh_female_meitoujieer_moon_bigtts", "lang": "中文-长沙口音", "emotions": [], "keywords": ["妹抖洁儿", "趣味口音", "女声", "长沙口音"]},
    {"scene": "趣味口音", "desc": "豫州子轩", "voice_type": "zh_male_yuzhouzixuan_moon_bigtts", "lang": "中文-河南口音", "emotions": [], "keywords": ["豫州子轩", "趣味口音", "男声", "河南口音"]},
    # ====== 角色扮演 ======
    {"scene": "角色扮演", "desc": "奶气萌娃", "voice_type": "zh_male_naiqimengwa_mars_bigtts", "lang": "中文", "emotions": [], "keywords": ["奶气萌娃", "角色扮演", "中文", "zh_male_naiqimengwa_mars_bigtts"]},
    {"scene": "角色扮演", "desc": "婆婆", "voice_type": "zh_female_popo_mars_bigtts", "lang": "中文", "emotions": [], "keywords": ["婆婆", "角色扮演", "中文", "zh_female_popo_mars_bigtts"]},
    {"scene": "角色扮演", "desc": "高冷御姐", "voice_type": "zh_female_gaolengyujie_moon_bigtts", "lang": "中文", "emotions": [], "keywords": ["高冷御姐", "角色扮演", "中文", "zh_female_gaolengyujie_moon_bigtts"]},
    {"scene": "角色扮演", "desc": "傲娇霸总", "voice_type": "zh_male_aojiaobazong_moon_bigtts", "lang": "中文", "emotions": [], "keywords": ["傲娇霸总", "角色扮演", "中文", "zh_male_aojiaobazong_moon_bigtts"]},
    {"scene": "角色扮演", "desc": "魅力女友", "voice_type": "zh_female_meilinvyou_moon_bigtts", "lang": "中文", "emotions": [], "keywords": ["魅力女友", "角色扮演", "中文", "zh_female_meilinvyou_moon_bigtts"]},
    {"scene": "角色扮演", "desc": "深夜博客", "voice_type": "zh_male_shenyeboke_moon_bigtts", "lang": "中文", "emotions": [], "keywords": ["深夜博客", "角色扮演", "中文", "zh_male_shenyeboke_moon_bigtts"]},
    {"scene": "角色扮演", "desc": "柔美女友", "voice_type": "zh_female_sajiaonvyou_moon_bigtts", "lang": "中文", "emotions": [], "keywords": ["柔美女友", "角色扮演", "中文", "zh_female_sajiaonvyou_moon_bigtts"]},
    {"scene": "角色扮演", "desc": "撒娇学妹", "voice_type": "zh_female_yuanqinjnyou_moon_bigtts", "lang": "中文", "emotions": [], "keywords": ["撒娇学妹", "角色扮演", "中文", "zh_female_yuanqinjnyou_moon_bigtts"]},
    {"scene": "角色扮演", "desc": "病弱少女", "voice_type": "ICL_zh_female_bingruoshaonv_tob", "lang": "中文", "emotions": [], "keywords": ["病弱少女", "角色扮演", "中文", "ICL_zh_female_bingruoshaonv_tob"]},
    {"scene": "角色扮演", "desc": "活泼女孩", "voice_type": "ICL_zh_female_huoponvhai_tob", "lang": "中文", "emotions": [], "keywords": ["活泼女孩", "角色扮演", "中文", "ICL_zh_female_huoponvhai_tob"]},
    {"scene": "角色扮演", "desc": "东方浩然", "voice_type": "zh_male_dongfanghaoran_moon_bigtts", "lang": "中文", "emotions": [], "keywords": ["东方浩然", "角色扮演", "中文", "zh_male_dongfanghaoran_moon_bigtts"]},
    {"scene": "角色扮演", "desc": "绿茶小哥", "voice_type": "ICL_zh_male_lvchaxiaoge_tob", "lang": "中文", "emotions": [], "keywords": ["绿茶小哥", "角色扮演", "中文", "ICL_zh_male_lvchaxiaoge_tob"]},
    {"scene": "角色扮演", "desc": "娇弱萝莉", "voice_type": "ICL_zh_female_jiaoruoluoli_tob", "lang": "中文", "emotions": [], "keywords": ["娇弱萝莉", "角色扮演", "中文", "ICL_zh_female_jiaoruoluoli_tob"]},
    {"scene": "角色扮演", "desc": "冷淡琉璃", "voice_type": "ICL_zh_male_lengdanshuil_tob", "lang": "中文", "emotions": [], "keywords": ["冷淡琉璃", "角色扮演", "中文", "ICL_zh_male_lengdanshuil_tob"]},
    {"scene": "角色扮演", "desc": "憨厚敦实", "voice_type": "ICL_zh_male_hanhoudunshi_tob", "lang": "中文", "emotions": [], "keywords": ["憨厚敦实", "角色扮演", "中文", "ICL_zh_male_hanhoudunshi_tob"]},
    {"scene": "角色扮演", "desc": "傲气凌人", "voice_type": "ICL_zh_male_aiqilangren_tob", "lang": "中文", "emotions": [], "keywords": ["傲气凌人", "角色扮演", "中文", "ICL_zh_male_aiqilangren_tob"]},
    {"scene": "角色扮演", "desc": "活泼刁蛮", "voice_type": "ICL_zh_female_huopodiaoman_tob", "lang": "中文", "emotions": [], "keywords": ["活泼刁蛮", "角色扮演", "中文", "ICL_zh_female_huopodiaoman_tob"]},
    {"scene": "角色扮演", "desc": "固执病娇", "voice_type": "ICL_zh_male_guzhibingjiao_tob", "lang": "中文", "emotions": [], "keywords": ["固执病娇", "角色扮演", "中文", "ICL_zh_male_guzhibingjiao_tob"]},
    {"scene": "角色扮演", "desc": "撒娇粘人", "voice_type": "ICL_zh_male_sajiaonianren_tob", "lang": "中文", "emotions": [], "keywords": ["撒娇粘人", "角色扮演", "中文", "ICL_zh_male_sajiaonianren_tob"]},
    {"scene": "角色扮演", "desc": "傲慢娇声", "voice_type": "ICL_zh_female_aomanjiaosheng_tob", "lang": "中文", "emotions": [], "keywords": ["傲慢娇声", "角色扮演", "中文", "ICL_zh_female_aomanjiaosheng_tob"]},
    {"scene": "角色扮演", "desc": "潇洒随性", "voice_type": "ICL_zh_male_xiaosasuixing_tob", "lang": "中文", "emotions": [], "keywords": ["潇洒随性", "角色扮演", "中文", "ICL_zh_male_xiaosasuixing_tob"]},
    {"scene": "角色扮演", "desc": "腹黑公子", "voice_type": "ICL_zh_male_fuheigongzi_tob", "lang": "中文", "emotions": [], "keywords": ["腹黑公子", "角色扮演", "中文", "ICL_zh_male_fuheigongzi_tob"]},
    {"scene": "角色扮演", "desc": "诡异神秘", "voice_type": "ICL_zh_male_guiyishenmi_tob", "lang": "中文", "emotions": [], "keywords": ["诡异神秘", "角色扮演", "中文", "ICL_zh_male_guiyishenmi_tob"]},
    {"scene": "角色扮演", "desc": "儒雅才俊", "voice_type": "ICL_zh_male_ruyacaijun_tob", "lang": "中文", "emotions": [], "keywords": ["儒雅才俊", "角色扮演", "中文", "ICL_zh_male_ruyacaijun_tob"]},
    {"scene": "角色扮演", "desc": "病娇白莲", "voice_type": "ICL_zh_male_bingjiaobailian_tob", "lang": "中文", "emotions": [], "keywords": ["病娇白莲", "角色扮演", "中文", "ICL_zh_male_bingjiaobailian_tob"]},
    {"scene": "角色扮演", "desc": "正直青年", "voice_type": "ICL_zh_male_zhengzhiqingnian_tob", "lang": "中文", "emotions": [], "keywords": ["正直青年", "角色扮演", "中文", "ICL_zh_male_zhengzhiqingnian_tob"]},
    {"scene": "角色扮演", "desc": "娇憨女王", "voice_type": "ICL_zh_female_jiaohannvwang_tob", "lang": "中文", "emotions": [], "keywords": ["娇憨女王", "角色扮演", "中文", "ICL_zh_female_jiaohannvwang_tob"]},
    {"scene": "角色扮演", "desc": "病娇萌妹", "voice_type": "ICL_zh_female_bingjiaomengmei_tob", "lang": "中文", "emotions": [], "keywords": ["病娇萌妹", "角色扮演", "中文", "ICL_zh_female_bingjiaomengmei_tob"]},
    {"scene": "角色扮演", "desc": "青涩小生", "voice_type": "ICL_zh_male_qingsenaigou_tob", "lang": "中文", "emotions": [], "keywords": ["青涩小生", "角色扮演", "中文", "ICL_zh_male_qingsenaigou_tob"]},
    {"scene": "角色扮演", "desc": "纯真学弟", "voice_type": "ICL_zh_male_chunzhenxuedi_tob", "lang": "中文", "emotions": [], "keywords": ["纯真学弟", "角色扮演", "中文", "ICL_zh_male_chunzhenxuedi_tob"]},
    {"scene": "角色扮演", "desc": "暖心学姐", "voice_type": "ICL_zh_female_nuanxinxuejie_tob", "lang": "中文", "emotions": [], "keywords": ["暖心学姐", "角色扮演", "中文", "ICL_zh_female_nuanxinxuejie_tob"]},
    {"scene": "角色扮演", "desc": "可爱女生", "voice_type": "ICL_zh_female_keainvsheng_tob", "lang": "中文", "emotions": [], "keywords": ["可爱女生", "角色扮演", "中文", "ICL_zh_female_keainvsheng_tob"]},
    {"scene": "角色扮演", "desc": "成熟姐姐", "voice_type": "ICL_zh_female_chengshujiejie_tob", "lang": "中文", "emotions": [], "keywords": ["成熟姐姐", "角色扮演", "中文", "ICL_zh_female_chengshujiejie_tob"]},
    {"scene": "角色扮演", "desc": "病娇姐姐", "voice_type": "ICL_zh_female_bingjiaojiejie_tob", "lang": "中文", "emotions": [], "keywords": ["病娇姐姐", "角色扮演", "中文", "ICL_zh_female_bingjiaojiejie_tob"]},
    {"scene": "角色扮演", "desc": "优柔帮主", "voice_type": "ICL_zh_male_youroubangzhu_tob", "lang": "中文", "emotions": [], "keywords": ["优柔帮主", "角色扮演", "中文", "ICL_zh_male_youroubangzhu_tob"]},
    {"scene": "角色扮演", "desc": "优柔公子", "voice_type": "ICL_zh_male_yourougongzi_tob", "lang": "中文", "emotions": [], "keywords": ["优柔公子", "角色扮演", "中文", "ICL_zh_male_yourougongzi_tob"]},
    {"scene": "角色扮演", "desc": "玩媚御姐", "voice_type": "ICL_zh_female_wumeiyujie_tob", "lang": "中文", "emotions": [], "keywords": ["玩媚御姐", "角色扮演", "中文", "ICL_zh_female_wumeiyujie_tob"]},
    {"scene": "角色扮演", "desc": "调皮公主", "voice_type": "ICL_zh_female_tiaopigongzhu_tob", "lang": "中文", "emotions": [], "keywords": ["调皮公主", "角色扮演", "中文", "ICL_zh_female_tiaopigongzhu_tob"]},
    {"scene": "角色扮演", "desc": "傲娇女友", "voice_type": "ICL_zh_female_aojiaonvyou_tob", "lang": "中文", "emotions": [], "keywords": ["傲娇女友", "角色扮演", "中文", "ICL_zh_female_aojiaonvyou_tob"]},
    {"scene": "角色扮演", "desc": "贴心男友", "voice_type": "ICL_zh_male_tiexinnanyou_tob", "lang": "中文", "emotions": [], "keywords": ["贴心男友", "角色扮演", "中文", "ICL_zh_male_tiexinnanyou_tob"]},
    {"scene": "角色扮演", "desc": "少年将军", "voice_type": "ICL_zh_male_shaonianjiangjun_tob", "lang": "中文", "emotions": [], "keywords": ["少年将军", "角色扮演", "中文", "ICL_zh_male_shaonianjiangjun_tob"]},
    {"scene": "角色扮演", "desc": "贴心女友", "voice_type": "ICL_zh_female_tiexinnvyou_tob", "lang": "中文", "emotions": [], "keywords": ["贴心女友", "角色扮演", "中文", "ICL_zh_female_tiexinnvyou_tob"]},
    {"scene": "角色扮演", "desc": "病娇哥哥", "voice_type": "ICL_zh_male_bingjiaogege_tob", "lang": "中文", "emotions": [], "keywords": ["病娇哥哥", "角色扮演", "中文", "ICL_zh_male_bingjiaogege_tob"]},
    {"scene": "角色扮演", "desc": "学霸男同桌", "voice_type": "ICL_zh_male_xuebanantongzhuo_tob", "lang": "中文", "emotions": [], "keywords": ["学霸男同桌", "角色扮演", "中文", "ICL_zh_male_xuebanantongzhuo_tob"]},
    {"scene": "角色扮演", "desc": "幽默叔叔", "voice_type": "ICL_zh_male_youmoshushu_tob", "lang": "中文", "emotions": [], "keywords": ["幽默叔叔", "角色扮演", "中文", "ICL_zh_male_youmoshushu_tob"]},
    {"scene": "角色扮演", "desc": "性感御姐", "voice_type": "ICL_zh_female_xingganyujie_tob", "lang": "中文", "emotions": [], "keywords": ["性感御姐", "角色扮演", "中文", "ICL_zh_female_xingganyujie_tob"]},
    {"scene": "角色扮演", "desc": "假小子", "voice_type": "ICL_zh_female_jiaxiaozi_tob", "lang": "中文", "emotions": [], "keywords": ["假小子", "角色扮演", "中文", "ICL_zh_female_jiaxiaozi_tob"]},
    {"scene": "角色扮演", "desc": "冷峻上司", "voice_type": "ICL_zh_male_lengjunshangsi_tob", "lang": "中文", "emotions": [], "keywords": ["冷峻上司", "角色扮演", "中文", "ICL_zh_male_lengjunshangsi_tob"]},
    {"scene": "角色扮演", "desc": "温柔男同桌", "voice_type": "ICL_zh_male_wenrounantongzhuo_tob", "lang": "中文", "emotions": [], "keywords": ["温柔男同桌", "角色扮演", "中文", "ICL_zh_male_wenrounantongzhuo_tob"]},
    {"scene": "角色扮演", "desc": "病娇弟弟", "voice_type": "ICL_zh_male_bingjiaodidi_tob", "lang": "中文", "emotions": [], "keywords": ["病娇弟弟", "角色扮演", "中文", "ICL_zh_male_bingjiaodidi_tob"]},
    {"scene": "角色扮演", "desc": "幽默大爷", "voice_type": "ICL_zh_male_youmodaye_tob", "lang": "中文", "emotions": [], "keywords": ["幽默大爷", "角色扮演", "中文", "ICL_zh_male_youmodaye_tob"]},
    {"scene": "角色扮演", "desc": "傲慢少爷", "voice_type": "ICL_zh_male_aomanshaoye_tob", "lang": "中文", "emotions": [], "keywords": ["傲慢少爷", "角色扮演", "中文", "ICL_zh_male_aomanshaoye_tob"]},
    {"scene": "角色扮演", "desc": "神秘法师", "voice_type": "ICL_zh_male_shenmifashi_tob", "lang": "中文", "emotions": [], "keywords": ["神秘法师", "角色扮演", "中文", "ICL_zh_male_shenmifashi_tob"]},
    # ====== 视频配音 ======
    {"scene": "视频配音", "desc": "和蔼奶奶", "voice_type": "ICL_zh_female_heainainai_tob", "lang": "中文", "emotions": [], "keywords": ["和蔼奶奶", "视频配音", "女声", "中文"]},
    {"scene": "视频配音", "desc": "邻居阿姨", "voice_type": "ICL_zh_female_linjuayi_tob", "lang": "中文", "emotions": [], "keywords": ["邻居阿姨", "视频配音", "女声", "中文"]},
    {"scene": "视频配音", "desc": "温柔小雅", "voice_type": "zh_female_wenrouxiaoya_moon_bigtts", "lang": "中文", "emotions": [], "keywords": ["温柔小雅", "视频配音", "女声", "中文"]},
    {"scene": "视频配音", "desc": "天才童声", "voice_type": "zh_male_tiancaitongsheng_mars_bigtts", "lang": "中文", "emotions": [], "keywords": ["天才童声", "视频配音", "男声", "中文"]},
    {"scene": "视频配音", "desc": "猴哥", "voice_type": "zh_male_sunwukong_mars_bigtts", "lang": "中文", "emotions": [], "keywords": ["猴哥", "视频配音", "男声", "中文"]},
    {"scene": "视频配音", "desc": "熊二", "voice_type": "zh_male_xionger_mars_bigtts", "lang": "中文", "emotions": [], "keywords": ["熊二", "视频配音", "男声", "中文"]},
    {"scene": "视频配音", "desc": "佩奇猪", "voice_type": "zh_female_peqizhu_mars_bigtts", "lang": "中文", "emotions": [], "keywords": ["佩奇猪", "视频配音", "女声", "中文"]},
    {"scene": "视频配音", "desc": "武则天", "voice_type": "zh_female_wuzetian_mars_bigtts", "lang": "中文", "emotions": [], "keywords": ["武则天", "视频配音", "女声", "中文"]},
    {"scene": "视频配音", "desc": "顾姐", "voice_type": "zh_female_gujie_mars_bigtts", "lang": "中文", "emotions": [], "keywords": ["顾姐", "视频配音", "女声", "中文"]},
    {"scene": "视频配音", "desc": "樱桃丸子", "voice_type": "zh_female_yingtaowanzi_mars_bigtts", "lang": "中文", "emotions": [], "keywords": ["樱桃丸子", "视频配音", "女声", "中文"]},
    {"scene": "视频配音", "desc": "广告解说", "voice_type": "zh_male_chunhui_mars_bigtts", "lang": "中文", "emotions": [], "keywords": ["广告解说", "视频配音", "男声", "中文"]},
    {"scene": "视频配音", "desc": "少儿故事", "voice_type": "zh_female_shaoergushi_mars_bigtts", "lang": "中文", "emotions": [], "keywords": ["少儿故事", "视频配音", "女声", "中文"]},
    {"scene": "视频配音", "desc": "四郎", "voice_type": "zh_male_silang_mars_bigtts", "lang": "中文", "emotions": [], "keywords": ["四郎", "视频配音", "男声", "中文"]},
    {"scene": "视频配音", "desc": "磁性解说男声/Morgan", "voice_type": "zh_male_jieshuonansheng_mars_bigtts", "lang": "中文, 美式英语", "emotions": [], "keywords": ["磁性解说男声", "Morgan", "视频配音", "男声", "中文", "美式英语"]},
    {"scene": "视频配音", "desc": "鸡汤铁娘/ Hope", "voice_type": "zh_female_jitangtienvsheng_mars_bigtts", "lang": "中文, 美式英语", "emotions": [], "keywords": ["鸡汤铁娘", "Hope", "视频配音", "女声", "中文", "美式英语"]},
    {"scene": "视频配音", "desc": "贴心女声/Candy", "voice_type": "zh_female_tiexinnvsheng_mars_bigtts", "lang": "中文, 美式英语", "emotions": [], "keywords": ["贴心女声", "Candy", "视频配音", "女声", "中文", "美式英语"]},
    {"scene": "视频配音", "desc": "俏皮女声", "voice_type": "zh_female_qiaopinvsheng_mars_bigtts", "lang": "中文", "emotions": [], "keywords": ["俏皮女声", "视频配音", "女声", "中文"]},
    {"scene": "视频配音", "desc": "萌丫头/Cutey", "voice_type": "zh_female_mengyatou_mars_bigtts", "lang": "中文, 美式英语", "emotions": [], "keywords": ["萌丫头", "Cutey", "视频配音", "女声", "中文", "美式英语"]},
    {"scene": "视频配音", "desc": "懒音萌宝", "voice_type": "zh_female_lanxiaoyangma_mars_bigtts", "lang": "中文", "emotions": [], "keywords": ["懒音萌宝", "视频配音", "女声", "中文"]},
    {"scene": "视频配音", "desc": "亮嗓萌仔", "voice_type": "zh_male_dongmanhaimian_mars_bigtts", "lang": "中文", "emotions": [], "keywords": ["亮嗓萌仔", "视频配音", "男声", "中文"]},
    # ====== 有声阅读 ======
    {"scene": "有声阅读", "desc": "晨曦解说", "voice_type": "zh_male_changtianyi_mars_bigtts", "lang": "中文", "emotions": [], "keywords": ["晨曦解说", "有声阅读", "男声", "中文"]},
    {"scene": "有声阅读", "desc": "儒雅青年", "voice_type": "zh_male_ruyaqingnian_mars_bigtts", "lang": "中文", "emotions": [], "keywords": ["儒雅青年", "有声阅读", "男声", "中文"]},
    {"scene": "有声阅读", "desc": "霸气青叔", "voice_type": "zh_male_baqiqingshu_mars_bigtts", "lang": "中文", "emotions": [], "keywords": ["霸气青叔", "有声阅读", "男声", "中文"]},
    {"scene": "有声阅读", "desc": "擎苍", "voice_type": "zh_male_qingcang_mars_bigtts", "lang": "中文", "emotions": [], "keywords": ["擎苍", "有声阅读", "男声", "中文"]},
    {"scene": "有声阅读", "desc": "活力小哥", "voice_type": "zh_male_yangguangqingnian_mars_bigtts", "lang": "中文", "emotions": [], "keywords": ["活力小哥", "有声阅读", "男声", "中文"]},
    {"scene": "有声阅读", "desc": "古风少御", "voice_type": "zh_female_gufengshaoyu_mars_bigtts", "lang": "中文", "emotions": [], "keywords": ["古风少御", "有声阅读", "女声", "中文"]},
    {"scene": "有声阅读", "desc": "温柔淑女", "voice_type": "zh_female_wenroushunv_mars_bigtts", "lang": "中文", "emotions": [], "keywords": ["温柔淑女", "有声阅读", "女声", "中文"]},
    {"scene": "有声阅读", "desc": "反转青年", "voice_type": "zh_male_fanjuanqingnian_mars_bigtts", "lang": "中文", "emotions": [], "keywords": ["反转青年", "有声阅读", "男声", "中文"]}
]

# 关键词优先映射表，方便扩展
KEYWORD_MCP = {
    "少女": "ICL_zh_female_bingruoshaonv_tob",
    "萝莉": "ICL_zh_female_jiaoruoluoli_tob",
    "御姐": "zh_female_gaolengyujie_moon_bigtts",
    "女友": "zh_female_meilinvyou_moon_bigtts",
    "小伙": "ICL_zh_male_shuaizhenxiaohuo_tob",
    "男孩": "zh_male_linjiananhai_moon_bigtts",
    "北京": "zh_male_beijingxiaoye_moon_bigtts",
    "四川": "zh_female_daimengchuanmei_moon_bigtts",
    # ...可继续扩展
}

def get_voice_type(nl_voice_type: str) -> str:
    """
    支持自然语言模糊检索音色，返回最匹配的 voice_type。
    """
    nl = nl_voice_type.strip().lower()
    # 关键词优先映射
    for k, v in KEYWORD_MCP.items():
        if k in nl:
            return v
    # 先精确查找
    for v in VOICE_LIST:
        if nl == v["voice_type"].lower():
            return v["voice_type"]
    # 再模糊查找（desc、keywords）
    for v in VOICE_LIST:
        if any(nl in k.lower() or k.lower() in nl for k in v["keywords"]):
            return v["voice_type"]
    # 默认返回官方女声
    return "zh_female_wanqudashu_moon_bigtts"

def get_voice_info(voice_type: str) -> dict:
    """
    根据 voice_type 获取完整音色信息。
    """
    for v in VOICE_LIST:
        if v["voice_type"] == voice_type:
            return v
    return {} 