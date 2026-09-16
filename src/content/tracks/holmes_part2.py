# src/content/tracks/holmes_part2.py
"""Sherlock Holmes Perspective: Chapters 6 through 10 (Expanded Novel-Length Edition).
Covers:
- Ch 6: Secret Deployment to Dartmoor & The Stone Hut on Black Tor
- Ch 7: The Man with the Butterfly Net & Beryl's Desperate Warning
- Ch 8: Watson's Dispatches Deciphered in the Cold Stone Lair
- Ch 9: The Midnight Candle Signal & The Figure upon the Tor
- Ch 10: The Secret of L.L. (Laura Lyons) Unveiled
"""

HOLMES_NODES_PART2 = [
    # -------------------------------------------------------------------------
    # Chapter 6: Part 1
    # -------------------------------------------------------------------------
    {
        "id": "holmes_ch06_part1_secret_departure",
        "ch_idx": 5, "part": 1,
        "title_en": "Chapter 6: Baskerville Hall (Part I: The Covert Deployment to Dartmoor)",
        "title_cn": "第六章 巴斯克维尔庄园（上：暗度陈仓与化装潜行）",
        "pov": "holmes", "type": "branch", "anchor": "anchor_arrival",
        "clues_en": [
            "Holmes watched Watson, Sir Henry, and Mortimer depart Paddington on the 10:30 express",
            "Holmes slipped out in the disguise of William Evans, surveyor, taking a slow local cattle train",
            "Dartmoor is under armed military cordon due to Selden, the Notting Hill murderer on the run",
        ],
        "clues_cn": [
            "在帕丁顿车站暗中注视华生、亨利爵士与摩梯末登上十点三十分的特快列车远赴德文郡",
            "福尔摩斯化名军械测绘员威廉·埃文斯，搭乘慢速运牛列车迂回潜入德文郡南端荒原",
            "因诺丁山杀人狂魔塞尔登从达特穆尔监狱越狱，整座荒原已被荷枪实弹的骑兵严密封锁",
        ],
        "choices_en": [
            {"id": "h_ch6_p1_c1", "text": "Scale Black Tor and establish your covert operational base in the stone hut.", "target": "holmes_ch06_part2_hut_surveillance"},
            {"id": "h_ch6_p1_c2", "text": "[Switch POV to Dr. Watson] See Sir Henry and Watson arrive at the gloomy Hall.", "target": "ch06_part1_arrival", "pov_switch": "watson"},
        ],
        "choices_cn": [
            {"id": "h_ch6_p1_c1", "text": "攀登黑色岩岗，在史前圆形石屋据点内设立绝密前沿侦查哨所。", "target": "holmes_ch06_part2_hut_surveillance"},
            {"id": "h_ch6_p1_c2", "text": "【视角切换：约翰·H·华生】目睹亨利爵士与华生一行抵达阴森苍凉的巴斯克维尔庄园。", "target": "ch06_part1_arrival", "pov_switch": "watson"},
        ],
        "content_en": """On the morning of Saturday, the third of October, I stood beneath the soot-blackened girders of Paddington Station, leaning against a stack of luggage crates with an unlit clay pipe clenched between my teeth. I wore the coarse, grease-stained frieze jacket of a provincial mechanic, a pair of corduroy trousers caked with clay, and a rough peaked cap pulled low over my brow. Not a soul among the bustling throng of travelers and porters paid the slightest heed to the weather-worn figure in the shadows.

Fifty paces down the platform, the 10:30 express for the West of England was taking on its passengers. I watched my dear Watson hand Sir Henry’s dressing-case to the guard. Watson’s face was a study in grim, soldierly responsibility; his square jaw was set, and beneath his heavy traveling ulster I could see the distinct bulge of his service revolver resting in his hip pocket. Sir Henry stood beside him, chatting with Mortimer, his keen dark eyes taking in the bustle of London for the last time before his exile.

“Good lad, Watson,” I murmured beneath my breath as the whistle shrieked and the great green engine belched white steam towards the glass roof. “You are the visible fortress that draws the enemy’s fire. Guard him with your life, and leave the night-work to me.”

The train groaned, slipped its wheels against the iron rails, and glided smoothly out into the autumn morning.

The moment the last carriage had cleared the signal box, I slipped through the side wicket of the station and vanished into the maze of back streets. Two hours later, under my assumed name of William Evans, surveyor, I was seated in the corner of a third-class wooden smoking carriage on a slow, grinding local train bound for Exeter and the south Devon junctions.

By nightfall, the gentle green pastures of Somerset and the orchards of Devon had fallen away behind us, replaced by the grim, forbidding ramparts of the great granite plateau. The air grew sharp and thin, bearing upon its wings the damp, earthy tang of decaying vegetation and sodden peat. At every crossroad and railway bridge along the moor boundary, two armed sentries stood shivering beneath oilskin capes, their carbines glinting beneath the carriage lamps.

The guard informed me in hushed tones of the cause: Selden, the Notting Hill murderer, had broken out of the great granite prison at Princetown three days prior. A savage, bloodthirsty brute whose atrocities had revolted the nation, he had vanished into the trackless bog, hunted like a wolf by two companies of the Devonshire Regiment.

“A charming reception for young Sir Henry,” I thought with a grim smile as I shouldered my canvas rucksack at the lonely junction of Newton Abbot. “An escaped ghoul upon the rocks, an ancestral demon in the mire, and a living assassin holding the strings!”

I struck out on foot into the teeth of a whistling autumn gale. In the darkness, the great moor rose up before me like the petrified billows of a prehistoric sea—vast, melancholy, and boundless. Miles of black heather stretched into the fog, broken only by the eerie, menacing silhouettes of the granite tors rising like jagged black teeth against the stormy sky. Here, upon this ancient battleground, the duel would be fought to the death.""",
        "content_cn": """十月三日，星期六的清晨。我斜倚在帕丁顿车站那被机车煤烟熏得乌黑的铸铁柱旁，嘴里叼着一截未点燃的粗陶烟斗。我此时身上套着一件沾满机油与泥渍的草黄色粗呢短大衣，下身是一条沾满硬泥的宽腿灯芯绒长裤，头顶扣着一顶破旧的宽檐鸭舌帽，帽檐压得极低，遮住了我大半张面庞。在站台上摩肩接踵的旅客、水手与搬运工洪流中，没有一个人会多看这个平庸邋遢的乡下勘测工第二眼。

在我前方五十码外的中央站台上，开往英格兰西部的十点三十分早班特快列车正喷吐着白色的蒸汽等待启程。我静静注视着我那忠诚的华生医生，正极其沉稳地将亨利爵士的皮面旅行手提箱递给列车员。华生的面孔宛如一尊经过战火洗礼的坚毅军人雕像：他的下颌紧绷成两道坚毅的冷线，而在他厚重的旅行大衣右侧口袋下方，赫然隆起一块沉甸甸的硬块——那是他擦拭得一尘不染、压满实弹的军用阿达姆斯左轮手枪！亨利爵士正精神抖擞地与摩梯末谈笑着，他那双机敏的黑眼睛最后环视了一圈伦敦繁华的车站，旋即大步踏上了通往险境的车厢。

‘好样的，华生，’在机车发出一声凄厉悠长的汽笛长鸣、喷吐着漫天滚滚白烟缓缓起步时，我对着那面渐行渐远的车窗玻璃，在心底低声耳语，‘你将是一座坚不可摧的明面堡垒，负责把潜伏恶敌的所有视线与杀机死死吸引在自己身上；而潜行在暗夜里的致命反击，就彻底交由我来执行吧！’

沉重的列车车轮在铁轨上发出沉闷刺耳的摩擦声，旋即加快速度，平稳地滑出了站台，消失在十月阴郁的晨光之中。

尾节车厢刚驶过调度道岔，我便如同幽灵般迅速拐出车站侧门的狭窄便道，转瞬湮没在帕丁顿后街的小巷迷宫里。两个小时后，我手持‘军械调查局地形测绘员威廉·埃文斯’的合法证件，已经端坐在了一列由伦敦发往埃克塞特方向的慢速牲畜混编列车的硬木三等车厢角落里。

待到夜幕降临时，萨默塞特郡柔美碧绿的起伏丘陵与德文郡丰茂的苹果园早已被列车抛在身后，取而代之的，是拔地而起、阴森险峻的花岗岩达特荒原高地。车窗外的空气骤然变得稀薄而冰寒彻骨，风中夹杂着陈年腐烂泥炭与湿冷植被特有的刺鼻土腥气。在荒原边缘的每一处铁路道口与石桥旁，赫然伫立着两名全副武装的郡警与步兵哨兵，他们裹着油布斗篷在凄风冷雨中瑟瑟发抖，手中的马枪在列车车灯的反射下闪烁着森冷的寒芒。

列车员在查票时，用战战兢兢的耳语向我道出了实情：就在三天前，关押在普林斯敦花岗岩巨石监狱里的诺丁山凶杀狂魔塞尔登，在暴风雨中成功越狱了！那个手段残暴如禽兽、其血腥恶行曾让全伦敦为之震悚的恶魔，如今正如困兽般潜伏在这片浩瀚无垠的花岗岩沼泽荒野之中，引得德文郡步兵团的两个整编连正端着刺刀在山岩间四处搜山捕猎。

‘这对年轻的亨利爵士而言，可真是一场别开生面的德文郡欢迎礼，’在牛顿阿伯特荒凉偏僻的岔道小站上，我将沉甸甸的帆布帆布背包甩在肩头，嘴角勾勒出一抹冰冷而残酷的微笑，‘荒岩间游荡着越狱的人形食尸鬼，死沼里蛰伏着古老相传的地狱恶兽，而在这一切的幕后，却端坐着一位手握提线、冷静自若的现代提线木偶大师！’

我压低帽檐，逆着迎面如刀割般刺骨的深秋荒原狂风，徒步踏入了茫茫无际的黑暗荒野。夜色下，广袤雄浑的达特荒原宛如一片凝固在史前时代的黑色狂涛巨浪，苍凉、死寂、无边无际。数英里连绵不绝的黑石楠苔原在翻滚的夜雾中无限蔓延，唯有一座座突兀孤绝、宛如巨兽利齿般直刺阴沉苍穹的花岗岩岩岗（Tor），在暴风雨的前奏中投下狰狞可怖的庞大剪影。

在这片亘古未变的蛮荒决斗场上，一场关乎生死与智谋的终极猎杀，终于拉开了血腥的帷幕！"""
    },

    # -------------------------------------------------------------------------
    # Chapter 6: Part 2
    # -------------------------------------------------------------------------
    {
        "id": "holmes_ch06_part2_hut_surveillance",
        "ch_idx": 5, "part": 2,
        "title_en": "Chapter 6: Baskerville Hall (Part II: The Telescope on Black Tor)",
        "title_cn": "第六章 巴斯克维尔庄园（下：黑色岩岗上的鹰隼视线）",
        "pov": "holmes", "type": "branch", "anchor": None,
        "clues_en": [
            "Prehistoric circular granite stone hut on Black Tor serves as Holmes’s covert fortress",
            "Messenger Cartwright delivers bread, tinned tongue, and clean water under cover of darkness",
            "High-powered brass telescope provides unobstructed surveillance of Baskerville Hall and Merripit House",
        ],
        "clues_cn": [
            "黑色岩岗顶峰的史前凯尔特双环花岗岩石屋，被改造为绝密隐蔽的战术观察据点",
            "忠诚机警的差役卡特赖特借黑夜掩护，隔日从库姆·特雷西村秘密送来面包、罐头与净水",
            "大倍率黄铜折射式望远镜清晰俯瞰巴斯克维尔庄园全景、水松夹道及格林盆泥潭边缘的梅立坪宅邸",
        ],
        "choices_en": [
            {"id": "h_ch6_p2_c1", "text": "Train your telescope upon the Grimpen Mire to monitor Jack Stapleton’s movements.", "target": "holmes_ch07_part1_naturalist"},
            {"id": "h_ch6_p2_c2", "text": "[Switch POV to Jack Stapleton] Discover how Stapleton watched the carriage arrive.", "target": "stapleton_ch06_part1_arrival_watch", "pov_switch": "stapleton"},
        ],
        "choices_cn": [
            {"id": "h_ch6_p2_c1", "text": "将高倍望远镜对准大格林盆泥潭，锁定博物学者斯台普吞的异常巡游轨迹。", "target": "holmes_ch07_part1_naturalist"},
            {"id": "h_ch6_p2_c2", "text": "【视角切换：杰克·斯台普吞】窥视反派如何站在沼地高处冷眼注视车队入驻庄园。", "target": "stapleton_ch06_part1_arrival_watch", "pov_switch": "stapleton"},
        ],
        "content_en": """The wind upon the summit of Black Tor was like an invisible wall of ice. It howled through the clefts of the granite crags, screaming across the heather with the fury of a pack of wolves. Yet inside the ancient, circular stone hut which I had chosen for my redoubt, the air was dry, still, and sheltered.

These prehistoric dwellings, erected by the primitive Iberians thousands of years before the Roman legions set foot in Britain, are masterpieces of primitive engineering. The rough granite blocks, fitted without mortar, have withstood the Atlantic gales of thirty centuries. The low doorway, scarcely four feet in height, faces south-east away from the prevailing storms. In the center of the earthen floor, beneath an opening in the conical stone roof, I had scraped clean a circle of flat stones to serve as a hearth. For bedding, I had gathered thick armfuls of dried bracken and mountain heather, covering them with a waterproof groundsheet and a heavy seaman’s blanket.

Here, in the very heart of the wilderness, I had established my headquarters.

At dawn, a faint, rhythmic whistle—like the call of a curlew—echoed from the gully beneath the tor. I stepped to the low lintel and peered out into the grey mist. A small, agile figure scrambled nimbly up the rock chimney, clutching a wicker hamper beneath his arm. It was young Cartwright, the sharpest lad in the district messenger service, whom I had stationed at an obscure tavern in the distant hamlet of Coombe Tracey.

“Everything quiet, Mr. Evans?” the boy panted, ducking his cap as he squeezed through the low entrance.

“Perfectly quiet, Cartwright,” I said, taking the hamper from his grasp. “What have you brought?”

“A fresh loaf of cottage bread, sir, two tins of preserved tongue, a pound of coffee, and half a dozen candles. And here is a packet of letters from Baker Street that arrived by the morning post.”

“Good boy. And has anyone in the village questioned your presence?”

“Not a soul, sir! I tell ’em I’m an artist’s apprentice sketching wildflowers on the moor for a London botanical shop. They think I’m a harmless simpleton.”

“Admirable. Keep that character, Cartwright. Return to Coombe Tracey by the sheep-paths along the river. If any letters or telegrams arrive from Dr. Watson, bring them to me after sunset under cover of the dark.”

When the boy had slipped away down the gully, I climbed to the natural stone platform on the southern face of the tor. Concealing my body behind two upright slabs of lichen-covered granite, I set up my high-powered brass field telescope upon its folding tripod and adjusted the brass focus-ring with steady fingers.

The whole panorama of Dartmoor leaped into startling, microscopic clarity.

Two miles to the south-east, nestled in a dense hollow of ancient oaks, rose the twin castellated towers and dark slate roofs of Baskerville Hall. With a quarter-turn of the screw, I brought the famous Yew Alley into focus: a long, dark, green tunnel terminating in the fateful wicket gate where Sir Charles had met his doom. I could see the gravel path where Watson and Sir Henry now walked side by side, their silhouettes tiny as chessmen, yet every gesture of Watson’s arm discernible as he pointed across the grounds.

I swung the barrel three miles eastward, traversing the vast, trembling expanse of the Great Grimpen Mire. Even through the brass tube, the swamp possessed an evil, treacherous beauty: undulating patches of emerald-green slime, glittering pools of black, stagnant water, and jagged ridges of dark peat. And perched upon the very brink of that watery graveyard, surrounded by a few stunted fir trees, sat Merripit House—an austere, whitewashed stone cottage that seemed to shudder in the moorland gale.

As I watched, the front door of Merripit House opened. A man stepped out into the autumn sunshine, carrying a long, slender pole in his right hand and a green butterfly net over his shoulder.

I locked the brass clamp and leaned into the eyepiece. “Jack Stapleton,” I whispered, my pulse steadying into ice. “Let us see what kind of specimens you collect in the heart of the dead bog.”""",
        "content_cn": """黑色岩岗（Black Tor）峰顶的花岗岩峭壁上，呼啸的狂风如同一道冰冷刺骨的无形巨墙。暴风雨穿过山岩间狭窄的裂隙，发出阵阵令人毛骨悚然的凄厉尖啸，如同一整群饥肠辘辘的恶狼正贴着石楠丛疯狂奔嚎。然而，在我选作秘密前沿指挥所的这座史前古老圆形石屋深处，空气却显得极其干燥、死寂而隐蔽。

这些由数千年前的古代伊比利亚土著居民留下的蜂巢状石构建筑，堪称原始工程学的奇迹。未经任何石灰砂浆粘合的花岗岩巨石相互咬合借力，竟在三千年的大西洋海风侵蚀下岿然不动。不到四英尺高的低矮门洞朝向东南，完美避开了肆虐的西北主风向。在坚硬泥土地面的正中心、石质圆锥形屋顶的排烟口正下方，我清理出了一圈平整的花岗岩石块作为临时炉灶；而在干燥的石壁内侧，我铺垫了厚达一英尺的干燥羊齿草与紫石楠枝桠，上覆军用防水帆布与深蓝色厚羊毛毯，构筑成一张温暖结实的行军卧榻。

在这片寸草不生、鸟兽绝迹的蛮荒死地腹心，我稳稳立下了我的指挥中枢。

拂晓时分，石屋下方险峻的花岗岩倒石堆深处，忽然传来了一声惟妙惟肖的麻鹬清脆鸟鸣——那是我们约定的联络暗号。我猫着腰钻出低矮的门洞，警惕地穿透晨雾向下俯瞰。只见一个瘦小敏捷的身影正宛如岩羊般在乱石嶙峋的山脊上飞攀而上，臂弯下紧紧夹着一只沉甸甸的柳条野餐篮。那正是年轻的卡特赖特——伦敦地区差役局里最机警可靠的机灵鬼，此刻正被我秘密安排潜伏在数英里外库姆·特雷西村的一家偏僻乡间小客栈里。

‘一切正常吗，埃文斯先生？’少年气喘吁吁地钻进低矮的石门，摘下鸭舌帽，满头大汗地将柳条篮递了过来。

‘寂静如坟，卡特赖特，’我接过篮子，熟练地翻检着补给，‘今天带了什么来？’

‘一大条刚烤出炉的乡村粗麦面包，先生；两罐咸牛肉罐头；一磅烘焙咖啡豆；半打牛油蜡烛；还有今天一早通过伦敦早班快信转寄到乡下邮局的几封贝克街信函。’

‘做得好。村里有人起疑吗？’

‘连半个怀疑的影子都没有，先生！我对客栈掌柜说我是伦敦一家植物标本商店老板雇来的学徒画工，专门在荒原上临摹罕见的石楠花标本。他们都把我当成一个成天漫山遍野乱跑的傻小子！’

‘很好。务必咬死这个身份，卡特赖特。回去时沿着河谷两岸的羊肠小道绕行。如果有任何华生医生发往贝克街被转寄过来的加密信件或电报，务必在天黑之后借着夜色送上岩岗。’

待少年的身影彻底隐没在下方的山谷浓雾中后，我手脚并用地攀上了石屋背风面一处天然的花岗岩平顶观察哨。我将整个身躯紧紧贴伏在两块布满斑驳地衣的古老巨石掩体后，从皮套中取出那具长达三英尺的大倍率黄铜折射式野战望远镜，将其稳固地架设在三脚架上，指尖沉稳地旋转着调节焦距的滚花螺母。

整座达特荒原的壮阔全景，在镜头中骤然被拉伸出令人屏息的微观纤毫！

向东南方向望去，相距两英里外的一片苍老古橡树浓密凹地中，巴斯克维尔庄园那对耸立的都铎风格雉堞双塔与幽暗的石板坡屋顶，清晰得宛如近在咫尺。随着望远镜微调螺栓的缓缓旋动，那条臭名昭著的水松夹道尽收眼底：那是一道由两排阴森浓密的水松巨树围拢而成的黑暗狭长隧道，其尽头便是查尔斯爵士暴毙的那扇简陋木质栅门。在庄园主楼前的碎石台阶上，华生正与年轻的亨利爵士并肩而行。他们小巧的身影在镜头中宛如棋盘上的棋子，然而华生指向远方石楠荒原时手势的每一个动作细节，都毫无遗漏地映照在我的晶状体上。

紧接着，我将黄铜镜筒向东缓缓平移了整整三英里，镜头横切过广袤翻滚、散发着死亡恶臭的大格林盆泥潭。即便隔着数层厚重的水晶镜片，那片巨大的食人沼泽依旧散发着一种令人毛骨悚然的妖异魅力：成片泛着翡翠般诱人光泽的剧毒水藓、一处处在日光下泛着死光的幽黑死水潭、以及起伏如黑色伤疤般的古老泥炭岩脊。而在那片吞噬一切的泥沼西侧边缘，在几棵被狂风扭曲成怪异姿态的枯萎矮松环抱之下，孤零零地耸立着梅立坪宅邸——那座通体涂着惨白石灰、在荒原烈风中瑟瑟发抖的阴森石砌小楼。

就在此时，梅立坪宅邸那扇紧闭的漆黑大门，悄无声息地推开了。一个身材精瘦修长的男子迈步走入了秋日的惨白阳光下。他的右手中握着一根长达数英尺的坚硬竹杖，左肩上则轻巧地斜挎着一只醒目的绿色长柄捕蝶网。

我迅速拧紧望远镜的三脚架锁扣，单眼深深陷入了橡胶目镜之中。‘杰克·斯台普吞，’我屏住呼吸，声音冷酷得如同结霜的坚冰，‘就让我好好瞧瞧，你在这片万劫不复的死亡死沼深处，究竟在搜集何种惊世骇俗的“生物标本”吧！’"""
    },

    # -------------------------------------------------------------------------
    # Chapter 7: Part 1
    # -------------------------------------------------------------------------
    {
        "id": "holmes_ch07_part1_naturalist",
        "ch_idx": 6, "part": 1,
        "title_en": "Chapter 7: The Stapletons of Merripit House (Part I: The Man with the Net)",
        "title_cn": "第七章 梅立坪的斯台普吞兄妹（上：手持捕蝶网的伪装者）",
        "pov": "holmes", "type": "branch", "anchor": None,
        "clues_en": [
            "Stapleton navigated the deadly Great Grimpen Mire with uncanny agility using hidden bog paths",
            "A moor pony was swallowed alive by the quagmire before Stapleton’s callous, indifferent gaze",
            "Stapleton intercepted Watson upon the moor road to probe his connection with Sherlock Holmes",
        ],
        "clues_cn": [
            "斯台普吞踩着深埋在泥炭下方的秘密枯柳木桩，在吞噬一切的大格林盆泥潭中如履平地",
            "一匹误入沼泽的荒原矮种野马在挣扎中被烂泥活活吞噬，斯台普吞冷眼旁观，神情冷酷漠然",
            "斯台普吞主动在荒原岔路口拦截华生，极力刺探其与伦敦神探歇洛克·福尔摩斯的秘密关联",
        ],
        "choices_en": [
            {"id": "h_ch7_p1_c1", "text": "Observe Beryl Stapleton’s frantic attempt to intercept and warn Watson.", "target": "holmes_ch07_part2_beryl_warning"},
            {"id": "h_ch7_p1_c2", "text": "[Switch POV to Jack Stapleton] Experience Stapleton’s calculated performance as the innocent naturalist.", "target": "stapleton_ch07_part1_naturalist_act", "pov_switch": "stapleton"},
        ],
        "choices_cn": [
            {"id": "h_ch7_p1_c1", "text": "调转镜头，紧盯贝丽尔·斯台普吞冒死拦截华生、发出绝望警告的惊险一幕。", "target": "holmes_ch07_part2_beryl_warning"},
            {"id": "h_ch7_p1_c2", "text": "【视角切换：杰克·斯台普吞】窥视凶手如何游刃有余地向华生假扮纯良无害的昆虫学家。", "target": "stapleton_ch07_part1_naturalist_act", "pov_switch": "stapleton"},
        ],
        "content_en": """Through the crystal optics of the brass telescope, Jack Stapleton was under constant, merciless dissection.

He was a small, slim, clean-shaven man of about thirty-five years, with straw-coloured hair and a narrow, ferret-like jaw. He wore a prim suit of grey flannel and a straw hat that gave him the ridiculous air of an overgrown schoolboy. Yet as I observed his movements across the treacherous margin of the Great Grimpen Mire, every trace of absurdity vanished, replaced by a cold, calculating awe.

The man walked with the effortless, springy tread of a panther. Where another man would have sunk to his hips in the treacherous green slime, Stapleton skipped from one tiny tussock of dry rushes to another with uncanny certainty. He carried a ten-foot pole with a barbed iron ferrule, testing the mire ahead of him, stepping only where some submerged, invisible pathway afforded purchase beneath the mud.

Suddenly, an agonizing shriek echoed across the waste.

Half a mile to the east of his position, a wild moor pony—a handsome dun creature that had wandered from the higher crags—had stepped onto a patch of bright emerald moss. In an instant, the crust gave way beneath its hooves. The pony plunged into the black peat slurry, thrashing its neck in frenzied terror, screaming with a sound so horribly human that it made my blood run cold. Its eyes rolled white; its nostrils flared; and then, with sickening, relentless suction, the mire closed over its flailing flanks, its arched neck, its tossing mane, until within sixty seconds nothing remained but a few oily green bubbles bursting upon the slime!

I lowered the glass for a fraction of a second, my jaw clenched tight. Then I swung the barrel back to Stapleton.

He had not flinched. He had not even broken his stride. He stood upon a dry ridge of peat, holding his butterfly net, watching the death agony of that noble animal with the mild, detached amusement of a schoolboy observing a beetle kicking on a pin!

“That,” I muttered to the granite stones beneath me, “is our man. A creature capable of watching agony with a smile; a man devoid of the common instincts of humanity; an intellectual monster of the first water.”

Presently, my telescope caught a second figure striding along the post-road from Baskerville Hall. It was Watson, clad in his brown tweed suit, his stout ash stick swinging in his hand. He had left Sir Henry at the Hall and had walked out towards the moor to reconnoitre the countryside.

Stapleton saw him instantly. The transformation was startling: the cold, aloof predator vanished behind a mask of cheerful, boyish amiability. Waving his straw hat, Stapleton bounded across the heather to intercept our good doctor at the junction of the Grimpen lane.

I could not hear their words, but their pantomime was as eloquent as an open book. Stapleton bowed, introduced himself with theatrical warmth, pointed with his cane towards the distant mire, and gesticulated towards Baskerville Hall. His head cocked to one side like a bird’s, probing, questioning, testing the limits of Watson’s knowledge. And Watson—bless his honest heart!—stood upright, hands behind his back, replying with that guarded, noncommittal gravity which he imagines to be the height of Machiavellian diplomacy.

Yet even as they talked, a sudden flutter of white linen on the distant moor track caught my attention. A woman had emerged from the gate of Merripit House, running frantically along the heather towards them!""",
        "content_cn": """透过高倍折射望远镜的水晶透镜，杰克·斯台普吞的一举一动都处于最无情、最严密的法医学解剖之下。

这是一个身材矮小精干、面部刮得干干净净的男子，年岁约莫三十五六上下。他生着一头泛黄干枯的浅金发，下巴狭窄尖削，宛如一只嗅觉灵敏的雪貂。他身着一套剪裁得体的浅灰色法兰绒常服，头戴一顶有些滑稽的硬顶草帽，整个人透着一种被学究气过度浸染的私塾教员气质。然而，当我通过镜头死死凝视着他在大格林盆泥潭那片危机四伏的致命边缘起伏跳跃的身影时，所有浮于表面的滑稽感在一瞬间荡然无存，取而代之的，是一种深入脊髓的冰冷战栗！

这个男人的步伐轻盈敏捷得近乎不可思议，宛如一头在沼泽深处悄然潜行的美洲黑豹！寻常成年男子若是踏入那片鲜艳翠绿的水生苔藓，瞬间便会被深不见底的烂泥彻底吸入没顶；然而斯台普吞却踩着极其精妙的碎步，在几丛枯黄的干芦苇苔藓墩之间从容跃进，其精准程度宛如脚下踩着一条深埋在水底的无形石阶！他手中握着一根十英尺长的带倒钩铁头探路竹竿，每迈出两步便探向泥面深处探查虚实——他深知那条穿越万劫不复泥渊的绝密死径！

突然间，一阵凄厉绝伦、撕心裂肺的狂暴惨叫声，穿透了整座荒原的死寂！

在距离斯台普吞所处位置以东约半英里处，一匹在石楠丛中觅食误入低地的德文郡野生栗毛矮种小马，踏上了一片看似娇嫩肥沃的亮绿色青苔地。刹那间，泥浆表层脆弱的浮皮轰然塌陷！那匹可怜的生灵四蹄深陷进黑色的泥炭浆液中，在濒死的癫狂恐惧中拼命扬起脖颈，从胸腔里爆发出一种近乎人类受难时那般凄惨绝望的狂暴悲鸣！它的双眼翻白，鼻孔中喷涌出血色的粗气；紧接着，一股令人作呕、无穷无尽的恐怖黏滞吸力从深不见底的泥渊深处狂暴涌出，无情地拉扯着它的前胸、鬃毛、以及扬起的马头，在短短不到六十秒的时间里，整匹骏马便被彻底拖入了淤泥地底，水面上唯余几个泛着幽绿油光的沼气水泡在咕嘟咕嘟地破裂！

我闭上单眼，从目镜前挪开身子，后槽牙咬得咯咯作响。旋即，我再次将镜头精准地压回了斯台普吞的脸上。

他甚至连眼皮都没有眨一下！他甚至连前行的步伐都未曾出现半秒的停顿！他就那样闲适地伫立在一道坚硬干燥的泥炭岩脊上，左手轻搭着那只绿色的捕蝶网，面带微笑、冷酷而抽离地注视着那匹高贵动物在死亡泥淖中受尽折磨的绝命挣扎，其神情宛如一个残忍顽劣的幼童在百无聊赖地端详着一只被钢针钉在软木上的金龟子！

‘就是他，’我对着身下冰冷死寂的花岗岩峭壁发出了低沉的宣判，‘这就是我们的死敌。一个能够微笑着欣赏生命痛苦消亡的恶魔；一个被彻底剥离了人类同理心与道德底线的怪物；一个货真价实、登峰造极的高智商天生罪犯！’

就在这时，镜头边缘忽然扫到了第二道沿着巴斯克维尔庄园驿道大步走来的身影。那是华生！他身披那件深褐色的粗花呢大衣，手中那根沉重的白蜡木手杖在身侧有力地挥动着。他显然是安顿好了亨利爵士，独自一人外出勘察庄园周边的地形环境。

斯台普吞几乎在同一秒钟敏锐地捕捉到了华生的脚步声。镜头中凶手的面部表情发生了一场令人惊骇的剧变：方才那副冷血嗜杀的残暴面孔如潮水般退去，转瞬被换上了一副洋溢着少年般热情天真、纯良无害的学者笑容！他脱下头上的草帽热情地在半空中挥舞着，迈着欢快的步伐穿过石楠丛，在通往格林盆村的岔路口主动截住了我们那位忠厚老实的医生！

我听不见他们交谈的字句，然而两人肢体语言的交锋却如展开的书页般一览无余。斯台普吞极具戏剧性地夸张欠身行礼，自我介绍，手中的竹竿夸张地指向远方的食人泥潭，又时不时指向巴斯克维尔庄园的高塔。他的脑袋如警觉的画眉般微微倾斜，每一个看似热情的发问，都在极其阴险地探查华生所掌握的实情底线！而华生——愿上帝保佑他的忠直灵魂！——正双手反剪在背后，下巴微扬，用那种他自以为极度老练圆融、实则一览无余的军人庄重辞令应付着对方的盘剥。

然而，正当他们二人伫立交谈之际，远方泥潭驿道上一闪而过的白色裙裾，骤然扯动了我紧绷的神经！

一名身披黑色披肩、长裙雪白的年轻女子，正如发疯的羚羊般推开梅立坪宅邸的大门，不顾一切地穿过石楠荒草，直奔华生所伫立的土坡狂奔而来！"""
    },

    # -------------------------------------------------------------------------
    # Chapter 7: Part 2
    # -------------------------------------------------------------------------
    {
        "id": "holmes_ch07_part2_beryl_warning",
        "ch_idx": 6, "part": 2,
        "title_en": "Chapter 7: The Stapletons of Merripit House (Part II: The Desperate Warning)",
        "title_cn": "第七章 梅立坪的斯台普吞兄妹（下：荒原惊魂与绝命告诫）",
        "pov": "holmes", "type": "branch", "anchor": None,
        "clues_en": [
            "Beryl Stapleton possesses stunning, dark, foreign elegance and terrified, haunted eyes",
            "Beryl mistook Watson for Sir Henry Baskerville, begging him to flee to London instantly",
            "Holmes deduces Beryl is not Stapleton’s sister, but his terrified, coerced lawful wife",
        ],
        "clues_cn": [
            "贝丽尔·斯台普吞展现出极具异域风情的拉丁绝色容颜，但眼神中充斥着濒临崩溃的极度惊恐",
            "她误将身材端正的华生当成了新袭爵的亨利爵士，泣血哀求其立刻搭乘列车逃回伦敦保命",
            "福尔摩斯凭其面对斯台普吞时那种深植骨髓的恐惧断定：她绝非其胞妹，而是受其残酷胁迫的结发妻子",
        ],
        "choices_en": [
            {"id": "h_ch7_p2_c1", "text": "Await Watson’s written report to synthesize the movements at Baskerville Hall.", "target": "holmes_ch08_watson_report"},
            {"id": "h_ch7_p2_c2", "text": "[Switch POV to Jack Stapleton] Discover how Stapleton neutralized Beryl’s blunder.", "target": "stapleton_ch07_part2_beryl_blunder", "pov_switch": "stapleton"},
        ],
        "choices_cn": [
            {"id": "h_ch7_p2_c1", "text": "静候卡特赖特送抵华生从庄园发出的亲笔密报，全盘推演巴斯克维尔宅邸动向。", "target": "holmes_ch08_watson_report"},
            {"id": "h_ch7_p2_c2", "text": "【视角切换：杰克·斯台普吞】窥视反派如何以甜言蜜语掩盖破绽，并对妻子施以恐怖惩戒。", "target": "stapleton_ch07_part2_beryl_blunder", "pov_switch": "stapleton"},
        ],
        "content_en": """I adjusted the focus-screw until the lens brought the approaching woman into vivid, razor-sharp magnification.

She was an extraordinarily beautiful woman, of a type as alien to the fair-skinned Saxon folk of Devonshire as could well be imagined. Slim, tall, and elegant, she possessed a proud, olive-tinted oval face, rich dark coils of hair, and enormous, expressive eyes that burned with feverish intensity. Yet in every line of her features was stamped a terror so abject, so raw, that it made my heart contract.

Stapleton had stepped fifty yards away into a hollow of reeds, pretending to chase a moth. The moment his back was turned, the woman reached Watson’s side.

She did not walk; she lunged towards him, her bosom heaving beneath her bodice, her slender hands clutching at the sleeve of his tweed coat. Through the glass, I could see her lips moving with frantic, desperate speed.

“Go back!” her lips formed the words unmistakably. “Go straight back to London, this very night! As you value your life, never set foot upon this moor again!”

Watson, completely taken aback by this sudden apparition of beauty and panic, stared at her in utter bewilderment. He raised his hat, attempting to introduce himself, but she cut him off with an impassioned gesture, glancing frantically over her shoulder towards the hollow where her supposed brother had disappeared.

“You must go!” her face contorted with agony. “Sir Henry, I beg of you upon my knees—hush, he is coming! Say nothing, on your life, say nothing!”

At that instant, Stapleton popped up over the bank of the hollow, his butterfly net trailing behind him.

The reaction of the woman was a revelation that gave me the master-key to the entire conspiracy.

Had she been his sister, a sudden interruption might have caused a blush, a start of surprise, or an embarrassed laugh. But what I witnessed through the lens was the reaction of a terrified captive before her torturer. Her eyes dilated with sheer, naked horror. Her head snapped down; her hands fell to her sides as though paralyzed; and her whole body seemed to shrink, trembling in every limb, as Stapleton sauntered towards them with an easy, mocking smile upon his lips!

“Ah!” I breathed aloud against the cold brass tube. “The veil is torn, Jack Stapleton! That is not a sister’s dread of an eccentric brother. That is the helpless, broken submission of a battered wife!”

I followed the pantomime as Stapleton engaged Watson in conversation, lightly introducing his “sister” Beryl, his voice evidently charming and smooth, while Beryl stood rigid beside him, her pale lips pressed tight, her dark eyes fixed upon the ground. Watson, polite as ever, bowed to the lady, accepted an invitation to take tea at Merripit House, and presently took his leave, striding back along the post-road towards Baskerville Hall.

I did not take my eye from the lens until the two figures at Merripit House had re-entered the cottage. The moment the heavy oak door closed behind them, I caught a brief, sickening glimpse through the parlour window: Stapleton’s hand shot out and gripped the woman’s wrist with savage, bruising force, dragging her violently towards the staircase!

“Hold on, madam,” I whispered, lowering the telescope into its leather case. “Your ordeal is nearing its end. Your brutal husband has set himself against Sherlock Holmes, and the day of reckoning is coming upon the moor!”""",
        "content_cn": """我迅速拧动望远镜的焦距旋钮，将那名自荒原小径飞奔而来的年轻女子，稳稳锁定在高倍放大镜的最中心。

那是一位美得令人窒息、甚至在整座纯朴粗粝的德文郡乡间显得格格不入的绝色丽人。与当地金发碧眼的萨克逊农家女子截然不同，她身材修长曼妙，生着一张古典高贵、带有迷人橄榄色光泽的异域鹅蛋脸。她那一头漆黑如瀑的卷曲长发在风中肆意飞舞，深邃如夜海的大眼睛里，正燃烧着一种濒临崩溃的疯狂焦灼。然而，在她那令人赞叹的惊艳面容之下，每一道肌肉线条里，都深深烙印着一种纯粹、原始、深入骨髓的极度恐惧！

恰在此刻，斯台普吞似乎为了追逐一只罕见的灰斑蛾，佯装兴奋地快步跃下了一道背风的深芦苇凹地。就在他背对着大路的这一瞬间，那名女子如旋风般扑到了华生的身侧！

她几乎不是在走，而是在扑向华生。她那白色的裙摆因剧烈的奔跑而沾满了泥浆，胸口在束胸衣下剧烈起伏，两只戴着黑蕾丝手套的纤细手掌，在极度的惶恐中死死抓住了华生粗花呢大衣的衣袖！透过高倍望远镜，我能清晰地读出她那张惨白双唇间以惊人语速吐露的每一串唇形：

‘快逃！’她的唇形清晰得如在耳畔呐喊，‘今夜立刻乘车逃回伦敦去！只要你还珍惜自己的性命，就万万不要再在这座被诅咒的荒原上停留半步！’

华生显然被这位从天而降的惊惶绝色女子彻底震懵了。他下意识地脱帽致意，正准备开口自报家门，但那名女子却以近乎绝望的急迫手势狠狠打断了他！她一边浑身战栗地回头瞟向斯台普吞消失的凹地，一边以近乎泣血的哀绝姿态死死抓着华生的手腕：

‘你必须走！亨利爵士，我跪下来求你了——嘘！他回来了！求求你，看在上帝的份上，什么都别对他说！什么都别说！’

就在那一刹那，斯台普吞手持绿色的长柄捕蝶网，脸上挂着纯良无害的学者笑容，从芦苇从后轻巧地一跃而上，重新出现在土坡之上。

紧接着发生的一幕，成为了整桩阴谋中最具决定性、彻底为我打开案件核心暗锁的启示性瞬间！

如果她当真只是他的亲生妹妹，那么在被兄长撞见自己与陌生男子秘密私语时，她的第一反应应当是面红过耳、尴尬退避、或是发出一声掩饰性的娇嗔失笑。然而，我透过镜片亲眼目睹的，却是一个备受严刑拷打的无助囚徒，在撞见冷血狱卒那一瞬间所爆发出的原始本能反应！

她的双瞳在刹那间因极度的恐惧而放大到极致！她的螓首猛地垂下，原本死死抓住华生衣袖的双手如同触电般僵死地垂落身侧，整个人仿佛在一瞬间矮了半截，全身的每一根神经都在止不住地疯狂打颤——而此时的斯台普吞，正迈着轻快的步伐，嘴角噙着一抹戏谑而残忍的冷笑，徐徐朝他们踱步而来！

‘哈！’我对着身前冰凉刺骨的黄铜镜筒，从喉咙深处吐出了一句沉重的断语，‘面具被撕碎了，杰克·斯台普吞！那绝不是一个胞妹面对怪癖兄长时的敬畏；那是一个长期遭受残酷家庭暴力与精神控制的可怜妻子，在残暴丈夫淫威下彻底被摧毁人格的绝望屈从！’

镜头紧紧追随着接下来的哑剧表演：斯台普吞极其自然熟稔地同华生寒暄搭话，微笑着引介他这位‘性情孤僻的胞妹贝丽尔’；他的语调显然温和如春风，而站在他身旁的贝丽尔却整个人僵直如石雕，惨白的嘴唇紧紧抿成一条没有血色的死线，两只美丽而惊恐的黑眸死死钉在脚下的泥土里。华生一如既往地保持着无可挑剔的英国绅士风度，向女士脱帽鞠躬，礼貌地应允了前往梅立坪宅邸做客的邀请，旋即提着手杖，大步踏上了返回巴斯克维尔庄园的驿道。

我没有将目光从目镜前移开哪怕一寸，直到那对所谓的‘兄妹’并肩步入梅立坪宅邸的大门。就在那扇厚重的黑橡木大门‘砰’的一声在身后合拢的同一瞬间，透过一楼起居室未拉窗帘的狭窄窗户，我捕捉到了极其令人发指的残暴一幕：斯台普吞的一只大手如铁箍般猛然探出，狠狠扭住那名可怜女子的纤细手腕，将她近乎粗暴地向二楼的楼梯死死拖拽而去！

‘撑住，可怜的夫人，’我徐徐将望远镜收回鹿皮镜筒，在峰顶冰冷的烈风中低声自语，‘你的苦难即将走到尽头了。你那位自作聪明的残暴丈夫，如今已经彻底撞上了歇洛克·福尔摩斯的枪口——清算罪恶的那一天，很快就要降临在这片荒原之上了！’"""
    },

    # -------------------------------------------------------------------------
    # Chapter 8
    # -------------------------------------------------------------------------
    {
        "id": "holmes_ch08_watson_report",
        "ch_idx": 7, "part": 1,
        "title_en": "Chapter 8: First Report of Dr. Watson (Dispatches Deciphered in the Hut)",
        "title_cn": "第八章 华生医生的第一份报告（石屋幽光下的绝密信函）",
        "pov": "holmes", "type": "branch", "anchor": "anchor_first_report",
        "clues_en": [
            "Watson dispatches reveal Barrymore creeping down corridors at 2 a.m. with a candle",
            "Sir Henry is pursuing an ardent courtship of Beryl Stapleton, provoking Jack Stapleton’s jealous fury",
            "Holmes identifies Stapleton’s irrational rage as that of a possessive husband, not a protective brother",
        ],
        "clues_cn": [
            "华生书信详报：管家巴里摩尔每逢凌晨两点便手持蜡烛潜行至西侧偏廊窗前，向荒原深处打出神秘光信号",
            "亨利爵士对贝丽尔·斯台普吞一见钟情并热烈求爱，引发斯台普吞近乎疯魔的狂暴干涉",
            "福尔摩斯彻底坐实推论：斯台普吞的病态占有欲绝非源自兄妹亲情，而是丈夫对私有妻子的极端控制狂乱",
        ],
        "choices_en": [
            {"id": "h_ch8_c1", "text": "Keep watch on the moor at midnight to trace the answering signal to Barrymore’s light.", "target": "holmes_ch09_part1_midnight_watch"},
            {"id": "h_ch8_c2", "text": "[Switch POV to Dr. Watson] Read Watson’s original journal dispatch from the Hall.", "target": "ch08_watson_report", "pov_switch": "watson"},
        ],
        "choices_cn": [
            {"id": "h_ch8_c1", "text": "午夜埋伏岩岗顶峰，追踪与巴里摩尔烛火相互呼应的荒原回应光号。", "target": "holmes_ch09_part1_midnight_watch"},
            {"id": "h_ch8_c2", "text": "【视角切换：约翰·H·华生】阅读华生在巴斯克维尔庄园壁炉旁写下的原汁原味的长篇第一纪实报告。", "target": "ch08_watson_report", "pov_switch": "watson"},
        ],
        "content_en": """The October gales intensified with the coming of night, hurling sheets of freezing rain against the curved granite exterior of my stone hut. Inside, sheltered behind a stack of flat peat slabs, a single tallow candle burned with a steady, yellow flame. I sat cross-legged upon my blanket, wrapped in my pea-jacket, with my blackened clay pipe clamped firmly between my teeth.

Spread out across my knee were four dense sheets of fine, thin paper, closely written in the neat, upright hand of Dr. John H. Watson.

Cartwright had brought them two hours after sunset, splashing through the sodden heather like an otter. The boy was now snoring peacefully in the corner of the hut, curled like a hound in a pile of dry bracken.

I smoothed out the first page, my eyes dancing with satisfaction.

“Capital, Watson!” I murmured aloud. “Admirable fellow! He has kept his eyes open, and his pen does not spare the ink.”

Watson’s dispatch was a masterly digest of the situation at Baskerville Hall. With his customary fidelity to fact, he recorded every incident of his first week upon the moor:

Item One: The escaped convict, Selden. The military cordon had failed to capture him. The guards had been withdrawn, and the county authorities had concluded that the wretch had either perished in the quagmires of Grimpen Mire or had succeeded in reaching the southern seaports. Yet Watson noted a strange, uneasy tension in the household: food had disappeared from the larder, and Mrs. Barrymore’s eyes were perpetually red and swollen with weeping.

Item Two: The nightly movements of Mr. John Barrymore. Watson and Sir Henry had kept watch in the dark corridor outside the master suite. Twice, at two o’clock in the morning, the heavy, silent tread of the butler had passed their door. Holding a flickering candle in his hand, Barrymore had stolen to an empty guest chamber at the western end of the corridor. There, leaning against the window-pane, he had held the candle aloft for several minutes, staring out into the pitch-black void of the moor, as though waiting for an answering signal!

Item Three: The romance between Sir Henry and Beryl Stapleton. Young Sir Henry had fallen violently, hopelessly in love with the dark-eyed beauty of Merripit House. He visited her daily; he walked with her across the heather. But then had occurred a scene of singular violence: Sir Henry had attempted to take Beryl’s hand and embrace her on the moor road. At that instant, Jack Stapleton had burst from behind a granite boulder like a madman, his face livid with fury, his eyes blazing, screaming insults and demanding that Sir Henry unhand his sister and never dare address her again! Yet only two hours later, Stapleton had called at Baskerville Hall, apologized profusely for his ungentlemanly conduct, and invited Sir Henry to dine with them at Merripit House at the earliest opportunity.

I leaned back against the curved stone wall, a ring of blue pipe-smoke drifting up into the roof opening.

“How beautifully the pieces interlock!” I said softly to myself. “Watson is baffled by Stapleton’s conduct. He attributes it to the eccentric jealousy of a brother who cannot bear to lose his companion. Blind, honest Watson! A brother would welcome a match with a baronet of ancient blood and a fortune of three-quarters of a million pounds! It is the dream of every ambitious social-climber in England! Why, then, did Stapleton foam at the mouth like a rabid dog when he saw another man’s arm around her waist?”

The answer was written in the blood of human nature.

“Because Beryl is his wife!” I whispered into the silence of the hut. “The monster has forced his lawful wife to play the part of an unmarried sister, dangling her beauty as a lure before young Sir Henry to draw him onto the isolated moor roads! Yet when the trap begins to spring, the brute’s own animal jealousy overmasters his cunning, and he flies at the throat of his victim!”

And as for Barrymore’s candle in the window?

I glanced through the low doorway towards the black crags of the tor. “Barrymore is not the killer,” I concluded. “He is signaling to someone in the rocks. Someone who is starving; someone connected to Mrs. Barrymore’s tears. That is an underplot, Watson—a domestic melodrama played out against the backdrop of our great tragedy. Tonight, I shall take post upon the rocks and see who answers the butler’s candle!”""",
        "content_cn": """进入十月之后，荒原的凄风苦雨在入夜后变得愈发狂暴，冰冷的狂风卷着成片的暴雨，狠狠抽打在史前石屋坚硬如铁的圆形花岗岩外壁上，发出阵阵沉闷的撞击声。然而在石屋内侧，在一排厚厚的泥炭板屏风遮挡下，一根白牛油蜡烛正散发着稳定而温暖的黄色火光。我身披水手粗呢厚大衣，双腿盘坐在羊毛毯上，嘴里紧紧咬着我那只漆黑的短柄陶土烟斗。

平铺在我膝头上的，是整整四张写得密密麻麻的薄便签纸，上面的字迹工整、有力、刚劲挺拔，正出自约翰·H·华生医生之手。

卡特赖特在日落两个小时后，宛如水獭破浪般涉水穿过泥泞的石楠丛，将这份密封的情报稳稳送达了我手中。这会儿，那个机灵的苦力小子正蜷缩在石屋角落厚厚的干羊齿草堆里，宛如一条疲惫的猎犬般发出了香甜轻微的鼾声。

我轻轻抚平信纸的第一页，眼眸深处闪烁着由衷的欣慰与赞许。

‘干得太漂亮了，华生！’我忍不住对着摇曳的烛火低声赞叹，‘真是个值得托付后背的得力臂膀！他的眼睛没有放过任何蛛丝马迹，他的笔尖也毫不吝啬墨水。’

华生发来的这份第一阶段战地侦查报告，堪称一份登峰造极的绝妙情报摘要。以其一贯崇尚客观事实的军医本色，他极其详尽地记录了入驻巴斯克维尔庄园第一周以来发生的所有离奇变故：

第一项：越狱的杀人魔塞尔登。军警封锁线搜寻无果后，正规军步兵连已经撤回了普林斯敦兵营，郡当局初步推断那个恶魔要么早已溺毙在格林盆泥潭深处的无底死沼里，要么已经侥幸逃窜到了南部沿海港口。然而华生敏锐地注意到，庄园宅邸内部却弥漫着一种诡异的极度紧张感：食品储藏室里的熏肉和干面包频频离奇失窃，而管家巴里摩尔太太的一双红肿泪眼，却暴露出她终日处于极度悲伤与恐惧之中。

第二项：管家约翰·巴里摩尔的深夜诡祟异动。华生与亨利爵士连续两夜潜伏在二楼走廊漆黑的阴影中。接连两晚，在凌晨两点整，伴随着一阵沉重而刻意压抑的赤脚轻步声，那个蓄着黑胡子的高大管家手持一盏幽暗的铜烛台，悄无声息地溜过了他们的房门，潜入了走廊西端一间朝向荒原的空置客房。在那里，巴里摩尔将蜡烛高高举向窗前，面孔死死贴在冰冷的玻璃上，目光狂热地凝视着荒原漆黑一片的死寂夜幕，仿佛在苦苦等候着某种来自幽冥的回应信号！

第三项：年轻爵士与贝丽尔·斯台普吞之间炽热危险的罗曼史。亨利爵士几乎不可救药地坠入了对梅立坪那位异域美人的疯狂爱河。他每日策马前往拜访，甚至同她在荒原的石楠小径上漫步私语。然而，就在昨天下午，荒原上却爆发了一场不可思议的暴烈冲突：亨利爵士情难自禁，试图在岩石旁握住贝丽尔的手并亲吻她。就在那一瞬间，原本潜伏在乱石后的杰克·斯台普吞如同发了疯的恶犬般猛然窜了出来，面色因暴怒而扭曲成铁青色，双眼喷火，用极其恶毒粗暴的污言秽语尖叫着勒令亨利爵士立刻放手，并发誓永远不许他再踏近他妹妹半步！然而仅仅过了两个小时，斯台普吞却又亲自登门造访巴斯克维尔庄园，为自己的‘冲动失态’向爵士进行了极其卑微下贱的谢罪道歉，并极其热情地力邀亨利爵士在近日内务必赏光光临梅立坪宅邸共进晚餐！

我深深地倚靠在冰凉的弧形石壁上，一圈青蓝色的烟圈缓缓升腾，没入了屋顶的排烟石隙中。

‘这些散落的拼图碎片，咬合得多么丝丝入扣啊！’我自言自语地冷笑道，‘华生对斯台普吞自相矛盾的乖戾举止百思不得其解。他竟然将其天真地归咎于一个自私兄长对即将失去相依为命的胞妹时爆发的病态占有欲！善良而单纯的华生啊！世间哪有一位寒酸落魄的乡村私塾教师，会拒绝自己的亲妹妹嫁给一位拥有世袭准男爵头衔、坐拥七十四万英镑庞大家产的名门望族？！这本该是全英格兰每一个钻营钻营之徒梦寐以求的通天捷径！那么，斯台普吞为何在看到另一个男人搂住她的腰肢时，会像狂犬病发作一样口吐白沫、彻底失控？’

答案早已用人类最原始丑恶的本能写就。

‘因为贝丽尔是他的合法妻子！’我对着石屋死寂的黑暗发出了冰冷的断语，‘那个畜生强迫自己的结发妻子隐匿身份，假扮成未婚的深闺碧玉，将她的绝世美貌当成最致命的淬毒诱饵，诱使年轻的亨利爵士一步步踏入荒原与泥潭绝境！然而，当猎物真正咬向诱饵的那一刻，那个恶棍体内恶毒的雄性占有欲却彻底压倒了他的伪装理智，迫使他如疯狗般狂噬受害者！’

至于巴里摩尔在深夜窗前点燃的那盏诡异蜡烛？

我转过头，望向门外风雨交加中巍峨伫立的花岗岩峰顶。‘巴里摩尔绝非凶手，’我心中了然，‘他是在向藏匿在岩岗深处的某个人传递信号。一个饥寒交迫、生命垂危、且深深牵动着巴里摩尔太太眼泪的落难者。华生，那不过是一出在庄严宏大的复仇悲剧幕布前同时上演的庸俗家庭小闹剧。今夜，我便要亲自登上黑色岩岗的绝壁之巅，亲眼看看——究竟是谁，在石楠丛深处回应着管家的烛火！’"""
    },

    # -------------------------------------------------------------------------
    # Chapter 9: Part 1
    # -------------------------------------------------------------------------
    {
        "id": "holmes_ch09_part1_midnight_watch",
        "ch_idx": 8, "part": 1,
        "title_en": "Chapter 9: The Light upon the Moor (Part I: The Candle and the Signal)",
        "title_cn": "第九章 荒原上的烛光（上：暗夜荧惑与亡命奔逃）",
        "pov": "holmes", "type": "branch", "anchor": "anchor_convict",
        "clues_en": [
            "Watched the midnight candle signal from Baskerville Hall window answered by a flicker on the rocks",
            "Identified the signal receiver as Selden, the Notting Hill convict and brother of Mrs. Barrymore",
            "A blood-chilling hound roar reverberates through the crags, terrifying Watson and Sir Henry",
        ],
        "clues_cn": [
            "从岩岗顶峰俯瞰巴斯克维尔庄园窗前的微弱烛光，荒原乱石堆中立刻闪烁出一簇回应的火星",
            "证实接头者正是诺丁山杀人狂魔塞尔登——他实为管家夫人溺爱放纵的亲胞弟",
            "在华生与亨利爵士冒死搜山之际，一声震撼荒原的凄厉恶犬咆哮自大格林盆泥潭深处轰然炸裂",
        ],
        "choices_en": [
            {"id": "h_ch9_p1_c1", "text": "Hold your position upon Black Tor to avoid blowing your covert surveillance.", "target": "holmes_ch09_part2_figure_on_the_tor"},
            {"id": "h_ch9_p1_c2", "text": "[Switch POV to Dr. Watson] Join the armed midnight chase across the rocky moor.", "target": "ch09_part2_moor_chase", "pov_switch": "watson"},
        ],
        "choices_cn": [
            {"id": "h_ch9_p1_c1", "text": "在黑色岩岗巨石掩体后按兵不动，恪守绝密监视纪律，静观事态演变。", "target": "holmes_ch09_part2_figure_on_the_tor"},
            {"id": "h_ch9_p1_c2", "text": "【视角切换：约翰·H·华生】亲历持枪涉险、在伸手不见五指的荒原乱石中突击搜捕逃犯的惊魂时刻。", "target": "ch09_part2_moor_chase", "pov_switch": "watson"},
        ],
        "content_en": """Midnight had struck from the distant church tower of Grimpen. The rain had ceased, but the gale continued to sweep across the high plateaus, tearing the scudding clouds into ragged black shreds.

I lay prone upon the flat granite summit of Black Tor, my canvas groundsheet beneath me, my field glass pressed to my eye. Two miles away, the dark, sprawling mass of Baskerville Hall sat like an island of black timber amid the silver-grey sea of heather.

Suddenly, a tiny point of yellow flame bloomed in the dark facade.

It was the window at the western gable. The flame flared once, twice, three times—a candle held close to the glass and shielded by a hand.

I swung the barrel of the telescope half a mile across the moor to the west, sweeping the broken granite clatters. For several minutes, there was only darkness. And then, from the hollow of a ruined dry-stone sheep-pen, an answering spark flickered into life! A dull, reddish glow—a match touched to a dry candle-end, held aloft for ten seconds, and then extinguished.

“Barrymore’s partner in crime,” I muttered. “Let us see who ventures out into the night.”

Down at the Hall, the side door opened. Two figures slipped out onto the terrace. Through the glass, the athletic stride of Sir Henry and the square, resolute shoulders of Watson were unmistakable. Both men wore heavy coats and carried revolvers. They were advancing swiftly and silently across the heather, heading straight for the beacon in the rocks!

The game was becoming perilous. If they cornered the man, there would be blood.

I followed their advance through the rocks. The candle in the sheep-pen flared again. The occupant was careless, driven by cold and starvation. As Sir Henry and Watson closed within thirty paces, the moonlight broke through a rift in the scudding clouds, casting a cold, silver glare over the amphitheatre of stones.

A creature sprang up from behind a rock.

Through the powerful magnification of my lens, I saw him with startling clarity: a gaunt, savage, filthy apparition with a matted beard, sunken, burning eyes, and the branded look of a hunted wolf. He wore the coarse, yellow-and-brown striped uniform of the convict, torn to shreds by brambles and caked with the dried muck of the peat bog.

It was Selden! The Notting Hill murderer!

Sir Henry shouted and dashed forward. Selden hurled a heavy granite stone, which crashed against a boulder within an inch of Watson’s shoulder. With the speed of an ape, the convict leaped over a chasm, scrambled up the steep face of a granite clatter, and fled frantically out onto the open moor!

Watson raised his revolver. Two flashes of orange fire punctured the night, followed by the whip-like crack of shots. The bullets whined off the rocks, but Selden was untouched; he bounded down the reverse slope and vanished into the labyrinth of boulders.

And then, as Watson and Sir Henry lowered their weapons, breathing hard upon the hillside...

It came.

From far away in the direction of the Great Grimpen Mire, a sound rose upon the wind—a deep, hollow, menacing howl that swelled into a prolonged, reverberating roar that made the granite stones beneath my chest vibrate with horror! It was not the bark of a sheep-dog; it was not the bay of a foxhound. It was a mournful, savage, thunderous cry of boundless ferocity, rising and falling like the voice of a demon howling in the abyss!

I felt the hairs upon the back of my neck stand on end.

Across the valley, Watson and Sir Henry stopped dead in their tracks. Through the glass, I saw Sir Henry grasp Watson’s arm, his face blanching to the colour of ash. Even across two miles of open moor, the primal terror of that sound seemed to freeze the blood in their veins!

“You hear it, don’t you, my friends?” I whispered into the howling gale, my hand closing over the cold steel of my own revolver. “The beast is awake. It smells the blood of the Baskervilles upon the wind!”""",
        "content_cn": """格林盆村远方那座古老教堂的高耸钟楼，在夜空中沉闷地敲响了午夜十二点的沉重钟声。连绵的暴雨终于停歇，然而凛冽刺骨的狂风却依旧在高原上肆虐呼啸，将漫天低垂的阴云撕扯成一道道狰狞飞掠的黑色碎片。

我整个人平趴在黑色岩岗最顶端平整的花岗岩石台上，身下垫着军用防水帆布，大倍率望远镜冰冷的黄铜目镜死死贴在我的眼眶上。两英里开外，巴斯克维尔庄园那片庞大深邃的阴暗建筑群，宛如一片在银灰色石楠浪涛中沉浮的黑色巨木方舟。

骤然间，漆黑一片的庄园西侧山墙上，绽放出了一点微弱如豆的黄色火光！

那是西翼顶层那间客房的窗户！火光在玻璃后微微晃动，一次、两次、三次——那是有人将蜡烛紧贴在窗棂上，用手掌遮挡着向外发出有节奏的呼应闪烁！

我迅速转动望远镜的三脚架云台，将镜头向西横切过半英里外的荒原乱石堆，在那些布满黑苔藓的破碎花岗岩裂谷中急速搜寻。在长达数分钟的时间里，镜头中唯有一片令人窒息的死寂漆黑。然而，就在我扫过一座半塌陷的史前环形石头羊圈废墟时，一簇回应的微弱火星，骤然撕裂了黑暗！一根被火柴点燃的残破蜡烛头在石缝间微弱地亮起了十秒钟，旋即被一只粗糙的大手迅速捏灭！

‘巴里摩尔的同谋终于现身了，’我低声冷语，‘就让我瞧瞧究竟是何方神圣在深夜领赏。’

视线拉回庄园主楼，东侧的厚重边门无声地推开了一条缝隙。两道矫健敏捷的身影宛如出穴的猎犬般闪身跨上了石阶。透过高倍透镜，亨利爵士充满爆发力的挺拔步伐，以及华生医生那宽阔刚毅的军人肩膀，在惨白的微弱天光下一览无余。两人皆身披厚重的长款风衣，右手死死插在大衣口袋深处——那里显然握着上膛的左轮手枪！他们二人动作迅疾而警觉，借着岩石的阴影掩护，径直朝着半英里外那处亮起烛光的羊圈废墟突击包抄而去！

局势瞬间滑向了极度危险的边缘！一旦这两个人与那名亡命徒狭路相逢，一场见血的生死火拼将不可避免！

我的视线紧咬着他们前行的轨迹。羊圈废墟里的蜡烛再次被点燃了——那名潜伏者显然被数日的酷寒与饥饿折磨得丧失了最基本的警惕。就在亨利爵士与华生悄然摸索推进到距离羊圈不足三十步的关键时刻，狂风猛然撕裂了天际密布的阴云，一轮冷酷如银盘的深秋明月，将惨白清冽的月光暴烈地泼洒在整片花岗岩乱石堆上！

一道人形如受惊的猿猴般猛然从石堆后一跃而起！

在镜头惊人的高倍率放大下，那张面孔在月光下呈现出令人毛骨悚然的清晰全貌：一个身材枯瘦如柴、面目狰狞可怖的凶蛮恶汉！他生着一头乱如鸟窝的肮脏头发与浓密板结的大胡子，深陷的眼窝里燃烧着困兽垂死般的血红凶光，浑身上下散发着一种唯有被全人类追杀的孤狼才特有的残暴野性！他身上裹着一套破烂成条状、被荆棘撕扯得体无完肤的粗呢黄褐相间囚服，裤腿上厚厚包裹着风干硬化的黑泥炭浆！

是塞尔登！那个让全伦敦市民闻风丧胆的诺丁山杀人狂魔！

‘站住！’亨利爵士爆发出一声怒吼，猛然向前飞扑！塞尔登在狂怒中抓起一块海碗大小的坚硬花岗岩巨石，狠狠砸向追兵，巨石擦着华生的肩头在岩壁上砸得火星四溅！那个恶徒展现出了令人惊骇的猿猴般身手，单手一撑翻越过两米宽的深沟，连滚带爬地踩着嶙峋的峭壁，发疯般朝着荒原深处狂奔突围！

华生毫不犹豫地拔出了阿达姆斯左轮手枪！两团耀眼的橘红色枪火骤然撕裂了黑夜，紧随其后的是两声宛如炸雷般的刺耳枪鸣！子弹尖啸着擦过花岗岩岩壁弹飞，但那个狡黠的亡命徒却毫发无损；他一个侧滚翻滑下了背风坡，转瞬间便彻底湮没在茫茫无际的花岗岩乱石迷宫之中！

正当华生与亨利爵士懊恼地垂下手枪、在山脊上剧烈喘息之际……

某种恐怖绝伦的事物，降临了。

顺着自大格林盆泥潭方向刮来的凄厉阴风，一道低沉、幽远、充满无尽怨毒与暴戾的咆哮声，在夜空中幽幽升起——那声音起初如地底传来的空洞闷雷，继而节节攀升、撕裂云层，化作一声震撼天地、足以令每一块花岗岩石板都为之战栗的恐怖巨兽狂吼！那绝非寻常看门土狗的狂吠；也绝非纯种猎狐犬的悲鸣！那是一声混杂着远古嗜血野性与地狱复仇怒焰的凄厉哀嗥，在荒原苍穹下久久回荡、经久不息！

我感到自己脖颈后方的每一根汗毛，在一瞬间根根倒竖而起！

在两英里开外的山脊上，华生与年轻的亨利爵士如遭雷击般瞬间僵死在原地。透过镜头，我清晰地看见年轻的巴斯克维尔爵士一把死死抓住了华生的大臂，他那张英挺的面庞在月光下一瞬间褪尽了全部血色，惨白得宛如一具死尸！即便相隔数英里之遥，那种直击人类灵魂深处最原始梦魇的凄厉凶嚎，依然在刹那间将他们体内流淌的血液冻结成了冰渣！

‘你们听到了吧，我亲爱的朋友们？’我趴在冰冷死寂的花岗岩绝壁上，右手缓缓扣紧了怀中军用转轮手枪冰冷的硬木握把，在迎面呼啸的阴风中低声宣誓，‘恶兽已经苏醒了！它已经顺着夜风，嗅到了巴斯克维尔家族血脉温热的气息！’"""
    },

    # -------------------------------------------------------------------------
    # Chapter 9: Part 2
    # -------------------------------------------------------------------------
    {
        "id": "holmes_ch09_part2_figure_on_the_tor",
        "ch_idx": 8, "part": 2,
        "title_en": "Chapter 9: The Light upon the Moor (Part II: The Figure upon the Tor)",
        "title_cn": "第九章 荒原上的烛光（下：月夜伫立的石岗幽灵）",
        "pov": "holmes", "type": "branch", "anchor": "anchor_man_on_tor",
        "clues_en": [
            "Holmes stood silhouetted atop Black Tor under the moonlight, arms folded, watching Watson",
            "Watson spotted the mysterious solitary watcher and fired a shot towards the summit",
            "Holmes deliberately vanished into the rocks to preserve the covert trap until all evidence was complete",
        ],
        "clues_cn": [
            "福尔摩斯在冷月穿云的一瞬伫立于黑色岩岗绝顶，双臂抱胸，居高临下俯瞰华生与亨利爵士",
            "华生在惊恐中骤然发现了这位遗世独立的神秘监视者，并朝着岩岗顶峰厉声喝问鸣枪",
            "福尔摩斯借岩石阴影如幽灵般潜入地底石屋，恪守铁律：在铁证如山之前绝不提前现身",
        ],
        "choices_en": [
            {"id": "h_ch9_p2_c1", "text": "Analyze Watson’s diary extracts regarding the charred letter signed “L.L.”", "target": "holmes_ch10_diary_and_laura"},
            {"id": "h_ch9_p2_c2", "text": "[Switch POV to Jack Stapleton] See Stapleton traversing the mire to feed the hound.", "target": "stapleton_ch09_part1_feeding_the_hound", "pov_switch": "stapleton"},
        ],
        "choices_cn": [
            {"id": "h_ch9_p2_c1", "text": "破译华生发来的绝密日记摘录，锁定带有‘L.L.’落款的神秘焚烧残信。", "target": "holmes_ch10_diary_and_laura"},
            {"id": "h_ch9_p2_c2", "text": "【视角切换：杰克·斯台普吞】窥视凶手如何摸黑涉过泥潭密道，向饥饿凶兽投喂鲜肉。", "target": "stapleton_ch09_part1_feeding_the_hound", "pov_switch": "stapleton"},
        ],
        "content_en": """The terrible baying died away into the gale, leaving in its wake a silence more dreadful than the cry itself.

Two miles away on the moonlit ridge, Watson and Sir Henry had abandoned all thought of pursuing the convict. They turned back towards the post-road, walking shoulder to shoulder, their eyes darting nervously towards every shadow in the heather.

I stood upright upon the highest pinnacle of Black Tor.

The moon had cleared the last bank of storm clouds, hanging like a burnished silver shield in the deep indigo vault of heaven. Its brilliant rays bathed the crags in an unearthly, crystalline light, etching every fissure of the rock in ink and bone. I wrapped my heavy pea-jacket tightly across my chest, folded my arms, and let the wind whip my hair, looking down from my aerial perch upon the retreating figures of my friends.

It was an imprudence, perhaps—a momentary indulgence of that theatrical dramatic instinct which Watson has so often diagnosed in my nature. Yet there was a sublime majesty in that desolate waste at two o’clock in the morning that stirred the blood like wine.

Suddenly, Watson stopped upon the path below.

He turned on his heel and looked back towards the high ridges of the north. His eyes swept the crags, and in that instant, his gaze locked onto the pinnacle of Black Tor.

Even without my glass, I saw the jerk of his arm as he gripped Sir Henry’s shoulder. There was no mistaking what they saw: against the silver disc of the full moon, silhouetted in razor-sharp relief upon the highest stone, stood the figure of a solitary man—tall, gaunt, motionless as an ebony statue, his arms folded across his breast, his cloaked shoulders outlined against the sky!

“Look! Look yonder!” I could almost hear Watson’s shout carry across the gale.

The doctor raised his revolver, his arm steadying as he aimed towards the high rock.

“Hold your fire, my dear fellow,” I whispered with a faint, wry smile. “You would scarcely hit a target at eight hundred yards with an Adams revolver, and you might seriously discommode your oldest friend.”

I did not wait for the bullet. With a single fluid step, I dropped backward into the deep shadow of the rock-cleft. Sliding down the granite chimney with the silent agility of an otter, I ducked through the low doorway of my stone hut and seated myself once more upon my blanket.

Outside, the sharp crack of Watson’s distant shot rolled across the waste, flat and puny against the vast silence of the night.

Cartwright stirred in his heather bed, muttering in his sleep, then settled back into slumber. I struck a match, shielded the flame with my palm, and lit my blackened clay pipe.

“A near thing, Watson,” I reflected, watching the smoke curl towards the stone rafters. “You are an indefatigable sentinel. But you must not know yet. If you knew, your honest, open countenance would betray the secret within twenty-four hours to the sharp eyes of Jack Stapleton. You would speak differently; you would look differently; your very step upon the gravel would lose that anxious weight which now convinces our enemy that Sir Henry stands alone and unprotected!”

No. The game must be played out to the bitter end. The net was closing, but three vital threads still needed to be spliced together:

First: The identity of the woman whose letter lured Sir Charles to the gate.

Second: The physical proof connecting Stapleton to the bloodline of the Baskervilles.

Third: The lair in the Great Grimpen Mire where the fire-breathing monster was chained!

I closed my eyes, leaned my head against the ancient granite, and listened to the wind howling across the roof of the world.""",
        "content_cn": """那声令人肝胆俱裂的凄厉长嚎终于随风消散在远方，然而它在荒原上留下的死寂，却比咆哮本身更加令人窒息。

在两英里开外惨白的月光山脊上，华生与亨利爵士显然彻底放弃了继续追捕逃犯的念头。两人并肩而行，警惕地背靠着背退向驿道方向，手中的转轮手枪始终平举着，惊恐万状的目光不断在沿途每一丛晃动的石楠阴影中扫射。

而我，则终于从平趴的石台上一跃而起，稳稳伫立在了黑色岩岗最险峻的花岗岩孤峰绝顶！

深秋的满月终于彻底冲破了最后一层铅灰色的浓云，宛如一面擦拭得锃光瓦亮的纯银战盾，高高悬挂在深邃沉寂的天鹅绒穹顶中央。冷冽清澈的月光如瀑布般倾泻在嶙峋的峭壁上，将每一道古老岩石的缝隙，都勾勒成由浓墨与白骨交织而成的严酷线条。我将水手厚大衣紧紧裹在胸前，双臂抱胸，任凭狂暴的高原烈风撕扯着我的衣角与黑发，宛如一只栖息在云端巨巢中的冷峻鹰隼，居高临下地俯视着我那两位正仓皇撤退的忠实挚友。

这或许是一种近乎轻率的冒险行径——是我体内那股常被华生批评为‘好大喜功的戏剧化表演狂热’在作祟。然而，在凌晨两点整面对这片吞噬一切的壮美苍茫死地，那种独揽风云的豪迈快意，确实如烈酒般在我的血液中狂野奔涌。

骤然间，远方驿道上的华生猛地刹住了脚步！

他霍然转身，将目光投向了北方这片巍峨起伏的高耸山脊。他的视线在嶙峋的怪石间急速搜寻，旋即在百分之一秒的时间内，他的目光如闪电般死死钉在了黑色岩岗的最顶峰！

即便无需望远镜，我也能清晰地看到他一把死死扣住亨利爵士肩头的剧烈动作！他们眼前所目睹的景象实在太具震慑力了：在圆月那轮巨大的纯银背景正中心，一道孤绝冷傲的黑色人形剪影，正以宛如黑檀木雕像般的完美姿态伫立在苍穹之巅——双臂抱胸，大衣如黑翼般在狂风中猎猎作响，宛如荒原守护神，又宛如索命的幽灵死神！

‘看！看那边！’我几乎能想象出华生隔着数英里烈风爆发出的一声惊骇长啸！

这位受过严格射击训练的陆军军医猛然举起了阿达姆斯左轮手枪，手臂如铁铸般平伸，枪口死死瞄准了岩岗顶峰的黑色剪影！

‘别开枪，我亲爱的朋友，’我嘴角勾起一抹戏谑而温暖的苦笑，低声耳语，‘八百码的超远距离，手枪弹丸不仅连我的衣角都摸不到，反而极有可能误伤你在这个世界上最老派的至交。’

我没有在原地停留等待那声毫无意义的枪响。脚下一错，我整个人宛如一道无形的鬼魅，轻巧地倒翻滑入了岩峰背阴面那道深邃的花岗岩裂隙中。伴随着水獭般灵巧轻盈的身法，我在陡峭的岩壁管道中飞速下行，闪身钻入了石屋那道低矮坚固的门洞，重新稳稳盘坐在了羊毛毯上。

数秒之后，一声极其微弱沉闷的破空枪响，在石屋厚重的外壁外随风消散，在这片浩瀚深邃的荒原之夜里显得如此渺小而滑稽。

角落里的卡特赖特在羊齿草堆里翻了个身，梦呓般嘟囔了一句，旋即又沉沉睡去。我划燃一根火柴，用手掌拢住火苗，再次点燃了那斗已然熄灭的黑板烟丝。

‘险些暴露，华生，’我凝视着袅袅升腾的蓝灰色烟雾，在心底轻叹，‘你真是一个不知疲倦的忠诚哨兵。然而，现在绝不是你得知真相的时机！一旦让你知晓我就潜伏在此，你那张写满军人真挚与坦荡的面庞，不出二十四小时便会在狡黠的斯台普吞面前彻底露出破绽！你的眼神会变，你的语气会变，甚至你在碎石路上迈出的每一步步伐，都将丧失那种此刻正让凶手深信“亨利爵士孤立无援”的焦虑与沉重！’

不。这场终极棋局必须毫无破绽地下完最后几步！

复仇的铁网正在急速收紧，然而眼下依然有三道决定生死的死结必须被彻底理清：

第一：那封用‘L.L.’签名将查尔斯爵士诱骗至午夜水松夹道栅门的神秘绝命信，其背后的女主人究竟是谁？

第二：连接杰克·斯台普吞与巴斯克维尔家族血脉源头的确凿物理铁证究竟何在？

第三：在大格林盆泥潭那片千万亩食人死沼深处，那只喷吐幽冥磷光的噬血魔犬，究竟被锁在哪一座孤岛废墟之中！

我缓缓合上双眼，将后脑勺紧紧贴在冰冷坚硬的史前花岗岩石壁上，静静聆听着屋顶上方那席卷了整座人间的荒原风暴之歌。"""
    },

    # -------------------------------------------------------------------------
    # Chapter 10
    # -------------------------------------------------------------------------
    {
        "id": "holmes_ch10_diary_and_laura",
        "ch_idx": 9, "part": 1,
        "title_en": "Chapter 10: Extract from the Diary of Dr. Watson (The Secret of L.L.)",
        "title_cn": "第十章 华生医生的日记摘录（神秘女人L.L.的破译）",
        "pov": "holmes", "type": "branch", "anchor": "anchor_diary",
        "clues_en": [
            "Watson cross-examined Barrymore: Sir Charles went to the gate to meet a woman",
            "Burnt letter postscript recovered from fireplace grate: “...as you are a gentleman, burn this letter, and be at the gate by ten o’clock. — L.L.”",
            "Dr. Mortimer identifies L.L. as Mrs. Laura Lyons, estranged daughter of old Frankland of Coombe Tracey",
        ],
        "clues_cn": [
            "华生严厉审讯管家巴里摩尔：证实查尔斯爵士在遇害当夜系收到一封女性来信秘密赴约",
            "壁炉灰烬残片中拼凑出绝密字条：‘……看在您是位绅士的份上，务必烧毁此信，十点整守候栅门前。——L.L.’",
            "摩梯末医生协助破译：‘L.L.’正是库姆·特雷西村老弗兰克兰德那离家出走、惨遭弃市的独生女劳拉·里昂斯夫人",
        ],
        "choices_en": [
            {"id": "h_ch10_c1", "text": "Proceed to Coombe Tracey to interrogate Laura Lyons and shatter Stapleton’s deceit.", "target": "holmes_ch11_part1_lyons"},
            {"id": "h_ch10_c2", "text": "[Switch POV to Jack Stapleton] Discover how Stapleton controlled and silenced Laura Lyons.", "target": "stapleton_ch10_coombe_control", "pov_switch": "stapleton"},
        ],
        "choices_cn": [
            {"id": "h_ch10_c1", "text": "驱车直奔库姆·特雷西村，当面质询劳拉·里昂斯夫人，粉碎斯台普吞的谎言锁链。", "target": "holmes_ch11_part1_lyons"},
            {"id": "h_ch10_c2", "text": "【视角切换：杰克·斯台普吞】窥视凶手如何凭借伪造的婚约与虚伪甜言死死封锁劳拉之口。", "target": "stapleton_ch10_coombe_control", "pov_switch": "stapleton"},
        ],
        "content_en": """The morning brought a temporary lull in the storm. Pale shafts of autumn sunlight broke through the mist, turning the sodden heather into a carpet of russet and gold. Inside the stone hut, I sat upon my pack, devouring the second dispatch from Baker Street which Cartwright had brought up the mountain at daybreak.

Watson had excelled himself. Driven by the mystery of the candle in the window, he and Sir Henry had confronted Barrymore in the library of Baskerville Hall.

The butler, broken by their accusations, had broken down and confessed the secret of the candle: the runaway convict Selden was indeed his wife’s youngest brother, the spoiled darling of her childhood, whom she could not bear to see starve upon the crags. That mystery was solved, exactly as my deductions had foretold.

But then, as Watson pressed the butler for any further facts concerning Sir Charles’s death, Barrymore had made a revelation of stupendous importance.

“Sir Charles went to the gate that night to meet a woman,” Barrymore had blurted out.

“A woman!” Watson had cried. “What woman?”

“I do not know her name, sir,” Barrymore had replied. “But on the morning of the day he died, Sir Charles received a letter postmarked Coombe Tracey, addressed in a woman’s delicate hand. After the tragedy, when my wife went to clean the study grate, she found the charred remnant of that letter. The body of the paper was consumed, but the postscript at the bottom had remained legible:

‘...Please, please, as you are a gentleman, burn this letter, and be at the gate by ten o’clock. — L.L.’”

I dropped the paper onto my knee, my eyes blazing like live coals.

“L.L.!” I whispered aloud. “L.L.! By heavens, the master-link has forged itself in the fire!”

I sprang to my feet and paced the narrow confines of the circular hut, my mind racing through every name, every scrap of gossip recorded in Mortimer’s notebook and the county directories.

Who in the district of Coombe Tracey bore the initials L.L.?

Watson’s notes provided the answer on the following page. In his methodical, bulldog fashion, Watson had consulted Mortimer immediately upon leaving the Hall. The doctor had supplied the missing name without hesitation:

Mrs. Laura Lyons.

She was the daughter of old Frankland of Lafter Hall, that litigious eccentric who spent his fortune suing his neighbours over ancient rights of way. Her father had disowned her five years earlier when she eloped with a penniless, scoundrelly landscape painter named Lyons. The husband had soon abandoned her in London, leaving her destitute. She had returned to Devonshire, where Sir Charles Baskerville and other charitable gentlemen had provided her with funds to establish a modest typewriting office in the market town of Coombe Tracey.

“A destitute, beautiful woman,” I reasoned, striking my open palm with my clenched fist. “A woman desperate to secure a legal divorce from a blackguard husband; a woman dependent upon the charity of Sir Charles Baskerville; and a woman residing in the very village where Jack Stapleton visits weekly under the guise of an entomological scholar!”

The entire sinister design burst upon my intellect with the blinding glare of an explosion.

Stapleton had courted Laura Lyons in secret! He had feigned an ardent passion; he had promised her marriage and respectability the moment her divorce was completed. But a divorce in England requires heavy legal fees. Stapleton had directed her to write an urgent, desperate plea for money to her wealthy patron, Sir Charles, begging for an appointment at the lonely gate of the Yew Alley at ten o’clock at night.

And then—the masterstroke of the demon!

Having induced Laura Lyons to write the fatal letter, Stapleton had prevented her from keeping the appointment! He had promised to handle the matter himself. He had sent the terrified woman home, and then... he had taken his phosphorus-coated beast to the wicket gate where the superstitious old baronet stood waiting in the dark!

“The net is complete!” I shouted into the stone dome above my head. “Cartwright! Pack the hamper! We ride to Coombe Tracey! Before this sun sets, Laura Lyons will tear the mask from the face of Jack Stapleton!”""",
        "content_cn": """次日清晨，呼啸了一整夜的荒原暴风雨终于迎来了短暂的宁静。几道惨白而温和的深秋阳光穿透了弥漫在山谷间的浓雾，将漫山遍野湿漉漉的石楠苔原，镀上了一层由赭红与碎金交织而成的绚丽绒毯。在史前石屋干燥的角落里，我盘坐在帆布行囊上，双眼如饥似渴地研读着卡特赖特拂晓时分摸索送上山巅的第二份华生亲笔密信。

华生这一次的表现，简直超越了他以往所有的刑侦水准！在深夜窗前诡异烛火的强烈驱动下，他与年轻的亨利爵士在昨日清晨于巴斯克维尔庄园那间阴森的橡木图书室里，对管家巴里摩尔发起了一场教科书级别的严厉盘问。

在两人出其不意的铁证逼视下，管家终于心理崩溃，痛哭流涕地招供出了蜡烛背后的全部实情：越狱的杀人魔塞尔登，正是巴里摩尔太太一母同胞的亲生幼弟，是她童年时代最宠溺心疼的骨肉亲人。那个可怜的妇人实在不忍心看着自己的亲生弟弟在寒风刺骨的花岗岩荒石堆中活活冻馁而死，这才由管家每夜暗中送粮接济。正如我最初那严密的病理心理学推断一模一样——这桩看似杀机四伏的凶案分支，不过是一出令人唏嘘的人间悲剧插曲。

然而，正当华生穷追猛打、逼问巴里摩尔关于查尔斯爵士暴卒前夕的蛛丝马迹时，这位惊魂未定的管家，却道出了一条具有惊天动地威力的决定性线索！

‘查尔斯爵士在遇害当晚走到栅门前，是为了去秘密会见一个女人！’巴里摩尔脱口而出。

‘一个女人！’华生失声惊呼，‘哪个女人？！’

‘小人不知道她的真实姓名，先生，’巴里摩尔颤抖着回答道，‘然而在爵士遇害那天的早晨，他收到了一封从库姆·特雷西村寄来的平信，上面的笔迹秀气娟秀，显然出自一位年轻体面的女士之手。在惨剧发生之后，我妻子在替爵士清理书房壁炉里的残灰时，从炉底的死灰中捡出了那封信的一块未被彻底焚化的残片！信身的主要内容早已被烈火化为灰烬，然而最底部那行用颤抖笔迹写下的附笔，却清晰可辨：

“……求求您，看在您是一位真正绅士的份上，务必立刻将此信付之一炬，并在今夜十点整准时守候在水松夹道的栅门前。——L.L.”’

信纸从我手中滑落至膝头，我的双眼在一瞬间迸发出宛如烧透焦炭般的骇人精光！

‘L.L.！’我对着石壁从胸腔深处爆发出一声雷鸣般的低啸，‘L.L.！老天爷啊！这条贯穿了整桩阴谋的决定性黄金链条，终于在烈火与灰烬中浴火重铸了！’

我猛然从行囊上一跃而起，在石屋狭窄的方寸之地内迅疾如风地来回疾走，我的大脑如同一台高速运转的精密差分机，以每秒数千次的速度疯狂检索着摩梯末手记与德文郡郡志名录中的每一个姓名、每一段流言蜚语！

在整个库姆·特雷西教区乃至方圆数十英里内，究竟有谁的姓名缩写是L.L.？！

华生在报告后半段写下的文字，以一种无可挑剔的严密逻辑为我奉上了答案。以其特有的军人执拗作风，华生在离开庄园后第一时间便密会了摩梯末医生。而这位对当地风土人情洞若观火的乡村医生，毫不犹豫地吐出了那个被尘封的名字：

劳拉·里昂斯夫人（Mrs. Laura Lyons）。

她是老弗兰克兰德唯一的掌上明珠——就是住在拉夫特庄园、那个整天痴迷于用天文望远镜窥探荒原、为了几条古代公共路权把全郡邻居告上法庭的诉讼狂老绅士。五年前，这位年轻貌美的姑娘因执意与一个身无分文、品行不端的蹩脚伦敦风景画家里昂斯私奔，被顽固的父亲当场断绝了父女关系扫地出门。婚后不久，那个恶棍画家便将她在伦敦始乱终弃，卷款逃逸，令她一度沦落到了濒临冻饿自尽的绝境。万般无奈之下，她唯有辗转返回德文郡，在仁慈的查尔斯·巴斯克维尔爵士及几位乡绅的慷慨资助下，在库姆·特雷西集镇上开办了一家维持基本温饱的打字事务行。

‘一个身世凄楚、走投无路、却又生得倾国倾城的绝色尤物，’我在石屋狭窄的地面上重重挥动铁拳，掌风呼啸，‘一个迫切渴望摆脱无赖丈夫纠缠、急需一笔巨款办理合法离婚手续的可怜女人；一个在经济上完全依赖查尔斯爵士慈善施舍的弱女子；而最致命的是——一个恰好居住在杰克·斯台普吞每周必定借标本采购之名频繁光顾的集镇上的女人！’

整场阴险毒辣到了极点的魔鬼杀人布局，宛如一道刺破黑夜的万丈狂雷，在我脑海中彻底轰然引爆！

斯台普吞在暗中疯狂追求着劳拉·里昂斯！他用虚伪的甜言蜜语编织了一场海枯石烂的爱情骗局；他信誓旦旦地向她许诺：只要她能筹得巨资与那个恶棍丈夫办妥离婚手续，他便会立刻迎娶她为明媒正娶的夫人！然而，在严苛的大英帝国婚姻法下，一场贵族级的离婚诉讼需要数以百计的昂贵法庭诉讼费！于是，斯台普吞极其阴险地暗中指使并起草了那封信，诱骗这个深陷情网的可怜女人向她最仁慈的庇护人查尔斯爵士写信求援，并利用老人对她名节的爱护，诱骗老人在午夜十点孤身一人守候在幽暗无人的水松夹道栅门前！

紧接着——便是这个恶魔最残暴冷酷的致命杀招！

在诱使劳拉·里昂斯寄出那封绝命信之后，斯台普吞却在当天傍晚突然以某种冠冕堂皇的借口，严厉制止了她赴约！他向她虚伪地保证自己已经筹措到了款项，亲自去替她向爵士致谢周旋。在稳住了那个被蒙在鼓里的可怜女人之后……这个冷血的凶手，便牵着他那只涂满剧毒磷光溶剂的嗜血魔兽，悄然潜伏到了水松夹道的木门外，将死亡的咽喉，狠狠扼向了在黑暗中苦苦守候的老绅士！

‘全案告破！’我对着石屋高耸的锥形穹顶爆发出了一声痛快淋漓的怒吼，‘卡特赖特！立刻收拾行囊！备好马车！我们直扑库姆·特雷西村！在今天的夕阳坠入地平线之前，我要让劳拉·里昂斯亲手撕碎杰克·斯台普吞脸上那副伪善的人皮面具！’"""
    },
]
