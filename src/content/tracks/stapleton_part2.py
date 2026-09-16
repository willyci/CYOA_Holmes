"""Jack Stapleton Track - Part 2: Chapters 6 to 10 (8 nodes).
Expanded canonical narrative from the villain's perspective.
"""

STAPLETON_NODES_PART2 = [
    # Chapter 6 Part 1
    {
        "id": "stapleton_ch06_part1_arrival_watch",
        "ch_idx": 5, "part": 1,
        "title_en": "Chapter 6: Baskerville Hall (Part I: The Arrival of the Quarry)",
        "title_cn": "第六章 巴斯克维尔庄园（上：猎物入瓮与荷枪护送）",
        "pov": "stapleton", "type": "anchor", "anchor": "anchor_arrival_moor_stapleton",
        "clues_en": [
            "Sir Henry and Dr. Watson arrive under armed police escort due to Selden’s prison break",
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
        "content_en": """On the afternoon of October 15th, I took up my station upon the high granite crest of Belliver Tor, pressing my brass pocket telescope against the rough lichen of a boulder to steady my hands. The autumn sky was a sullen vault of leaden grey, and a piercing, damp wind blew out of the Atlantic, flattening the brown heather and howling through the granite clefts. 

Far down the Bovey valley, where the white ribbon of the highroad wound through the moorland, a drifting plume of dust announced the approach of the wagonette from Coombe Tracey station.

I adjusted the brass draw-tubes until the vehicle sprang into sharp focus. 

There, perched upon the high rear seat, was young Sir Henry Baskerville. He had discarded his London bowler for a traveling cap and was wrapped to the chin in a heavy, Canadian fur-trimmed ulster. His dark, alert eyes scanned the desolate waste with an expression of youthful wonder and awe, drunk with the romantic grandeur of entering his ancestral kingdom. Beside him sat Dr. John Watson, rigid, vigilant, his square jaw thrust forward, his right hand resting conspicuously inside the flap of his tweed overcoat pocket—where, beyond any shadow of a doubt, his service Webley revolver lay cocked and ready for action. And flanking the horses, trotting upon two sturdy moorland cobs, were two mounted county constables in dark blue tunics, their Lee-Metford carbines resting across their saddlebows, their eyes roving nervously over every peat-hagg and gorse-clump!

A comical escort! What pathetic, childish vanity! As though a lead bullet or a pair of village bobbies could ward off a demonic incarnation of hell-fire and ancient darkness!

Yet the presence of those carbines had a specific, sinister significance which I had already learned from the postman that morning: Selden, the Notting Hill murderer, had burrowed out of the granite fortress at Princetown three nights earlier and was starving among the tors! The authorities had flooded the highroad with armed patrols, and every farmer on the moor was bolting his shutters before sundown.

A delicious complication! What could be more opportune for my designs? If an escaped cutthroat was known to be prowling the wastes with a butcher’s knife, every sudden death, every scream in the night, every mangled corpse discovered among the rocks would instantly and inevitably be laid at the convict’s door! The police would scour the heather for a wild human beast, while my phantom completed its bloody work unmolested!

The wagonette turned through the moss-grown granite piers of Baskerville Hall. The ancient, wrought-iron gates groaned upon their rusty hinges and clanged shut behind them.

The sheep was in the pen! Sir Henry was now cut off from the civilized world by twenty miles of untamed, treacherous wilderness, with only a credulous, blundering army doctor to stand between his throat and my waiting beast!

A predatory thrill, cold and intoxicating, pulsed through my veins. The golden hoard of Sir Charles seemed already glittering beneath my touch. I collapsed my telescope, thrust it into my pocket, and hastened down the rocky slope towards Merripit House to ensure that my domestic prisoner was broken to the harness before the game began!""",
        "content_cn": """十月十五日的午后，我登上了贝利弗岩岗（Belliver Tor）高耸的花岗岩顶峰，将单筒黄铜望远镜死死抵在一块生满地衣的粗糙巨石上以稳住双手。深秋的天空是一幅阴霾低沉的铅灰色穹顶，一股裹挟着大西洋刺骨湿气的冰冷朔风呼啸着掠过荒原，将枯黄的石楠草吹得紧贴地面，在花岗岩裂隙间激荡出阵阵尖厉的呜咽。

在波维谷地的远方，当那条白色的马车干道蜿蜒穿越沼泽时，一缕滚滚升腾的漫天尘烟宣告了从库姆马西火车站疾驰而来的双排敞篷马车。

我缓缓旋转调节着镜筒，马车上的每一张面孔瞬间在镜片中央纤毫毕现。

端坐在后排高位上的，正是那位年轻的继承人亨利·巴斯克维尔爵士。他换下了伦敦的硬顶礼帽，戴着一顶旅行鸭舌帽，身上裹着一件加皮毛领的厚实加拿大式大氅。他那对漆黑而警惕的眼眸满怀惊奇与震撼地打量着四周蛮荒苍凉的苔原，显然正沉醉在入主祖传王国的浪漫与豪情之中。坐在他身侧的正是约翰·H·华生医生，身躯挺拔笔直如雕像，警惕地挺着方下巴，右手沉甸甸地按在大衣翻领口袋的凸起处——毫无疑问，他那把大口径韦伯利军用左轮手枪早已压满子弹、处于随时待发的状态。而在马车两侧，两名身着深蓝制服的德文郡骑警正骑着健壮的荒原马全副戒备地护卫随行，手中的李-梅特福德卡宾枪横架在马鞍桥上，紧张的目光不断扫视着沿途的每一处泥炭沟与金雀花丛！

滑稽可笑的武装护卫！何等幼稚浅薄的虚荣挣扎！这帮蠢货竟然天真地以为，几枚凡间的铅弹或是两个乡村小警察，当真能够挡得住一头诞生于九幽地狱火海与古老魔咒之中的复仇恶兽？！

然而这批荷枪实弹的武装骑警之所以大动干戈，其背后那道令全教区人心惶惶的突发变故，早已在今晨由乡村邮差送到了我的耳中：三天前，残杀多名无辜者的诺丁山屠夫逃犯塞尔登，竟从普林斯敦花岗岩筑就的高墙重牢中凿壁越狱，此刻正潜伏在荒原的乱石滩中茹毛饮血！地方当局在交通要道上布满了武装巡逻队，荒原上的每一个农户在太阳落山前便死死插上了门栓。

这真是一个绝妙至极的混乱棋子！放眼全天下，还有什么比一个游荡在黑夜中、身负数条人命的越狱凶徒更适合充当我的烟幕弹？！倘若世人皆知荒原上游荡着一个穷凶极恶的持刀屠夫，那么在这片土地上发生的任何猝死、任何深夜撕心裂肺的惨叫，乃至任何横尸悬崖的碎骨惨案，都将在第一时间被愚蠢的世人与宪警顺理成章地扣在逃犯头上！全郡的警察会在石楠丛中掘地三尺搜捕一个野兽般的人类，而我的地狱幽灵则能在黑夜中从容收割生命！

敞篷马车辚辚转过了巴斯克维尔庄园那两座生满青苔的古老花岗岩石柱。两扇沉重锈蚀的熟铁雕花大门在他们身后发出刺耳的呻吟，轰然闭合。

羊羔终于正式赶入了屠宰圈！如今亨利爵士已被整整二十英里险象环生的原始死绝之地与文明世界彻底切断，在他那脆弱的咽喉前，仅仅横隔着一个自以为是、极易受骗的糊涂军医！

一股冰冷而令人狂醉的捕食快感瞬间传遍了我的四肢百骸。查尔斯老爵士那七十四万镑的黄金巨矿，已然在我指尖下绽放出触手可及的夺目光彩！我收起望远镜插回口袋，沿着岩石嶙峋的陡坡大步流星奔向梅利琵宅邸，务必在狩猎正式拉开序幕之前，将我的家宅牢笼彻底封死！"""
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
            {"id": "s_ch6_p2_c2", "text": "Prepare the hound’s feeding schedule on the mire island for the coming night.", "target": "stapleton_ch07_part1_naturalist_act"},
        ],
        "choices_cn": [
            {"id": "s_ch6_p2_c1", "text": "手提捕蝶网漫步荒原泥潭小径，主动结识华生医生并当面测试其观察力与警惕心。", "target": "stapleton_ch07_part1_naturalist_act"},
            {"id": "s_ch6_p2_c2", "text": "踏着暗径潜入大格林盆泥潭孤岛，为今晚恶兽的血食配给制定精准时刻表。", "target": "stapleton_ch07_part1_naturalist_act"},
        ],
        "content_en": """I entered Merripit House through the stone-flagged scullery. The cottage was bitter cold, reeking of damp lime-wash and the sharp, peach-blossom odour of potassium cyanide from the killing jars lining my specimen shelves.

In the sitting-room, Beryl stood motionless by the mullioned window, her forehead pressed against the cold glass, staring across the wasteland towards the distant, twin towers of Baskerville Hall. When my boot scraped upon the threshold, she started violently, spinning round like a trapped bird, her exquisite Spanish face drained of all colour.

“He is at the Hall,” I said calmly, stepping inside and locking the oak door behind me with a deliberate, metallic click. I dropped the heavy key into my waistcoat pocket.

She backed away until her shoulders struck the plaster wall, her dark, lustrous eyes wide with terror. “Jack... in the name of the God whose cross you wear, I beseech you! Abandon this horror! Let this boy live! He is young; he has never lifted a finger against you! We have our savings; take me away from this desolate swamp! Take me back to Costa Rica, where we may walk in the sunshine without blood upon our hands!”

I crossed the room in two strides. Before she could raise her arms, my right hand clamped around her slender throat like a steel vise, forcing her down into the high-backed horsehair chair until her breathing came in desperate, suffocating gasps.

“Listen to me, my pious little fool,” I whispered, leaning my face so close that my glasses touched her temple. “In London, you dared to cut my newspapers and send an anonymous warning to Sir Henry. I did not kill you then because your face is the only magnet that can draw the young fool across the moor to his destruction. But hear me now, Beryl, and let every syllable burn into your memory: we are not in London now! There are no police within five miles, no neighbours within two leagues, and the Great Grimpen Mire is thirty yards from our back door!”

Tears of physical agony and despair leaked from her tightly squeezed eyelids.

“If you whisper one syllable to Sir Henry when he visits this house—if by word, look, or gesture you hint that you are my lawful wife and not my maiden sister—I will not merely send your handsome young baronet to his grave. I will drag you across the stepping-stones in the dead of night, bind you to the iron ring in the floor of the smelting shed, and leave you in the dark with the starving beast! Do you understand me, Beryl?”

I loosened my grip slightly. She slid from the horsehair cushions onto the floor, trembling convulsively from head to foot, burying her face against the hem of my trousers, weeping in broken, animal terror.

“I will be silent!” she sobbed, her voice muffled in the cloth. “God forgive me, I will be silent! I will say nothing—nothing!”

“See that you remember it,” I said coldly, stepping over her prostrate body. “Tomorrow morning, Dr. Watson will undoubtedly walk out to survey the moorland topography. I shall take my green gauze net and intercept him near the mire. A garrulous, enthusiastic country naturalist—the very model of an unworldly eccentric! An honest, thick-headed army surgeon will take me into his confidence within ten minutes. And once I have Watson under my thumb, Sir Henry will walk straight into our parlour!”

I unlocked the door, walked into my study, and began laying out the pins and corkboards for tomorrow’s catch. The web was spun; the spider was poised for the feast!""",
        "content_cn": """我穿过铺着冰冷石板的后厨杂物间跨入了梅利琵宅邸。整栋农舍阴冷刺骨，弥漫着潮湿白灰的霉味，以及从标本架上一排排毒瓶中散发出的苦杏仁与氰化钾刺鼻甜香。

在昏暗狭窄的起居室里，贝丽尔正一动不动地伫立在直棂窗前，额头死死抵在冰冷的玻璃上，目光穿透荒原的雾霭，凝视着远方巴斯克维尔庄园那两座隐现的孪生古堡塔楼。当听到我那熟悉的皮靴在门槛上踩踏出的摩擦声时，她整个人如中箭的惊鸟般猛地一颤，仓皇转身，那张美艳绝伦的异国面庞上的血色在一秒钟之内褪得干干净净。

‘他进庄园了，’我神色从容如常地跨进室内，随手掩上厚重的橡木房门，伴随着一声清脆冰冷的金属咔嗒声将门锁徐徐反拧到底。我将沉甸甸的铁钥匙顺手滑入了西装背心的贴身口袋。

她背脊不住后退，直到肩膀死死抵住了粉刷的石膏墙壁，那对乌黑深邃的眼眸因极致的恐惧而剧烈放大。‘杰克……看在上帝的份上，看在十字架的面子上，我求求你了！收手吧！放过那个年轻人吧！他才三十岁，他从未做过任何伤害你的事啊！带上我们所有的积蓄，带我离开这片令人发疯的死绝沼泽吧！带我回哥斯达黎加吧，哪怕粗茶淡饭，只要我们能在阳光下堂堂正正生活，双手不再沾染鲜血！’

我两步跨越房间。还没等她来得及抬手护住面孔，我的右手如精钢铸就的老虎钳般瞬间卡死了她那纤细雪白的咽喉，以万钧之力将她整个人狠狠按死在高背马鬃扶手椅中，直到她的气管在压迫下发出急促绝望的窒息喘息！

‘给我听清楚了，我天真圣洁的小蠢货，’我俯下身庞，脸颊凑得极近，眼镜框甚至碰到了她剧烈颤抖的太阳穴，‘在伦敦，你敢瞒着我用修甲剪刀裁切报纸，给亨利爵士寄去匿名信。我当时没有掐死你，仅仅是因为你这张美艳动人的脸孔，乃是将那个年轻蠢货引诱过荒原迈向死地的唯一诱饵！但给我听好了，贝丽尔，把每一个音节都深深刻进你的脑髓里：这里绝非伦敦！方圆五英里内没有一个警察，方圆两英里内没有半户邻居，而大格林盆泥潭距离我们的后门只有短短三十码！’

肉体的剧痛与精神的彻底绝望化作泪水，顺着她死死紧闭的眼角无声滑落。

‘倘若那个年轻男爵踏入这栋房子时，你敢向他吐露半个字——倘若你敢通过眼神、手势或任何暗示走漏半句你是我的合法妻子而非胞妹的真相——我不仅会当场送你的堂弟下地狱，更会在夜半三更将你拖过暗石孤岛，用精钢铁链死死锁在炼铁工棚的石环上，将你一个人扔在无底的黑暗中，与那头饥肠辘辘的恶兽同处一室！你听明白了吗，贝丽尔？！’

我缓缓松开了铁铸般的右手。她浑身剧烈抽搐着从马鬃椅垫上瘫软滑落，像一条濒死的宠物犬般匍匐在地板上，脸颊死死贴着我的西裤裤脚，在极度的屈辱与动物般的恐惧中放声痛哭。

‘我闭嘴……我发誓我什么都不会说！’她在被泪水打湿的裤脚旁抽泣道，‘求求上帝宽恕我，我一个字都不会说的……我什么都不会透露！’

‘最好把你的誓言刻在骨头上，’我面无表情地跨过她瘫软的身躯，‘明天一早，那位自命不凡的华生医生必将只身踏勘荒原的地形地貌。我将带上我的绿纱网，在泥潭小道旁主动迎候他。一个滔滔不绝、沉溺学术的热心乡村博物学家——天下还有什么比这更完美的人畜无害伪装？！不出十分钟，那个脑袋少根筋的退伍老军医便会将我引为莫逆之交。而只要将华生玩弄于股掌之间，亨利爵士便会顺理成章地踏入我们的客厅！’

我旋开书房门锁，坐在长桌前，从容地摆弄起明天用来固定战利品的钢针与软木板。死亡的巨网已然彻底织就；深渊的剧毒蜘蛛，正耐心静候着猎物步入罗网！"""
    },

    # Chapter 7 Part 1
    {
        "id": "stapleton_ch07_part1_naturalist_act",
        "ch_idx": 6, "part": 1,
        "title_en": "Chapter 7: The Stapletons of Merripit House (Part I: The Mask of the Naturalist)",
        "title_cn": "第七章 梅利琵宅邸的主人斯台普吞（上：温雅博物学者的伪装）",
        "pov": "stapleton", "type": "anchor", "anchor": "anchor_naturalist_stapleton",
        "clues_en": [
            "Stapleton charms Watson with eccentric naturalist persona near Grimpen Mire",
            "Demonstrates pony swallowed in mire to establish bog’s terrifying lethality",
            "Inquires about Sherlock Holmes to confirm the great detective is truly in London",
        ],
        "clues_cn": [
            "手持捕蝶网在荒原小径截获华生，以博学温和的学者谈吐博取对方信任",
            "当场向华生展示达特穆尔矮种野马失足陷顶惨死全过程，借泥潭神威震慑其胆魄",
            "旁敲侧击试探歇洛克·福尔摩斯的真实行踪，确凿核实神探确未随行亲临德文郡",
        ],
        "choices_en": [
            {"id": "s_ch7_p1_c1", "text": "Pursue a cyclopides moth into the heather, leaving Watson to encounter Beryl.", "target": "stapleton_ch07_part2_beryl_blunder"},
            {"id": "s_ch7_p1_c2", "text": "[Switch POV to Dr. Watson] View Watson’s first encounter with Stapleton upon the moor.", "target": "ch07_part1_naturalist", "pov_switch": "watson"},
        ],
        "choices_cn": [
            {"id": "s_ch7_p1_c1", "text": "假意扑打珍稀环纹蝶脱身深入草丛，暗中窥视华生与从后方冲出的贝丽尔之接触。", "target": "stapleton_ch07_part2_beryl_blunder"},
            {"id": "s_ch7_p1_c2", "text": "【视角切换：约翰·H·华生】切换至华生视角，见证他如何对这位古怪学者产生最初好感。", "target": "ch07_part1_naturalist", "pov_switch": "watson"},
        ],
        "content_en": """The morning of October 16th broke with a pale, watery brilliance, the autumn sun glistening upon the miles of wet heather. Equipped with my green gauze butterfly net, my zinc specimen box strapped across my shoulder, and an old tweed Norfolk jacket that lent me the air of an eccentric academic, I strolled along the cart-track that led from Merripit House towards the Hall.

Within half an hour, my patience was rewarded. The square, sturdy silhouette of Dr. John Watson appeared upon the crest of the hill, walking at a brisk military pace, his briar pipe sending a blue spiral of smoke into the clear air, his eyes roving over the undulating moorland.

I quickened my pace, cutting across a patch of bilberry scrub, waving my hat with the uninhibited, bustling enthusiasm of an isolated country enthusiast starved for cultivated conversation.

“Dr. Watson, I presume!” I hailed him in a high, cheerful voice. “Pray forgive the lack of rural ceremony, but when a man lives on the borders of the Great Grimpen Mire, he dispenses with the formalities of St. James’s! I am Jack Stapleton, of Merripit House.”

The honest soldier stopped, removed his pipe, and greeted me with that frank, open warmth which makes an English gentleman so easy to manipulate. In five minutes, I had him completely disarmed. I chatted with boyish animation about the rare orchids hiding in the peat-hags, pointed out the ancient circular stone huts of the Neolithic tribesmen clinging to the tors, and lamented with grave, melancholy deference the untimely death of our mutual friend, poor Sir Charles.

Suddenly, as we stood upon a low granite knoll overlooking the emerald expanse of the Great Grimpen Mire, a sound tore through the quiet air—a wild, agonized scream that rose into a bubbling gurgle!

Twenty yards away, a small Dartmoor pony, venturing onto the deceptive green turf in search of fresh bog-cotton, had broken through the crust! The black, oily slime was already up to its withers. It threw back its shaggy head, its eyes rolling in terror, thrashing frantically with its forelegs; but with every convulsive movement, the subterranean suction dragged it deeper, faster!

I gripped Watson’s arm with my hand, pointing my butterfly net towards the tragedy.

“Look, Dr. Watson!” I cried, my voice dropping to a tense, dramatic whisper. “The Great Grimpen Mire! It is a quicksand of bottomless depth! A misstep of six inches from the firm path, and a man or beast is sucked into the bowels of the earth! That pony will be dead within two minutes!”

Watson stood frozen, his face pale with horror, watching the animal’s muzzle vanish beneath the bubbling, iridescent slime. A foul belch of swamp gas broke the surface, and the green moss closed smoothly over the spot, leaving not a ripple behind.

The demonstration was sublime! The horror of the moor was burned into the good doctor’s soul. He would never venture onto the bog alone, nor would he allow Sir Henry to wander from the beaten track without a shudder of dread!

Then, while his guard was lowered by the shock, I dropped my probe—smooth, casual, and delivered with an air of innocent curiosity:

“We were all grievously disappointed down here that Mr. Sherlock Holmes was unable to accompany Sir Henry. May we hope to see that illustrious gentleman visit Devonshire before the season ends?”

Watson smiled with modest, professional pride. “His hands are completely tied by an affair of international importance in London. For the present, the safety of Sir Henry Baskerville rests entirely in my hands.”

Entirely in your hands! 

I had to drop my gaze to the heather and feign a sudden sneeze to conceal the triumphant grin that twitched at the corners of my mouth! The great detective was safely bottled up in London! The game was ours to play, and the prize was within my grasp!""",
        "content_cn": """十月十六日清晨，惨淡而湿润的深秋日光洒落荒原，将漫山遍野被露水打湿的石楠苔原映照出一片朦胧的光晕。我手提绿纱长柄捕蝶网，肩头斜挎着锌制标本采集盒，身上套着一件洗得发白的粗花呢诺福克夹克，整个人散发出一种令人生不起半点戒心的落魄学者气质，神态自若地漫步在从梅利琵宅邸通往庄园的大道碎石路旁。

仅仅过了半个小时，我的守株待兔便获得了丰厚的回报。约翰·H·华生医生那敦实魁梧的身形很快出现在了山脊的转角处。他迈着标准的军人步伐，嘴里叼着石楠烟斗，将一缕青蓝色的烟雾吐向清冽的空气，警惕而好奇的目光不断扫视着这片起伏不平的荒原。

我加快脚步迎上前去，抄近路穿过一处越橘灌木丛，热情地挥动着宽边帽子，脸上洋溢着常年幽居偏远乡野的学者在偶遇文明同道时特有的爽朗与急切。

‘想必阁下定是华生医生了！’我用高亢轻快的声音高声致意，‘万望恕我乡村野夫的唐突失礼，但当一个人住在荒无人烟的大格林盆泥潭边缘时，圣詹姆斯宫廷那套繁文缛节便早已被抛之脑后！在下杰克·斯台普吞，梅利琵宅邸的主人。’

这位诚朴的军官停下脚步，摘下烟斗，脸上流露出那种英国绅士特有的坦荡与温和——正是这种毫无心机的正直，使得他们成为世上最容易被玩弄于股掌之间的猎物。短短五分钟之内，我已然彻底卸下了他的全副心理防线。我像个热衷学问的少年般滔滔不绝地向他炫耀着隐藏在泥炭裂隙中的珍稀兰花，信手指向远古峰峦上那些依附在岩壁上的新石器时代圆形石屋遗址，并以极其肃穆深沉的语调，表达了对我们共同的故友、可怜查尔斯爵士猝然长逝的无限哀思。

突然之间，当我们并肩伫立在一处俯瞰大格林盆泥潭翠绿沼面的花岗岩低岗上时，一声撕心裂肺的绝望惨嘶骤然撕碎了荒原的晨曦——那是一声伴随着咕嘟水泡冒出声的垂死挣扎！

在相距我们仅仅二十码的沼泽边缘，一匹达特穆尔矮种小马因贪恋嫩绿的棉草，一脚踩穿了伪装成草坪的致命泥壳！黑亮油腻的剧毒死浆已然漫过了它的马肩隆！小马绝望地仰起毛茸茸的头颅，双眼圆睁充血，前蹄在泥浆中狂暴扑腾踢蹬；然而它的每一次剧烈抽搐挣扎，都仅仅在将它以更快的速度拖入深不见底的地心深渊！

我一把死死抓住华生的衣袖，手中的捕蝶网竹柄如剑般直指眼前的惨剧。

‘瞧啊，华生医生！’我惊呼出声，嗓音骤然降调为充满戏剧张力的紧绷低语，‘这便是大格林盆泥潭！一片深不见底的绝命流沙！只要脚下一步踏错坚实的暗径，无论是凡人还是走兽，都会在顷刻间被卷入万丈深渊！不出两分钟，那匹马便会彻底沉入地心！’

华生目瞪口呆、浑身僵直地伫立在原地，面色因极度的惊骇而惨白如纸。他亲眼目睹着那匹矮马的口吻与悲鸣的眼睛彻底没入了翻滚着五彩油光的水泡之下。泥潭深处恶臭的沼气咕嘟破裂，翠绿的苔藓随即便平滑如初地合拢覆盖，在水面上连半圈涟漪都未曾留下。

这场即兴教科书般的死亡演示堪称绝妙至极！大荒原那吞人嚼骨的恐怖梦魇已然深深烙印在了这位退伍军医的灵魂深处。从今往后，他绝不敢孤身涉足沼泽半步，更绝不敢放任亨利爵士离开正道而毫无恐惧之感！

紧接着，趁着他的心智被这震撼一幕彻底缴械的空当，我从容不迫地抛出了那枚致命的试探之针——语气轻松温和，仿佛只是出于纯粹的乡野好奇：

‘未能在这片土地上亲眼瞻仰大名鼎鼎的歇洛克·福尔摩斯先生的风采，真是令全教区上下遗憾万分。不知传闻是否确凿，那位大神探果真因公繁忙，整个季节都无暇亲临德文郡视察吗？’

华生脸上流露出一丝军人特有的含蓄自豪：‘伦敦有一桩极其重大的公海勒索要案死死缠住了他的身躯。在目前这段时期内，亨利爵士的一切安全防务全权交由我一人全权照料。’

全权交由你一人照料！

我必须立刻低下头去佯装端详石楠草，借着一声喷嚏的掩护，才勉强死死压抑住了嘴角那抹险些撕裂我温雅伪装的狰狞狂笑！那位名满天下的大神探被死死锁在了伦敦！整盘大棋已任由我肆意驰骋，七十四万镑的黄金王座已然近在咫尺！"""
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
            "Realizes Beryl’s rebellious spirit must be crushed before the final strike",
        ],
        "clues_cn": [
            "贝丽尔背地里狂奔出农舍拦路阻截，误将华生当作亨利爵士发出绝命撤退警告",
            "斯台普吞假意扑蝶折返撞破密谈，以高超冷酷的‘兄长’伪装掩饰滔天杀机",
            "清醒认识到妻子内心的反叛烈火仍在燃烧，决意在决战前夜施加更残酷的高压管制",
        ],
        "choices_en": [
            {"id": "s_ch7_p2_c1", "text": "Invite Watson and Sir Henry to dine at Merripit House to cement the social trap.", "target": "stapleton_ch08_probing_watson"},
            {"id": "s_ch7_p2_c2", "text": "Inspect the hound’s chains and security upon the mire island.", "target": "stapleton_ch08_probing_watson"},
        ],
        "choices_cn": [
            {"id": "s_ch7_p2_c1", "text": "正式向华生与亨利爵士发出梅利琵宅邸午后茶会之约，将猎物引入社交死角。", "target": "stapleton_ch08_probing_watson"},
            {"id": "s_ch7_p2_c2", "text": "踏着暗径返回泥潭孤岛，复查恶兽项圈铁链的坚固度与绝密防御设施。", "target": "stapleton_ch08_probing_watson"},
        ],
        "content_en": """I feigned a sudden, ecstatic burst of scientific passion, pointing my butterfly net towards a tiny fluttering speck of grey among the heather.

“A cyclopides!” I shouted with the frenzy of an enthusiast. “A rare skipper moth, long believed extinct in the southwest! Pray excuse me, Dr. Watson—it must not escape!”

I plunged headlong into the bilberry bushes, leaping across the peat-rifts, swinging my net with comical exaggeration until I had put two granite knolls between Watson and myself. 

My sprint was a calculated diversion. I wished to double back under the cover of the rocks and observe the good doctor’s unguarded demeanour through my field-glass. But as I scrambled to the summit of the ridge, the sight that greeted my eyes struck my heart like an icy spear!

Beryl! 

The miserable, defiant creature had slipped from the house and was running breathless across the moor, her black Spanish mantilla trailing in the wind! 

Through the gaps in the gorse, I watched her rush up to Dr. Watson. Her face was flushed with passionate agitation, her dark eyes flashing with terror and desperate appeal! Even across three hundred yards of moorland air, her pantomime was unmistakable: she was grasping the doctor’s coat sleeve, gesturing violently towards the south, commanding him to turn back, to quit Dartmoor, to flee for his life to London that very day! 

The blind idiot had mistaken Watson’s square-shouldered, tweed-clad figure for Sir Henry Baskerville!

My fingers clenched around the bamboo cane of my net until the wood groaked and split in my palm. One word of the hound—one whisper of our true marriage—and the hangman’s rope would be around my neck before Sunday!

I did not hesitate for a heartbeat. I leaped from behind the boulders, swinging my net aloft, whistling a jaunty air from Carmen as though returning triumphant from my chase.

“Halloa, Beryl!” I hailed them, descending the slope with bounding, cheerful strides. “What brings you out upon the heath in this raw autumn wind?”

The transformation was instantaneous. She stiffened as though an electric current had shot down her spine. She stepped back from Watson in guilty haste, her lips blanching, her face freezing into that marble, expressionless mask she always wore when the whip was raised over her head.

“I was out walking, Jack,” she stammered, her voice shaking with suppressed terror. “And I... I was admiring the moorland views with this gentleman.”

I laughed—a rich, hearty, indulgent laugh that resonated with brotherly affection.

“You must forgive my sister’s eccentricities, Dr. Watson!” said I, stepping between them and clapping Watson on the shoulder with easy familiarity. “She is a delicate plant from sunny climes, and this gloomy Devonshire moor terrifies her nervous constitution. The tragic fate of poor Sir Charles has completely unstrung her imagination. Come, Dr. Watson! You must not return to the Hall without tasting our hospitality. Walk back with us to Merripit House; Beryl shall make you a cup of genuine Costa Rican coffee, and I shall show you my cabinet of Dartmoor Lepidoptera!”

Watson was utterly enchanted by my geniality. The suspicion planted by Beryl’s frantic warnings dissolved like morning mist before my polished, sunny charm.

Yet as we walked three abreast down the narrow sheep-track, my nails dug into the palms of my clenched fists until blood welled beneath the skin. 

Beryl’s defiance had ceased to be an annoyance; it had become an acute, mortal hazard. Her sentimental conscience was a leaking dam that threatened to drown me at any hour. When the fatal night arrived, words and threats would no longer suffice. She must be gagged, bound to the bedposts with hemp cords, and locked in darkness where no human ear could catch her screams!""",
        "content_cn": """我故作狂喜失态，指着石楠花丛中一只翩跹翻飞的灰色飞蛾，整个人展现出一副走火入魔的狂热学者姿态。

‘是一只弄蝶！’我像个疯子般手舞足蹈地大喊，‘一只在整个英格兰西南部早已被认定灭绝的珍稀环纹弄蝶！千万恕我失陪，华生医生——绝不能让它逃出我的视线！’

我拔腿狂奔深入厚密的越橘灌木丛，大步跃过一道道泥炭裂谷，夸张地在空中挥舞着捕蝶网，直到两座花岗岩矮岗彻底将华生的身影隔绝在我的视线之后。

这场追逐纯粹是一场经过精密计算的障眼法。我本意是借着巨石的天然掩护暗中迂回包抄，通过袖珍望远镜逆向端详这位军医在独处时的警惕神态。然而，当我攀上一处花岗岩山脊回首眺望的一刹那，眼前的景象如同一柄淬毒的冰刃，瞬间狠狠扎入了我的心脏！

贝丽尔！

那个该死、执迷不悟的贱人竟然趁我不备偷偷溜出了宅邸，正气喘吁吁地在石楠丛中亡命狂奔，她那袭黑色的西班牙蕾丝头巾在朔风中如丧幡般猎猎作响！

透过金雀花灌木的枝权缝隙，我惊骇地目睹她一路飞奔扑到了华生医生面前！她满脸通红，神色激动得近乎神经错乱，黑亮深邃的眼眸中喷涌着极致的恐惧与绝望的哀求！即便隔着整整三百码的距离，我也能轻易读懂她那疯狂的肢体语言：她死死拽着华生的大衣衣袖，手臂激烈地指向南方，声嘶力竭地命令对方立刻撤退、滚出达特穆尔、在今天天黑之前搭乘火车亡命逃回伦敦！

这个瞎了眼的蠢女人，竟然把华生那身着粗花呢大衣的敦实方正身材，误当成了远道而来的年轻男爵亨利·巴斯克维尔！

我的十指死死捏紧了手里的竹柄捕蝶网，指节泛出惨白，坚硬的竹竿甚至在掌心发出一声刺耳的脆裂呻吟！只要她嘴里吐出半句关于恶犬的真相——哪怕透露半字我们乃是合法夫妻而非兄妹的实情——粗糙的绞刑索便将在本周日套死在我的脖颈之上！

我没有半分犹豫。我猛地从巨石后飞身跃下，高高举起手中的绿纱网，嘴里欢快地吹奏着歌剧《卡门》的轻快选段，迈着大步从容走下斜坡，俨然一副刚刚大获全胜归来的无邪模样。

‘哈喽，贝丽尔！’我爽朗地高声呼喊道，‘究竟是什么兴致，竟把你这位娇小姐也引到了这寒风刺骨的荒原上？’

奇迹般的震慑效果在一瞬间显现无遗。她整个人宛如被数万伏特的高压电流穿透了脊椎，浑身剧烈一僵，触电般飞速从华生身侧退开两步，面孔在半秒钟之内被冻结成了一张毫无生气的惨白大理石面具——正是每当皮鞭高高举起在她头顶时，她所展现出的绝望麻木。

‘我只是出来散散步，杰克，’她结结巴巴地强咽下一口唾沫，嗓音在强行压抑的恐慌中不住发颤，‘而我……我刚才正陪这位先生一同欣赏荒原的风景。’

我仰天大笑起来，笑声温厚、慈爱而充满了长兄对幼妹那种宠溺的宽容包容。

‘啊，我亲爱的华生医生，您可千万别见怪！’我一步跨到他们二人中间，亲切地拍了拍华生的肩膀，展现出令人如沐春风的熟稔与体面，‘我这妹妹生性胆怯脆弱，对这片阴冷的达特穆尔荒原畏之如虎，查尔斯老爵士的不幸惨死更是彻底摧毁了她的神经。走吧，华生医生！既然到了家门口，若不尝尝我们的乡野款待，我可绝不放您回庄园！随我们一同踏入梅利琵宅邸品上一杯正宗的哥斯达黎加现磨咖啡，我还要带您参观我私藏的达特穆尔珍稀鳞翅目昆虫标本柜呢！’

华生完全被我这副热情爽朗的绅士派头彻底俘获缴械。贝丽尔刚才那番神经质的绝命警告，在我灿烂如春风的温雅谈吐面前，如晨雾般消散得无影无踪。

然而当我们三人并肩穿过狭窄的羊肠碎石小道时，我的指甲已然深深刺入了紧握的拳头掌心，鲜血顺着指甲缝悄然溢出。

贝丽尔那不可救药的反叛已然演变成了最致命的定时炸弹。她骨子里那多愁善感的情感良知，是一道随时可能决堤淹没我的致命破口。等到决战收网的那个良夜降临之时，口头警告与皮鞭恐吓已然远远不够了。我必须用粗麻绳将她彻底五花大绑在床柱上、用布条死死封住嘴唇，将她关在暗无天日的密室中，让她连半声绝叫都休想传出宅邸！"""
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
            {"id": "s_ch8_c2", "text": "[Switch POV to Sherlock Holmes] View Holmes in his stone hut reading Watson’s first dispatch.", "target": "holmes_ch08_watson_report", "pov_switch": "holmes"},
        ],
        "choices_cn": [
            {"id": "s_ch8_c1", "text": "趁着午夜万籁俱寂，手提生鲜血食潜入大格林盆泥潭深处，犒劳饥渴暴虐的恶兽。", "target": "stapleton_ch09_part1_feeding_the_hound"},
            {"id": "s_ch8_c2", "text": "【视角切换：歇洛克·福尔摩斯】切换至黑色岩岗石屋，看名侦探就着烛光逐字剖析华生密报。", "target": "holmes_ch08_watson_report", "pov_switch": "holmes"},
        ],
        "content_en": """The fortnight that followed was a masterclass in social manipulation and psychological camouflage.

I paid a formal call at Baskerville Hall, presenting my compliments to the new master with all the deference of an eccentric, bookish neighbour. Young Sir Henry, suffocating in the gloomy vastness of that ancient granite mausoleum, seized upon my society with transparent, boyish enthusiasm. Within forty-eight hours, the path between the Hall and Merripit House was beaten bare by his boots.

And there, beneath my own roof, the second grand engine of my plot began to revolve with intoxicating power: Sir Henry fell head-over-heels, blindly, passionately in love with Beryl!

He could not tear his eyes from her dark, foreign beauty. Whenever she poured his tea, his hands trembled; whenever she sang a Spanish romance to her guitar, his honest Canadian face glowed with adoration. It was a card of immense strategic value, yet one that required the balance of a tightrope walker over an abyss. If I permitted an open courtship, Sir Henry would propose marriage within a week, whisk her away to a London church, and our true marital status would be unmasked before I had struck the blow!

I resolved the dilemma with a stroke of theatrical genius: I staged a scene of violent, pathological brotherly jealousy!

When Sir Henry contrive to meet Beryl upon the moor path near the quarry to declare his love, I sprang from the rocks like a madman. I cursed the baronet, accused him of abusing our hospitality and attempting to dishonor an unprotected maiden, and ordered him from our presence with every insult my tongue could summon!

The young baronet was bewildered and humiliated, but his Canadian stubbornness was inflamed a hundredfold. Opposition transformed an infatuation into an all-consuming obsession! He called upon me the next day, offered an abject apology for his precipitation, and pledged his sacred honour to keep his distance until I should formally bestow my brotherly consent upon his suit.

I had him completely in my web. He was bound by his own code of chivalry, while Beryl was kept under my immediate surveillance.

Meanwhile, what of the doughty Dr. Watson?

The good doctor spent his evenings sitting before the roaring hearth at the Hall, his service revolver on the mantlepiece, industriously covering reams of foolscap paper with his observations. Through the daughter of the Grimpen postmaster, who was on terms of intimacy with my kitchen-maid, I learned that Watson was despatching immense packets of manuscript addressed to Mr. Sherlock Holmes at 221B Baker Street twice a week.

Let the fool write! Let him describe the melancholy trees, the crying of the curlews, the suspicious tears of the butler Barrymore, and the blameless eccentricities of Jack Stapleton! While Dr. Watson penned his romance and Sherlock Holmes sat five hundred miles away smoking his pipe by the London fire, the clock was ticking relentlessly down towards the final catastrophe!""",
        "content_cn": """在接下来的整整两周时间里，我上演了一场堪称心理操控与社交伪装教科书的绝妙大戏。

我以邻家书卷气学者的体面身份正式登门造访巴斯克维尔庄园，向新主人致以最崇高的敬意。在这座空旷阴冷、犹如古墓般死寂的花岗岩古堡里，百无聊赖、渴望交际的年轻亨利爵士如获至宝般抓住了我的友谊。短短四十八小时之内，从庄园通往梅利琵宅邸的那条荒原小道，便已被他的马靴踏出了一条清晰的光溜溜黄泥小径。

正是在我的屋檐之下，我庞大谋杀杀局的第二重致命引擎开始以令人狂醉的威力轰然运转：亨利爵士不可救药、彻底盲目地疯狂迷恋上了贝丽尔！

他的那双眼睛一刻也舍不得从她那张绝美动人的异国面庞上挪开。每当贝丽尔为他斟倒红茶时，他的手指甚至在抑制不住地微微发颤；每当她抱着吉他轻声吟唱西班牙浪漫曲时，这位年轻男爵那张轮廓分明的面孔上便喷涌出无限的崇拜与爱慕！这是一张价值连城的超级王牌，然而却需要最为精确的走钢丝操作。倘若我放任他们公开热恋，亨利爵士必定会在一周内当面求婚并将其带往伦敦大教堂完婚，从而在我的致命杀机动手前戳破我们乃是合法夫妻的铁幕真相！

于是，我当众上演了一出堪称戏剧化天才的癫狂大戏：一记蓄谋已久的病态吃醋狂怒！

当亨利爵士在采石场附近的荒原小径旁背地里拦住贝丽尔吐露炽热衷肠时，我如疯狗般猛地从巨石后杀出。我当着华生的面厉声痛骂男爵居心叵测、竟敢恩将仇报企图玷污侮辱一个无依无靠的乡野纯洁孤女，并用尽刻薄至极的恶毒辞令当场将他粗暴地轰出了我的领地！

亨利爵士被骂得无地自容、羞愧万分，然而美洲开荒者骨子里的倔强却将他的占有欲与征服欲瞬间点燃了上百倍！得不到的阻隔，反而让他发疯般下定决心务必明媒正娶迎娶贝丽尔。他次日便登门谢罪，苦苦哀求我的宽恕，并立下庄严的骑士誓言：在未获得我这位‘大舅哥’的首肯之前绝不再越雷池半步！

我将他彻底锁死在了我的蛛网中央。他被他自己的骑士道德所捆绑，而贝丽尔则处于我时刻不停的严密贴身监视之下。

与此同时，那位勇敢忠诚的华生医生又在做些什么呢？

这位善良憨厚的退伍军医每天夜晚都窝在庄园那熊熊燃烧的壁炉旁，左轮手枪搁在壁炉架上，整夜整夜在厚厚的日记纸上奋笔疾书，详尽记录着他收集到的每一丝鸡毛蒜皮。透过格林盆村邮局局长的女儿——她同我后厨的洗碗女仆情同姐妹——我确凿获悉，华生每周都会雷打不动地向伦敦贝克街221号B的歇洛克·福尔摩斯寄出厚厚两大包信件战报。

任由这个蠢材去写吧！让他去极尽能事地描摹荒原凄凉的落叶、石楠丛中夜莺的啼哭、管家白利墨可疑的眼泪，以及杰克·斯台普吞那些看似人畜无害的珍稀昆虫标本！当华生在写着他的侦探纪实小说、而歇洛克·福尔摩斯正安坐于五百英里外的伦敦壁炉旁无聊吐着烟圈之际，死亡的钟摆正在一分一秒地逼近最后的末日审判！"""
    },

    # Chapter 9 Part 1
    {
        "id": "stapleton_ch09_part1_feeding_the_hound",
        "ch_idx": 8, "part": 1,
        "title_en": "Chapter 9: The Light upon the Moor (Part I: Feeding the Demon in the Mire)",
        "title_cn": "第九章 沼地上的烛光（上：夜入泥潭饲喂恶兽）",
        "pov": "stapleton", "type": "anchor", "anchor": "anchor_convict_stapleton",
        "clues_en": [
            "Stapleton sneaks across the mire at 1 AM to feed blood and meat to the starving hound",
            "The beast’s muffled baying rolls across the moor, striking terror into the district",
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
        "content_en": """At one o’clock in the morning of October 20th, when the silence of the dead had settled over Merripit House and Beryl was safely locked in her upstairs bedroom, I slipped through the scullery door into the pitch-black fog.

In my canvas pack, I carried fifteen pounds of raw, dripping butcher’s offal and bullock’s liver, purchased under cover of night from an isolated slaughter-house near Bovey. The midnight traverse of the Great Grimpen Mire was an ordeal that would have driven an ordinary man screaming into madness. The quagmire on either side hissed and gurgled with noxious marsh gases; the foul water bubbled around my waterproof leggings; and a misstep of four inches would have meant sinking into an icy, subterranean grave from which no human hand could drag me forth. But my feet knew every submerged granite block, every tussock of firm rush, with the mechanical instinct of a wolf.

I reached the island knoll and unlocked the heavy padlock on the smelting shed.

The moment the bolt grated, a sound rumbled from the gloom that set the very marrow of my bones vibrating—a low, rhythmic, thunderous growl of ravenous, untamed fury.

The beast knew my step.

I lit my storm lantern and hung it upon the iron bracket. In the yellow light, the monster loomed against the stone wall like an apparition from the book of Revelation. Its coat was matted, its flanks lean and hollow with hunger, its fiery yellow eyes fixed upon my canvas sack with a ferocity that strained the heavy iron staples in the granite wall. 

I cut the cords and emptied the contents of the sack onto the stone floor.

The hound threw itself upon the bloody offal with a savage, crunching roar! In the dim shed, the sounds of snapping sinews and fracturing marrow-bones were so sickening, so terrifyingly primal, that even my hardened nerves were tested. While it devoured the meat, I dipped a sponge into a bucket of fresh rain-water, wiped the crusted dried blood from its jowls, and inspected the heavy links of its chain.

When the last shred of gristle had disappeared down its throat, the creature threw back its massive, bull-like head, pointed its black muzzle towards the broken rafters of the roof, and gave vent to a long, shuddering, bloodcurdling howl!

It was a sound that began in a deep, subterranean rumble, rose to a piercing, despairing shriek of ancient malice, and died away in a mournful, sobbing cadence that echoed across the vast, moonlit desert of the moor!

I stood motionless, smiling in the shadows of the shed. I made no effort to silence it.

Let the moor hear the voice of its phantom! Let Sir Henry Baskerville start awake beneath the heavy counterpanes of his bed, clutching his blankets in superstitious terror! Let the ignorant rustics cower by their hearths and cross themselves! Every echo of that demon voice was preparing the public mind—preparing the coroner, the magistrates, and the jury—to accept the heir’s coming death as the inevitable, supernatural vengeance of the Baskerville curse!""",
        "content_cn": """十月二十日凌晨一点整，当死一般的死寂彻底笼罩了梅利琵宅邸、贝丽尔已被我稳稳反锁在二楼卧室之后，我悄然穿过后厨侧门，一头扎入了浓黑如墨的夜雾之中。

在沉重的粗帆布背包里，装着我趁着夜色从波维附近一家偏僻屠宰场秘密采买来的十五磅血淋淋的碎肉与牛肝。在深更半夜只身横渡大格林盆泥潭，是对人类神经极限的最残酷考验。两侧的无底黑浆咕嘟翻滚着致命的毒气与气泡；冰冷刺骨的脏水拍打着我的高筒防水皮裤；只要脚下踏错四英寸，便会瞬间被拖入永无天日的地下万丈深渊，绝无任何人力能将我拖出！然而我的双脚对于每一块沉在水下的花岗岩暗石、每一丛结实的芦苇草墩的熟悉程度，宛如一头出巡的野狼熟知自己的领地。

我登上了孤岛花岗岩高岗，旋开了废弃炼铁工棚上的沉重铜锁。

就在插销发出刺耳金属声的一刹那，工棚内部轰然爆发出一阵低沉浑厚的共鸣——一阵令我骨髓深处都为之剧烈颤栗的雷霆闷吼，那是原始野兽饥肠辘辘、毁灭一切的暴虐咆哮。

恶犬嗅到了我的脚步声。

我擦亮风雨马灯，挂在墙壁的铁支架上。在昏黄摇曳的光柱中，那头庞然巨兽宛如从《启示录》预言深处爬出的活体恶魔。它的黑毛纠结杂乱，两侧肋骨因极度饥饿而深陷下瘪，两只泛着凶残黄光的兽瞳死死锁定了我的帆布背包，庞大的身躯狠狠扯动着精钢铁链，震得嵌在石壁里的巨大铁环咯咯作响。

我割断麻绳，将背包里大块大块鲜血淋漓的碎肉与内脏轰然倒在石板地面上。

恶犬发出一声狂暴的低吼，猛扑向这堆血肉！在幽暗的工棚里，獠牙嚼碎筋腱与大口撕咬骨骼的脆响令人毛骨悚然，那声音是如此凶残原始，即便是我这般冷酷如铁的神经也不禁隐隐发憷。在它狼吞虎咽之际，我用海绵蘸着洁净的雨水，仔细擦拭着它口角结痂的干涸血迹，仔细复查着铁链每一个坚硬的环扣。

当最后一块骨髓被嚼碎咽下肚时，这头巨兽猛地扬起庞大沉重的头颅，黑色粗壮的口吻直指残破的屋顶椽木，从肺腑最深处爆发出一声凄厉、悠长、在天地间悲怆回荡的恐怖长嗥！

那长嗥声从地底深处的闷雷声开端，逐渐拔高为撕裂苍穹的古老恶毒尖啸，最终在一种令人毛骨悚然的凄绝余音中渐渐平息，在皎洁月色笼罩下的浩瀚荒原上空久久回荡！

我伫立在工棚的阴影之中，面露微笑，丝毫没有伸手制止它的狂吠。

让这片荒原在它恶魔的咆哮声中战栗吧！让亨利·巴斯克维尔爵士从庄园厚重的被褥深处惊坐而起，死死抓紧床单在迷信的恐惧中瑟瑟发抖吧！让那些愚昧的乡民蜷缩在壁炉前拼命在胸口画十字吧！恶犬长嗥的每一丝回音，都在为日后的验尸官、治安法官以及陪审团心甘情愿地将新男爵之死归咎于超自然的天谴魔咒，打下最坚不可摧的心理铁证！"""
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
        "content_en": """I locked the heavy oak door of the shed and picked my way back across the secret stepping-stones. But just as my boots struck the firm, springy heather of the mainland shore, a sound shattered the freezing night air like the snapping of dry pine!

A gunshot!

A sharp, whip-like pistol report, followed instantly by a second crack that echoed off the jagged granite cliffs of Black Tor!

I dropped flat into the deep shadow of a dry peat-hagg, unbuttoning the flap of my revolver holster. Had the Princetown constabulary located my island?

Lifting my head above the heather, I scanned the vast, moonlit amphitheater of the waste. High upon the northern plateau, illuminated by the brilliant silver glare of the full moon, three human figures were sprinting across the crags! In the lead, bounding from boulder to boulder like a hunted mountain goat, was a wild, shaggy wretch clad in the mud-stained yellow convict garb—Selden! And fifty yards in his rear, their revolvers flashing in the moonlight, firing wild shots into the dark, ran Sir Henry Baskerville and Dr. Watson!

They were chasing the convict! The fools had interrupted a midnight rendezvous and were wasting their powder upon a starving wretch!

I watched the pursuit with contemptuous amusement. But then, as my gaze followed the towering black ridge of Black Tor against the silver disc of the moon, my breath stopped dead in my throat!

High upon the very pinnacle of the highest crag, standing motionless as a statue carved from basalt rock, was the silhouette of a man!

He stood with his arms folded across his breast, his head bent forward in an attitude of intense, vigilant scrutiny. His tall, gaunt frame was framed sharply against the pale moonlight; a peaked traveling cap was drawn low over his brow. He looked down upon the valley where Sir Henry ran, watching the hunt like an omniscient bird of prey perched upon its roost.

Who in heaven or hell was he?

It was not a parish constable. No rustic bumpkin ever stood with that commanding, aristocratic poise. Could it be a confederate of the convict? Or was it... someone infinitely more dangerous?

In a flash of cold sweat, the memory of Regent Street rushed back upon my mind—the hawk-like profile, the cold, steel-grey eyes that had bored through the glass of cab No. 2704!

Could Sherlock Holmes have deceived the world? Could the great detective have slipped into Devonshire in secret, living upon the open moor like a wild Indian, directing Watson’s movements from the shadows?

An icy shiver of dread crawled down my spine. If Holmes was upon Dartmoor, the game was a matter of life and death! I must discover who occupied that crag. But before I launched a probe into the tors, my flank had to be secured: Laura Lyons in Coombe Tracey must be muzzled beyond any possibility of betrayal!""",
        "content_cn": """我锁好工棚厚重的橡木大门，踩着沉水暗石折返陆地。然而就在我的皮靴刚刚踏上北侧山脊结实松软的石楠苔原时，一声清脆震耳的巨响骤然撕碎了冰冷的寒夜，宛如干枯的松枝被硬生生折断！

是枪声！

一声清脆如鞭笞般的手枪枪响，紧接着是第二声枪响，在黑色岩岗那犬牙交错的花岗岩绝壁间激荡起久久不绝的脆烈回音！

我瞬间伏倒在一处干燥泥炭沟的浓黑阴影中，右手啪的一声解开了大衣下左轮手枪的枪套扣带。难道是普林斯敦的警队摸到了我隐匿恶兽的孤岛？！

我缓缓从石楠丛后探出头颅，目光扫过整片在皎洁月色笼罩下的浩瀚荒原。在北部高耸的荒原高原上，在满月那惨白银辉的映照下，三条狂奔的人影正在乱石滩上飞速掠过！领头狂奔的，是一个身穿黄条纹囚服、蓬头垢面如野兽般在巨石间上蹿下跳的亡命徒——正是越狱犯塞尔登！而在他身后五十码远的地方，亨利·巴斯克维尔爵士与华生医生正端着左轮手枪狂暴穷追不舍，手中的枪口不断在黑夜中喷吐出刺目的火舌！

他们在追捕逃犯！这帮自作聪明的蠢材，显然撞破了管家白利墨与逃犯的深夜联络，竟然把宝贵的火药与体力浪费在一个饥寒交迫的丧家之犬身上！

我正暗自冷笑鄙夷，然而当我的视线顺着黑色岩岗那陡峭高耸的花岗岩脊线、投向圆月悬挂的夜空背景时，我的心脏猛地爆发出了一记剧烈沉重的狂跳，呼吸瞬间在喉咙里彻底冻结！

在黑色岩岗最险峻孤绝的巨岩之巅，在万丈月光那惨白的照耀之下，赫然傲立着一个如同玄武岩雕像般一动不动的瘦高人影！

他双臂冷冷环抱于胸前，头颈微微前倾，以一种近乎全知全能的深邃与警惕，居高临下死死俯瞰着谷底亨利爵士的一举一动！那具挺拔瘦削的身躯在月色背景下轮廓分明；一顶鸭舌旅行帽深深压在眉际。他宛如一头栖息在绝壁之巅的冷血猛禽，冷冷注视着谷底的一切骚乱。

他究竟是人是鬼？！

那绝非笨拙愚钝的乡野巡警，更不可能是本地的羊倌。在这片蛮荒贫瘠的土地上，绝无任何凡夫俗子能够展现出如此冷峻孤高、傲视一切的统帅威仪！难道是逃犯暗中联络的接头同伙？抑或是……某个比逃犯凶险千百倍的索命克星？！

在瞬间涌出的冷汗之中，伦敦摄政街上那惊心动魄的对决记忆如烙铁般再次烫痛了我的脑髓——2704号马车车窗外，那对穿透玻璃的鹰隼般灰色寒眸！

难道歇洛克·福尔摩斯在全世界面前演了一场弥天大谎？！难道全欧洲最顶尖的神探早已隐姓埋名潜入了德文郡，如同一头野蛮的印第安人般在达特穆尔荒原上露营扎寨，在暗中全盘操盘着华生的一举一动？！

一阵刺骨的寒意顺着我的脊椎骨疯狂向下蔓延。倘若福尔摩斯当真亲临达特穆尔，这场博弈便已彻底演变成了你死我活的悬崖决斗！我必须彻查黑色岩岗上究竟盘踞着何方神圣！然而在探查岩岗之前，我必须首先彻底封死后方的侧翼：库姆马西的劳拉·里昂斯，绝不能让她漏出半点威胁我的口风！"""
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
            {"id": "s_ch10_c2", "text": "[Switch POV to Sherlock Holmes] View Holmes reading Watson’s diary extract regarding L.L.", "target": "holmes_ch10_diary_and_laura", "pov_switch": "holmes"},
        ],
        "choices_cn": [
            {"id": "s_ch10_c1", "text": "手持望远镜严密盘查黑色岩岗，暗中跟踪给史前石屋神秘怪客送饭的小厮行踪。", "target": "stapleton_ch11_part1_spy_on_tor"},
            {"id": "s_ch10_c2", "text": "【视角切换：歇洛克·福尔摩斯】切换至石屋，见证名侦探根据华生日记锁定L.L.真容。", "target": "holmes_ch10_diary_and_laura", "pov_switch": "holmes"},
        ],
        "content_en": """On the morning of October 22nd, I rode my horse into the market town of Coombe Tracey. A rumour had reached my ears through the village blacksmith that Dr. Watson had been inquiring into the charitable beneficiaries of the late Sir Charles Baskerville.

If Watson or his invisible master approached Laura Lyons, the entire architecture of my plot was in mortal danger!

I entered her small parlour behind the typing office unannounced. Laura was sitting before her Remington machine, her face pale, her dark hair disheveled. When the door opened and she recognized my figure, she sprang up with a cry of mingled terror and relief, throwing herself against my chest with that suffocating, desperate passion that made my gorge rise.

“Jack!” she wept, clutching my lapels. “Thank God you have come! The doctor from Baskerville Hall was seen speaking to my father’s tenants! If they discover that I wrote to Sir Charles on the very night he died—if they find out about the appointment at the wicket-gate—”

I took her wrists, disengaged her clinging arms, and forced her gently but inexorably back into her chair. I drew up a stool, sat directly before her, and looked into her hazel eyes with an expression of profound, tender reproach.

“Laura, my dearest,” I said softly, smoothing the dark curls from her clammy forehead. “Have you so little faith in the man who has risked everything for your happiness? Do you not understand that my silence—and yours—is the only shield that stands between you and destruction?”

She stared at me, trembling. “Destruction, Jack?”

“Consider your position before the law!” My voice dropped to the cold, cutting hardness of a scalpel. “You are a destitute, abandoned woman. You wrote a desperate letter to an elderly, wealthy gentleman, begging for a private meeting in the dead of night at an isolated garden gate. You commanded him, upon his honour as a gentleman, to burn the letter. That very night, within minutes of the appointment, Sir Charles dropped dead of heart failure! What will an English jury say if that letter is dragged into the light? They will say you were an accomplice in a scheme of extortion! They will say you lured an old man into the darkness to be frightened into his grave! The barristers will strip your character to ribbons; you will stand in the felon’s dock at Exeter; and you will be condemned as a common criminal!”

A piercing shriek broke from her lips. She buried her face in her hands, her whole body shaking in an agony of convulsive terror.

“I will never speak!” she sobbed through her fingers. “I swear it before Almighty God, Jack! I will die before I utter a word! If the doctor comes, I will deny that I ever wrote a line! I will swear I know nothing of Sir Charles’s death!”

“Good girl,” I whispered, pressing a cold kiss upon her brow. “Keep silent for just one more week. The money for your divorce is almost in my hands. Within seven days, Laura, we shall quit England forever and begin our glorious new life under the southern sun.”

I left her weeping with gratitude and bound in a psychological cage of my own making. But as I mounted my horse and rode out onto the high moor, I knew that time was running out. Watson was sniffing at my heels. The climax could not be delayed another forty-eight hours!""",
        "content_cn": """十月二十二日清晨，我骑着快马赶往库姆马西集镇。村里铁匠铺的闲言碎语已然传到了我的耳中：那位自命不凡的华生医生，近来正在四处打听查尔斯老爵士生前暗中资助的慈善对象！

倘若华生或是他背后那位隐匿的幕后主使当真找上了劳拉·里昂斯，我那盘耗尽心血的大棋将面临万劫不复的灭顶之灾！

我不宣而入径直推开了打字行后方的起居室房门。劳拉正神色惶恐地坐在雷明顿打字机前，脸色惨白，头发凌乱。当房门推开、看清我的身影时，她发出了一声交织着惊恐与解脱的哭喊，猛地扑上前死死搂住我的胸膛，展现出那种令我心底作呕的黏腻依附。

‘杰克！’她泪如雨下地攥紧我的大衣翻领，‘谢天谢地你终于来了！庄园来的那个军医正在到处盘问我父亲的佃农！倘若让他们知道在爵士暴毙当晚是我写信约他在侧门相见——倘若他们查出木栅侧门的密约——’

我扣住她的双手手腕，从容而坚决地分开了她死死搂抱的手臂，将她按回扶手椅中。我拉过一张圆凳坐在她正对面，居高临下凝视着她那双充满泪水的栗色眼眸，换上了一副充满深情却又痛心疾首的忧郁神情。

‘劳拉，我唯一的挚爱，’我抚摩着她冰凉额头上散乱的黑发低语道，‘难道你对我这个为你押上全部身家性命的男人，就如此缺乏信任吗？难道你当真不明白，我对外界保持绝对缄默，以及你自己的守口如瓶，才是在这场风暴中保全你性命的唯一坚盾？！’

她战战兢兢地望着我，浑身发抖：‘保全我，杰克？’

‘动动你的脑子，看清你当下面对的法律深渊！’我的嗓音骤然降温，变得如冰冷的手术刀般森寒刺骨，‘你是一个穷困潦倒、被丈夫抛弃的落魄女人。你在案发当天亲笔写下一封十万火急的密信，哀求一位家财万贯的贵族老人在深夜十点独自在偏僻荒凉的花岗岩侧门与你私会！你还以绅士名誉逼迫他读罢立即烧毁信件！而就在当晚，就在约定的时间，老爵士便横死侧门！倘若这封信的内容公之于众，英国法庭的法官与陪审团会怎么想？！他们会指控你伙同奸夫敲诈勒索！他们会认定是你充当诱饵将一个体面的老绅士送入了死地！全伦敦的讼棍会把你撕得体无完肤，最终把你作为谋杀共犯推上埃克塞特的绞刑架！’

一声撕心裂肺的凄厉尖叫从她唇间喷涌而出。她双手死死捂住面孔，在极致的恐慌中如触电般剧烈抽搐。

‘我发誓我一个字都不会说的！’她在泪流满面中近乎发狂般起誓道，‘看在全能上帝的份上，杰克！我宁死也绝不吐露半个音节！就算那个军医找上门来，我也绝不承认自己曾给他写过半个字！我发誓我对查尔斯爵士之死一无所知！’

‘这才是我的乖女孩，’我伏身在她前额印上一记冰冷的吻，‘再死死咬牙坚持七天。为你赎买自由身的巨额离婚费已然尽在我的掌控之中。七天之后，劳拉，我们将永远离开英格兰，在南方的暖阳下开启我们辉煌的新生。’

我将这个惊弓之鸟彻底锁死在被恐慌与虚幻美梦编织的心理牢笼之中。然而当我翻身上马驰骋在荒原的高坡上时，我深知死神留给我的时间已然所剩无几。华生的猎犬鼻子已然嗅到了我的脚后跟，终极决战的屠刀必须在四十八小时内悍然挥下！"""
    }
]
