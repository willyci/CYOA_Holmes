"""Jack Stapleton Track - Part 1: Chapters 1 to 5 (8 nodes).
Expanded canonical narrative from the villain's perspective.
"""

STAPLETON_NODES_PART1 = [
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
            {"id": "s_ch1_p1_c2", "text": "[Switch POV to Sherlock Holmes] See Holmes examining Mortimer’s walking stick.", "target": "holmes_ch01_part1_observation", "pov_switch": "holmes"},
        ],
        "choices_cn": [
            {"id": "s_ch1_p1_c1", "text": "踏上大格林盆泥潭暗径深入绝密孤岛，检视囚禁在废弃锡矿工棚中的嗜血巨兽。", "target": "stapleton_ch01_part2_beast"},
            {"id": "s_ch1_p1_c2", "text": "【视角切换：歇洛克·福尔摩斯】切换至伦敦贝克街，目睹名侦探以手杖展开神准演绎。", "target": "holmes_ch01_part1_observation", "pov_switch": "holmes"},
        ],
        "content_en": """I sat in the dim stillness of my study at Merripit House, the dissecting needle steady between my forefinger and thumb as I pinned a rare specimen of the marsh fritillary to the drying cork. Through the narrow casement window, the vast, treeless wilderness of Dartmoor rolled away towards the jagged horizon, broken only by the sullen, grey granite ramparts of Belliver and Vixen Tors. To the dull clods of Devonshire—to the country squires, the illiterate peat-cutters, and the pompous parish surgeons—I was merely Jack Stapleton: a harmless, bespectacled schoolmaster turned entomologist, an eccentric recluse who spent his blameless days pursuing Lepidoptera with a green gauze net and pressing marsh orchids between sheets of blotting paper.

Fools! Blind, provincial dolts, incapable of seeing beyond the modest spectacles on my nose!

In my veins ran the fierce, turbulent blood of the Baskervilles, untamed and predatory. My father was Rodger Baskerville, the youngest of the three sons of the old Hall—the dark, reckless rover who had disgraced the family name, fled England under a cloud of debt, and sought his fortune in the turbulent republics of Central America. I was born in the humid heat of Costa Rica, christened with his name and endowed with all his ruthless audacity, wedded to an intellectual cunning he never possessed. When I returned to England with my exquisite Spanish-American wife, Beryl Garcia, I took the name of Vandeleur and established a boys’ boarding academy in the north of Yorkshire. For three seasons fortune seemed within my reach; but an outbreak of typhus swept through the dormitories, three boys perished in agony, the school collapsed in public scandal and bankruptcy, and I found myself an outcast in London, penniless and pursued by relentless creditors.

It was in the bitter squalor of that flight that a chance perusal of the London society gazettes changed the course of my life. My uncle, Sir Charles Baskerville, had returned from the South African diamond diggings, fabulously enriched, and had repurchased the ancestral manor at Dartmoor. Seven hundred and forty thousand pounds! A colossal fortune invested in gilt-edged consols and South African gold, with vast revenues accruing every month! And between that golden mountain and myself stood only two fragile lives: Sir Charles, an aging widower with an aneurysm of the aorta who lived in terror of his own shadow, and a distant nephew, Henry Baskerville, who was grubbing out a living on a Canadian farm!

I realized instantly that my destiny had arrived. I abandoned the ruined name of Vandeleur, assumed that of Stapleton, and removed to Devonshire. I rented this lonely, whitewashed cottage upon the very brink of the Great Grimpen Mire, using our last sovereigns to furnish it. I coerced Beryl, under threats that froze the blood in her veins, to pass as my unmarried sister. A beautiful unmarried woman is a magnet, a weapon of infinite utility in a secluded countryside; a wife is merely a domestic impediment. 

And then, in the candlelit library of Baskerville Hall, under the guise of an admiring neighbour studying the family history, I discovered the weapon that Providence had forged for my hand: the yellowed, water-stained manuscript of 1742 detailing the legendary curse of Hugo Baskerville and the fiery hound that had torn his throat upon the moor!

An ancestral demon! A spectral hound that lived in the superstitious marrow of every tenant on the estate! What chemist, what assassin in history could devise an instrument of murder more flawless, more completely untraceable than an ancestral legend made flesh? Sir Charles possessed a heart that fluttered like a trapped bird at every sudden creak in the night. He would not require poison; he would not require a dagger. One glimpse of the ancestral nightmare bursting from the darkness of the yew trees would be enough to rupture his fragile heart and send him headlong to his grave!""",
        "content_cn": """我静坐在梅利琵宅邸那间幽暗的书房里，食指与拇指沉稳地捏着解剖钢针，将一只珍稀的沼泽网蛱蝶标本精准刺入干燥软木板的中央。透过狭窄的铅条窗格，达特穆尔荒原浩瀚苍凉、寸草不生的荒野向着低垂的灰色天际线无垠蔓延，唯有贝利弗岩岗与泼妇岩岗那犬牙交错的花岗岩残壁在风中沉重伫立。在德文郡那些愚昧庸俗的乡巴佬眼中——在那些肥头大耳的乡村乡绅、目不识丁的泥炭雇工，以及自命不凡的教区外科医生眼里——我仅仅是杰克·斯台普吞：一个戴着金丝眼镜、温文尔雅的落魄乡村教师兼昆虫学者，一个在山间整日挥舞着一面绿纱网追逐飞蛾、用吸水纸压制沼泽兰花的古怪隐士。

蠢材！一帮瞎了眼的乡巴佬，一帮连我鼻梁上的眼镜伪装都看不透的凡夫俗子！

在我的骨髓与血管深处，奔淌着的乃是巴斯克维尔家族最原始、最桀骜不驯的狂暴贵族之血！我的亲生父亲罗杰·巴斯克维尔，是查尔斯爵士那一辈三兄弟中最年幼的幼弟——那个在挥霍败家后背负巨债潜逃海外、被家族族谱彻底除名的浪子。我出生在哥斯达黎加湿热难耐的种植园里，继承了父亲的名字，更继承了他毫无怜悯之心的冷酷野心，以及他毕生未曾拥有的绝顶狡黠智慧。当我携带着美艳绝伦的异国娇妻贝丽尔·加西亚重返英格兰时，我曾化名凡德勒（Vandeleur），在约克郡北部开办了一所贵族男子寄宿学校。整整三年，荣华富贵看似唾手可得；然而一场突如其来的恶性斑疹伤寒席卷了整座学生宿舍，三名贵族幼童在惨叫中痛苦夭折，学校在铺天盖地的公众丑闻与债权人围剿中彻底破产清算。我一夜之间沦为了负债累累、东躲西藏的丧家之犬。

正是在那场仓皇屈辱的伦敦暗巷逃亡之中，伦敦社交报刊上的一则不起眼的新闻，彻底改写了我毕生的轨迹。我的亲伯父查尔斯·巴斯克维尔爵士携带着南非金矿与钻石田挖掘出的滔天横财载誉归国，豪掷重金重新买下了达特穆尔祖传的宏伟庄园。七十四万英镑！整整七十四万英镑的金边国债与南非金矿股票，每个月都在产生令人发狂的滚滚红利！而在那座令人目眩神迷的黄金王座与我之间，仅仅阻隔着两条脆弱不堪的人命：一个膝下无子、患有严重主动脉瘤且整日被自己的影子吓得胆战心惊的垂死老头，以及一个远在加拿大冰原拓荒务农的远亲侄子亨利·巴斯克维尔！

我瞬间清醒地意识到，我登临绝顶的命运时刻已然轰然降临。我果断埋葬了凡德勒这个破产污名，化名为斯台普吞，变卖了最后的随身金饰移居德文郡。我在这片紧邻大格林盆泥潭边缘的死绝之地租下了这座白垩粉刷的荒原独栋农舍。我用令她骨髓结冰的严厉死亡威胁，逼迫贝丽尔在世人面前隐瞒夫妻真相，假扮成我尚未出阁的亲妹妹。一个容貌绝美、楚楚动人的未婚异国尤物，在这偏僻闭塞的乡野是一面无往不利的社交磁石与致命武器；而一个合法的妻子，却只会成为束缚我宏图伟业的累赘。

紧接着，在巴斯克维尔庄园那座烛影摇曳的古老藏书室里，我以一位仰慕邻人、潜心考据地方志学者的温雅姿态，从积满灰尘的橡木柜深处掘出了上苍赐予我的终极杀器：那份泛黄水渍斑斑的一七四二年羊皮纸手稿——详细记载着恶魔雨果·巴斯克维尔在午夜荒原遭到幽灵猎犬撕碎咽喉的血腥家族魔咒！

一个家族传承两百年的恶魔鬼话！一个深植在庄园每一名佃农骨髓深处的迷信梦魇！古往今来，还有哪位绝顶刺客能够构想出比将古老传说化为肉身更完美、更毫无物理破绽的绝命杀器？！查尔斯老爵士那颗脆弱不堪的心脏，每逢夜半听见窗棂震动便会如惊弓之鸟般疯狂悸动。他根本不需要咽下剧毒砒霜，更不需要承受锋利的匕首刺入胸膛——只要让那头来自九幽地狱的祖传恶魔咆哮着破雾而出，他那根行将破裂的主动脉便会在胸膛中瞬间炸裂，将他干脆利落地送入万劫不复的坟墓！"""
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
            {"id": "s_ch1_p2_c2", "text": "Test the hound’s ferocity upon the bog island with fresh red meat.", "target": "stapleton_ch02_part1_laura_trap"},
        ],
        "choices_cn": [
            {"id": "s_ch1_p2_c1", "text": "利用爱情陷阱彻底套牢劳拉·里昂斯，指使她写下深夜约见查尔斯爵士的致命诱饵信。", "target": "stapleton_ch02_part1_laura_trap"},
            {"id": "s_ch1_p2_c2", "text": "在泥潭孤岛上以新鲜生牛肉逗弄恶犬，测试其在极度饥饿状态下的凶暴撕咬力。", "target": "stapleton_ch02_part1_laura_trap"},
        ],
        "content_en": """I pulled on my high waterproof boots, picked up my heavy walking staff, and slipped quietly from the back scullery of Merripit House into the gathering gloom of twilight. The path into the Great Grimpen Mire was a secret known to no living soul save myself. To an untrained eye, the bog appeared an unbroken sea of bright emerald green, dotted with deceptive tussocks of flowering cotton-grass. Yet underneath that carpet of deceptive velvet lay ten square miles of bottomless, quivering slime, ready to engulf horse and rider in three breathless seconds. Over six grueling months of patient exploration, I had mapped a labyrinthine chain of sunken stepping-stones—ancient granite slabs and submerged peat-ladders dating from prehistoric tin-miners—that led across the morass to an isolated, granite-strewn knoll rising from the quagmire like the spine of a sleeping leviathan.

Upon that knoll stood the crumbling stone huts and rotting timber sheds of an Elizabethan tin-working abandoned three centuries ago. No shepherd dared approach within a mile of the place; local superstition held it to be the dancing ground of boggarts and marsh demons. It was my impenetrable fortress, my secret laboratory of death.

I reached the heavy wooden door of the old smelting house and unlocked the padlock with a brass key. The moment the hinges groaned, a low, resonant rumble vibrated through the timber walls—a sound so deep, so full of primordial menace, that it set the fillings in my jaw aching. In the pitch darkness within, a heavy iron chain rattled across the stone flags with a harsh, metallic rasp.

I lit my storm lantern and stepped over the threshold.

Looming against the stone wall was the creature that would win me my empire. It was an immense beast, coal-black as a raven, with the towering shoulder-height of a mastiff and the savage, sinewy endurance of a bloodhound. I had purchased it in London under an assumed name from Ross and Mangles, the notorious dealers in Fulham Road, who had bred it from their fiercest fighting stock. I had transported it south by circuitous railway routes in a padded crate labeled as botanical machinery, and had walked it out here across the tors on a moonless midnight so that no rustic eye had ever glimpsed its silhouette. It stood nearly thirty inches at the shoulder, with jaws that could snap the thigh bone of a heifer, eyes that burned with unslaked hunger, and muscles that rippled like wound steel cords beneath its glossy black coat.

Setting my lantern on a stone ledge, I took from my leather satchel the dark glass jar containing my masterpiece of chemical invention. White phosphorus, painstakingly dissolved in a refined preparation of non-volatile bone oil and odorless glycerin. It was a formula that had cost me weeks of delicate laboratory trial. Ordinary phosphorus would scorch the flesh and deaden the animal’s olfactory nerves with its acrid fumes; my mixture was cold, odorless, and utterly harmless to the skin, yet in darkness it radiated a ghostly, bluish-green luminosity of terrifying intensity.

The brute growled, its black lips curling back to expose two-inch fangs wet with saliva. I knew how to master it. I spoke in that low, harsh, guttural tone to which I had accustomed it, tossing it a half-pound knuckle of beef from my bag. While it tore the meat with ravenous crunches, I dipped my cloth brush into the jar and began my work.

With broad, deliberate strokes, I painted the luminous paste across its massive muzzle, around the hollows of its bloodshot eyes, and along the bristling dewlaps of its chest and jowls. 

I stepped backward to the threshold, drew down the tin shade of my storm lantern, and shut off the light.

A gasp of involuntary, shuddering awe escaped my own lips! Even though I had engineered the deception myself, the spectacle that confronted me in the sudden darkness struck a chill of primeval horror through my marrow! The beast stood completely transformed into a demon spawned from the nethermost pit of hell! Its mouth appeared to vomit forth licking sheets of cold blue and emerald flame; its sockets glowed like burning coals dug from the embers of the damned; its massive head and neck flickered with shimmering, unearthly phosphorescence, casting long, wavering shadows across the roof-beams!

It was Hugo Baskerville’s hound incarnate. No mortal heart afflicted with disease could endure the apparition of that blazing monster bounding from the night. The weapon was perfected; all that remained was to fashion the lure that would deliver my aging uncle into its jaws!""",
        "content_cn": """我套上长及大腿的高筒防湿靴，握紧沉重的橡木手杖，趁着暮色苍茫悄然溜出了梅利琵宅邸后院的杂物间。通往大格林盆泥潭深处的绝密暗径，放眼全天下唯有我一人了然于胸。在生人的眼中，这片浩瀚的沼泽是一片毫无破绽的翠绿草地，点缀着具有欺骗性的白头棉草与苔藓；然而在那层如丝绒般绚丽的浮皮之下，却是方圆十英里深不见底、翻滚涌动的剧毒死沼，只需短短三秒便能将一匹狂奔的烈马连人带鞍生吞活剥。在过去的六个月里，我忍受着刺骨的风霜，一点一滴勘探出了一条由沉水巨石与古代矿工步道组成的曲折链条——顺着那些隐没在泥浆下的花岗岩暗石，可以横渡死渊，直抵沼泽最核心那座宛如史前海怪脊梁般凸起的花岗岩孤岛。

在那座孤岛之上，坐落着三座由伊丽莎白时代锡矿工棚遗留下的坍塌石屋与腐烂木棚。方圆数英里内的羊倌与泥炭工从不敢靠近此处半步，乡野传闻这里是荒原水鬼与山妖跳舞的极阴之地。这里是我固若金汤的复仇堡垒，是我制造死亡的绝密实验室。

我来到最深处那座旧炼铁工棚的厚重木门前，用黄铜钥匙旋开了巨大的挂铁锁。就在门轴发出刺耳呻吟的一刹那，整面木板墙壁内部轰然爆发出一阵低沉浑厚的剧烈闷吼——那吼声低沉而充满着毁灭一切的原始杀戮气息，震得我牙床骨深处隐隐作痛。在棚内的无底黑暗之中，一条精钢打制的粗重铁链在石板地面上哗啦啦猛烈拖拽，激荡出刺耳的金属摩擦声。

我擦亮马灯，稳步跨过了门槛。

在昏黄的光柱边缘，巍然矗立着那头即将为我夺取整个黄金帝国的嗜血活物。那是一头堪称庞然巨物的猛兽，通体如渡鸦般漆黑，兼具马士提夫獒犬的高大骨架与纯种寻血猎犬那惊人的凶残撕咬力。这是我隐姓埋名专程奔赴伦敦富勒姆路臭名昭著的‘罗斯与曼格尔斯’名犬行重金购得的极品斗犬杂交种。我通过北部的迂回货运列车将其装入贴有‘植物标本压制机械’的密封木箱运抵德文郡，又在一个没有月色的狂风午夜牵着它徒步翻越荒原，从未让任何世人的目光瞥见过它的半点影子。它肩高足足接近三十英寸，宽阔如重锤的下颚骨足以一口咬碎牛犊的腿骨，一对猩红的巨眼中燃烧着永不熄灭的嗜血凶焰，周身肌肉宛如紧绷的钢缆在油亮的黑毛下剧烈起伏。

我将马灯置于石阶上，从皮囊中取出了装有我毕生化学杰作的深色广口玻璃瓶。这是将高纯度白磷经由复杂工艺完全溶解在精炼骨油与无味甘油中的特制冷光油膏。这是我耗费数周时间在微型烧杯前反复试验的终极结晶。普通的白磷会烧灼皮肉并散发出刺鼻的气味，从而破坏猎犬极其敏感的嗅觉；而我这套独特的配方不仅毫无异味，质地冰凉温润完全不伤毛皮，却能在伸手不见五指的黑暗中爆发出极其耀眼、泛着惨绿与幽蓝交织的恐怖冷光！

恶犬喉咙深处发出阵阵威胁的低吼，黑色的嘴唇翻起，露出两排长达两英寸、滴淌着唾液的惨白尖牙。我知道该如何驯服这头野兽。我口中发出它早已习惯的低沉喉音，顺手从布袋中甩出一大块带骨鲜牛肉。当恶兽在饥不择食的狂暴咀嚼中咔嚓撕碎骨骼之际，我用软布刷饱蘸油膏，从容展开了涂抹。

我以沉稳精准的笔触，将磷光油膏均匀涂刷在它的粗壮口吻、两只充血眼眶的边缘，以及它颈项下那一圈层层下垂的狰狞鬃毛垂肉之上。

我向后退开五步退至门槛，啪的一声将马灯的铁皮遮光罩狠狠拉到底，掐灭了最后一缕凡间的光亮。

一声抑制不住的惊骇倒吸冷气声从我自己的喉咙里脱口而出！即便是我这位亲手缔造这具怪物的造物主，在黑暗轰然降临的刹那，眼前的景象依然令我的骨髓深处泛起阵阵彻骨的战栗！那头恶兽已然彻底蜕变成了一具从九幽地狱火海中爬出的活体恶魔！它的血盆大口仿佛在向外疯狂喷吐着惨绿幽蓝的熊熊烈焰；两只巨眼宛如从炼狱深处抠出的烧红火炭；滴淌涎水的下颚与獠牙周围环绕着刺骨的阴冷鬼火，将跳跃闪烁的阴森幽芒映照在工棚的穹顶横梁之上！

这正是雨果·巴斯克维尔魔咒手稿里的复仇猎犬！放眼全天下，绝没有任何一个患有严重心脏病的老人，能够承受这头通体喷吐烈焰的巨兽在黑夜中咆哮扑击的恐怖视觉暴击！死神的镰刀已然彻底磨砺完毕；现在，我只需为查尔斯伯父布下一记令他无法拒绝的致命诱饵，将他从庄园的深宅大院引诱至午夜的荒原侧门！"""
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
        "content_en": """The instrument to lure Sir Charles into my trap lay ready to my hand in the neighbouring hamlet of Coombe Tracey: Mrs. Laura Lyons, the daughter of that litigious old lunatic Frankland of Lafter Hall. 

She was a creature of pathetic, fragile vanity, possessed of a fading Spanish-type beauty and trapped in a web of desperate poverty. Her scoundrel husband, an artist named Lyons, had deserted her in London years before; her tyrannical father had cast her out without a shilling for daring to marry against his tyrannical decree; and she was now attempting to maintain a miserable, debt-ridden livelihood by typing legal briefs on an old Remington machine. Over several months, I had spun a web of insidious sympathy around her battered ego. I played the role of the chivalrous, intellectual protector. I listened to her grievances with sorrowful brown eyes, purchased paper for her office, and gradually fed her romantic imagination with promises of an idyllic future.

“If only you were legally emancipated from this scoundrel Lyons,” I would whisper, sitting beside her small hearth and stroking her trembling fingers, “if only you possessed the funds to institute divorce proceedings in the High Court in London, you would find a haven in my arms. Beryl and I would welcome you as the honoured mistress of Merripit House.”

The sum required to clear her pressing local debts and pay the retainers of London solicitors was substantial—two thousand pounds. Where upon Dartmoor was such wealth to be found, coupled with a chivalrous disposition towards distressed gentlewomen? Nowhere save in the open pocket of Sir Charles Baskerville!

On the morning of May 4th, I called upon Laura at her cottage in Coombe Tracey. She was in a state bordering on hysterical collapse. A London creditor had that morning threatened her with legal attachment and the debtor’s prison at Exeter.

“Sir Charles leaves for London tomorrow morning,” I told her, my voice urgent, grave, and compelling. “His valet has already packed his trunks. He goes to consult heart specialists, and his friends whisper that he may never return to Devonshire! If you write him a formal appeal through the post, he will refer you to his London solicitors, Messrs. Gautier and Brown, and you know how cold lawyers treat appeals for cash. You must see him yourself, face to face! You must touch his chivalry and extract his promise before the London train bears him away!”

“He will never receive me in his library at night!” she gasped, twisting her handkerchief. “The servants—the scandal—”

“Then meet him at the private wicker gate that opens from the yew alley onto the moor!” I urged, drawing a sheet of her own notepaper towards her. “It is completely private. No servant ever enters the gardens after nine o’clock. Sit here, Laura. Write what I dictate, word for word.”

With a trembling hand, weeping tears of mingled hope and humiliation, she dipped her pen and wrote down the fatal lines:

“Please, please, as you are a gentleman, burn this letter, and be at the gate by ten o’clock.”

“Sign it with your initials,” I said softly, standing behind her chair. “L. L. It will pique his memory without compromising your name if the paper should miscarry.”

I took the envelope, sealed it myself, and had it posted directly to Baskerville Hall by the local carrier.

At five o’clock that very afternoon, I returned to Laura’s cottage. My face was set in an expression of wounded masculine pride, stern and sorrowful.

“Laura,” I said, seizing both her wrists and looking down at her with fiery indignation, “I have reflected upon this interview, and my soul revolts! My honour as a gentleman cannot suffer the woman I intend to make my bride to beg money at a dark garden gate from an elderly libertine! I have this afternoon arranged a mortgage upon my own securities. I have secured the two thousand pounds from my bankers in Plymouth! You shall not go to Baskerville Hall tonight!”

She collapsed against my chest, sobbing in an agony of overwhelming gratitude, kissing my hands and calling me her savior, her noble knight!

The silly, blind dupe! She believed she had been rescued from humiliation. In reality, she had signed Sir Charles Baskerville’s death warrant, while leaving herself bound in a conspiracy of silence that would prevent her from ever daring to breathe a word of our appointment to the constabulary!""",
        "content_cn": """将查尔斯老爵士诱入死局的最完美人选，早已现成地摆在库姆马西集镇：劳拉·里昂斯夫人——拉夫特庄园那个整日沉迷打官司的诉讼狂老弗兰克兰的亲生骨肉。

这是一个性格脆弱、虚荣心极强，容貌带着几分凋零异国风韵，却在残酷现实中被贫困彻底逼入死角的绝望女人。她的无赖丈夫是一个在伦敦寻欢作乐的三流画家，多年前便卷走积蓄将其狠心抛弃；她那个脾气暴躁如雷的法盲父亲因她当年私奔抗婚，与她彻底恩断义绝断绝了父女关系；如今她只能窝在狭小的寓所里，靠一台旧雷明顿打字机替律师抄写公文艰难度日，整日生活在债台高筑的屈辱恐慌之中。在过去的数月里，我以极具欺骗性的绅士温情精心编织了一张无形的情网。我扮演着高尚、博学的同情者与守护神，用充满怜惜的忧郁目光倾听她的抽泣，自掏腰包为她采买打字纸，并用一纸虚幻的婚姻诺言彻底麻痹了她的心智。

‘倘若你能摆脱那个流氓里昂斯在法律上的枷锁，’我常常坐在她那狭窄的壁炉旁，轻抚着她冰凉发颤的手指低语道，‘只要有一笔钱能支付伦敦高等法院那昂贵繁琐的离婚诉讼费，你便能在我的怀抱中找到永恒的避风港。我和贝丽尔会张开双臂，迎接你成为梅利琵宅邸尊贵的女主人。’

结清她积欠的本地债务并支付伦敦大律师的定金，需要整整两千英镑。放眼整片达特穆尔荒原，究竟何人拥有如此惊天巨富，又对落难名媛怀有骑士般的救济热忱？唯有查尔斯·巴斯克维尔爵士那大敞四开的钱袋！

五月四日清晨，我踏入了劳拉在库姆马西集镇的打字行。她正处于精神濒临崩溃的绝望边缘。伦敦的一名债权人今早派人送来了传票，威胁将在埃克塞特法庭申请强制执行将她投进债务人监狱。

‘查尔斯爵士明天清晨就要动身前往伦敦，’我神色严峻，嗓音低沉而充满了不容置疑的紧迫感，‘男仆已经在为他收拾皮箱。他是去伦敦延请心脏病权威会诊，庄园里甚至私下传闻他此番离去可能再也不会重返德文郡！倘若你仅仅寄去一封公事公办的求援信，他只会将你推给伦敦高瑟父子律师行那帮冷血无情的讼棍！你必须当面见他！你必须当面哭诉，在他登上火车之前彻底唤醒他骨子里的骑士怜悯之心！’

‘可他绝不会允许我在深夜踏入庄园的藏书室！’她双手死死绞着手帕，语无伦次地颤声道，‘那些仆人……流言蜚语……’

‘那就约在从庄园红豆杉林荫道通向荒原的木栅侧门相见！’我催促着，顺手将一张信纸推到她的眼前，‘那里绝对隐蔽！晚上九点之后绝无任何仆人踏足后花园半步！坐下，劳拉，按我念的写，一字不差地写下来。’

在极度的惶恐与重获新生的盲目狂喜中，她颤抖着握紧钢笔，就着泪水写下了那行绝命的密约：

‘求求您，求求您，倘若您当真是一位体面的绅士，读罢请将此信烧毁，并于今晚十点整在侧门相候！’

‘署上你的缩写字母，’我站在她椅后温柔低语，‘L. L. 这样既能唤醒他的记忆，即便信件意外遗失也绝不会玷污你的名节。’

我亲手接过信封封好火漆，当场交由本地的乡村信使火速投递往巴斯克维尔庄园。

下午五点，我再次跨入了劳拉的寓所。我脸上换上了一副严厉、自尊受辱却又充满痛苦深情的凝重表情。

‘劳拉，’我一把扣住她的双手手腕，以炽热的目光注视着她，‘我反复思量了这场会面，我的灵魂在承受无法忍受的煎熬！作为一个男人的尊严，我绝不能容忍我未来的妻子在漆黑的荒原侧门向一个老头子摇尾乞怜！今天下午，我已经通过普利茅斯的银行质押了我自己的海外投资证券，成功筹措到了这笔两千英镑的现款！今晚，你绝对不许踏足巴斯克维尔庄园半步！’

她感动得扑入我的怀中放声大哭，吻着我的手背，把我当成了救她于水火的高贵骑士。

这个愚不可及的蠢女人！她做梦也想不到，她亲手写下的不仅是查尔斯爵士的死刑判决书，更将她自己牢牢焊死在了一场无法向任何警方吐露真相的自绝退路之中！"""
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
        "content_en": """The night of May 4th was suffocatingly damp and pitch-black, with heavy banks of rain-clouds blotting out every star. At a quarter past nine, I slipped out from the rear of Merripit House, leading my beast upon a double-braided hemp leash. Over its head, muzzle, and shoulders I had cast a heavy army blanket to shroud the terrifying gleam of its phosphorus coating. We walked through the black peat like two shadows, skirting the edge of the mire where the turf was springy and muffled our footfalls.

By twenty minutes to ten, I had reached the northern boundary of the Baskerville estate. Outside the dense, twelve-foot wall of trimmed yew trees that enclosed the famous alley, the moor stretched away in unbroken solitude. I took up my position behind a dense clump of gorse bushes, barely twenty paces from the low, wooden wicket-gate that opened through the hedge onto the open heath.

Through the black, interlacing twigs of the yews, I saw a tiny red spark ignite.

Sir Charles had arrived! He had stepped from the manor house, walked down the long, gravel alley, and unlocked the wicket-gate. He stood leaning over the top rail, looking out into the misty darkness of the moor, expecting to see the timid figure of Laura Lyons hurrying from the track. The red glow of his cigar brightened and dimmed rhythmically. Even at that distance, I could hear the nervous tapping of his shoe upon the gravel and the raspy, wheezing sound of his labored breathing.

Ten o’clock struck from the square granite tower of the church down at Widecombe. The sound rolled through the damp air, deep and mournful.

The old baronet was growing anxious. He opened the gate, took two paces out onto the turf, and then turned back to the hedge. He tapped his first cigar against the rail, scattering ash upon the ground, struck a second sulfur match, and lit a fresh Havana. Ten more agonizing minutes ticked away. The night chill was settling into his ruined chest; he began to cough, a dry, rattling cough that shook his stooping shoulders.

His hour had come.

I pulled off the heavy woolen blanket. I held the beast by its stout brass collar, leaned my face against its burning temple, and whispered into its flattened ear. I pointed its glowing muzzle through the gorse straight towards the gap in the hedge where the old man stood.

“Take him, boy!” I snarled in a savage undertone. “Go!”

The hound sprang forward with a low, earth-shaking roar!

Sir Charles heard the thunder of galloping paws and whirled round. What met his superstitious, terror-haunted gaze was the very incarnation of his family’s two-hundred-year-old nightmare: an enormous, black demon bounding through the darkness, its eyes smouldering like fiery pits, its jaws dripping with blue and emerald flames!

A scream of unimaginable agony tore from the old man’s throat—a shriek that choked into a dry rattle before it was half spent. He did not even attempt to pull the wooden wicket shut behind him. He spun on his heels and fled down the yew alley towards the distant sanctuary of the Hall. But terror had paralyzed his limbs; he ran in a grotesque, stumbling frenzy, his toes digging into the gravel, his hands clutching frantically at his breast as the aneurysm ruptured beneath his ribs!

After fifty yards of blind, stumbling flight, his heart burst. He plunged headlong onto the turf beside the path, his fingers clawing at the earth, his face contorted in a mask of terminal horror!

I blew my high-pitched ultrasonic Galton whistle. The hound, trained to instant mechanical obedience by months of reward and punishment, skidded to a halt twenty yards short of the fallen body. It turned, bounded back across the wicket, and crouched panting at my knee. 

I threw the blanket over its head, snapped the lead onto its collar, and led it swiftly back across the bog into the black sanctuary of the Grimpen Mire.

Not a single tooth had touched his skin. Not a drop of blood had been spilled. A clean, undetectable execution! The coroner would find nothing save natural heart failure; the superstitious locals would whisper of the curse; and the first of the two lives standing between myself and seven hundred and forty thousand pounds was extinguished forever!""",
        "content_cn": """五月四日深夜，天气闷热潮湿，夜色浓黑如墨，低垂的乌云将漫天的星光吞噬殆尽。九点一刻，我牵着被厚毛毯严密包裹头部的恶兽，从梅利琵宅邸后门悄然遁入了夜色。恶犬口吻与双眼处散发出的森冷磷火被沉重的军用羊毛毯死死遮挡。我们宛如两只无声的幽灵，贴着泥潭边缘吸水松软的苔原无声前行，甚至连半点脚步声都未曾惊动荒原。

差二十分十点，我们抵临了巴斯克维尔庄园的北侧边界。在庄园那道高达十二英尺、由修剪整齐的红豆杉树篱构筑的林荫道外，茫茫荒原沉浸在一片死寂之中。我在一丛高大茂密的金雀花灌木后伏下身躯，距离那扇通向荒原的低矮木栅侧门仅仅只有二十步之遥。

穿透红豆杉树篱那纵横交错的漆黑缝隙，一点微弱暗红的火光骤然亮起。

查尔斯老爵士如期而至！他独自走出了庄园主楼，信步穿过长长的碎石林荫道，伸手旋开了木栅侧门的铜栓。他倚靠在门栅边沿，神色焦灼地向着荒原雾霭笼罩的远方极目远眺，苦苦等待着劳拉·里昂斯那柔弱的身影从羊肠小径上匆匆赶来。他指间雪茄烟头的暗红微光有节奏地忽明忽暗。即便隔着二十步的距离，我也能清晰听见他的皮鞋在碎石上不安踱步的声响，以及他那破损不堪的气管在寒夜中发出的急促喘息。

威德库姆村教堂花岗岩方塔的大钟沉闷地敲响了十点的钟声。钟声穿透潮湿的夜雾，低沉而宛如丧钟。

这位年迈的男爵越发显得坐立不安。他推开木门，向荒原草地上迈出了两步，随即又退回了树篱边。他弹落了第一撮雪茄烟灰，擦亮第二根硫磺火柴，点燃了另一支新鲜的哈瓦那雪茄。又是令人窒息的漫长十分钟过去了。夜半的寒气开始钻透他那早已溃烂的心肺；他剧烈地咳嗽起来，干咳的声音震得他佝偻的肩膀不住战栗。

死神降临的时辰彻底成熟了。

我猛地一把扯掉了蒙在恶犬头上的厚羊毛毯！我死死攥住它坚硬如铁的黄铜项圈，脸颊贴在它发烫的太阳穴旁，对着它贴服的耳朵吐出恶魔般的命令，将它那张喷吐着惨绿幽火的巨口死死对准了树篱缝隙中老人的身影。

‘上，咬死他！’我牙缝中挤出嗜血的厉喝，‘去！’

恶兽发出一声惊天动地的闷吼，轰然自灌木丛中暴起扑出！

查尔斯爵士听到了巨爪踏碎草皮的雷霆狂飙声，骇然回首！然而映入这位长期深陷家族诅咒梦魇的老人眼帘的，是彻底撕裂其理智的活体梦魇：一头体型如牛、周身燃着森森绿火的巨大黑魔，正张牙舞爪自虚空中狂暴扑杀而来！

老爵士发出一声被扼死在喉咙里的凄厉绝叫！他甚至根本来不及关上侧门，猛然转身沿着红豆杉小径用脚尖亡命狂奔，双手绝望地死死撕扯着胸口的衣襟！仅仅狂奔了五十码远，他那颗脆弱的心脏便彻底破裂碎裂，整个人面孔朝下，轰然仆倒在草坪之中！

我立刻吹响了高频无声犬笛（Galton whistle）。受过严苛训练的恶犬在距离尸体二十码远的地方硬生生刹住了脚步，欢快地折返奔回我的身旁。我将厚毛毯重新罩上它的头颅，拍了拍它的背脊，牵着它如幽灵般悄然隐没在大格林盆泥潭那片深不可测的黑色庇护所中。

死者身上没有留下任何物理创口。一桩完美绝伦、毫无破绽的绝世谋杀！第一块绊脚石已然彻底扫清！"""
    },

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
        "content_en": """The coroner’s inquest at Widecombe proceeded with the blind, bovine predictability that I had counted upon. The jury of rustic dunderheads listened to the medical evidence of Dr. Mortimer, stared at the diagrams of the yew alley, nodded their solemn wigs, and brought in a unanimous verdict: death from natural causes, due to long-standing cardiac disease. Mortimer, obsessed with his craniological measurements and terrified of igniting a county-wide panic, kept his mouth shut concerning the giant footprint in the peat twenty yards from the body. The local sheets praised the deceased baronet for his benevolence, and within a fortnight the world had buried Sir Charles Baskerville and moved on.

I believed the prize was in my hands. I had only to wait a decent interval, bring forward my birth certificates from Costa Rica, establish my descent from Rodger Baskerville, and claim the estate as the next of kin. 

And then, on the morning of October 8th, a thunderbolt struck.

The Western Morning News carried an announcement that turned my blood to gall. Messrs. Gautier and Brown, the family solicitors in London, had established communication through the High Commissioner for Canada with a direct heir: Sir Henry Baskerville! The young man was the son of my father’s elder brother, the middle brother who had died in America thirty years before. He was young, thirty years of age, robust as a pine tree, and had spent his youth clearing timber and cattle-farming near Lake Superior. He had already taken passage upon the transatlantic steamship RMS Etruria, was due to land at Southampton within the week, and intended to take immediate possession of Baskerville Hall!

My rage in the solitude of my study was so violent that I smashed my microscope against the stone hearth! 

Was I to be cheated at the very threshold of paradise? Had I braved the gallows, lived for months on the edge of a pestilential bog, and stained my soul with my uncle’s blood, only to see the seven hundred and forty thousand pounds handed to an illiterate colonial clodhopper?

Never! Not while breath remained in my body!

A second blow was imperative, and it must be struck without mercy. But to repeat the tragedy upon Dartmoor immediately after Sir Henry’s arrival was out of the question. Even the dullest constables in Devonshire would smell foul play if two successive heirs dropped dead at the gates of the Hall within five months. The assassination must take place in London—in that vast, indifferent labyrinth of four million souls, where street accidents, river drownings, and drunken affrays are buried beneath tomorrow’s newspapers!

I acted with lightning speed. I took fifty pounds of horse-flesh across the mire to my island, securing the hound with extra chains and water enough for a fortnight. I packed two valises, purchased an adhesive black beard and heavy tinted spectacles from a theatrical costumier in Exeter, and dragged Beryl with me to the railway station.

She guessed my intent. On the train to London, she knelt upon the floor of our first-class compartment, weeping, clinging to my knees, begging me to renounce the inheritance and fly with her to South America.

I seized her throat with my left hand and forced her head back against the carriage cushions until her lips turned blue.

“Listen to me, Beryl,” I hissed, smiling into her terror-stricken eyes. “If you breathe one word to a living soul—if you drop one hint that I am not Jack Stapleton, or that you are my wife—I will not merely send your handsome Canadian cousin to his grave. I will bring you back to the mire, strip you naked, and chain you to the post inside the smelting shed with the hound!”

She fainted in my hands. When we reached Waterloo, I took modest lodgings in a quiet street in St. John’s Wood under the name of Vandeleur. Within twenty-four hours, my inquiries had located Sir Henry Baskerville and Dr. Mortimer at the Northumberland Hotel in the Strand. The quarry was in London, and the hunter had closed the ring!""",
        "content_cn": """在威德库姆村召开的验尸法庭，完全按照我预先设计好的剧本滑稽上演。那帮脑满肠肥的乡村陪审员听完了摩梯末医生的医学陈述，木然端详着小树道的现场草图，郑重其事地晃动着假发，最终给出了一致裁决：死于因长期心脏器质性病变引发的自然猝死。摩梯末那个整日沉迷于颅骨测量的书呆子，生怕引发全教区的迷信恐慌，对距离尸体二十码外的巨大兽印三缄其口。地方报纸极尽溢美之词追忆逝者生前的善举，不出两周，世人便彻底将查尔斯爵士埋入了尘土。

我原本以为那座金山已然尽入囊中。我只需耐心等待一段体面的哀悼期，随后拿出我在哥斯达黎加的出生证明，确凿证实我乃是罗杰·巴斯克维尔的亲生血脉，便能顺理成章地以唯一近亲的身份接管全部信托遗产。

然而十月八日清晨，晴空霹雳轰然炸响！

《西部晨报》头版刊登的一则官方通告，险些将我的胆汁彻底气裂。伦敦高瑟父子律师行通过加拿大高级专员公署，正式联络到了庄园的法定第一顺位继承人：亨利·巴斯克维尔爵士！他是二伯父的遗孤——那个三十年前客死美洲的二哥留下的亲骨肉！这位年轻男爵年方三十，身板健壮得宛如苏必利尔湖畔的参天松柏，自幼在加拿大冰原开荒伐木、经营牧场。他已然搭乘皇家邮轮‘伊特鲁里亚号’横渡大西洋，一周之内便将在南安普顿靠岸，并誓言将火速亲临达特穆尔全权入主庄园！

在我那间逼仄的书房里，我的狂怒险些撕碎理智，我当场将整架昂贵的黄铜显微镜狠狠砸碎在花岗岩壁炉上！

难道我千辛万苦抵达的天堂之门，竟要眼睁睁被一个粗鄙野蛮的殖民地庄稼汉夺走？！难道我冒着同赴绞刑架的万丈深渊、在恶臭的沼泽边缘潜伏数月，双手染满亲伯父的热血，最终只是为他人做嫁衣？！

绝不可能！只要我胸膛中尚存一丝呼吸，这笔财富便绝不可能易手！

必须立刻施以第二记雷霆绝杀！然而若在亨利抵庄后立刻如法炮制，即便是德文郡最愚钝的巡警也必将嗅出人为谋杀的血腥味。最理想的行刑场，唯有帝国的心脏——庞大臃肿、人情冷漠的伦敦！在这座吞吐着四百万孤魂野鬼的迷雾之都，一场马车倾覆、一次泰晤士河溺水或是一场暗巷斗殴，不出一天便会被翻篇的新闻彻底淹没！

我以闪电般的速度展开行动。我运送了五十磅马肉踏入泥潭孤岛，为恶兽加固了铁链并备足了半个月的清水。我收拾好两只提箱，从埃克塞特的一家戏院道具行采买了一副黏贴假黑胡须与深色墨镜，强行将贝丽尔拖上了前往伦敦的列车。

她猜到了我的杀机。在飞驰的头等舱包厢里，她跪倒在地板上痛哭流涕，死死抱住我的双膝，苦苦哀求我放弃继承权同她远走高飞逃回南美。

我伸出左手死死卡住她的咽喉，硬生生将她的头颅按在天鹅绒坐垫上，直到她娇嫩的嘴唇泛出缺氧的青紫。

‘给我听清楚了，贝丽尔，’我微笑着凝视着她那双充满绝望恐惧的黑眼睛低语道，‘倘若你敢向任何活人吐露半个字——倘若你敢泄露半句我不是斯台普吞，或者你是我的合法妻子——我不仅会把你的加拿大堂弟送进坟墓，更会亲手把你拖回大格林盆泥潭，扒光你的衣服，用铁链将你锁在工棚里，与那头饥饿的恶兽同处一室！’

她在我的铁掌下当场吓得昏死过去。抵达滑铁卢车站后，我以凡德勒之名在圣约翰伍德一条僻静的小街租下了简朴的寓所。短短二十四小时之内，我的眼线便查明了亨利爵士与摩梯末入驻了河岸街的诺森伯兰旅馆。猎物已然入瓮，猎手的大网已然彻底合围！"""
    },

    # Chapter 4 Part 1
    {
        "id": "stapleton_ch04_part1_hotel_shadow",
        "ch_idx": 3, "part": 1,
        "title_en": "Chapter 4: Sir Henry Baskerville (Part I: Shadows at the Northumberland Hotel)",
        "title_cn": "第四章 亨利·巴斯克维尔爵士（上：诺森伯兰旅馆的眼线与剪报）",
        "pov": "stapleton", "type": "anchor", "anchor": "anchor_london_shadow_stapleton",
        "clues_en": [
            "Beryl secretly composes warning letter using words cut from yesterday’s Times",
            "Stapleton discovers the betrayal, terrifies Beryl, but the letter is already mailed",
            "Stapleton bribes chambermaid to steal Sir Henry’s boot to secure his scent",
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
        "content_en": """On the evening of October 12th, returning to our lodgings in St. John’s Wood after reconnoitering the Strand, I stepped into the parlour to find Beryl crouched upon the hearth-rug in an attitude of guilty panic. Beside her lay a discarded copy of yesterday’s Times, its leading article disfigured by gaping, razor-cut holes, and a pair of curved nail-scissors still gripped in her trembling fingers.

My eye fell upon the gum-pot and the slips of printed paper scattered across the mahogany table.

A snarling oath broke from my lips! I crossed the room in two strides, gripped her long hair, and dragged her to her knees.

“What have you done, you wretched traitress?” I hissed, shaking her until her teeth rattled.

“I warned him!” she gasped through a torrent of weeping. “I pasted the words upon an envelope and posted it to the Northumberland Hotel! I told him to keep away from Dartmoor! I could not bear the damnation of another murder on our souls, Jack! Strike me if you will, kill me if you dare, but the letter is in the Charing Cross post and beyond your reach!”

A surge of volcanic fury almost drove me to strangle her on the spot. I hurled her against the sofa with a blow that bruised her shoulder. The miserable fool! If Sir Henry took fright at an anonymous scrap of print and fled back to the Canadian backwoods, the estate would slip through my grasp forever! 

There was not a moment to be lost. My hand was forced. If the young fool was not to escape me, I must acquire the means to hunt him down wherever he fled. And to hunt a man with my beast across any terrain, there was one indispensable requirement: a personal article saturated with his living scent.

At six o’clock the following morning, wearing a dark Inverness cape and tinted spectacles, I entered the bustling lobby of the Northumberland Hotel amidst the confusion of the morning departures. I mounted the rear service stairs to the second floor, where Sir Henry occupied Suite 34. A sleepy Irish chambermaid was sweeping the drugget corridor.

I stepped beside her, dropped my voice to a respectful, confidential murmur, and pressed a golden half-sovereign into her apron pocket.

“My good girl,” said I, smiling with polite deference, “the Canadian gentleman in Room 34 has asked me to take one of his boots to the cobbler in the Strand to have a heel-plate adjusted. He is still asleep, but he left them outside the door to be cleaned. Give me one of them, and this gold is yours for your trouble.”

The girl’s eyes widened at the sight of the gold coin. She darted to the doorway of Room 34, snatched a boot from the mat, and thrust it beneath my cape.

I hurried down the service staircase, exited through the luggage door into the autumn morning, and walked briskly into the nearest alley off the Strand. With trembling fingers, I drew the boot from beneath my cloak.

A roar of choked, impotent fury burst from my throat!

It was a brand-new tan boot! The polished calfskin was stiff, pristine, and unstained by a single drop of rain or perspiration! The fool of a Canadian had purchased it in London only the day before and had put it out to be polished for the first time!

An unworn boot! It was as useless to my hound as a lump of wood! A bloodhound cannot hunt an abstract silhouette of tanned leather; it requires the pungent, acidic odour of human sweat, the oily secretions of living skin ground into the lining by days of vigorous walking!

My teeth ground together in bitter frustration. The maid’s stupidity had foiled me. But I could not abandon the chase. Sir Henry would soon emerge for breakfast; I would take up my post outside the hotel, trail him into the city, and discover who was advising him and what steps he intended to take next!""",
        "content_cn": """十月十二日傍晚，当我勘察完河岸街的诺森伯兰旅馆返回圣约翰伍德的寓所时，一推开起居室的房门，赫然撞见贝丽尔正以一种做贼心虚的恐慌姿态蜷缩在壁炉前的地毯上。在她身旁，扔着一份被修甲小剪刀剪得千疮百孔的昨日《泰晤士报》，头版社论上布满了犬牙差互的方形窟窿，而那把小巧弯曲的剪刀还被她死死攥在颤抖的指缝中。

我的目光瞬间扫过了红木桌面上摆放的浆糊瓶，以及散落的零星铅字碎纸屑。

一声野兽般的暴怒咒骂从我牙缝中喷涌而出！我两步跨越房间，一把揪住她乌黑的长发，硬生生将她整个人从地毯上扯跪起来。

‘你干了什么，你这个吃里扒外的贱人？！’我厉声咆哮，晃得她牙齿咯咯作响。

‘我警告了他！’她在滂沱的泪水中绝望地哭喊道，‘我把剪下来的字贴在信封上，投进了查令十字街的邮筒！我警告他永远别踏足达特穆尔荒原半步！杰克，我们的灵魂承受不起再背负一条人命的万丈诅咒了！你想打就打，想杀就杀吧，但信件已然落入了邮政系统，你休想追回来了！’

一股毁天灭地的狂暴杀机险些令我当场掐断她的脖颈。我狠狠一掌将她抽翻在沙发上，撞得她肩膀一片青紫。这个成事不足败事有余的蠢妇！倘若亨利爵士被这封荒诞的匿名拼贴信吓破了胆，连夜卷铺盖逃回加拿大荒野，那七十四万英镑的滔天富贵便将永远同我擦肩而过！

形势已然万分火急，绝无半秒钟可以虚耗。我的退路已被彻底切断。为了防止这个年轻男爵脱钩逃窜，我必须立刻拿到将他碎尸万段的最关键道具：一件吸饱了他活人体味、足以引导恶兽追杀万里的贴身物件！

次日清晨六点整，我换上一袭深色因弗内斯斗篷，戴上深色墨镜，趁着清晨旅客结账离店的纷乱人潮大摇大摆迈入了诺森伯兰旅馆的大堂。我踩着后楼梯轻手轻脚摸上了二楼长廊——亨利爵士入驻的34号套房门外。一名睡眼惺忪的爱尔兰女仆正拿着长柄笤帚清扫地毯。

我悄然闪身立在她身侧，嗓音压得极低，展现出管家特有的体面谦恭，同时顺手将半枚金光闪闪的金镑滑入了她的围裙口袋。

‘好姑娘，’我微笑着温言道，‘34号房间的那位加拿大贵客吩咐我，替他将门外的一只皮靴送往河岸街的鞋匠铺调整鞋跟钢片。他还在熟睡，靴子就放在门外地垫上。把其中一只交给我，这枚金币便是你的辛苦费。’

女仆的眼珠子在见到金币的一刹那瞬间放光。她敏捷地溜到34号门前，抄起地垫上的一只皮靴便塞入了我的斗篷底下。

我顺着后门安全通道疾步溜出旅馆，踏入了清晨喧嚣的伦敦街头，一头扎入了河岸街转角的一条僻静小巷。在狂乱的心跳中，我迫不及待地将皮靴掏出斗篷。

然而，一声因极度暴怒而走调的嘶哑咆哮瞬间从我喉管中炸裂！

那竟然是一只崭新锃亮、散发着生牛皮气息的黄褐色新皮靴！坚硬挺括的牛皮一尘不染，鞋底甚至连一粒凡间的尘埃都未曾沾染！那个愚蠢的加拿大土包子昨天刚在伦敦的商铺里买下它，昨夜是第一次将它摆出门外打油！

一双毫无体味的新靴子！这对于我那头依赖嗅觉追踪的恶犬而言，简直形同无用的一块木头！寻血猎犬绝不可能凭借毫无生命的鞣制皮革去追踪活人——它需要的是长期步行踩踏压入鞋底内衬的酸性汗液，是活人毛孔深处分泌出的浓烈体脂与热血气息！

我的牙齿咬得咯咯作响。那个蠢笨女仆的盲目彻底打乱了我的计划。但我绝不能放弃追踪。亨利爵士很快便会下楼用餐，我必须守在旅馆门外暗中盯梢，查清究竟何人在为他出谋划策，查清他下一步的动向！"""
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
            "Sherlock Holmes spots him; Stapleton escapes and brazenly uses Holmes’s own name",
        ],
        "clues_cn": [
            "斯台普吞贴上假黑胡子、戴上墨镜雇佣2704号双轮马车在摄政街尾随爵士",
            "在与歇洛克·福尔摩斯目光凌空撞击的瞬间果断策马飞驰逃逸，并傲慢挑衅地假借名侦探之名脱身",
        ],
        "choices_en": [
            {"id": "s_ch4_p2_c1", "text": "Return to the hotel corridor to steal Sir Henry’s worn black boot and flee to Devon.", "target": "stapleton_ch05_black_boot"},
            {"id": "s_ch4_p2_c2", "text": "[Switch POV to Sherlock Holmes] View Holmes receiving the report from cabman Clayton.", "target": "holmes_ch05_threads", "pov_switch": "holmes"},
        ],
        "choices_cn": [
            {"id": "s_ch4_p2_c1", "text": "潜回旅馆趁乱调换盗取亨利爵士踩满泥巴的旧黑皮靴，带上致命气味火速潜回达特穆尔。", "target": "stapleton_ch05_black_boot"},
            {"id": "s_ch4_p2_c2", "text": "【视角切换：歇洛克·福尔摩斯】切换至贝克街，见证名侦探在马车夫口中得知自己姓名被盗用的震怒。", "target": "holmes_ch05_threads", "pov_switch": "holmes"},
        ],
        "content_en": """I applied a thick, bushy black beard of theatrical hair to my chin and upper lip, pressed a soft slouch hat down to the bridge of my nose, and took up my station beneath the colonnade near the corner of Trafalgar Square. 

At a quarter past ten, Sir Henry Baskerville and Dr. Mortimer emerged from the hotel vestibule. They walked briskly up Cockspur Street and turned into Pall Mall, Sir Henry gesticulating with animated Canadian vigor, Mortimer clutching his gold-headed cane. I hailed a passing two-wheeled hansom cab—No. 2704, driven by a burly, red-whiskered fellow named John Clayton.

“Keep those two gentlemen ahead of you at a distance of two hundred yards,” I instructed, tossing him a half-sovereign through the trap in the roof. “Do not overtake them, and follow them wherever they lead.”

We crawled into Regent Street amidst the thick press of morning traffic. For twenty minutes, the stalk proceeded with mathematical perfection. My quarry walked along the eastern pavement, pausing occasionally to admire the shopfronts. I leaned back into the dark corner of the hansom, my pulse steady, congratulating myself upon my surveillance. Mortimer was evidently escorting the young heir to a consultation with a man of business. But who?

Suddenly, a cold shock of sheer, paralyzing horror stopped the breath in my lungs!

Walking briskly along the opposite pavement, twenty paces behind Sir Henry, were two men whose appearance struck me like a blow between the eyes. One was a sturdy, military gentleman with an upright carriage and a brown moustache—Dr. John H. Watson. And beside him, tall, gaunt, wrapped in an ulster coat, his hawk-like, aquiline profile unmistakable to any educated man in Europe, was Sherlock Holmes!

Mortimer had brought the foremost intellect in the world into the arena!

At that very fraction of a second, as though drawn by a psychic needle of danger, Holmes turned his head sharply towards the roadway. His piercing, grey eyes bored straight through the glass window of my hansom! For one dreadful, eternal heartbeat, our gazes collided across the crowded street! He had seen my face; he had recognized that the two gentlemen were being stalked!

“Drive!” I roared through the roof-trap, ramming the ferrule of my cane into the cabman’s back. “Drive like the devil to Waterloo! A full sovereign if you shake them off!”

Clayton’s whip cracked like a pistol shot over the horse’s flank! The hansom leaped forward with a violent lurch, throwing me against the cushions! We tore down Regent Street, cutting recklessly through the line of omnibuses, scattering pedestrian crossing-sweepers, with Holmes sprinting in our wake along the pavement! We careened into Waterloo Place, rocketed across Westminster Bridge through the swirling river mists, and screeched to a halt amidst the deafening roar and steam of Waterloo station.

I leaped from the cab before the wheels had ceased turning. I pulled two golden sovereigns from my purse and slapped them into Clayton’s astonished palm.

“You drove like a champion, cabby,” said I, leaning close, my mouth twisting in an insolent, mocking grin. “And if a tall, sharp-eyed gentleman should ask you who your fare was, tell him: My name is Mr. Sherlock Holmes, and don’t you forget it!”

I plunged into the roaring, soot-filled labyrinth of the railway platforms, ducked through the luggage tunnel, and emerged into the southern streets, vanishing like smoke into the London fog. 

I had cheeked the great detective to his face! I had thrown his own name in his teeth! Yet as I walked through the damp alleys, my hands were shaking with cold adrenaline. The mask of provincial obscurity was shattered. Sherlock Holmes was in the game! The contest had become a mortal duel between the finest brain of the law and the finest brain of crime!""",
        "content_cn": """我将一圈浓密黑亮的黏贴假连鬓胡须死死粘在下颚与上唇，把一顶深色软呢帽压低到鼻梁骨，在特拉法尔加广场转角处的柱廊阴影下守株待兔。

十点一刻，亨利·巴斯克维尔爵士与摩梯末医生终于并肩走出了诺森伯兰旅馆的大理石门廊。他们大步流星走上科克斯珀街，拐入苍凉壮丽的蓓尔美尔街。亨利爵士展现出加拿大年轻人特有的充沛活力，一边走一边激烈地比划着手势；摩梯末则紧紧抱着他那根失而复得的手杖。我顺手拦下了一辆正从街角慢跑而过的双轮轻便马车——车牌号2704，车夫是一个生着红胡子、名叫约翰·克莱顿的魁梧汉子。

‘远远咬住前面那两位先生，保持两百码距离，’我顺手将半枚金镑从车顶的传话天窗掷进车夫怀里，‘绝不要超车，无论他们拐进哪条街，死死跟住。’

马车缓缓驶入摄政街清晨拥挤的车流之中。在整整二十分钟的时间里，这场盯梢进行得如精密机械般严丝合缝。我的猎物走在东侧的人行道上，偶尔停下脚步端详着高档橱窗里的陈设。我将整个身躯深陷在马车阴暗的软垫角落里，脉搏平稳，暗自得意于我那毫无破绽的潜伏。摩梯末显然正在护送这位年轻男爵前往某处拜会一位至关重要的大人物。然而究竟是谁？

突然之间，一股寒彻骨髓的绝命恐惧如冰水浇头般瞬间冻结了我肺腑里的呼吸！

就在马路对面的另一侧人行道上，距离亨利爵士身后仅仅二十步之遥的地方，并肩阔步走着两位令我瞳孔骤然收紧的身影。其中一人步履沉稳如军人，留着棕色短髭——约翰·H·华生医生；而在他身侧，那个身形异常挺拔瘦削、身披长款奥斯特大氅，生着一张在全欧洲无人不晓的鹰喙般锐利侧颜的绅士，赫然正是歇洛克·福尔摩斯！

摩梯末竟然把全天下最顶尖的名侦探请上了猎杀的战场！

就在我认出他的千分之一秒内，仿佛受到了危险第六感的牵引，福尔摩斯猛然转过了头颅！他那对如出鞘冰刃般的灰色寒眸，竟穿透车流与马车玻璃窗直直刺入了我的瞳孔！在嘈杂喧嚣的人潮之中，我们的目光在半空中发生了一记惊心动魄的凌空撞击！他看见了我的假胡须；他识破了前面两位先生正处于被人暗中盯梢的死局！

‘快赶车！’我发疯般用手杖顶开天窗，手杖铁箍死死戳在车夫的后背上厉声咆哮，‘拼死赶往滑铁卢车站！甩掉他们，我多赏你一整枚金镑！’

克莱顿的长鞭在骏马背上抽出凄厉如火枪般的脆响！双轮马车伴随着剧烈的颠簸猛地窜出，将我重重甩在靠垫上！我们如同疯牛般在摄政街密集的双层公共马车与货车车流中亡命穿梭飞驰，沿街将打扫马路的清洁工逼得四散奔逃，而福尔摩斯的大氅却在后方的人行道上如猎豹般狂奔追赶！我们轰鸣着杀过滑铁卢广场，在滚滚江雾中风驰电掣般冲过威斯敏斯特大桥，刺耳地急刹在喧嚣混乱的滑铁卢车站进站口！

还没等车轮完全停稳，我便飞身跳下了车厢。我掏出两枚金光闪闪的金镑重重拍进车夫惊愕的手心里。

‘赶得漂亮，车夫，’我凑上前去，嘴角咧开一抹狂妄至极的恶毒冷笑，‘待会儿要是有个高个子、目光如电的瘦削绅士向你打听刚才坐车的是哪位大人物，你便如实回他：“老子的名字叫歇洛克·福尔摩斯，可千万给老子记牢了！”’

我一个闪身潜入了滑铁卢车站那充满煤灰与蒸汽的站台迷宫之中，顺着货运地下通道神不知鬼不觉地溜出了南门，宛如一缕青烟彻底消散在伦敦的迷雾之中。

我当面挑衅了全英国最顶尖的神探！我把他的名字当众甩在了他自己的脸上！然而当我走在阴冷的暗巷中时，我的双手却在狂涌的肾上腺素中抑制不住地微微发颤。乡野落魄学者的面具已被彻底撕破。歇洛克·福尔摩斯已然正式参战！这场角逐，已然演变成了一场全天下最顶尖的正义智脑与最冷血犯罪智囊之间的不死不休决斗！"""
    },

    # Chapter 5
    {
        "id": "stapleton_ch05_black_boot",
        "ch_idx": 4, "part": 0,
        "title_en": "Chapter 5: Three Broken Threads (Securing the Old Black Boot)",
        "title_cn": "第五章 三条断了的线索（盗取旧黑靴与遁回达特穆尔）",
        "pov": "stapleton", "type": "anchor", "anchor": "anchor_arrival_stapleton",
        "clues_en": [
            "Stapleton returns the new tan boot and successfully steals Sir Henry’s old black boot",
            "Learns Holmes declined to go to Devon, sending only Dr. Watson as bodyguard",
            "Returns triumphant to Merripit House to prepare the hound with the fatal scent",
        ],
        "clues_cn": [
            "斯台普吞悄然潜回旅馆物归原主退回新黄靴，成功盗取亨利爵士穿过、沾满烂泥的旧黑皮靴",
            "暗探获悉歇洛克·福尔摩斯借故公务缠身留守伦敦，仅派军医华生随行护送男爵",
            "怀揣浸透目标体味的绝密旧靴狂喜返回梅利琵宅邸，着手以血腥气味饲喂训练恶兽",
        ],
        "choices_en": [
            {"id": "s_ch5_c1", "text": "Take position upon the ridge overlooking the moor road to watch Sir Henry’s arrival.", "target": "stapleton_ch06_part1_arrival_watch"},
            {"id": "s_ch5_c2", "text": "[Switch POV to Dr. Watson] View Watson traveling west on the express to Devonshire.", "target": "ch06_part1_arrival", "pov_switch": "watson"},
        ],
        "choices_cn": [
            {"id": "s_ch5_c1", "text": "登上梅利琵宅邸高坡山脊隐蔽处，架起单筒望远镜等候亨利爵士与华生自伦敦入瓮。", "target": "stapleton_ch06_part1_arrival_watch"},
            {"id": "s_ch5_c2", "text": "【视角切换：约翰·H·华生】切换至西行快车车厢，体验华生护送男爵奔赴古老庄园的凝重思绪。", "target": "ch06_part1_arrival", "pov_switch": "watson"},
        ],
        "content_en": """The encounter in Regent Street would have driven an ordinary conspirator into blind panic, sending him fleeing on the first packet-boat to the Continent. But my intellect operates with the cold precision of a mathematical instrument under pressure. I knew that Holmes would spend the afternoon questioning cabman Clayton and chasing down district messenger boys. The Northumberland Hotel, having already been inspected, would be the very last place where he would anticipate my return!

At two o’clock, having shaved off my theatrical beard and discarded my tinted glasses, I walked calmly through the side entrance of the Northumberland Hotel in the guise of a quiet tourist returning to his room.

I ascended to the second-floor corridor. Sir Henry and Dr. Mortimer were absent, locked in earnest consultation in Baker Street. I slipped that useless, scentless tan boot beneath a wicker arm-chair in the corner of the corridor to divert suspicion. And then, glancing down at the mat outside Room 34, my patience was rewarded by the gods of fortune!

There, placed upon the drugget to be cleaned by the boots, stood a pair of worn black boots! The leather was supple and creased by months of walking; the heels were worn down at the outer edge; and the welts and soles were heavily caked with the dried red mud of Canadian pastures!

I snatched one of the black boots, jammed it beneath the breast of my heavy overcoat, and walked calmly down the grand staircase and out the revolving front doors into the Strand.

I had it! The master key to Sir Henry’s life! A boot soaked through with the living, pungent essence of his sweat, carrying the unique chemical signature of his bloodstream! With this talisman, my starved demon could track the Canadian baronet across twenty miles of wind-swept moor and never lose the scent for an instant!

That evening, my private surveillance outside 221B Baker Street bore a second piece of priceless fruit: a porter at Paddington station, bribed by my telegram, confirmed that Sir Henry Baskerville and Dr. Watson had booked first-class tickets for the 10:30 express to Devonshire for the following Saturday. But of Sherlock Holmes, there was no mention! The great detective was remaining behind in London to attend to other pressing cases!

I laughed aloud in the shadows of the platform until a passing constable glanced at me in suspicion. 

Holmes was not coming! He was sending his sheep to the slaughter under the sole protection of a blundering army doctor! Against Sherlock Holmes, the struggle would have been a razor-edge gamble; against Dr. John Watson, the good-natured, literal-minded veteran of Maiwand, it would be child’s play!

I returned to St. John’s Wood, packed our bags, and dragged Beryl to Paddington. We took the midnight mail train westward, and by sunrise on October 14th we were back in the bleak seclusion of Merripit House.

Without removing my traveling coat, I took the muddy black boot straight across the secret stepping-stones to the mire island. I unlocked the smelting shed. The hound sprang towards me, rattling its chains. I thrust the boot directly beneath its quivering, black nostrils.

The creature snorted, inhaled deeply, and its yellow eyes narrowed to slits of murderous recognition. A deep, slobbering whimper of bloodlust rattled in its throat. It tasted the man; it memorized the prey.

The trap was sprung. Sir Henry Baskerville was walking straight into the jaws of eternity!""",
        "content_cn": """摄政街上与福尔摩斯那电光石火的生死遭遇，换作任何平庸的阴谋家，此刻早已吓得魂飞魄散、搭乘第一班客轮逃往欧洲大陆。然而我的头脑在极度的高压之下，却展现出如精密数理仪器般令人心悸的绝对冷静。我深知福尔摩斯在接下来的整个下午，必将被车夫克莱顿的口供与全城搜寻各区信差的徒劳线索缠得焦头烂额。已被他搜查排查过的诺森伯兰旅馆，恰恰是他做梦也想不到我会杀个回马枪的安全盲区！

下午两点整，我刮掉了黏贴假黑胡子，收起了深色墨镜，以一位体面斯文的乡村游客形象，泰然自若地从侧门再次跨入了诺森伯兰旅馆的大堂。

我轻车熟路地摸上了二楼长廊。亨利爵士与摩梯末此刻正紧闭在贝克街221号B的起居室里向福尔摩斯闭门求教。我将那只毫无体味、毫无用处的崭新黄褐色皮靴顺手塞入了长廊转角的藤椅底下以扰乱视线。随后，当我低头扫向34号门外的地垫时，命运之神向我露出了最狰狞快意的微笑！

在那里，整整齐齐摆放着一双准备交给杂役刷洗的旧黑皮靴！柔软的牛皮上满布着数月跋涉留下的深深褶皱；鞋跟外侧磨损倾斜；而鞋帮与鞋底的缝隙里，厚厚凝结着一层加拿大牧场特有的干涸深红泥浆！

我闪电般抄起其中一只旧黑皮靴，塞入沉重风衣的内袋，神色从容如常地迈着优雅的步伐走下宽阔的大理石主楼梯，穿过旋转门施施然踏上了河岸街的人潮。

我拿到了！通往亨利·巴斯克维尔咽喉的最致命钥匙！一只彻底被他肉体毛孔深处分泌出的酸性汗液浸透的旧鞋，承载着他血液循环独一无二的生化气味样本！有了这件死神信物，我那头饥肠辘辘的恶魔巨兽即便在狂风肆虐的二十英里荒原上，也能在茫茫黑夜中死死咬住目标，不差分毫！

当天傍晚，我在贝克街暗中布下的眼线更是为我送来了一道价值千金的绝密战报：帕丁顿车站一位被我五金镑电报买通的行李领班确凿证实，亨利爵士与华生医生预订了本周六上午十点半开往德文郡的头等舱车票；然而在登记名单上，绝无歇洛克·福尔摩斯的半点踪影！这位名满天下的大神探，竟然声称因伦敦公务缠身留守首都，分身乏术！

在阴暗潮湿的站台角落里，我忍不住发出了快意至极的低声狂笑，甚至引来了巡警怀疑的侧目。

福尔摩斯竟然不亲自来！他竟然自以为是地将他的温顺羔羊独自送入了屠宰场，仅仅委派了一位头脑迟钝的退伍军医充当保镖！若正面与福尔摩斯那等妖孽过招，鹿死谁手尚未可知；然而若对手仅仅是约翰·H·华生那个头脑简单、四肢发达的迈旺德退伍老兵，这场狩猎简直宛如杀鸡宰鹅般轻而易举！

我返回圣约翰伍德，收拾好行囊，粗暴地扯起面如死灰的贝丽尔直奔帕丁顿车站。我们搭乘午夜的邮政快车秘密西行。十月十四日晨曦初露之际，我们已然重返达特穆尔荒原深处冷酷幽绝的梅利琵宅邸。

我甚至连身上的旅行大氅都未曾脱下，怀揣着那只沾满干泥的旧黑皮靴，踩着暗石直奔泥潭核心孤岛。我旋开工棚的重铁锁。恶犬狂暴地朝我扑来，粗重的铁链剧烈震荡。我将旧皮靴硬生生怼到了它那剧烈耸动的黑色湿润鼻孔前！

这头巨兽贪婪地深吸了一大口，两只猩红凶残的黄瞳骤然收缩为针芒状的狂暴杀机。一阵滴淌口水、狂暴难耐的嗜血呜咽在它的喉咙深处轰然炸响。它记住了这个活人的气味；它将这个猎物的血肉深烙在了兽性的核心！

地狱的天罗地网已然全面张开。亨利·巴斯克维尔，正一步步踏入我为你量身定做的万劫不复深渊！"""
    }
]
