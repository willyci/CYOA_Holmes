"""Comprehensive generator for 15-Chapter Multi-POV Edition of 'The Hound of the Baskervilles'.
Generates src/content/hound_story_en.py and src/content/hound_story_cn.py.
Features:
- Watson Track: Full canonical 15 chapters with at most 2 nodes per chapter and extensive authentic prose from book_en.txt / book_cn.txt.
- Holmes Track: 15 playable nodes from Sherlock Holmes's perspective (POV: Sherlock Holmes / 歇洛克·福尔摩斯).
- Stapleton Track: 15 playable nodes from Jack Stapleton's antagonist perspective (POV: Jack Stapleton / 杰克·斯台普吞).
- start_nodes:
    POV.WATSON: ch01_part1_stick
    POV.HOLMES: holmes_ch1_baker_street
    POV.STAPLETON: stapleton_ch1_london
"""
import json
import re
import sys
import subprocess
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

ROOT = Path(__file__).resolve().parent

with open(ROOT / 'src/content/book_en.txt', 'r', encoding='utf-8') as f:
    en_raw = f.read()

with open(ROOT / 'src/content/book_cn.txt', 'r', encoding='utf-8') as f:
    cn_raw = f.read()

en_ch_blocks = re.split(r'\n(?=Chapter \d+\.)', en_raw)[1:]
cn_ch_blocks = re.split(r'\n(?=第[一二三四五六七八九十]+章\u3000)', cn_raw)[16:]

def normalize_en_paras(text):
    raw_paras = re.split(r'\n\s*\n+', text)
    paras = []
    for p in raw_paras:
        lines = [l.strip() for l in p.split('\n') if l.strip()]
        if lines and not (lines[0].startswith('Chapter ') or lines[0].startswith('CHAPTER ')):
            paras.append(' '.join(lines))
    return paras

def normalize_cn_paras(text):
    raw_paras = re.split(r'\n\s*\n+', text)
    paras = []
    for p in raw_paras:
        lines = [l.strip() for l in p.split('\n') if l.strip()]
        if lines and not (lines[0].startswith('第') and '章' in lines[0]):
            paras.append(''.join(lines))
    return paras

en_chapters = [normalize_en_paras(b) for b in en_ch_blocks]
cn_chapters = [normalize_cn_paras(b) for b in cn_ch_blocks]

# Split indices for 2-node chapters: (en_split_idx, cn_split_idx)
split_indices = {
    0: (40, 41),   # Ch 1
    1: (27, 29),   # Ch 2
    3: (94, 98),   # Ch 4
    5: (47, 46),   # Ch 6
    6: (87, 88),   # Ch 7
    8: (87, 95),   # Ch 9
    10: (67, 72),  # Ch 11
    11: (60, 74),  # Ch 12
    13: (40, 42),  # Ch 14
}

