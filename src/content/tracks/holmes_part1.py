# src/content/tracks/holmes_part1.py
"""Sherlock Holmes Perspective: Chapters 1 through 5 (Expanded Novel-Length Edition).
Covers:
- Ch 1: The Science of Deduction & Mortimer's Walking Stick / The 1742 Manuscript
- Ch 2: The Legend of Hugo Baskerville / Footprints of a Gigantic Hound
- Ch 3: Dartmoor Topography & The Shag-Smoke Vigil
- Ch 4: The Cut-out Times Letter & Regent Street Hansom Chase (Cab 2704)
- Ch 5: Three Broken Threads, Cabman John Clayton, & The Covert Strategy
"""

HOLMES_NODES_PART1 = [
    # -------------------------------------------------------------------------
    # Chapter 1: Part 1
    # -------------------------------------------------------------------------
    {
        "id": "holmes_ch01_part1_observation",
        "ch_idx": 0, "part": 1,
        "title_en": "Chapter 1: Mr. Sherlock Holmes (Part I: The Science of Deduction)",
        "title_cn": "第一章 歇洛克·福尔摩斯先生（上：演绎的科学与手杖）",
        "pov": "holmes", "type": "anchor", "anchor": "anchor_chapter1_holmes",
        "clues_en": [
            "Mortimer walking stick worn iron ferrule indicates rural gravel walking",
            "C.C.H. 1884 inscription resolves to Charing Cross Hospital house-surgeon",
            "Tooth impressions identify a curly-haired spaniel retriever",
        ],
        "clues_cn": [
            "摩梯末手杖磨损过半的铁箍印证了德文郡荒原碎石路的长期跋涉",
            "C.C.H. 1884铭文证实其为查令十字医院五年前离职的青年外科医士",
            "手杖齿痕精准测定为一只卷毛西班牙猎犬所留",
        ],
        "choices_en": [
            {"id": "h_ch1_p1_c1", "text": "Greet Dr. James Mortimer and invite him to explain his extraordinary visit.", "target": "holmes_ch01_part2_consultation"},
            {"id": "h_ch1_p1_c2", "text": "[Switch POV to Dr. Watson] View Mortimer from Watson’s sympathetic gaze.", "target": "ch01_part2_mortimer", "pov_switch": "watson"},
        ],
        "choices_cn": [
            {"id": "h_ch1_p1_c1", "text": "迎接杰姆士·摩梯末医生入座，请他陈述此番非同寻常的来访缘由。", "target": "holmes_ch01_part2_consultation"},
            {"id": "h_ch1_p1_c2", "text": "【视角切换：约翰·H·华生】以华生医生的同理心视角端详这位来客。", "target": "ch01_part2_mortimer", "pov_switch": "watson"},
        ],
        "content_en": """The autumn sun broke through the yellow haze of Baker Street, casting pale, slanting rectangles of light across our sitting-room rug. I sat at the breakfast-table, my back deliberately turned towards the hearth, leaning back in my armchair while the bitter steam from my black coffee curled upward. In the polished convex surface of the silver-plated coffeepot before me, the whole room was distorted into a miniature, curved panorama: the bookshelf, the coal-scuttle, and the upright, earnest figure of Dr. John H. Watson standing upon the bearskin rug.

For ten full minutes Watson had been turning over the heavy walking stick left behind by our unknown nocturnal visitor. I watched his reflection with silent relish. His brow was furrowed into deep ridges of concentration; he squinted through his brows, tapped the wood against his knuckles, and held the silver band up to the morning light as though he were deciphering a Greek palimpsest.

“Well, Watson,” said I softly, without turning my head, “what do you make of it?”

He started violently, nearly fumbling the cane. “How in heaven’s name did you know what I was doing?” he gasped, blinking at my shoulders. “I could swear you have eyes in the back of your head, Holmes!”

“I have, at least, a very well-polished silver-plated coffee-pot in front of me,” I replied with a dry chuckle, turning my chair round to face him. “You see, Watson, you provide me with perpetual entertainment. Since we were so unfortunate as to miss our caller last evening and had no inkling of his errand, this accidental souvenir becomes an object of capital importance. Come, let me hear you reconstruct the man by a rigorous examination of his stick.”

Watson squared his shoulders, cleared his throat, and assumed that peculiarly grave, judicial expression which he reserves for medical consultations. “I think,” said he, following as best he could the methods I had so frequently demonstrated, “that Dr. Mortimer is a successful, elderly medical man, held in high esteem, since those who know him have bestowed this mark of appreciation upon him.”

“Good!” I nodded encouragingly. “Admirable!”

“I think also that the probability is in favour of his being a country practitioner who does a great deal of his visiting on foot.”

“Why so?”

“Because this stick, though originally a handsome piece of timber, has been so knocked about that I can hardly imagine a town practitioner carrying it. The thick iron ferrule is worn down to half its depth, so it is evident that he has done an immense amount of rough walking with it.”

“Perfectly sound!” said I. “Your observation of the ferrule does you credit.”

“And then again,” Watson continued, visibly flushed with triumph, “there is the engraving: ‘To James Mortimer, M.R.C.S., from his friends of the C.C.H., 1884.’ I should hazard a guess that C.C.H. stands for the Something Hunt—the Charlington or Cambridgeshire Hunt—to whose sportsmen he has rendered some timely surgical aid, in return for which they presented him with this sturdy Penang lawyer.”

I pushed back my chair, struck a wax match, and lit my morning pipe of pungent shag tobacco. “Really, Watson, you excel yourself. I am bound to say that in all the accounts with which you have favoured the public regarding my own small achievements, you habitually underrate your own faculties. It may be that you are not yourself luminous, but you are undeniably a conductor of light! Some men, lacking genius themselves, possess an extraordinary power of stimulating it in others. I confess, my dear fellow, that I am deeply in your debt.”

Watson beamed with an honest, boyish pride that was touching to witness. It was almost cruel to dispel so innocent a satisfaction, yet the severe laws of science cannot bow to sentiment. I reached out and took the stick from his grasp, placing it across my knees beneath the bright glare of my pocket magnifying lens.

“Interesting, though elementary,” I remarked, tracing the grain of the wood. “There are certainly several distinct indications upon this timber which furnish the basis for half a dozen certain deductions. I am afraid, my dear Watson, that most of your conclusions were completely erroneous.”

Watson’s smile faded into an injured pucker. “Erroneous? Has anything of consequence escaped me?”

“Almost everything of capital importance,” I answered, rotating the cane beneath the glass. “Consider the facts. When I said that you stimulated me, I meant that in noting your fallacies I was guided directly towards the truth. First: could a man presented with this stick be an elderly, established physician? Assuredly not. The initials C.C.H. do not stand for a hunt; hunts do not present modest Penang lawyers, nor do they append the letters of medical qualification. Turn your gaze to the Medical Directory on the shelf behind you. C.C.H. is Charing Cross Hospital. And who receives a presentation upon leaving a great London hospital? Only a young house-surgeon or house-physician who has completed his residency! The date is 1884—precisely five years ago. Our man is therefore not an elderly, venerable practitioner, but a young fellow under thirty, amiable, unambitious, absent-minded, and the possessor of a beloved dog.”

“A dog!” cried Watson in sheer bewilderment. “Where on earth do you find a dog?”

I pointed the tip of my lens at the middle of the shaft. “Here, running horizontally across the wood, are unmistakable tooth-impressions. The marks of the canine teeth are clearly defined. A dog has carried this stick behind its master by the balance-point. Look at the breadth of the jaw: too broad for a terrier, yet far too narrow for a mastiff. Notice the tiny white curl of canine hair lodged in the rough grain near the lower tooth-dent. It is, beyond question, a curly-haired spaniel.”

As the words left my lips, the sharp clatter of paws echoed from the pavement below, followed by the firm jangle of our front-door bell. I glanced through the lace curtains to the street.

“And there, Watson,” I added with a smile, “stands the gentleman in question: a tall, thin figure in tweed, with a curly-haired spaniel panting at his heels!”""",
        "content_cn": """秋日的晨曦冲破贝克街上空泛着硫磺味的昏黄雾气，将几道狭长而惨白的斜射光斑投洒在我们起居室的波斯地毯上。我坐在早餐桌旁，背对着壁炉，懒散地陷在扶手椅深处，任由面前浓黑咖啡散发的微苦热汽在晨光中袅袅升腾。在那只擦拭得纤尘不染、泛着冷冽银光的镀银咖啡壶的凸面上，整个房间被压缩成一幅微缩而扭曲的全景图：高耸的书架、煤斗、以及伫立在熊皮地毯上、神情肃穆庄重的约翰·H·华生医生。

在过去的整整十分钟里，华生一直翻来覆去地摆弄着昨夜那位神秘访客遗落在此的粗大手杖。我透过银壶的反光，暗自欣赏着他的一举一动。他的眉头紧锁成几道深刻的纵纹，眼神专注而严苛，时不时用手指关节敲击着坚硬的木质，又将镶嵌在杖头下方的银箍凑到光亮处细细端详，其审慎的模样宛如学者在破译一份湮没千年的希腊古卷。

‘那么，华生，’我无需回头，只是用平静而柔和的语调开口道，‘对于这件器物，你究竟得出了什么高见？’

华生浑身猛地一震，手中的手杖险些脱手滑落。‘看在上帝的份上，福尔摩斯，你怎么知道我在做什么？’他转过身，瞪大双眼难以置信地盯着我的后背，‘我敢发誓你后脑勺上一定长着一双眼睛！’

‘眼睛倒是没有，但我面前恰好有一把反光极佳的纯银咖啡壶，’我轻笑一声，转过椅子正对着他，‘你总是能给我带来无穷的智力乐趣，华生。既然昨晚我们十分不巧地错过了那位来客，对其来意一无所知，那么这根偶然留下的纪念物就具有了第一流的重要性。来吧，让我听听你如何运用严密的观察法，依据这根手杖重构其主人的全貌。’

华生挺直了胸膛，清了清嗓子，脸上浮现出那种他在诊所面对疑难病症时特有的庄严神情。‘我认为，’他努力模仿着我平日展示的推导程序，字斟句酌地说道，‘这位摩梯末医生是一位功成名就、备受尊敬的老牌医生，因为唯有德高望重之人，才能从相识之人手中获赠这样一份表达敬意的精美纪念品。’

‘很好！’我鼓励地点了点头，‘精彩极了！’

‘我还认为，他极有可能是一位在乡间行医的乡村医生，而且大部分出诊全凭步行。’

‘何以见得？’

‘因为这根手杖虽然选料考究，乃是一根上好的槟榔屿杂木，但它受到的磕碰和磨损实在太严重了，城里的体面医生绝不可能随身携带这样一根满是伤痕的手杖。你看，杖底那枚厚重的铁箍已经被粗糙的碎石路磨去了一半，这无可辩驳地证明他曾拄着它跋涉过极其漫长而艰险的泥泞道路。’

‘丝丝入扣！’我赞许道，‘能注意到铁箍的磨损程度，这很见功力。’

‘不仅如此，’华生受到赞许，面颊泛起兴奋的红晕，声音也洪亮了几分，‘还有银箍上的刻字：“谨以此赠杰姆士·摩梯末医士（M.R.C.S.），C.C.H.诸友人赠，一八八四年。”我推测，这个所谓的C.C.H.，必然是当地的某种乡村狩猎俱乐部——比如查林顿狩猎会（Charlington Hunt）或者剑桥郡狩猎会。摩梯末医生必定是在某次狩猎事故中为落马的乡绅提供了高超的外科急救，那些心怀感激的猎手们便集资赠送了他这根结实的杂木防身手杖。’

我推开餐椅站起身，划燃一根硫磺火柴，点燃了清晨那斗辛辣刺鼻的黑烟丝。‘坦白讲，华生，你真让我刮目相看。在我发表的那些关于我个人微末成就的纪实文字中，你总是过分贬低自己的才能。你自己或许并非璀璨的发光体，但你却无可否认是一根绝佳的“光之导体”！世间有些人虽然自身不具备天才，却拥有一种激发他人灵感的不凡魔力。我必须承认，我亲爱的朋友，我欠你一份极大的情谊。’

华生脸上洋溢着一种近乎孩童般的纯真自豪。看着他如此由衷的欣慰，我几乎不忍心去戳破这层美丽的假说；然而科学的法则严苛无情，绝不容许向温情妥协。我伸出手，从他手中取过手杖，横置在膝盖上，旋即从西装口袋中取出高倍放大镜，在清晨的充足光线下逐寸审视。

‘确实很有意思，尽管依然属于初级范畴，’我用指尖划过木材的纹理，‘木头上铭刻的几处客观事实，足以构成半打确定无疑的演绎基石。然而，我亲爱的华生，我不得不遗憾地指出，你的绝大部分结论都南辕北辙了。’

华生嘴角的微笑顿时凝固了，神情显得颇受打击。‘谬误？难道我遗漏了什么决定性的线索？’

‘几乎遗漏了所有关乎本质的核心，’我一边用放大镜旋转着手杖，一边从容不迫地说道，‘请审视事实：获赠这根手杖的人，会是一位年迈德高望重的资深医士吗？绝无可能。C.C.H.绝非狩猎俱乐部；乡间猎手绝不会赠送一根平实的杂木手杖，更不会在刻字时大费周折地附上皇家外科学会会员（M.R.C.S.）这种学术头衔。请你把目光投向身后书架上的那本《英国医学名录》。C.C.H.是伦敦著名的查令十字医院（Charing Cross Hospital）！而在什么样的情况下，一个人会在离开一家伦敦顶尖教学医院时获赠纪念品？唯有完成实习轮转、即将离职的年轻住院外科或住院内科医生！铭文的年份是一八八四年——距今整整五年。因此，我们的来客绝非迟暮长者，而是一位未满三十岁的年轻医生，性格温和、缺乏野心、心不在焉，并且拥有一只他形影不离的心爱爱犬。’

‘一只狗！’华生失声惊呼，满脸茫然，‘看在老天的份上，你到底从哪儿看出了一只狗？’

我将放大镜的聚焦点稳稳落在手杖中段的一处浅凹上。‘看这里。横贯木质纤维的中段，留有一串极其鲜明的齿痕。犬齿刺破清漆留下的压痕清晰可辨。显然，这只狗经常叼着手杖的正中心平衡点，欢快地跟在主人身后小跑。再仔细测量上下颚咬合齿距：齿宽远超普通的㹴犬，却又明显逊色于粗壮的马士提夫獒犬。此外，注意看下排牙齿凹陷处深深卡着的一小簇极细的白色卷毛——毫无疑问，这是一只卷毛西班牙猎犬。’

话音未落，楼下潮湿的石阶上骤然传来了一阵急促欢快的爪子扑腾声，紧接着，门厅的大铜铃发出了清脆而坚决的铮铮鸣响。我走到窗前，撩开蕾丝窗帘的一角，俯瞰着清晨薄雾弥漫的街道。

‘看吧，华生，’我微笑着示意他凑过来看，‘那位当事人已经登门了：一位身材瘦长、身披粗花呢大衣的年轻绅士，而在他的脚边，正跟着那只气喘吁吁、吐着舌头的卷毛西班牙猎犬！’"""
    },

    # -------------------------------------------------------------------------
    # Chapter 1: Part 2
    # -------------------------------------------------------------------------
    {
        "id": "holmes_ch01_part2_consultation",
        "ch_idx": 0, "part": 2,
        "title_en": "Chapter 1: Mr. Sherlock Holmes (Part II: The 1742 Manuscript)",
        "title_cn": "第一章 歇洛克·福尔摩斯先生（下：颅骨研究与1742年手稿）",
        "pov": "holmes", "type": "branch", "anchor": None,
        "clues_en": [
            "Dr. James Mortimer is a passionate physical anthropologist and comparative anatomist",
            "1742 Baskerville parchment describes the demonic hound curse originating with Hugo Baskerville",
            "Mortimer considers Holmes the second-highest expert in Europe after Monsieur Bertillon",
        ],
        "clues_cn": [
            "摩梯末医生痴迷于比较解剖学与颅骨测量学，随身携带人体骨骼研究文献",
            "1742年巴斯克维尔家族泛黄手稿详述邪恶领主雨果招致地狱猎犬世袭诅咒的原委",
            "摩梯末直言在精准科学分类上福尔摩斯仅次于巴黎法医贝蒂荣，令名侦探深感被挑衅",
        ],
        "choices_en": [
            {"id": "h_ch1_p2_c1", "text": "Listen attentively as Mortimer reads the dark 1742 manuscript aloud.", "target": "holmes_ch02_part1_legend"},
            {"id": "h_ch1_p2_c2", "text": "Demand Mortimer skip the ancient myth and present the recent physical evidence.", "target": "holmes_ch02_part2_footprints"},
        ],
        "choices_cn": [
            {"id": "h_ch1_p2_c1", "text": "保持专注，倾听摩梯末医生逐字宣读这份来自1742年的古老黑暗手稿。", "target": "holmes_ch02_part1_legend"},
            {"id": "h_ch1_p2_c2", "text": "打断神话传说，要求摩梯末医生直接呈报关乎当下的最新现场物理物证。", "target": "holmes_ch02_part2_footprints"},
        ],
        "content_en": """The door opened to the measured tread of our visitor. Dr. James Mortimer was an extraordinarily tall, thin man with a long beak of a nose projecting between two keen, grey eyes that twinkled brightly from behind a pair of gold-rimmed spectacles. His frock-coat was dingy and his trousers frayed, yet there was that in his bearing which bespoke the scholar. To my infinite amusement, the curly-haired spaniel made an immediate dart for the hearth-rug, curling up with a heavy canine sigh.

“I had feared,” said our visitor, bowing with formal old-world courtesy, “that I might have left my walking stick here last night. I would not lose that stick for the world.”

“A presentation, I observe,” said I.

“Yes, sir, from friends at Charing Cross Hospital on the occasion of my marriage.”

“Ah! Your marriage!” I shot a glance of malicious triumph at Watson, whose jaw slackened in rueful surrender. “And you retired to the country?”

“Precisely, Mr. Holmes. I married and settled in Grimpen, Dartmoor, where my scientific pursuits in comparative pathology and craniology could be conducted far from the noise of London.” Mortimer suddenly fixed his gaze upon my brow with unmasked scientific passion. “Indeed, sir, you have an extraordinary skull! I had hardly expected such marked dolichocephalic development with such well-pronounced supra-orbital ridges. A cast of your skull, Mr. Holmes, until the original becomes available, would be an ornament to any anthropological museum in Europe!”

Watson stared in horror at this cheerful contemplation of my post-mortem cranium. I could not repress a dry smile. “You are an enthusiast in your line of thought, sir, as I am in mine. But I presume it was not merely to examine my parietal bones that you honoured me with your visit?”

“No, sir, no! Though I am happy to have had the opportunity. I come to you, Mr. Holmes, because I am confronted with a problem so singular, so dark, and so completely outside the pale of ordinary human experience that only the second highest expert in Europe could unravel it.”

I stiffened slightly in my armchair. “Indeed, sir? And may I inquire who possesses the honour of being the first?”

“To the man of precisely scientific mind, Monsieur Bertillon of Paris must always claim the pre-eminence,” Mortimer replied with disarming candour.

“Then had you not better consult him?” I asked with freezing politeness.

“Monsieur Bertillon, Mr. Holmes, is a master of physical measurement and classification. But for the balance of forces, the weighing of subtle psychological motives, and the intuitive comprehension of the inexplicable, you stand without a rival. And the matter I bring before you involves the sudden, horrifying death of my friend and patron, Sir Charles Baskerville.”

The atmosphere of the room shifted in an instant. The faint scientific banter evaporated like morning frost. Sir Charles Baskerville’s death on Dartmoor three months prior had formed a three-line paragraph in the daily press: an elderly philanthropist dying suddenly of heart failure in his garden alley. But the haunted shadow in Mortimer’s eyes told a far more terrible tale.

Reaching into his breast-pocket, Mortimer drew forth a thick, yellowed packet of foolscap, folded flat and tied with a faded ribbon of green silk.

“This manuscript,” said Mortimer, laying it upon the breakfast table, “was entrusted to me by Sir Charles Baskerville three months before his lamented end. It is an heirloom of the Baskerville family, written in the year 1742. It sets forth the origin of that ghastly curse which has dogged that ancient house since the days of the Great Rebellion.”

I leaned forward, my pipe resting unheeded in my fingers. “You speak of a family legend, Dr. Mortimer. My practice is confined to this world and the living beings who inhabit it. Are you asking me to investigate an 18th-century ghost?”

“I am asking you, Mr. Holmes,” Mortimer replied, his voice dropping to a trembling whisper, “to hear the ancient chronicle, and then to examine the fresh, bloody footprints that stamped Sir Charles Baskerville into his grave!”""",
        "content_cn": """房门随着一阵沉稳的脚步声被推开。杰姆士·摩梯末医生是一位身材异乎寻常瘦高、面庞清癯的绅士。他生着一只鹰钩长鼻，鼻梁两侧镶嵌着一双敏锐而温和的灰色眼睛，在金丝边眼镜的镜片后闪烁着学者的睿智光芒。他的双排扣常礼服显得有些陈旧褪色，裤脚边也略有磨损，然而其举手投足间的儒雅风度，却彰显出其深厚的学识涵养。令我倍感莞尔的是，那只卷毛西班牙猎犬一溜烟窜进了屋里，直奔壁炉前的毛皮地毯，舒舒服服地蜷缩成一团，喉咙里发出一声惬意的呼噜声。

‘昨晚离去时我十分惶恐，’访客欠身行了一个无可挑剔的旧式绅士礼，‘唯恐将我的手杖遗失在了贵处。对我而言，哪怕倾尽家财，我也绝不愿失去那根手杖。’

‘我注意到那是一件赠礼，’我微笑道。

‘是的，先生，是我大婚之际，查令十字医院的同仁们所赠。’

‘哈！结婚的赠礼！’我意味深长地瞥了华生一眼，华生则报以苦涩而心悦诚服的无奈苦笑。‘于是您便退隐乡野了？’

‘正是如此，福尔摩斯先生。婚后我便定居在德文郡荒原边缘的格林盆村，唯有在远离伦敦喧嚣的静谧荒野，我关于比较病理学与颅骨测量学的科学研究才能得以潜心进行。’摩梯末医生的目光忽然牢牢钉在我的前额上，眼神中迸发出未加掩饰的解剖学狂热：‘老天啊，先生！您的颅骨结构真是太令人叹为观止了！我万万没有想到，在如此显著的长头型骨骼特征下，竟然发育出如此坚实深邃的眶上嵴！福尔摩斯先生，在您这具尊贵的颅骨尚无法制成标本之前，哪怕只是能得到一份翻模石膏像，也足以成为全欧洲任何一座人类学博物馆的镇馆之宝！’

华生目瞪口呆地听着这位年轻医生当面公然剖析我死后的头骨归宿，脸上写满了骇然。我却不由得哑然失笑。‘摩梯末医生，您在您的专业领域里显然是一位不折不扣的热狂者，恰如我在我的行当里一样。不过我想，您清晨造访寒舍，总不会仅仅是为了测量我的顶骨弧度吧？’

‘不，先生，绝非如此！尽管能亲眼瞻仰您的头骨确实令我不虚此行。’摩梯末医生的神情骤然阴沉下来，眼中的狂热被一种深深的阴霾与恐惧所取代，‘我之所以冒昧前来求助于您，福尔摩斯先生，是因为我正面临着一个极其诡谲、黑暗、且彻底超出了常规人类认知经验的惊天谜团——一个唯有全欧洲第二高的权威专家才有可能破解的谜团。’

我眉峰微挑，身子在扶手椅里微微挺直。‘哦？欧洲第二？那么敢问先生，在您心目中，谁有幸高居首位呢？’

‘对于真正崇尚严密科学分类的实证学者而言，巴黎的阿道夫·贝蒂荣（Bertillon）先生始终享有不可动摇的桂冠。’摩梯末以一种令人无法反驳的坦率回答道。

‘那您为何不干脆去巴黎向他请教？’我用一种冰冷而克制的礼貌反问道。

‘贝蒂荣先生是一位登峰造极的人体测量学大师，福尔摩斯先生。然而，若论及在错综复杂的犯罪迷雾中权衡微妙的心理动机、洞察蛛丝马迹背后的因果锁链、并以惊人的直觉重构不可思议的真相，全欧洲无人能望您项背！而我今天呈现在您面前的，正是我的挚友与赞助人——查尔斯·巴斯克维尔爵士骇人听闻的暴卒惨案！’

起居室内的空气仿佛在刹那间凝结了。方才关于颅骨与手杖的学术轻松气氛彻底消散在晨光中。三个月前，查尔斯·巴斯克维尔爵士在德文郡荒原庄园猝死的消息，曾在《泰晤士报》的讣告栏上占过短短三行的篇幅：一位年迈仁慈的慈善家，在自家庄园的花园散步道上突发心脏衰竭逝世。然而，摩梯末医生此刻眼底翻滚的惊骇，却分明预示着一个全然不同的恐怖深渊。

摩梯末颤抖着手伸入西装内侧口袋，取出一个沉甸甸、纸页发黄的长方形封套。封套被平整地折叠着，外层系着一根褪色的暗绿色丝带。

‘这份手稿，’摩梯末小心翼翼地将它放在我们餐桌的中央，声音发颤，‘是查尔斯·巴斯克维尔爵士在他悲惨辞世前三个月亲手托付给我的。这是巴斯克维尔家族世代相传的绝密祖训，定稿于西元一七四二年。它用颤抖的笔迹，详尽记载了那个自大叛乱时期以来，便如梦魇般死死缠绕着这个古老门阀的恐怖诅咒！’

我倾身上前，任凭手中的石楠木烟斗熄灭在指间。‘您口中所言，不过是一段尘封的历史传说，摩梯末医生。我的侦查实践仅局限于当下的现实世界，以及活在这个世界上的血肉之躯。难道您是要我花费宝贵的时间，去缉拿一个十八世纪的亡魂吗？’

‘我要您做的，福尔摩斯先生，’摩梯末的呼吸变得短促而沉重，声音压低得如同来自幽冥，‘是先听完这段古老可怖的血腥编年史，然后再亲眼过目那两行将查尔斯爵士活活逼入绝境的、温热未消的巨大脚印！’"""
    },

    # -------------------------------------------------------------------------
    # Chapter 2: Part 1
    # -------------------------------------------------------------------------
    {
        "id": "holmes_ch02_part1_legend",
        "ch_idx": 1, "part": 1,
        "title_en": "Chapter 2: The Curse of the Baskervilles (Part I: The Legend of Hugo)",
        "title_cn": "第二章 巴斯克维尔的诅咒（上：雨果·巴斯克维尔的手稿）",
        "pov": "holmes", "type": "branch", "anchor": "anchor_curse",
        "clues_en": [
            "1742 manuscript details Hugo Baskerville’s profane oath and pursuit of the yeoman’s daughter",
            "The spectral beast tore Hugo’s jugular vein in the great granite goyal under the moonlight",
            "The curse warns all heirs never to cross the moor in the dark hours when evil powers are exalted",
        ],
        "clues_cn": [
            "1742年手稿详述雨果·巴斯克维尔在清教徒战争期间背弃神明、纵犬追猎农家少女的罪孽",
            "在荒原深处的花岗岩沟壑中，一只喷吐磷光的地狱巨犬在月夜撕裂了雨果的颈动脉",
            "手稿立下严厉祖训：后世子嗣万不可在黑夜与邪恶猖獗之时孤身涉足德文郡荒原",
        ],
        "choices_en": [
            {"id": "h_ch2_p1_c1", "text": "Cross-examine Mortimer on the physical reality of Sir Charles’s recent demise.", "target": "holmes_ch02_part2_footprints"},
            {"id": "h_ch2_p1_c2", "text": "[Switch POV to Jack Stapleton] Discover how the antagonist weaponized this ancient legend.", "target": "stapleton_ch02_part1_laura_trap", "pov_switch": "stapleton"},
        ],
        "choices_cn": [
            {"id": "h_ch2_p1_c1", "text": "严厉质询摩梯末医生，探明查尔斯爵士近期暴卒现场的客观物理真相。", "target": "holmes_ch02_part2_footprints"},
            {"id": "h_ch2_p1_c2", "text": "【视角切换：杰克·斯台普吞】窥探这位幕后主凶如何将古老传说铸为杀人利器。", "target": "stapleton_ch02_part1_laura_trap", "pov_switch": "stapleton"},
        ],
        "content_en": """I settled back into the cushions of my settee, my fingers laced across my knee, and watched Dr. Mortimer through half-closed eyelids. Outside, the roar of London traffic was subdued by the heavy autumn fog that pressed against the windowpanes. Inside, the only sound was the rustle of brittle parchment as the physician smoothed out the manuscript of 1742.

With a solemn, resonant voice that trembled with genuine dread, Mortimer began to read the chronicle:

“Of the origin of the Hound of the Baskervilles there have been many statements, yet as I am lineally descended from Hugo Baskerville, and had it from my father, I have put it down with all credence...”

The narrative was couched in the quaint, ornate diction of the early Georgian era. It told of this wild, profane Cavalier, Hugo Baskerville, who ruled the ancestral manor with an iron fist during the Great Rebellion. A lawless roisterer, he had conceived an unholy passion for the daughter of a modest yeoman whose lands lay near the estate. Finding his advances spurned, Hugo, aided by five or six desperate companions, rode to the yeoman’s farm on Michaelmas Eve, seized the terrified girl, and carried her off to the Hall, imprisoning her in an upper chamber whilst he and his drunken ruffians caroused below.

The girl, driven nearly mad by the riotous songs and foul oaths rising through the floorboards, did what might have daunted the bravest man: she climbed through the window, scrambled down the thick mantle of ivy covering the stone wall, and fled out into the black expanse of Dartmoor, running towards her father’s home some nine miles distant.

When Hugo discovered her flight, he broke into a frenzy of rage so appalling that his companions drew back in horror. Leaping upon the banqueting table amid the overturned wine-jugs, he swore a terrible oath before God and Satan that he would render his body and soul to the Evil One that very night if he might but overtake the wench. Rushing to the courtyard, he loosed his pack of hounds, thrust the girl’s kerchief to their muzzles, and sprang upon his black mare, spurring furiously out into the moonlit moor.

His companions, partly sobered by his demonic madness, mounted their horses and galloped after him. For miles across the barren wastes they rode, until they came upon a solitary shepherd shivering upon the crags. Shaking with terror, the man pointed towards a deep granite goyal—a ravine cutting through the peat bog—and swore that he had seen Hugo riding hard upon his black mare, but that galloping close behind him was a hound such as God never made, running silently upon his heels.

Dashing forward, the horsemen reached the brink of the goyal. The black mare stood trembling, her flanks white with lather, staring down into the darkness. Half the hounds were whimpering near the edge, while the others crawled away into the heather with tails between their legs.

The three boldest riders rode down into the amphitheatre. In the center of the clearing lay the dead body of the unhappy maiden, perished of fear and fatigue. But beside her...

Mortimer’s voice dropped to a guttural rasp:

“There, standing over the prostrate body of Hugo Baskerville, and plucking at his throat, was a foul thing, a great black beast, shaped like a hound yet larger than any hound that ever mortal eye had rested upon. And even as they looked, the monster tore the throat out of Hugo Baskerville, and turned its blazing eyes and dripping jaws upon them! With screams of terror, the three men spurred their horses and fled for their lives; one died that very night of the horror he had seen, and the other two were broken, gibbering madmen for the remainder of their days.”

Mortimer ceased reading. He folded the parchment with shaking hands and looked up at me through his spectacles, his face as pale as chalk.

“Such, Mr. Holmes,” said he, “is the ancient legend. It concludes with an earnest injunction from the chronicler to his sons, that they should never cross the moor in those dark hours when the powers of evil are exalted.”

I took a slow sip of my tepid coffee and suppressed a yawn. “A most picturesque piece of seventeenth-century melodrama,” I remarked coolly. “It would make an admirable nursery tale to frighten refractory children. But surely, Dr. Mortimer, you have not brought me this Gothic relic under the impression that it possesses any bearing upon modern criminal jurisprudence?”

“Mr. Holmes,” said Mortimer, his hands gripping the arms of his chair until the knuckles whitened, “I have read this manuscript because it was Sir Charles Baskerville’s daily terror! He believed every syllable of it with his whole soul. And three months ago, on a night as black as pitch, Sir Charles was found dead at the foot of his garden alley—his face distorted into an expression of mortal agony that no man who beheld it will ever forget!”""",
        "content_cn": """我将背脊深陷在皮沙发的软垫里，十指交叉搭在膝头，透过半合的眼睑静静凝视着摩梯末医生。窗外，被深秋浓雾浸润的伦敦街市喧嚣显得沉闷而遥远；起居室内，唯有那张脆化发黄的羊皮纸在医生指间摩挲出的沙沙声在空气中回荡。摩梯末以一种因本能战栗而发颤的肃穆低音，开始逐字宣读这份来自一七四二年的家族手稿：

‘关于巴斯克维尔魔犬之起源，世间传闻甚多。然余既系雨果·巴斯克维尔之直系后裔，复从先父口中得闻其详，因笔之于书，以垂后世……’

整篇文字洋溢着乔治一世时代那种古雅而庄重的修辞风范。手稿详尽记载了那位在清教徒大叛乱时期横行乡里的残暴骑士——雨果·巴斯克维尔。此人荒淫无度、目无王法，对庄园近邻一位朴实自耕农的妙龄女儿产生了狂热的邪念。求欢遭拒之后，在当年米迦勒节前夕，雨果纠集了五六名亡命恶徒，趁着夜色策马突袭自耕农的农庄，将那名惊恐万状的少女强行掳至巴斯克维尔庄园，锁在南侧塔楼的顶层偏房内，而雨果本人则与同伙在楼下的大厅里彻夜狂饮作乐。

楼下传来的污言秽语与狂暴酒歌，令那名不幸的姑娘陷入了濒临崩溃的绝望。在极度恐惧的驱使下，她做出了连最勇敢的壮士也未必敢尝试的惊人之举：她爬出狭窄的窗棂，攀附着覆盖在庄园外墙上粗壮如缆绳的老常春藤藤蔓，顺着石壁滑落至地面，旋即义无反顾地冲入德文郡荒原漆黑死寂的旷野，企图奔向九英里外父亲的农庄。

当雨果在醉眼朦胧中发现人去房空时，他爆发出的狂怒令在场最凶悍的亡命徒也为之胆寒。他一跃跳上面前杯盘狼藉的长条橡木餐桌，当着天地与魔鬼的面发下了恶毒的誓言：只要今夜能让他追上并凌辱那个逃跑的贱人，他愿在此时此刻将自己的肉体与灵魂悉数出卖给地狱的撒旦！他狂呼着冲进庭院，放出豢养的恶犬，将少女遗落的方巾塞到猎犬鼻尖前，旋即翻身跃上他的黑鬃烈马，如狂风般疾驰冲入月色惨淡的荒原。

残存的同伙被雨果近乎中邪的癫狂所震慑，酒意登时清醒了大半。他们纷纷跨上马鞍，循着蹄声策马疾追。在大片荒凉起伏的花岗岩与石楠丛中狂奔了数英里后，他们遇到了一位在风中瑟瑟发抖的守夜老牧羊人。老人面无人色、牙齿打战地指向荒原深处一道名为‘黑沟壑’的巨大花岗岩裂谷，颤抖着发誓说：他确实看见雨果骑着黑马呼啸而过，但在那匹马身后不远处，赫然紧跟着一只‘上帝绝未创造过的恐怖巨犬’，正悄无声息地贴地狂奔，紧咬着雨果的马蹄印不放！

追兵们策马冲到了裂谷边缘。那匹黑马正浑身冒汗、瘫软在岩石旁剧烈抽搐，双眼翻白地盯着裂谷下方的黑暗。半数猎犬蜷缩在悬崖边缘呜咽哀鸣，其余的则夹着尾巴没命地逃窜进沼地的荒草丛中。

三名胆量最大的骑士拔出佩剑，战战兢兢地策马下到裂谷底部的圆形空地上。眼前的一幕令他们肝胆俱裂：在那片惨白月光照耀的泥沼旁，倒卧着那位可怜少女的尸身，她已被过度惊吓与长途奔命活活夺去了呼吸。而在她身旁……

摩梯末医生的喉咙里发出了一阵干涩而尖利的破音：

‘……只见一只通体漆黑、体形硕大如小牛犊般的恶兽，正赫然骑跨在倒地的雨果·巴斯克维尔身上，疯狂撕咬着他的咽喉！那绝非凡间任何猎犬所能比拟的怪物，它的双目喷吐着幽绿的火焰，滴血的下颚在月光下闪烁着惨白的光芒！就在那三名骑士魂飞魄散的注视下，那恶兽猛地扯碎了雨果的喉管，转过那张淌着血水的可怖面孔，将两道地狱般的目光直刺向他们！那三人发出绝望的凄厉尖叫，发疯般勒马狂奔逃命。其中一人在当夜便因惊骇过度暴毙而亡，另外两人则彻底沦为神志不清、终日胡话连篇的疯子，直至残生终了。’

摩梯末医生停止了宣读。他用冰冷颤抖的手将羊皮纸重新折叠，摘下金丝眼镜，隔着镜片望向我，面颊惨白如纸。

‘这就是那个古老的传说，福尔摩斯先生，’他的嗓音沙哑微弱，‘手稿在末尾严厉告诫巴斯克维尔家族的历代子孙：无论何时，切不可在黑夜猖獗、邪灵得势的时辰孤身踏入德文郡荒原。’

我端起微凉的咖啡轻轻抿了一口，掩饰住一个微不可察的呵欠。‘一段极其生动且充斥着十七世纪通俗剧色彩的传奇故事，’我语气淡漠地评述道，‘拿来在冬夜壁炉旁吓唬不听话的孩童倒是不错的素材。然而，摩梯末医生，您总不会天真地认为，这样一份充斥着哥特式迷信色彩的陈年旧稿，会对十九世纪现代严谨的刑事法医学侦查具有任何实际指导价值吧？’

‘福尔摩斯先生！’摩梯末枯瘦的手掌死死扣住扶手椅的硬木边缘，指节因用力而泛白，‘我之所以必须先读这份手稿，是因为它正是查尔斯·巴斯克维尔爵士生前最大的恐惧源头！他用整个灵魂坚信着这份诅咒的每一个字！而就在三个月前那个漆黑如墨的夏夜，查尔斯爵士在水松夹道尽头轰然倒毙——他死前面容扭曲所呈现出的极致惊恐，凡是亲眼目睹过的人，这一生都绝不可能将其从梦魇中抹去！’"""
    },

    # -------------------------------------------------------------------------
    # Chapter 2: Part 2
    # -------------------------------------------------------------------------
    {
        "id": "holmes_ch02_part2_footprints",
        "ch_idx": 1, "part": 2,
        "title_en": "Chapter 2: The Curse of the Baskervilles (Part II: Footprints of a Gigantic Hound)",
        "title_cn": "第二章 巴斯克维尔的诅咒（下：巨大猎犬的足迹）",
        "pov": "holmes", "type": "branch", "anchor": None,
        "clues_en": [
            "Sir Charles stood smoking for 5 to 10 minutes at the Yew Alley gate, dropping ash twice",
            "Footprints changed from flat heel-to-toe walking to running on tiptoes down the alley",
            "Twenty yards beyond the body, in the soft moist soil, were the enormous pawprints of a hound",
        ],
        "clues_cn": [
            "查尔斯爵士曾在水松夹道栅门前驻足停留5至10分钟，雪茄烟灰在地面散落两次",
            "足迹在栅门处发生突变：由原本从容的平脚着地变为极度惊恐下的踮脚狂奔",
            "在距离尸体二十码开外的湿软泥土中，赫然印有一串巨硕无朋的凶兽爪印",
        ],
        "choices_en": [
            {"id": "h_ch2_p2_c1", "text": "Formulate the operational hypothesis and prepare for Sir Henry’s arrival tomorrow.", "target": "holmes_ch03_problem"},
            {"id": "h_ch2_p2_c2", "text": "[Switch POV to Jack Stapleton] See how the mastermind arranged this fatal midnight meeting.", "target": "stapleton_ch02_part2_yew_alley", "pov_switch": "stapleton"},
        ],
        "choices_cn": [
            {"id": "h_ch2_p2_c1", "text": "构建初步案件假说，闭门推演荒原地理，准备迎接入境的亨利爵士。", "target": "holmes_ch03_problem"},
            {"id": "h_ch2_p2_c2", "text": "【视角切换：杰克·斯台普吞】检视这位致命元凶如何精心布局那场午夜绝命会面。", "target": "stapleton_ch02_part2_yew_alley", "pov_switch": "stapleton"},
        ],
        "content_en": """I set down my coffee cup, and for the first time since Mortimer had crossed our threshold, my mind locked entirely onto the problem. The ancient myth was mere romantic froth, but a man driven to death by terror in a modern garden—that was solid ground.

“Give me the facts, Dr. Mortimer,” I commanded, leaning forward, my eyes fixed upon his countenance. “Omit nothing. The official inquest returned a verdict of death by natural causes, did it not?”

“It did, Mr. Holmes. The county coroner found that Sir Charles had suffered from long-standing neurosis and cardiac degeneration. His heart failed while he was taking his customary evening walk down the famous Yew Alley of Baskerville Hall. The medical evidence showed no trace of violence.”

“And your own examination?”

“I arrived at the scene within an hour of the discovery of the body,” Mortimer said, his voice lowering until it vibrated with suppressed excitement. “The local authorities saw only what was obvious. They noted that the gate leading to the open moor was unlatched. They saw that Sir Charles lay fifty yards from the gate, face downward upon the gravel path. But they did not see what I saw, Mr. Holmes, because they did not know how to look!”

“Tell me what you saw.”

“The Yew Alley,” Mortimer explained, gesturing with his long, bony fingers, “is a double line of old, impenetrable yew trees, twelve feet high, forming a tunnel down the eastern side of the Hall grounds. Outside the hedge lies the boundless moor. Midway down the alley is a wicket gate opening out into the heather. Now, observe: Sir Charles had walked from the house down to this wicket gate. There he had stood for some time—I calculated five to ten minutes at least, for the ash had dropped twice from his cigar upon the gravel.”

“Excellent!” I ejaculated. “This man is a colleague after your own heart, Watson! He noted the ash!”

Mortimer bowed slightly. “Sir Charles had leaned his arms upon the wooden gate, looking out across the dark moor. And then—something occurred. Something so appalling that he turned and fled for his life back towards the house. But he did not run as an ordinary man runs.”

“How did he run?”

“He ran upon his tiptoes!” Mortimer whispered. “His tracks altered completely. The heel marks vanished. He bounded down that dark alley upon his toes, like a man possessed, his stride lengthening with frenzied panic, until his diseased heart burst beneath the strain and he pitched forward into the grass, his fingernails digging deep into the turf!”

I sprang to my feet and began to pace the room. The scent of a true problem was in my nostrils. “And you say he was running away from the gate? Towards the house?”

“Towards the Hall.”

“And what lay beyond the gate?”

“The open moor, Mr. Holmes. Miles of desolate heather and peat bog.”

“And now, Dr. Mortimer—the central fact. Why did you say the inquest did not know the truth?”

The physician looked nervously at Watson, then back to me. He swallowed hard before answering. “Mr. Holmes, the coroner asked me if there were any marks upon the gravel near the body. I answered that there were none. But he did not ask me what was upon the damp, soft peat beside the pathway!”

“And what was there?”

“I walked twenty yards beyond the spot where Sir Charles had fallen, where the path passes near a moist depression in the soil. There, fresh and clearly defined in the black loam, were marks.”

“Footprints?”

“Yes, footprints.”

“A man’s or a woman’s?”

Dr. Mortimer looked at us for a moment, and his voice sank into a whisper that chilled the room:

“Mr. Holmes, they were the footprints of an enormous hound!”

I stopped dead in my tracks. “You saw them yourself?”

“As clearly as I see you now.”

“And they were fresh?”

“The night was damp and drizzling; the edges of the impressions were sharp and moist. They were the prints of a dog of gigantic proportions—a creature such as no keeper on the moor has ever bred.”

“And did they approach the body?”

“No. They circled the moor-gate, twenty yards distant, and then turned back towards the Great Grimpen Mire.”

I rubbed my chin, my pulses racing. “This is deep water, Watson,” I murmured. “Deep and perilous water. And what is your immediate objective in consulting me, Dr. Mortimer?”

“Tomorrow morning, Mr. Holmes,” the doctor replied, “Sir Henry Baskerville—the sole surviving nephew, son of Sir Charles’s younger brother—arrives at Waterloo from Canada to take possession of the title and the estate of £740,000. He is the last of the direct bloodline. What in God’s name am I to do with him?”""",
        "content_cn": """我将微凉的咖啡杯轻轻放回托盘，自摩梯末跨入寒舍以来，我的大脑第一次全神贯注地锁定了这个案子。古老的鬼怪传说不过是浪漫主义的浮云泡沫，然而，一位现代绅士在自家庄园的花园散步道上被活活吓死——这才是坚实确凿、值得严密推敲的刑侦实证！

‘请把全部客观事实原原本本地讲给我听，摩梯末医生，’我身子前倾，目光如两道利刃般直刺他的面庞，‘切勿遗漏任何细节。据我所知，当地验尸法庭给出的官方裁决是自然死亡，不是吗？’

‘正是如此，福尔摩斯先生。’摩梯末深吸了一口气，语调紧绷，‘郡验尸官认定，查尔斯爵士生前长期罹患严重的神经衰弱与器质性心脏功能退化。他在当晚如往常一样，在庄园那条著名的水松夹道散步时，突发急性心脏衰竭倒毙。法医的尸检报告明确排除了任何外力暴力的痕迹。’

‘那么您亲自勘验现场的结论呢？’

‘在尸体被仆人发现后不到一个小时，我便赶到了现场，’摩梯末的声音压得极低，甚至因极度克制而微微颤抖，‘当地的警察与法医只看到了那些浮于表面的平庸现象。他们注意到通往荒原的外侧小木门虚掩着；他们看到查尔斯爵士趴倒在距离木门五十码开外的碎石路上，面部朝下紧贴着泥土。然而，他们全都没有看到我所看到的东西，福尔摩斯先生，因为他们根本不懂得该如何观察！’

‘告诉我，你看到了什么？’

‘巴斯克维尔庄园的水松夹道，’摩梯末伸出修长如枯骨般的手指在空中比划着，‘是由两排高逾十二英尺、树龄数百年的古老水松树构成的双列绿色林荫隧道，密不透风地横亘在庄园东侧边缘。在树篱之外，便是无边无际的荒原。在夹道的中段，有一扇简陋的栅门，推开便可直接步入石楠丛生的荒野。请注意：查尔斯爵士是从主宅沿着夹道一直信步走到这扇木门前的。他在那里驻足停留了相当长的时间——据我精确测算，至少有五到十分钟，因为他手中的高档雪茄烟灰在碎石地面上完整脱落了两次！’

‘精彩绝伦！’我忍不住脱口赞叹，‘华生，这位医生简直是与你志同道合的楷模！他居然注意到了烟灰！’

摩梯末微微欠身致意，继续说道：‘查尔斯爵士当时双臂搭在木门上，面朝漆黑的荒原驻足远眺。然而就在那一瞬间——某种恐怖绝伦的事态骤然爆发了！某种足以摧毁人类理智的恐怖存在骤然降临，迫使他猛然转身，发疯般沿着夹道朝主宅方向亡命飞奔！然而，他的奔跑姿态却与常人完全不同！’

‘足迹呈现出怎样的形态？’

‘他是踮着脚尖狂奔的！’摩梯末以气声嘶哑地耳语道，‘他的脚印完全变了形状！原本深陷的脚后跟压痕彻底消失了！他就这样像中邪的幽灵一般，仅凭前脚掌和脚趾在狭长的阴森甬道中拼命蹬地狂奔，步幅因极度的惊恐而拉得大得惊人，直到那颗早已不堪重负的病弱心脏在狂暴的跳动中彻底爆裂，他整个人重重地栽倒在草皮边缘，手指深深抠入了泥泞的草根之中！’

我霍然从扶手椅上站起，在起居室的地毯上迅疾地来回踱步。一股真正属于高智商犯罪的气味在空气中弥漫开来，令我体内的每一个神经元都战栗起来。‘你说他是背对着那扇栅门狂奔？也就是朝向宅邸的方向逃命？’

‘正是朝向主宅的方向。’

‘而在木门之外，究竟有什么？’

‘是达特荒原，福尔摩斯先生。无边无际、吞噬一切的石楠泥沼与花岗岩死寂旷野。’

‘那么现在，摩梯末医生——请道出最核心的事实。你为何断定验尸官隐瞒了真相？’

这位年轻的医生不安地瞥了华生一眼，随后将目光重新死死锁定在我身上。他艰难地咽了一口唾沫，声音低沉得宛如来自坟墓：

‘福尔摩斯先生，验尸官在法庭上曾当面质问我，尸体周围的碎石路上是否有任何搏斗或外力留下的痕迹。我如实回答没有。然而，他却根本没有询问我，在远离步道两旁那片湿软的泥炭藓沼泽里，究竟留下了什么！’

‘那里留下了什么？’

‘我沿着查尔斯爵士倒毙的地点朝外走出了二十码，在靠近一片潮湿低洼的黑泥苔藓边缘，清晰、深刻、毫无瑕疵地印着一串痕迹！’

‘是脚印？’

‘是的，脚印。’

‘是男人的皮鞋，还是女人的便鞋？’

摩梯末医生死死盯着我们二人，从齿缝中挤出了一句令整座房间瞬间坠入冰窟的话语：

‘福尔摩斯先生……那是一只体形巨硕无朋的凶兽爪印！’

我的脚步在瞬间骤停。‘你亲眼所见？’

‘正如我此刻亲眼看见您一样千真万确。’

‘足迹是新鲜的？’

‘当夜一直飘着细密的冷雨；爪印边缘的泥土锐利湿润，绝对是当夜所留。那毫无疑问是一只骨架庞大如小牛犊般的恶犬留下的抓痕——德文郡荒原上的任何猎场看守，都绝不可能培育出如此硕大的怪物！’

‘那只恶犬靠近过尸体吗？’

‘没有。爪印只是在距离木门二十码外的湿地处徘徊打转，随后便调转方向，径直奔回了大格林盆泥潭深处！’

我用拇指重重摩挲着下颚，体内沉寂多日的血液开始狂野地奔流。‘这水很深啊，华生，’我低声自语，‘这是一池深不可测且杀机四伏的险水！那么，摩梯末医生，你今天不远千里赶来伦敦向我求助，究竟有何诉求？’

‘明天上午，福尔摩斯先生，’摩梯末颤抖着说道，‘查尔斯爵士唯一的直系血亲、他二弟的儿子亨利·巴斯克维尔爵士，便将从加拿大乘船抵达滑铁卢车站，正式继承这一爵位以及高达七十四万英镑的巨额遗产！他是巴斯克维尔家族最后的骨血。看在上帝的份上，我究竟该拿他怎么办？我能放任他踏入那片被诅咒的荒原吗？！’"""
    },

    # -------------------------------------------------------------------------
    # Chapter 3
    # -------------------------------------------------------------------------
    {
        "id": "holmes_ch03_problem",
        "ch_idx": 2, "part": 1,
        "title_en": "Chapter 3: The Problem (Dartmoor Topography and the Lone Vigil)",
        "title_cn": "第三章 疑案（烟雾缭绕中的沉思与荒原地图）",
        "pov": "holmes", "type": "branch", "anchor": "anchor_london_mission",
        "clues_en": [
            "Mortimer requested to meet Sir Henry Baskerville at Waterloo and bring him to 221B at ten tomorrow",
            "Ordnance Survey map of Dartmoor reveals the topography of Grimpen Mire, Princetown prison, and Black Tor",
            "Holmes deduces an acute, living intellect is weaponizing the hound superstition to eliminate the heir",
        ],
        "clues_cn": [
            "已叮嘱摩梯末医生在滑铁卢车站迎候亨利爵士，并于明晨十点准时引荐至贝克街221号B",
            "六英寸一英里的军械调查局高精度地图清晰展示了格林盆泥潭、达特穆尔监狱与黑色岩岗的险恶地貌",
            "福尔摩斯断定：绝非幽冥恶鬼作祟，而是一个极其阴险缜密的高智商活人正在利用传说猎杀巨额遗产继承人",
        ],
        "choices_en": [
            {"id": "h_ch3_c1", "text": "Receive Sir Henry Baskerville and examine the warning letter clipped from The Times.", "target": "holmes_ch04_part1_warning"},
            {"id": "h_ch3_c2", "text": "[Switch POV to Dr. Watson] Experience Watson’s perspective during the Baker Street smoke vigil.", "target": "ch03_problem", "pov_switch": "watson"},
        ],
        "choices_cn": [
            {"id": "h_ch3_c1", "text": "次日清晨会见亨利·巴斯克维尔爵士，剖析那封以《泰晤士报》剪贴而成的恐吓信。", "target": "holmes_ch04_part1_warning"},
            {"id": "h_ch3_c2", "text": "【视角切换：约翰·H·华生】从华生的视角体察名侦探整夜沉浸烟草浓雾中的冥想。", "target": "ch03_problem", "pov_switch": "watson"},
        ],
        "content_en": """When Dr. Mortimer and his panting spaniel had departed down the stairs, the quiet of our room seemed deeper, heavier with the dark freight of the problem left behind.

“Well, Watson,” said I, “what do you think of it?”

“It seems to me,” he replied earnestly, “that if Dr. Mortimer’s belief is well-founded, and some supernatural agency is at work—”

“Ah, the supernatural!” I interrupted, shaking my head. “We have hitherto confined our cases to this planet, Watson. To invoke the supernatural is to confess intellectual bankruptcy. If an actual, physical hound can leave pawprints twenty yards wide in moist Devonshire peat, then that hound has teeth and claws, weighs so many stones, requires so many pounds of butcher’s meat a day, and can be brought down with an ordinary lead bullet from an Adams revolver!”

I turned on my heel and walked to my desk. “Go out, Watson. The day is fine. Go to your club; walk in the park. But leave me alone with this room and my thoughts until dusk. I have a problem here that cannot be solved without a thorough clearing of the ground.”

When Watson reluctantly closed the door behind him, I stripped off my frock-coat and pulled on my mouse-coloured dressing gown. From the mantelpiece I fetched down my blackened clay pipe and the Persian slipper containing a pound of strong, pungent shag tobacco. Next, I took from the corner shelf the huge, linen-backed Ordnance Survey map of Dartmoor—drawn to the scale of six inches to the mile—and pinned it across the center of our large oak table.

For the next eight hours, I did not leave that chair. A blue cloud of rank, suffocating tobacco smoke gathered beneath the ceiling, rolling in dense wreaths until the gas lamps burned like yellow lanterns in a maritime fog.

My eyes traversed every contour line, every boulder-strewn slope, every treacherous marsh of that wild Devon plateau. There lay Baskerville Hall, an ancient Tudor fortress flanked by its dark yew alley. Beyond it, three miles to the south, stood the sinister circle of the prehistoric stone huts atop the granite monolith of Black Tor. To the east, like a festering wound in the earth, stretched the Great Grimpen Mire—miles of bright green peat-bog concealing bottomless quagmires of liquid mud, where cattle and wandering ponies were swallowed alive in seconds. And nestled along the western margin of that dreadful swamp sat Merripit House, the isolated dwelling of a brother and sister named Stapleton, described in Mortimer’s notes as a naturalist and a schoolmaster.

I lit match after match, watching the yellow flame flare against the map. Two distinct lines of reasoning began to take shape within my mind.

First: The weapon. If the hound was flesh and blood, where had it been hidden? It could not be kept in a village kennel without setting every tongue in the county wagging. It required vast quantities of food; it required seclusion; it required an owner who possessed both scientific knowledge and ruthless nerve.

Second: The motive. Sir Charles had died of cardiac arrest induced by mortal terror. Who stood to gain from his sudden death? The estate was valued at nearly three quarters of a million pounds sterling. If young Sir Henry from Canada were to perish on the moor, who was the next of kin? Mortimer had mentioned an aged, distant cousin named Desmond, a saintly clergyman in Westmorland who had no interest in wealth. Was there another? An unacknowledged branch of the family tree?

I leaned back, inhaling the bitter smoke deeply, watching the embers glow in the darkened room. A cold, methodical, highly cultivated intellect was directing this game. The murderer knew of Sir Charles’s weak heart; he knew of his obsessive superstition regarding the ancestral curse; and he had weaponized an 18th-century ghost story into an instrument of modern assassination!

Tomorrow morning, the last direct heir would walk into this room. And behind him, unseen and silent, walked the shadow of the beast.""",
        "content_cn": """当摩梯末医生带着那只气喘吁吁的西班牙猎犬离开后，楼梯间回荡的沉重脚步声逐渐隐没在街头的车马声中。起居室内的静谧显得愈发幽深，仿佛空气中凭空增添了那桩诡谲凶案带来的沉重压迫感。

‘那么，华生，’我转过身来，‘对此你作何感想？’

‘在我看来，’华生神情极其严肃地回答道，‘如果摩梯末医生的直觉并非空穴来风，如果这背后真有某种超自然的力量在作祟……’

‘哈！超自然！’我挥手打断了他，严厉地摇了摇头，‘迄今为止，我们的刑侦业务始终立足于这颗坚实的人类行星之上，华生！诉诸超自然，是对人类理智破产的怯懦自白！如果真有一只现实中的恶犬能在德文郡潮湿的泥炭地上留下深达数寸的清晰爪印，那么这只恶犬就必然长着利齿与爪牙，有着沉甸甸的肉体骨骼，每天必须吞食数磅屠户供应的碎肉，而且——它也绝不可能抵挡得住一发从阿达姆斯转轮手枪里射出的正义铅弹！’

我在地毯上霍然转身，径直走到书桌前。‘出去走走吧，华生。今天外面的天气还不算太糟。去你的俱乐部坐坐，或者去摄政公园散散步。但在黄昏降临之前，请把这间屋子和我脑中的思绪彻底留给我一个人。摆在我们面前的这桩谜案，若不将地基彻底夯实清理，绝无可能窥破其全貌。’

当华生带着一丝关切而无奈的神情轻轻带上房门后，我迅速脱下紧绷的常礼服外套，换上了那件磨损严重的鼠灰色旧晨袍。我从壁炉架上取下那只被焦油熏得漆黑的陶土短烟斗，又从挂在墙角的波斯拖鞋鞋尖里掏出一大把辛辣浓烈、足以呛死常人的黑板烟丝。紧接着，我从书架最底层的角落里抽出了一张巨大的、背衬粗麻布的军械调查局高精度达特荒原军事地形图——其测绘比例尺达到了惊人的每英里六英寸——并用图钉将它牢牢固定在我们宽大的橡木餐桌中央。

在接下来的整整八个小时里，我未曾离开过那把硬木高背椅半步。一团泛着蓝黑色的辛辣烟云在天花板下逐渐积聚、翻滚、凝结成一道道沉重的烟瘴，直到黄昏时分街灯亮起时，起居室内的煤气壁灯宛如深海迷雾中两盏昏黄摇曳的渔火。

我的指尖与目光，不知疲倦地划过那张地图上的每一条等高线、每一处遍布嶙峋乱石的花岗岩荒坡、以及那片被德文郡人视作死亡禁区的蛮荒死沼。那里赫然标注着巴斯克维尔庄园——那座被高大水松夹道严密环绕的都铎时代坚固城堡；往南三英里处，则是伫立在黑色岩岗顶峰、由史前凯尔特蛮族留下的古老环形石屋遗迹；而在庄园东侧，宛如大地上一道溃烂脓疮般蔓延数英里的，正是那片恶名昭彰的大格林盆泥潭——无数看似娇艳翠绿的水生苔藓下方，隐藏着能在一瞬间将健壮公牛与误入野马活活吞噬的万丈泥渊！而在那座死亡泥潭西侧边缘的孤绝孤岛上，孤零零地坐落着梅立坪宅邸——据摩梯末笔记记载，那里住着一位名叫斯台普吞的博物学者及其胞妹。

我划燃一根又一根火柴，借着微弱跳动的火光注视着地图上的这几个坐标。两条截然不同却又在暗中交汇的逻辑脉络，在我脑海中逐渐淬炼成型。

第一：作案凶器。如果那只恶犬确实是血肉之躯，那么在凶案发生之前与之后，凶手究竟将它藏匿在何处？如此庞大的恶兽，绝不可能圈养在寻常村落的犬舍中而不引起乡邻的惊觉；它需要巨量的鲜肉维持生机；它需要绝对与世隔绝的隐秘据点；最关键的是，它的主人必须同时兼备广博的生物生理学知识，以及冷酷如铁的坚韧神经。

第二：谋杀动机。查尔斯爵士死于极度惊恐诱发的急性心脏骤停。那么，他的猝死究竟能让谁坐收渔翁之利？巴斯克维尔的庄园与信托基金总额高达七十四万英镑！如果远道而来的继承人亨利爵士也在荒原上死于非命，这笔庞大的财产将顺位继承给谁？摩梯末曾提及一位远在威斯特摩兰郡行医传教的远亲戴斯蒙德老牧师——一位视金钱如粪土的圣徒。然而，在族谱的阴影里，是否还潜藏着未被公开承认的私生子嗣或旁系血脉？

我深深地吸了一口刺鼻的浓烟，倚在椅背上，在渐浓的夜色中凝视着烟斗中明灭的火星。一个冷酷、缜密、受过极高教育且深谙人性的非凡大脑，正在暗中操纵着这场死局！凶手深知查尔斯爵士脆弱的心脏病灶；深知他对家族古老诅咒那深入骨髓的迷信恐惧；他竟然极其阴险地将一段十八世纪的哥特鬼怪故事，锻造为现代谋杀最锋利无形的凶刃！

明晨十点，巴斯克维尔家族最后的继承人就将踏入这间屋子。而在他的身后，一道无形而致命的巨兽阴影，已然在泥潭的迷雾中露出了森森利齿！"""
    },

    # -------------------------------------------------------------------------
    # Chapter 4: Part 1
    # -------------------------------------------------------------------------
    {
        "id": "holmes_ch04_part1_warning",
        "ch_idx": 3, "part": 1,
        "title_en": "Chapter 4: Sir Henry Baskerville (Part I: The Cut Times and the Missing Boot)",
        "title_cn": "第四章 亨利·巴斯克维尔爵士（上：剪贴信件与失窃新靴）",
        "pov": "holmes", "type": "branch", "anchor": None,
        "clues_en": [
            "Warning letter composed from words clipped with nail scissors from yesterday’s Times leading article",
            "Faint scent of white jessamine perfume reveals a woman’s involuntary presence in the drafting",
            "Sir Henry’s brand new unworn tan boot stolen from Northumberland Hotel room corridor",
        ],
        "clues_cn": [
            "恐吓信系用指甲剪从昨日《泰晤士报》关于自由贸易的社论中剪下资产阶级字体拼接而成",
            "信纸边缘残留一丝微弱的白素馨花香水气味，揭示出有女性在极度不情愿中参与起草",
            "亨利爵士入住诺森伯兰饭店第一夜，一双崭新未穿过的黄褐色皮靴在走廊离奇失窃",
        ],
        "choices_en": [
            {"id": "h_ch4_p1_c1", "text": "Shadow Sir Henry and Mortimer down Regent Street to flush out their tail.", "target": "holmes_ch04_part2_cab_chase"},
            {"id": "h_ch4_p1_c2", "text": "[Switch POV to Jack Stapleton] See Stapleton stalking the baronet from Cab 2704.", "target": "stapleton_ch04_part1_hotel_shadow", "pov_switch": "stapleton"},
        ],
        "choices_cn": [
            {"id": "h_ch4_p1_c1", "text": "尾随亨利爵士与摩梯末步入摄政街，逼出暗中盯梢追踪的幕后眼线。", "target": "holmes_ch04_part2_cab_chase"},
            {"id": "h_ch4_p1_c2", "text": "【视角切换：杰克·斯台普吞】窥视潜伏在2704号马车里的反派如何紧盯猎物。", "target": "stapleton_ch04_part1_hotel_shadow", "pov_switch": "stapleton"},
        ],
        "content_en": """At exactly ten o’clock the following morning, the door opened and Dr. Mortimer ushered into our room the young baronet whose life and fortune hung in the balance. Sir Henry Baskerville was a small, alert, dark-eyed man of about thirty years of age, very sturdily built, with thick black eyebrows and a strong, pugnacious face. He wore a ruddy-tinted tweed suit and possessed the weather-beaten complexion of one who has spent his best years in the open air of the Canadian prairies. Yet there was that calm, steady assurance in his gaze which proclaimed the English gentleman.

“I am delighted to meet you, Mr. Holmes,” said he, shaking hands with a firm, sinewy grip. “If Dr. Mortimer had not suggested our visit, I should have come to you on my own account. I understand that you solve riddles, and I’ve run into one this morning that has completely floored me.”

“Pray take a seat, Sir Henry,” said I, indicating the armchair. “Do I understand that you have already met with some unexpected adventure since your arrival in London?”

“Nothing of serious consequence, perhaps, but queer enough to make a man scratch his head.” He drew an envelope from his breast pocket and tossed it onto the breakfast table. “Look at that.”

The envelope was of cheap cream-laid paper, addressed in rough, splotchy block capitals: “Sir Henry Baskerville, Northumberland Hotel.” It bore the postmark of Charing Cross and had been mailed the preceding evening.

I unfolded the single sheet of ruled paper inside. Pasted across the center was a single sentence formed of printed words cut out and gummed to the page:

“As you value your life or your reason keep away from the moor.”

Only the final word, “moor,” had been written in ink.

“Now, Mr. Holmes,” Sir Henry asked, “what on earth can this mean, and who is taking such an interest in my affairs?”

“A singular document,” I murmured, examining it under my pocket lens. “And one that speaks volumes to the trained eye.”

“Can you tell who sent it?”

“I can tell you a great deal about the mechanical circumstances under which it was composed,” I answered, rotating the slip beneath the bright gaslight. “Notice first the print. These words were cut from a leading article of yesterday’s Times. You can recognize the distinctive Bourgeois type used exclusively in the major editorials of that journal. Look at the ragged edge where the word ‘reason’ is severed: it was not cut with shears, but clipped with short-bladed nail scissors. The blade slipped twice; the operator was in frantic haste.”

“In haste?” echoed Watson.

“In desperate haste, and working under extreme agitation,” I replied. “Notice also the gum: it is office mucilage, applied with an unsteady brush. But hold the paper half an inch from your nostrils, Watson. What do you detect?”

Watson sniffed gingerly. “A faint, delicate scent... like flowers.”

“White jessamine,” I declared. “The subtle perfume used by women of refined taste. The hand that wielded those scissors was trembling, and the hand was female! A woman, coerced or terrified by an overbearing master, sat in a hotel sitting room last evening and desperately pasted together this warning to preserve the life of a stranger!”

Sir Henry stared at the paper with renewed awe. “By thunder, Mr. Holmes, you see further into a piece of paper than any man I ever met. But wait—that is not the only piece of lunacy that has happened to me!”

“Indeed? Has something else occurred at your hotel?”

“My boot has been stolen!” cried Sir Henry in exasperation. “I bought a pair of handsome tan boots on the Strand yesterday. I put them outside my door last night to be polished. This morning, one of them was gone! The hotel staff searched the entire floor from attic to cellar—vanished into thin air!”

“A new tan boot?” I asked sharply, my pulse quickening. “Had it ever been worn?”

“Never. Not once.”

I leaned back, tapping my pipe bowl against my teeth. The puzzle was becoming crystalline. If an ordinary thief had taken the boot, he would have taken the pair. If a sneak-thief wanted leather, he would steal boots he could sell. But to steal a single boot? A single boot is useless to a thief—unless it is required by a predator seeking a scent! Yet a brand-new boot carries only the smell of factory varnish and calfskin—it possesses no human odour!

“The thief has made an egregious blunder,” I thought silently. “He took the tan boot, discovered it had no scent, and discarded it. He will come back for a worn boot before this day is done!”

I turned to Sir Henry. “Keep your eyes open, my dear sir. We are dealing with an enemy whose cunning matches his ruthlessness. Are you going straight back to your hotel?”

“Dr. Mortimer and I are going to stroll down Regent Street to do a little shopping first,” Sir Henry replied.

“Admirable,” said I. “Watson, fetch your hat and your service revolver. The game is afoot!”""",
        "content_cn": """次日上午十点整，楼梯口准时传来了沉稳而有力的脚步声。摩梯末医生推开房门，引介着那位性命与庞大遗产皆悬于一线的年轻爵士步入了我们的起居室。亨利·巴斯克维尔爵士约莫三十岁上下，身材不高却极其结实精悍。他生着一双机警敏锐、黑白分明的深邃眼睛，浓密粗黑的眉毛下方，是一张轮廓硬朗、隐隐透出一股顽强好斗气质的英挺面庞。他身着一套剪裁得体的红褐色粗花呢猎装，皮肤呈现出常年在加拿大西部无垠草原风吹日晒所特有的古铜色光泽；然而其举手投足间展现出的沉稳自若与得体教养，却无时无刻不在彰显着一位正统英国乡绅的名门底蕴。

‘能在此与您会面，真是深感荣幸，福尔摩斯先生，’年轻的爵士微笑着迎上前，与我握了握手。他的掌心宽厚有力，指节坚实如铁。‘即便摩梯末医生昨晚没有极力劝我前来拜访，我今天一早也必定会亲自登门向您求教。我听说您是一位专门破解世间难解之谜的大师，而我今天清晨在饭店恰好遭遇了一桩让我百思不得其解的怪事。’

‘请坐，亨利爵士，’我指了指壁炉旁的硬木扶手椅，‘这么说，您才刚踏上伦敦的土地不到二十四小时，便已经遭遇到某种非同寻常的意外波折了？’

‘严格说来，或许算不上什么天塌下来的灾祸，但其古怪程度足以让任何一个理智正常的人抓破头皮。’他将手伸进猎装的内侧口袋，掏出一枚发皱的信封，随手抛在我们面前的早餐桌上，‘二位请过目吧。’

信封用的是极其廉价普通的奶油色条纹信纸，正面的收信人地址用歪歪扭扭、粗劣笨拙的墨水大写印刷体写着：‘诺森伯兰饭店，亨利·巴斯克维尔爵士收’。邮戳显示是查令十字街邮局昨夜寄出的平信。

我用裁纸刀挑开封口，抽出了里面折叠平整的一张单页横格便签纸。便签纸的中央，赫然粘贴着由铅印字粒拼接而成的一整句短语：

“只要你还在乎自己的性命或理智，就请千万远离那片荒原。”

整句话中，唯有最后一个单词“荒原”（moor），是用普通的黑墨水手写补全的。

‘那么，福尔摩斯先生，’亨利爵士双臂抱胸，审视着我问道，‘这究竟意味着什么？到底是谁在如此煞费苦心地暗中刺探我的行程？’

‘一份极其非同寻常的物证，’我将便签纸平铺在膝头，取出高倍放大镜，在清晨透入窗户的明亮光线下逐字微观审视，‘对于经过严谨刑侦训练的眼睛而言，这薄薄的一张纸片所吐露的实情，简直比一场当面口供还要详实丰富得多。’

‘您能推断出寄信人是谁吗？’

‘我至少能为您彻底重构出这份信件在拼贴制作时的物理全貌，’我一边转动放大镜，一边徐徐剖析道，‘首先请看这些印刷字粒的字形。这行字是从昨天出版的《泰晤士报》头版社论中剪裁下来的。凡是对现代报业印刷术略有研究的人，一眼便能辨认出这种专属于《泰晤士报》严肃政治社评的“资产阶级体”（Bourgeois type）铅字。再请注意看“理智”（reason）这个词边缘那参差不齐的毛糙切口：它绝非裁纸大剪刀所裁，而是用一把刀刃极其短小的弯头指甲剪仓促剪下的！刀刃在转折处滑脱了两次，剪裁者当时的心情极其慌乱急迫！’

‘仓促慌乱？’华生忍不住插话道。

‘处于极度惊恐与十万火急的仓皇状态之下，’我指着字粒边缘溢出的暗黄色胶水痕迹，‘看这里的胶水：这是普通办公桌上常用的阿拉伯树胶浆糊，是用一支颤抖不稳的毛刷胡乱涂抹上去的。然而，华生，请将这封信拿起来，凑到你的鼻尖半寸以内。你能捕捉到什么？’

华生依言将信纸凑近鼻端，耸了耸鼻子：‘一种极其清淡微妙的幽香……似乎是某种花卉的香水？’

‘白素馨花（White Jessamine），’我笃定地断言，‘这是上流社会极具教养品位的名门闺秀才习惯使用的冷门名贵香氛！昨夜坐在某间幽暗的会客室里、手持指甲剪颤抖着剪碎报纸的，赫然是一位年轻女性的手！她受到了某种极其冷酷残暴势力的严密监控或强力威胁，却在良知的煎熬下，不惜冒着生命危险，拼死向一位素昧平生的陌生人发出最后的泣血警告！’

年轻的亨利爵士目瞪口呆地注视着我手中的信纸，眼神中流露出毫不掩饰的由衷敬佩：‘天呐，福尔摩斯先生，您竟然能从一张废纸里看出这么多门道！然而，昨夜发生的荒唐事还远不止这一桩！’

‘哦？饭店里还发生了什么离奇变故？’

‘我的皮靴被人偷了！’亨利爵士懊恼地一拍大腿，忿忿不平地嚷道，‘昨天下午我刚在斯特兰德大街的一家高档鞋店里，花重金买了一双崭新的黄褐色小牛皮短靴。昨晚临睡前，我随手将那双新靴子放在客房门外准备让侍从打油擦亮。结果今天早晨一开门——其中一只靴子竟然不翼而飞了！饭店经理带着仆役上上下下搜遍了整栋大楼，甚至连地下室的煤斗都翻了个底朝天，那只靴子就像融化在空气里一样彻底蒸发了！’

‘一双崭新的黄褐色小牛皮靴？’我的双眸瞬间亮起如同寒夜中的鹰隼，‘一次也没有穿过？’

‘一次也没有！崭新得连鞋底的涂层都没掉！’

我缓缓仰靠在椅背上，用指甲轻轻敲击着烟斗的硬柄。整个错综复杂的杀人迷局，在这一瞬间化作了晶莹剔透的因果罗网！如果是普通的宵小盗贼潜入饭店行窃，他必然会成双成对地将整双皮靴盗走变卖；世间绝无只盗走单只靴子的窃贼，除非——这只靴子不是为了穿戴，而是为了供某种具备极其敏锐嗅觉的掠食凶兽提取猎物的气味追踪媒介！然而，一双刚从工厂陈列架上取下的崭新皮靴，除了刺鼻的生皮鞣制油与鞋油味之外，根本没有任何属于人类躯体的活体皮脂气味！

‘凶手犯下了一个极其致命的盲动错误，’我在心中如电石火花般急速推导，‘他偷走了那只新靴，拿回隐秘巢穴后才懊恼地发现上面根本没有亨利爵士的体味媒介！他必定会再次潜回饭店，盗取一双饱含主人汗液的旧鞋！’

我霍然从椅子上站起身，目光如炬地注视着年轻的巴斯克维尔公爵：‘打起十二分的精神来，亨利爵士！我们此刻面对的，是一个智慧、胆魄与残忍程度皆登峰造极的可怕死敌！您现在是打算直接返回诺森伯兰饭店吗？’

‘摩梯末医生陪我去摄政街的裁缝铺定做几件体面的常服，顺便采购些乡间行囊，’亨利爵士答道。

‘绝妙之极！’我转头看向华生，‘带上你的遮阳软呢帽，华生，再把你的军用阿达姆斯左轮手枪压满子弹！真正的猎杀游戏，现在正式开场了！’"""
    },

    # -------------------------------------------------------------------------
    # Chapter 4: Part 2
    # -------------------------------------------------------------------------
    {
        "id": "holmes_ch04_part2_cab_chase",
        "ch_idx": 3, "part": 2,
        "title_en": "Chapter 4: Sir Henry Baskerville (Part II: The Shadow in Regent Street)",
        "title_cn": "第四章 亨利·巴斯克维尔爵士（下：摄政街的幽灵马车）",
        "pov": "holmes", "type": "branch", "anchor": None,
        "clues_en": [
            "Hansom Cab No. 2704 crawled behind Sir Henry and Mortimer down Regent Street",
            "Passenger possessed a bushy black square beard and gold-rimmed spectacles",
            "Passenger spotted Holmes, snapped roof trapdoor, and bolted down Oxford Circus",
        ],
        "clues_cn": [
            "牌照为2704号的双轮轻便马车沿着摄政街人行道边缘鬼祟尾随亨利爵士一行",
            "车厢侧窗后暗藏一名蓄着浓密方型黑大胡子、佩戴金丝眼镜的冷酷监视者",
            "监视者与福尔摩斯目光骤然相撞后，猛扣车顶活门催促车夫向牛津圆环狂飙突围",
        ],
        "choices_en": [
            {"id": "h_ch4_p2_c1", "text": "Trace the three broken threads: Cartwright’s hotel search, the wire to Barrymore, and Cabman 2704.", "target": "holmes_ch05_threads"},
            {"id": "h_ch4_p2_c2", "text": "[Switch POV to Jack Stapleton] Experience the tension inside Cab 2704 as Holmes gives chase.", "target": "stapleton_ch04_part2_cab_chase", "pov_switch": "stapleton"},
        ],
        "choices_cn": [
            {"id": "h_ch4_p2_c1", "text": "逐一收网三条追踪线索：卡特赖特排查废纸篓、电报试探管家、传讯2704号车夫。", "target": "holmes_ch05_threads"},
            {"id": "h_ch4_p2_c2", "text": "【视角切换：杰克·斯台普吞】体验2704号马车内直面福尔摩斯逼视时的惊魂瞬间。", "target": "stapleton_ch04_part2_cab_chase", "pov_switch": "stapleton"},
        ],
        "content_en": """We waited until Sir Henry and Dr. Mortimer had descended the stairs and turned down Baker Street before slipping out through the front door. The morning mist had cleared, giving way to a crisp autumn chill. Ahead of us, two hundred yards down the bustling pavement, the tall, stooping figure of Mortimer and the sturdy baronet were clearly discernible.

“Walk on the opposite side of the road, Watson,” I whispered, pulling my soft felt hat low over my eyes. “Keep your pace even. We must not alert them, and above all, we must not alert anyone who may be watching them.”

We crossed Oxford Street and turned into the broad sweep of Regent Street. The morning shopping traffic was thickening; carriages, omnibuses, and hansoms rattled noisily over the wooden paving blocks. Sir Henry and Mortimer paused before a shop window displaying sporting rifles.

And then my eye was caught by an anomaly in the traffic.

A hansom cab had pulled up along the kerb fifty yards behind our two friends. It did not discharge a passenger, nor did the driver raise his whip to solicit fares. Instead, it crawled at a snail’s pace, keeping precisely that distance between its yellow wheels and Sir Henry’s tweed back.

I gripped Watson’s forearm with fingers of steel. “Look, Watson! Look at that cab!”

“I see it. An ordinary hansom.”

“Look at the side window! Look through the side glass!”

The driver sat high up on his perch, bundled in an oilskin cape. But through the square side glass of the hansom’s cab-body, I caught the unmistakable silhouette of a passenger. A man sat back in the dark interior, leaning forward just far enough to keep his eyes trained on Sir Henry. He had a bushy, square black beard that swept over his coat collar, and the sunlight caught the glint of a pair of gold-rimmed spectacles upon his nose!

A spy! A professional tail, disguised with a heavy false beard!

At that instant, Sir Henry turned away from the shop and crossed the street. The cab immediately swung round and followed him.

“By heavens, Watson, he’s onto them!” I muttered. “We must have his number! Run!”

We darted through the stream of omnibuses, dodging a dray horse and plunging straight towards the hansom. But my swift movement had caught the passenger’s vigilant eye. As I reached within thirty paces of the cab, the bearded face turned sharply towards me. For one fraction of a second, our eyes locked—mine blazing with hunting fury, his widening with shock and sudden, razor-sharp recognition.

Instantly, a hand shot upward inside the cab. The trapdoor in the roof slammed shut with a wooden crack. The driver’s whip whistled through the air, cracking across the horse’s flank with the sound of a pistol shot.

The horse sprang forward like a courser. The hansom bounded over the curb, scattered a cluster of screaming pedestrians, and plunged recklessly into the roaring vortex of traffic converging on Oxford Circus!

“Stop! Stop that cab!” I shouted, sprinting down the pavement.

It was utterly futile. A heavy brewer’s dray swung across the mouth of the street, blocking our path. By the time Watson and I fought our way past the lumbering shire horses, the hansom was a receding speck disappearing into the maze of Cavendish Square.

I stopped beneath a lamp-post, leaning against the iron standard, breathing hard through my teeth. Yet even in the bitter sting of defeat, a savage satisfaction burned within me.

“Well, Watson,” said I, smiling through my vexation, “we have met a foeman worthy of our steel! Our friend does not lack resource. He spotted me the instant I closed the distance.”

“Did you get his number?” Watson panted.

“No. 2704,” I answered, tapping my notebook. “A registered London cab. That gives us our first handle upon the mystery. And now, Watson, we must return to Baker Street and set our three lines of counter-attack in motion!”""",
        "content_cn": """我们耐心地在起居室里等了足足两分钟，直到亨利爵士与摩梯末医生的脚步声彻底消失在贝克街的街口，我和华生才悄无声息地闪身出了大门。清晨弥漫的黄褐色浓雾已经渐渐被冷冽的秋风吹散，呈现出一片阴沉而明净的天光。在我们前方两百码外喧嚣的人行道上，摩梯末医生瘦长微驼的背影，以及亨利爵士结实利落的红褐色粗花呢猎装，在熙熙攘攘的人流中清晰可辨。

‘走到街道对面的骑楼阴影里去，华生，’我压低帽檐，低声叮嘱道，‘步幅保持均匀自然。我们既不能惊动前面的委托人，更绝不能惊动那条可能咬在他们身后的恶犬眼线！’

我们穿过牛津街，拐入开阔繁华的摄政街。清晨购物的人潮与马车车流逐渐变得稠密起来；四轮大马车、双层公共马车与轻便双轮马车在坚硬的木块路面上碾压出震耳欲聋的隆隆轰鸣。亨利爵士与摩梯末在一间陈列着精致猎枪的橱窗前停下了脚步，指指点点地交谈着。

就在这一刹那，车流中出现的一处极其反常的微小异动，猛然刺痛了我的双眼！

一辆墨绿色的双轮轻便马车（Hansom Cab），正不紧不慢地贴着人行道边缘的街沿徐徐滑行，恰好停在距离我们那两位朋友身后约五十码开外的马路上。车夫既没有拉门招揽乘客，车内也没有任何乘客起身下车的迹象。相反，马车的前轮宛如蜗牛般缓缓碾动，始终将它与亨利爵士那身粗花呢背影之间的距离，极其精准地锁定在五十码以内！

我的右手宛如铁钳般瞬间死死扣住了华生的大臂。‘看，华生！看那辆轻便马车！’

‘我看到了。一辆普普通通的双轮马车。’

‘看马车车厢侧面的长方形观景玻璃！透过玻璃看车厢里面！’

车夫高高地坐在车厢后上方的御手座上，身上裹着厚重的防雨油布披风。然而，透过车厢侧面那扇狭窄的茶色玻璃窗，我清晰地捕捉到了车厢深处端坐着的一个人形剪影！那名乘客将身躯深陷在幽暗的阴影里，仅仅探出小半张面孔，两道冰冷如毒蛇般的视线，正死死穿透窗户，牢牢钉在亨利爵士的后颈上！那人蓄着一部极其浓密扎眼、一直垂落到大衣领口的方型黑大胡子，而在他高挺的鼻梁上，一副金丝边眼镜的镜片，正反射出摄政街清晨惨白的冷光！

一个职业级的跟踪盯梢者！一个用浓密假胡子与假眼镜精心伪装的冷酷刺客！

正当此时，亨利爵士似乎看完了橱窗，转身穿过马路朝对面的商铺走去。那辆马车几乎在同一秒钟迅速调转马头，悄然跟了上去！

‘该死，华生，他紧咬住他们不放！’我低吼一声，‘我们必须拿到他的牌照号码！跑起来！’

我们二人如离弦之箭般冲出骑楼，在呼啸而过的双层马车与重型运货马车之间急速穿插穿梭，径直朝着那辆双轮马车狂奔而去！然而，我迅疾如风的突进动作，终究还是落入了那名潜伏者极其警觉的双眼！就在我冲刺到距离马车仅剩不到三十码的瞬间，车厢内那张黑胡子面孔猛然扭转向我！

在百分之一秒的电光石火之间，我和他的目光在晨光中轰然相撞——我的双眸燃烧着猎犬咬住猎物时的狂暴怒火，而他的瞳孔则在一瞬间因剧烈的惊骇与骤然的辨认而骤然收缩！

他认出了我！

车厢内部猛然伸出一只戴着皮手套的手，车顶上方的小木活门发出‘砰’的一声清脆爆响！车夫手中的长鞭在半空中呼啸抽落，伴随着一声宛如火枪击发般的清脆炸裂，重重抽打在拉车烈马的臀肉上！

那匹高大的骏马宛如受惊的狂兽般人立而起，两只黄色车轮猛地弹上街沿，险些撞翻人行道上几名尖叫退避的体面淑女，旋即如疯狂的战车般横冲直撞，一头扎入了汇聚在牛津圆环那片汹涌如潮的庞大车流漩涡之中！

‘拦住他！拦住那辆马车！’我一边在人行道上全力冲刺，一边声嘶力竭地厉声长啸！

然而一切都太迟了。一辆满载着厚重啤酒桶的重型八轮运货马车恰在此时缓缓横穿十字路口，庞大的车身如同一堵移动的木墙，彻底封死了我们的追击路线。等到我和华生好不容易绕过那几匹喷着粗气的夏尔挽马时，那辆轻便马车早已化作一道绿色的残影，彻底湮灭在卡文迪许广场错综复杂的小巷迷宫深处！

我在路边的一根铸铁煤气灯柱下骤然刹住脚步，单手扶着冰冷的灯柱，胸膛剧烈起伏，呼吸急促而粗重。然而，即便咽下了这口转瞬即逝的挫败苦果，一团炽热狂暴的战斗快感，却在我的胸腔深处熊熊燃烧起来！

‘精彩，华生，’我抹去额角渗出的一层冷汗，对着气喘吁吁的同伴露出了猎手特有的冷酷狞笑，‘我们终于遭遇了一位智勇双全、足以与我匹敌的强劲劲敌！这家伙绝非泛泛之辈，在距离缩短到致命范围的前一秒，他竟然精准地捕捉到了我的意图！’

‘你……你看清他的车牌号了吗？’华生扶着膝盖，上气不接下气地喘息着问道。

‘二七零四号，’我用铅笔在怀中的便签本上重重写下这四个数字，‘一辆在伦敦市交通管理局正式登记造册的营运马车！这为我们反撕开这场迷局提供了一根坚实的原点杠杆！现在，华生，立刻返回贝克街，我们预先准备的三路围剿铁网，现在必须以最快速度全线收拢了！’"""
    },

    # -------------------------------------------------------------------------
    # Chapter 5
    # -------------------------------------------------------------------------
    {
        "id": "holmes_ch05_threads",
        "ch_idx": 4, "part": 1,
        "title_en": "Chapter 5: Three Broken Threads (The Insolent Cabman & The Secret Expedition)",
        "title_cn": "第五章 三条断落的线索（傲慢的车夫与绝密潜伏计划）",
        "pov": "holmes", "type": "branch", "anchor": "anchor_threads",
        "clues_en": [
            "Thread 1 fails: Cartwright searched 23 hotel wastebaskets; found zero mutilated copies of The Times",
            "Thread 2 fails: Telegram to Barrymore at Baskerville Hall was delivered to his wife, proving nothing",
            "Thread 3 delivers a shock: Cabman John Clayton reveals his fare paid him two guineas and said “I am Sherlock Holmes!”",
            "Sir Henry’s old, scent-soaked black boot stolen from Northumberland Hotel, confirming predator now has the scent",
        ],
        "clues_cn": [
            "第一条线索断裂：差役卡特赖特搜遍查令十字街23家旅馆废纸篓，未找到被剪残的《泰晤士报》",
            "第二条线索断裂：发往巴斯克维尔庄园探查管家行踪的电报由其妻子代签，无法证实其当时身在何处",
            "第三条线索带来震撼挑衅：2704号车夫约翰·克雷顿招认，黑胡子雇主付了两坚尼并嚣张宣称‘我就是歇洛克·福尔摩斯！’",
            "亨利爵士一双沾满体味气味的旧黑皮靴在饭店离奇失窃，证实凶手已成功猎取用于恶犬追凶的气味媒介",
        ],
        "choices_en": [
            {"id": "h_ch5_c1", "text": "Dispatch Watson to escort Sir Henry to Devon while you secretly infiltrate Dartmoor.", "target": "holmes_ch06_part1_secret_departure"},
            {"id": "h_ch5_c2", "text": "[Switch POV to Jack Stapleton] Discover how Stapleton secured the old black boot.", "target": "stapleton_ch05_black_boot", "pov_switch": "stapleton"},
        ],
        "choices_cn": [
            {"id": "h_ch5_c1", "text": "派遣华生公开护送亨利爵士前往德文郡，自己则化装潜行、秘密潜伏达特荒原。", "target": "holmes_ch06_part1_secret_departure"},
            {"id": "h_ch5_c2", "text": "【视角切换：杰克·斯台普吞】窥探斯台普吞如何利用内应神不知鬼不觉窃走旧黑靴。", "target": "stapleton_ch05_black_boot", "pov_switch": "stapleton"},
        ],
        "content_en": """By evening, the three threads upon which I had relied to seize the London conspirator had snapped in my fingers, one by one.

The first thread was young Cartwright, the messenger boy from the district telegraph office whom I had dispatched to inspect the waste-paper baskets of twenty-three hotels in the Charing Cross district, seeking the mutilated copy of yesterday’s Times. He returned to Baker Street at five o’clock, his face smudged with soot, shaking his head. In twenty-three hotels, not a single sheet of mutilated newsprint had been preserved; the chambermaids had emptied the grates into the furnace hours before his arrival.

The second thread was my test telegram addressed to Mr. Barrymore, the butler at Baskerville Hall. If Barrymore had been in London shadowing Sir Henry, my telegram—marked “to be delivered into his own hand”—would have been forwarded to the capital or held awaiting his return. But the wire from the postmaster of Grimpen arrived at six: “Telegram delivered as addressed. Mr. Barrymore being in the loft at the time, receipt was signed by his wife.” An ambiguous, maddening result! Barrymore might indeed have been in Devon, or he might have arrived by the morning train, or his wife might have lied to cover his absence.

There remained the third thread: the driver of Hansom Cab No. 2704.

At seven o’clock, heavy boots climbed our staircase, and a burly, red-faced cabman in a drab box-coat stood upon our threshold, twisting his bowler hat in his calloused hands.

“John Clayton, sir,” said he, glancing nervously at our bookshelf and the chemical retorts on the side table. “I had a message from the yard that you wanted to see the man who drove cab No. 2704 down Regent Street this morning.”

“Precisely, Mr. Clayton,” said I, tossing a half-sovereign onto the table. “Tell me everything about the fare who engaged you this morning to shadow those two gentlemen.”

Clayton’s jaw dropped. “Lord love you, sir! How could you know he was shadowing them? He hailed me at ten o’clock in the Trafalgar Square cab-rank. He told me he was a private detective, and that if I followed a gentleman in tweed and another in black spectacles without being spotted, he’d give me two sovereigns. We followed them to Baker Street, then down to Regent Street, until you came tearing across the street like a mad bull. The moment he saw you, he yelled through the trapdoor: ‘Drive like hell to Waterloo Station, and there’s another guinea for you!’”

“And you drove him to Waterloo?”

“Straight to the station, sir! He jumped out before the cab had even stopped, threw two guineas into my lap, and vanished into the crowd on the platform!”

“Did he say anything before he left you?”

Clayton scratched his head, looking distinctly uncomfortable. “Well, sir, as he hopped out, he turned around and grinned at me through his black whiskers. ‘Cabman,’ says he, ‘if anyone asks who your passenger was, tell him that my name is Sherlock Holmes!’”

Watson sprang from his chair with an oath of indignation. For my part, I burst into a roar of laughter.

“A touch, Watson!” I cried, clapping my hands. “An undeniable touch! Our gentleman possesses a sense of humour as well as an iron nerve! He saw that I had marked his cab, he knew that I would trace the driver, and he sends me back his greeting with two sovereigns of insolence! This is no common criminal, Watson. This is a master of the craft!”

At that moment, the bell rang once more, and Sir Henry Baskerville burst into our sitting-room in a towering rage, accompanied by Mortimer.

“By heaven, Mr. Holmes!” the baronet shouted, slamming his hat onto the sofa. “This hotel of mine is a den of thieves! The joke is played out! Yesterday it was my brand-new tan boot that went missing; this afternoon, while I was washing my hands, someone walked into my bedroom and stole one of my old black boots—the ones I bought in Toronto and wore all across the Atlantic!”

I stopped laughing. In an instant, every trace of mirth vanished from my mind, replaced by a cold, deadly clarity.

“An old black boot?” I asked, my voice dropping to an icy monotone. “A boot that had been worn for weeks? A boot saturated with the perspiration of your feet?”

“Yes, sir! An old, worn, dirty boot!”

I looked at Watson, and in his startled eyes I saw the reflection of my own dread. The initial theft of the tan boot had been a false start; the predator had realized his error, returned to the hotel, and secured the true prize. Somewhere on the wild wastes of Dartmoor, a savage, flesh-and-blood monster was at this moment having the scent of Sir Henry Baskerville pressed against its ravenous nostrils!

“Sir Henry,” said I gravely, “there is no time to lose. You must leave for Dartmoor tomorrow morning. But you must not go alone.”

“Dr. Mortimer goes with me,” said the baronet.

“Dr. Mortimer has his patients, and his house is miles from the Hall. No, Sir Henry, you must take a companion whose courage and loyalty are beyond question, who will never leave your side by day and who will sleep outside your bedroom door with a loaded revolver by night.”

“And who might that be, Mr. Holmes? Will you come yourself?”

“My business in London imperatively forbids it,” I answered smoothly, avoiding Watson’s gaze. “I have vital matters here which chain me to the capital. But if he will consent, there is one man in all England whom I would trust with your life: my friend and comrade, Dr. Watson!”

Watson’s eyes widened with proud, resolute surprise. He gripped Sir Henry’s hand without a second’s hesitation. “I will go with all my heart, Sir Henry!”

Later that night, when Sir Henry and Mortimer had departed to pack, Watson looked at me across the hearth. “You really cannot come, Holmes? Is there no way you can accompany us to Devonshire?”

“It is impossible, Watson,” I replied, staring into the flickering embers of the fire. “I must remain in London. But you will send me daily reports—minute, detailed reports of every face, every movement, every whisper upon that moor.”

Watson nodded with soldierly devotion and retired to his chamber.

As the door clicked shut, I stepped to my desk and opened the secret drawer beneath the writing slope. From it, I took out my second passport, a rough peaked cap, a heavy frieze seaman’s pea-jacket, and a false identity papers under the name of “William Evans, surveyor.”

“Forgive me, my dear Watson,” I whispered into the darkness of the room. “If they know that Sherlock Holmes is in Devon, the spider will never venture out of the web. You must be the visible shield; I must be the unseen sword!”""",
        "content_cn": """到了当夜八点，我原以为十拿九稳能够擒获伦敦幕后黑手的三条追踪线索，竟然如同脆弱的蛛丝一般，在我指间被一一无情地绷断了。

第一条线索是年轻的卡特赖特——那个来自地区电报局、机灵能干的差役小子。我曾派他去逐一排查查令十字街附近的二十三家大饭店，在所有的废纸篓与壁炉炉灰里搜寻那张被残忍剪碎的昨日《泰晤士报》。下午五点整，他满头煤灰、垂头丧气地返回了贝克街。在整整二十三家饭店里，没有留下一星半点报纸的残片；那些手脚麻利的客房女仆早在清晨便将所有的壁炉炉灰与废纸通通倒进了大楼底层的焚化炉里！

第二条线索是我发给巴斯克维尔庄园管家巴里摩尔的那封暗藏杀机的试探电报。如果巴里摩尔此刻确实潜伏在伦敦暗中盯梢亨利爵士，那么我那封特别注明‘必须由收信人亲启当面签收’的电报，要么会被转寄至伦敦，要么会因无人签收而滞留在当地邮局。然而，格林盆村邮局在傍晚六点发回的回电却令我大失所望：‘电报已按地址送达。巴里摩尔先生当时正在阁楼清点杂物，收条由其夫人代为签署。’这是一个充满致命歧义与不确定性的狡猾结果！巴里摩尔可能当时确实身在德文郡，也可能是在收到风声后搭乘清晨的头班早车仓皇赶回，甚至可能是他的妻子在替他撒谎隐瞒行踪！

如今，唯有第三条线索尚存一线生机：那就是二七零四号轻便马车的当事车夫。

晚上七点整，伴随着楼梯上一阵沉重厚实的皮靴踏步声，一位面色红润、身材魁梧粗壮的马车夫推门走了进来。他身披一件厚重的草黄色粗呢大衣，手中拘谨地揉捏着那顶破旧的圆顶硬礼帽，神情紧张地打量着我们满屋的书架与实验桌上的化学蒸馏瓶。

‘小人名叫约翰·克雷顿，先生，’他结结巴巴地说道，‘车行调度所传信给我，说有位贵人急着要找今天上午在摄政街拉车的那位二七零四号车夫。’

‘正是如此，克雷顿先生，’我随手在桌上抛下一枚金光闪闪的半索弗林金币，‘把今天上午雇你的那位乘客的所有细节，原原本本地讲给我听。他当时是如何指使你尾随前面那两位绅士的？’

克雷顿的下巴惊得险些合不拢。‘老天爷保佑您，先生！您怎么会知道他在暗中盯梢？今天上午十点，那人在特拉法尔加广场的马车停靠点拦下了我的车。他自称是一名私家侦探，对我说只要我死死咬住前面那两位一位穿粗花呢猎装、一位戴金丝眼镜的绅士而不被发觉，他就赏我两枚金坚尼！我们一路从特拉法尔加广场跟着他们到了贝克街，又一路跟进了摄政街，直到您像一头被激怒的雄牛一样横穿马路朝我们猛扑过来！他一看见您，立刻拉开车顶的活门，发疯般朝我嘶吼：“别管红灯！快马加鞭冲到滑铁卢车站！到了我再赏你一坚尼！”’

‘然后你真把他送到了滑铁卢车站？’

‘一路狂奔直奔车站，先生！马车还没完全刹稳，他就跟泥鳅一样敏捷地窜了出去，把两枚沉甸甸的金坚尼随手扔在我的皮围裙上，一眨眼便湮没在站台汹涌的人潮里了！’

‘在离开马车之前，他难道没有留下任何话？’

克雷顿抓了抓后脑勺，脸上的表情显得极其古怪而尴尬：‘哎，先生，说来真邪门。就在他跳下踏板的那一瞬间，他突然转过身，隔着那丛浓密刺眼的黑胡子对我狞笑了一声。他说：“车夫，如果待会儿有人向你打听刚才坐车的人是谁，你就大大方方地告诉他——我的名字就叫歇洛克·福尔摩斯！”’

华生听到这里，忍不住从扶手椅上一跃而起，愤怒地爆出了一句罕见的军人粗口。而我却在短暂的惊愕之后，忍不住爆发出一阵震耳欲聋的狂笑！

‘漂亮，华生！’我狠狠抚掌大笑道，‘击中了！毫无疑问，这一剑结结实实地刺中了我们的要害！我们的这位对手不仅拥有钢铁铸就的坚韧神经，竟然还兼备一种近乎挑衅的黑色幽默感！他看穿了我记下了他的车牌号，料定我一定会顺藤摸瓜找到车夫，于是他竟然大模大样地借车夫之口，奉还给我两枚金坚尼的傲慢嘲弄！这不是寻常的下三滥窃贼，华生，这是一位深谙犯罪艺术的顶尖大师！’

正当此时，楼下的门铃再度急促地震响起来。紧接着，年轻的亨利·巴斯克维尔爵士在一脸惊慌失措的摩梯末陪同下，怒气冲冲地推门闯入了我们的起居室。

‘看在上帝的份上，福尔摩斯先生！’年轻的爵士一把将猎装软帽狠狠砸在皮沙发上，气得满脸通红，‘我住的那家诺森伯兰饭店简直是一个无法无天的贼窝！这种恶作剧到底还有完没完？！昨天刚偷了我一只崭新的黄褐色小牛皮靴；今天下午趁我回房洗手的功夫，居然又有人偷偷溜进我的寝室，把我的一只旧黑皮靴偷走了！那是我几年前在多伦多买的老靴子，穿着它横渡了整个大西洋，鞋底都快磨穿了！’

起居室内的欢笑声在刹那间荡然无存。我脸上的笑容如退潮般瞬间冻结，取而代之的是一种冷酷如冰霜般的极度严峻。

‘一双旧的黑皮靴？’我的语调骤然降低到接近绝对零度的冰冷极值，‘一双被你穿了数月、浸透了你双足体温与汗液气味的旧皮靴？！’

‘是的，先生！一双又脏又旧、散发着汗味的破皮靴！’

我猛然转头望向华生，在他剧烈收缩的惊骇眼眸中，我看到了自己内心深处那抹未曾言明的极度战栗。昨日失窃的那只新靴，仅仅是凶手在混乱中的盲动失误；而现在，这头潜伏在暗处的食人恶魔终于纠正了偏差，在诺森伯兰饭店成功猎取到了最完美的生物追踪媒介！此时此刻，在数百英里外荒凉凄厉的德文郡荒原深处，那只蛰伏在泥潭黑夜里的食人恶兽，正在凶手的驱使下，将它滴淌着涎水的巨大鼻孔，贪婪而兴奋地贴在亨利爵士这只浸透体味的旧靴子上！

‘亨利爵士，’我语气沉重如铅，‘刻不容缓。您必须在明天上午立即启程前往德文郡荒原。但您绝不能孤身一人前往。’

‘摩梯末医生会与我同行，’爵士说道。

‘摩梯末医生有他自己的诊所和病人，他的住宅距离巴斯克维尔庄园足足有数英里之遥。不，亨利爵士，您身边必须有一位忠诚如铁、胆魄过人、在白天形影不离、在黑夜能手握上膛左轮手枪贴身守卫在您卧房门外的高尚勇士！’

‘那会是谁呢，福尔摩斯先生？难道您愿意亲自同我前往？’

‘我伦敦的庞大刑侦业务严酷地剥夺了我离开首都的自由，’我语气平静自然，目光却刻意避开了华生投来的探询视线，‘伦敦有几桩牵涉内阁的重大机密案件正将我死死捆绑在此。但是，如果他愿意屈尊首肯的话，全英格兰唯有一人，我愿将您的身家性命毫不保留地托付于他——那就是我的挚友与战友，约翰·H·华生医生！’

华生的双眼瞬间因这突如其来的崇高使命感而闪烁出决然的光芒。他没有哪怕半秒钟的迟疑，大步上前紧紧握住了年轻爵士的手：‘我万分愿意同您前往，亨利爵士！’

深夜，当亨利爵士与摩梯末告辞返回饭店收拾行装之后，华生隔着熊熊燃烧的壁炉余烬注视着我：‘福尔摩斯，你真的抽不出身吗？难道就没有任何微小的可能，能让你与我们一同踏上开往德文郡的列车？’

‘绝无可能，华生，’我凝视着壁炉中噼啪作响的木柴火星，‘我必须留在伦敦。但我需要你每隔一天便向我发回一份详尽到极致的调查报告——荒原上的每一张陌生面孔、每一阵可疑的风声、甚至每一句私语，你都必须巨细靡遗地呈报给我。’

华生带着军人特有的绝对服从庄重地点了点头，熄灭烟斗返回了二楼寝室。

当他的房门发出一声轻微的合栓声后，我迅速走到书桌旁，按动机关弹开了藏在桌板夹层里的暗格。我从里面取出了我的另一本备用化名护照、一顶粗呢海员帽、一件沾满煤灰的厚重水手短大衣，以及一份伪造得天衣无缝的军械勘测员工作证件，上面的名字赫然写着：威廉·埃文斯。

‘原谅我的隐瞒，我最亲爱的华生，’我对着窗外漆黑深邃的贝克街夜空低声耳语，‘若让凶手得知歇洛克·福尔摩斯已经亲临德文郡，那只毒蛛便绝不会轻易爬出它的巢穴！你将是吸引那只恶犬全部注意力的坚固明盾；而我——将是在达特荒原黑暗迷雾中，给它以致命一击的无形利剑！’"""
    },
]
