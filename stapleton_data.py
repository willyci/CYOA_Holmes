# Initialize stapleton_data.py
import json

STAPLETON_NODES = []
# Stapleton Chapter 1 & 2
STAPLETON_NODES.extend([
    # Chapter 1 Part 1
    {
        "id": "stapleton_ch01_part1_heritage",
        "ch_idx": 0, "part": 1,
        "title_en": "Chapter 1: The Genesis of the Plot (Part I: The Blood of Rodger Baskerville)",
        "title_cn": "第一章 阴谋的序曲（上：罗杰·巴斯克维尔的血脉与野心）",
        "pov": "stapleton", "type": "anchor", "anchor": "anchor_chapter1_stapleton",
        "clues_en": [
            "Stapleton is born the son of Rodger Baskerville, the South American black sheep",
            "Past bankruptcy of his Yorkshire school forced the adoption of the name Stapleton",
            "Inheritance of the £740,000 Baskerville estate requires eliminating Charles and Henry",
        ],
        "clues_cn": [
            "斯台普吞真实血统乃是流亡南美的幼弟罗杰·巴斯克维尔之亲生骨肉",
            "在约克郡开办贵族学校破产倒闭后，携娇妻贝丽尔隐姓埋名伪装兄妹潜入达特穆尔",
            "吞并高达七十四万英镑庞大信托遗产的宏图，必须彻底扫除堂兄查尔斯与堂侄亨利两大路障",
        ],
        "choices_en": [
            {"id": "s_ch1_p1_c1", "text": "Inspect the secret lair on the mire island and examine the beast.", "target": "stapleton_ch01_part2_beast"},
            {"id": "s_ch1_p1_c2", "text": "[Switch POV to Sherlock Holmes] See Holmes examining Mortimer's walking stick.", "target": "holmes_ch01_part1_observation", "pov_switch": "holmes"},
        ],
        "choices_cn": [
            {"id": "s_ch1_p1_c1", "text": "踏上大格林盆泥潭暗径深入绝密孤岛，检视囚禁在废弃锡矿工棚中的嗜血巨兽。", "target": "stapleton_ch01_part2_beast"},
            {"id": "s_ch1_p1_c2", "text": "【视角切换：歇洛克·福尔摩斯】切换至伦敦贝克街，目睹名侦探以手杖展开神准演绎。", "target": "holmes_ch01_part1_observation", "pov_switch": "holmes"},
        ],
        "content_en": """I sat in my study at Merripit House, pinning a rare specimen of the marsh fritillary to the cork board. Through the small window, the vast, treeless wilderness of Dartmoor rolled away toward the gray granite rampart of the tors. To the world, I was Jack Stapleton, an inoffensive, bespectacled schoolmaster turned naturalist, spending his blameless days chasing butterflies with a green gauze net.

Fools! Blind, provincial dolts!

In my veins ran the proud, turbulent blood of the Baskervilles. My father was Rodger Baskerville, the youngest of the three brothers—the reckless, dark-faced rover who had fled England in disgrace to seek his fortune in Central America. I was born in the heat of Costa Rica, christened with his name, and endowed with his fiery, ruthless intellect. When I returned to England with my exquisite wife, Beryl Garcia, I established a boarding school in Yorkshire under the name of Vandeleur. An epidemic of typhus broke out; three boys died, the school collapsed into ruin, and I found myself an impoverished outcast with a fortune in debts.

It was then, in the depths of our flight, that I discovered the fortune awaiting me. My uncle, Sir Charles Baskerville, had returned from the South African diamond fields, an invalid childless widower with £740,000 invested in gold and consols, restoring the ancestral seat at Baskerville Hall.

Between that colossal fortune and myself stood only two lives: an ailing old man with a ruined heart, and a distant nephew farming the Canadian bush!

I sold the remnants of my Yorkshire property, moved south to Devonshire, and rented this lonely cottage upon the very edge of the Great Grimpen Mire. I compelled Beryl, under threat of death, to pass as my unmarried sister. And here, in the ancient library of Sir Charles, I unearthed the weapon of my salvation: the 1742 manuscript detailing the legend of the spectral hound that had torn the throat of wicked Hugo Baskerville!

An ancestral curse! What genius could invent a more perfect instrument of untraceable murder?""",
        "content_cn": """我坐在梅利琵宅邸的书房里，正用细钢针将一只罕见的沼泽网蛱蝶标本精准刺入软木板中。透过临窗的狭小玻璃，达特穆尔荒原浩瀚苍凉的苔原向着远方灰暗的花岗岩峰峦无垠蔓延。在世人眼中，我是杰克·斯台普吞——一个戴着金丝眼镜、温文尔雅的落魄乡村教师兼昆虫学者，整日挥舞着一面绿纱网在泥潭边扑捉飞蛾度日。

蠢材！一帮瞎了眼的乡巴佬！

在我的骨髓与血管深处，奔淌着的乃是巴斯克维尔家族最纯正、最桀骜不驯的狂暴贵族之血！我的亲生父亲罗杰·巴斯克维尔，是查尔斯爵士那一辈三兄弟中最年幼的幼弟——那个在放荡败家后潜逃中美洲、被家族族谱彻底抹杀的浪子。我出生在哥斯达黎加酷热的种植园里，继承了父亲的名字，更继承了他冷酷果决的惊人头脑。当我携带着美艳绝伦的异国娇妻贝丽尔·加西亚重返英格兰时，我曾在约克郡以凡德勒（Vandeleur）之名开办了一所贵族男子寄宿学校。然而一场突如其来的斑疹伤寒夺走了三名男童的性命，学校在一夜间破产清算，我也瞬间沦为了负债累累的落魄乞丐。

正是在那场仓皇逃亡的穷途末路之中，命运向我掀开了最璀璨的宝藏帷幕。我的亲伯父查尔斯·巴斯克维尔爵士从南非金矿载誉归来，一个膝下无子、身患绝症的鳏夫老人，怀揣着高达七十四万英镑的金边债券与现款，正在达特穆尔斥资重修祖业！

在那座令人发狂的金山与我之间，仅仅阻隔着两条微不足道的脆弱性命：一个心脏彻底损坏、苟延残喘的糟老头子，以及一个远在加拿大冰原上挥舞锄头的粗鄙农夫侄子！

我变卖了约克郡的全部破烂家当，带着贝丽尔隐姓埋名潜入德文郡，在紧挨大格林盆泥潭边缘租下了这座孤零零的梅利琵宅邸。我以暴力威慑严令贝丽尔对外宣称是我的未婚胞妹。而在老爵士好客热情的引荐下，我在庄园古老的藏书室中掘出了最完美的索命神器：那份记载着恶棍雨果·巴斯克维尔遭地狱猎犬撕碎咽喉的一七四二年祖传诅咒手稿！

一个传承两百年的家族血腥魔咒！放眼全天下，还有什么比这个幽灵神话更适合充当毫无物理痕迹的完美谋杀工具？！"""
    },

    # Chapter 1 Part 2
    {
        "id": "stapleton_ch01_part2_beast",
        "ch_idx": 0, "part": 2,
        "title_en": "Chapter 1: The Genesis of the Plot (Part II: The Monster in Grimpen Mire)",
        "title_cn": "第一章 阴谋的序曲（下：泥潭孤岛的巨兽与磷光配方）",
        "pov": "stapleton", "type": "branch", "anchor": None,
        "clues_en": [
            "Giant mastiff-bloodhound cross purchased from Ross and Mangles in Fulham Road",
            "Hidden in abandoned tin mine island in the heart of Great Grimpen Mire",
            "Luminous chemical preparation: phosphorus dissolved in bone oil glow without scorching",
        ],
        "clues_cn": [
            "从伦敦富勒姆路著名的‘罗斯与曼格尔斯’犬商处暗中购得血统最暴虐的獒犬杂交种",
            "囚禁在大格林盆泥潭最幽深绝密的核心孤岛废弃锡矿工棚之中",
            "研制出独门秘方：将白磷溶入骨油与甘油制成无嗅冷光涂料，使恶兽在暗夜中通体喷火而不伤毛皮",
        ],
        "choices_en": [
            {"id": "s_ch1_p2_c1", "text": "Entangle Laura Lyons into writing the appointment letter to lure Sir Charles.", "target": "stapleton_ch02_part1_laura_trap"},
            {"id": "s_ch1_p2_c2", "text": "Test the hound's ferocity upon the bog island with fresh red meat.", "target": "stapleton_ch02_part1_laura_trap"},
        ],
        "choices_cn": [
            {"id": "s_ch1_p2_c1", "text": "利用爱情陷阱彻底套牢劳拉·里昂斯，指使她写下深夜约见查尔斯爵士的致命诱饵信。", "target": "stapleton_ch02_part1_laura_trap"},
            {"id": "s_ch1_p2_c2", "text": "在泥潭孤岛上以新鲜生牛肉逗弄恶犬，测试其在极度饥饿状态下的凶暴撕咬力。", "target": "stapleton_ch02_part1_laura_trap"},
        ],
        "content_en": """I crossed the quagmire along my secret path of sunken stones, stepping onto the isolated granite knoll at the heart of Grimpen Mire. Here, concealed within the crumbling stone huts of an abandoned Elizabethan tin-mine, lay my masterpiece.

I pushed open the heavy wooden door of the old smelting shed. A low, terrifying growl rattled from the darkness, accompanied by the metallic rasp of an iron chain.

Two eyes, burning with savage hunger, fixed upon me.

It was an immense creature, coal-black, a devilish cross between a bloodhound and a mastiff, which I had purchased in London from Ross and Mangles in the Fulham Road. I had brought it down by northern routes, walking it by night across the tors so that no human eye had rested upon it. It stood nearly thirty inches at the shoulder, with the jaw of a tiger and the iron sinews of a lion.

From my leather bag, I produced my secret chemical concoction: a paste of white phosphorus dissolved in refined bone oil and glycerin. It was completely odorless, so as not to deaden the creature's keen hunting scent.

I approached the snarling brute, stroked its massive head, and smeared the paste over its muzzle, across the circles of its eyes, and down its bristling dewlap.

I stepped back and extinguished my lantern.

A cry of involuntary awe broke from my lips! In the pitch blackness of the shed, the beast stood transformed into a thing of pure nightmare! Its mouth appeared to vomit forth green and bluish flames; its eyes smouldered like twin coals from the pit; its massive jaws were dripping with cold fire!

Sir Charles was an old man, steeped in superstitious terror, with a heart that fluttered like a wounded sparrow. He would never survive the shock. The hound would not need to set a tooth in him. One glimpse of this roaring phantom springing from the yew trees would burst his heart in his chest!

The weapon was ready. Now, I needed the lure to draw the old baronet from his sanctuary into the dark.""",
        "content_cn": """我踩着那些唯有我自己知晓的沉水暗石，轻巧穿过大格林盆泥潭的致命泥浆，踏上了位于沼泽核心孤立无援的花岗岩小岛。在这里，隐匿在一座伊丽莎白时代废弃旧锡矿的坍塌石棚之中，囚禁着我的毕生杰作。

我推开厚重的旧工棚木门。一阵从喉管深处爆发出的低沉闷吼在幽暗中轰然作响，伴随着铁链哗啦啦剧烈拉扯的金属摩擦声。

两只在黑暗中泛着嗜血绿光的凶残巨眼瞬间死死锁定了我的咽喉。

那是一头堪称庞然巨物的怪兽，通体如炭黑，兼具马士提夫獒犬的恐怖骨骼与寻血猎犬的杀戮本能。这是我亲自赶赴伦敦富勒姆路‘罗斯与曼格尔斯’名犬行重金购得的极品。我通过北部的货运支线将其秘密运抵德文郡，趁着夜色徒步翻山越岭，从未让任何世人的目光瞥见过它的半点影子。它肩高足有三十英寸，颚骨粗壮如猛虎，四肢肌肉坚硬如钢铁。

我从皮包里掏出了我潜心研制的绝密化学配方：一种将高纯度白磷溶解于精炼骨油与甘油中的特制冷光油膏。它不含任何刺激性挥发气味，完全不会破坏恶犬那敏锐无匹的嗅觉追踪系统。

我安抚着狂躁低吼的恶兽，伸手抚摸着它坚硬如铁的头颅，小心翼翼地将磷光油膏均匀涂抹在它的口吻、獠牙边缘、双眼眼眶以及颈下那圈骇人的鬃毛垂肉之上。

我向后退开三步，啪的一声合上了马灯的遮光罩。

即便是早有心理准备的我，在黑暗降临的一刹那也不禁倒吸了一口凉气！在伸手不见五指的幽暗工棚之中，眼前的猛兽彻底蜕变成了一头降临人间的地狱幽冥恶魔！它的血盆大口仿佛在向外疯狂喷吐着惨绿幽蓝的熊熊烈焰；两只巨眼宛如从炼狱深处抠出的烧红火炭；滴淌腥血的獠牙周围环绕着刺骨的阴冷鬼火！

查尔斯老爵士是一个长期深陷中世纪迷信恐惧的垂死老人，他的心脏衰弱得宛如一只中箭的惊弓之鸟。他绝对无法承受这等毁天灭地的视觉暴击！我的恶犬甚至根本不需要碰他一根汗毛——只要让这头喷吐烈焰的巨兽在红豆杉树篱后咆哮现身，老东西脆弱的心脏便会瞬间在胸膛中彻底炸裂！

死神的镰刀已然磨砺完毕。现在，我只需抛出一根致命的诱饵，将那个深居简出的老顽固从庄园高墙里引诱至午夜的黑暗荒原！"""
    },

    # Chapter 2 Part 1
    {
        "id": "stapleton_ch02_part1_laura_trap",
        "ch_idx": 1, "part": 1,
        "title_en": "Chapter 2: The Fall of Sir Charles (Part I: The Pawn of Coombe Tracey)",
        "title_cn": "第二章 查尔斯爵士之死（上：被诱骗的棋子劳拉·里昂斯）",
        "pov": "stapleton", "type": "anchor", "anchor": "anchor_laura_trap_stapleton",
        "clues_en": [
            "Stapleton promises marriage to Laura Lyons if she secures divorce funds from Sir Charles",
            "Dictates the desperate letter demanding a meeting at 10 PM at the yew alley gate",
        ],
        "clues_cn": [
            "斯台普吞以虚假结婚诺言为饵，诱骗走投无路的劳拉·里昂斯向查尔斯爵士索要两千镑赎身费",
            "亲自口述并逼迫劳拉写下绝命密约信，要求老爵士在深夜十点务必孤身在侧门相会",
        ],
        "choices_en": [
            {"id": "s_ch2_p1_c1", "text": "Command Laura Lyons to stay away while you bring the hound to the yew alley.", "target": "stapleton_ch02_part2_yew_alley"},
            {"id": "s_ch2_p1_c2", "text": "Prepare the hound with the phosphorus paste as twilight falls upon the moor.", "target": "stapleton_ch02_part2_yew_alley"},
        ],
        "choices_cn": [
            {"id": "s_ch2_p1_c1", "text": "当面严令劳拉·里昂斯今晚绝不许赴约，自己则暗中牵出涂满磷光的恶犬奔赴红豆杉侧门。", "target": "stapleton_ch02_part2_yew_alley"},
            {"id": "s_ch2_p1_c2", "text": "在夕阳沉入地平线之际完成恶犬的磷光涂抹，将杀戮倒计时推向最后一刻。", "target": "stapleton_ch02_part2_yew_alley"},
        ],
        "content_en": """The instrument to lure Sir Charles into my trap was ready to hand in Coombe Tracey: Mrs. Laura Lyons.

She was a woman of desperate vanity and even more desperate poverty. Abandoned by her scoundrel husband, disowned by her cantankerous father Frankland, she was drowning in debt. I cultivated her with sweet, insidious sympathy. I played the chivalrous protector, listened to her tears, and gradually fed her romantic imagination with promises of marriage.

'If only you were free of this monster Lyons,' I would whisper, stroking her hair. 'If only you had the funds to obtain a legal divorce, Beryl and I would welcome you as mistress of Merripit House!'

Two thousand pounds was the sum required to clear her debts and fund the London lawyers. Who had such wealth and the generosity to bestow it? Sir Charles Baskerville!

On the morning of May 4th, I called upon Laura at her cottage. I found her in a state of high agitation, receiving threats of legal attachment from her creditors.

'Sir Charles leaves for London tomorrow,' I told her urgently. 'He is old, frail, and his heart is failing. If you write him a formal appeal, he will refer you to his lawyers. You must see him yourself, face to face! You must touch his chivalry before he departs!'

I sat beside her and dictated the fateful words:

'Please, please, as you are a gentleman, burn this letter, and be at the gate by ten o'clock.'

She signed it with a trembling hand and posted it to Baskerville Hall.

At five o'clock that afternoon, I returned to her cottage with a look of stern, wounded pride.

'Laura,' I said, seizing her hands, 'I cannot permit it! My honor as a man revolts at the thought of my future wife begging money from another man! I have secured the two thousand pounds from my own investments. You shall not go to Baskerville Hall tonight!'

She fell upon my neck with tears of overwhelming gratitude. The fool! She believed she was saved. In reality, she had sealed Sir Charles's death warrant, while leaving herself without an alibi to reveal my hand!""",
        "content_cn": """将查尔斯老爵士引诱入陷阱的最佳工具，就现成地摆在库姆马西集镇：劳拉·里昂斯夫人。

这是一个虚荣心极强、而在现实中又被贫困彻底逼入绝境的脆弱女人。她被无赖丈夫抛弃，又被那个成天打官司的暴躁父亲弗兰克兰断绝了父女关系，整日生活在债台高筑的屈辱之中。我以极具欺骗性的绅士温情精心编织了一张罗网。我扮演着慷慨高贵的庇护者，倾听她的抽泣，并在不经意间用一纸虚幻的婚姻诺言彻底俘获了她的心智。

‘倘若你能摆脱那个无赖里昂斯的法律枷锁，’我轻抚着她的秀发低语道，‘只要有一笔钱能支付伦敦昂贵的离婚诉讼费，我和贝丽尔便会张开双臂，迎接你成为梅利琵宅邸真正的主人！’

结清债务并聘请顶级大律师需要整整两千英镑。在这片荒原上，究竟何人拥有这等巨富且生性乐善好施？唯有查尔斯·巴斯克维尔爵士！

五月四日清晨，我踏入了劳拉的打字行。她正因债权人发出的破产传票而精神濒临崩溃。

‘查尔斯爵士明天清晨就要动身前往伦敦，’我神色严峻地催促道，‘他年迈体衰，心脏随时可能衰竭。倘若你寄去一份公事公办的求援信，他只会将你推给冷酷的律师团！你必须当面见他！你必须当面哭诉以唤醒他骨子里的骑士精神！’

我坐在她身旁，一字一句口述出了那行致命的绝命信：

‘求求您，求求您，倘若您当真是一位绅士，读罢请将此信烧毁，并于今晚十点整在侧门相候！’

她在极度惶恐中颤抖着签下了名字，将信函火速投递往巴斯克维尔庄园。

下午五点，我再次跨入她的寓所，脸上换上了一副严厉而自尊受辱的悲愤表情。

‘劳拉，’我一把抓住她的双手，‘我绝不容许这种事发生！作为一个男人的尊严，我绝不能容忍我未来的妻子去向另一个男人摇尾乞怜！我已经从我自己的海外投资中变现了这两千英镑！今晚，你绝对不许踏足巴斯克维尔庄园半步！’

她感动得扑入我的怀中放声大哭，将我视作救世主。这个天真的蠢女人！她做梦也想不到，她亲手签下的不仅是老爵士的死刑判决书，更是彻底斩断了她自己今后所有公开抗辩的退路！"""
    },

    # Chapter 2 Part 2
    {
        "id": "stapleton_ch02_part2_yew_alley",
        "ch_idx": 1, "part": 2,
        "title_en": "Chapter 2: The Fall of Sir Charles (Part II: Terror at the Wicker Gate)",
        "title_cn": "第二章 查尔斯爵士之死（下：小树道侧门的致命恐惧）",
        "pov": "stapleton", "type": "branch", "anchor": None,
        "clues_en": [
            "Sir Charles waited 20 minutes smoking at the gate expecting Laura Lyons",
            "The phosphorescent hound was unleashed; Sir Charles fled in terminal cardiac panic",
            "The hound was recalled into the mire, leaving only footprints twenty yards away",
        ],
        "clues_cn": [
            "查尔斯爵士在侧门足足抽烟等待了二十分钟，期盼着劳拉·里昂斯前来赴约",
            "当喷吐烈焰的地狱恶兽在夜色中破草扑出时，老爵士在极致的恐怖中心脏彻底爆裂",
            "斯台普吞吹响无声犬笛引回猎犬遁入泥潭，在现场二十码外的湿泥上留下了不可磨灭的鬼印",
        ],
        "choices_en": [
            {"id": "s_ch2_p2_c1", "text": "Plan the London expedition to eliminate the new Canadian heir, Sir Henry Baskerville.", "target": "stapleton_ch03_new_heir"},
            {"id": "s_ch2_p2_c2", "text": "[Switch POV to Sherlock Holmes] View Holmes receiving the case from Dr. Mortimer.", "target": "holmes_ch01_part2_consultation", "pov_switch": "holmes"},
        ],
        "choices_cn": [
            {"id": "s_ch2_p2_c1", "text": "筹划远赴伦敦的秘密暗杀行动，抢在年轻的加拿大继承人踏足荒原前将其就地格杀。", "target": "stapleton_ch03_new_heir"},
            {"id": "s_ch2_p2_c2", "text": "【视角切换：歇洛克·福尔摩斯】切换至贝克街，看名侦探如何从摩梯末口中审讯现场足印。", "target": "holmes_ch01_part2_consultation", "pov_switch": "holmes"},
        ],
        "content_en": """The night of May 4th was pitch-black and damp. At nine o'clock, I slipped out of Merripit House, leading my hound upon a heavy hemp lead. Its muzzle and eyes blazed with their hideous coat of phosphor, shielded beneath a thick woolen blanket.

We reached the boundary of Baskerville Hall at a quarter to ten. Outside the dense, twelve-foot yew hedge that bordered the alley, the damp peat of the moor was silent as a tomb. I crouched behind a clump of furze bushes, twenty yards from the wooden wicker gate that opened onto the heath.

Through the gaps in the hedge, I saw the red glow of a cigar.

Sir Charles had arrived! He had opened the gate, looked out into the darkness, and was pacing nervously upon the turf, checking his pocket watch every few minutes.

Ten o'clock struck from the village church across the valley.

The old man grew restless. He tossed his first cigar ash to the gravel, struck a second match, and waited another ten minutes. The cold night air was tormenting his lungs.

It was time.

I stripped the blanket from the hound. I held the beast by its heavy brass collar, whispered into its ear, and pointed its glowing muzzle through the gloom toward the gate.

'Go, boy!' I hissed. 'Take him!'

The beast leaped forward with a low, bloodcurdling roar!

Through the wicket, Sir Charles heard the thud of giant paws and turned. What met his superstitious gaze was the nightmare that had haunted his family for two hundred years: an immense, coal-black demon charging through the darkness, its jaws and eyes spouting hellish flame!

He uttered a shriek that died in his throat. He did not even attempt to shut the gate. He whirled round and ran down the alley on his tiptoes, his hands clawing at his chest in mortal agony! After fifty yards, his heart ruptured, and he crashed headlong onto the turf.

I blew my high-pitched galton whistle. The hound, trained to instant obedience, swerved twenty yards short of the body and bounded back to my side. I slipped the blanket over its head, patted its flank, and led it safely back into the black sanctuary of Grimpen Mire.

Not a mark was on his body. A clean, untraceable kill! The first hurdle was down!""",
        "content_cn": """五月四日深夜，暴雨将至，夜色浓黑如墨。九点整，我用一条粗麻绳牵着恶犬悄然溜出了梅利琵宅邸。在厚重的羊毛毯包裹掩盖之下，这头巨兽的口吻与双眼依然隐隐透出令人窒息的磷光幽火。

差一刻十点，我们抵达了巴斯克维尔庄园的边界。在红豆杉树篱外的荒原沼泽地上，湿漉漉的泥炭寂静得犹如一座乱葬岗。我伏身在一丛带刺的金雀花灌木后，距离那扇通向荒原的木栅侧门刚好二十码远。

透过红豆杉树篱的缝隙，一截暗红色的雪茄烟头亮光清晰可见。

查尔斯老爵士如约而至！他推开侧门，神色焦躁地向荒原黑夜中眺望，在狭窄的草坪上不安地来回踱步，隔几分钟便掏出怀表借着烟火查看时间。

谷地对面的村庄教堂沉闷地敲响了十点的钟声。

老爵士显得越发焦躁不安。他弹落了第一撮雪茄烟灰，擦亮第二根火柴点燃了新的烟卷，在刺骨的寒风中又苦苦等了十分钟。

死神降临的时刻到了。

我一把猛地扯掉了蒙在恶犬头上的厚毛毯！我死死攥住它颈项上的沉重黄铜项圈，贴在它喷吐热气的耳朵旁吐出恶魔般的命令，将那颗燃烧着幽蓝烈焰的巨头猛地指向侧门的方向！

‘去！咬死他！’我咬牙厉喝。

那恶兽发出一声惊天动地的闷吼，狂暴地凌空飞跃而出！

透过树篱，查尔斯爵士听到了巨爪踏碎枯枝的雷霆奔袭声，猛然回首。然而映入这位长期深陷家族诅咒梦魇的老人眼帘的，是一具彻底撕碎其理智的活体梦魇：一头体型如牛、两眼喷吐着地狱绿火的巨大黑魔，正张牙舞爪自虚空中狂暴扑杀而来！

老爵士发出一声被扼死在喉咙里的凄厉绝叫！他甚至根本来不及关上侧门，猛然转身沿着红豆杉小径用脚尖亡命狂奔，双手绝望地死死撕扯着胸口的衣襟！仅仅狂奔了五十码远，他那颗脆弱的心脏便彻底破裂碎裂，整个人面孔朝下，轰然仆倒在草坪之中！

我立刻吹响了高频无声犬笛（Galton whistle）。受过严苛训练的恶犬在距离尸体二十码远的地方硬生生刹住了脚步，欢快地折返奔回我的身旁。我将厚毛毯重新罩上它的头颅，拍了拍它的背脊，牵着它如幽灵般悄然隐没在大格林盆泥潭那片深不可测的黑色庇护所中。

死者身上没有留下任何物理创口。一桩完美绝伦、毫无破绽的绝世谋杀！第一块绊脚石已然彻底扫清！"""
    }
])
# Stapleton Chapter 3 & 4
STAPLETON_NODES.extend([
    # Chapter 3
    {
        "id": "stapleton_ch03_new_heir",
        "ch_idx": 2, "part": 0,
        "title_en": "Chapter 3: The Threat from Canada (The Obstacle to the £740,000 Estate)",
        "title_cn": "第三章 疑案（来自加拿大的威胁与伦敦暗杀计划）",
        "pov": "stapleton", "type": "branch", "anchor": None,
        "clues_en": [
            "Sir Henry Baskerville is summoned from Canada as sole heir to the estate",
            "Stapleton travels to London under an alias to shadow and eliminate Sir Henry",
            "Beryl is forced to accompany him, watched day and night under constant surveillance",
        ],
        "clues_cn": [
            "获悉远在加拿大的年轻农夫亨利·巴斯克维尔正作为唯一法定继承人受召返英",
            "斯台普吞决意化名潜入伦敦，务必在亨利爵士抵达达特穆尔前将其彻底清除",
            "强逼妻子贝丽尔同行，日夜严密监控，严防其走漏半点风声",
        ],
        "choices_en": [
            {"id": "s_ch3_c1", "text": "Shadow Sir Henry to the Northumberland Hotel and secure an agent within the staff.", "target": "stapleton_ch04_part1_hotel_shadow"},
            {"id": "s_ch3_c2", "text": "[Switch POV to Dr. Watson] View Watson discussing the Dartmoor problem with Holmes at 221B.", "target": "ch03_problem", "pov_switch": "watson"},
        ],
        "choices_cn": [
            {"id": "s_ch3_c1", "text": "尾随亨利爵士入驻诺森伯兰旅馆，以重金买通大堂侍者搜集暗杀情报。", "target": "stapleton_ch04_part1_hotel_shadow"},
            {"id": "s_ch3_c2", "text": "【视角切换：约翰·H·华生】切换至贝克街，见证华生与福尔摩斯在浓密烟雾中推敲疑案。", "target": "ch03_problem", "pov_switch": "watson"},
        ],
        "content_en": """The coroner's verdict was everything I had prayed for: death from natural causes, cardiac syncope. The fools had looked at the yew hedge and seen nothing. Even Mortimer, with his ridiculous anthropological chatter, had kept silent out of fear of rural hysteria.

I believed the prize was within my grasp. But within a fortnight, the Devon papers announced a bitter complication: Sir Charles had a surviving nephew, Henry Baskerville, son of his middle brother. The young man had emigrated to Canada in his youth, was farming near Lake Superior, and had already been summoned home by the family solicitors, Messrs. Gautier and Brown of London, to assume the title and the £740,000 estate!

My fury was boundless! Was I to allow a colonial clodhopper to wrest the ancestral gold from my grasp after I had braved the gallows to win it?

Never!

A second strike was imperative. But to strike Sir Henry on the open moor would invite instant suspicion from the county constabulary. The ideal ground was London—a city of four million souls, where street accidents, river drownings, and drunken affrays are forgotten in a day!

I locked my hound on the mire island with thirty pounds of horseflesh. I packed two leather valises, purchased a disguise of dark spectacles and an adhesive black beard, and dragged Beryl with me to a quiet boarding house in St. John's Wood under the name of Vandeleur.

She wept, she pleaded, she went upon her knees, begging me to renounce the inheritance and fly with her back to Central America.

'Touch that door,' I snarled, twisting her slender wrist until she cried out, 'or speak one word to a living soul, and I swear by heaven your Canadian lover will die a death ten times more hideous than his uncle!'

On October 12th, Sir Henry landed at Southampton. Within two hours, I had picked up his trail at Waterloo station and followed him and Dr. Mortimer to the Northumberland Hotel in the Strand. The hunt had moved to the capital!""",
        "content_cn": """验尸法庭给出的官方裁决完美得超出了我最狂妄的祈求：急性心力衰竭，自然猝死。这帮脑满肠肥的乡村陪审员除了红豆杉树篱外什么也看不见；即便是摩梯末那个整日沉溺在颅骨测量中的书呆子，也出于对乡民恐慌的顾虑对现场足印三缄其口。

我原本以为那座七十四万镑的金山已然落入囊中。然而短短两周之后，德文郡的各大地方报纸却刊登出了一条令我五内俱焚的噩耗：查尔斯爵士在世上竟然还有一个亲侄儿——亨利·巴斯克维尔！二伯父的亲生骨肉！这位年轻男爵早年远涉重洋前往加拿大苏必利尔湖畔开荒务农，如今伦敦的高瑟父子律师行已通过跨洋电报紧急将其召回本土，全权继承头衔与整座庞大的家族信托！

我心中的狂怒险些撕裂胸膛！难道我冒着同赴绞刑架的万丈深渊夺得的泼天富贵，竟要眼睁睁拱手让给一个粗鄙无知的殖民地庄稼汉？！

绝不可能！

必须立刻发动第二轮致命打击！然而若在达特穆尔荒原上接连暴毙两位庄园继承人，即便是最愚钝的郡警也必将嗅出人为谋杀的气息。最理想的猎杀擂台，唯有庞大臃肿的伦敦市区——一座吞吐着四百万孤魂野鬼的迷雾之都，在这里，一场车祸、一次溺水或是一场醉酒斗殴，不出一天便会被忘得干干净净！

我给囚禁在孤岛上的恶兽备足了整整三十磅马肉与洁水。我收拾好两只牛皮提箱，备齐了一副墨镜与一把精巧的人造黏贴黑胡须，强行将贝丽尔掳上火车，在圣约翰伍德（St. John's Wood）以凡德勒之名租下了一间幽暗的寄宿公寓。

贝丽尔跪倒在地板上撕心裂肺地痛哭流涕，苦苦哀求我放弃这笔沾满鲜血的罪恶遗产，求我带她远走高飞逃回中美洲。

‘你敢碰一下那扇门，’我恶狠狠地拧紧她娇嫩纤细的手腕，疼得她倒抽冷气发出尖叫，‘或是胆敢向任何活人吐露半个字，我向地狱起誓，你的那位加拿大堂弟必将死得比他伯父惨烈十倍！’

十月十二日，亨利爵士搭乘的邮轮在南安普顿靠港。短短两小时后，我便在滑铁卢车站咬住了他和摩梯末医生的行踪，一路贴身尾随至河岸街的诺森伯兰旅馆。猎杀的舞台，已然正式迁入了帝国的心脏！"""
    },

    # Chapter 4 Part 1
    {
        "id": "stapleton_ch04_part1_hotel_shadow",
        "ch_idx": 3, "part": 1,
        "title_en": "Chapter 4: Sir Henry Baskerville (Part I: Shadows at the Northumberland Hotel)",
        "title_cn": "第四章 亨利·巴斯克维尔爵士（上：诺森伯兰旅馆的眼线与剪报）",
        "pov": "stapleton", "type": "anchor", "anchor": "anchor_london_shadow_stapleton",
        "clues_en": [
            "Beryl secretly composes warning letter using words cut from yesterday's Times",
            "Stapleton discovers the betrayal, terrifies Beryl, but the letter is already mailed",
            "Stapleton bribes chambermaid to steal Sir Henry's boot to secure his scent",
        ],
        "clues_cn": [
            "贝丽尔背叛丈夫，用修甲剪刀从昨日《泰晤士报》社论裁剪词句拼贴匿名警告信",
            "斯台普吞当场截获通敌行径并将贝丽尔毒打威慑，然而警告信却已被其暗中投入邮筒",
            "斯台普吞重金贿赂旅馆女侍盗取亨利爵士置于门外的皮靴，企图为恶犬锁定致命气味",
        ],
        "choices_en": [
            {"id": "s_ch4_p1_c1", "text": "Discover the maid brought an unworn tan boot; trail Sir Henry into Regent Street in a hansom.", "target": "stapleton_ch04_part2_cab_chase"},
            {"id": "s_ch4_p1_c2", "text": "[Switch POV to Sherlock Holmes] View Holmes analyzing the cut Times letter at 221B.", "target": "holmes_ch04_part1_warning", "pov_switch": "holmes"},
        ],
        "choices_cn": [
            {"id": "s_ch4_p1_c1", "text": "惊见女仆竟偷来一只毫无气味的新黄皮靴；戴上假黑胡子雇佣马车在摄政街紧咬爵士不放。", "target": "stapleton_ch04_part2_cab_chase"},
            {"id": "s_ch4_p1_c2", "text": "【视角切换：歇洛克·福尔摩斯】切换至贝克街，看名侦探用显微镜拆解素馨花香气与五号铅字。", "target": "holmes_ch04_part1_warning", "pov_switch": "holmes"},
        ],
        "content_en": """On the evening of October 12th, I returned to our lodgings in St. John's Wood to find Beryl crouched beside the table, her face bathed in tears. Scattered upon the rug lay an open copy of yesterday's Times and a pair of curved nail-scissors.

My eye caught the jagged gap in the leading article. I seized her by the hair, dragging her head back until her dark eyes stared into mine.

'What have you done?' I hissed.

She sobbed in terror. 'I warned him! I pasted the words upon a sheet and dropped it into the Charing Cross pillar-box! I could not let you slaughter an innocent boy, Jack! I could not bear the blood on our souls!'

A savage oath escaped my lips! I struck her across the face, hurling her against the sofa. The little traitress had almost destroyed my life's work! The letter was already in the post; it was beyond recall. If Sir Henry took fright and returned to Canada, the estate would slip through my fingers forever!

I must act without an hour's delay.

At dawn, disguised in a dark frock coat and heavy tinted glasses, I entered the Northumberland Hotel. I slipped half a sovereign into the apron pocket of the chambermaid who was cleaning the second-floor corridor.

'My girl,' said I with a polite smile, 'the gentleman in Room 34 has asked me to take one of his boots to the cobbler in the Strand to be repaired. Hand me one from outside his door, and keep the gold for yourself.'

She looked at the coin, grinned greedily, and darted to Room 34. She returned in thirty seconds, pressing a boot into my hands.

I slipped it into my bag, hurried down the service stairs, and walked briskly into the morning air. But when I reached an alleyway and drew the boot from my bag, I uttered a roar of frustrated fury!

It was a brand-new tan boot! The leather was stiff, polished, and virgin—it had never touched a human foot!

An unworn boot carries no scent! The hound cannot hunt an abstract shape of calfskin—it requires the unmistakable, pungent scent of living sweat and blood!

Furious at the maid's blundering stupidity, I resolved to follow Sir Henry on his morning walk, watch his movements, and contrive to seize a worn boot before the day was out!""",
        "content_cn": """十月十二日傍晚，当我返回圣约翰伍德的幽暗寓所时，赫然发现贝丽尔正蜷缩在桌角抽泣。地板上散落着一份被裁得千疮百孔的昨日《泰晤士报》，以及一把小巧弯曲的女士修甲剪刀。

社论通栏上那排犬牙差互的空白瞬间刺痛了我的双眼。我一把揪住她的长发，硬生生将她的头颈向后扯起，令她那双充满泪水的黑眼睛死死迎向我充血的双眸。

‘你干了什么？！’我牙缝中挤出毒蛇般的低吼。

她吓得浑身瘫软，痛哭失声：‘我警告了他！我把那些剪下来的字贴在纸上，投进了查令十字街的邮筒！杰克，我不能眼睁睁看着你再杀害一个无辜的年轻人！我们的灵魂承受不起更多的血债了！’

一声狂暴的咒骂从我口中喷涌而出！我狠狠一记耳光将她抽翻在沙发上。这个成事不足败事有余的贱人，险些将我毕生的心血彻底毁于一旦！信件已然落入邮政管道，绝无追回可能！倘若那个胆小的加拿大男爵被这封匿名信吓破了胆，连夜卷铺盖逃回美洲，那七十四万英镑的金山便将永远离我而去！

必须抢在一切不可挽回之前以雷霆万钧之势就地格杀！

清晨时分，我换上一袭黑色常礼服，戴上深色墨镜潜入了诺森伯兰旅馆。我将半枚金镑悄悄塞进了正在二楼长廊打扫卫生的女仆围裙口袋里。

‘好姑娘，’我换上一副优雅温和的管家笑容，‘34号房间的那位加拿大贵客吩咐我，替他将一只破损的皮靴送往河岸街的鞋匠铺修补。把门外那双靴子交给我一只，这枚金币就是你的了。’

女仆贪婪地摩挲着金币，眉开眼笑，飞快地溜到34号门前。短短三十秒后，她便将一只沉甸甸的皮靴塞到了我的手中。

我迅速将靴子塞入皮包，顺着后门安全通道疾步溜出旅馆，踏入了清晨喧嚣的伦敦街头。然而，当我拐入一条僻静的暗巷、满怀狂喜地将皮靴掏出皮包的一瞬间，我忍不住在晨风中爆发出一声暴怒至极的咆哮！

那竟然是一只崭新锃亮的黄褐色新皮靴！鞋面的牛皮坚硬挺括，鞋底一尘不染——一双从未上过脚的全新靴子！

一双没穿过的鞋子根本没有任何体味！我的恶犬绝不可能凭借毫无气味的鞣制皮革去追踪活人——它必须吸饱活人毛孔深处分泌出的酸性汗液与热血气味！

被这个愚蠢的女仆气得七窍生烟的我，只得咬碎钢牙收起行头。我必须亲自贴身咬住亨利爵士的一举一动，在今天之内务必顺走他穿过的旧靴！"""
    },

    # Chapter 4 Part 2
    {
        "id": "stapleton_ch04_part2_cab_chase",
        "ch_idx": 3, "part": 2,
        "title_en": "Chapter 4: Sir Henry Baskerville (Part II: The Duel in Regent Street: Cab 2704)",
        "title_cn": "第四章 亨利·巴斯克维尔爵士（下：摄政街的对决与马车2704）",
        "pov": "stapleton", "type": "branch", "anchor": None,
        "clues_en": [
            "Stapleton hires cab No. 2704 disguised with adhesive black beard and dark glasses",
            "Sherlock Holmes spots him; Stapleton escapes and brazenly uses Holmes's own name",
        ],
        "clues_cn": [
            "斯台普吞贴上假黑胡子、戴上墨镜雇佣2704号双轮马车在摄政街尾随爵士",
            "在与歇洛克·福尔摩斯目光凌空撞击的瞬间果断策马飞驰逃逸，并傲慢挑衅地假借名侦探之名脱身",
        ],
        "choices_en": [
            {"id": "s_ch4_p2_c1", "text": "Return to the hotel corridor to steal Sir Henry's worn black boot and flee to Devon.", "target": "stapleton_ch05_black_boot"},
            {"id": "s_ch4_p2_c2", "text": "[Switch POV to Sherlock Holmes] View Holmes receiving the report from cabman Clayton.", "target": "holmes_ch05_threads", "pov_switch": "holmes"},
        ],
        "choices_cn": [
            {"id": "s_ch4_p2_c1", "text": "潜回旅馆趁乱调换盗取亨利爵士踩满泥巴的旧黑皮靴，带上致命气味火速潜回达特穆尔。", "target": "stapleton_ch05_black_boot"},
            {"id": "s_ch4_p2_c2", "text": "【视角切换：歇洛克·福尔摩斯】切换至贝克街，见证名侦探在马车夫口中得知自己姓名被盗用的震怒。", "target": "holmes_ch05_threads", "pov_switch": "holmes"},
        ],
        "content_en": """I applied a thick, adhesive black beard to my chin, pulled a dark slouch hat over my brow, and stationed myself near the Strand.

At ten o'clock, Sir Henry and Mortimer emerged, walking briskly toward Oxford Street. I hailed a hansom cab driven by a burly fellow named Clayton.

'Follow those two gentlemen at two hundred yards,' I commanded, tossing him a half-sovereign. 'Keep pace on the opposite side of the road!'

For twenty minutes, the hunt proceeded smoothly. We crawled down Regent Street behind them. I observed their energetic gestures; Mortimer was evidently taking Sir Henry to a professional consultation. But to whom?

Suddenly, cold horror seized my heart!

Walking briskly down the pavement behind Sir Henry, his keen, aquiline profile unmistakable to any educated man in Europe, was Sherlock Holmes! Accompanying him was a sturdy military gentleman—Dr. Watson!

Mortimer had brought Holmes into the case! The foremost detective in the world had taken the field!

At that instant, Holmes turned his head. His hawk-like gray eyes bored straight through the glass of my cab! He had penetrated my shadow!

'Quick!' I roared, thrusting my stick through the roof-trap into the cabby's back. 'Drive like the devil to Waterloo! A sovereign if you shake them off!'

Clayton lashed his horse into a wild gallop. The hansom tore down Regent Street, swerving between omnibuses and drays, leaving Holmes sprinting in our wake. We careened into Waterloo Place, crossed the river, and pulled up amidst the chaos of Waterloo station.

I leaped from the cab, pulled out two golden sovereigns, and pressed them into Clayton's palm.

'You did well, cabby,' said I with a mocking, insolent grin. 'And if a tall gentleman asks you who your fare was, tell him: My name is Sherlock Holmes, and don't you forget it!'

I plunged into the labyrinth of the station, vanished through the southern exit, and left the greatest detective in England grasping at smoke! But the game was now deadly earnest. I had crossed swords with Sherlock Holmes!""",
        "content_cn": """我将一圈浓密黑亮的黏贴假连鬓胡须死死粘在下颚，把一顶深色阔边软呢帽压低到眉际，在河岸街转角处守株待兔。

十点整，亨利爵士与摩梯末并肩走出旅馆大堂，快步朝牛津街方向走去。我顺手拦下了一辆由一个名叫克莱顿的魁梧汉子拉乘的双轮轻便马车。

‘远远咬住前面那两位先生，保持两百码距离，’我将半枚金镑掷进他怀里，‘走马路对面，别靠得太近！’

在整整二十分钟的时间里，追踪进行得如丝般顺滑。我们在摄政街的车流中缓缓并排前行。我仔细研读着亨利爵士激动的肢体语言；摩梯末显然正在陪同他前往某处接受极高规格的私人专业咨询。然而究竟是去见谁？

突然之间，一股寒彻骨髓的绝命恐惧瞬间扼死了我的心脏！

就在亨利爵士身后不远处的人行道上，一个身形挺拔、生着一张在全欧洲无人不晓的鹰喙般锐利侧颜的高大绅士，正目光如炬地步步紧逼！身旁还紧跟着一位步履沉稳的军医装束同伴——约翰·H·华生！

歇洛克·福尔摩斯！摩梯末竟然把这个名震英伦的活阎王给请出了山！

就在我认出他的电光石火之间，福尔摩斯猛然转过了头颅！他那双鹰隼般的灰色寒眸如同两柄出鞘的利刃，竟穿透车窗玻璃直直刺入了我的瞳孔！他识破了我的暗中盯梢！

‘快！’我发疯般用手杖顶开马车车顶的传话天窗，死死戳在车夫的后背上厉声咆哮，‘拼死赶往滑铁卢车站！甩掉他们，我多赏你一整枚金镑！’

车夫的长鞭在空中抽出凄厉的裂响，骏马狂性大发，拉着马车在摄政街密密麻麻的双层公共马车与货车车流中亡命穿梭飞驰！把狂奔追赶的福尔摩斯彻底甩在了烟尘之后！我们风驰电掣般杀过滑铁卢广场，轰鸣着冲过泰晤士河大桥，猛地急刹在喧嚣混乱的滑铁卢车站进站口！

我跳下车厢，掏出两枚金光闪闪的金镑重重拍进车夫的手心里。

‘干得漂亮，车夫，’我嘴角咧开一抹狂妄至极的恶毒狞笑，‘待会儿要是有个瘦高个绅士向你打听刚才坐车的是哪位大人物，你便如实回他：“老子的名字叫歇洛克·福尔摩斯，可千万给老子记牢了！”’

我一个闪身潜入了滑铁卢车站浩瀚杂乱的人流迷宫之中，顺着南侧货运出口神不知鬼不觉地溜之大吉，只留给全英国最顶尖的神探一片抓不住的虚妄青烟！然而这场对决在这一秒已然彻底变成了不死不休的你死我活——我已然正式拔剑，与歇洛克·福尔摩斯狭路相逢！"""
    }
])
# Stapleton Chapter 5 & 6
STAPLETON_NODES.extend([
    # Chapter 5
    {
        "id": "stapleton_ch05_black_boot",
        "ch_idx": 4, "part": 0,
        "title_en": "Chapter 5: Three Broken Threads (Securing the Old Black Boot)",
        "title_cn": "第五章 三条断了的线索（盗取旧黑靴与遁回达特穆尔）",
        "pov": "stapleton", "type": "anchor", "anchor": "anchor_arrival_stapleton",
        "clues_en": [
            "Stapleton returns the new tan boot and successfully steals Sir Henry's old black boot",
            "Learns Holmes declined to go to Devon, sending only Dr. Watson as bodyguard",
            "Returns triumphant to Merripit House to prepare the hound with the fatal scent",
        ],
        "clues_cn": [
            "斯台普吞悄然潜回旅馆物归原主退回新黄靴，成功盗取亨利爵士穿过、沾满烂泥的旧黑皮靴",
            "暗探获悉歇洛克·福尔摩斯借故公务缠身留守伦敦，仅派军医华生随行护送男爵",
            "怀揣浸透目标体味的绝密旧靴狂喜返回梅利琵宅邸，着手以血腥气味饲喂训练恶兽",
        ],
        "choices_en": [
            {"id": "s_ch5_c1", "text": "Take position upon the ridge overlooking the moor road to watch Sir Henry's arrival.", "target": "stapleton_ch06_part1_arrival_watch"},
            {"id": "s_ch5_c2", "text": "[Switch POV to Dr. Watson] View Watson traveling west on the express to Devonshire.", "target": "ch06_part1_arrival", "pov_switch": "watson"},
        ],
        "choices_cn": [
            {"id": "s_ch5_c1", "text": "登上梅利琵宅邸高坡山脊隐蔽处，架起单筒望远镜等候亨利爵士与华生自伦敦入瓮。", "target": "stapleton_ch06_part1_arrival_watch"},
            {"id": "s_ch5_c2", "text": "【视角切换：约翰·H·华生】切换至西行快车车厢，体验华生护送男爵奔赴古老庄园的凝重思绪。", "target": "ch06_part1_arrival", "pov_switch": "watson"},
        ],
        "content_en": """The encounter in Regent Street had sent an icy shudder of danger through my marrow, but it did not shake my resolve. A lesser intellect would have fled the city. I did the opposite: I doubled back to the Northumberland Hotel.

In the confusion of the afternoon, while Sir Henry and Mortimer were closeted in consultation with Holmes in Baker Street, I re-entered the hotel. I slipped that useless, unscented tan boot beneath a wicker chair in the second-floor sitting-room. And outside the door of Room 34, my patience was rewarded by the gods of fortune!

There, set out upon the drugget to be brushed, lay a pair of old black boots, their heels worn down and their toes caked with dried red mud from Sir Henry's Canadian rambles!

I snatched one of the black boots, jammed it beneath my overcoat, and walked calmly out of the front entrance into the Strand.

I had it! The master scent! The heavy, unmistakable odour of human sweat and leather that my starved beast could track across twenty miles of wind-swept bog!

That evening, my private surveillance outside Baker Street bore another piece of priceless fruit: Sir Henry and Dr. Watson were observed purchasing railway tickets for Devonshire, but Sherlock Holmes was remaining behind in London! The great detective was sending his sheep to the slaughter while he occupied himself with metropolitan trifles!

I laughed aloud in the shadows of the platform. Against Sherlock Holmes, the battle would have been fierce; against Dr. John Watson, the blundering, good-natured army surgeon, it would be child's play!

I returned to St. John's Wood, dragged Beryl by the arm, and boarded the midnight mail train westward. By sunrise on October 14th, we were back at Merripit House.

I went straight to the mire island. I held the muddy black boot beneath the panting nostrils of the monster. The beast snorted, its yellow eyes narrowing in ferocious recognition, and let out a low, slobbering whimper of bloodlust.

The stage was set. Sir Henry was walking into the jaws of hell!""",
        "content_cn": """摄政街上与福尔摩斯那电光石火的生死遭遇，虽令我的骨髓深处泛起阵阵彻骨寒意，却丝毫未能撼动我钢铁般的杀心。换作任何凡夫俗子，此刻早已吓得抱头鼠窜逃离伦敦；而我却反其道而行之，杀了一记漂亮的回马枪，径直折返了诺森伯兰旅馆！

趁着午后大堂人员换岗、而亨利爵士与摩梯末正赶赴贝克街向福尔摩斯闭门求教的绝佳空当，我再次潜入了二楼长廊。我将那只毫无气味的崭新黄皮靴随手塞回了二楼起居室的藤椅底下以掩人耳目。而在34号房门外的地垫上，命运之神向我露出了最狰狞的微笑！

那里整整齐齐摆放着一双饱经风霜的旧黑皮靴，鞋跟磨损倾斜，鞋头与鞋帮上厚厚结着一层加拿大荒野跋涉遗留下来的深红泥垢！

我闪电般抄起其中一只旧黑靴塞入大衣内衬，神色从容如常地从容迈出旅馆正门，施施然消失在河岸街熙攘的人潮之中！

我拿到了！最致命的核心气味样本！那双旧靴深处吸附着的人体汗液、毛孔油脂与牛皮混合而成的鲜明体味，足以令我那头饥肠辘辘的恶兽在风声鹤唳的方圆二十英里荒原上死死锁定目标！

当天傍晚，我在贝克街暗中布下的眼线更是送来了一道价值千金的绝密喜讯：亨利爵士与华生医生在火车站预定了次日清晨奔赴德文郡的干线车票，然而歇洛克·福尔摩斯先生却留守伦敦，分身乏术！这位名震天下的大神探，竟然自以为是地将他的温顺羔羊独自送入了屠宰场！

在阴暗的站台角落里，我忍不住发出了快意至极的低声狂笑。若正面与福尔摩斯那等妖孽较量，鹿死谁手尚未可知；然而若对手仅仅是约翰·H·华生那个头脑简单、四肢发达的钝拙退伍军医，这场狩猎简直宛如杀鸡宰鹅般轻而易举！

我返回圣约翰伍德，粗暴地扯起面如死灰的贝丽尔，搭乘午夜的邮政快车秘密西行。十月十四日拂晓时分，我们已然重返达特穆尔荒原深处的梅利琵宅邸。

我片刻未歇，踏着暗径直奔泥潭核心孤岛。我将那只沾满干泥的旧黑靴死死贴在那头嗜血巨兽喷吐粗气的鼻孔前。恶兽贪婪地深吸着这股浓烈的人肉体味，两只凶残的黄瞳骤然收紧，喉咙里爆发出一阵滴淌口水、狂暴难耐的嗜血呜咽！

陷阱已然全面合围。亨利·巴斯克维尔，正一步步踏入我为你量身定做的地狱血盆大口！"""
    },

    # Chapter 6 Part 1
    {
        "id": "stapleton_ch06_part1_arrival_watch",
        "ch_idx": 5, "part": 1,
        "title_en": "Chapter 6: Baskerville Hall (Part I: The Arrival of the Quarry)",
        "title_cn": "第六章 巴斯克维尔庄园（上：猎物入瓮与荷枪护送）",
        "pov": "stapleton", "type": "anchor", "anchor": "anchor_arrival_moor_stapleton",
        "clues_en": [
            "Sir Henry and Dr. Watson arrive under armed police escort due to Selden's prison break",
            "Stapleton spots the Escaped Convict Selden factor as a chaotic wildcard",
        ],
        "clues_cn": [
            "亨利爵士与华生医生在持枪骑警全副戒备的武装护卫下踏入巴斯克维尔庄园大门",
            "惊悉诺丁山残暴屠夫逃犯塞尔登越狱潜伏荒原，将其锁定为随时可资利用的嗜血乱局棋子",
        ],
        "choices_en": [
            {"id": "s_ch6_p1_c1", "text": "Return to Merripit House and brutally terrorize Beryl into absolute submission.", "target": "stapleton_ch06_part2_beryl_chains"},
            {"id": "s_ch6_p1_c2", "text": "[Switch POV to Sherlock Holmes] View Holmes observing the wagonette from the Black Tor hut.", "target": "holmes_ch06_part2_hut_surveillance", "pov_switch": "holmes"},
        ],
        "choices_cn": [
            {"id": "s_ch6_p1_c1", "text": "折返梅利琵宅邸，以最残忍的暴力手段将企图反抗的贝丽尔彻底威慑囚禁在掌中。", "target": "stapleton_ch06_part2_beryl_chains"},
            {"id": "s_ch6_p1_c2", "text": "【视角切换：歇洛克·福尔摩斯】切换至黑色岩岗史前石屋，看名侦探如何用军用远望镜俯瞰马车抵庄。", "target": "holmes_ch06_part2_hut_surveillance", "pov_switch": "holmes"},
        ],
        "content_en": """On the afternoon of October 15th, I stood upon the granite crest of Belliver Tor, pressing my brass pocket telescope to my eye. The autumn sky was dull and overcast, and a cold, wet wind blew from the Atlantic across the waste.

Upon the Bovey road, a cloud of dust heralded the approach of the wagonette.

Through the glass, I brought the travelers into focus. There was young Sir Henry, looking eagerly about him at his ancestral moors, wrapped in a Canadian fur-trimmed coat. Beside him sat Dr. Watson, square-jawed, upright, his hand resting conspicuously upon the bulge of his tweed overcoat pocket where his army service revolver lay ready for action. And flanking the vehicle rode two county constables with carbines resting upon their saddlebows.

A comical escort! As though a lead bullet could stop a demon forged of hell-fire and ancient darkness!

The presence of the armed police had an unexpected cause: Selden, the Notting Hill murderer, had escaped from the granite cells at Princetown three days before and was starving somewhere upon the tors. A delicious complication! If an escaped cutthroat was known to roam the moor, any sudden violence, any cry in the dark, any mangled corpse upon the stones would instantly be laid at the convict's door!

I watched the wagonette turn through the ancient stone piers of Baskerville Hall. The heavy iron gates swung shut behind them.

The sheep was in the pen! Sir Henry was now separated from civilization by twenty miles of untamed moorland, with only a credulous doctor to shield his throat!

A thrill of predatory exultation pulsed through my veins. The gold of Sir Charles was already glittering before my eyes. I packed my glass and hastened down the slope to Merripit House to ensure that my domestic cage was secure.""",
        "content_cn": """十月十五日的午后，我伫立在贝利弗岩岗（Belliver Tor）最高处的花岗岩脊线上，单筒黄铜望远镜死死锁定了波维大道的尽头。深秋的天空阴霾低沉，一股裹挟着湿气的冰冷朔风正掠过大西洋浩瀚的荒原。

在大道转角处，一扬漫天而起的黄色尘土宣告了双排敞篷马车的疾驰逼近。

借由镜片，来客的面容清晰可辨。那位年轻的亨利爵士正满怀好奇与新奇地眺望着他祖辈留下的苍凉荒原，身上裹着一件加皮毛领的厚实大氅；坐在他身侧的便是华生医生，方下巴，身板笔挺，右手警惕地按在大衣口袋沉甸甸的凸起处——那里显然紧贴着他那把大口径军用左轮手枪；而在马车两侧，两名郡警正横挎卡宾枪如临大敌般护卫随行。

滑稽可笑的武装护卫！这帮蠢货竟然天真地以为，凡间的铅弹当真能够挡得住一头诞生于九幽地狱火海与古老魔咒之中的复仇恶兽？！

而这批武装骑警的全副戒备，源于另一桩令整片教区人心惶惶的突发事变：三天前，残杀多名无辜者的诺丁山屠夫逃犯塞尔登凿壁越狱，此刻正潜藏在花岗岩乱石迷宫中茹毛饮血！这真是一个绝妙而极具利用价值的意外收获！倘若世人皆知荒原上游荡着一个穷凶极恶的持刀越狱犯，那么在这片土地上发生的任何暴行、任何夜半凄厉的惨叫，乃至任何横尸悬崖的碎尸惨案，都将在第一时间被愚蠢的世人顺理成章地扣在逃犯头上！

我目送着马车辚辚驶入巴斯克维尔庄园那两座古老的石柱大门，两扇沉重锈蚀的铁门在他们身后重重闭合。

羊羔终于正式赶入了屠宰圈！如今亨利爵士已被方圆二十英里的荒蛮荒原与现代文明彻底切断，在他脆弱的脖颈前，仅仅横隔着一个头脑简单、极易受骗的糊涂军医！

一股野兽撕咬猎物前的狂暴快感瞬间传遍了我的四肢百骸。查尔斯那七十四万镑的黄金巨矿，已然在我眼前绽放出触手可及的夺目光彩！我收起望远镜，快步走下山脊折返梅利琵宅邸，务必在狩猎拉开序幕之前，将我的家宅牢笼彻底封死！"""
    },

    # Chapter 6 Part 2
    {
        "id": "stapleton_ch06_part2_beryl_chains",
        "ch_idx": 5, "part": 2,
        "title_en": "Chapter 6: Baskerville Hall (Part II: The Tyrant of Merripit House)",
        "title_cn": "第六章 巴斯克维尔庄园（下：梅利琵宅邸的暴虐枷锁）",
        "pov": "stapleton", "type": "branch", "anchor": None,
        "clues_en": [
            "Stapleton violently threatens Beryl with the hound if she speaks to Sir Henry",
            "Beryl is kept prisoner in the lonely house surrounded by the deadly bog",
        ],
        "clues_cn": [
            "斯台普吞以恶犬撕碎咽喉为要挟，严令贝丽尔绝不许向新爵士吐露半字实情",
            "在孤立无援的荒原农舍中将美貌异国娇妻彻底囚禁，充当引诱富豪的致命玩偶",
        ],
        "choices_en": [
            {"id": "s_ch6_p2_c1", "text": "Stroll onto the moor with butterfly net to intercept Watson and evaluate his intellect.", "target": "stapleton_ch07_part1_naturalist_act"},
            {"id": "s_ch6_p2_c2", "text": "Prepare the hound's feeding schedule on the mire island for the coming night.", "target": "stapleton_ch07_part1_naturalist_act"},
        ],
        "choices_cn": [
            {"id": "s_ch6_p2_c1", "text": "手提捕蝶网漫步荒原泥潭小径，主动结识华生医生并当面测试其观察力与警惕心。", "target": "stapleton_ch07_part1_naturalist_act"},
            {"id": "s_ch6_p2_c2", "text": "踏着暗径潜入大格林盆泥潭孤岛，为今晚恶兽的血食配给制定精准时刻表。", "target": "stapleton_ch07_part1_naturalist_act"},
        ],
        "content_en": """I entered Merripit House through the kitchen scullery. The house was cold and damp, filled with the sharp, acidic odor of the cyanide jars I used to kill my insect specimens.

In the sitting-room, Beryl was standing by the window, staring out toward the dark towers of Baskerville Hall. When she heard my step, she started like a struck deer, her face blanching to the lips.

'He has arrived,' I said, shutting the door behind me and locking it with a slow, deliberate turn of the key.

She pressed her back against the wall, her dark eyes wide with terror. 'Jack... I implore you! In the name of the Christ you blaspheme, let this boy live! He has never wronged you! Take what money we have and let us fly!'

I crossed the room in two strides, seized her by the throat, and forced her down into an armchair until her breath came in ragged, choking gasps.

'Listen to me, my beautiful little hypocrite,' I murmured, leaning over her until my lips brushed her ear. 'You tried to ruin me in London with your cut newspaper. I forgave you because I needed your face. But here on Dartmoor, the game is played with blood, not paper! If you whisper one syllable to Sir Henry—if you breathe one hint that you are my wife and not my sister—I will not merely kill him. I will take you out to the tin-shed in the mire, chain you to the iron ring in the wall, and leave you in the dark with the beast!'

A shudder of convulsive horror racked her slender frame. She slid from the chair onto her knees, weeping in broken, hopeless despair.

'I will be silent,' she moaned, kissing the hem of my coat. 'God help me, I will be silent!'

'See that you are,' I said, stepping over her. 'Tomorrow, the doctor will explore the moor. I shall go out with my butterfly net and introduce myself. A charming, garrulous naturalist—the very man to win an honest soldier's confidence!'

I unlocked the door and went into the kitchen to prepare my poisons. The web was spun; the spider was ready.""",
        "content_cn": """我穿过满是煤灰的后厨侧门跨入了梅利琵宅邸。整栋宅院阴冷刺骨，弥漫着我用来毒杀昆虫标本的氰化钾药瓶散发出的微苦杏仁味与刺鼻酸气。

在昏暗狭窄的起居室里，贝丽尔正伫立在窗棂前，双眼失魂落魄地凝视着远方巴斯克维尔庄园那两座森严高耸的雉堞塔楼。当听到我那熟悉的皮鞋踩踏木地板的脚步声时，她整个人如中箭的雌鹿般猛地一颤，脸上的血色瞬间退至毫无生气的惨白。

‘他到了，’我随手掩上房门，神色平静地将门锁徐徐反拧到底。

她背脊死死抵住冰冷的墙壁，两只黑亮深邃的眼眸因极度的恐惧而剧烈放大。‘杰克……我求求你！看在上帝的面子上，放过那个年轻人吧！他从未做过任何对不起你的事！带上我们所有的积蓄，求你带我远走高飞吧！’

我两步跨越房间，右手如铁钳般瞬间卡死了她那纤细雪白的咽喉，将她整个人狠狠按死在扶手椅中，直到她的喉管发出急促痛苦的窒息抽噎！

‘给我听清楚了，我美艳绝伦的小伪君子，’我俯下身躯，温热的呼吸吐在她发颤的耳垂上，‘在伦敦，你用那张破报纸险些砸了我毕生的心血。我没有杀你，仅仅是因为这具绝美的皮囊日后还有大用！然而在这片荒蛮嗜血的达特穆尔荒原上，博弈的筹码是滚烫的活人热血，而不是小女人的剪纸游戏！倘若你敢向亨利爵士吐露半个字——倘若你敢向任何人走漏半句你是我的合法妻子而非胞妹的真相——我不仅会当场要了他的命，更会将你亲手拖进大格林盆泥潭的废弃工棚，用铁链死死锁在墙角的石环上，将你一个人扔在漆黑的绝境中，与那头饥肠辘辘的恶兽同处一室！’

一阵濒临神经崩溃的剧烈抽搐瞬间传遍了她娇柔的身躯。她无力地从扶手椅上滑跪在地板上，掩面放声痛哭，发出绝望无助的凄厉悲鸣。

‘我闭嘴……我发誓我什么都不会说！’她屈辱地亲吻着我的皮鞋边沿抽泣道，‘求求上帝救救我，我一个字都不会说的！’

‘最好如此，’我面无表情地跨过她瘫软的身躯，‘明天一早，那位自以为是的华生医生必定会巡查荒原。我将带上我的捕蝶网亲自出迎。一个博学热情、滔滔不绝的温良学者——天下还有什么比这更适合博取一位直肚肠退伍老兵的无条件信赖？！’

我旋开门锁，径直踏入暗室调配我的化学毒药。天罗地网已然彻底织就；捕杀猎物的剧毒蜘蛛，已然磨砺好了致命的毒牙！"""
    }
])
# Stapleton Chapter 7 & 8
STAPLETON_NODES.extend([
    # Chapter 7 Part 1
    {
        "id": "stapleton_ch07_part1_naturalist_act",
        "ch_idx": 6, "part": 1,
        "title_en": "Chapter 7: The Stapletons of Merripit House (Part I: The Mask of the Naturalist)",
        "title_cn": "第七章 梅利琵宅邸的主人斯台普吞（上：温雅博物学者的伪装）",
        "pov": "stapleton", "type": "anchor", "anchor": "anchor_naturalist_stapleton",
        "clues_en": [
            "Stapleton charms Watson with eccentric naturalist persona near Grimpen Mire",
            "Demonstrates pony swallowed in mire to establish bog's terrifying lethality",
            "Inquires about Sherlock Holmes to confirm the great detective is truly in London",
        ],
        "clues_cn": [
            "手持捕蝶网在荒原小径截获华生，以博学温和的学者谈吐博取对方信任",
            "当场向华生展示达特穆尔矮种野马失足陷顶惨死全过程，借泥潭神威震慑其胆魄",
            "旁敲侧击试探歇洛克·福尔摩斯的真实行踪，确凿核实神探确未随行亲临德文郡",
        ],
        "choices_en": [
            {"id": "s_ch7_p1_c1", "text": "Pursue a cyclopides moth into the heather, leaving Watson to encounter Beryl.", "target": "stapleton_ch07_part2_beryl_blunder"},
            {"id": "s_ch7_p1_c2", "text": "[Switch POV to Dr. Watson] View Watson's first encounter with Stapleton upon the moor.", "target": "ch07_part1_naturalist", "pov_switch": "watson"},
        ],
        "choices_cn": [
            {"id": "s_ch7_p1_c1", "text": "假意扑打珍稀环纹蝶脱身深入草丛，暗中窥视华生与从后方冲出的贝丽尔之接触。", "target": "stapleton_ch07_part2_beryl_blunder"},
            {"id": "s_ch7_p1_c2", "text": "【视角切换：约翰·H·华生】切换至华生视角，见证他如何对这位古怪学者产生最初好感。", "target": "ch07_part1_naturalist", "pov_switch": "watson"},
        ],
        "content_en": """The morning of October 16th was brilliant with pale, watery autumn sunshine. Armed with my green gauze net and botanical collecting box, I strolled along the cart track leading from Merripit House toward the Hall.

Presently, as I had anticipated, the square, burly figure of Dr. Watson appeared upon the crest of the hill. He walked with his hands in his pockets, his pipe between his teeth, scanning the wilderness with the curious eye of a stranger.

I quickened my pace, calling out with the cheerful, uninhibited warmth of an isolated country enthusiast.

'Dr. Watson, I presume! Pray excuse the lack of ceremony, but here upon the moor we dispense with provincial etiquette. I am Jack Stapleton, of Merripit House.'

The good doctor was charmed. In two minutes, we were conversing like old comrades. I pointed out the ancient ruins of the Neolithic stone huts upon the tors, descanted upon the rare flora of the peat-bogs, and spoke with tender melancholy of poor Sir Charles's tragic demise.

Suddenly, from the emerald quagmire behind us, a wild shriek broke upon our ears. A Dartmoor pony, venturing onto the false green moss, was being sucked alive into the black morass!

I gripped Watson's arm, pointing with my net. 'Look, Dr. Watson! The Great Grimpen Mire! A false step means instant, inescapable death! That pony will be under in two minutes!'

Watson stared in frozen horror as the beast vanished beneath the bubbling slime. The lesson was etched into his soul: the moor was a place of deadly horror.

Then, with casual indifference, I dropped the probe:

'We were all deeply disappointed that Mr. Sherlock Holmes did not honor our county with a visit. Is it true that he remains entirely in London?'

Watson smiled with modest pride. 'He is immersed in an urgent metropolitan affair. For the present, Sir Henry is under my sole charge.'

Under your sole charge! I had to bite my lips to suppress the triumphant grin that threatened to unmask my face. The road to the fortune was clear!""",
        "content_cn": """十月十六日清晨，惨淡湿润的深秋日光洒满荒原。我手挽绿纱长柄捕蝶网，肩跨采集铁盒，悠闲地漫步在从梅利琵宅邸通往庄园的大道碎石路旁。

果不其然，正如我所预料的那样，华生医生那敦实魁梧的身形很快出现在了山脊的转角处。他双手插在风衣口袋里，嘴里叼着石楠烟斗，正用一个外来异乡人特有的好奇与警惕审视着这片荒凉的荒原。

我加快脚步迎上前去，脸上堆满了常年隐居乡野的学者在偶遇同道时特有的爽朗与狂热。

‘想必阁下定是华生医生了！万望恕我冒昧未递名片，但在这片天高地阔的荒原之上，繁文缛节早已被我们抛之脑后。在下杰克·斯台普吞，梅利琵宅邸的主人。’

这位善良憨厚的退伍军官瞬间被我的热情所打动。短短两分钟之内，我们已然如故交老友般并肩侃侃而谈。我信手指向远古石屋遗址向他考据新石器时代的不列颠土著，滔滔不绝地品评着泥炭藓类的珍稀属性，并适时流露出对可怜查尔斯爵士猝然长逝的无限哀思。

突然之间，我们身后的大格林盆泥潭深处猛地炸响了一声凄厉绝望的惨嘶！一匹野生矮种小马因贪恋嫩草，一脚踩穿了伪装成草坪的致命泥壳，正在万丈黑浆中绝望扑腾灭顶！

我一把死死抓住华生的手腕，捕蝶网的竹柄遥指泥沼：‘瞧啊，华生医生！这便是大格林盆泥潭！踏错半步，便是神仙难救的万劫不复！不出两分钟，那匹马便会彻底沉入地心！’

华生目瞪口呆、浑身战栗地亲眼目睹着那头可怜的活物被翻滚恶臭的水泡彻底吞噬。这堂生动惨烈的现场解剖课已将深入骨髓的恐惧深深烙印在了他的脑海深处：达特穆尔是一座动辄吞人嚼骨的绝命死渊！

紧接着，在漫不经心的谈笑之间，我漫不经心地抛出了那枚致命的试探之针：

‘原本全教区的人都热切期盼着大名鼎鼎的歇洛克·福尔摩斯先生能亲临德文郡避暑视察，真是令人遗憾万分。不知传闻是否属实，那位大神探果真彻底留守伦敦未曾成行吗？’

华生脸上流露出一丝军人特有的含蓄自豪：‘伦敦有一桩极其重大的公海勒索要案死死缠住了他的身躯。在目前这段时期内，亨利爵士的一切安全防务全权交由我一人全权照料。’

全权交由你一人照料！我必须死死咬住舌尖，才勉强压抑住了那抹险些撕破我温雅伪装的狰狞狂笑！通往七十四万英镑黄金王座的康庄大道，已然坦荡如砥！"""
    },

    # Chapter 7 Part 2
    {
        "id": "stapleton_ch07_part2_beryl_blunder",
        "ch_idx": 6, "part": 2,
        "title_en": "Chapter 7: The Stapletons of Merripit House (Part II: The Blunder on the Path)",
        "title_cn": "第七章 梅利琵宅邸的主人斯台普吞（下：泥潭小径上的惊险破绽）",
        "pov": "stapleton", "type": "branch", "anchor": None,
        "clues_en": [
            "Beryl secretly ran out to intercept Watson, mistaking him for Sir Henry",
            "Stapleton catches her, suppresses her with cold sisterly domestic facade",
            "Realizes Beryl's rebellious spirit must be crushed before the final strike",
        ],
        "clues_cn": [
            "贝丽尔背地里狂奔出农舍拦路阻截，误将华生当作亨利爵士发出绝命撤退警告",
            "斯台普吞假意扑蝶折返撞破密谈，以高超冷酷的‘兄长’伪装掩饰滔天杀机",
            "清醒认识到妻子内心的反叛烈火仍在燃烧，决意在决战前夜施加更残酷的高压管制",
        ],
        "choices_en": [
            {"id": "s_ch7_p2_c1", "text": "Invite Watson and Sir Henry to dine at Merripit House to cement the social trap.", "target": "stapleton_ch08_probing_watson"},
            {"id": "s_ch7_p2_c2", "text": "Inspect the hound's chains and security upon the mire island.", "target": "stapleton_ch08_probing_watson"},
        ],
        "choices_cn": [
            {"id": "s_ch7_p2_c1", "text": "正式向华生与亨利爵士发出梅利琵宅邸午后茶会之约，将猎物引入社交死角。", "target": "stapleton_ch08_probing_watson"},
            {"id": "s_ch7_p2_c2", "text": "踏着暗径返回泥潭孤岛，复查恶兽项圈铁链的坚固度与绝密防御设施。", "target": "stapleton_ch08_probing_watson"},
        ],
        "content_en": """I feigned sudden excitement, pointing my net toward a fluttering speck of brown among the heather, and sprinted away across the bog, leaving Watson to walk down the track alone.

My departure was no accident. I wished to observe the doctor from behind the boulders. But what met my eyes as I crested the granite ridge turned my blood to liquid fire!

Beryl! The wretched, rebellious little fool had slipped from the cottage and was running breathless across the heath!

Through the gaps in the gorse, I watched her seize Watson by the arm. Her hands were flying, her eyes wild with passionate appeal. Even from a distance of two hundred yards, I could read her frantic pantomime: she was commanding him to turn back, to flee to London, to escape the doom of the Baskervilles! She had mistaken the stocky doctor for the Canadian baronet!

My hand clenched around my butterfly stick until the bamboo groaked. One word of the hound, one whisper of our true marriage, and my neck would feel the hemp before the week was out!

I leaped from the rocks, swinging my net, whistling a light operatic air as though returning from a successful chase.

'Halloa, Beryl!' I shouted cheerfully. 'What brings you out upon the moor?'

The effect was instantaneous. She stiffened as though an electric shock had passed through her spine. She stepped back from Watson, her face freezing into that blank, marble mask she wore when the whip was raised.

'I was out walking, Jack,' she stammered, 'and I... I mistook this gentleman for Sir Henry.'

I laughed, a rich, pleasant brotherly laugh that radiated amused indulgence.

'Ah, my dear, you must forgive my sister, Dr. Watson! She is terrified of the moor, and the tragedy of poor Sir Charles has unstrung her nerves. Come, Watson, you must walk back with us to Merripit House and take a cup of coffee before you return to the Hall!'

Watson was utterly disarmed. He suspected nothing. But as we walked three abreast down the gravel lane, my nails dug into the palms of my hands until the blood ran.

Beryl's defiance was becoming an acute, intolerable hazard. When the night of the final kill arrived, she would not merely be warned—she would be bound, gagged, and broken beyond the power to betray!""",
        "content_cn": """我故作狂喜失态，指着石楠花丛中一只翻飞的褐色飞蛾，挥舞着捕蝶网狂奔深入沼泽，留下华生一人沿着小道信步漫游。

我的抽身绝非偶然。我本意是借着巨石盲区暗中反向监视这位军医的独处神态。然而，当我翻上一处花岗岩山脊回首眺望的一刹那，眼前的景象险些将我浑身的血液彻底烧沸！

贝丽尔！那个该死、愚不可及的反叛贱人竟然趁我不备偷偷溜出了宅邸，正气喘吁吁地在石楠丛中亡命飞奔！

透过荆棘丛的空隙，我惊见她猛地扑上前死死抓住了华生的衣袖！她双手狂乱地比划着，眼中喷涌着撕心裂肺的绝望哀求！即便隔着整整两百码的距离，我也能轻易读懂她那疯狂的肢体语言：她在声嘶力竭地逼迫对方立刻滚回伦敦，逃离这片必死的诅咒荒原！她竟然把这个敦实的矮个子军医误当成了远道而来的加拿大堂弟！

我的右手死死捏紧了手里的竹柄捕蝶网，指节泛出青白，竹竿甚至被我硬生生捏裂！只要她从牙缝里吐出半句关于恶犬的实情，或是泄露半点我们真实夫妻关系的秘密，不出七天，粗糙的绞索便将套死在我的脖颈之上！

我猛地从巨石后飞身跃下，嘴里轻快地吹着一曲欢快的歌剧口哨，捕蝶网在空中漫不经心地摇晃，俨然一副刚刚大获全胜归来的无邪模样。

‘哈喽，贝丽尔！’我爽朗地高声呼喊道，‘究竟是什么兴致把你这位娇小姐也引到了荒原上？’

奇迹般的震慑效果在一刹那间显现无遗。她整个人宛如被数万伏特的高压电穿透了脊椎，浑身剧烈一僵，面孔在半秒钟之内被冻结成了一张毫无生气的惨白大理石面具——正是每当皮鞭举起时她所展现出的绝望麻木。

‘我只是出来散散步，杰克，’她结结巴巴地强咽下一口唾沫，‘而我……我刚才误将这位先生认成了亨利爵士。’

我仰天大笑起来，笑声温厚、慈爱而充满了长兄对幼妹那种宠溺的宽容包容。

‘啊，我亲爱的华生医生，您可千万别见怪！我这妹妹生性胆怯脆弱，对这片荒原畏之如虎，查尔斯老爵士的不幸暴毙更是彻底摧毁了她的神经。走吧，华生，既然到了家门口，务必请随我们一同踏入梅利琵宅邸品上一杯热咖啡再返庄园！’

华生完全被这温馨体面的家庭伪装彻底缴械，毫无半点戒心。然而当我们三人并肩穿过碎石车道时，我的指甲已然深深刺入了掌心的皮肉，鲜血顺着指缝悄然滴落。

贝丽尔的桀骜不驯已然演变成了最致命的定时炸弹。等到最后动手猎杀的那个良夜降临之时，我绝不会仅仅满足于言语恐吓——我将用粗麻绳将她彻底五花大绑、用布条死死塞住嘴唇，让她连半个背叛的音节都休想吐露！"""
    },

    # Chapter 8
    {
        "id": "stapleton_ch08_probing_watson",
        "ch_idx": 7, "part": 0,
        "title_en": "Chapter 8: First Report of Dr. Watson (Probing the Doctor over Tea)",
        "title_cn": "第八章 华生医生的第一份报告（品茶试探与虚假的安心）",
        "pov": "stapleton", "type": "branch", "anchor": None,
        "clues_en": [
            "Sir Henry visits Merripit and falls violently in love with Beryl at first sight",
            "Stapleton feigns hysterical brotherly jealousy to prevent dangerous intimacy",
            "Watson writes extensive reports to Baker Street, unaware Holmes is secretly deployed",
        ],
        "clues_cn": [
            "亨利爵士亲临梅利琵宅邸登门拜访，在茶会上一眼不可自拔地迷恋上了贝丽尔",
            "斯台普吞假意暴跳如雷上演‘护妹心切’的病态吃醋狂怒，严防二人私相授受",
            "确信华生正日夜不停向伦敦贝克街寄出毫无威胁的书信战报，对全局毫无警觉",
        ],
        "choices_en": [
            {"id": "s_ch8_c1", "text": "Sneak into the Great Grimpen Mire at midnight to feed raw meat to the hungry beast.", "target": "stapleton_ch09_part1_feeding_the_hound"},
            {"id": "s_ch8_c2", "text": "[Switch POV to Sherlock Holmes] View Holmes in his stone hut reading Watson's first dispatch.", "target": "holmes_ch08_watson_report", "pov_switch": "holmes"},
        ],
        "choices_cn": [
            {"id": "s_ch8_c1", "text": "趁着午夜万籁俱寂，手提生鲜血食潜入大格林盆泥潭深处，犒劳饥渴暴虐的恶兽。", "target": "stapleton_ch09_part1_feeding_the_hound"},
            {"id": "s_ch8_c2", "text": "【视角切换：歇洛克·福尔摩斯】切换至黑色岩岗石屋，看名侦探就着烛光逐字剖析华生密报。", "target": "holmes_ch08_watson_report", "pov_switch": "holmes"},
        ],
        "content_en": """The days that followed were a masterpiece of calculated sociability.

I called at Baskerville Hall, paying my respects to the young baronet with all the deferential charm of an eccentric country neighbor. Sir Henry, starving for companionship in that cavernous granite mausoleum, seized upon my company with boyish gratitude. Within forty-eight hours, he was a regular visitor at Merripit House.

And there, the second half of my strategy bore instant, intoxicating fruit: Sir Henry fell passionately, blindly, head-over-heels in love with Beryl!

He could not take his eyes from her exquisite face. Whenever she poured his tea, his hand trembled; whenever she spoke in that soft, foreign cadence, his eyes shone with adoration.

It was a magnificent advantage, yet one that required razor-sharp navigation. If I permitted an open courtship, Sir Henry might marry her, take her away to London, and discover our true marriage before I could strike!

I executed a stroke of psychological genius: I staged a scene of violent, hysterical jealousy!

When Sir Henry attempted to declare his passion to Beryl upon the moor path, I burst from the gorse bushes, white with simulated fury. I insulted the baronet, accused him of taking advantage of an unprotected maiden, and ordered him from my property!

Sir Henry was humiliated and bewildered, but his desire was inflamed a hundredfold. Opposition merely stoked his determination to possess her. He apologized, begged for my forgiveness, and promised to keep his distance until I gave my brotherly consent.

Meanwhile, Dr. Watson was scribbling away in his notebook by the hall fireside. Through the village postmaster, whose daughter was friendly with my scullery maid, I learned that Watson was mailing voluminous packets of manuscript to Baker Street twice a week.

Let the fool write! Let him describe the trees, the clouds, the melancholy butler, and my eccentric botanical collections! While Dr. Watson wrote romance and Sherlock Holmes sat idly smoking by his London fireplace, the clock was ticking down to the final catastrophe!""",
        "content_cn": """接下来的几天堪称一场教科书级别的社交心理战杰作。

我以邻家热心学者的体面身份正式登门造访巴斯克维尔庄园。在这座空旷阴冷、犹如古墓般死寂的花岗岩城堡里，百无聊赖、渴望交际的年轻亨利爵士如获至宝般抓住了我的友谊。短短四十八小时之内，他便已然成为了梅利琵宅邸茶席上的常客。

正是在这里，我杀局的另一重毒计结出了令我狂喜沉醉的丰硕果实：亨利爵士无可救药、彻底盲目地疯狂迷恋上了贝丽尔！

他的那对黑眼睛一刻也舍不得从她那张绝美动人的异国面庞上挪开。每当贝丽尔为他斟倒红茶时，他的手指甚至在抑制不住地微微发颤；每当她用那软糯带有异国腔调的嗓音开口时，这位年轻男爵的眸子里便喷涌出无限的崇拜与爱慕！

这是一记价值连城的王牌，然而却需要最为精确的走钢丝操作。倘若我放任他们公开热恋，亨利爵士很可能当场求婚并将其强行带往伦敦完婚，从而在我的猎杀动手前戳破我们乃是合法夫妻的真相！

于是，我当众上演了一出堪称心理学奇迹的癫狂大戏：一记蓄谋已久的病态吃醋狂怒！

当亨利爵士试图在荒原小径旁背地里向贝丽尔吐露炽热衷肠时，我如疯狗般猛地从金雀花丛中杀出，面孔扭曲、浑身发颤。我当着华生的面厉声痛骂男爵居心叵测、竟敢企图玷污侮辱一个无依无靠的乡野纯洁孤女，并当场将他粗暴地轰出了我的领地！

亨利爵士被骂得无地自容、羞愧万分，然而这记当头棒喝却将他骨子里的占有欲与征服欲瞬间点燃了上百倍！得不到的阻隔，反而让他发疯般下定决心务必娶到贝丽尔。他登门谢罪，苦苦哀求我的宽恕，并信誓旦言在未获得我这位‘大舅哥’的首肯之前绝不越雷池半步！

与此同时，那位可爱的华生医生正整日窝在庄园壁炉旁奋笔疾书。透过村邮局的私下眼线，我确凿获悉，华生每周都会雷打不动地向伦敦贝克街寄出厚厚两大包详尽的日记战报。

任由这个蠢材去写吧！让他去极尽能事地描摹荒原的落叶、凄凉的乌云、红眼睛的管家以及我那些看似人畜无害的珍稀昆虫标本！当华生在写着他的骑士小说、而歇洛克·福尔摩斯正安坐于伦敦壁炉旁无聊吐着烟圈之际，死亡的钟摆正在一分一秒地逼近最后的末日审判！"""
    }
])
# Stapleton Chapter 9 & 10
STAPLETON_NODES.extend([
    # Chapter 9 Part 1
    {
        "id": "stapleton_ch09_part1_feeding_the_hound",
        "ch_idx": 8, "part": 1,
        "title_en": "Chapter 9: The Light upon the Moor (Part I: Feeding the Demon in the Mire)",
        "title_cn": "第九章 沼地上的烛光（上：夜入泥潭饲喂恶兽）",
        "pov": "stapleton", "type": "anchor", "anchor": "anchor_convict_stapleton",
        "clues_en": [
            "Stapleton sneaks across the mire at 1 AM to feed blood and meat to the starving hound",
            "The beast's muffled baying rolls across the moor, striking terror into the district",
        ],
        "clues_cn": [
            "斯台普吞在凌晨一点踏着暗径潜入孤岛，以鲜血淋漓的碎肉喂养饥肠辘辘的恶魔巨兽",
            "任由恶兽饱食后压抑沉闷的嗜血长嚎在荒原黑夜中滚滚回荡，在全教区播撒深入骨髓的恐怖",
        ],
        "choices_en": [
            {"id": "s_ch9_p1_c1", "text": "Hear gunshots across the granite tors and observe Watson chasing the convict.", "target": "stapleton_ch09_part2_night_alarm"},
            {"id": "s_ch9_p1_c2", "text": "[Switch POV to Dr. Watson] View Watson and Sir Henry hunting Selden across the moonlit moor.", "target": "ch09_part2_moor_chase", "pov_switch": "watson"},
        ],
        "choices_cn": [
            {"id": "s_ch9_p1_c1", "text": "听闻花岗岩绝壁方向骤然爆发出清脆枪响，隐蔽在巨石后窥视华生夜巡围捕逃犯。", "target": "stapleton_ch09_part2_night_alarm"},
            {"id": "s_ch9_p1_c2", "text": "【视角切换：约翰·H·华生】切换至荒原乱石堆，体验华生与爵士端枪疾驰围捕狂暴越狱犯。", "target": "ch09_part2_moor_chase", "pov_switch": "watson"},
        ],
        "content_en": """At one in the morning of October 20th, when the house was silent and Beryl was safely locked in her bedroom, I slipped out into the fog.

In my canvas sack, I carried ten pounds of bloody sheep-offal obtained from an outlying farm near Ashburton. The journey across the Great Grimpen Mire by night was a test that would have shattered the nerve of any ordinary man. The black slime bubbled and hissed on either side; a misstep of four inches would have meant plunging into the subterranean abyss. But my feet knew every sunken tussock and granite footing as a spider knows its web.

I reached the island. The moment my boot scraped the threshold of the tin shed, a deep, resonant rumble vibrated the timber walls.

The hound knew my step.

I unhitched the lantern and hung it from the central beam. In the dim yellow glow, the beast loomed like a nightmare from the nether world. Its ribs were lean, its eyes blazing with famished fury. I flung the raw meat across the floor. It seized the flesh with savage, crunching jaws, tearing the sinews with sounds that turned my own heart to ice.

While it fed, I dipped a rag into my bucket of water, wiped its crusted jaws, and smoothed the matted black fur of its flank.

When the last scrap was devoured, the creature threw back its massive head and gave vent to a long, mournful, shuddering howl that rose and fell in a dreadful cadence, echoing out through the broken roof of the shed across the vast, moonlit expanse of the moor!

I did not silence it.

Let the moor hear the voice of its demon! Let Sir Henry tremble beneath his blankets in the Hall! Let the legend sink deeper into the superstitious marrow of the countryside! Every howl prepared the minds of the coroner and the jury to accept his death as the inevitable visitation of the ancestral curse!""",
        "content_cn": """十月二十日凌晨一点整，当整座宅邸万籁俱哀、贝丽尔已被我反锁在二楼卧室之后，我悄然踏入了茫茫夜雾之中。

在沉重的帆布粗麻袋里，装着我从阿什伯顿附近偏远农庄秘密采买来的十磅血淋淋的羊杂与碎肉。在深更半夜只身横穿大格林盆泥潭，是对人类神经极限的最残酷考验。两侧的无底黑浆咕嘟翻滚着致命的毒气与气泡；只要脚下踏错四英寸，便会瞬间被拖入永无天日的地下万丈深渊！然而我的双脚对于每一块沉水暗石与草墩的熟悉程度，宛如一只剧毒蜘蛛熟知自己的蛛网。

我踏上了孤岛。就在我的鞋尖刚刚触及废弃锡矿工棚门槛的一瞬间，一阵从地底深处泛起的低沉共鸣震得整面木板墙壁嗡嗡作响！

恶犬嗅到了我熟悉的气味。

我摘下马灯挂在中央的横梁上。在昏黄摇曳的光柱中，那头庞然巨兽宛如一具从幽冥血海中爬出的活体恶魔。它的肋骨根根毕现，两只黄瞳中喷涌着饥肠辘辘的狂暴凶焰。我将大块带血的鲜肉重重掷在地板上。它发出一声狂暴的低吼，两排如匕首般锋利的利齿伴随着刺耳的骨骼脆响疯狂咀嚼撕扯，那咀嚼血肉的动静足以令任何硬汉的心脏彻底冰封。

在它狼吞虎咽之际，我用浸湿的抹布擦拭着它口角结痂的干涸血迹，梳理着它背脊上纠结成团的硬硬黑毛。

当最后一块碎骨被嚼碎咽下肚时，这头巨兽猛地扬起庞大沉重的头颅，从肺腑最深处爆发出一声凄厉、悠长、在天地间悲怆回荡的恐怖长嗥！那嚎叫如狂暴的海潮般忽高忽低，穿透坍塌的石板屋顶，在整片皎洁月色笼罩下的浩瀚荒原上空滚滚奔涌！

我没有制止它的狂吠。

让这片土地在它恶魔的咆哮声中战栗吧！让亨利爵士在庄园冰冷的被褥深处瑟瑟发抖吧！让这两百年的血腥神话更深地扎入乡野愚民迷信的骨髓之中！每一声震碎夜空的恶犬狂嗥，都在为日后验尸官与陪审团心甘情愿地将男爵之死归咎于天谴恶咒而打下最完美的心理铺垫！"""
    },

    # Chapter 9 Part 2
    {
        "id": "stapleton_ch09_part2_night_alarm",
        "ch_idx": 8, "part": 2,
        "title_en": "Chapter 9: The Light upon the Moor (Part II: Chaos on the Moor)",
        "title_cn": "第九章 沼地上的烛光（下：追捕逃犯与荒原暗机）",
        "pov": "stapleton", "type": "branch", "anchor": None,
        "clues_en": [
            "Watson and Sir Henry hunt Selden across the moonlit granite crags",
            "Stapleton spots an unknown tall, thin figure standing upon the summit of Black Tor",
        ],
        "clues_cn": [
            "华生与亨利爵士开枪追击诺丁山逃犯塞尔登，枪声打破荒原午夜死寂",
            "斯台普吞在返程途中惊见黑色岩岗绝壁顶端巍然伫立着一个神秘的瘦高黑影",
        ],
        "choices_en": [
            {"id": "s_ch9_p2_c1", "text": "Visit Laura Lyons at Coombe Tracey to ensure her absolute silence.", "target": "stapleton_ch10_coombe_control"},
            {"id": "s_ch9_p2_c2", "text": "Scout the prehistoric huts upon Black Tor to unmask the mysterious watcher.", "target": "stapleton_ch11_part1_spy_on_tor"},
        ],
        "choices_cn": [
            {"id": "s_ch9_p2_c1", "text": "火速亲赴库姆马西集镇密会劳拉·里昂斯，加固对其精神控制，彻底封死信件口风。", "target": "stapleton_ch10_coombe_control"},
            {"id": "s_ch9_p2_c2", "text": "带上猎枪暗中摸向黑色岩岗史前石屋群，彻查那个在月下傲视荒原的神秘暗哨。", "target": "stapleton_ch11_part1_spy_on_tor"},
        ],
        "content_en": """I locked the shed and picked my way back to the mainland. But as I reached the firm heather of the northern ridge, the crack of a pistol shot ripped through the freezing air!

A second shot followed, echoing sharp and clean against the granite tor!

I crouched in the shadow of a peat-hagg, unbuttoning my revolver. Had the county police discovered my island?

Then, through the silver moonlight, I saw the true cause of the commotion: across the high plateau, two miles distant, a shaggy, wild figure in yellow prison rags was leaping from boulder to boulder like a hunted stag. Pursuing him, firing into the dark, were Sir Henry and Dr. Watson!

They were hunting Selden! The fools were wasting their powder on a starving wretch!

I watched the chase with contemptuous amusement. But then, as my gaze followed the ridge of Black Tor against the brilliant disc of the full moon, my heart gave a sudden, violent thud!

High upon the jagged pinnacle of rock, standing motionless as a pillar of basalt, was the silhouette of a man!

A tall, gaunt figure, his arms crossed over his chest, his head bent forward in profound, vigilant concentration! He looked down into the valley where Sir Henry ran, watching the hunt like an omniscient bird of prey.

Who was he?

It was neither a constable nor a shepherd. No rustic ever held himself with that commanding, aristocratic poise. Could it be an accomplice of the convict? Or... could it be someone far more dangerous?

I remembered the duel in Regent Street—the piercing gray eyes through the glass of cab No. 2704!

Could Sherlock Holmes have lied? Could the great detective have slipped into Devonshire under a false name, camping upon the open moor like a wild beast?

An icy prickle of unease rippled down my neck. I must know who lived upon Black Tor! But first, I had to ensure that my rear was secure: Laura Lyons must be silenced beyond all possibility of betrayal!""",
        "content_cn": """我锁好工棚木门，踩着暗石折返陆地。然而就在我的双足刚刚踏上北侧山脊结实的石楠苔原时，一声清脆震耳的手枪枪响骤然撕碎了冰冷的寒夜！

紧接着是第二声枪响，在空旷的花岗岩峰峦间激荡起久久不绝的脆烈回音！

我瞬间伏倒在一处泥炭沟的浓黑阴影中，左手啪的一声解开了大衣下左轮手枪的枪套扣带。难道是这帮该死的郡警摸到了我隐匿恶犬的巢穴？！

然而，借由皎洁明亮的银白月色，我很快看清了骚乱的真相：在相距两英里外的高原乱石滩上，一个身穿黄色条纹囚服、蓬头垢面的狂暴身影正如被追捕的野鹿般在巨石间疯狂跳跃飞奔。而在他身后拔枪穷追不舍、在黑夜中连发数枪的，赫然正是亨利爵士与华生医生！

他们在围捕越狱犯塞尔登！这帮自作聪明的蠢材，竟然把珍贵的火药浪费在一个快要冻死的丧家犬身上！

我正暗自冷笑鄙夷，然而当我的视线顺着黑色岩岗那陡峭高耸的脊线、投向圆月悬挂的夜空背景时，我的心脏猛地爆发出了一记剧烈沉重的狂跳！

在黑色岩岗最险峻孤绝的巨岩之巅，在万丈月光那惨白的照耀之下，赫然傲立着一个如同玄武岩铁铸般的瘦高黑影！

那是一个身材异常瘦削挺拔的神秘人，双臂冷冷环抱于胸前，头颈微微前倾，以一种近乎全知全能的深邃与警惕，居高临下死死俯瞰着谷底亨利爵士的一举一动！

他是谁？！

那绝非笨拙愚钝的乡野巡警，更不可能是本地的羊倌。在这片蛮荒贫瘠的土地上，绝无任何凡夫俗子能够展现出如此冷峻孤高、傲视一切的统帅威仪！难道是逃犯暗中联络的同伙？抑或是……某个比逃犯凶险千百倍的索命克星？！

伦敦摄政街上那惊心动魄的对视如烙铁般再次烫痛了我的记忆——2704号马车车窗外，那对穿透玻璃的鹰隼般灰色寒眸！

难道歇洛克·福尔摩斯在贝克街演了一场弥天大谎？！难道全欧洲最顶尖的神探早已隐姓埋名潜入了德文郡，如同一头野兽般在达特穆尔荒原上秘密筑巢扎寨？！

一阵刺骨的寒意顺着我的颈椎疯狂向下攀爬。我必须彻查黑色岩岗上究竟盘踞着何方神圣！然而在此之前，我必须首先加固后方的防线：库姆马西的劳拉·里昂斯，绝不能让她漏出半点威胁我的口风！"""
    },

    # Chapter 10
    {
        "id": "stapleton_ch10_coombe_control",
        "ch_idx": 9, "part": 0,
        "title_en": "Chapter 10: Extract from the Diary of Dr. Watson (Muzzling Laura Lyons)",
        "title_cn": "第十章 华生医生日记摘录（封锁劳拉·里昂斯之口）",
        "pov": "stapleton", "type": "branch", "anchor": None,
        "clues_en": [
            "Stapleton visits Laura Lyons, renewing false promises of marriage and financial aid",
            "Warns her that any mention of the burnt letter will ruin her reputation and bring prison",
        ],
        "clues_cn": [
            "亲赴库姆马西重申婚姻虚妄诺言，用甜言蜜语与金钱资助进一步麻痹劳拉·里昂斯",
            "声色俱厉恐吓劳拉一旦向任何人透露半句侧门烧毁信件之事，必将名誉扫地同赴刑场",
        ],
        "choices_en": [
            {"id": "s_ch10_c1", "text": "Scout Black Tor with field glass and track the boy delivering supplies to the stone hut.", "target": "stapleton_ch11_part1_spy_on_tor"},
            {"id": "s_ch10_c2", "text": "[Switch POV to Sherlock Holmes] View Holmes reading Watson's diary extract regarding L.L.", "target": "holmes_ch10_diary_and_laura", "pov_switch": "holmes"},
        ],
        "choices_cn": [
            {"id": "s_ch10_c1", "text": "手持望远镜严密盘查黑色岩岗，暗中跟踪给史前石屋神秘怪客送饭的小厮行踪。", "target": "stapleton_ch11_part1_spy_on_tor"},
            {"id": "s_ch10_c2", "text": "【视角切换：歇洛克·福尔摩斯】切换至石屋，见证名侦探根据华生日记锁定L.L.真容。", "target": "holmes_ch10_diary_and_laura", "pov_switch": "holmes"},
        ],
        "content_en": """On the morning of October 22nd, I rode into Coombe Tracey. A rumor had reached me through the village gossip that Dr. Watson had been inquiring into the charitable beneficiaries of the late Sir Charles Baskerville.

If Watson approached Laura Lyons, the entire edifice of my plot was in mortal danger!

I stepped into her modest parlor unannounced. Laura was sitting at her Remington typewriter, looking pale and nervous. When she saw me, she sprang to her feet, throwing her arms around my neck with that clinging, suffocating affection that made my gorge rise.

'Jack!' she wept. 'I have been so terrified! The doctor from the Hall has been asking questions in the village! If they discover that I wrote to Sir Charles on the very day he died—'

I caught her wrists and forced her gently back into her chair. I looked deep into her hazel eyes with an expression of tender, sorrowful reproach.

'Laura, my dearest,' I murmured, stroking her trembling cheek. 'Have you so little faith in my love? Do you not understand that my silence is your only shield?'

'My shield?' she stammered.

'Consider your position!' I said, my voice hardening to the coldness of steel. 'You wrote an urgent letter pleading for a secret midnight interview at an isolated garden gate. That very night, Sir Charles died of terror. What will an English jury say if that letter comes to light? They will say you were an accomplice in a scheme of extortion! They will say you lured an old man to his doom! The lawyers will tear your character to shreds, and you will stand in the dock as a felon!'

She shrieked, burying her face in her hands, shivering in convulsive terror.

'I will never speak!' she gasped through her tears. 'I swear it by the holy cross, Jack! I burned his reply, and I will deny that I ever wrote a line!'

'Good girl,' I whispered, pressing a kiss upon her brow. 'Keep silent for seven more days. The money for your divorce is almost in my hands. In one week, Laura, we shall leave Devonshire forever and begin our new life across the sea.'

I left her comforted and terrified—the ideal psychological cage. But as I rode back to the moor, I knew that time was running out. Watson was sniffing at my heels. The climax could not be delayed!""",
        "content_cn": """十月二十二日清晨，我单骑快马赶往库姆马西集镇。村妇们的窃窃私语已然传到了我的耳中：那位多管闲事的华生医生，近来正在四处打听查尔斯老爵士生前暗中资助的慈善对象！

倘若华生当真找上了劳拉·里昂斯，我那盘耗尽心血的大棋将面临万劫不复的灭顶之灾！

我不宣而入径直推开了她的起居室房门。劳拉正神色惶恐地坐在雷明顿打字机前发呆。当看到我的身影时，她如溺水者抓住浮木般猛地扑上前死死搂住我的脖颈，展现出那种令我心底作呕的黏腻依附。

‘杰克！’她泪如雨下地抽泣道，‘我快要被吓疯了！庄园来的那个军医正在镇上到处打听老爵士的往事！倘若让他们知道在爵士暴毙当天是我写信约他在侧门相见——’

我稳稳扣住她的手腕，温柔而坚定地将她按回扶手椅中。我居高临下凝视着她那双充满泪水的栗色眼眸，换上了一副充满深情却又痛心疾首的忧郁神情。

‘劳拉，我唯一的挚爱，’我抚摩着她冰凉的面颊低语道，‘难道你对我坚贞的誓言就如此缺乏信任吗？难道你当真不明白，我对外界保持绝对缄默，才是在这场风暴中保全你名节与性命的唯一坚盾？！’

‘保全我？’她战战兢兢地颤声问道。

‘动动你的脑子，看清你当下的处境！’我的嗓音骤然降温，变得如冰冷的刀锋般森寒刺骨，‘你在案发当天亲笔写下一封十万火急的密信，哀求一位家财万贯的贵族老人在深夜十点独自在偏僻荒凉的花岗岩侧门与你私会！而就在当晚，老爵士便横死侧门！倘若这封信的内容公之于众，英国法庭的法官与陪审团会怎么想？！他们会指控你伙同奸夫敲诈勒索！他们会认定是你充当诱饵将一个体面的老绅士送入了死地！全伦敦的讼棍会把你撕得体无完肤，最终把你推上绞刑架！’

她发出了一声撕心裂肺的凄厉尖叫，双手死死捂住面孔，在极致的恐慌中如触电般剧烈抽搐。

‘我发誓我一个字都不会说的！’她在泪流满面中近乎发狂般起誓道，‘看在上帝的十字架份上，杰克！我已经烧毁了所有信件，哪怕天塌下来，我也绝不承认自己曾给他写过半个字！’

‘这才是我的乖女孩，’我伏身在她前额印上一记冰冷的吻，‘再死死咬牙坚持七天。为你赎买自由身的巨额离婚费已然尽在我的掌控之中。一周之后，劳拉，我们将永远离开德文郡，在汪洋大海的彼岸开启我们辉煌的新生。’

我将这个惊弓之鸟彻底锁死在被恐慌与虚幻美梦编织的心理牢笼之中。然而当我策马折返荒原时，我深知死神留给我的时间已然所剩无几。华生的猎犬鼻子已然嗅到了我的脚后跟，终极决战的屠刀必须以最快速度悍然挥下！"""
    }
])
# Stapleton Chapter 11 & 12
STAPLETON_NODES.extend([
    # Chapter 11 Part 1
    {
        "id": "stapleton_ch11_part1_spy_on_tor",
        "ch_idx": 10, "part": 1,
        "title_en": "Chapter 11: The Man on the Tor (Part I: The Unknown Watcher on Black Tor)",
        "title_cn": "第十一章 岩岗上的人（上：黑色岩岗石屋的神秘暗哨）",
        "pov": "stapleton", "type": "anchor", "anchor": "anchor_spy_stapleton",
        "clues_en": [
            "Stapleton spots young boy Cartwright delivering food parcels to Neolithic huts on Black Tor",
            "Confirms a secret operative is camping upon the moor observing his movements",
        ],
        "clues_cn": [
            "斯台普吞暗中抓到小厮卡特赖特定期向黑色岩岗史前石屋运送面包与烟草的规律",
            "确凿证实有一位隐秘统帅正深藏荒原石屋严密监控全局，决意先下手为强除掉亨利",
        ],
        "choices_en": [
            {"id": "s_ch11_p1_c1", "text": "Hasten to the mire island and lay Sir Henry's stolen black boot before the hound.", "target": "stapleton_ch11_part2_setting_scent"},
            {"id": "s_ch11_p1_c2", "text": "[Switch POV to Dr. Watson] View Watson cornering Laura Lyons in Coombe Tracey.", "target": "ch11_part1_lyons", "pov_switch": "watson"},
        ],
        "choices_cn": [
            {"id": "s_ch11_p1_c1", "text": "火速奔赴泥潭孤岛，将从伦敦偷来的旧黑皮靴浸透气味喂给饥渴暴怒的恶犬。", "target": "stapleton_ch11_part2_setting_scent"},
            {"id": "s_ch11_p1_c2", "text": "【视角切换：约翰·H·华生】见证华生在库姆马西打字行以正义辞令攻破劳拉防线。", "target": "ch11_part1_lyons", "pov_switch": "watson"},
        ],
        "content_en": """On the afternoon of October 23rd, I climbed to the crest of High Tor with my powerful field glass. My target was the ancient British settlement upon Black Tor.

For three days, the mysterious silhouette against the moon had haunted my nightmares. If that watcher was an agent of Scotland Yard—or worse, if it was Sherlock Holmes himself—my time was measured in hours!

I focused my lens upon the circular stone huts. For two hours, nothing moved save the wind in the gorse. Then, picking his way up the sheep-track from the direction of Coombe Tracey, came a boy!

A sharp London lad of fourteen, carrying a wicker basket covered with a coarse cloth!

I followed the urchin with my glass. He scrambled up the rocks, looked warily about him, and ducked straight into the low entrance of the largest stone hut. Five minutes later, he emerged with an empty basket and sprinted back toward the road.

The proof was incontrovertible!

A man was living in that hut! A man supplied with provisions from Coombe Tracey! A man who lived like a hunted fox, observing everything, keeping his existence a secret from the Hall and from the village!

Who else in England possessed the audacity, the iron endurance, and the dramatic eccentricity to camp in a prehistoric stone hut in the freezing autumn winds of Dartmoor?

Sherlock Holmes!

The blood drummed against my temples like a war-drum. The master detective had outmaneuvered me! While I believed he was idling in London, he had been perched upon the tor above my head, watching my every stroll, tracking my every movement!

There was no time for subtlety. No time for intricate legal traps. If Holmes completed his inquiries, he would tie me to the hound, to Laura Lyons, and to the stolen boots.

I must strike Sir Henry down tonight! Once the heir was dead, the estate would pass to me as the next of kin. With seven hundred and forty thousand pounds, I could bribe, flee, or defy the world!

I shut my glass, scrambled down the crags, and made straight for the mire island!""",
        "content_cn": """十月二十三日下午，我手提强力单筒远望镜，如猎豹般潜上了海岩岗（High Tor）的最高峰峦。我的观察目标，直指黑色岩岗那片三千年前不列颠土著留下的史前石屋群。

连续整整三天，那个在月夜顶峰傲立的神秘黑影如跗骨之蛆般折磨着我的神经。倘若那个暗哨当真是苏格兰场的密探——甚至更糟，倘若正是歇洛克·福尔摩斯本人——我留给自己的生路将按小时计算！

我将镜头牢牢对准那些粗糙的圆形花岗岩石壁。在漫长的两个小时里，除了朔风摇曳石楠花外没有任何生机。然而就在午后三点，一个敏捷瘦小的身影突然踩着从库姆马西方向延伸而来的羊肠小径，悄然出现在山脊拐角处！

一个十四五岁的精明伦敦报童打扮的小厮，手里提着一只蒙着粗麻布的野餐竹篮！

我的镜头死死锁定了这个毛头小子。只见他警惕地四下张望，随后身形一猫，径直钻入了最大也是保存最完好的那座圆形石屋之中！仅仅五分钟后，小厮两手空空提着空竹篮疾步钻出石屋，一溜烟奔下了山道。

铁证如山！

那座石屋里确确实实活生生住着一个凡人！一个靠库姆马西集镇提供吃食的神秘密使！一个如老狐狸般昼伏夜出、对庄园和警局彻底隐匿全部踪迹的最高统帅！

放眼全英伦三岛，究竟何人拥有这等惊天动地的胆识、钢铁铸造的耐力以及近乎走火入魔的戏剧化狂热，竟敢在达特穆尔刺骨的冰霜寒夜里餐风露宿在三千年前的史前石窟之中？！

歇洛克·福尔摩斯！

太阳穴两侧的青筋狂暴突跳，血液如战鼓般擂击着我的耳膜。这位名满天下的神探以彼之道还施彼身，狠狠将了我一军！当我自以为得计他在伦敦虚耗光阴时，他竟然早已如雄鹰般盘旋在我头顶的黑色绝壁之上，冷眼俯瞰着我的一举一动！

没有时间再玩弄文绉绉的借刀杀人了！更没有时间再去周旋什么繁复的法理借口！一旦让福尔摩斯彻底合拢证据链，他必将把恶犬、劳拉·里昂斯以及伦敦失窃的旧靴彻底焊死在我的脖颈上！

必须在今晚将亨利爵士格杀勿论！只要这位唯一的拦路虎横尸荒野，按继承法典，我作为仅存的至亲血脉将合法加冕全部七十四万镑巨款！手握如此滔天富贵，我足以买通一切官僚，或是远走高飞逍遥法外！

我啪的一声合上望远镜，飞身跃下峭壁，直扑大格林盆泥潭深处的魔窟孤岛！"""
    },

    # Chapter 11 Part 2
    {
        "id": "stapleton_ch11_part2_setting_scent",
        "ch_idx": 10, "part": 2,
        "title_en": "Chapter 11: The Man on the Tor (Part II: Laying the Fatal Scent)",
        "title_cn": "第十一章 岩岗上的人（下：给猎犬闻取旧靴气味）",
        "pov": "stapleton", "type": "branch", "anchor": None,
        "clues_en": [
            "Stapleton starves the beast and rubs Sir Henry's worn black boot across its jaws",
            "Prepares to release the hound into the darkness to slaughter the baronet",
        ],
        "clues_cn": [
            "故意剥夺恶兽两日饮食激发极致狂暴，用从伦敦盗来的亨利旧黑皮靴死死擦拭恶犬獠牙与吻部",
            "在狂风大作的黄昏全面备齐磷光油膏，决意在黑夜降临时放出巨兽清洗荒原",
        ],
        "choices_en": [
            {"id": "s_ch11_p2_c1", "text": "Unleash the hound into the foggy night and listen for the slaughter upon the crags.", "target": "stapleton_ch12_part1_screams_on_crags"},
            {"id": "s_ch11_p2_c2", "text": "[Switch POV to Sherlock Holmes] View Holmes revealing Stapleton's identity to Watson.", "target": "holmes_ch11_part2_stone_hut", "pov_switch": "holmes"},
        ],
        "choices_cn": [
            {"id": "s_ch11_p2_c1", "text": "趁着浓雾涌起解开铁链放出恶魔巨兽，在荒原冷夜中侧耳倾听绝命哀嚎。", "target": "stapleton_ch12_part1_screams_on_crags"},
            {"id": "s_ch11_p2_c2", "text": "【视角切换：歇洛克·福尔摩斯】切换至石屋，见证名侦探撕破斯台普吞假面具的经典一幕。", "target": "holmes_ch11_part2_stone_hut", "pov_switch": "holmes"},
        ],
        "content_en": """I entered the tin shed upon the mire island, my heart hardened to granite.

The hound had not tasted meat for two days. When it saw me, it lunged against its chain with a ferocity that shook the iron staples in the wall. Foam dripped from its jaws; its red eyes were glazed with murderous hunger.

I drew Sir Henry's stolen black boot from my oilskin pouch.

I approached the beast, speaking in that low, harsh hiss that drove it to madness. I rubbed the muddy leather across its quivering nostrils. I thrust the worn heel between its jaws, forcing it to gnaw the leather, to inhale the sweat, the skin, the living essence of Henry Baskerville!

The creature let out a low, choking whine of recognition. Its tail lashed like an iron rod. It knew its quarry! It knew the scent that it was born to tear from the bone!

I took up my pot of phosphorus paste. With swift, merciless strokes, I painted the glowing venom over its eyes, down its muzzle, and along the ridges of its bristling spine.

Outside, twilight was fading into an ocean of clinging, gray moorland fog. The wind shrieked through the rifts in the granite tor.

I snapped the release on the brass collar.

'Kill!' I snarled, pointing toward the Hall. 'Hunt him down and tear his throat!'

The monster sprang through the open door like a bolt from a crossbow! A streak of roaring green fire across the black slime, vanishing into the fog toward the scent that called it!

I stood upon the threshold, shivering with triumphant anticipation, waiting for the screams of death to roll back across the waste!""",
        "content_cn": """我一步迈入泥潭孤岛的旧锡矿工棚，胸膛中的心脏已然冷硬如玄武岩石。

为了彻底激发最原始狂暴的杀戮兽性，我已经整整两天未曾给这头恶兽喂食半星生肉。当它在黑暗中见到我手中提着的皮囊时，发头发狂般猛扑向前，庞大的身躯狠狠扯动着精钢铁链，震得镶嵌在花岗岩石壁里的铁环沙沙作响！黏稠恶臭的涎水顺着它白森森的獠牙不断滴落，两只充血的血瞳在饥饿与绝望的驱使下已近乎癫狂！

我从油布皮囊里掏出了那只从伦敦诺森伯兰旅馆顺手牵羊而来的亨利爵士旧黑皮靴。

我缓缓逼近暴躁的巨兽，嘴唇深处发出那种足以将其逼入杀戮狂态的尖锐嘶鸣。我用那只沾满干泥的旧鞋帮在它剧烈耸动的湿漉漉鼻翼上狠狠来回摩擦！我甚至粗暴地将磨损的鞋跟直接塞入它的血盆大口之中，逼迫它狠狠撕咬着牛皮，将亨利·巴斯克维尔肉体毛孔深处散发出的酸性汗液与热血气味，深深吸入它的五脏六腑！

恶兽的喉咙深处猛地爆发出一阵被遏制不住的狂喜呜咽！它的尾巴犹如铁棒般狂暴地抽打着地面！它记住了这个气味！它认准了这个它受训毕生、誓要从骨髓深处撕咬嚼碎的唯一死敌！

我抓起特制的白磷冷光油膏。以最娴熟冷酷的手法，迅速涂满了它的双眼眼眶、獠牙边缘以及背脊上根根倒竖的硬直鬃毛。

在工棚外，深沉的暮色已然被整片翻滚涌动的阴森灰雾所彻底吞噬。凄厉的夜风在花岗岩绝壁间发出鬼哭狼嚎般的尖啸。

我啪的一声按开了黄铜项圈上的弹簧锁扣！

‘杀！’我指着巴斯克维尔庄园的方向厉声咆哮，‘循着气味，撕碎他的喉咙！’

那头恶魔巨兽如同一支从重弩中射出的夺命铁箭，轰然破门而出！一团在浓墨死沼上狂暴掠过的幽绿烈焰，咆哮着瞬间撕开重重迷雾，沿着旧靴指引的致命气味，狂暴扑向黑夜荒原！

我傲立在工棚门槛上，在凛冽的夜风中狂热战栗，静候着撕心裂肺的绝望惨嚎滚滚传遍整片死沼！"""
    },

    # Chapter 12 Part 1
    {
        "id": "stapleton_ch12_part1_screams_on_crags",
        "ch_idx": 11, "part": 1,
        "title_en": "Chapter 12: Death on the Moor (Part I: The Hound Unleashed)",
        "title_cn": "第十二章 沼地的惨剧（上：巨兽出柙与夜空绝叫）",
        "pov": "stapleton", "type": "anchor", "anchor": "anchor_screams_stapleton",
        "clues_en": [
            "Stapleton tracks the hound's progress by its muffled bays echoing off the crags",
            "A scream of mortal terror and a heavy falling crash ring out near Black Tor",
        ],
        "clues_cn": [
            "斯台普吞循着恶犬在花岗岩裂谷间激荡回响的恐怖长嚎，紧随其后见证收割成果",
            "黑色岩岗方向骤然炸响一声撕心裂肺的垂死人类惨呼与重重坠崖摔碎的沉闷巨响",
        ],
        "choices_en": [
            {"id": "s_ch12_p1_c1", "text": "Hasten with your lantern to inspect the broken corpse at the foot of the cliff.", "target": "stapleton_ch12_part2_confronting_holmes"},
            {"id": "s_ch12_p1_c2", "text": "[Switch POV to Sherlock Holmes] View Holmes discovering the dead convict in Sir Henry's suit.", "target": "holmes_ch12_part2_selden_death", "pov_switch": "holmes"},
        ],
        "choices_cn": [
            {"id": "s_ch12_p1_c1", "text": "手提马灯快步穿过乱石滩赶往绝壁脚下，亲手检验亨利爵士脑浆迸裂的尸骸成果。", "target": "stapleton_ch12_part2_confronting_holmes"},
            {"id": "s_ch12_p1_c2", "text": "【视角切换：歇洛克·福尔摩斯】切换至悬崖底部，目睹福尔摩斯如何擦亮火柴识破死者乃逃犯替身。", "target": "holmes_ch12_part2_selden_death", "pov_switch": "holmes"},
        ],
        "content_en": """I followed the beast at a distance of three hundred yards, moving lightly across the heather with my unlit lantern.

The fog had rolled into the hollows, leaving the granite crests floating like dark islands upon a milky sea. The silence was absolute.

Then, from the direction of Black Tor, the baying began!

A deep, rolling roar of pure malice that shook the granite rocks! The hound was in full cry! It had found the trail! It was running at speed across the high plateau!

I quickened my pace to a run, my boots flying over the peat.

Suddenly, high upon the crags above me, a human voice shrieked in mortal agony!

'Help! For God's sake, help!'

The scream was choked off by a frenzied snarling of jaws and the heavy thud of bounding paws. A wild scramble of feet echoed across the shale—the desperate, frantic flight of a hunted man sprinting along the edge of the abyss!

A second scream tore through the mist, rising to a piercing, despairing shriek:

'No! No! Ahhhh—'

A sickening, splintering crash echoed from the base of the forty-foot precipice! The dull, heavy thud of bone and flesh smashing against solid granite! Then—total, unbroken silence.

My heart surged with intoxicating, triumphant ecstasy!

He had fallen! The hound had driven Sir Henry over the edge of the cliff! The young baronet lay dashed to pieces upon the stones!

The title was extinct! The gold was mine!

I struck a match, lit my yellow lantern, and hastened with eager, bounding strides through the dark boulders toward the foot of the crag to gaze upon my conquest!""",
        "content_cn": """我手提熄灭的马灯，在恶兽后方三百码远的距离如鬼魅般在石楠苔原上全速跟进。

翻滚的浓雾已然填满了低洼的山谷，唯有那些刀削般的黑色花岗岩峰峦如漆黑的孤岛般漂浮在惨白粘稠的乳海之上。整片天地死寂无声。

突然之间，从黑色岩岗正前方的山脊方向，猛然爆发出了惊天动地的狂暴狂吠！

那是一阵浑厚沉重、纯粹由嗜血仇恨淬炼而成的绝命咆哮！恶犬已然彻底锁定了目标！它在以狂暴至极的时速在高岩绝壁上疯狂奔驰扑杀！

我立刻拔腿狂奔，皮靴在碎石与湿泥炭上飞掠而过。

电光石火之间，在高耸入云的花岗岩峭壁之巅，一个人类的嗓音在极度的绝望中爆发出了撕心裂肺的凄厉呼救！

‘救命！看在上帝的份上，救救我啊——！’

呼救声在一瞬间被一阵狂暴凶残的獠牙撕咬声与巨爪践踏声所打断！碎石在悬崖边沿疯狂倾泻坍塌——那是一个亡命徒在悬崖绝壁边缘被死神紧逼时的绝望奔逃！

紧接着，第二声凄厉至极的破胆尖叫撕裂了茫茫雾海：

‘不！不要啊！啊啊啊啊——！’

下一秒，在四十英尺高的垂直悬崖底部，骤然回荡起一声令人毛骨悚然、骨骼寸寸碎裂的沉闷撞击巨响！那是肉体与头颅狠狠砸在坚硬花岗岩上时的钝响！随后，天地重归永恒的冰冷死寂。

一股近乎令人窒息的狂热狂喜瞬间从我胸腔中喷涌而出！

他坠崖了！我的恶犬终于硬生生将亨利爵士逼下了万丈深渊！那个粗鄙的加拿大农夫，此刻已然在悬崖底部撞得粉身碎骨、脑浆涂地！

巴斯克维尔的直系血脉彻底断绝！七十四万镑的黄金属于我了！

我擦亮火柴点燃了手中的昏黄马灯，迈开轻快狂喜的大步，在漆黑错落的花岗岩乱石滩上飞速前行，急不可耐地要亲眼鉴赏我亲手缔造的尸骸杰作！"""
    },

    # Chapter 12 Part 2
    {
        "id": "stapleton_ch12_part2_confronting_holmes",
        "ch_idx": 11, "part": 2,
        "title_en": "Chapter 12: Death on the Moor (Part II: Face to Face with Sherlock Holmes)",
        "title_cn": "第十二章 沼地的惨剧（下：错杀逃犯与遭遇福尔摩斯）",
        "pov": "stapleton", "type": "branch", "anchor": None,
        "clues_en": [
            "Corpse is not Sir Henry, but Selden the convict wearing Sir Henry's old clothes",
            "Sherlock Holmes is standing by the body in the flesh alongside Dr. Watson",
            "Stapleton is forced to play the innocent neighbor while his life hangs by a thread",
        ],
        "clues_cn": [
            "惨死悬崖脚下的竟非爵士，而是身穿亨利淘汰旧西装的诺丁山越狱逃犯塞尔登",
            "歇洛克·福尔摩斯大侦探本尊竟全副武装携华生屹立在尸体身旁，目光森冷如刀",
            "斯台普吞在濒死的极度恐慌中强撑笑颜扮演纯良邻居，深知已陷入绝境，唯有最后一击方能翻盘",
        ],
        "choices_en": [
            {"id": "s_ch12_p2_c1", "text": "Retreat to Merripit House to invite Sir Henry to his final, fatal dinner.", "target": "stapleton_ch13_fatal_dinner"},
            {"id": "s_ch12_p2_c2", "text": "[Switch POV to Sherlock Holmes] View Holmes revealing the face of Hugo Baskerville.", "target": "holmes_ch13_portrait", "pov_switch": "holmes"},
        ],
        "choices_cn": [
            {"id": "s_ch12_p2_c1", "text": "强压内心的万丈惊恐遁回梅利琵宅邸，下定决心布下最后的夺命鸿门宴做殊死一搏。", "target": "stapleton_ch13_fatal_dinner"},
            {"id": "s_ch12_p2_c2", "text": "【视角切换：歇洛克·福尔摩斯】切换至庄园画廊，看神探遮挡雨果画像揭开两百年魔鬼血脉。", "target": "holmes_ch13_portrait", "pov_switch": "holmes"},
        ],
        "content_en": """I swung my lantern around the base of the crag, stepping eagerly toward the crumpled heap upon the stones.

Two men were already kneeling beside the body.

I raised the lantern. The yellow beam struck the face of the taller man, and my breath stopped dead in my lungs!

Sherlock Holmes!

He was standing upright, his gray eyes piercing the gloom like cold daggers! Beside him stood Watson, his pistol drawn!

My mind convulsed in sheer, dizzying terror! But worse—infinitely worse—was the sight upon the ground!

The dead man was clad in Sir Henry's ruddy tweed suit. But the face turned up to the lantern was not the strong, clean-shaven face of the baronet! It was a hideous, ape-like countenance, framed in a thick, matted black beard—the broken corpse of Selden, the Notting Hill convict!

Selden! The dog had hunted Sir Henry's clothes, not Sir Henry himself! Barrymore had given the Canadian garments to his starving brother-in-law, and the beast had slaughtered the wrong man!

My entire soul screamed in frustrated agony. Yet I had to stand there, thirty inches from Sherlock Holmes, and smile!

'Mr. Holmes!' I stammered, my throat parched as sand. 'Is it possible? What an unexpected honour! And... who is this unfortunate man?'

Holmes looked at me with cool, impenetrable amusement. 'An escaped convict, Mr. Stapleton. He seems to have fallen from the crags and broken his neck. A tragic accident. My friend Watson and I return to London tomorrow; our little holiday is at an end.'

He was leaving! Holmes was returning to London!

He did not know! He thought it was a common accident! The fool had missed the connection!

I bowed, uttered a few hypocritical condolences, and walked back into the fog toward Merripit House. My knees were shaking, but my brain was afire with renewed, desperate resolve.

One last throw of the dice remained! Tomorrow night, Sir Henry was dining with me at Merripit House. If Holmes was in London, the baronet would walk home alone across the moor! And this time, there would be no mistake!""",
        "content_cn": """我提着马灯转过悬崖底部的巨石转角，迫不及待地大步迈向横卧在碎石中的那摊扭曲血肉。

然而在尸骸旁，竟然早已跪伏着两条矫健的人影。

我高高举起马灯。昏黄的光柱在照亮那位身材瘦高绅士面庞的一刹那，我肺腑里的呼吸在一秒钟内彻底停滞！

歇洛克·福尔摩斯！

他静静直立起身躯，那对鹰隼般的灰色寒眸在黑暗中宛如两柄剥皮抽骨的手术刀，正冷冷地凝视着我！身旁端立着面带杀气的华生，手中的左轮手枪黑洞洞的枪口直指前方！

极致的眩晕与恐慌瞬间撕裂了我的神智！然而更可怕、比噩梦还要恐怖万倍的景象，却横亘在冰冷的花岗岩地面之上！

死者身上的确紧紧包裹着亨利爵士那套红褐色的粗花呢猎装。然而在马灯光芒的照耀下，那张沾满鲜血脑浆的死人脸，绝非年轻男爵那张轮廓分明的面孔！那是一张狰狞丑陋如野猿、满脸虬结杂乱黑须的凶徒面孔——臭名昭著的诺丁山越狱杀人犯塞尔登！

塞尔登！我的恶犬循着旧靴的气味，追踪的仅仅是这套衣服！是管家白利墨将爵士淘汰的行头施舍给了逃亡的内弟，而饥渴嗜血的恶兽，竟然把这个倒霉的替死鬼硬生生逼下了悬崖！

我内心的每一个细胞都在狂怒与挫败中泣血悲鸣！然而此时此刻，面对近在咫尺的歇洛克·福尔摩斯，我必须强行从脸上挤出最无辜、最优雅的笑容！

‘福……福尔摩斯先生！’我的喉咙干渴得如同荒原的沙砾，结结巴巴地强颜欢笑道，‘真没想到竟能在此地得见真颜！只是……这位不幸罹难的先生究竟是哪位？’

福尔摩斯面无表情地吐出一口烟圈，眼神中带着一种高深莫测的冷酷淡漠：‘一个在荒原上逃亡的重犯，斯台普吞先生。似乎是他失足坠崖跌断了脖子。纯属意外。我和华生明天一早便要搭乘早班火车返回伦敦，我们的假期到此结束了。’

他要回伦敦！福尔摩斯竟然要撤退回京！

他根本不知道内情！他以为这仅仅是一桩普通的逃犯失足意外！这位大神探到底还是漏算了最核心的玄机！

我恭敬地欠身行礼，假惺惺地挤出几句叹惋的辞令，随即转身踩着虚浮的步子遁回迷雾深处的梅利琵宅邸。我的双膝在恐惧中剧烈颤抖，然而我的大脑却在绝境逢生中被疯狂的嗜血杀念重新引燃！

老天爷还留给了我最后一次逆天改命的绝杀契机！明晚，亨利爵士已然应允孤身前来梅利琵宅邸赴宴！只要福尔摩斯一上火车，年轻男爵在深夜十点便必须孤身一人步行横穿达特穆尔！而这一次，我绝不会再犯任何错误！"""
    }
])
# Stapleton Chapter 13 & 14
STAPLETON_NODES.extend([
    # Chapter 13
    {
        "id": "stapleton_ch13_fatal_dinner",
        "ch_idx": 12, "part": 0,
        "title_en": "Chapter 13: Fixing the Nets (The Last Supper at Merripit House)",
        "title_cn": "第十三章 设网（梅利琵宅邸的最后鸿门宴）",
        "pov": "stapleton", "type": "anchor", "anchor": "anchor_dinner_stapleton",
        "clues_en": [
            "Sir Henry arrives alone for dinner at Merripit House, believing Holmes returned to London",
            "Beryl is brutally tied and gagged upstairs in the locked bedroom to ensure silence",
            "Stapleton prepares the phosphorus paste and slips out into the dense rolling fog",
        ],
        "clues_cn": [
            "亨利爵士单刀赴会孤身抵梅利琵宅邸赴宴，深信福尔摩斯与华生已然乘车返回伦敦",
            "斯台普吞在二楼反锁的卧房中将企图示警的贝丽尔彻底五花大绑在床柱上封嘴囚禁",
            "借口查看天色溜出后院，调配剧毒冷光白磷，静候大雾将唯一的泥潭小道彻底切断",
        ],
        "choices_en": [
            {"id": "s_ch13_c1", "text": "Unleash the phosphorescent hound into the rolling fog as Sir Henry walks home.", "target": "stapleton_ch14_part1_release_hound"},
            {"id": "s_ch13_c2", "text": "[Switch POV to Sherlock Holmes] View Holmes, Watson, and Lestrade waiting in the fog ambush.", "target": "holmes_ch14_part1_fog_ambush", "pov_switch": "holmes"},
        ],
        "choices_cn": [
            {"id": "s_ch13_c1", "text": "在深夜十点亨利爵士踏入夜色时，解开暗室铁链放出通体燃烧地狱磷火的嗜血巨兽。", "target": "stapleton_ch14_part1_release_hound"},
            {"id": "s_ch13_c2", "text": "【视角切换：歇洛克·福尔摩斯】切换至巨石埋伏圈，见证神探三人组在滚滚白雾中拔枪以待。", "target": "holmes_ch14_part1_fog_ambush", "pov_switch": "holmes"},
        ],
        "content_en": """The evening of October 24th was the culmination of six months of meticulous preparation.

In the afternoon, Beryl had fallen upon her knees before me once more, clawing at my hands, weeping that she would throw herself into the bog if I harmed the Canadian boy.

I did not waste words. I struck her down, dragged her up the narrow staircase to the rear bedroom, and tied her wrists and ankles to the brass uprights of the bed with heavy sash cords. I wound a silk scarf tightly across her mouth until she could only moan through her nostrils, locked the door, and pocketed the heavy iron key.

At seven o'clock, Sir Henry Baskerville arrived alone.

He was in high spirits, cheerful and robust. He announced that Holmes and Watson had indeed boarded the morning express for London, leaving him to make his farewells to his neighbors.

'A pity Mr. Holmes could not join us,' I remarked with polished regret, pouring him a generous goblet of old port. 'A remarkable intellect, though perhaps a trifle theatrical for country tastes.'

Dinner went with deceptive brilliance. I was the charming host, discussing agriculture, cattle-breeding, and Canadian timber. Sir Henry drank freely, his eyes straying constantly toward the door, visibly saddened by Beryl's 'sudden, severe migraine.'

At twenty minutes to ten, I excused myself, stepped into the scullery, and peered out into the night.

Nature itself was fighting upon my side!

From the Great Grimpen Mire, a dense, suffocating white fog was rolling inland across the heather like a rising tide! In fifteen minutes, it would swallow the rocks, the paths, and the gates! A man wandering upon the moor in that blinding white vapour would be helpless as a newborn babe!

I hurried to the outhouse where I had concealed the hound. I smeared the cold, oily phosphorus across its jaws, its eyes, and its back until it glowed like an infernal forge.

Ten o'clock chimed from my grandfather clock. In the parlor, Sir Henry was rising to take his leave! The hour of retribution had arrived!""",
        "content_cn": """十月二十四日的这个良夜，是我整整半年呕心沥血布下这盘惊世棋局的最高潮！

午后时分，贝丽尔再次如疯妇般跪倒在地板上死死抱住我的膝盖，指甲抠破了我的皮鞋，歇斯底里地发誓若我敢伤害那位加拿大堂弟，她便一头撞死在泥潭巨石上。

我再也没有跟她浪费半句唇舌。我干脆利落地一拳将她击倒在地，粗暴地将她拖上狭窄的木质楼梯塞入后院最偏僻的次卧。我用厚重的窗帘粗绳将她的手腕与脚踝死死反绑在冰冷的黄铜床柱之上，用一条厚丝巾死死勒紧了她的嘴唇，直到她只能从鼻腔中发出绝望凄厉的悲咽。我反锁了房门，将那把沉甸甸的铁钥匙塞入怀中内袋。

晚间七点整，亨利·巴斯克维尔爵士单刀赴会、如约而至。

他显得兴致极高，红光满面，充满着年轻人的勃勃生机。他亲自向我证实，福尔摩斯与华生确实已搭乘清晨的西行列车返回了伦敦，留他一人在庄园向教区邻里从容告别。

‘福尔摩斯先生未能赏光亲临寒舍共进晚餐，当真是万分遗憾，’我脸上挂着体面而得体的惋惜微笑，为他斟满了一大杯醇厚芬芳的陈年波尔多红酒，‘那真是一位头脑非凡的大人物，只是行事风格未免过于戏剧化了些。’

宴席在极具欺骗性的欢声笑语中顺利推展。我扮演着一位博学风趣的庄园主人，从农耕畜牧一直高谈阔论到加拿大的原始森林采伐。亨利爵士一杯接一杯地畅饮着美酒，然而他的目光却总是不自觉地飘向空荡荡的侧门，显然为贝丽尔因‘突发严重偏头痛’无法作陪而深感怅惘。

九点四十分，我借故离席跨入后厨，推开后窗凝视黑夜。

大自然母亲在这一刻竟然全心全意地站在了我的阵营！

从大格林盆泥潭深处，一堵厚重粘稠、遮天蔽日的雪白大雾正犹如汹涌的海啸般顺着石楠苔原向内陆狂暴席卷！不出十五分钟，整片荒原的小径、岔路与指示石块将被彻底吞没！任何凡人在如此浓密如浆的绝命大雾中涉足荒原，都将脆弱盲目得犹如一个刚出生的婴儿！

我飞步穿过后院隐蔽的储藏石棚。我解开恶兽的铁链，将冰冷黏稠的特制白磷油膏飞速涂满了它的双眼、獠牙与背脊，直到整头恶兽在黑暗中通体燃烧起地狱幽火！

客厅里的老式自鸣钟当啷当啷敲响了十点的丧钟。在走廊尽头，亨利爵士已然穿好了厚大衣准备推门告辞！

巴斯克维尔家族的灭顶之刻，终于轰然降临！"""
    },

    # Chapter 14 Part 1
    {
        "id": "stapleton_ch14_part1_release_hound",
        "ch_idx": 13, "part": 1,
        "title_en": "Chapter 14: The Hound of the Baskervilles (Part I: The Fog and the Gunfire)",
        "title_cn": "第十四章 巴斯克维尔的猎犬（上：迷雾施放猎犬与枪声骤响）",
        "pov": "stapleton", "type": "anchor", "anchor": "anchor_climax_stapleton",
        "clues_en": [
            "Stapleton releases the phosphorescent hound into the rolling fog after Sir Henry",
            "A sudden volley of revolver shots tears through the mist, accompanied by the dying shriek of the beast",
        ],
        "clues_cn": [
            "借着滚滚白雾掩护解开项圈，指使燃烧着幽蓝烈焰的食人恶兽扑向亨利爵士后背",
            "浓雾深处突然爆发出密集如爆豆般的左轮手枪齐射火光，伴随着恶犬临死前震碎云霄的凄厉悲鸣",
        ],
        "choices_en": [
            {"id": "s_ch14_p1_c1", "text": "Flee into the swirling fog of the Great Grimpen Mire to escape the law.", "target": "stapleton_ch14_part2_panic_flight"},
            {"id": "s_ch14_p1_c2", "text": "[Switch POV to Sherlock Holmes] View Holmes emptying his revolver into the fire-breathing beast.", "target": "holmes_ch14_part1_fog_ambush", "pov_switch": "holmes"},
        ],
        "choices_cn": [
            {"id": "s_ch14_p1_c1", "text": "深知大势已去，抛下一切仓皇逃入漆黑大雾笼罩的大格林盆泥潭深处。", "target": "stapleton_ch14_part2_panic_flight"},
            {"id": "s_ch14_p1_c2", "text": "【视角切换：歇洛克·福尔摩斯】切换至决战前线，看神探连射五枪粉碎两百年魔咒。", "target": "holmes_ch14_part1_fog_ambush", "pov_switch": "holmes"},
        ],
        "content_en": """I watched from the shadows of the scullery door as Sir Henry stepped down the gravel path into the night. He paused at the garden gate, buttoned his collar against the damp chill, and set off along the stone track that led across the moor.

Within twenty yards, the white fog swallowed him up.

Now!

I darted to the shed door. The hound was snarling in a frenzy of famished madness, snapping at the air, its mouth and eyes blazing with green fire.

I slipped the lead from its collar.

'Go!' I hissed, pointing down the path. 'Tear him to pieces!'

The beast leaped into the fog with a monstrous roar! A flash of emerald fire, tearing across the heather with giant bounds! In three seconds, it had vanished into the white wall of vapour.

I stood upon the gravel, listening with wild, exultant heartbeats for the screams of death.

One second... two seconds... five seconds...

Suddenly, a voice roared through the fog—a voice of brass that struck terror into my very soul:

'Look out! It's coming!'

Sherlock Holmes!

Before my paralyzed brain could comprehend the disaster, the night exploded into flame!

Crack! Crack! Crack! Crack! Crack!

A volley of heavy revolver shots tore through the mist! A shriek of agony—not of a man, but of a beast—rent the heavens! A sound of thrashing bodies, a second sharp report, and then... a dying whimper that ceased in the wet heather.

Silence.

My hound was dead!

Holmes had never left! He had laid an ambush in the rocks! The law was fifty yards from my doorstep, armed, triumphant, and closing the net!

Panic—blind, primal, suffocating terror—shattered my iron nerves! If I was taken, the gallows at Exeter awaited me!

I whirled round, bolted into the house, grabbed my boots, and fled into the swirling fog toward the Great Grimpen Mire!""",
        "content_cn": """我蜷缩在后厨大门的深黑阴影之中，屏息凝视着亨利爵士迈开步子踏上碎石小道。他在院门前停顿了片刻，系紧了大衣的纽扣抵御刺骨寒气，随后大步流星踏上了紧挨大格林盆泥潭边缘的返程小道。

仅仅走出了二十码远，滚滚翻涌的雪白大雾便如怪兽巨口般将他的身形彻底吞噬。

就是现在！

我如离弦之箭般冲入储藏石棚。那头恶犬在极度饥饿的狂怒驱使下早已癫狂嗜血，两排巨齿咬得空气噼啪作响，口吻与眼眶喷涌着骇人的幽绿地狱鬼火！

我一把扯掉了项圈上的保险栓！

‘去！’我指着小道的方向咬牙厉哮，‘把他撕成碎片！’

巨兽发出一声惊天动地的狂暴咆哮，轰然破雾扑出！一道在石楠苔原上凌空飞跃的幽绿闪电，以惊人的狂飙时速瞬间没入了茫茫白雾之墙！

我傲立在庭院碎石上，两手死死按住狂跳的心脏，贪婪地侧耳倾听着即将响彻天际的骨碎肉烂绝命惨叫！

一秒……两秒……五秒……

然而，从大雾深处猛然炸响的一声厉声暴喝，却如九天玄雷般将我的三魂七魄当场震碎！

‘注意隐蔽！它来了！’

歇洛克·福尔摩斯！

还没等我僵死的大脑理清这场灭顶之灾，整片迷雾荒原瞬间化作了一片火海！

砰！砰！砰！砰！砰！

密集如爆豆般的重型军用左轮手枪齐射火光刺破浓雾！一声撕裂苍穹的凄厉嚎叫——绝非人类的惨呼，而是恶兽中弹濒死的绝命长嗥！紧接着是一阵巨体砸落草丛的疯狂翻滚抓挠声，随后是最后一记清脆补枪的枪响，伴随着一声微弱的抽搐悲鸣，彻底绝了生息。

死寂。

我的恶犬被打死了！

福尔摩斯根本未曾离境！他在巨石圈外布下了天罗地网！苏格兰场的神探与荷枪实弹的宪警距离我的家门仅仅只有五十码远！

恐慌——一种原始、盲目、彻底扼死理智的绝灭恐惧瞬间摧毁了我钢铁般的意志！一旦被捕，埃克塞特监狱那冰冷的绞刑架便将套死在我的脖颈之上！

我猛然转身撞入后门，一把抓起防湿长筒靴，一头扎入了翻滚如海的大雾之中，亡命奔向大格林盆泥潭的无底深渊！"""
    },

    # Chapter 14 Part 2
    {
        "id": "stapleton_ch14_part2_panic_flight",
        "ch_idx": 13, "part": 2,
        "title_en": "Chapter 14: The Hound of the Baskervilles (Part II: The Flight into the Abyss)",
        "title_cn": "第十四章 巴斯克维尔的猎犬（下：恶犬毙命与绝命逃遁）",
        "pov": "stapleton", "type": "branch", "anchor": None,
        "clues_en": [
            "Stapleton flees into the Great Grimpen Mire in pitch-black blinding fog",
            "Loses his secret path of sunken stones amidst the churning white morass",
            "Swallowed alive by the foul slime of the Great Grimpen Mire",
        ],
        "clues_cn": [
            "斯台普吞在伸手不见五指的大雾中惊慌失措仓皇踏入大格林盆泥潭",
            "在狂乱狂奔中迷失了沉水暗石的方向，失足踏破浮草坠入万丈泥浆死渊",
            "被大格林盆泥潭那万劫不复的冰冷污泥彻底漫过头顶活活吞噬，化作永恒坟墓",
        ],
        "choices_en": [
            {"id": "s_ch14_p2_c1", "text": "Plunge forever into the bottomless morass of Grimpen Mire (Canonical Ending).", "target": "ch15_mire"},
            {"id": "s_ch14_p2_c2", "text": "Face trial and the gallows at the Old Bailey before the bar of justice.", "target": "ch15_arrest"},
            {"id": "s_ch14_p2_c3", "text": "Witness Holmes deduce the complete anatomy of the crime in Baker Street.", "target": "ch15_holmes"},
            {"id": "s_ch14_p2_c4", "text": "Acknowledge the heroic triumph of Dr. Watson and the breaking of the curse.", "target": "ch15_watson"},
            {"id": "s_ch14_p2_c5", "text": "Witness the complete restoration of Baskerville Hall and the victory of reason.", "target": "ch15_victory"},
            {"id": "s_ch14_p2_c6", "text": "Reflect upon the shattered nerves of Sir Henry and the bitter cost of crime.", "target": "ch15_tragedy"},
        ],
        "choices_cn": [
            {"id": "s_ch14_p2_c1", "text": "在绝望挣扎中彻底沉入大格林盆泥潭无底深渊，魂归死沼（正统宿命终局）。", "target": "ch15_mire"},
            {"id": "s_ch14_p2_c2", "text": "在泥潭边缘遭雷斯垂德生擒活捉，解往老贝利法庭领受绞刑架的正义裁决。", "target": "ch15_arrest"},
            {"id": "s_ch14_p2_c3", "text": "见证福尔摩斯在贝克街暖融融的壁炉旁，彻底解剖斯台普吞全部罪恶解构。", "target": "ch15_holmes"},
            {"id": "s_ch14_p2_c4", "text": "见证忠诚果决的华生医生神勇发枪击毙恶犬，破除百年恶咒的英雄篇章。", "target": "ch15_watson"},
            {"id": "s_ch14_p2_c5", "text": "正义终得昭雪，巴斯克维尔庄园重沐理性晨曦，百年阴霾一扫而空的圆满凯旋。", "target": "ch15_victory"},
            {"id": "s_ch14_p2_c6", "text": "反思亨利爵士罹患重度神经衰弱远渡重洋的惨痛创伤，罪恶虽诛伤痛难泯。", "target": "ch15_tragedy"},
        ],
        "content_en": """I stumbled into the churning white fog of the Great Grimpen Mire, my heart hammering like a dying engine.

Behind me, in the direction of Merripit House, the shouts of men echoed through the vapor. I could hear the sharp, barking orders of Lestrade and the heavy pounding of boots! They had found Beryl! She would tell them everything—she would guide them straight to my island lair!

I must reach the tin shed. I must seize my passport, my gold notes, and the Canadian boots, and escape north toward the Bristol Channel!

The fog was an impenetrable white blanket, so thick that I could not see my own knees. I ran onto the bog path, gasping for breath.

Left... right... three paces across the peat... then the diagonal jump to the submerged granite slab.

My boot struck stone. I leaped again.

Where was the willow wand? I reached out into the blinding white mist, my fingers trembling. The guide-pole was gone! Had a pony knocked it down? Had the rising mire swallowed the marker?

A scream of panic broke from my parched throat. I took a wild step forward.

Under my right foot, the solid earth gave way!

It did not crack—it dissolved! A sickening, jelly-like suction clamped around my ankle and dragged me down!

'No!' I shrieked, clawing frantically at the false green moss.

The moss tore away in my bleeding fingers. My knee sank into the foul, bubbling black slime. I struggled with all the strength of a dying wolf, thrashing, kicking, throwing my body backward!

Every movement only accelerated the suction! The cold, foul mud rose to my thigh—to my waist—to my chest! The sulfurous stench of the primeval abyss choked my nostrils.

Through the drifting fog, across the waste, I heard the faint, distant whistle of the Plymouth express roaring toward London. Civilization! Wealth! Life! All slipping away into the black pit!

'Beryl!' I screamed into the void. 'Help me!'

Only the gurgling bubbles of the mire answered. The cold slime closed over my chin, over my lips, over my staring eyes.

The Great Grimpen Mire held me in its eternal, bottomless embrace.""",
        "content_cn": """我跌跌撞撞地一头撞入了大格林盆泥潭那片翻滚涌动的雪白大雾之中，胸膛中的心脏狂暴撞击得犹如一台濒临爆炸的引擎。

在我身后梅利琵宅邸的方向，男人们愤怒的呐喊声穿透浓雾滚滚袭来。我清晰地听到了雷斯垂德那威严刺耳的搜查命令，以及大头皮鞋践踏地板的沉重撞击声！他们找到贝丽尔了！那个饱受皮鞭折磨的女人必将招供出一切——她会带着军警径直抄了我隐匿在孤岛上的魔窟！

我必须登上孤岛！我必须取回藏在石缝里的假护照、巨额金镑现钞以及那只定罪的加拿大旧皮靴，借着大雾一路向北潜逃至布里斯托尔海峡登船出境！

然而四周的迷雾浓稠得宛如一堵移动的大理石墙壁，伸手不见五指，我甚至连自己的膝盖都看不清。我全凭记忆踏上暗径，胸口剧烈起伏抽搐。

左三步……右两步……横跨三英尺泥炭……随后斜向猛跃踏上那块沉在水下的花岗岩暗石！

我的皮靴重重踏上了石头。我再次飞身一跃。

可是插在泥潭里的柳树标记枝条在哪儿？！我伸出颤抖的双手在白茫茫的死雾中发狂般摸索。标记不见了！是被受惊的野马踩断了？还是上涨的泥浆吞没了标记？！

一声惊骇欲绝的尖叫从我干涸的喉咙深处喷涌而出。在极致的恐慌中，我仓皇向前迈出了一大步！

然而就在我的右脚踏落的一刹那，脚下结实的泥土瞬间崩溃了！

那不是开裂——而是融化！一股令人作呕、犹如巨大冰冷果冻般的万钧吸力死死咬住了我的脚踝，以无可抗拒的蛮力将我向下疯狂拖拽！

‘不——！’我撕心裂肺地尖叫，十指如鹰爪般发疯抓挠着表面伪装成草坪的绿色浮苔！

浮苔在我的血肉模糊的指甲缝中碎裂剥离。我的整条右腿膝盖瞬间陷入了翻滚恶臭的黑色烂泥之中。我拼尽一头濒死恶狼的全部野性疯狂扑腾、蹬踹，拼命将整个后背向后拉扯倾斜！

然而每一次挣扎，都只是在成倍加速那万丈深渊的吞噬速度！冰冷刺骨、腥臭难闻的远古污泥迅速漫过了我的大腿——漫过了我的腰际——漫过了我的胸膛！那股混合着剧毒硫磺与腐殖质的地狱恶臭死死堵塞了我的鼻腔！

穿透重重迷雾，在遥远的天地尽头，我隐约听到了普利茅斯开往伦敦的夜班特快列车那雄浑清脆的汽笛长鸣。那是现代文明！那是泼天的富贵！那是活生生的生命！然而这一切，都在不可逆转地向着万丈黑渊急速坠落！

‘贝丽尔——！’我绝望地对着虚无的雾海仰天凄厉哀嚎，‘救救我啊——！’

回应我的，唯有泥沼深处那咕嘟翻滚的一串串冰冷恶臭的毒气水泡。粘稠冰冷的黑色泥浆无情漫过了我的下巴，漫过了我绝望抽搐的嘴唇，最终彻底吞噬了我那双圆睁暴突的眼球。

大格林盆泥潭，用它那永恒无底的冰冷怀抱，将恶魔永远封锁在了大地的最核心。"""
    }
])