# 1. WATSON'S 15-CHAPTER CANONICAL NODES (29 nodes)
WATSON_NODES = [
    # Chapter 1
    {
        "id": "ch01_part1_stick",
        "ch_idx": 0, "part": 1,
        "title_en": "Chapter 1: Mr. Sherlock Holmes (Part I: The Walking Stick)",
        "title_cn": "第一章 歇洛克·福尔摩斯先生（上：手杖与来客）",
        "pov": "watson", "type": "anchor", "anchor": "anchor_chapter1",
        "clues_en": [
            "Penang-lawyer stick engraved: To James Mortimer, M.R.C.S., from his friends of the C.C.H., 1884",
            "Spaniel jaw tooth-marks on the walking stick",
        ],
        "clues_cn": [
            "刻有‘一八八四年，C.C.H.的朋友们赠给皇家外科医学院会员杰姆士·摩梯末’字样的槟榔屿手杖",
            "手杖上被猎犬利齿咬出的齿痕",
        ],
        "choices_en": [
            {"id": "ch1_p1_c1", "text": "Listen intently as Dr. Mortimer prepares to present his business.", "target": "ch01_part2_mortimer"},
            {"id": "ch1_p1_c2", "text": "Inquire why Dr. Mortimer has sought out the second highest expert in Europe.", "target": "ch01_part2_mortimer"},
        ],
        "choices_cn": [
            {"id": "ch1_p1_c1", "text": "专心聆听摩梯末医生说明来意与所携文书。", "target": "ch01_part2_mortimer"},
            {"id": "ch1_p1_c2", "text": "询问摩梯末医生为何专程造访‘欧洲第二高明的专家’。", "target": "ch01_part2_mortimer"},
        ],
    },
    {
        "id": "ch01_part2_mortimer",
        "ch_idx": 0, "part": 2,
        "title_en": "Chapter 1: Mr. Sherlock Holmes (Part II: The Consultation)",
        "title_cn": "第一章 歇洛克·福尔摩斯先生（下：神秘的手稿）",
        "pov": "watson", "type": "branch", "anchor": None,
        "clues_en": [
            "Dr. James Mortimer consults Holmes regarding Sir Charles Baskerville's death",
            "An ancient 1742 manuscript kept in Mortimer's breast pocket",
        ],
        "clues_cn": [
            "摩梯末医生就查尔斯·巴斯克维尔爵士猝死案向福尔摩斯求助",
            "摩梯末医生胸前口袋中深藏的一份一七四二年古代手稿",
        ],
        "choices_en": [
            {"id": "ch1_p2_c1", "text": "Request Dr. Mortimer to unfold and read the 1742 manuscript of the Baskerville curse.", "target": "ch02_part1_legend"},
            {"id": "ch1_p2_c2", "text": "Ask Dr. Mortimer about Sir Charles Baskerville's state of mind prior to his death.", "target": "ch02_part1_legend"},
        ],
        "choices_cn": [
            {"id": "ch1_p2_c1", "text": "请摩梯末医生展开宣读一七四二年巴斯克维尔诅咒手稿。", "target": "ch02_part1_legend"},
            {"id": "ch1_p2_c2", "text": "向摩梯末医生询问查尔斯·巴斯克维尔爵士生前的心态与恐惧。", "target": "ch02_part1_legend"},
        ],
    },
    # Chapter 2
    {
        "id": "ch02_part1_legend",
        "ch_idx": 1, "part": 1,
        "title_en": "Chapter 2: The Curse of the Baskervilles (Part I: The 1742 Manuscript)",
        "title_cn": "第二章 巴斯克维尔的灾祸（上：古老的手稿）",
        "pov": "watson", "type": "anchor", "anchor": "anchor_curse",
        "clues_en": [
            "1742 Baskerville manuscript: Hugo's wickedness and the hound of hell",
            "Solemn warning to the sons of Baskerville never to cross the moor in the dark hours",
        ],
        "clues_cn": [
            "一七四二年手稿：雨果·巴斯克维尔的罪恶行径与地狱火犬传说",
            "对手足子孙的严厉告诫：夜黑之时切莫穿行达特沼地",
        ],
        "choices_en": [
            {"id": "ch2_p1_c1", "text": "Inquire into Sir Charles's recent habits and the coroner's inquest.", "target": "ch02_part2_footprints"},
            {"id": "ch2_p1_c2", "text": "Ask Dr. Mortimer whether he personally believes in this supernatural hound.", "target": "ch02_part2_footprints"},
        ],
        "choices_cn": [
            {"id": "ch2_p1_c1", "text": "问询查尔斯爵士近期的生活习惯及验尸官的调查结论。", "target": "ch02_part2_footprints"},
            {"id": "ch2_p1_c2", "text": "询问摩梯末医生是否也坚信超自然的巨犬传说是真实的。", "target": "ch02_part2_footprints"},
        ],
    },
    {
        "id": "ch02_part2_footprints",
        "ch_idx": 1, "part": 2,
        "title_en": "Chapter 2: The Curse of the Baskervilles (Part II: The Footprints)",
        "title_cn": "第二章 巴斯克维尔的灾祸（下：巨犬的足迹）",
        "pov": "watson", "type": "branch", "anchor": None,
        "clues_en": [
            "Coroner verdict: Sir Charles died of heart failure at the Yew Alley gate",
            "Altered tiptoe footprints indicating Sir Charles was waiting or fleeing in terror",
            "The secret withheld from the coroner: Footprints of a gigantic hound!",
        ],
        "clues_cn": [
            "法医结论：查尔斯爵士在水松夹道栅门前死于心脏衰竭",
            "改变的足印表明查尔斯爵士曾在门前久驻或惊慌奔逃",
            "法庭未公开的惊天隐秘：一头巨大的猎犬的足迹！",
        ],
        "choices_en": [
            {"id": "ch2_p2_c1", "text": "Proceed to analyze the problem in Baker Street with Holmes.", "target": "ch03_problem"},
            {"id": "ch2_p2_c2", "text": "Question Dr. Mortimer closely regarding the distance and size of the footprints.", "target": "ch03_problem"},
        ],
        "choices_cn": [
            {"id": "ch2_p2_c1", "text": "跟随福尔摩斯在贝克街推演整个案情的脉络与焦点。", "target": "ch03_problem"},
            {"id": "ch2_p2_c2", "text": "严密追问摩梯末医生关于猎犬足迹距离与形态的细节。", "target": "ch03_problem"},
        ],
    },
    # Chapter 3
    {
        "id": "ch03_problem",
        "ch_idx": 2, "part": 0,
        "title_en": "Chapter 3: The Problem",
        "title_cn": "第三章 疑案",
        "pov": "watson", "type": "branch", "anchor": None,
        "clues_en": [
            "Sir Henry Baskerville, next heir, arrives in London tomorrow from America",
            "Ordnance map of Dartmoor: Baskerville Hall, Grimpen Mire, and prehistoric stone huts",
            "Holmes's twin problems: Has a crime been committed, and how to protect Sir Henry",
        ],
        "clues_cn": [
            "下一位合法继承人亨利·巴斯克维尔爵士明日自美洲抵达伦敦",
            "德文郡军用地图：巴斯克维尔庄园、大格林盆泥潭与史前石屋群",
            "福尔摩斯的两大疑难：究竟有无罪案发生，以及如何保全亨利爵士性命",
        ],
        "choices_en": [
            {"id": "ch3_c1", "text": "Prepare for the interview with Sir Henry Baskerville tomorrow morning.", "target": "ch04_part1_warning"},
            {"id": "ch3_c2", "text": "Review the topography of Dartmoor and consider the risks of Sir Henry going down.", "target": "ch04_part1_warning"},
        ],
        "choices_cn": [
            {"id": "ch3_c1", "text": "准备明早与亨利·巴斯克维尔爵士及摩梯末医生的关键会面。", "target": "ch04_part1_warning"},
            {"id": "ch3_c2", "text": "再次审视达特沼地的险峻地形与亨利爵士奔赴庄园的潜在危险。", "target": "ch04_part1_warning"},
        ],
    },
    # Chapter 4
    {
        "id": "ch04_part1_warning",
        "ch_idx": 3, "part": 1,
        "title_en": "Chapter 4: Sir Henry Baskerville (Part I: The Warning Letter)",
        "title_cn": "第四章 亨利·巴斯克维尔爵士（上：警告信与丢失的皮靴）",
        "pov": "watson", "type": "anchor", "anchor": "anchor_london_mission",
        "clues_en": [
            "Pasted warning letter from The Times: 'As you value your life or your reason keep away from the moor'",
            "Cut with short-bladed nail-scissors and posted from Charing Cross",
            "Sir Henry's brand new tan boot stolen from the Northumberland Hotel",
        ],
        "clues_cn": [
            "剪自昨日《泰晤士报》的匿名警告信：‘你如果还在乎自己的理智或生命，就应当远离那片沼地’",
            "字迹由短刃指甲刀剪切，投寄自查令十字街邮局",
            "亨利爵士在诺森伯兰旅馆丢失了一只崭新的黄色新皮靴",
        ],
        "choices_en": [
            {"id": "ch4_p1_c1", "text": "Suggest shadowing Sir Henry and Mortimer down Regent Street to see if they are followed.", "target": "ch04_part2_cab_chase"},
            {"id": "ch4_p1_c2", "text": "Examine the stolen tan boot and question Sir Henry about his hotel room.", "target": "ch04_part2_cab_chase"},
        ],
        "choices_cn": [
            {"id": "ch4_p1_c1", "text": "提议暗中跟踪亨利爵士与摩梯末医生，查明沿途是否有密探盯梢。", "target": "ch04_part2_cab_chase"},
            {"id": "ch4_p1_c2", "text": "进一步盘问亨利爵士新靴失窃的细节与旅馆环境。", "target": "ch04_part2_cab_chase"},
        ],
    },
    {
        "id": "ch04_part2_cab_chase",
        "ch_idx": 3, "part": 2,
        "title_en": "Chapter 4: Sir Henry Baskerville (Part II: The Cab Chase)",
        "title_cn": "第四章 亨利·巴斯克维尔爵士（下：摄政街马车追踪）",
        "pov": "watson", "type": "branch", "anchor": None,
        "clues_en": [
            "Bearded spy with piercing eyes observing Sir Henry from Hansom Cab No. 2704",
            "The spy flees when Holmes catches sight of him in Regent Street",
            "Young Cartwright hired to search waste-paper baskets of 23 hotels for the cut Times",
        ],
        "clues_cn": [
            "生着浓密黑须与凌厉双目的密探乘坐2704号双轮马车沿途尾随",
            "密探发现被福尔摩斯识破后立即令马车夫疾驰逃脱",
            "雇用卡特赖特搜查查令十字区23家旅馆的废纸篓以搜寻剪剩的《泰晤士报》",
        ],
        "choices_en": [
            {"id": "ch4_p2_c1", "text": "Return to the Northumberland Hotel to unravel the three broken threads.", "target": "ch05_threads"},
            {"id": "ch4_p2_c2", "text": "Trace the registered number of Hansom Cab 2704 through the Cab Office.", "target": "ch05_threads"},
        ],
        "choices_cn": [
            {"id": "ch4_p2_c1", "text": "返回诺森伯兰旅馆汇合，梳理追查三条关键线索。", "target": "ch05_threads"},
            {"id": "ch4_p2_c2", "text": "通过马车调度行彻查2704号双轮马车车主与车夫底细。", "target": "ch05_threads"},
        ],
    },
    # Chapter 5
    {
        "id": "ch05_threads",
        "ch_idx": 4, "part": 0,
        "title_en": "Chapter 5: Three Broken Threads",
        "title_cn": "第五章 三条断了的线索",
        "pov": "watson", "type": "anchor", "anchor": "anchor_threads",
        "clues_en": [
            "Sir Henry's old black boot stolen while the lost tan boot mysteriously reappears",
            "Cartwright finds no cut Times in 23 hotel waste-baskets",
            "Barrymore verified at Baskerville Hall via telegram",
            "Cabman John Clayton: The bearded passenger audaciously claimed his name was Sherlock Holmes",
            "Watson ordered to accompany Sir Henry to Dartmoor armed with his revolver",
        ],
        "clues_cn": [
            "亨利爵士的一只旧黑皮靴失窃，而此前丢失的黄皮靴又离奇现身",
            "卡特赖特搜查23家旅馆废纸篓一无所获",
            "达特沼地庄园电报核实白瑞摩确实留在庄园",
            "马车夫约翰·克莱顿供述：那蓄黑胡须的乘客狂妄自称‘歇洛克·福尔摩斯’",
            "福尔摩斯指令华生佩带左轮手枪随同亨利爵士奔赴德文郡贴身护卫",
        ],
        "choices_en": [
            {"id": "ch5_c1", "text": "Watson accepts the perilous assignment and boards the Devonshire express with Sir Henry.", "target": "ch06_part1_arrival"},
            {"id": "ch5_c2", "text": "Receive final instructions from Holmes regarding suspects and precautions on the moor.", "target": "ch06_part1_arrival"},
        ],
        "choices_cn": [
            {"id": "ch5_c1", "text": "华生毅然接受重托，佩带手枪与亨利爵士同登前往德文郡的特快列车。", "target": "ch06_part1_arrival"},
            {"id": "ch5_c2", "text": "聆听福尔摩斯关于防范危险与排查嫌犯的临行绝密嘱托。", "target": "ch06_part1_arrival"},
        ],
    },
    # Chapter 6
    {
        "id": "ch06_part1_arrival",
        "ch_idx": 5, "part": 1,
        "title_en": "Chapter 6: Baskerville Hall (Part I: The Journey onto Dartmoor)",
        "title_cn": "第六章 巴斯克维尔庄园（上：阴森的荒原与初抵庄园）",
        "pov": "watson", "type": "anchor", "anchor": "anchor_arrival",
        "clues_en": [
            "Armed soldiers and warders patrol the moor roads: Selden, the Notting Hill murderer, escaped from Princetown",
            "Gloomy ancient architecture of Baskerville Hall and dark granite towers",
            "Butler Barrymore and his pale, sorrowful wife welcome the party",
        ],
        "clues_cn": [
            "荷枪实弹的骑兵在荒原路口盘查：诺丁山杀人凶犯塞尔登自达特穆尔监狱越狱脱逃",
            "巴斯克维尔庄园阴森肃穆的双塔与布满常春藤的高大花岗岩古建",
            "面带阴郁之气的管家白瑞摩及其苍白哀伤的妻子出迎",
        ],
        "choices_en": [
            {"id": "ch6_p1_c1", "text": "Retire to the bedchamber with loaded revolver, remaining alert to the night.", "target": "ch06_part2_night_sob"},
            {"id": "ch6_p1_c2", "text": "Inspect the gloomy dining hall and corridors before turning in.", "target": "ch06_part2_night_sob"},
            {"id": "ch6_p1_c3", "text": "[Switch POV to Sherlock Holmes] View Holmes's covert headquarters in the stone hut on Black Tor.", "target": "holmes_ch06_part2_hut_surveillance", "pov_switch": "holmes"},
            {"id": "ch6_p1_c4", "text": "[Switch POV to Jack Stapleton] Observe the arrival from Merripit House and the deadly Grimpen Mire.", "target": "stapleton_ch06_part1_arrival_watch", "pov_switch": "stapleton"},
        ],
        "choices_cn": [
            {"id": "ch6_p1_c1", "text": "持枪就寝，在庄园卧室中警惕倾听深夜的风吹草动。", "target": "ch06_part2_night_sob"},
            {"id": "ch6_p1_c2", "text": "就寝前环视阴暗的大厅与历代祖先画像，感受古宅气氛。", "target": "ch06_part2_night_sob"},
            {"id": "ch6_p1_c3", "text": "【视角切换：歇洛克·福尔摩斯】查看福尔摩斯在黑色岩岗史前石屋的隐蔽指挥所。", "target": "holmes_ch06_part2_hut_surveillance", "pov_switch": "holmes"},
            {"id": "ch6_p1_c4", "text": "【视角切换：杰克·斯台普吞】自梅利琵宅邸与大格林盆泥潭监视庄园动静。", "target": "stapleton_ch06_part1_arrival_watch", "pov_switch": "stapleton"},
        ],
    },
    {
        "id": "ch06_part2_night_sob",
        "ch_idx": 5, "part": 2,
        "title_en": "Chapter 6: Baskerville Hall (Part II: The Midnight Sob)",
        "title_cn": "第六章 巴斯克维尔庄园（下：午夜的哭声）",
        "pov": "watson", "type": "branch", "anchor": None,
        "clues_en": [
            "Watson awakened at 2 a.m. by the suppressed, agonized sobs of a woman in the corridors",
            "Barrymore denies his wife was crying, yet Mrs. Barrymore has red, swollen eyes at breakfast",
            "Telegram inquiry reveals telegram was delivered to Mrs. Barrymore, leaving Barrymore's London alibi unproven",
        ],
        "clues_cn": [
            "华生于凌晨两点被走廊深处传来的女人凄惨抽泣声惊醒",
            "白瑞摩坚称妻子安睡未哭，但华生在早饭时敏锐察觉白瑞摩太太双眼红肿",
            "电报调查发现电报实际由白瑞摩太太代收，白瑞摩当时在伦敦的不在场证明失效",
        ],
        "choices_en": [
            {"id": "ch6_p2_c1", "text": "Walk out onto the moor to explore the vicinity of Merripit House.", "target": "ch07_part1_naturalist"},
            {"id": "ch6_p2_c2", "text": "Inquire further about Barrymore's movements with Dr. Mortimer at the post office.", "target": "ch07_part1_naturalist"},
        ],
        "choices_cn": [
            {"id": "ch6_p2_c1", "text": "漫步走向荒原，探查梅利琵宅邸与格林盆泥潭周边动静。", "target": "ch07_part1_naturalist"},
            {"id": "ch6_p2_c2", "text": "前往格林盆邮局核实白瑞摩接发电报的具体细节。", "target": "ch07_part1_naturalist"},
        ],
    },
    # Chapter 7
    {
        "id": "ch07_part1_naturalist",
        "ch_idx": 6, "part": 1,
        "title_en": "Chapter 7: The Stapletons of Merripit House (Part I: The Naturalist & The Mire)",
        "title_cn": "第七章 梅利琵宅邸的主人斯台普吞（上：博物学者与格林盆泥潭）",
        "pov": "watson", "type": "anchor", "anchor": "anchor_mire",
        "clues_en": [
            "Jack Stapleton, eccentric naturalist of Merripit House, carrying butterfly net and specimen box",
            "A moor pony swallowed whole before their eyes by the lethal Great Grimpen Mire",
            "A deep, blood-chilling howling sound rolling across the moorland",
        ],
        "clues_cn": [
            "梅利琵宅邸的博物学者杰克·斯台普吞，手持捕蝶网与标本盒巡游荒原",
            "亲眼目睹一匹小矮马陷入大格林盆泥潭的致命绿色泥淖中被活活吞没",
            "荒原深处回荡起沉闷、悠长而令人毛骨悚然的凄厉犬嚎",
        ],
        "choices_en": [
            {"id": "ch7_p1_c1", "text": "Approach Miss Beryl Stapleton as she emerges upon the moor path.", "target": "ch07_part2_beryl_warning"},
            {"id": "ch7_p1_c2", "text": "Observe Stapleton chasing the rare cyclopides moth toward the edge of the mire.", "target": "ch07_part2_beryl_warning"},
        ],
        "choices_cn": [
            {"id": "ch7_p1_c1", "text": "走上前去迎候出现在荒原小径上的斯台普吞小姐。", "target": "ch07_part2_beryl_warning"},
            {"id": "ch7_p1_c2", "text": "注视斯台普吞狂热追逐罕见飞蛾扑向泥潭边缘的险恶身法。", "target": "ch07_part2_beryl_warning"},
        ],
    },
    {
        "id": "ch07_part2_beryl_warning",
        "ch_idx": 6, "part": 2,
        "title_en": "Chapter 7: The Stapletons of Merripit House (Part II: The Desperate Warning)",
        "title_cn": "第七章 梅利琵宅邸的主人斯台普吞（下：绝望的警告）",
        "pov": "watson", "type": "branch", "anchor": None,
        "clues_en": [
            "Miss Beryl Stapleton mistakes Watson for Sir Henry Baskerville",
            "Her frantic, passionate warning: 'Go back! Go straight back to London, instantly! Tonight if possible!'",
            "Stapleton's abrupt return forces Beryl to disguise her frantic warning as female anxiety",
        ],
        "clues_cn": [
            "斯台普吞小姐误将华生当作亨利·巴斯克维尔爵士",
            "她语气焦急而热烈地严厉警告：‘回去吧！马上回到伦敦去，马上就走！’",
            "斯台普吞突然折返，迫使她匆忙掩饰，假称这只是无根据的女人忧虑",
        ],
        "choices_en": [
            {"id": "ch7_p2_c1", "text": "Draft Dr. Watson's first comprehensive report to Sherlock Holmes in London.", "target": "ch08_watson_report"},
            {"id": "ch7_p2_c2", "text": "Ponder Miss Stapleton's terror and why she took such immense risk to warn Sir Henry.", "target": "ch08_watson_report"},
        ],
        "choices_cn": [
            {"id": "ch7_p2_c1", "text": "起草华生医生的第一份详尽报告，寄往伦敦贝克街福尔摩斯处。", "target": "ch08_watson_report"},
            {"id": "ch7_p2_c2", "text": "反复思量斯台普吞小姐眼中的极度恐惧与冒死警告背后的真相。", "target": "ch08_watson_report"},
        ],
    },
    # Chapter 8
    {
        "id": "ch08_watson_report",
        "ch_idx": 7, "part": 0,
        "title_en": "Chapter 8: First Report of Dr. Watson",
        "title_cn": "第八章 华生医生的第一份报告",
        "pov": "watson", "type": "anchor", "anchor": "anchor_first_report",
        "clues_en": [
            "Sir Henry deeply attracted to Beryl Stapleton, but Stapleton shows bizarre, violent jealousy",
            "Eccentric Mr. Frankland of Lafter Hall observing the moor through an astronomical telescope",
            "Barrymore creeps down the dark corridor at 2 a.m. holding a candle to a window facing the black moor",
        ],
        "clues_cn": [
            "亨利爵士与斯台普吞小姐情愫日深，但斯台普吞表现出不可理喻的狂怒阻挠",
            "莱夫特大庄园的古怪绅士弗兰克兰德整日用大型天文望远镜巡视荒原",
            "夜半两点，华生暗中跟踪白瑞摩，目睹他手持蜡烛走到西侧窗前向黑夜中的荒原发信号",
        ],
        "choices_en": [
            {"id": "ch8_c1", "text": "Arrange a midnight stakeout with Sir Henry to catch Barrymore in the act.", "target": "ch09_part1_midnight_watch"},
            {"id": "ch8_c2", "text": "Confer with Sir Henry about the candle signal and prepare revolvers for the night.", "target": "ch09_part1_midnight_watch"},
        ],
        "choices_cn": [
            {"id": "ch8_c1", "text": "与亨利爵士秘密商定午夜伏击计划，当场抓获白瑞摩的通敌行径。", "target": "ch09_part1_midnight_watch"},
            {"id": "ch8_c2", "text": "向亨利爵士披露烛光信号疑点，备好防身手枪准备彻夜蹲守。", "target": "ch09_part1_midnight_watch"},
        ],
    },
    # Chapter 9
    {
        "id": "ch09_part1_midnight_watch",
        "ch_idx": 8, "part": 1,
        "title_en": "Chapter 9: The Light upon the Moor (Part I: Confronting Barrymore)",
        "title_cn": "第九章 沼地上的烛光（上：抓获白瑞摩与身世大白）",
        "pov": "watson", "type": "anchor", "anchor": "anchor_convict",
        "clues_en": [
            "Barrymore seized red-handed at the window holding a candle signal to the moor",
            "Mrs. Barrymore breaks down in tears: Selden the escaped convict is her younger brother",
            "Sir Henry grants mercy, providing cast-off clothing and food so Selden can flee to South America",
        ],
        "clues_cn": [
            "在黑暗走廊当场抓获正向荒原摇晃烛光发信号的管家白瑞摩",
            "白瑞摩太太失声痛哭招认：越狱逃犯塞尔登正是她亲弟弟",
            "亨利爵士出于宽大仁慈答应不予告发，并赠送旧衣物食物助其逃亡南美",
        ],
        "choices_en": [
            {"id": "ch9_p1_c1", "text": "Arm themselves and set out into the dark, moonlit moor to hunt the convict.", "target": "ch09_part2_moor_chase"},
            {"id": "ch9_p1_c2", "text": "Pardon Barrymore and observe the candle flame flickering upon the distant moor.", "target": "ch09_part2_moor_chase"},
        ],
        "choices_cn": [
            {"id": "ch9_p1_c1", "text": "带上左轮手枪，在凄风苦雨的月夜中踏入漆黑荒原缉捕逃犯。", "target": "ch09_part2_moor_chase"},
            {"id": "ch9_p1_c2", "text": "体恤白瑞摩夫妇苦衷，追踪沼地深处那一点幽微的烛火。", "target": "ch09_part2_moor_chase"},
        ],
    },
    {
        "id": "ch09_part2_moor_chase",
        "ch_idx": 8, "part": 2,
        "title_en": "Chapter 9: The Light upon the Moor (Part II: The Man on the Tor)",
        "title_cn": "第九章 沼地上的烛光（下：荒原追捕与岩岗上的神秘客）",
        "pov": "watson", "type": "branch", "anchor": None,
        "clues_en": [
            "Selden cornered near his candle, hurls a rock and vanishes into the labyrinth of tors",
            "Under the emerging moon, Watson spots the tall, thin silhouette of the Man on the Tor standing motionless with folded arms",
            "A deep, blood-curdling baying echoing across the moor as the figure vanishes",
        ],
        "clues_cn": [
            "在乱石堆中包围塞尔登，逃犯投掷巨石后窜入昏黑岩壑逃遁",
            "当月光破云而出时，华生赫然望见黑色岩岗巅峰矗立着一个双臂抱胸的神秘高瘦身影",
            "荒原远方再度传来凄厉狂暴的犬嚎，黑影随即隐没在夜色之中",
        ],
        "choices_en": [
            {"id": "ch9_p2_c1", "text": "Record the mysterious Man on the Tor in Watson's diary and investigate his lair.", "target": "ch10_diary_and_laura"},
            {"id": "ch9_p2_c2", "text": "Search the surrounding tors at sunrise to uncover the stranger's purpose.", "target": "ch10_diary_and_laura"},
        ],
        "choices_cn": [
            {"id": "ch9_p2_c1", "text": "在日记中详实记录岩岗神秘人的身影，拟定追查其巢穴的方略。", "target": "ch10_diary_and_laura"},
            {"id": "ch9_p2_c2", "text": "决定破晓时分搜查荒原岩岗石屋，查明神秘人究竟是友是敌。", "target": "ch10_diary_and_laura"},
        ],
    },
    # Chapter 10
    {
        "id": "ch10_diary_and_laura",
        "ch_idx": 9, "part": 0,
        "title_en": "Chapter 10: Extract from the Diary of Dr. Watson",
        "title_cn": "第十章 华生医生日记摘录",
        "pov": "watson", "type": "anchor", "anchor": "anchor_diary",
        "clues_en": [
            "Barrymore reveals burnt letter fragment from Sir Charles's fireplace: '...be at the gate by ten o'clock. L.L.'",
            "Mortimer reveals L.L. is Laura Lyons of Coombe Tracey, Frankland's daughter who made an unfortunate marriage",
            "Frankland boasts his telescope spotted a boy carrying a package of food up into the prehistoric stone huts on the tor",
        ],
        "clues_cn": [
            "白瑞摩为报不告之恩，透露查尔斯爵士壁炉中烧焦的信件残片：‘……十点钟务请至大门前相见。L.L.’",
            "摩梯末医生证实L.L.即库姆·特雷西的劳拉·里昂斯夫人——弗兰克兰德婚姻不幸的女儿",
            "弗兰克兰德得意夸口其望远镜发现一个男孩每天提着食物篮送往岩岗的史前石屋",
        ],
        "choices_en": [
            {"id": "ch10_c1", "text": "Journey to Coombe Tracey to interrogate Mrs. Laura Lyons.", "target": "ch11_part1_lyons"},
            {"id": "ch10_c2", "text": "Ascend Black Tor to storm the prehistoric stone hut spotted by Frankland.", "target": "ch11_part1_lyons"},
        ],
        "choices_cn": [
            {"id": "ch10_c1", "text": "立即动身前往库姆·特雷西，当面问询劳拉·里昂斯夫人。", "target": "ch11_part1_lyons"},
            {"id": "ch10_c2", "text": "攀登黑色岩岗，直扑弗兰克兰德望远镜所见的神秘史前石屋据点。", "target": "ch11_part1_lyons"},
        ],
    },
    # Chapter 11
    {
        "id": "ch11_part1_lyons",
        "ch_idx": 10, "part": 1,
        "title_en": "Chapter 11: The Man on the Tor (Part I: Interviewing Laura Lyons)",
        "title_cn": "第十一章 岩岗上的人（上：问讯劳拉·里昂斯）",
        "pov": "watson", "type": "branch", "anchor": None,
        "clues_en": [
            "Mrs. Laura Lyons admits writing the letter asking Sir Charles for money to obtain a divorce",
            "She insists someone else stepped in with funds and she never kept the 10 p.m. appointment at the gate",
            "Watson senses she is concealing a deadly secret out of terror",
        ],
        "clues_cn": [
            "劳拉·里昂斯夫人承认写信求助查尔斯爵士以筹资办理离婚",
            "她坚决否认案发当夜去过水松夹道栅门，声称因有人另予相助而爽约",
            "华生敏锐察觉她在极度恐惧中隐藏着致命的内情",
        ],
        "choices_en": [
            {"id": "ch11_p1_c1", "text": "Ascend Black Tor into the prehistoric stone hut to confront the mysterious stranger.", "target": "ch11_part2_stone_hut"},
            {"id": "ch11_p1_c2", "text": "Press Mrs. Lyons on whether Jack Stapleton was the person who helped her.", "target": "ch11_part2_stone_hut"},
        ],
        "choices_cn": [
            {"id": "ch11_p1_c1", "text": "驱车返回达特沼地，直上黑色岩岗探查史前石屋据点。", "target": "ch11_part2_stone_hut"},
            {"id": "ch11_p1_c2", "text": "严厉追问劳拉·里昂斯夫人暗中资助她的是否正是斯台普吞。", "target": "ch11_part2_stone_hut"},
        ],
    },
    {
        "id": "ch11_part2_stone_hut",
        "ch_idx": 10, "part": 2,
        "title_en": "Chapter 11: The Man on the Tor (Part II: The Hermit of the Tor)",
        "title_cn": "第十一章 岩岗上的人（下：石屋隐士的真面目）",
        "pov": "watson", "type": "anchor", "anchor": "anchor_man_on_tor",
        "clues_en": [
            "Stone hut reveals blankets, empty tins, water pannikin, and a slip of paper: 'Dr. Watson has gone to Coombe Tracey'",
            "Watson waits with cocked revolver inside the dark hut",
            "A calm, beloved voice breaks the silence: 'A lovely evening, my dear Watson!' — Sherlock Holmes is the Man on the Tor!",
        ],
        "clues_cn": [
            "史前石屋中藏有粗呢毯、吃剩的舌头罐头、小水桶，以及一张纸条：‘华生医生已前往库姆·特雷西’",
            "华生退入昏暗屋角，手扣左轮机头屏息设伏",
            "熟悉的从容语调在夕阳余晖中响起：‘真是个可爱的黄昏，亲爱的华生！’——岩岗上的人正是福尔摩斯！",
        ],
        "choices_en": [
            {"id": "ch11_p2_c1", "text": "Demand Holmes explain his secret presence on Dartmoor and compare notes.", "target": "ch12_part1_revelations"},
            {"id": "ch11_p2_c2", "text": "Share the findings of the Laura Lyons interrogation with Holmes.", "target": "ch12_part1_revelations"},
            {"id": "ch11_p2_c3", "text": "[Switch POV to Sherlock Holmes] Experience Holmes's secret analysis of the moor and the portrait.", "target": "holmes_ch13_portrait", "pov_switch": "holmes"},
            {"id": "ch11_p2_c4", "text": "[Switch POV to Sherlock Holmes] Catch the stranger from the blind side of the stones.", "target": "holmes_ch11_part2_stone_hut", "pov_switch": "holmes"},
        ],
        "choices_cn": [
            {"id": "ch11_p2_c1", "text": "要求福尔摩斯彻底阐明其秘密潜伏荒原的意图并交换侦查情报。", "target": "ch12_part1_revelations"},
            {"id": "ch11_p2_c2", "text": "将刚刚在库姆·特雷西问询劳拉·里昂斯夫人所获全盘告知福尔摩斯。", "target": "ch12_part1_revelations"},
            {"id": "ch11_p2_c3", "text": "【视角切换：歇洛克·福尔摩斯】以福尔摩斯第一人称检视雨果画像与绝密线索。", "target": "holmes_ch13_portrait", "pov_switch": "holmes"},
            {"id": "ch11_p2_c4", "text": "【视角切换：歇洛克·福尔摩斯】潜出石屋，从巨石盲区反向包抄设伏神秘来客。", "target": "holmes_ch11_part2_stone_hut", "pov_switch": "holmes"},
        ],
    },
    # Chapter 12
    {
        "id": "ch12_part1_revelations",
        "ch_idx": 11, "part": 1,
        "title_en": "Chapter 12: Death on the Moor (Part I: Holmes's Revelations)",
        "title_cn": "第十二章 沼地的惨剧（上：福尔摩斯的惊人揭秘）",
        "pov": "watson", "type": "anchor", "anchor": "anchor_revelation",
        "clues_en": [
            "Holmes reveals Beryl Stapleton is not Stapleton's sister, but his lawful wife",
            "Stapleton used Laura Lyons's letter to lure Sir Charles to the gate at midnight",
            "A dreadful, blood-chilling cry of agonized horror and the deep baying of a hound shatters the moor!",
        ],
        "clues_cn": [
            "福尔摩斯揭示惊人真相：所谓的斯台普吞小姐并非其妹妹，而是其结发妻子",
            "斯台普吞诱使劳拉·里昂斯写信将查尔斯爵士引至午夜栅门前作为猎杀诱饵",
            "一声撕心裂肺、充满绝望哀嚎的凄厉惨叫与浑厚的猎犬咆哮震撼了整座荒原！",
        ],
        "choices_en": [
            {"id": "ch12_p1_c1", "text": "Sprint blindly through the darkness toward the cries of agony and hound roars.", "target": "ch12_part2_selden_death"},
            {"id": "ch12_p1_c2", "text": "Advance cautiously with drawn revolvers and shaded lantern across the rocks.", "target": "ch12_part2_selden_death"},
        ],
        "choices_cn": [
            {"id": "ch12_p1_c1", "text": "在漆黑的荒原乱石堆中不顾一切狂奔，直扑惨叫与恶犬吠声处。", "target": "ch12_part2_selden_death"},
            {"id": "ch12_p1_c2", "text": "双手紧握左轮手枪、隐蔽提灯，在乱石阴影中协同警戒跃进。", "target": "ch12_part2_selden_death"},
        ],
    },
    {
        "id": "ch12_part2_selden_death",
        "ch_idx": 11, "part": 2,
        "title_en": "Chapter 12: Death on the Moor (Part II: Selden's Fall)",
        "title_cn": "第十二章 沼地的惨剧（下：塞尔登之死与狭路相逢）",
        "pov": "watson", "type": "branch", "anchor": None,
        "clues_en": [
            "Corpse found dashed over the jagged crag, wearing Sir Henry's reddish-tweed suit",
            "Holmes turns the body over: It is Selden the convict, killed because the hound pursued Sir Henry's scent on the clothes",
            "Jack Stapleton appears out of the fog, shaken to find Holmes on the moor; Holmes conceals his knowledge",
        ],
        "clues_cn": [
            "在犬牙交错的危岩峭壁下发现摔碎头颈的尸体，身着亨利爵士标志性的红褐色粗花呢套装",
            "福尔摩斯翻转尸身：死者是逃犯塞尔登！恶犬正是循着亨利爵士旧衣上的气味追咬至其坠崖",
            "杰克·斯台普吞自浓雾中现身，见福尔摩斯在场大惊失色；福尔摩斯故意示弱隐瞒真相",
        ],
        "choices_en": [
            {"id": "ch12_p2_c1", "text": "Return to Baskerville Hall to set the final snare for the murderer.", "target": "ch13_portrait"},
            {"id": "ch12_p2_c2", "text": "Conceal suspicions from Stapleton and pretend to return to London tomorrow.", "target": "ch13_portrait"},
        ],
        "choices_cn": [
            {"id": "ch12_p2_c1", "text": "回到巴斯克维尔庄园，布设彻底收紧法网的致命圈套。", "target": "ch13_portrait"},
            {"id": "ch12_p2_c2", "text": "在斯台普吞面前假装受挫退却，声称明日一早返回伦敦。", "target": "ch13_portrait"},
        ],
    },
    # Chapter 13
    {
        "id": "ch13_portrait",
        "ch_idx": 12, "part": 0,
        "title_en": "Chapter 13: Fixing the Nets",
        "title_cn": "第十三章 设网",
        "pov": "watson", "type": "anchor", "anchor": "anchor_portrait",
        "clues_en": [
            "Hugo Baskerville's portrait reveals the startling likeness of Jack Stapleton when hair and hat are covered",
            "Stapleton proven to be a Baskerville heir (son of Rodger Baskerville) murdering for the title and £740,000",
            "Inspector Lestrade arrives from Scotland Yard with warrants",
            "Sir Henry instructed to dine alone at Merripit House and walk home across the dark moor path",
        ],
        "clues_cn": [
            "遮盖画中雨果·巴斯克维尔的帽发后，画像面容与杰克·斯台普吞惊人吻合！",
            "查明斯台普吞乃罗杰·巴斯克维尔之子，其谋杀全系为继承爵位与七十四万镑巨额遗产",
            "苏格兰场刑警雷斯垂德携搜捕令乘特快列车抵达德文郡集结",
            "福尔摩斯严命亨利爵士单身赴梅利琵宅邸赴宴，并务必夜半步行穿过荒原小径返家",
        ],
        "choices_en": [
            {"id": "ch13_c1", "text": "Deploy the ambush on the moor path near Merripit House in the dark.", "target": "ch14_part1_fog_ambush"},
            {"id": "ch13_c2", "text": "Verify Lestrade's Scotland Yard warrants and position the party near the mire path.", "target": "ch14_part1_fog_ambush"},
            {"id": "ch13_c3", "text": "[Switch POV to Jack Stapleton] View Stapleton setting the fatal dinner trap at Merripit House.", "target": "stapleton_ch13_fatal_dinner", "pov_switch": "stapleton"},
        ],
        "choices_cn": [
            {"id": "ch13_c1", "text": "在梅利琵宅邸外的小径乱石堆后设伏，静候终局较量。", "target": "ch14_part1_fog_ambush"},
            {"id": "ch13_c2", "text": "检视雷斯垂德的苏格兰场拘捕令，在格林盆泥潭边缘卡死伏击据点。", "target": "ch14_part1_fog_ambush"},
            {"id": "ch13_c3", "text": "【视角切换：杰克·斯台普吞】窥探斯台普吞在梅利琵宅邸筹备致命晚餐的险恶心机。", "target": "stapleton_ch13_fatal_dinner", "pov_switch": "stapleton"},
        ],
    },
    # Chapter 14
    {
        "id": "ch14_part1_fog_ambush",
        "ch_idx": 13, "part": 1,
        "title_en": "Chapter 14: The Hound of the Baskervilles (Part I: The Ambush in the Fog)",
        "title_cn": "第十四章 巴斯克维尔的猎犬（上：迷雾中的伏击）",
        "pov": "watson", "type": "climax", "anchor": "anchor_climax",
        "clues_en": [
            "Dense white fog rolling in from the Great Grimpen Mire threatening to blind the investigators",
            "Sir Henry walks out onto the moor path in the dark",
            "A monstrous beast bursts through the mist: Coals of fire flickering from its jaws, muzzle, and eyes!",
        ],
        "clues_cn": [
            "大格林盆泥潭涌出的苍白浓雾以惊人速度吞噬地面，严重阻隔伏击视线",
            "亨利爵士孑然一身走出宅邸步入漆黑的荒原小径",
            "浓雾中赫然跃出一头庞大无匹的黑色怪兽：鼻吻、巨目与巨齿间喷涌着熊熊磷火！",
        ],
        "choices_en": [
            {"id": "ch14_p1_c1", "text": "Fire a coordinated volley instantly into the leaping beast.", "target": "ch15_victory"},
            {"id": "ch14_p1_c2", "text": "Watson charges forward firing his revolver to shield Sir Henry from the jaws.", "target": "ch15_watson"},
            {"id": "ch14_p1_c3", "text": "Holmes calculates the mist path and fires directly into the hound's heart.", "target": "ch15_holmes"},
            {"id": "ch14_p1_c4", "text": "Hesitate in frozen terror as the blazing hound leaps through the vapor.", "target": "ch15_tragedy"},
            {"id": "ch14_p1_c5", "text": "The hound falls dead; rush into Merripit House to rescue Mrs. Stapleton and pursue the villain into the mire.", "target": "ch14_part2_mire_pursuit"},
        ],
        "choices_cn": [
            {"id": "ch14_p1_c1", "text": "三人齐射！在怪兽腾空飞扑的瞬间予以致命排枪齐射。", "target": "ch15_victory"},
            {"id": "ch14_p1_c2", "text": "华生奋不顾身持枪疾进，以血肉之躯在恶犬扑倒亨利爵士前将其击毙。", "target": "ch15_watson"},
            {"id": "ch14_p1_c3", "text": "福尔摩斯精准算准雾障风向，一枪洞穿发光巨兽的心脏。", "target": "ch15_holmes"},
            {"id": "ch14_p1_c4", "text": "因眼前突现的地狱火兽而惊骇失神，错失最佳射击战机。", "target": "ch15_tragedy"},
            {"id": "ch14_p1_c5", "text": "恶犬毙命！三人即刻冲入梅利琵宅邸解救受困夫人，并追击凶犯直插泥潭。", "target": "ch14_part2_mire_pursuit"},
        ],
    },
    {
        "id": "ch14_part2_mire_pursuit",
        "ch_idx": 13, "part": 2,
        "title_en": "Chapter 14: The Hound of the Baskervilles (Part II: The Mire Pursuit)",
        "title_cn": "第十四章 巴斯克维尔的猎犬（下：泥潭追凶与营救夫人）",
        "pov": "watson", "type": "branch", "anchor": None,
        "clues_en": [
            "Dead beast examined: Bloodhound-mastiff hybrid coated in odorless luminous phosphorus preparation",
            "Mrs. Beryl Stapleton found bound, gagged, and brutally beaten in the upstairs bedroom",
            "Beryl directs them to Stapleton's tin-mine island refuge in the Great Grimpen Mire",
        ],
        "clues_cn": [
            "验看死犬尸身：纯种血狸与獒犬杂交巨兽，通体涂满无嗅无害的发光磷质",
            "在宅邸阁楼发现被五花大绑、惨遭鞭笞封口的斯台普吞夫人",
            "夫人绝望指认斯台普吞潜逃至大格林盆泥潭深处废弃锡矿孤岛的秘密路线",
        ],
        "choices_en": [
            {"id": "ch14_p2_c1", "text": "Follow the small guide-sticks into the treacherous, fathomless Grimpen Mire.", "target": "ch15_mire"},
            {"id": "ch14_p2_c2", "text": "Form a police cordon around the moor perimeter at daybreak to trap Stapleton.", "target": "ch15_arrest"},
        ],
        "choices_cn": [
            {"id": "ch14_p2_c1", "text": "循着泥潭中微弱的小木桩路标，冒险突入深不见底的格林盆绝境。", "target": "ch15_mire"},
            {"id": "ch14_p2_c2", "text": "封锁泥潭周边出口，调集郡警于黎明破晓时分发动天罗地网合围。", "target": "ch15_arrest"},
        ],
    },
    # Chapter 15: 6 Endings
    {
        "id": "ch15_victory",
        "ch_idx": 14, "part": 0,
        "title_en": "Chapter 15: A Retrospection (Ending: Canonical Victory)",
        "title_cn": "第十五章 回顾（终局：正义凯旋与案情回顾）",
        "pov": "watson", "type": "ending", "anchor": "anchor_retrospection",
        "clues_en": ["Full canonical resolution in Baker Street: Rodger Baskerville's son, stolen boot, phosphorus compound analyzed"],
        "clues_cn": ["贝克街炉火旁的完整回顾：罗杰·巴斯克维尔孽子身世大白，盗靴引犬疑案水落石出，发光磷液完全剖析"],
        "choices_en": [],
        "choices_cn": [],
    },
    {
        "id": "ch15_watson",
        "ch_idx": 14, "part": 0,
        "title_en": "Chapter 15: A Retrospection (Ending: Watson's Heroic Action)",
        "title_cn": "第十五章 回顾（终局：华生之英勇功绩）",
        "pov": "watson", "type": "ending", "anchor": None,
        "clues_en": ["Watson's prompt gunfire celebrated by Holmes and Scotland Yard for saving Sir Henry Baskerville's life"],
        "clues_cn": ["华生临危决断、果断开火解救亨利爵士性命的英勇功绩，赢得福尔摩斯与苏格兰场的一致赞许"],
        "choices_en": [],
        "choices_cn": [],
    },
    {
        "id": "ch15_holmes",
        "ch_idx": 14, "part": 0,
        "title_en": "Chapter 15: A Retrospection (Ending: Holmes's Master Deduction)",
        "title_cn": "第十五章 回顾（终局：福尔摩斯之理性大捷）",
        "pov": "holmes", "type": "ending", "anchor": None,
        "clues_en": ["Supreme triumph of scientific deduction and cold logic dispelling gothic terror and superstition forever"],
        "clues_cn": ["科学理性与严谨逻辑的崇高胜利，将几个世纪以来笼罩达特沼地的哥特迷信阴霾彻底扫荡"],
        "choices_en": [],
        "choices_cn": [],
    },
    {
        "id": "ch15_tragedy",
        "ch_idx": 14, "part": 0,
        "title_en": "Chapter 15: A Retrospection (Ending: Baskerville Tragedy)",
        "title_cn": "第十五章 回顾（终局：巴斯克维尔之痛惜余波）",
        "pov": "watson", "type": "ending", "anchor": None,
        "clues_en": ["A somber reflection on the close brush with death, Sir Henry's long recovery, and the dark cost of evil"],
        "clues_cn": ["在炉火旁沉痛回望死里逃生的惨烈搏杀，亨利爵士漫长的疗伤休养，以及罪恶留下的永恒伤疤"],
        "choices_en": [],
        "choices_cn": [],
    },
    {
        "id": "ch15_mire",
        "ch_idx": 14, "part": 0,
        "title_en": "Chapter 15: A Retrospection (Ending: Swallowed by Grimpen Mire)",
        "title_cn": "第十五章 回顾（终局：葬身格林盆泥潭深渊）",
        "pov": "stapleton", "type": "ending", "anchor": None,
        "clues_en": ["Stapleton swallowed forever by the foul green slime of the Great Grimpen Mire, leaving only Sir Henry's boot"],
        "clues_cn": ["大格林盆泥潭永远吞噬了罪大恶极的凶犯，绿色的泥浆之上，只留下了亨利爵士那只旧皮靴"],
        "choices_en": [],
        "choices_cn": [],
    },
    {
        "id": "ch15_arrest",
        "ch_idx": 14, "part": 0,
        "title_en": "Chapter 15: A Retrospection (Ending: Justice at the Old Bailey)",
        "title_cn": "第十五章 回顾（终局：老贝利法庭的最终审判）",
        "pov": "stapleton", "type": "ending", "anchor": None,
        "clues_en": ["Jack Stapleton captured at dawn, convicted at the Old Bailey on Mrs. Stapleton's testimony, and sentenced to the gallows"],
        "clues_cn": ["杰克·斯台普吞在黎明合围中束手就擒，在老贝利法庭由夫人出庭指证罪状，终伏国法判处绞刑"],
        "choices_en": [],
        "choices_cn": [],
    },
]

