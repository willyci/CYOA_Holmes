"""Jack Stapleton Track - Part 3: Chapters 11 to 14 (7 nodes).
Expanded canonical narrative from the villain's perspective.
"""

STAPLETON_NODES_PART3 = [
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
            {"id": "s_ch11_p1_c1", "text": "Hasten to the mire island and lay Sir Henry’s stolen black boot before the hound.", "target": "stapleton_ch11_part2_setting_scent"},
            {"id": "s_ch11_p1_c2", "text": "[Switch POV to Dr. Watson] View Watson cornering Laura Lyons in Coombe Tracey.", "target": "ch11_part1_lyons", "pov_switch": "watson"},
        ],
        "choices_cn": [
            {"id": "s_ch11_p1_c1", "text": "火速奔赴泥潭孤岛，将从伦敦偷来的旧黑皮靴浸透气味喂给饥渴暴怒的恶犬。", "target": "stapleton_ch11_part2_setting_scent"},
            {"id": "s_ch11_p1_c2", "text": "【视角切换：约翰·H·华生】见证华生在库姆马西打字行以正义辞令攻破劳拉防线。", "target": "ch11_part1_lyons", "pov_switch": "watson"},
        ],
        "content_en": """On the afternoon of October 23rd, armed with my powerful naval field glass, I climbed to the jagged summit of High Tor. My target lay a mile to the west: the ancient, ruined British settlement that clustered like honeycombs upon the granite crest of Black Tor.

For three nights, the memory of that tall, motionless silhouette framed against the moonlit disc of the sky had haunted my sleep with the persistence of an open grave. If that watcher was an agent of Scotland Yard—or worse, if it was the man with the grey eyes from cab No. 2704—my life was hanging by a thread of spider’s silk!

I wedged my body into a cleft of the rock, shielded from the biting northern wind, and leveled the twin brass barrels upon the Neolithic huts. 

For two hours, nothing moved across the desolate waste save the scudding shadows of autumn clouds and a stray sheep grazing among the gorse. Then, at a quarter to four, my patience was rewarded.

Moving along the sheep-track that wound up from the Coombe Tracey road came a small, nimble figure. Through the high-magnification lenses, I brought the intruder into sharp focus: a lad of fourteen, wearing the patched jacket and cloth cap of a London street Arab. Over his shoulder hung a wicker basket, covered with a clean white napkin.

I followed the boy’s progress step by step. He scrambled over the boulders with the agility of a mountain goat, glancing warily to his right and left at every stride, his London street instincts alive to danger. Reaching the high knoll of Black Tor, he made straight for the largest circular hut—the only dwelling whose ancient corbelled granite roof remained partially intact. He ducked beneath the low stone lintel.

Five minutes elapsed. Then the boy emerged. The basket on his arm was empty, but he held a white envelope in his right hand. He thrust the paper into his pocket, leaped down the crags, and sprinted away down the valley towards Coombe Tracey!

The chain of proof was forged to the final link!

A man was living in that prehistoric hovel! A man who received daily provisions of bread and meat from the market town! A man who despatched written orders to London! A man who lived like a hunted outlaw, enduring the freezing winds of Dartmoor, keeping his very existence a profound secret from Sir Henry Baskerville and Dr. Watson!

Who in the British Empire possessed the iron endurance, the audacity, and the theatrical mania to live in a stone hut on a freezing moor while directing an investigation of murder?

Sherlock Holmes!

The blood drummed against my temples like the hammers of a forge. The master detective had outmaneuvered me! While I had gloated that he was lounging in London, he had been perched like an eagle above my head, studying every step I took, watching every visit to the mire!

There was no time now for legal subtlety, no time for elaborate financial plots. If Holmes completed his inquiries, he would tie me to Laura Lyons, to the stolen boots, and to the hound within forty-eight hours! The law was closing in, and the shadow of the Exeter gallows fell dark across my path!

I must strike Sir Henry down tonight! Once the heir was dead, the direct line of Baskerville was extinct. I would present my claims through South American agents, seize the seven hundred and forty thousand pounds, and vanish across the Atlantic before Holmes could assemble his proofs!

I shut my glass, scrambled down the rocky slope, and made straight across the bog for the island of the beast!""",
        "content_cn": """十月二十三日下午，我手提强力双筒海军望远镜，如猎豹般潜上了海岩岗（High Tor）那犬牙交错的花岗岩绝壁。我的侦察目标直指西侧一英里外：黑色岩岗顶峰那些宛如蜂窝般聚集的不列颠史前圆形石屋遗址。

连续整整三个夜晚，那个在月夜顶峰傲视荒原的瘦高黑影，如同一座开敞的阴森坟墓般死死纠缠着我的梦魇。倘若那个暗哨当真是苏格兰场的便衣密探——甚至更糟，倘若正是伦敦摄政街2704号马车外那位灰眸如刀的神探——我的咽喉距离绞刑架便仅仅只剩下一根游丝的距离！

我将整个身躯楔入两块巨大花岗岩之间的避风裂隙，任凭刺骨的北风从头顶呼啸而过，两支黄铜镜头牢牢锁定了那些古老的石屋残壁。

在漫长而煎熬的两个小时里，除了掠过荒原的秋云阴影与几只在石楠丛中啃食的野羊外，整片死绝之地没有半点生命迹象。然而就在差一刻四点之际，我的苦心侦查终于迎来了突破！

顺着从库姆马西集镇方向蜿蜒而上的羊肠小道，一个精明敏捷的瘦小身影悄然出现在了山脊的拐角处。透过高倍率的凸透镜组，入侵者的面貌瞬间在焦距中心纤毫毕现：那是一个年约十四五岁的少年，穿着一身打满补丁的粗呢夹克，头戴歪斜的报童帽，俨然一副伦敦流浪街童的打扮。在他肩头，斜挎着一只蒙着洁白餐巾的野餐竹篮。

我屏住呼吸，死死追踪着这个少年的一举一动。他像只岩羊般在乱石堆上灵活纵跃，每跨出三步便警惕地向左右四下张望，伦敦街童那深入骨髓的生存嗅觉展露无遗。登上黑色岩岗顶峰后，他毫不迟疑地径直走向了那座最大、也是唯一一座史前石板穹顶保存相对完好的圆形石窟。他猫腰钻入了低矮的石门楣之下。

整整五分钟过去了。少年再次钻出了石门。他手臂上的竹篮已然空空如也，而他的右手里却紧紧攥着一封白色的信封！他将信函迅速塞入贴身口袋，随后飞身跃下峭壁，如离弦之箭般沿着山谷向库姆马西方向飞奔而去！

铁证如山，证据链的最后一环被彻底焊死！

那座三千年前的史前石屋里，确确实实住着一个活人！一个每天由集镇供应面包、肉类与烟草的活人！一个向外界拍发密令的统帅！一个昼伏夜出、忍受着达特穆尔刺骨寒夜，却对亨利爵士与华生医生彻底隐瞒自身行踪的最高谍报核心！

放眼整个大英帝国，究竟何人拥有这等钢铁铸造的非凡耐力、惊天动地的胆识，以及近乎走火入魔的戏剧化狂热，竟敢在达特穆尔刺骨的冰霜荒原上餐风露宿在野兽石窟之中指导破案？！

歇洛克·福尔摩斯！

太阳穴两侧的青筋狂暴突跳，血液如锻铁重锤般轰击着我的耳膜。这位名满天下的神探将了我一军！当我自鸣得意他在伦敦虚耗光阴时，他竟然早已如雄鹰般盘旋在我头顶的黑色绝壁之上，将我的每一步潜行、每一次入沼尽收眼底！

没有时间再玩弄文绉绉的借刀杀人了！更没有时间再去推敲繁复的海外继承诉讼！一旦让福尔摩斯彻底合拢证据链，不出四十八小时，他便会把劳拉·里昂斯、伦敦失窃的旧靴以及恶犬彻底套在我的脖子上！绞刑架的阴影已然笼罩在了我的头顶！

必须在今晚将亨利爵士格杀勿论！只要这位唯一的拦路虎横尸荒野，巴斯克维尔的直系血脉便彻底断绝！我将通过南美的代理律师火速接收全部七十四万镑巨款，在福尔摩斯拼凑出完整的法庭证据之前横渡大西洋，逍遥法外！

我啪的一声合上望远镜，飞身跃下峭壁，踩着沼泽暗径直扑恶兽盘踞的魔窟孤岛！"""
    },

    # Chapter 11 Part 2
    {
        "id": "stapleton_ch11_part2_setting_scent",
        "ch_idx": 10, "part": 2,
        "title_en": "Chapter 11: The Man on the Tor (Part II: Laying the Fatal Scent)",
        "title_cn": "第十一章 岩岗上的人（下：给猎犬闻取旧靴气味）",
        "pov": "stapleton", "type": "branch", "anchor": None,
        "clues_en": [
            "Stapleton starves the beast and rubs Sir Henry’s worn black boot across its jaws",
            "Prepares to release the hound into the darkness to slaughter the baronet",
        ],
        "clues_cn": [
            "故意剥夺恶兽两日饮食激发极致狂暴，用从伦敦盗来的亨利旧黑皮靴死死擦拭恶犬獠牙与吻部",
            "在狂风大作的黄昏全面备齐磷光油膏，决意在黑夜降临时放出巨兽清洗荒原",
        ],
        "choices_en": [
            {"id": "s_ch11_p2_c1", "text": "Unleash the hound into the foggy night and listen for the slaughter upon the crags.", "target": "stapleton_ch12_part1_screams_on_crags"},
            {"id": "s_ch11_p2_c2", "text": "[Switch POV to Sherlock Holmes] View Holmes revealing Stapleton’s identity to Watson.", "target": "holmes_ch11_part2_stone_hut", "pov_switch": "holmes"},
        ],
        "choices_cn": [
            {"id": "s_ch11_p2_c1", "text": "趁着浓雾涌起解开铁链放出恶魔巨兽，在荒原冷夜中侧耳倾听绝命哀嚎。", "target": "stapleton_ch12_part1_screams_on_crags"},
            {"id": "s_ch11_p2_c2", "text": "【视角切换：歇洛克·福尔摩斯】切换至石屋，见证名侦探撕破斯台普吞假面具的经典一幕。", "target": "holmes_ch11_part2_stone_hut", "pov_switch": "holmes"},
        ],
        "content_en": """I entered the rotting timber shed upon the mire island, my face set like a slab of Dartmoor granite.

For forty-eight hours, I had deliberately denied the hound a single scrap of meat or water. The creature had been driven to the outer frontiers of starvation. When it heard my key rattle in the iron padlock, it hurled its massive body against the chains with an explosion of famished fury that threatened to pull the iron ringbolts from the stone foundation! Yellow foam flecked its black dewlaps; its bloodshot eyes glowed with murderous madness; and its breath whistled through its bared fangs in dry, choking gasps.

From my oilskin satchel, I drew forth the talisman of death: Sir Henry Baskerville’s worn black boot, stolen from the Northumberland Hotel in the Strand.

I approached the snarling brute, speaking in that low, harsh hiss that had signaled every blood-kill since its puppyhood. I held the mud-encrusted leather directly beneath its quivering, black nostrils. I pressed the worn heel between its jaws, forcing it to bite the stiffened calfskin, to lick the dried perspiration, to inhale the oily, animal odour of the Canadian’s living skin until its brain was intoxicated by the scent!

The effect was instantaneous and terrifying!

The beast let out a deep, strangling moan of recognition. Its tail whipped like an iron rod against the flagstones; its neck muscles swelled as it inhaled the trail; its claws dug frenzied furrows into the dirt. It knew its quarry! It understood that this was the living flesh that would slake the torment of its belly!

Setting the boot upon the stone shelf, I took up my jar of white phosphorus preparation. With rapid, merciless sweeps of my hog’s-bristle brush, I coated the beast for its final flight. 

I painted the cold, luminous venom around its gaping sockets until its eyes seemed to smoulder with volcanic brimstone. I dragged the brush along the serrated edges of its teeth, over its black, slobbering lips, and down the deep creases of its throat and chest.

Outside the shed, twilight had dissolved into an ocean of rolling, clammy white moorland fog. The freezing wind shrieked through the gaps in the slate roof.

I stepped to the iron collar, gripped the brass release catch, and snapped the bolt!

“Kill!” I snarled, pointing through the open door into the gathering night. “Hunt him down and tear his throat!”

The monster erupted into the fog like a thunderbolt hurled from the abyss! 

A streak of roaring green and bluish flame, it bounded across the black quagmire, its giant paws skimming over the treacherous slime, vanishing into the swirling white vapour in the direction of the high tor!

I stepped out upon the threshold of the shed, shivering with predatory ecstasy, my head cocked towards the crags, waiting for the screams of agony that would announce my victory to the stars!""",
        "content_cn": """我一步跨入了泥潭孤岛那座腐烂的木质工棚，面孔冷硬得宛如一块饱经风霜的花岗岩墓碑。

为了将这头恶兽逼入极致的杀戮疯狂，整整四十八个小时里，我未曾给它喂食过哪怕半星肉末或一滴清水。恶兽已被极度的饥饿彻底逼入了发狂的绝境。当听到钥匙在铁锁孔中转动的脆响时，它庞大如牛的身躯如炮弹般猛烈撞击着精钢铁链，暴虐的蛮力险些将深嵌在石墙底座里的铁环生生拔出！焦黄恶臭的唾液泡沫挂满它黑色的嘴角；猩红充血的双眼中喷涌着嗜血的癫狂；粗重急促的喘息顺着裸露的獠牙发出干瘪窒息的尖鸣。

我从油布皮包里掏出了那件死神的信物：那只从伦敦河岸街诺森伯兰旅馆盗取的、亨利·巴斯克维尔爵士穿过的旧黑皮靴。

我缓缓逼近暴躁低吼的恶犬，口中发出那种从它幼年起便用来指引血腥杀戮的尖锐嘶鸣。我将那只沾满干泥的旧鞋帮死死塞到它剧烈耸动的黑色湿润鼻孔前！我甚至粗暴地将磨损的鞋跟直接卡入它的血盆大口之中，逼迫它狠狠咀嚼着坚硬的牛皮，将内衬深处吸附的加拿大男爵人体汗液、体脂油脂与鲜血气味，深深吸入五脏六腑，直到它的兽脑被这种独特的气味彻底烧沸！

狂暴的效果在半秒钟之内显现无遗！

恶兽喉咙深处猛地爆发出一声深沉窒息的狂喜呜咽！它的尾巴犹如铁棍般狂暴地抽打着石板地面；颈项上的肌肉因极度亢奋而高高坟起；四爪在泥地上疯狂抓挠出深沟！它记住了这个气味！它狂暴的心智清晰地意识到，只要撕碎这个散发着汗臭的活人，它腹中的烈火便能得到无尽的甘霖！

我将旧皮靴置于石架上，抓起了盛满特制白磷冷光油膏的广口瓶。我握着野猪鬃硬毛刷，以娴熟冷酷的手法，迅速为它披上死神的战甲。

我将那层冰冷而散发着幽光的剧毒油膏均匀涂刷在它凹陷的眼眶周围，直到它的两只眼睛在黑暗中宛如燃烧着地狱硫磺的深坑；我将毛刷狠狠扫过它獠牙的齿缝边缘、黑亮滴涎的嘴唇，以及胸膛与颈下层层下垂的狰狞鬃毛。

在工棚外，暮色已然被漫天滚滚翻涌、湿冷粘稠的雪白大雾所彻底吞噬。刺骨的寒风在残破石板屋顶的裂隙间发出凄厉如鬼哭的尖啸。

我大步跨到恶犬颈项前，右手死死攥住黄铜项圈上的弹簧插销，啪的一声按下了扳手！

‘杀！’我指着工棚大敞四开的大门厉声咆哮，‘循着气味，撕碎他的喉咙！’

那头恶魔巨兽如同一道从九幽深渊中撕裂而出的霹雳雷霆，轰然暴起扑入了浓雾！

一团燃烧着惨绿与幽蓝交织烈焰的夺命鬼火，在漆黑翻滚的泥浆表面凌空飞跃，巨大的脚爪踏过致命的沼泽，咆哮着瞬间撕开漫天雪白的死雾，狂暴扑向黑色岩岗的方向！

我迈步踏上工棚门槛，在凛冽的夜风中因极致的捕食快感而剧烈战栗，耳朵警惕地竖起偏向悬崖方向，耐心静候着即将响彻天际的绝命惨嚎，向星空宣告我无上的凯旋！"""
    },

    # Chapter 12 Part 1
    {
        "id": "stapleton_ch12_part1_screams_on_crags",
        "ch_idx": 11, "part": 1,
        "title_en": "Chapter 12: Death on the Moor (Part I: The Hound Unleashed)",
        "title_cn": "第十二章 沼地的惨剧（上：巨兽出柙与夜空绝叫）",
        "pov": "stapleton", "type": "anchor", "anchor": "anchor_screams_stapleton",
        "clues_en": [
            "Stapleton tracks the hound’s progress by its muffled bays echoing off the crags",
            "A scream of mortal terror and a heavy falling crash ring out near Black Tor",
        ],
        "clues_cn": [
            "斯台普吞循着恶犬在花岗岩裂谷间激荡回响的恐怖长嚎，紧随其后见证收割成果",
            "黑色岩岗方向骤然炸响一声撕心裂肺的垂死人类惨呼与重重坠崖摔碎的沉闷巨响",
        ],
        "choices_en": [
            {"id": "s_ch12_p1_c1", "text": "Hasten with your lantern to inspect the broken corpse at the foot of the cliff.", "target": "stapleton_ch12_part2_confronting_holmes"},
            {"id": "s_ch12_p1_c2", "text": "[Switch POV to Sherlock Holmes] View Holmes discovering the dead convict in Sir Henry’s suit.", "target": "holmes_ch12_part2_selden_death", "pov_switch": "holmes"},
        ],
        "choices_cn": [
            {"id": "s_ch12_p1_c1", "text": "手提马灯快步穿过乱石滩赶往绝壁脚下，亲手检验亨利爵士脑浆迸裂的尸骸成果。", "target": "stapleton_ch12_part2_confronting_holmes"},
            {"id": "s_ch12_p1_c2", "text": "【视角切换：歇洛克·福尔摩斯】切换至悬崖底部，目睹福尔摩斯如何擦亮火柴识破死者乃逃犯替身。", "target": "holmes_ch12_part2_selden_death", "pov_switch": "holmes"},
        ],
        "content_en": """I followed the fiery trail of the beast at a distance of three hundred yards, moving across the heather with the swift, silent stealth of a panther, my unlit dark-lantern clutched in my left hand.

The autumn fog had rolled into every valley and depression, turning the hollows into lakes of swirling white vapour from which the black granite tor-crests rose like jagged islands in an arctic sea. The silence was absolute, broken only by the whistling of the freezing wind through the gorse.

Then, echoing off the vertical cliffs of Black Tor, the baying began!

It was a sound to freeze the blood of the bravest soldier—a deep, rolling, hollow roar that reverberated through the granite tors like subterranean thunder! The hound was in full cry! It had struck the scent! It was coursing across the high stony plateau at the speed of a racehorse!

I broke into a dead run, my boots tearing through the bilberry scrub, my breath coming in short, exultant gasps.

Suddenly, high upon the crags half a mile to my right, a human voice shrieked aloud into the night—a piercing cry of mortal agony and despair that rent the freezing air!

“Help! Help! For God’s sake, help!”

The scream was choked off by a savage, frenzied snarling of iron jaws and the dull thud of heavy paws bounding across the turf! A wild scramble of feet echoed across the shale—the frantic, blind flight of a hunted man running for his life along the razor-edge of a sheer granite precipice!

A second shriek tore through the mist, rising to a dreadful, blood-chilling crescendo:

“No! Keep off! Oh, God—ahhhhh!”

Then came a sound that turned my triumph into ice—a sickening, splintering crash at the foot of the fifty-foot cliff! The heavy, bone-breaking thud of a human body smashing headlong onto the jagged granite boulders below!

Silence fell over the moor. Complete, terrible, unbroken silence.

My heart surged with a wave of wild, dizzying delirium!

He had fallen! The hound had driven Sir Henry Baskerville over the edge of the precipice! The Canadian heir lay dashed to pieces upon the rocks! 

The direct line was extinct! The £740,000 was mine! The title, the ancestral halls, the golden securities—all mine!

I struck a vesta match, touched the wick of my lantern, pulled down the shutter, and sprinted with leaping strides through the dark boulders towards the base of the crag to gaze upon my fallen enemy!""",
        "content_cn": """我手提熄灭的马灯，在恶兽后方三百码远的距离如鬼魅般在石楠苔原上全速跟进，身形轻盈迅捷宛如暗夜巡猎的黑豹。

深秋的浓雾已然填满了每一处低洼的谷地与沟壑，将低处的沼泽化作了一片翻滚涌动的白浪海洋，唯有一座座漆黑险峻的花岗岩峰峦如北冰洋中的黑色孤岛般刺破云海。整片荒原死寂无声，唯有刺骨的寒风呼啸着穿透枯萎的金雀花丛。

突然之间，从黑色岩岗垂直耸立的花岗岩峭壁方向，猛然炸响了惊天动地的狂暴狂吠！

那是一声足以令最勇敢的战士骨髓彻底结冰的恐怖咆哮——一声沉闷、悠长、如地底闷雷般在乱石绝壁间激荡回响的狂吠！恶犬已然彻底锁定了气味！它在以赛马般狂飙的时速，在崎岖的花岗岩高原上疯狂追杀！

我立刻迈开大步亡命狂奔，皮靴在碎石与湿泥炭上飞掠而过，呼吸急促而充斥着捕猎收割的狂喜。

电光石火之间，在相距我右侧半英里外的高耸绝壁之巅，一个人类的嗓音在极度的绝望中爆发出了撕心裂肺的凄厉惨叫，骤然撕裂了冰冷的寒夜！

‘救命！救命！看在上帝的份上，救救我啊——！’

呼救声在一瞬间被一阵狂暴凶残的獠牙撕咬声与巨爪践踏声所打断！碎石在悬崖边沿疯狂倾泻坍塌——那是一个亡命徒在悬崖绝壁边缘被死神紧逼时的绝望奔逃！

紧接着，第二声凄厉至极的破胆尖叫撕裂了茫茫雾海，拔高为一声撕碎灵魂的绝命惨呼：

‘不！滚开！啊，上帝啊——啊啊啊啊！’

下一秒，在五十英尺高的垂直绝壁脚下，骤然回荡起一声令人毛骨悚然、骨骼寸寸碎裂的沉闷撞击巨响！肉体与头颅狠狠砸在坚硬花岗岩巨石上时的钝响！随后，天地重归永恒的冰冷死寂。

死一般的沉寂笼罩了荒原。

一股近乎令我窒息的狂热狂喜如山洪爆发般瞬间淹没了我的神智！

他坠崖了！我的恶犬终于将亨利·巴斯克维尔逼下了万丈深渊！那个粗鄙的加拿大农夫，此刻已然在悬崖底部撞得粉身碎骨、脑浆涂地！

巴斯克维尔的直系血脉彻底断绝！七十四万英镑是我的了！古老的爵位、祖传的城堡、金光闪闪的金边债券——全都是我的了！

我擦亮火柴点燃了手中的马灯，迈开轻快狂喜的大步，在漆黑错落的花岗岩乱石滩上飞速前行，急不可耐地要亲眼鉴赏我亲手缔造的尸骸杰作！"""
    },

    # Chapter 12 Part 2
    {
        "id": "stapleton_ch12_part2_confronting_holmes",
        "ch_idx": 11, "part": 2,
        "title_en": "Chapter 12: Death on the Moor (Part II: Face to Face with Sherlock Holmes)",
        "title_cn": "第十二章 沼地的惨剧（下：错杀逃犯与遭遇福尔摩斯）",
        "pov": "stapleton", "type": "branch", "anchor": None,
        "clues_en": [
            "Corpse is not Sir Henry, but Selden the convict wearing Sir Henry’s old clothes",
            "Sherlock Holmes is standing by the body in the flesh alongside Dr. Watson",
            "Stapleton is forced to play the innocent neighbour while his life hangs by a thread",
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
        "content_en": """I swung my lantern around the massive base of the crag, my pulse racing with predatory triumph, stepping eagerly towards the dark, crumpled heap that lay sprawled upon the scree.

Two men were already standing over the corpse.

I raised the lantern. The bright yellow beam struck the face of the taller man—and every drop of blood in my body turned to liquid ice!

Sherlock Holmes!

He was standing erect, wrapped in his dark ulster, his keen, eagle face set in lines of iron determination, his grey eyes piercing the gloom like cold daggers! And beside him, his service revolver cocked in his right hand, stood Dr. John Watson!

My soul convulsed in dizzying, paralyzing terror! But worse—infinitely worse—was the horror that greeted my eyes upon the ground!

The dead man was dressed from neck to heel in Sir Henry’s unmistakable ruddy tweed suit—the very suit he had worn in London! But the face turned up to the lantern light was not the clean-shaven, handsome countenance of the Canadian baronet! It was a brutal, low-browed, bestial visage, framed in a filthy, matted black beard—the mangled corpse of Selden, the Notting Hill convict!

Selden! 

The hound had hunted the clothes, not the man! Barrymore had given the discarded Canadian garments to his starving brother-in-law, and my starved demon had torn the wrong throat!

Every nerve in my brain screamed in frustrated, murderous fury! I stood within thirty inches of the greatest detective in Europe, and if my face betrayed one flicker of guilt, the handcuffs would close upon my wrists!

I summoned every atom of my will to force my mouth into an expression of bewildered, horrified innocence.

“Mr. Holmes!” I stammered, my throat dry as lime. “Is it possible? What an unexpected honour! And... who is this unfortunate gentleman?”

Holmes looked at me with cool, impenetrable amusement. “An escaped convict, Mr. Stapleton. He appears to have broken his neck among the rocks. A very ordinary accident. My friend Watson and I return to London tomorrow; our little holiday in Devonshire is at an end.”

He was leaving! Holmes was returning to London!

He did not know! The fool had seen only an accident! He had missed the scent, the boot, the phosphorus, everything!

I bowed, uttered a few hypocritical condolences with shaking lips, and turned into the fog towards Merripit House. My knees trembled with reaction, but my brain was afire with renewed, desperate resolve.

One last chance remained! Tomorrow night, Sir Henry was engaged to dine with me at Merripit House. If Holmes was in London, the baronet would walk home alone across the moor at ten o’clock! And this time, there would be no mistake!""",
        "content_cn": """我提着马灯转过悬崖底部的巨石转角，迫不及待地大步迈向横卧在碎石中的那滩扭曲血肉。

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
    },

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
        "content_en": """The evening of October 24th was the grand climax towards which every beat of my heart had driven me for six grueling months.

At three o’clock that afternoon, Beryl had fallen upon her knees before me in the dining-room, clawing at my coat, weeping that she would throw herself into the Great Grimpen Mire before she allowed me to murder Sir Henry under our roof.

I wasted no breath on argument. I struck her across the temple with my clenched fist. While she lay stunned upon the rug, I bound her wrists and ankles with stout window-sash cords, gagged her with a silk scarf knotted behind her ears, dragged her up the stairs to the rear bedroom, and lashed her securely to an upright of the brass bedstead. I locked the oak door, double-turned the key, and placed it in my waistcoat pocket.

At seven o’clock, Sir Henry Baskerville arrived alone.

He was in radiant spirits, brimming with robust Canadian health. He confirmed that Holmes and Watson had indeed taken the morning express from Coombe Tracey to London.

“A pity Mr. Holmes could not join us,” I remarked with suave regret, filling his glass with vintage port. “A brilliant mind, no doubt, but perhaps a trifle eccentric for rustic tastes.”

Dinner was a triumph of deceit. I was the gracious, witty host, discussing timber tracts and Canadian railways. Sir Henry drank deeply, his eyes straying wistfully towards the empty chair, visibly downcast by Beryl’s “severe, sudden migraine.”

At twenty minutes to ten, I rose, made an excuse of consulting the weather, and slipped into the scullery.

I pushed open the back door. Nature had allied herself with my genius!

From the Great Grimpen Mire, a dense, blinding bank of white fog was rolling inland across the heather like a tidal wave! Within fifteen minutes, the path between Merripit House and the Hall would be completely submerged! A man walking the moor path in that impenetrable white wall would be blind and helpless as a newborn babe!

I ran to the stone outhouse where I had concealed the hound. I smeared the cold, oily phosphorus paste over its jaws, its eyes, and along the ridges of its spine until it blazed with hellish green fire!

Ten o’clock chimed from the tall clock in the hall. Sir Henry was buttoning his coat in the vestibule! The hour of retribution was here!""",
        "content_cn": """十月二十四日的这个良夜，是我整整六个月呕心沥血布下这盘惊世棋局的最高潮！

午后三点，贝丽尔再次如疯妇般跪倒在餐厅的地板上死死抓紧我的下摆，歇斯底里地哭喊发誓若我敢在今晚谋害亨利爵士，她便一头撞入泥潭万劫不复。

我再也没有跟她多费半句唇舌。我一记重拳狠狠抽在她的太阳穴上。趁着她头晕目眩瘫软在地毯上之际，我用厚重的窗帘粗绳死死绑紧了她的手腕与脚踝，用一条厚丝巾塞入口腔打结封嘴，将她粗暴地拖上二楼后侧次卧，牢牢绑在冰冷的黄铜床柱之上。我反锁了房门，将沉甸甸的钥匙揣入贴身口袋。

晚间七点整，亨利·巴斯克维尔爵士单刀赴会、如约而至。

他显得兴致极高，红光满面，充满着年轻人的勃勃生机。他亲自向我证实，福尔摩斯与华生确实已搭乘清晨的西行列车返回了伦敦。

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
        "content_en": """I watched from the black shadow of the scullery door as Sir Henry stepped out into the night. He paused at the garden gate, buttoned his collar against the chill, and set off briskly along the stone cart-track that led towards Baskerville Hall.

Within thirty yards, the dense, white wall of fog swallowed him up.

Now!

I dashed to the outhouse, threw open the door, and slipped the heavy brass lead from the hound’s collar.

“Go, boy!” I snarled into its ear. “Tear him to ribbons!”

With an earth-shattering roar, the monster leaped into the fog! A streak of emerald flame, bound after bound across the heather! In two seconds, it had vanished into the white shroud of vapour.

I stood upon the gravel, my pulse hammering in savage, triumphant ecstasy, waiting for the screams of death.

One second... three seconds... five seconds...

Suddenly, a voice of thunder tore through the fog:

“Look out! It’s coming!”

Sherlock Holmes!

Before my brain could grasp the catastrophe, the night exploded into sheets of orange flame!

Crack! Crack! Crack! Crack! Crack!

A volley of heavy revolver shots ripped through the mist! A shriek of agony—a dreadful, animal howl of dying fury—rent the heavens! The sound of a heavy body thrashing in the heather... a final, sharp pistol shot... and then, a dying rattle that ceased into total silence.

My hound was dead!

Holmes had laid an ambush in the rocks! The law was fifty yards from my door, armed and closing the net!

Blind panic shattered my nerves! The gallows of Exeter loomed before my eyes! I whirled, bolted into the house, seized my boots, and fled into the swirling fog of the Great Grimpen Mire!""",
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
        "content_en": """I plunged blindly into the churning white fog of the Great Grimpen Mire, my heart knocking against my ribs like a dying beast.

Behind me, the shouts of men echoed across the heather. I heard the sharp, imperious voice of Lestrade and the heavy pounding of police boots against the gravel! They had broken into Merripit House; they had released Beryl; she was guiding them to the back door!

I must reach my island fortress. In the tin shed lay my false passport, my golden sovereigns, and the stolen boots. From there, under the cover of night, I could strike north towards the Bristol Channel and board a tramp steamer for the Americas!

The fog was an impenetrable wall of curdled milk. I could not see my own hands stretched before my face. I stepped onto the secret bog-path, gasping for air.

Two paces forward... leap to the flat granite boulder... three paces across the firm peat...

Where was the willow wand? 

I reached out into the blinding mist, my bleeding fingers sweeping the empty air. The guide-stick had vanished! Had a wild pony trodden it into the mire? Had the rising black water washed it away?

A scream of animal terror broke from my throat! In blind panic, I took a wild, desperate stride forward!

The earth dissolved beneath my right boot!

It did not crack—it gave way like cold grease! A sickening, jelly-like suction seized my ankle and dragged me down!

“No!” I shrieked, throwing my body backward, clawing frantically at the false green moss.

The moss tore away in my bleeding hands. My knee sank into the foul, bubbling black slime. The more I kicked, the deeper the subterranean vacuum dragged me down! The icy, foul-smelling mud rose to my waist—to my chest! The sulfurous stench of the ancient bog choked my lungs.

Far across the waste, the distant whistle of the night express tore through the fog. Civilization! Wealth! Life! All slipping away into the black abyss!

“Beryl!” I screamed into the void. “Help me!”

Only the gurgling bubbles of the mire answered. The cold slime closed over my chin, over my lips, over my staring eyes.

The Great Grimpen Mire held me forever in its bottomless embrace.""",
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
]