def get_watson_node_text(cfg, lang):
    ch_idx = cfg["ch_idx"]
    part = cfg["part"]
    paras = en_chapters[ch_idx] if lang == "en" else cn_chapters[ch_idx]

    if part == 0:
        selected_paras = paras
    elif part == 1:
        split_pt = split_indices[ch_idx][0 if lang == "en" else 1]
        selected_paras = paras[:split_pt]
    elif part == 2:
        split_pt = split_indices[ch_idx][0 if lang == "en" else 1]
        selected_paras = paras[split_pt:]

    node_id = cfg["id"]
    if node_id == "ch15_watson":
        prefix = (
            "Holmes raised his glass to me by the crackling fireside in Baker Street. "
            "'Watson,' said he, 'never in our long partnership have I witnessed such promptitude and courage. "
            "Your decisive gunfire shattered the hound in mid-leap, preserving Sir Henry Baskerville's life at the supreme crisis. "
            "The chronicles of the Baskervilles shall record that Dr. John H. Watson was the shield that broke the curse.'\n\n"
            if lang == "en" else
            "在贝克街熊熊燃烧的壁炉旁，福尔摩斯向我高高举起了酒杯。“华生，”他微笑着说道，“在我们长久的合作之中，我从未见过如此果决勇敢的身手。你在最后危急关头的疾进开火，直接在恶犬腾空一跃时挽救了亨利·巴斯克维尔爵士的性命。巴斯克维尔家族的历史必将铭记：约翰·H·华生医生才是彻底粉碎诅咒的坚固盾牌。”\n\n"
        )
        return prefix + "\n\n".join(selected_paras)
    elif node_id == "ch15_holmes":
        prefix = (
            "Holmes leaned back against his cushions, blowing delicate smoke-rings into the winter twilight. "
            "'A pure problem of reason, Watson,' he murmured with quiet satisfaction. 'From the moment Mortimer brought that 1742 manuscript, "
            "it was a battle between gothic superstition and cold, analytical science. By measuring the physical bounds of the bog, "
            "the timing of the fog, and the trajectory of the hound, science has triumphed utterly over darkness.'\n\n"
            if lang == "en" else
            "福尔摩斯倚靠在软垫上，向冬日暮色中悠闲地吐出缕缕精巧的烟圈。“这是一场纯粹理性的较量，华生，”他带着平静的欣慰低语道，“从摩梯末医生带进那份一七四二年的手稿那一刻起，这就是一场哥特式迷信与冷峻分析科学之间的搏斗。通过测算泥潭的实际边界、大雾推进的时间与猎犬奔袭的弹道，科学最终彻底击碎了盘踞数个世纪的黑暗。”\n\n"
        )
        return prefix + "\n\n".join(selected_paras)
    elif node_id == "ch15_tragedy":
        prefix = (
            "A heavy melancholy hung over our sitting-room as the autumn rain beat against the Baker Street panes. "
            "Sir Henry had survived the monstrous hound, yet his nervous system was shattered by the horror. "
            "Dr. Mortimer was taking him upon a year-long voyage across the globe to heal his spirit. "
            "'We struck the beast down, Watson,' Holmes observed gravely, 'yet evil never passes without exacting a bitter toll from the innocent.'\n\n"
            if lang == "en" else
            "当秋雨淅淅沥沥敲打着贝克街的窗扉时，一股沉重的忧伤笼罩在我们的起居室中。亨利爵士虽从发光怪兽的獠牙下死里逃生，但神经遭受了剧烈的创伤。摩梯末医生已陪同他踏上了环球航行以抚慰心灵。“我们虽然打死了恶犬，华生，”福尔摩斯神色肃穆地说道，“但邪恶在被消灭之前，往往总要向无辜者索取沉痛的代价。”\n\n"
        )
        return prefix + "\n\n".join(selected_paras)
    elif node_id == "ch15_mire":
        prefix = (
            "Holmes paused, gazing into the amber embers of the hearth. "
            "'Somewhere in the heart of the Great Grimpen Mire, down in the foul slime of the huge morass which had sucked him in, "
            "that cold and cruel heart is sleeping forever,' said he. 'No trace of Jack Stapleton will ever emerge to stand before an earthly judge. "
            "The ancient mire which sheltered his crime became his tomb.'\n\n"
            if lang == "en" else
            "福尔摩斯停顿了下来，凝视着壁炉里暗红的余烬。“在大格林盆泥潭的极深处，在那吞噬了他的巨大泥淖的肮脏泥浆底下，”他低声说道，“那颗冷酷残忍的心已经永远停止了跳动。杰克·斯台普吞永远不会站在人间的法庭上了。那庇护了他罪恶阴谋的古老沼泽，最终成为了他万劫不复的坟墓。”\n\n"
        )
        return prefix + "\n\n".join(selected_paras)
    elif node_id == "ch15_arrest":
        prefix = (
            "The morning newspapers lay scattered across our table, their headlines blazing with the sensational trial at the Old Bailey. "
            "Stapleton, cornered upon the edges of the mire by Lestrade and the county police, had stood in the dock facing the damning testimony of his wife. "
            "'A complete victory for justice, Watson,' said Holmes, tapping the Times. 'The gallows of Exeter await him, and the law has proved that no cunning "
            "can escape the net of retribution.'\n\n"
            if lang == "en" else
            "早晨的报纸散落在我们的桌案上，头版通栏大字刊登着老贝利法庭轰动全国的审判。在格林盆泥潭边缘被雷斯垂德与郡警天罗地网生擒的斯台普吞，在法庭上遭到了其夫人的当堂指证。“这是正义毫无瑕疵的胜利，华生，”福尔摩斯轻敲着《泰晤士报》微笑道，“埃克塞特监狱的绞刑架正等待着他，法律用事实证明，再狡黠的诡计也绝不可能逃脱恢恢法网。”\n\n"
        )
        return prefix + "\n\n".join(selected_paras)

    return "\n\n".join(selected_paras)

# 2. HOLMES & STAPLETON 15-CHAPTER TRACKS
from holmes_data import HOLMES_NODES
from stapleton_data import STAPLETON_NODES

def render_watson_nodes_code(lang):
    code_blocks = []
    for cfg in WATSON_NODES:
        content = get_watson_node_text(cfg, lang)
        node_type = f"NodeType.{cfg['type'].upper()}"
        anchor_str = f'"{cfg["anchor"]}"' if cfg["anchor"] else "None"
        clues_str = json.dumps(cfg["clues_en" if lang == "en" else "clues_cn"], ensure_ascii=False)
        pov_enum = f"POV.{cfg['pov'].upper()}"
        choices = cfg["choices_en" if lang == "en" else "choices_cn"]
        choices_code = []
        for c in choices:
            sw = f', pov_switch=POV.{c["pov_switch"].upper()}' if "pov_switch" in c else ""
            choices_code.append(
                f'            Choice(id="{c["id"]}", text={json.dumps(c["text"], ensure_ascii=False)}, target_node_id="{c["target"]}"{sw}),'
            )
        choices_block = "\n".join(choices_code)
        if choices_block:
            choices_block = f"[\n{choices_block}\n        ]"
        else:
            choices_block = "[]"

        title_str = json.dumps(cfg["title_en" if lang == "en" else "title_cn"], ensure_ascii=False)
        code_block = f'''    nodes["{cfg['id']}"] = PassageNode(
        id="{cfg['id']}",
        title={title_str},
        pov={pov_enum},
        node_type={node_type},
        anchor_name={anchor_str},
        content={json.dumps(content, ensure_ascii=False)},
        choices={choices_block},
        clues_discovered={clues_str},
    )
'''
        code_blocks.append(code_block)
    return "".join(code_blocks)

def render_track_nodes_code(track_list, lang):
    code_blocks = []
    for cfg in track_list:
        content = cfg["content_en"] if lang == "en" else cfg["content_cn"]
        node_type = f"NodeType.{cfg['type'].upper()}"
        anchor_str = f'"{cfg["anchor"]}"' if cfg.get("anchor") else "None"
        clues_str = json.dumps(cfg["clues_en" if lang == "en" else "clues_cn"], ensure_ascii=False)
        pov_enum = f"POV.{cfg['pov'].upper()}"
        choices = cfg["choices_en" if lang == "en" else "choices_cn"]
        choices_code = []
        for c in choices:
            sw = f', pov_switch=POV.{c["pov_switch"].upper()}' if "pov_switch" in c else ""
            choices_code.append(
                f'            Choice(id="{c["id"]}", text={json.dumps(c["text"], ensure_ascii=False)}, target_node_id="{c["target"]}"{sw}),'
            )
        choices_block = "\n".join(choices_code)
        if choices_block:
            choices_block = f"[\n{choices_block}\n        ]"
        else:
            choices_block = "[]"

        title_str = json.dumps(cfg["title_en" if lang == "en" else "title_cn"], ensure_ascii=False)
        code_block = f'''    nodes["{cfg['id']}"] = PassageNode(
        id="{cfg['id']}",
        title={title_str},
        pov={pov_enum},
        node_type={node_type},
        anchor_name={anchor_str},
        content={json.dumps(content, ensure_ascii=False)},
        choices={choices_block},
        clues_discovered={clues_str},
    )
'''
        code_blocks.append(code_block)
    return "".join(code_blocks)

print("Writing hound_story_en.py...")
en_code = f'''"""English narrative content adapting 'The Hound of the Baskervilles' by Sir Arthur Conan Doyle.
Multi-POV Canonical 15-Chapter Edition:
- Dr. John H. Watson: 15 Canonical Chapters with extensive authentic prose (book_en.txt)
- Sherlock Holmes: 15 Canonical Chapters with extensive first-person deductive prose
- Jack Stapleton: 15 Canonical Chapters with chilling antagonist first-person prose
"""

from src.models import Choice, NodeType, POV, PassageNode, StoryGraph


def build_story_en() -> StoryGraph:
    """Constructs the English StoryGraph with all three playable perspectives."""
    nodes: dict[str, PassageNode] = {{}}

    # =========================================================================
    # 1. WATSON CANONICAL TRACK (15 Chapters, extensive text)
    # =========================================================================
{render_watson_nodes_code("en")}

    # =========================================================================
    # 2. SHERLOCK HOLMES TRACK (15 Chapters, extensive text)
    # =========================================================================
{render_track_nodes_code(HOLMES_NODES, "en")}

    # =========================================================================
    # 3. JACK STAPLETON TRACK (15 Chapters, extensive text)
    # =========================================================================
{render_track_nodes_code(STAPLETON_NODES, "en")}

    return StoryGraph(
        language="en",
        title="The Hound of the Baskervilles: Multi-POV Interactive Edition",
        author="Sir Arthur Conan Doyle",
        description=(
            "Experience The Hound of the Baskervilles across three playable perspectives across all 15 canonical chapters: "
            "Dr. John H. Watson (authentic full-length investigation), Sherlock Holmes (covert moor surveillance and deduction), "
            "and Jack Stapleton (the antagonist mastermind of Grimpen Mire)."
        ),
        start_nodes={{
            POV.WATSON: "ch01_part1_stick",
            POV.HOLMES: "holmes_ch01_part1_observation",
            POV.STAPLETON: "stapleton_ch01_part1_heritage",
        }},
        nodes=nodes,
    )
'''

with open(ROOT / 'src/content/hound_story_en.py', 'w', encoding='utf-8') as f:
    f.write(en_code)
print(f"Generated hound_story_en.py ({len(en_code)} bytes)")

print("Writing hound_story_cn.py...")
cn_code = f'''"""中文原著互动版《巴斯克维尔的猎犬》（阿瑟·柯南·道尔著）。
多视角全十五章节原著典藏版：
- 约翰·H·华生医生：完整15章原著宏篇长篇纪实（book_cn.txt），保留原著详尽篇幅。
- 歇洛克·福尔摩斯：完整15章名侦探第一人称深度探案、荒原石屋隐蔽暗察与严密逻辑推理。
- 杰克·斯台普吞：完整15章幕后主使第一人称暗黑密谋、训育荧光猎犬夺取遗产的反派主线。
"""

from src.models import Choice, NodeType, POV, PassageNode, StoryGraph


def build_story_cn() -> StoryGraph:
    """构建涵盖三重视角与原著完整15章节的中文互动故事图谱。"""
    nodes: dict[str, PassageNode] = {{}}

    # =========================================================================
    # 1. 华生正典主线（全15章原著宏篇长文）
    # =========================================================================
{render_watson_nodes_code("cn")}

    # =========================================================================
    # 2. 福尔摩斯正典主线（全15章第一人称宏篇长文）
    # =========================================================================
{render_track_nodes_code(HOLMES_NODES, "cn")}

    # =========================================================================
    # 3. 斯台普吞正典主线（全15章第一人称宏篇长文）
    # =========================================================================
{render_track_nodes_code(STAPLETON_NODES, "cn")}

    return StoryGraph(
        language="cn",
        title="巴斯克维尔的猎犬：多视角原著互动典藏版",
        author="阿瑟·柯南·道尔",
        description=(
            "完整重现阿瑟·柯南·道尔原著十五个章节的宏篇巨著。三大人物视角全篇15章完整覆盖："
            "华生医生（全15章原汁原味长篇探案纪实）、福尔摩斯（全15章神探第一人称破案纪实）与斯台普吞（全15章反派罪枭第一人称沉浸密谋）。"
        ),
        start_nodes={{
            POV.WATSON: "ch01_part1_stick",
            POV.HOLMES: "holmes_ch01_part1_observation",
            POV.STAPLETON: "stapleton_ch01_part1_heritage",
        }},
        nodes=nodes,
    )
'''

with open(ROOT / 'src/content/hound_story_cn.py', 'w', encoding='utf-8') as f:
    f.write(cn_code)
print(f"Generated hound_story_cn.py ({len(cn_code)} bytes)")
