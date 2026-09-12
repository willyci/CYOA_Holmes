# Initialize holmes_data.py
import json

HOLMES_NODES = []
# Holmes Chapter 1
HOLMES_NODES.extend([
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
            {"id": "h_ch1_p1_c2", "text": "[Switch POV to Dr. Watson] View Mortimer from Watson's sympathetic gaze.", "target": "ch01_part2_mortimer", "pov_switch": "watson"},
        ],
        "choices_cn": [
            {"id": "h_ch1_p1_c1", "text": "迎接杰姆士·摩梯末医生入座，请他陈述此番非同寻常的来访缘由。", "target": "holmes_ch01_part2_consultation"},
            {"id": "h_ch1_p1_c2", "text": "【视角切换：约翰·H·华生】以华生医生的同理心视角端详这位来客。", "target": "ch01_part2_mortimer", "pov_switch": "watson"},
        ],
        "content_en": """I sat at the breakfast-table in 221B Baker Street, my back turned toward the hearth-rug, watching the curved reflection of Dr. Watson in the well-polished silver coffee-pot. He had been turning Dr. Mortimer's forgotten walking stick in his fingers for the past ten minutes, his brow furrowed with earnest academic concentration.

'Well, Watson,' said I, 'what do you make of it?'

'How did you know what I was doing?' he gasped, glancing round with that ingenuous astonishment which never fails to delight me. 'I believe you have eyes in the back of your head!'

'I have, at least, a very well-polished silver-plated coffee-pot in front of me,' I answered, smiling. 'Come, Watson, tell me what you deduce from the stick. Let me hear you reconstruct the man by an examination of it.'

With immense gravity, Watson delivered his diagnosis: an elderly, venerable country doctor, esteemed by the local hunt, who had received this sturdy Penang-lawyer from grateful rural patients. It was a charming hypothesis, conceived with all of Watson's generous enthusiasm, but utterly innocent of the severe laws of observation.

'Really, Watson, you excel yourself,' I remarked, turning to face him. 'In noting your fallacies, one is guided toward the truth. You are not yourself luminous, but you are a conductor of light!'

I took the stick from his hands and examined it under my pocket lens. The facts were written across the wood with the clarity of print. The thick iron ferrule was worn down to half its original length, indicating extensive walking across rough gravel roads. The initials 'C.C.H.' stood not for a hunt club, but for Charing Cross Hospital. The date, 1884, five years past, marked the moment when a promising young house-surgeon, rather than a venerable practitioner, had resigned his post to establish a modest practice in rural Devonshire. And finally, running across the middle of the stick, were unmistakable indented marks—the tooth-impressions of a dog. The spaniel's jaw was distinctly outlined: teeth too broad for a terrier, too narrow for a mastiff. A curly-haired spaniel, which was even now trotting behind its master up our front steps!

The hall bell rang below. Through the window, I caught sight of a gaunt gentleman and a small, panting dog waiting upon the pavement.""",
        "content_cn": """我坐在贝克街221号B起居室的早餐桌旁，背对着壁炉前的地毯，通过那把擦拭得锃光瓦亮的纯银咖啡壶的反光，静静端详着华生医生的身影。在过去的十分钟里，他一直捧着那位神秘访客遗留下的槟榔屿手杖，眉头深锁，神情专注得近乎一位在显微镜下解剖标本的学者。

‘那么，华生，’我适时开口道，‘对于这根手杖，你究竟得出了什么高见？’

‘你怎么知道我在做什么？’华生惊愕地抬起头，脸上流露出那种每每令我由衷愉悦的单纯诧异，‘我敢发誓你后脑勺上一定长着眼睛！’

‘眼睛倒是没有，但我面前恰好有一把反光极佳的镀银咖啡壶，’我微笑着转过身，‘来吧，华生，把你的推论讲给我听听。让我听听你是如何根据这件器物来勾勒出主人的面貌的。’

华生清了清嗓子，以其惯有的庄重语调给出了推断：一位年长而受人爱戴的乡村老医生，深得当地狩猎俱乐部的信赖，因而获赠了这根粗壮结实的槟榔屿手杖。这是一个充满温情的假说，饱含着华生善良天性所特有的浪漫联想，然而在严密冰冷的观察法则面前，却破绽百出。

‘坦白讲，华生，你真让我刮目相看，’我接过手杖，赞赏地点了点头，‘在指出你的谬误的过程中，真理往往反而变得清晰可见。你自己或许并非发光体，但你却是一位极佳的光之导体！’

我掏出口袋里的放大镜，借着晨光细细审视手杖的纹理。事实如同铅字印刷般清晰地刻在木质之上。厚重的铁箍已被粗糙的碎石路磨去了一半，证明主人经常在崎岖的乡间长途跋涉；‘C.C.H.’并非某种乡村猎狐俱乐部，而是伦敦著名的查令十字医院（Charing Cross Hospital）；手杖上刻有‘一八八四年’的赠别年份，这表明一位才华横溢、前途远大的青年住院外科医士，在五年前离开都市前往德文郡乡间行医；而最有趣的是手杖正中那一排清晰可见的凹陷齿痕——那是犬类在叼衔手杖时留下的牙印。上下颚齿距比㹴犬宽，却远比马士提夫獒犬狭窄，毫无疑问，那是一只卷毛西班牙猎犬。而此时此刻，这只小猎犬正欢快地跟随着它的主人踏上我们门前的台阶！

楼下的门铃适时响起。透过临街的窗户，我已望见一位身材瘦高的绅士与一只气喘吁吁的小狗正伫立在贝克街的雾气之中。"""
    },
    {
        "id": "holmes_ch01_part2_consultation",
        "ch_idx": 0, "part": 2,
        "title_en": "Chapter 1: Mr. Sherlock Holmes (Part II: The 1742 Manuscript)",
        "title_cn": "第一章 歇洛克·福尔摩斯先生（下：古老手稿与医学专家的求助）",
        "pov": "holmes", "type": "branch", "anchor": None,
        "clues_en": [
            "Mortimer identifies Holmes as second-highest expert in Europe behind Bertillon",
            "Ancient manuscript dated 1742 preserved from Baskerville Hall",
        ],
        "clues_cn": [
            "摩梯末将福尔摩斯列为仅次于贝蒂荣的欧洲第二高明专家",
            "摩梯末胸袋中珍藏的一七四二年巴斯克维尔庄园古老手稿",
        ],
        "choices_en": [
            {"id": "h_ch1_p2_c1", "text": "Invite Mortimer to read the manuscript of the Baskerville curse.", "target": "holmes_ch02_part1_legend"},
            {"id": "h_ch1_p2_c2", "text": "Question Mortimer directly regarding the sudden demise of Sir Charles Baskerville.", "target": "holmes_ch02_part2_footprints"},
        ],
        "choices_cn": [
            {"id": "h_ch1_p2_c1", "text": "请摩梯末医生展开那份一七四二年的古老手稿，宣读巴斯克维尔的诅咒传说。", "target": "holmes_ch02_part1_legend"},
            {"id": "h_ch1_p2_c2", "text": "直接向摩梯末询问查尔斯·巴斯克维尔爵士猝死案的现代物理线索。", "target": "holmes_ch02_part2_footprints"},
        ],
        "content_en": """The door opened, and Dr. James Mortimer stepped into the room. He was very tall, very thin, with a long nose like a beak, which jutted out between two keen, grey eyes, set closely together and sparkling brightly behind a pair of gold-rimmed glasses. He was clad in a professional but rather slovenly fashion, for his frock-coat was dingy and his trousers frayed. Though young, his long back was already bowed, and he walked with a forward thrust of his head and a general air of peering benevolence.

'I had hardly hoped,' he said, bowing with awkward courtliness, 'to find you in. Mr. Sherlock Holmes, I presume? And Dr. Watson. Ah, Mr. Holmes, you interest me extremely. I had hardly expected so dolichocephalic a skull or such well-marked supra-orbital development! Would you have any objection to my running my finger along your parietal fissure? A cast of your skull, sir, until the original is available, would be an ornament to any anthropological museum.'

I waved him to an armchair, mildly amused by his enthusiastic craniology. 'You are an enthusiast in your line of thought, sir, as I am in mine. But I observe from your forefinger that you make your own cigarettes. Pray do not hesitate to light up.'

He drew a paper from his breast-pocket with nervous fingers. 'The truth is, Mr. Holmes, I have come upon a matter of the most singular and grave importance. In your special line of research, you stand second only to Monsieur Bertillon of Paris.'

'Indeed, sir! Then perhaps Monsieur Bertillon would be the proper person to consult.'

'In pure precision of anthropometry, perhaps,' he corrected quickly. 'Yet as a practical man of affairs, as an unraveller of dark and tangled skeins, you are without a rival in Europe. The matter which brings me to you relates to the family of the Baskervilles. I hold in my pocket an ancient manuscript, dating from the year 1742, placed in my trust by the late Sir Charles Baskerville, whose sudden and tragic death three months ago cast a pall of horror across the whole of Dartmoor.'

He smoothed the yellowed parchment across his knee, his eyes dark with an emotion that transcended mere academic curiosity.""",
        "content_cn": """房门应声而开，杰姆士·摩梯末医生大步迈入房内。他身材高瘦得惊人，鼻梁如鹰喙般挺拔凸起，在两只灰色锐目间显得分外醒目；镜片之后的眼神充满着学者的狂热与探求。他的装束带着专业医者的体面，却又略显不修边幅——长礼服下摆微微泛黄，长裤裤脚也有磨损的毛边。尽管年纪尚轻，他的后背已微微前屈，走起路来头颈前倾，整个人散发着一种专注而略带拘谨的仁慈学究气息。

‘我原本不敢抱太大奢望，’他笨拙而谦逊地欠身行礼，‘竟能如此顺利地拜会二位。想必阁下就是歇洛克·福尔摩斯先生？而这位便是华生医生了。啊，福尔摩斯先生，您的头部结构实在令我着迷至极！我万万没有想到，您的颅骨竟然呈现如此完美的超长头型（dolichocephalic），眉间上眶的骨骼突起更是如此显著！您介意让我用手指抚摸一下您的顶骨骨缝吗？倘若在令尊令堂百年之后能为您翻制一座颅骨模型，那必将成为任何人类学博物馆的无上珍宝！’

我微笑着抬手请他在扶手椅上就坐，对这位狂热的人类学家不免感到几分莞尔。‘先生，在您所专精的领域里，您无疑是一位饱含热忱的专家，正如同我在我的行当一样。不过从您食指内侧的焦黄痕迹来看，您平日习惯自己卷烟，请不必客气，尽情抽吧。’

摩梯末医生闻言，神经质地从长礼服内袋中掏出一卷泛黄的纸卷。‘实不相瞒，福尔摩斯先生，我此次登门，乃是为了委托一件极度离奇、性命攸关的重大事件。在某些专门的研究领域里，您的声望放眼全欧洲，恐怕仅次于巴黎的贝蒂荣先生（Monsieur Bertillon）。’

‘哦，果真如此吗？那么阁下或许应当直接渡海去向贝蒂荣先生求教才对。’

‘在人体测量学的绝对精度上，或许贝蒂荣先生独步一时，’他急切地辩解道，‘但在实际纷繁复杂的事务处理上，在解开幽暗阴森的绝望谜团方面，全欧洲绝无人能与您比肩！我今日带来的，正是关于巴斯克维尔家族的惊天疑案。我的口袋里装着一份一七四二年的古代家族手稿，它是在三个月前不幸猝死的查尔斯·巴斯克维尔爵士生前亲手托付给我的遗物。而查尔斯爵士的骤然离世，至今仍让整片达特穆尔荒原笼罩在无尽的恐怖阴霾之中。’

他小心翼翼地将那卷发脆发暗的手稿平铺在膝盖上，苍白的镜片后透出一种绝非纯粹学术研究所能解释的恐惧。"""
    }
])
# Holmes Chapter 2
HOLMES_NODES.extend([
    {
        "id": "holmes_ch02_part1_legend",
        "ch_idx": 1, "part": 1,
        "title_en": "Chapter 2: The Curse of the Baskervilles (Part I: The Legend of Hugo)",
        "title_cn": "第二章 巴斯克维尔的灾祸（上：雨果传说与迷信神话）",
        "pov": "holmes", "type": "anchor", "anchor": "anchor_curse_holmes",
        "clues_en": [
            "1742 manuscript recounts Hugo Baskerville's profane revels and death upon the moor",
            "Legend warns the sons of Baskerville never to cross the moor in the dark hours",
        ],
        "clues_cn": [
            "一七四二年手稿记载了恶棍雨果·巴斯克维尔掳掠少女并遭地狱猎犬撕裂喉管的诅咒始末",
            "手稿郑重告诫巴斯克维尔家族子嗣切勿在黑暗降临后夜渡达特穆尔荒原",
        ],
        "choices_en": [
            {"id": "h_ch2_p1_c1", "text": "Listen to the modern facts of Sir Charles's death and the physical footprints.", "target": "holmes_ch02_part2_footprints"},
            {"id": "h_ch2_p1_c2", "text": "Dismiss the romantic fairy tale and demand tangible, modern evidence.", "target": "holmes_ch02_part2_footprints"},
        ],
        "choices_cn": [
            {"id": "h_ch2_p1_c1", "text": "聆听查尔斯爵士猝死案的现代事实与现场留下的物理脚印。", "target": "holmes_ch02_part2_footprints"},
            {"id": "h_ch2_p1_c2", "text": "驳斥封建中世纪的神话传说，要求摩梯末出示当下发生的切实证据。", "target": "holmes_ch02_part2_footprints"},
        ],
        "content_en": """Mortimer pushed his spectacles up onto his high forehead and began to read from the 1742 manuscript with a high, cracked voice. It was written in the quaint, legalistic English of the early eighteenth century, warning the heirs of Baskerville against the ancestral curse that had haunted the line since the Great Rebellion.

The tale was familiar enough in the annals of rural folklore: Hugo Baskerville, a wild, profane, God-forsaken roisterer, had conceived a ruthless passion for the maiden daughter of a yeoman near Widecombe. One Michaelmas night, with five of his dissolute companions, he carried the girl off to the Hall and locked her in an upper chamber. While the revellers bellowed obscene songs below, the terrified girl lowered herself by the ivy and fled across the moonlit moor toward her father's farm, nine miles distant.

When Hugo discovered her escape, he swore a hideous oath, giving his body and soul to the powers of evil if he might overtake her, and unleashed his pack of hounds into the dark. His companions mounted their horses and galloped after him. In a deep granite gorge upon the moor, they came upon Hugo's black mare, riderless and lathered in white foam. Pushing their horses down into the ravine, they found the maiden lying dead upon the heather, slain by fear and fatigue. But beyond her, crouched over the prostrate body of Hugo Baskerville, was a foul thing—a great, black beast, shaped like a hound yet larger than any hound that ever mortal eye had rested upon, tearing at his throat. As they watched in frozen terror, the monster turned its blazing eyes and dripping jaws upon them, and the horsemen shrieked and fled for their lives.

I leaned back in my chair, stifling a yawn, and pressed my fingertips together.

'Well, Mr. Holmes?' asked Mortimer, looking up over his glasses. 'Does the narrative interest you?'

'To a collector of fairy tales, perhaps,' said I coolly. 'It has the picturesque extravagance of an eighteenth-century melodrama. But surely, Dr. Mortimer, you have not brought me this Gothic nursery-rhyme to solve in the year of our Lord 1889?'""",
        "content_cn": """摩梯末医生将眼镜推到高耸的前额上，用一种尖细而略显沙哑的声音宣读起那份一七四二年的手稿。字里行间充斥着十八世纪初那种古朴刻板的法言法语，郑重告诫巴斯克维尔家族的历代子嗣，警惕自大叛乱（Great Rebellion）时期便纠缠不散的祖传魔咒。

这段故事若放在乡野民间传说的范畴里，倒也算得上一桩典型的志异题材：庄园先祖雨果·巴斯克维尔是一个狂暴放荡、目无神明的恶棍。他在达特穆尔荒原上看中了怀德康附近一位自耕农的美貌女儿。某一年的米迦勒节前夜，雨果纠集了五名狐朋狗友，强行将那少女掳掠至巴斯克维尔庄园并囚禁在楼上的客房中。正当恶汉们在楼下彻夜狂饮作乐之际，惊恐绝望的姑娘顺着窗外的常春藤滑下高墙，趁着惨淡的月色狂奔向九英里外的父亲农庄。

雨果发现少女逃跑后暴跳如雷，公然发下毒誓：若能追上此女，宁愿将肉体与灵魂悉数奉献给魔鬼！他随即牵出整整一队猎犬扑入荒野，同伙们亦策马穷追不舍。当狂欢者们追至荒原深处的一处花岗岩裂谷时，首先映入眼帘的是雨果那匹狂奔脱缰、口吐白沫的纯黑战马。他们战战兢兢地策马探入谷底，只见那不幸的少女已因惊惧和力竭香消玉殒于石楠花丛之中。而在不远处雨果倒毙的尸骸之上，正踞坐着一头令人毛骨悚然的怪兽——那是一只巨大如恶魔般的纯黑凶兽，身形虽酷似猎犬，其体魄却比凡间任何巨犬更为可怖！这头地狱巨兽正大口撕咬着雨果的喉管，当它转过两只喷吐烈焰的血红巨眼与滴淌腥血的獠牙望向来人时，所有人吓得魂飞魄散，狂呼逃窜！

我靠在扶手椅背上，极力克制着一个呵欠，双手指尖轻轻相对。

‘那么，福尔摩斯先生？’摩梯末医生从镜片上方凝视着我，‘这篇文字难道未能引起您的兴趣吗？’

‘倘若对于一位搜集乡村志异的民间学者而言，或许颇具趣味，’我冷淡地答道，‘字里行间充满了十八世纪通俗哥特剧那华丽而夸张的辞藻。然而，摩梯末医生，您总不至于指望我在公元一八八九年的今天，去侦破一桩百年前的中世纪童话吧？’"""
    },
    {
        "id": "holmes_ch02_part2_footprints",
        "ch_idx": 1, "part": 2,
        "title_en": "Chapter 2: The Curse of the Baskervilles (Part II: Footprints of a Gigantic Hound)",
        "title_cn": "第二章 巴斯克维尔的灾祸（下：巨大恶犬的足迹）",
        "pov": "holmes", "type": "branch", "anchor": None,
        "clues_en": [
            "Sir Charles stood smoking for 20 minutes at the moor gate before his death",
            "Footprints changed to tiptoes, indicating flight from a terrifying pursuer",
            "Twenty yards from the body lay the fresh, distinct footprints of a gigantic hound",
        ],
        "clues_cn": [
            "查尔斯爵士猝死前在通往荒原的侧门足足驻足抽烟二十分钟",
            "现场足印突然变为脚尖点地，证明其在极度恐慌中亡命飞奔",
            "距尸体二十码外的松软湿泥上，留有清晰无误的巨大恶犬足印",
        ],
        "choices_en": [
            {"id": "h_ch2_p2_c1", "text": "Commit to investigating the modern problem and order a complete survey map of Dartmoor.", "target": "holmes_ch03_problem"},
            {"id": "h_ch2_p2_c2", "text": "Interrogate Mortimer closely concerning the precise physical ground and barriers around the gate.", "target": "holmes_ch03_problem"},
        ],
        "choices_cn": [
            {"id": "h_ch2_p2_c1", "text": "决定全力接手这桩现代命案，要求调阅整幅达特穆尔军用测量地形图。", "target": "holmes_ch03_problem"},
            {"id": "h_ch2_p2_c2", "text": "就侧门周遭的物理地势、泥土湿润度及树篱阻隔向摩梯末展开高强度盘问。", "target": "holmes_ch03_problem"},
        ],
        "content_en": """'The legend is old, Mr. Holmes,' Mortimer replied, his voice dropping to a whisper, 'but what I have now to read to you is of today.'

He drew a folded copy of the Devon County Chronicle from his pocket and read the coroner's verdict on the sudden death of Sir Charles Baskerville. Sir Charles, having made a vast fortune in South African speculation, had returned to restore his ancestral seat. He was beloved for his benevolence, but suffered from chronic heart disease and nervous dread. On the night of May 4th, he took his customary evening stroll down the famous yew alley of Baskerville Hall. He never returned. At midnight, his butler, Barrymore, found the old baronet lying dead at the far end of the alley, near the wicker gate opening onto the moor. The autopsy revealed no trace of violence, and the verdict was death from cardiac exhaustion.

Mortimer refolded the paper. 'That is the official account, Mr. Holmes. It was the account given to the coroner's jury. But I have withheld the real facts, because as a doctor and a trustee of the estate, I feared to depopulate the district by exciting panic.'

My attention sharpened instantly. 'You investigated the ground yourself?'

'I did. The yew alley is bounded on either side by impenetrable twelve-foot hedges. Down the center is a strip of turf eight feet broad, with gravel paths on either side. Sir Charles had walked down the path, stopped at the wicker gate that opens onto the moor, and stood there smoking for at least twenty minutes, as proved by the two cigar ashes dropped on the ground. When he turned to leave the gate, his footprints changed! He had not walked back—he had run, run desperately for his life, running on his tiptoes until his heart burst and he pitched forward upon his face.'

'And what of the marks upon the earth?' I demanded.

Mortimer leaned forward until his pale face was within six inches of mine. His pupils were dilated with sheer horror.

'Mr. Holmes, there were no marks upon his body. But twenty yards beyond where he lay, upon the soft, damp peat outside the wicker gate, where no sheep or cattle could have trodden—I saw them distinctly, freshly pressed into the mire!'

'Footprints?'

'Footprints.'

'A man's or a woman's?'

Dr. Mortimer looked at us in a whisper that made the window-panes seem to rattle:

'Mr. Holmes, they were the footprints of a gigantic hound!'""",
        "content_cn": """‘传说固然陈旧，福尔摩斯先生，’摩梯末医生的声音骤然降低，变得森冷沉重，‘但我接下来要读给二位听的，却是发生在此刻的事实！’

他从口袋中掏出一张折叠整齐的《德文郡纪事报》，宣读了关于查尔斯·巴斯克维尔爵士猝死案的验尸官官方裁决。查尔斯爵士在南非矿业投机中积累了数以十万计的巨额财富，晚年回归故里斥资重修祖宅。他为人慷慨仁厚，却长期罹患严重的心脏器质性病变并伴有极度神经衰弱。五月四日深夜，他按照惯例前往庄园著名的红豆杉小径（Yew Alley）散步，却再也没有归来。午夜时分，管家白利墨在通往荒原的侧门旁发现了老爵士仆倒在地的尸身。尸检未见任何机械性损伤痕迹，陪审团最终裁定死因为急性心力衰竭。

摩梯末医生将报纸重新折好。‘这是公开的版本，福尔摩斯先生。也是提交给验尸法庭的唯一陈述。然而，我却隐瞒了最致命的核心事实——因为身为他的私人医师与遗产托管人，我深知一旦将真相公之于众，整片达特穆尔地区的居民都将陷入无法遏制的癫狂恐慌，庄园也将就此荒废废弃！’

我的神经瞬间紧绷起来，坐直了身子。‘你亲自勘验了案发现场的地面？’

‘正是！那条红豆杉小径两旁是足有十二英尺高、密不透风的严密树篱。中央是八英尺宽的平整草坪，两侧铺有碎石小径。查尔斯爵士沿着小径走到通向荒原的木栅侧门旁，他在那里足足驻足抽烟了二十分钟以上——散落在地面的两小撮雪茄烟灰可以确凿无误地证明这一点！然而，当他离开侧门折返时，地面的脚印彻底改变了！他绝非步行返回——而是在极度的绝望与恐慌中亡命狂奔！他的脚尖深深扎入泥土，整个脚掌几乎离地飞奔，直到心脏终于不堪重负破裂骤停，面朝下扑倒在草坪之中！’

‘那么地面上可曾发现其他印记？’我立刻追问道。

摩梯末医生猛地前倾身躯，苍白的面孔几乎贴到了我的鼻尖。他的瞳孔因极度的骇异而剧烈放大。

‘福尔摩斯先生，死者身上没有任何伤痕。然而在距离尸体倒卧处二十码外、位于侧门外潮湿松软的泥炭沼地之上——在绝无牛羊能够涉足的盲区之中——我清清楚楚地看到了一串崭新的印记！’

‘脚印？’

‘正是脚印。’

‘是男人的，还是女人的？’

摩梯末医生凝视着我和华生，吐出了一句令整间起居室温度骤降的惊悚耳语：

‘福尔摩斯先生……那是属于一只巨大无朋的恶犬的足印！’"""
    }
])
# Holmes Chapter 3 & 4
HOLMES_NODES.extend([
    # Chapter 3
    {
        "id": "holmes_ch03_problem",
        "ch_idx": 2, "part": 0,
        "title_en": "Chapter 3: The Problem (Dartmoor Topography and the Lone Vigil)",
        "title_cn": "第三章 疑案（达特穆尔地图与浓烟沉思）",
        "pov": "holmes", "type": "branch", "anchor": None,
        "clues_en": [
            "Sir Henry Baskerville is arriving from Canada at Waterloo Station",
            "Ordnance Survey maps reveal Grimpen Mire, Merripit House, and isolated tors",
            "Total estate valued at £740,000 creates monumental financial motive",
        ],
        "clues_cn": [
            "查尔斯爵士唯一法定继承人亨利·巴斯克维尔爵士正从加拿大抵英",
            "军用测绘地图标注出大格林盆泥潭、梅利琵宅邸及荒原险要岩岗",
            "巴斯克维尔庄园总估值高达七十四万英镑，形成极度庞大的买凶谋财动机",
        ],
        "choices_en": [
            {"id": "h_ch3_c1", "text": "Prepare to receive Sir Henry Baskerville and Dr. Mortimer at Baker Street tomorrow.", "target": "holmes_ch04_part1_warning"},
            {"id": "h_ch3_c2", "text": "[Switch POV to Dr. Watson] See Watson returning to find 221B choked with shag tobacco.", "target": "ch03_problem", "pov_switch": "watson"},
        ],
        "choices_cn": [
            {"id": "h_ch3_c1", "text": "整理达特穆尔地理论据，准备明早十点在贝克街迎接亨利爵士与摩梯末。", "target": "holmes_ch04_part1_warning"},
            {"id": "h_ch3_c2", "text": "【视角切换：约翰·H·华生】从华生的视角见证他傍晚归来时被浓烈烟丝笼罩的贝克街。", "target": "ch03_problem", "pov_switch": "watson"},
        ],
        "content_en": """The moment Mortimer took his departure, I sent Watson out for the day, advising him to seek fresh air. For my own part, I had no desire for movement. I had a problem of the first magnitude to digest.

I took down my mouse-coloured dressing-gown, filled a cherry-wood pipe with the strongest, foulest shag tobacco from the toe of my Persian slipper, and locked myself in the sitting-room. By noon, the air was dense with an impenetrable blue haze. Upon the table lay spread a six-inch Ordnance Survey map of Dartmoor.

Here, within this five-mile perimeter of wild Devonshire bog and granite, lay the arena of our duel. I traced every contour line with a dry pen. Baskerville Hall stood encircled by dense plantations, facing south toward the vast, treeless wilderness. Four miles to the north-east lay the Great Grimpen Mire, marked with sinister marsh-crosses—a quagmire capable of swallowing an ox whole. Isolated within its fringes sat Merripit House, occupied, so Mortimer told me, by a naturalist named Stapleton and his sister. Further south lay Coombe Tracey and the estate of old Frankland.

The financial calculus was inescapable. Sir Charles had died intestate, and the entire estate—securities, land, timber, and liquid funds amounting to upwards of £740,000—passed by law to his nephew, Sir Henry Baskerville, a young farmer from Canada who was even now landing at Waterloo station.

If the superstition of the hound was an engine devised by human cunning, who stood to profit? If Sir Henry fell, who was the next heir? Mortimer had spoken of a distant cousin, James Desmond, an elderly clergyman in Westmorland. But behind the screen of wilderness, what other hands moved the pawns? The hound was physical—its footprints in the peat settled that beyond dispute. If it was flesh and blood, it required feeding, sheltering, and directing.

I knocked the gray ashes from my third pipe as twilight fell over London. A worthy adversary had thrown down the gage of battle. Tomorrow morning, at ten o'clock, Sir Henry Baskerville would arrive at 221B Baker Street. We should see whether human intellect could unravel what provincial terror had consecrated to the devil.""",
        "content_cn": """摩梯末医生刚一告辞，我便劝说华生外出散心。至于我自己，则完全没有任何漫步街头的兴致。摆在我面前的，是一桩足以令全欧洲最顶尖的大脑为之高度亢奋的头等智力悬案。

我换上了那件鼠灰色的旧晨袍，从波斯软头拖鞋尖里掏出那袋最冲、最浓烈的黑色烟丝塞满石楠烟斗，将起居室的门窗紧紧反锁。正午时分，整间屋子早已弥漫着浓密得伸手不见五指的蓝灰色烟雾。长条木桌之上，赫然摊开着一幅大比例尺的德文郡达特穆尔军用测量局地形图。

在这方圆五英里的荒蛮泥潭与花岗岩巨石丛中，便是我们将要与凶手博弈的生死擂台。我用没蘸墨水的钢笔尖细细摩挲着每一条等高线。巴斯克维尔庄园被厚密的古树林环绕，正面朝向荒凉无垠的荒原；东北方四英里处，便是密密麻麻标有沼泽危险十字的大格林盆泥潭（Great Grimpen Mire）——那是一处足以将整头活牛吞噬得尸骨无存的万丈泥渊！而在泥潭边缘孤零零伫立的，是一座名为梅利琵（Merripit House）的宅邸，据摩梯末称，那里住着一位名叫斯台普吞的昆虫博物学家及其胞妹；再往南，则是库姆马西村以及酷爱诉讼的弗兰克兰老头。

而这桩案件背后的经济脉络更是显豁至极。查尔斯爵士生前未立正式遗嘱，整座庄园、大批证券、林地及银行现款——总额高达惊人的七十四万英镑巨款——按继承法则将悉数归于其侄儿亨利·巴斯克维尔名下！这位年轻的加拿大垦殖农夫，此时此刻正搭乘列车抵达滑铁卢车站！

倘若恶犬的迷信乃是凡间歹徒假借幽灵之名所设的杀人工具，那么究竟何人能从这场连环死亡中攫取巨利？倘若亨利爵士亦步其后尘暴毙荒原，下一个法定继承人又是谁？摩梯末曾提及远在威斯特摩兰郡的一位年迈穷牧师詹姆斯·戴斯蒙。然而在达特穆尔荒原的迷雾背后，是否隐匿着另一只操盘全局的无形黑手？那只恶犬必定是具备实体血肉的造物——留在泥炭上的真实足印已无可辩驳地证实了这一点！既然是血肉之躯，便需要有人饲养、隐匿，并指引其展开血腥撕咬！

当暮色笼罩伦敦街头时，我将第三斗烟灰磕入壁炉。一位足以令我倾尽心力的强大对手已然向我掷下了战书。明早十点，亨利·巴斯克维尔爵士将踏入贝克街221号B。且让我们看看，究竟是人类的理性科学能刺破迷雾，还是乡野的邪恶阴谋能继续肆虐！"""
    },

    # Chapter 4 Part 1
    {
        "id": "holmes_ch04_part1_warning",
        "ch_idx": 3, "part": 1,
        "title_en": "Chapter 4: Sir Henry Baskerville (Part I: The Cut Times and the Missing Boot)",
        "title_cn": "第四章 亨利·巴斯克维尔爵士（上：剪报警告与失窃的靴子）",
        "pov": "holmes", "type": "anchor", "anchor": "anchor_london_mission_holmes",
        "clues_en": [
            "Anonymous warning letter composed from words cut from yesterday's Times lead article",
            "Cut with short-bladed nail scissors, pasted with gum, faintly scented with white jessamine",
            "Sir Henry's brand new tan boot stolen from Northumberland Hotel",
        ],
        "clues_cn": [
            "匿名警告信所有词句均从昨日《泰晤士报》社论中剪裁拼贴而成",
            "使用指甲短刃剪刀裁剪，涂抹植物树胶，带有极其微弱的素馨花香水气息",
            "亨利爵士置于诺森伯兰旅馆门外的一只崭新黄褐色皮靴不翼而飞",
        ],
        "choices_en": [
            {"id": "h_ch4_p1_c1", "text": "Shadow Sir Henry and Mortimer down Regent Street to flush out any watcher.", "target": "holmes_ch04_part2_cab_chase"},
            {"id": "h_ch4_p1_c2", "text": "[Switch POV to Jack Stapleton] See the stalker tracking Sir Henry with a false beard.", "target": "stapleton_ch04_part1_hotel_shadow", "pov_switch": "stapleton"},
        ],
        "choices_cn": [
            {"id": "h_ch4_p1_c1", "text": "尾随亨利爵士与摩梯末步入摄政街，引蛇出洞侦测暗中盯梢的眼线。", "target": "holmes_ch04_part2_cab_chase"},
            {"id": "h_ch4_p1_c2", "text": "【视角切换：杰克·斯台普吞】从跟踪者的视角窥视他戴着假黑胡子监视旅馆的阴谋。", "target": "stapleton_ch04_part1_hotel_shadow", "pov_switch": "stapleton"},
        ],
        "content_en": """At precisely ten o'clock, Sir Henry Baskerville was ushered into our sitting-room by Dr. Mortimer. He was a small, alert, dark-eyed man about thirty years of age, very sturdily built, with thick black eyebrows and a strong, pugnacious face. He wore a ruddy-tinted tweed suit and had the weather-beaten complexion of one who has spent most of his life in the open air.

He wasted no time in civilities. 'Mr. Holmes,' said he, tossing an envelope upon the table, 'I have received this extraordinary letter this morning at the Northumberland Hotel. Perhaps you can tell me what the devil it means!'

The envelope was of rough, cheap paper, addressed in crude, printed characters to 'Sir Henry Baskerville, Northumberland Hotel.' Inside lay a single sheet of folio paper, upon which was pasted a sentence composed of printed words cut out from a newspaper:

'As you value your life or your reason keep away from the moor.'

The word 'moor' alone was written in ink.

I took out my lens and examined the slip with intense interest. 'A charming specimen!' I murmured. 'Watson, observe the type. It is Bourgeois, leaded, exactly five points. These words were cut from yesterday's Times—specifically, the leading article on the tariff question. The scissors used were short-bladed nail-scissors, for the cuts are curved and ragged. And notice the faint, delicate odor that clings to the paper—white jessamine, the perfume of an educated woman.'

'Good heavens!' cried Mortimer. 'An educated woman?'

'And that is not all,' Sir Henry broke in, his temper flaring. 'Somebody has played a senseless prank upon me at my hotel! Last night I put out a brand-new pair of tan boots on the corridor mat to be varnished. This morning, one of the boots has vanished into thin air! The hall-porter and the boot-boy have searched every corner of the hotel in vain.'

'A new tan boot?' I asked, my brows knitting. 'A boot that had never been worn?'

'Never! I bought them only yesterday in the Strand, and had never yet had them on my feet.'

I leaned back, my pulse quickening. An enemy was shadowing Sir Henry in London with terrifying audacity. But why steal an unworn boot?""",
        "content_cn": """上午十点整，亨利·巴斯克维尔爵士在摩梯末医生的陪同下准时跨入了贝克街的房门。他身材不高却精悍结实，年约三十上下，生着一对机敏果决的黑眼睛，浓密的剑眉下一张轮廓分明、带有昂扬斗志的面庞。他身着一套红褐色的粗花呢猎装，皮肤黝黑发亮，浑身上下散发着长期在加拿大荒野风吹日晒所特有的粗犷活力。

他没有把时间浪费在繁文缛节上。‘福尔摩斯先生，’他大步走到桌前，将一封信封啪的一声掷在桌上，‘今早我在诺森伯兰旅馆收到了这封莫名其妙的信！但愿您能告诉我，这究竟见鬼的是怎么一回事！’

那是一只廉价粗糙的平价信封，上面用笨拙印刷体字样写着‘诺森伯兰旅馆，亨利·巴斯克维尔爵士收’。抽开信封，里面是一张四开大小的信纸，纸上整整齐齐地粘贴着一排从报纸上裁剪下来的印刷词句：

‘倘若你珍视你的性命与理智，切切远离那片荒原。’

唯独‘荒原’（moor）二字，是用粗糙的黑墨水手写补全的。

我立刻抽出口袋里的放大镜，将信纸贴近镜片细细检视。‘一件极其精妙的标本！’我赞叹道，‘华生，注意这些铅字字模。这是典型的五号铅字（Bourgeois），通栏加空铅排版。这些词句全部裁剪自昨天的《泰晤士报》——确切地说，是关于关税问题的主题社论！而裁剪这些字迹的工具，是一把刃口极短的女士修甲剪刀，因为边缘处留有弧形微小的咬痕。再留神一下纸张边缘隐隐散发的香气——这是素馨花（white jessamine）的清香，一位受过良好教育的女性留下的印记！’

‘上帝啊！’摩梯末失声惊呼，‘一位有教养的女人？’

‘这还不是全部呢！’亨利爵士按捺不住心头的怒火打断道，‘昨晚在旅馆里，还有某个该死的贼骨头跟我开了一个荒谬绝伦的恶劣玩笑！我昨晚把刚买的一双崭新黄褐色皮靴放在房门外的地垫上等着擦油，结果今天早晨一瞧，其中一只竟然不翼而飞了！旅馆的领班和擦鞋童把整栋楼翻了个底朝天，那只靴子就像蒸发了一样！’

‘一双新买的黄褐色皮靴？’我眼神一敛，追问道，‘一双此前从未上过脚的新靴子？’

‘从没穿过！我昨天刚在河岸街（Strand）买回来的，鞋底连一点灰尘都没沾过！’

我靠回椅背，大脑深处飞速运转。一个隐蔽的仇敌正以骇人的胆量在伦敦市区紧咬着亨利爵士不放。然而，凶手盗取一只完全没有穿过的新靴子，究竟意欲何为？"""
    },

    # Chapter 4 Part 2
    {
        "id": "holmes_ch04_part2_cab_chase",
        "ch_idx": 3, "part": 2,
        "title_en": "Chapter 4: Sir Henry Baskerville (Part II: The Shadow in Regent Street)",
        "title_cn": "第四章 亨利·巴斯克维尔爵士（下：摄政街的幽灵与马车2704）",
        "pov": "holmes", "type": "branch", "anchor": None,
        "clues_en": [
            "Hansom cab No. 2704 was shadowing Sir Henry down Regent Street",
            "Spy inside cab had piercing black eyes and a full, bushy black beard",
            "The tan boot reappeared at the hotel, but an old, worn black boot was stolen in its place",
        ],
        "clues_cn": [
            "车号为2704号的双轮小马车在摄政街对亨利爵士展开贴身尾随",
            "车内密探生有一双鹰隼般的黑眼睛与满脸浓密浓黑的假连鬓大胡子",
            "那只新黄皮靴竟被悄悄送回旅馆，但亨利爵士的一只旧黑皮靴却紧接着被盗走",
        ],
        "choices_en": [
            {"id": "h_ch4_p2_c1", "text": "Dispatch Cartwright to 23 hotels and summon cabman No. 2704 to Baker Street.", "target": "holmes_ch05_threads"},
            {"id": "h_ch4_p2_c2", "text": "Confront the Northumberland Hotel manager regarding the boot substitutions.", "target": "holmes_ch05_threads"},
        ],
        "choices_cn": [
            {"id": "h_ch4_p2_c1", "text": "派遣小厮卡特赖特搜查二十三家旅馆垃圾纸篓，并传唤2704号马车夫前来说明。", "target": "holmes_ch05_threads"},
            {"id": "h_ch4_p2_c2", "text": "就皮靴调包失窃案对诺森伯兰旅馆大堂经理与侍者展开现场高压质询。", "target": "holmes_ch05_threads"},
        ],
        "content_en": """The moment Sir Henry and Mortimer left Baker Street to walk toward their hotel, I sprang to my feet.

'Quick, Watson! Your hat and boots! Not a second to lose!'

We slipped down into the street and shadowed them at two hundred yards. They turned into Oxford Street and down Regent Street. Ahead of them, keeping pace on the opposite side of the road, crawled a hansom cab. Inside the cab, dimly visible through the glass, sat a passenger leaning forward with sharp, watchful eyes.

I quickened my pace. Suddenly, the passenger's eyes met mine. He recognized me in a flash! A hand was thrust through the trap-door in the roof, the cabby whipped his horse, and in an instant the hansom went tearing down Regent Street toward Waterloo Place.

'No. 2704!' I shouted, memorizing the white numerals upon the vehicle's rear. 'A bushy black beard and piercing black eyes! He was an adversary worthy of our steel, Watson.'

We walked straight to the District Messenger Office, where I engaged my sharp young aide, Cartwright. I sent him with five sovereigns to visit all twenty-three hotels in the Charing Cross district, with instructions to examine the waste-paper baskets for the mutilated copy of yesterday's Times.

At two o'clock, we called upon Sir Henry at the Northumberland Hotel. We found the baronet purple with fury.

'Look here, Mr. Holmes!' he roared, pointing to the wardrobe. 'The madman has been at it again! That missing tan boot of mine has turned up under the wicker chair in the corner. But now—by all the devils in hell—one of my old black boots, a worn pair that I brought with me from Canada, has been stolen from outside my door!'

My heart gave a fierce leap. The pieces of the puzzle slammed together in my mind with blinding clarity.

'An old black boot!' I exclaimed. 'A boot that you had actually walked in?'

'Yes, covered with mud from yesterday's walk!'

'Ah!' I whispered to Watson. 'An unworn boot carries no scent. But a worn boot carries the unmistakable scent of living flesh!'""",
        "content_cn": """亨利爵士与摩梯末前脚刚踏出贝克街的大门，我便霍地从扶手椅上一跃而起。

‘快，华生！抓起你的帽子和大衣！一秒钟都不能耽搁！’

我们如幽灵般穿入街市，在两百码外的距离悄然尾随其后。他们二人拐入牛津街，随即顺着摄政街信步南行。而在他们前方的马路对面，一辆双轮轻便小马车（hansom cab）正以反常的慢速悄然并排行进。透过马车的车窗玻璃，隐约可以看见车厢里端坐着一个微微前倾的黑影，两只阴鸷的眼睛正死死锁定着前方的爵士。

我骤然加快了脚步。电光石火之间，车厢内的乘客突然转过脸来，目光与我正正撞在了一起！他在一瞬间认出了我！一只手猛地顶开了车顶上的通话小窗，车夫的长鞭在空中抽出刺耳的脆响，那匹拉车骏马瞬间扬蹄狂奔，小马车如离弦之箭般沿着摄政街朝滑铁卢广场方向绝尘而去！

‘2704号！’我厉声高呼，死死记住了车尾那排白色的编号，‘满脸漆黑浓密的连鬓大胡子，目光锐利如刀！华生，我们当真遇上了一位值得交锋的强悍劲敌！’

我带着华生径直奔向地区信差所，雇佣了我手下最机灵的小厮卡特赖特。我塞给他五枚金镑，命他逐一搜查查令十字街附近的全部二十三家大旅馆，务必将清洁工收集的垃圾纸篓翻个底朝天，搜寻那份被剪掉社论字句的昨日《泰晤士报》。

下午两点，我们如约来到诺森伯兰旅馆拜会亨利爵士。一进房门，只见这位年轻的男爵气得满脸通红，正在起居室内暴跳如雷。

‘福尔摩斯先生，您快瞧瞧这叫什么事！’他指着墙角的衣柜怒吼道，‘那个疯子又对我下手了！我那只丢了的新黄皮靴，竟然莫名其妙地出现在了墙角藤椅底下！可现在——见他妈的大头鬼——我的一只旧黑皮靴，一双我特意从加拿大穿过来、踩满泥巴的旧靴子，又在门外被人顺手牵羊给偷了！’

我的心脏猛地剧烈狂跳了一下。脑海中散落的所有拼图碎块在一刹那间严丝合缝地拼接在了一起！

‘一只旧黑皮靴？’我脱口追问道，‘一双你确确实实长途穿过的皮靴？’

‘对啊，鞋帮上甚至还沾着昨天下雨踩的烂泥呢！’

‘啊！’我转头向华生低声耳语道，‘一只崭新的靴子根本没有任何气味。然而一双穿过的旧鞋，却吸附着活人血肉特有的鲜明气味！’"""
    }
])
# Holmes Chapter 5 & 6
HOLMES_NODES.extend([
    # Chapter 5
    {
        "id": "holmes_ch05_threads",
        "ch_idx": 4, "part": 0,
        "title_en": "Chapter 5: Three Broken Threads (The Insolent Cabman & The Secret Expedition)",
        "title_cn": "第五章 三条断了的线索（傲慢的马车夫与秘密出征）",
        "pov": "holmes", "type": "anchor", "anchor": "anchor_arrival_holmes",
        "clues_en": [
            "Cartwright finds no mutilated Times in 23 hotel wastebaskets",
            "Telegram confirms Barrymore is at Baskerville Hall",
            "Cabman John Clayton states passenger brazenly declared: 'My name is Sherlock Holmes'",
        ],
        "clues_cn": [
            "卡特赖特翻遍二十三家旅馆垃圾篓未见被裁剪的《泰晤士报》残页",
            "发往庄园的测试电报确认管家白利墨当时身在达特穆尔庄园内",
            "2704号车夫约翰·克莱顿证实那名黑胡子乘客傲慢挑衅地自称：‘我的名字叫歇洛克·福尔摩斯’",
        ],
        "choices_en": [
            {"id": "h_ch5_c1", "text": "Dispatch Watson to Devon with Sir Henry while secretly preparing your own covert moor deployment.", "target": "holmes_ch06_part1_secret_departure"},
            {"id": "h_ch5_c2", "text": "[Switch POV to Jack Stapleton] View the villain retreating to Dartmoor with the stolen black boot.", "target": "stapleton_ch05_black_boot", "pov_switch": "stapleton"},
        ],
        "choices_cn": [
            {"id": "h_ch5_c1", "text": "命华生作为公开护卫陪同亨利爵士奔赴德文郡，自己暗中筹备秘密潜入达特穆尔荒原。", "target": "holmes_ch06_part1_secret_departure"},
            {"id": "h_ch5_c2", "text": "【视角切换：杰克·斯台普吞】目睹恶谋得逞的恶魔怀揣染有气味的旧靴潜回达特穆尔。", "target": "stapleton_ch05_black_boot", "pov_switch": "stapleton"},
        ],
        "content_en": """By evening, the three threads of our London inquiry had snapped like rotten twine.

First, Cartwright returned, dust-stained and exhausted, to report that in all twenty-three hotels, not a scrap of cut newspaper could be found. The cunning author of the warning letter had burned the mutilated Times or cast it down a sewer grating.

Second, the test telegram I had wired to the butler, Barrymore, at Baskerville Hall had been delivered into his own hands by the postmaster's boy, proving that the man with the black beard in London was unlikely to be the butler away from his post.

And third, cabman John Clayton, driver of hansom No. 2704, arrived at Baker Street in response to our police enquiry. He was a hearty, honest fellow who told his story without hesitation.

'The gentleman hailed me in Trafalgar Square,' Clayton said. 'He was a gent with a thick black beard and dark glasses, dressed like a toff. He bade me follow that brown-clad Canadian gentleman all morning down Regent Street and Waterloo Place. And when you came running after us, sir, he told me to drive like the devil to Waterloo station.'

'And what did he say his name was when he paid you?' I asked.

Clayton grinned. 'Well, sir, you'll hardly believe it, but when he gave me two sovereigns at the station, he looked me in the eye and said: 'My name is Sherlock Holmes, and don't you forget it!''

I laughed aloud, though an icy thrill of combative fury surged through my veins. The rascal had brazenly flung my own name back into my face!

'A master stroke, Watson!' said I, pacing the hearth-rug. 'He knows my methods, he anticipated my inquiry, and he has slipped through our fingers with Sir Henry's old boot in his pocket. Sir Henry departs for Devonshire tomorrow. You must accompany him, Watson. You must be his shield, his eyes, and his constant companion. Report every fact to me without speculation.'

Watson accepted the perilous commission with characteristic fidelity. But as the door closed behind him, my plan was already formed. I could not remain in London while my friend walked into the wolf's mouth. I would follow him to Dartmoor in secret, establish a hidden command upon the open moor, and strike the monster from the darkness.""",
        "content_cn": """到了傍晚时分，我们在伦敦查探的三条线索，竟如同腐朽的细麻绳般悉数崩断。

第一条线索：卡特赖特满身灰尘、精疲力竭地返回贝克街。他翻遍了全部二十三家旅馆的废纸篓，却连半片被裁剪的《泰晤士报》残页也没找到。那个狡猾的写信人显然早已将剩下的废报纸付之一炬，或是随手扔进了阴沟。

第二条线索：我发往巴斯克维尔庄园给管家白利墨的核实电报，已被当地邮差童亲手递交到了白利墨手中，这表明摄政街上那个满脸黑胡子的密探，绝不可能是擅离职守远赴伦敦的管家。

而第三条线索，更是彻底将案情推向了白热化。2704号双轮马车的车夫约翰·克莱顿在警方的传唤下应声来到了贝克街。这是一个老实憨厚的朴素汉子，毫无保留地吐露了实情。

‘那位先生是在特拉法尔加广场叫上我的车，’克莱顿擦着脑门上的汗水道，‘他留着一大把乌黑浓密的连鬓大胡子，戴着一副黑墨镜，衣着考究体面。他吩咐我远远咬住那位穿着褐色粗花呢大衣的加拿大绅士，一路上从摄政街跟到了滑铁卢广场。后来当您二位拔腿追过来时，他把头伸进小窗大喊，让我拼了老命把车赶向滑铁卢车站！’

‘当他在车站付钱下车时，可曾留下姓名？’我冷冷问道。

克莱顿咧嘴苦笑了一声。‘先生，说出来您大概都不敢信。当他把两枚沉甸甸的金镑拍在我手心里时，他狠狠瞪着我，傲慢地甩下一句话：“记住了，车夫，我的名字叫歇洛克·福尔摩斯！”’

我忍不住仰天大笑起来，但一股刺骨的战意与怒火却瞬间传遍了我的每一根神经！这个胆大包天的恶徒，竟然当面将我的名字当成了玩弄警方的嘲弄盾牌！

‘好一记漂亮的反击，华生！’我按捺着内心的波澜，在壁炉前大步踱步，‘他谙熟我的办案路数，甚至预判了我的调查节奏，如今他怀里揣着亨利爵士带有体味的旧皮靴，从我们的指缝中彻底溜回了老巢！亨利爵士明天一早便要启程前往德文郡。华生，你必须作为他的私人护卫一同前行！你必须成为他的坚固盾牌、他的耳目与形影不离的同伴，将达特穆尔发生的一切细节毫无保留地据实向我汇报！’

华生以其一贯的崇高忠诚毫不犹豫地接下了这桩九死一生的重托。然而，当起居室的大门在他身后缓缓合上时，我脑海中的整盘大棋却已成竹在胸。我绝不可能安坐于伦敦的壁炉旁，眼睁睁看着我挚爱的挚友只身步入恶狼的血盆大口！我将乔装潜伏，暗度陈仓秘密潜入达特穆尔荒原，在苍凉的花岗岩石屋中构筑隐秘的前线指挥所，在最致命的危局时刻给黑暗中的凶手以雷霆万钧的致命一击！"""
    },

    # Chapter 6 Part 1
    {
        "id": "holmes_ch06_part1_secret_departure",
        "ch_idx": 5, "part": 1,
        "title_en": "Chapter 6: Baskerville Hall (Part I: The Covert Deployment to Dartmoor)",
        "title_cn": "第六章 巴斯克维尔庄园（上：暗度陈仓南下达特穆尔）",
        "pov": "holmes", "type": "anchor", "anchor": "anchor_arrival_moor_holmes",
        "clues_en": [
            "Holmes travels secretly to Devon under cover of night avoiding rail terminals",
            "Cartwright stationed at Coombe Tracey as secret logistic courier",
            "Neolithic stone hut upon Black Tor secured as covert operations base",
        ],
        "clues_cn": [
            "福尔摩斯避开干线火车站，于深夜乔装潜行秘密南下德文郡",
            "安排小厮卡特赖特驻扎库姆马西负责采买干粮、烟草与转递华生信件",
            "选定黑色岩岗上一座干燥隐蔽的史前新石器时代圆形石屋作为绝密基地",
        ],
        "choices_en": [
            {"id": "h_ch6_p1_c1", "text": "Occupy the Black Tor stone hut and sweep the moor with your field glasses.", "target": "holmes_ch06_part2_hut_surveillance"},
            {"id": "h_ch6_p1_c2", "text": "[Switch POV to Dr. Watson] View Watson's arrival at the grim gates of Baskerville Hall.", "target": "ch06_part1_arrival", "pov_switch": "watson"},
        ],
        "choices_cn": [
            {"id": "h_ch6_p1_c1", "text": "进驻黑色岩岗史前石屋，架起军用远望镜俯瞰监视整片达特穆尔荒原。", "target": "holmes_ch06_part2_hut_surveillance"},
            {"id": "h_ch6_p1_c2", "text": "【视角切换：约翰·H·华生】从华生的视角经历他与亨利爵士抵达阴森庄园大门的一刻。", "target": "ch06_part1_arrival", "pov_switch": "watson"},
        ],
        "content_en": """The deception was complete. To Watson, to Sir Henry, and to the watchful eyes that shadowed 221B Baker Street, Sherlock Holmes was safely detained in London, immersed in the tangled blackmail cases of the Duke of Devonshire.

Under cover of darkness, disguised as an elderly, eccentric botanist with a worn knapsack and a tin specimen box, I boarded an unadvertised milk-train westward. I avoided Exeter and Newton Abbot, stepping down at a lonely wayside halt miles north of the moor.

My preparations had been executed with military precision. I had summoned young Cartwright down from London and billeted him in the quiet market town of Coombe Tracey, six miles east of the Hall. His duty was perilous but simple: he was to act as my secret quartermaster. Twice a week, he would purchase bread, cold meat, clean water, and my essential shag tobacco, slip into the moor along the sheep-tracks, and deposit the supplies within my chosen retreat. Most crucially, he was instructed to collect Watson's letters from the local post office and convey them to me without Watson's knowledge.

My lair was already chosen. High upon the jagged ridge of Black Tor, commanding an unhindered panorama of Baskerville Hall, the treacherous expanse of Grimpen Mire, and the stone track to Merripit House, lay a cluster of prehistoric circular stone huts, abandoned by the ancient Britons three thousand years ago.

One of these huts had preserved its conical slate roof and dry granite walls intact. I cleared the floor, lined it with dry, springy heather, laid out my waterproof ulster, and established the covert headquarters of the defense. Through the narrow door, the granite peaks rose like dark sentinels against the swirling gray mist.""",
        "content_cn": """瞒天过海的伪装堪称天衣无缝。在华生、亨利爵士以及那双在贝克街门外暗中窥伺的鹰犬眼中，歇洛克·福尔摩斯先生正被德文郡公爵那桩扑朔迷离的敲诈勒索案死死拖在伦敦，分身乏术。

然而在深夜浓黑的掩护下，我换上了一身落魄古怪的年迈植物学者的行头，肩挎磨破的帆布帆布包，手提一只绿漆斑驳的标本铁盒，登上一列无人注意的运奶货运列车秘密西行。我巧妙地避开了埃克塞特与牛顿阿博特等繁华换乘大站，在荒原以北数英里外一个荒凉冷清的乡村小站悄然滑入夜色。

整套行动方案按照军用特战标准精密展开。我早已密令小厮卡特赖特从伦敦启程，隐匿在距离庄园六英里外平静古朴的库姆马西集镇（Coombe Tracey）。他的使命危险而关键：充当我的绝密后勤官。每周两次，他将负责采买面包、冷肉、洁净水以及我赖以提神的黑烟丝，沿着隐蔽的羊肠小径翻山越岭，将补给神不知鬼不觉地送入我的秘密藏身点。更为关键的是，他将全权负责从镇邮局截取华生寄往伦敦的密报，第一时间送达我手中，而华生对此将毫不知情！

而我的作战前哨更是经过了千挑万选。在黑色岩岗（Black Tor）犬牙差互的悬崖绝壁顶端，有一片三千年前古代不列颠土著遗留下的新石器时代圆形史前石屋群。这里的视野辽阔无匹，居高临下足以俯瞰巴斯克维尔庄园的森严高墙、大格林盆泥潭那片致命的惨绿泥沼，以及通往梅利琵宅邸的必经小道！

其中一座圆形石屋历经三千年风霜，其圆锥形的厚重石板屋顶与花岗岩石壁依然坚固完整，滴水不漏。我清扫了地面碎石，铺上厚厚一层干燥柔软的野生石楠花，垫上我那件厚重的防水大氅，一座隐蔽的战略反击前哨便告落成。透过狭窄昏暗的石门望去，荒原上一座座花岗岩峰峦犹如远古巨人般在狂风与苍茫的灰雾中冷冷肃立。"""
    },

    # Chapter 6 Part 2
    {
        "id": "holmes_ch06_part2_hut_surveillance",
        "ch_idx": 5, "part": 2,
        "title_en": "Chapter 6: Baskerville Hall (Part II: The Telescope on Black Tor)",
        "title_cn": "第六章 巴斯克维尔庄园（下：黑色岩岗石屋的隐秘哨位）",
        "pov": "holmes", "type": "branch", "anchor": None,
        "clues_en": [
            "Mounted guards patrol moor searching for escaped Notting Hill murderer Selden",
            "Through field glasses, Holmes observes Watson and Sir Henry entering the gloomy Hall",
        ],
        "clues_cn": [
            "荷枪实弹的骑兵正在荒原各处关卡荷枪戒备，搜捕诺丁山屠夫逃犯塞尔登",
            "透过高倍军用远望镜，福尔摩斯亲眼目睹华生与亨利爵士跨入阴森肃杀的庄园大门",
        ],
        "choices_en": [
            {"id": "h_ch6_p2_c1", "text": "Turn your telescope toward the treacherous paths of Grimpen Mire and Merripit House.", "target": "holmes_ch07_part1_naturalist"},
            {"id": "h_ch6_p2_c2", "text": "[Switch POV to Jack Stapleton] View the villain watching the arrivals from Merripit House.", "target": "stapleton_ch06_part1_arrival_watch", "pov_switch": "stapleton"},
        ],
        "choices_cn": [
            {"id": "h_ch6_p2_c1", "text": "调整远望镜焦距，将侦查视线延伸至大格林盆泥潭深处与梅利琵宅邸。", "target": "holmes_ch07_part1_naturalist"},
            {"id": "h_ch6_p2_c2", "text": "【视角切换：杰克·斯台普吞】从梅利琵宅邸窗口俯视猎物入瓮的阴冷狞笑。", "target": "stapleton_ch06_part1_arrival_watch", "pov_switch": "stapleton"},
        ],
        "content_en": """Late in the afternoon of October 15th, the deep silence of the moor was broken by the clatter of hoofs. I crouched behind a cleft in the granite rampart, bringing my powerful naval field-glass to bear upon the white ribbon of road that wound from Bovey Tracey.

The sight was dramatic. A wagonette drawn by two steaming bays rolled briskly across the heath. Upon the box sat Sir Henry Baskerville and Dr. Watson, wrapped in heavy ulsters, flanked by armed county constables. A few miles back, at the junction of the moor road, two mounted soldiers with carbines rested upon their thighs stood motionless against the sky.

The explanation had already reached me: Selden, the ferocious Notting Hill murderer, had broken from Dartmoor Prison at Princetown three days ago and was lurking somewhere in the vast granite labyrinth. A dangerous complication! A starving convict roaming the crags would inject an element of chaotic violence into a situation already poised upon a razor's edge.

I swung my glass toward Baskerville Hall. The ancient mansion emerged from its dense cordon of dying trees like a sinister phantom. The twin crenellated towers, black against the dull autumn sky, looked grim and forbidding. As the carriage passed beneath the ruined arch of the gateway, the great iron gates clanged shut. Watson and Sir Henry had entered the web.

A mile to the east, across the shimmering, deceptive green of Grimpen Mire, another chimney was smoking. Merripit House! There, within that lonely cottage, sat the brain that had devised the terror. I adjusted the focus, settling down for a long, cold, merciless vigil.""",
        "content_cn": """十月十五日的暮色时分，荒原死一般的寂静被一阵急促杂乱的马蹄声骤然撕碎。我屈身潜伏在黑色岩岗犬牙交错的花岗岩裂隙之后，将那架高倍双筒海军军用远望镜稳稳架在巨石之间，镜头牢牢锁定了从波维特雷西方向蜿蜒而来的雪白碎石驿道。

视野中的景象分外引人瞩目。一辆由两匹健马拉乘的双排轻便敞篷马车在荒原上疾驰。车厢之中，端坐着身裹厚重呢大氅的亨利·巴斯克维尔爵士与我的挚友华生医生，身旁还紧紧跟随着两名荷枪实弹的郡警。而在数英里外的道路交叉口，两名跨骑骏马、大腿上横挎卡宾枪的骑兵如铁铸般在苍凉的晚霞中巍然屹立。

情报早已传到了我的石屋：三天前，臭名昭著的诺丁山残忍杀人犯塞尔登（Selden）凿穿了普林斯敦的达特穆尔重犯监狱，正潜藏在方圆数十里的花岗岩乱石迷宫之中！这无疑是一桩极度危险的不可控变量！一个在荒原上濒临绝境、茹毛饮血的狂暴逃犯，随时可能将这盘原本就命悬一线的智力棋局搅入血腥的混乱。

我缓缓转动镜筒，将视线投向了巴斯克维尔庄园。那座古老森严的庞大宅邸在枯死林木的环抱中宛如一座从地狱深处钻出的幽灵城堡。两座高耸的城垛式雉堞塔楼在阴霾的天空下显得分外森冷阴郁。随着马车辚辚驶入坍塌的拱门，那两扇沉重锈蚀的生铁大门伴随着刺耳的巨响重重合拢。华生与亨利爵士，已然正式跨入了恶魔布下的捕兽夹！

而在东方一英里外，横跨大格林盆泥潭那片泛着诡异磷光的惨绿泥淖边缘，另一栋孤零零的烟囱正冒出缕缕青烟。梅利琵宅邸（Merripit House）！在那座看似清幽僻静的乡村农舍之中，便盘踞着操纵整场死亡恐慌的幕后大脑。我微调镜头焦距，平静地呼出一口白气，准备迎接一场漫长、冰冷而绝不容情的铁血坚守。"""
    }
])
# Holmes Chapter 7 & 8
HOLMES_NODES.extend([
    # Chapter 7 Part 1
    {
        "id": "holmes_ch07_part1_naturalist",
        "ch_idx": 6, "part": 1,
        "title_en": "Chapter 7: The Stapletons of Merripit House (Part I: The Man with the Net)",
        "title_cn": "第七章 梅利琵宅邸的主人斯台普吞（上：捕蝶网背后的窥探）",
        "pov": "holmes", "type": "anchor", "anchor": "anchor_naturalist_holmes",
        "clues_en": [
            "Stapleton demonstrates unnatural familiarity traversing lethal Grimpen Mire",
            "A wild Dartmoor pony swallowed alive in the mire proves the bog's absolute lethality",
        ],
        "clues_cn": [
            "斯台普吞在凶险万状的大格林盆泥潭中健步如飞，展现出令人惊骇的泥沼暗径掌控力",
            "一匹野生达特穆尔矮种小马在泥潭中惨叫下陷、活活灭顶，证明了泥沼吞噬万物的致命绝境",
        ],
        "choices_en": [
            {"id": "h_ch7_p1_c1", "text": "Track Watson's meeting with Beryl Stapleton through your high-powered lens.", "target": "holmes_ch07_part2_beryl_warning"},
            {"id": "h_ch7_p1_c2", "text": "[Switch POV to Jack Stapleton] View Stapleton playing the eccentric naturalist with his butterfly net.", "target": "stapleton_ch07_part1_naturalist_act", "pov_switch": "stapleton"},
        ],
        "choices_cn": [
            {"id": "h_ch7_p1_c1", "text": "紧密转动远望镜，监视华生与从草丛中疾步冲出的斯台普吞‘胞妹’贝丽尔的接触。", "target": "holmes_ch07_part2_beryl_warning"},
            {"id": "h_ch7_p1_c2", "text": "【视角切换：杰克·斯台普吞】以斯台普吞视角体验他手挥捕蝶网在沼泽边伪装学者的狡诈嘴脸。", "target": "stapleton_ch07_part1_naturalist_act", "pov_switch": "stapleton"},
        ],
        "content_en": """The morning sun of October 16th burned through the drifting mist, revealing the full treachery of the Great Grimpen Mire. Through my lens, the vast morass looked like an immense, undulating emerald carpet, broken here and there by dark pits of bubbling slime and jagged islets of granite.

Presently, a small figure appeared upon the mire track, moving with extraordinary agility. It was a slender, dapper man of middle height, with straw-coloured hair and a sharp, clean-shaven face. He carried a green butterfly net in one hand and a botanist's tin box slung across his shoulder.

Jack Stapleton!

I studied his movements with intense scientific admiration. Where any ordinary man would have plunged into the bottomless bog within three paces, this fellow sprang lightly from tussock to tussock, following an invisible zigzag trail known only to himself. Suddenly, he halted, raised his net, and sprinted with wild leaps across the quagmire in pursuit of an elusive cyclopides butterfly.

A few hundred yards away, Dr. Watson was walking down the moor path from the Hall. Stapleton spotted him, turned, and hastened to meet him with open arms and the easy, bubbling geniality of a harmless savant.

As they stood conversing by the edge of the mire, a terrifying scream rent the air. A tragic spectacle unfolded: a wild moorland pony, venturing too close to the false green crust, had broken through into the mire! Through my glass, I watched the wretched creature's frantic thrashing. Its neck stretched in agony, its wild eyes rolled, and within two minutes, the sucking black mud closed over its nostrils. Not a ripple remained.

Stapleton pointed toward the spot, smiling pleasantly at Watson as though demonstrating a textbook specimen in a lecture hall. A cold, cruel demon, wearing the mask of an eccentric scholar!""",
        "content_cn": """十月十六日清晨的惨白日光撕开了荒原弥漫的浓雾，大格林盆泥潭令人毛骨悚然的险恶全貌终于清晰地呈现在我的镜片之下。这片浩瀚万顷的巨大死沼，远看犹如一张铺展在天地间的鲜绿翡翠绒毯，然而在那片生机勃勃的草皮之下，却密布着一口口咕嘟翻滚着毒气恶臭的吞人泥浆深渊与零星凸起的花岗岩残礁。

不多时，泥潭小径上出现了一个敏捷小巧的身影。那是一个中等身材、体态利落轻盈的男子，生着一头淡黄色头发，下巴刮得干干净净，面容清秀而线条冷硬。他手里挥舞着一面绿色的长柄捕蝶网，肩上斜跨着一只植物标本铁盒。

杰克·斯台普吞！

我以冷峻严密的眼光凝视着他的一举一动，心中对其在泥沼中的身手不免升起一丝近乎赞叹的警惕。若换作任何常人，只要踏错三步，便会瞬间被这万丈泥渊吞噬得尸骨无存；然而这个家伙却如同一只轻灵的山羊，在零星点缀在泥沼间的草墩石块上轻巧跳跃，精准地踩踏着一条唯有他自己掌握的隐秘暗径。突然间，他高高举起捕蝶网，狂奔跳跃着穿过一片看似必死的沼泽，疯狂扑捕着一只珍稀的环纹蝶（cyclopides）。

而在数百码外，华生正迈着军人特有的稳健步伐沿着从庄园通来的小径漫步。斯台普吞很快察觉到了华生的到来，他猛地转身迎上前去，脸上洋溢着一位纯良无害的乡村学者那种热情爽朗、滔滔不绝的温和笑容。

然而正当他们二人在泥潭边缘攀谈之际，一声刺耳凄厉的惨嘶骤然划破长空。一幕惨烈至极的自然悲剧在镜筒中上演：一匹在荒原上觅食的野生矮种马因贪食嫩草，一脚踏破了伪装成草坪的致命泥壳！透过高倍远望镜，我清晰地看到了那匹可怜牲畜垂死挣扎的惨状——它的脖颈绝望地向上伸长，马眼因恐惧而剧烈凸出翻白，短短两分钟内，那贪婪粘稠的黑浆便彻底漫过了它的鼻孔。水泡咕嘟翻滚，泥潭表面随即重新恢复了令人窒息的死寂平整。

斯台普吞微笑着抬手指着马匹灭顶之处，神色自若地向惊骇万状的华生指点解说，神态从容得宛如一位在大学讲堂里为学生演示显微镜切片的博学教授。好一个戴着学者面具、骨子里却冷血残虐至极的恶魔！"""
    },

    # Chapter 7 Part 2
    {
        "id": "holmes_ch07_part2_beryl_warning",
        "ch_idx": 6, "part": 2,
        "title_en": "Chapter 7: The Stapletons of Merripit House (Part II: The Desperate Warning)",
        "title_cn": "第七章 梅利琵宅邸的主人斯台普吞（下：泥潭小径上的慌乱警告）",
        "pov": "holmes", "type": "branch", "anchor": None,
        "clues_en": [
            "Beryl Stapleton frantically warns Watson mistaking him for Sir Henry",
            "Deep domestic terror and unnatural tension observed between the supposed siblings",
        ],
        "clues_cn": [
            "贝丽尔·斯台普吞误将华生认作亨利爵士，在荒原小径上极度恐慌地发出绝命撤离警告",
            "福尔摩斯敏锐捕获这对所谓‘兄妹’之间弥漫的家庭暴力威慑与反常心理控制",
        ],
        "choices_en": [
            {"id": "h_ch7_p2_c1", "text": "Prepare to receive and decode Watson's first written dispatch from the Hall.", "target": "holmes_ch08_watson_report"},
            {"id": "h_ch7_p2_c2", "text": "Direct your spy glass to intercept Cartwright's rendezvous point at the crags.", "target": "holmes_ch08_watson_report"},
        ],
        "choices_cn": [
            {"id": "h_ch7_p2_c1", "text": "返回石屋做好准备，接收并破译华生从庄园寄往伦敦的第一份长篇战报。", "target": "holmes_ch08_watson_report"},
            {"id": "h_ch7_p2_c2", "text": "将视线转向岩岗隐蔽隘口，锁定小厮卡特赖特送粮投递邮件的秘密交接点。", "target": "holmes_ch08_watson_report"},
        ],
        "content_en": """Stapleton suddenly darted off across the heather in pursuit of another moth, leaving Watson alone upon the track. At that exact moment, a tall, striking woman stepped from the bushes into Watson's path.

Beryl Stapleton!

She was of a beauty as rare as it was un-English: dark-eyed, olive-skinned, with a proud, exquisite profile and a figure of extraordinary grace. But her face was pale as marble, and her dark eyes were dilated with acute, desperate terror.

Through my field glass, I could read the pantomime of their encounter with utter clarity. She had evidently mistaken Watson for Sir Henry Baskerville! She seized Watson by the arm, speaking with frantic, breathless rapidity. Her hands gestured passionately toward the southern road, imploring him—commanding him—to pack his trunks and return instantly to London before night fell!

Watson, taken aback by this sudden apparition, tried to calm her. When he revealed his true identity as Dr. Watson, the woman's reaction was singular: a look of mingled relief and doubled terror flashed across her features.

At that moment, Stapleton reappeared over the crest of the hill, his net swinging by his side. The transformation in the woman was instantaneous: she stiffened, her face froze into an emotionless mask, and she stepped back as though she had been struck across the mouth.

Stapleton greeted his sister with a smile that failed to reach his small, cold eyes. A master of dissimulation! Yet beneath that polished domestic exterior, I sensed the brutal tension of a tyrant and his prisoner. This woman was no willing accomplice—she was an unwilling captive held under the lash of fear!

I lowered the glass, my mind racing. The pieces were shifting. In London, the warning letter had been composed by an educated hand and scented with white jessamine. Here on the moor, this exotic 'sister' risked her life to warn the baronet. The battle lines were drawn.""",
        "content_cn": """斯台普吞忽然为了追扑另一只飞蛾再次钻入了远处的石楠丛，留下华生一人孤零零地伫立在荒原小径旁。恰在此刻，一个身材高挑、容貌绝美的年轻女子蓦地从灌木丛后疾步冲出，径直拦住了华生的去路！

贝丽尔·斯台普吞！

那是一种在英格兰本土极其罕见、带有浓郁南美异域风情的惊人美貌：橄榄色的细腻肌肤，轮廓分明而高贵冷艳的五官，以及一双黑亮如夜却满溢着极度恐慌的深眸。此刻她面色惨白如纸，胸脯因剧烈的喘息而剧烈起伏。

借由这架强大的军用远望镜，我几乎能够毫不费力地读懂她与华生交谈时的每一个肢体动作。她显然将华生误认成了刚刚抵英的亨利·巴斯克维尔爵士！只见她一把死死抓住了华生的衣袖，嘴唇飞速开合，神情急迫凄厉得令人窒息。她拼命打着手势指向南方通往外界的大道，苦苦哀求——乃至近乎发疯般命令对方立刻收拾行囊，务必在今晚夜幕降临之前滚回伦敦去，永远不要再踏足这片受诅咒的土地半步！

华生显然被这位突如其来的异国佳人吓了一跳，连忙试图安抚她的狂躁。而当华生表明自己并非亨利爵士、而是约翰·H·华生医生时，那女人的反应更是耐人寻味：一丝劫后余生般的庆幸一闪而过，紧接着涌上的却是更为深重的绝望与惶恐！

就在此时，斯台普吞的身影已然越过了山脊，捕蝶网在他腿边漫不经心地摇晃。那女子在察觉到动静的刹那间发生的变化，堪称戏剧性——她浑身骤然僵硬得如同一具石雕，脸上那副撕心裂肺的急迫在一秒钟内被冰冷麻木的机械笑容所取代，整个人甚至本能地向后瑟缩倒退了一步，仿佛脸上刚刚挨了一记无形的皮鞭！

斯台普吞微笑着迎向自己的‘胞妹’，然而那抹笑容却始终无法渗透进他那双毒蛇般森冷阴鸷的小眼睛里。好一个巧舌如簧的伪装大师！然而在这对看似和谐体面的乡居‘兄妹’表象之下，我敏锐地嗅出了一种暴君与其掌中囚徒之间令人作呕的恐怖高压。这位美丽的女子绝非心甘情愿的共谋者——她是一个在暴力威胁下忍辱负重、试图暗中打破枷锁的惊弓之鸟！

我缓缓放下了远望镜，大脑深处的思绪如电光石火般飞速流转。所有的线索正在迅速交织闭合。在伦敦，那封剪报警告信出自受过高等教养的女性之手，并隐隐散发着素馨花的幽香；而在这片危机四伏的荒原之上，这位神秘的‘妹妹’竟然冒着性命之危试图搭救爵士的性命。决战的战线，已然彻底划定！"""
    },

    # Chapter 8
    {
        "id": "holmes_ch08_watson_report",
        "ch_idx": 7, "part": 0,
        "title_en": "Chapter 8: First Report of Dr. Watson (Dispatches Deciphered in the Hut)",
        "title_cn": "第八章 华生医生的第一份报告（石屋中拆阅的前线密报）",
        "pov": "holmes", "type": "branch", "anchor": None,
        "clues_en": [
            "Watson reports Barrymore's midnight prowling with a candle in the west tower",
            "Mrs. Barrymore's weeping eyes confirm hidden domestic grief",
            "Sir Henry falling deeply in love with Beryl Stapleton",
        ],
        "clues_cn": [
            "华生密报管家白利墨深夜手持蜡烛在庄园西塔空屋鬼祟徘徊探照荒原",
            "白利墨太太红肿的泪眼证实这对仆人夫妇深藏不可告人的隐秘悲痛",
            "亨利爵士不可救药地坠入爱河，对贝丽尔·斯台普吞展开热烈追求",
        ],
        "choices_en": [
            {"id": "h_ch8_c1", "text": "Focus your telescope on the west tower of Baskerville Hall for the midnight candle signal.", "target": "holmes_ch09_part1_midnight_watch"},
            {"id": "h_ch8_c2", "text": "[Switch POV to Dr. Watson] Read Watson's original diary dispatch sent from Baskerville Hall.", "target": "ch08_watson_report", "pov_switch": "watson"},
        ],
        "choices_cn": [
            {"id": "h_ch8_c1", "text": "入夜后将远望镜死死锁定庄园西塔窗口，静候管家白利墨的午夜烛火暗号。", "target": "holmes_ch09_part1_midnight_watch"},
            {"id": "h_ch8_c2", "text": "【视角切换：约翰·H·华生】阅读华生在庄园书房奋笔疾书寄出的第一份原汁原味战报。", "target": "ch08_watson_report", "pov_switch": "watson"},
        ],
        "content_en": """On the evening of October 18th, Cartwright scrambled into the stone hut, his breath coming in hoarse gasps. From his greasy canvas satchel, he drew a packet of cold roast beef, two loaves of bread, a pouch of my beloved Latakia shag, and a thick, sealed envelope addressed to Baker Street in Watson's neat, upright handwriting.

I struck a match, lit my tallow candle, and unfolded my friend's first report.

Watson had done magnificent work. With the painstaking precision of an army surgeon, he had documented the life of the Hall. He described the oppressive gloom of the great oak-panelled corridors, the ancestral portraits, and the nervous agitation of the staff.

Three crucial points leaped from his pages:

First, Barrymore the butler had been caught creeping down the west corridor at two in the morning, holding a candle to a window that commanded the moor, waiting in rigid concentration as though signaling someone in the dark.

Second, Mrs. Barrymore had been observed in tears, her eyes swollen and red. What secret bond tied the respectable butler to the perils of the moor? My mind flew to Selden, the escaped convict. A woman's tears, a butler's midnight vigils—could the convict be a relative, shielded by family blood?

And third, Sir Henry had met Beryl Stapleton and had fallen violently in love with her at first sight. Stapleton, far from encouraging a match that would elevate his sister to a ladyship, had intervened with furious, hysterical jealousy, forbidding Sir Henry from addressing her!

I blew a long stream of smoke against the stone roof. Why should a penniless naturalist fly into a rage when a wealthy baronet courts his sister?

There was only one rational answer in the whole lexicon of crime: because she was not his sister at all! She was his wife! A wife employed as a decoy, yet protected by the jealous fury of a possessive tyrant! The master deduction fell into place. I rolled myself in my ulster, my revolver loaded beneath my head, ready for the midnight watch.""",
        "content_cn": """十月十八日的深夜，小厮卡特赖特气喘吁吁地爬进了黑色岩岗石屋。他从油腻的粗帆布书包里掏出一包凉烤牛肉、两块粗面包、一整包我视若性命的黑色拉塔基亚散烟丝，以及一封厚实沉重、封漆完好的大信封——上面的收件人写着贝克街，笔迹正是华生那工整挺拔的军人字迹！

我擦亮一根火柴，点燃了牛油蜡烛，小心翼翼地展开了挚友的第一份亲笔长篇密报。

华生的表现堪称卓越绝伦。他以陆军军医特有的严密细致，毫无遗漏地记录了庄园内的一切动静。他生动地描摹了橡木护墙长廊那令人窒息的阴森、历代祖先肖像画的冷酷凝视，以及仆从们神经质的惊恐。

而在密密麻麻的墨水字迹中，有三条至关重要的核心情报如闪电般跃入我的眼帘：

第一，管家白利墨在凌晨两点钟蹑手蹑脚地潜入西侧长廊，手持蜡烛死死贴在一扇俯瞰荒原的窗户前，神情极度紧绷地凝视着黑暗，仿佛在向荒原深处的某个神秘人传递烛火暗号！

第二，白利墨太太在白天多次被人目睹掩面痛哭，双眼红肿。究竟是什么不可告人的罪孽将这位体面的老管家与危险的荒原死死拴在一起？我的思绪瞬间联想到了潜逃的诺丁山杀人犯塞尔登！一个女人的眼泪，一个管家的午夜放哨——难道那个嗜血的逃犯，竟是白利墨太太血脉相连的至亲？

第三，亨利爵士与贝丽尔·斯台普吞正式相识，并在一瞬间陷入了无法自拔的热恋！然而斯台普吞非但没有为妹妹能够嫁入豪门成为爵士夫人而狂喜，反而如疯狗般当场爆发出了歇斯底里的病态嫉妒与狂怒，当面厉声喝止亨利爵士，严禁其向贝丽尔吐露半句爱意！

我向着粗糙的石屋顶吐出一口浓郁的青烟。世间哪有一个穷困潦倒的乡居博物学者，会在一位家财万贯的年轻男爵向其‘未婚胞妹’求婚时气急败坏、暴跳如雷？

在全部犯罪心理学的法典之中，合乎理性的解释唯有一条：那个女人根本就不是他的妹妹！她是他的合法妻子！一个被恶魔当作致命诱饵、却又被其极度病态的占有欲死死锁在掌中的可怜囚徒！

这道至高无上的逻辑演绎终于水落石出！我将自己紧紧裹在大氅之中，将装满子弹的左轮手枪枕在头下，阖上双目，静候今晚午夜钟声的敲响。"""
    }
])
# Holmes Chapter 9 & 10
HOLMES_NODES.extend([
    # Chapter 9 Part 1
    {
        "id": "holmes_ch09_part1_midnight_watch",
        "ch_idx": 8, "part": 1,
        "title_en": "Chapter 9: The Light upon the Moor (Part I: The Candle and the Signal)",
        "title_cn": "第九章 沼地上的烛光（上：黑夜西窗的灯火暗号）",
        "pov": "holmes", "type": "anchor", "anchor": "anchor_convict_holmes",
        "clues_en": [
            "A yellow candle flares in the west window of Baskerville Hall at 2 AM",
            "A tiny answering flame flickers upon the granite crags of Black Tor",
            "Selden is hiding among prehistoric huts, receiving food from the Barrymores",
        ],
        "clues_cn": [
            "凌晨两点整庄园西塔昏暗的窗棂上亮起了一道惨黄的烛火暗号",
            "黑色岩岗对面的花岗岩绝壁缝隙中，随即闪烁起微弱的烛光回应",
            "证实诺丁山逃犯塞尔登正潜伏在史前石洞中，靠白利墨夫妇暗中供给衣食残喘",
        ],
        "choices_en": [
            {"id": "h_ch9_p1_c1", "text": "Step onto the moonlit summit of Black Tor to observe Watson and Henry hunting the convict.", "target": "holmes_ch09_part2_figure_on_the_tor"},
            {"id": "h_ch9_p1_c2", "text": "[Switch POV to Dr. Watson] Experience the midnight chase across the granite crags.", "target": "ch09_part2_moor_chase", "pov_switch": "watson"},
        ],
        "choices_cn": [
            {"id": "h_ch9_p1_c1", "text": "登上月色笼罩下的黑色岩岗之巅，俯瞰华生与亨利爵士夜巡荒原围捕逃犯。", "target": "holmes_ch09_part2_figure_on_the_tor"},
            {"id": "h_ch9_p1_c2", "text": "【视角切换：约翰·H·华生】与亨利爵士并肩在乱石横行的月光荒原上展开惊险狂奔。", "target": "ch09_part2_moor_chase", "pov_switch": "watson"},
        ],
        "content_en": """At two in the morning of October 20th, the moor lay submerged beneath an ocean of silver moonlight. The air was crisp with frost. I stood upon the granite ledge outside my hut, the night-glass pressed to my eye.

Precisely as Watson had reported, a yellow pinprick of flame flared in the high, narrow window of the Hall's western tower. For five minutes it shone steadily. Then it waved twice to and fro.

I swept my glass across the silent crags. A mile away, perched high upon an isolated pinnacle of rock, an answering spark appeared! A tiny, trembling spark of light, glowing like a glow-worm among the ancient boulders.

The secret was laid bare: the Barrymores were feeding the escaped convict Selden! Mrs. Barrymore was his sister; the family ties had proved stronger than the fear of the gallows.

Suddenly, two dark figures broke from the shadows of the Hall and sprinted across the heather toward the beacon. Watson and Sir Henry! They had laid an ambush for the butler, forced his confession, and were now galloping across the moonlit granite to capture the murderer themselves!

Bravo, Watson! The loyal fellow was risking neck and limb upon the treacherous rocks. Through my glass, I watched the wild drama unfold: the convict, a shaggy, ape-like creature in prison rags, spotted them, hurled a boulder down the ravine, and went bounding across the moor like a mountain goat, Watson's revolver cracking behind him.

The pursuit drew near the base of my very ridge. It was time to show them that a guardian angel walked the moor.""",
        "content_cn": """十月二十日凌晨两点，整片达特穆尔荒原沉浸在一片冷冽凄清的银白月海之中。空气中凝结着刺骨的秋霜。我伫立在石屋外的花岗岩突岩上，夜视远望镜稳稳贴紧眼眶。

分毫不差，正如华生所奏报的那样，巴斯克维尔庄园西侧塔楼那一扇狭窄幽暗的高窗上，骤然亮起了一粒黄豆般大小的惨黄色烛火！那簇火苗足足静止燃烧了五分钟之久，随即在窗口有力地来回挥动了两次！

我迅速转动镜筒，在荒凉死寂的花岗岩峭壁间来回搜寻。果不其然，在相距一英里外、一座突兀孤立的花岗岩峰峦裂隙之中，一记微弱的暗号闪烁着应声亮起！那是一簇极其微小的摇曳火光，在荒古的巨石间犹如一只荧光惨淡的萤火虫。

一切谜底终于彻底揭晓：白利墨夫妇正在暗中接济潜逃的杀人犯塞尔登！白利墨太太正是这个恶贯满盈屠夫的亲生姐姐；手足之情最终战胜了对绞刑架的恐惧！

突然间，两个矫健的身影猛地从庄园围墙的阴影中疾冲而出，踏着碎石与石楠花朝着荒原上的那簇微光全速飞奔！华生与亨利爵士！他们显然早已在长廊中设下埋伏抓获了管家，逼其吐露实情后，竟不顾生死亲自拔枪冲入月光荒原，誓要将这名嗜血狂徒当场擒获！

干得漂亮，华生！这位忠勇的退伍军官正为了保护爵士，在险象环生的巨石阵中出生入死。借着惨白的月光，我亲眼目睹了一场扣人心弦的荒原夜猎：那个满头杂草、身形宛如猿猴般褴褛凶残的逃犯察觉到了追兵，他恶狠狠地掀翻一块巨石砸入峡谷，随即如羚羊般在花岗岩裂缝间疯狂跳跃遁逃，华生的左轮手枪在他身后爆发出清脆震耳的枪声与火光！

而那个逃犯逃窜的方向，恰好直逼我所在的这片悬崖底部。该是让我的挚友明白，在这片危机四伏的荒原之上，并非唯有恶魔在游荡，还有一位冷眼监视全局的守护神！"""
    },

    # Chapter 9 Part 2
    {
        "id": "holmes_ch09_part2_figure_on_the_tor",
        "ch_idx": 8, "part": 2,
        "title_en": "Chapter 9: The Light upon the Moor (Part II: The Figure upon the Tor)",
        "title_cn": "第九章 沼地上的烛光（下：月色岩岗上的静默黑影）",
        "pov": "holmes", "type": "branch", "anchor": None,
        "clues_en": [
            "Watson catches sight of the tall, thin silhouette on the summit of Black Tor",
            "A blood-chilling hound howl rolls across the moor, freezing Watson and Henry in terror",
        ],
        "clues_cn": [
            "华生在荒原追捕尽头抬头仰望，瞥见了傲立在黑色岩岗之巅的瘦高孤峭剪影",
            "一阵令人毛骨悚然、仿佛来自地狱深渊的恶犬凄厉长嚎在夜空炸响，令华生与爵士当场惊骇僵立",
        ],
        "choices_en": [
            {"id": "h_ch9_p2_c1", "text": "Slip back into the stone hut and await Watson's diary dispatch regarding Laura Lyons.", "target": "holmes_ch10_diary_and_laura"},
            {"id": "h_ch9_p2_c2", "text": "[Switch POV to Jack Stapleton] View Stapleton stirring the hound in the mire at midnight.", "target": "stapleton_ch09_part1_feeding_the_hound", "pov_switch": "stapleton"},
        ],
        "choices_cn": [
            {"id": "h_ch9_p2_c1", "text": "隐身退回史前石屋内部，静候卡特赖特转交华生关于劳拉·里昂斯信件的绝密日记。", "target": "holmes_ch10_diary_and_laura"},
            {"id": "h_ch9_p2_c2", "text": "【视角切换：杰克·斯台普吞】目睹恶魔在午夜潜入大格林盆泥潭深处饲喂恶兽的阴森狂喜。", "target": "stapleton_ch09_part1_feeding_the_hound", "pov_switch": "stapleton"},
        ],
        "content_en": """I climbed to the very apex of Black Tor, stepping out upon the highest granite boulder where the full silver moon threw my shadow across the plateau. I stood motionless, my arms folded across my chest, looking down into the valley.

Below, panting upon the heather, Watson and Sir Henry had halted their fruitless pursuit. Suddenly, Watson raised his eyes. Through the crystal night air, his gaze locked upon me!

I saw him start violently and grip Sir Henry's shoulder, pointing his revolver up toward my silhouette. He saw a tall, thin man, motionless as a statue of bronze, standing high above the world upon the crest of the tor.

At that supreme moment of drama, an appalling sound shattered the silence of Dartmoor.

A low, deep-toned moan rolled across the heath. It swelled into a wild, mournful bay, a hideous crescendo of savage fury that made the granite boulders seem to vibrate. It was the bay of a gigantic hound! The cry of blood, rising from the black depths of Grimpen Mire!

I saw Watson and Sir Henry freeze in their tracks, their faces turned upward, drained of every drop of blood. Sir Henry stumbled against a rock, crossing himself in superstitious dread. Even Watson, seasoned soldier of Maiwand, lowered his pistol with a trembling hand.

The beast was alive. Stapleton was preparing for the kill!

Before Watson could rally his spirits and scramble up the rocks toward me, I slipped backward into the shadow of the cleft, melted into the darkness of the prehistoric huts, and vanished without a footprint.""",
        "content_cn": """我敏捷地攀上黑色岩岗最顶端的兀岩巨石，在皎洁圆月的万丈清辉之下，将自己挺拔孤峭的剪影清晰地投射在整片荒原的高空之中。我双臂环抱于胸前，犹如一尊冷硬的青铜雕像，静静俯瞰着山谷中的一切。

在下方数百英尺外的石楠丛中，气喘吁吁的华生与亨利爵士终于停下了无功而返的追击脚步。电光石火之间，华生本能地抬起了头颅。透过清澈透明的寒夜空气，他的目光与山巅上的我正正撞在了一起！

我看到华生浑身剧烈一震，一把死死抓住了身旁亨利爵士的肩膀，右手中的左轮手枪下意识地对准了岩岗顶端我的身影！在他眼中，一个身材瘦高、双臂交叉、沉静如石的神秘黑影，正孤独傲立于达特穆尔之巅，宛如荒原黑夜的的主宰者！

然而就在这极具戏剧性的对峙瞬间，一声撕心裂肺、足以冻结骨髓的恐怖嚎叫骤然在大地深处炸响！

那是一阵从地底深处泛起的低沉闷吼，转瞬间化为凄厉、绝望而狂暴的凄凉长嗥！那声音带着嗜血残虐的滔天凶焰，在整片寂静的花岗岩荒原上空疯狂回荡回响，震得脚下的巨石都隐隐颤抖！那是巨大恶犬的嚎叫！那是从大格林盆泥潭最幽深恶臭的泥浆底下喷吐而出的恶魔之音！

我清晰地看见华生与亨利爵士整个人被定格在了碎石丛中，他们的面孔瞬间褪尽了最后一丝血色！亨利爵士甚至踉跄着撞在岩壁上，在极度的祖传恐惧中颤抖着按住胸口；即便是身经百战的迈万德老兵华生，握着手枪的右手亦因骇然战栗而无力垂下！

那只恶兽确实存在！斯台普吞正在泥潭深处磨砺獠牙，准备发动最后的致命一击！

正当华生重整心神、准备端枪顺着石壁向岩岗顶端攀爬搜索之际，我脚下一滑，敏捷地缩入了巨石的浓厚阴影之中，悄然隐没在史前石屋的迷宫暗处，未曾留下半点可寻之迹。"""
    },

    # Chapter 10
    {
        "id": "holmes_ch10_diary_and_laura",
        "ch_idx": 9, "part": 0,
        "title_en": "Chapter 10: Extract from the Diary of Dr. Watson (The Secret of L.L.)",
        "title_cn": "第十章 华生医生日记摘录（L.L.的烧毁信件与达特穆尔之网）",
        "pov": "holmes", "type": "branch", "anchor": None,
        "clues_en": [
            "Barrymore confesses Sir Charles went to the gate to meet a woman signing 'L.L.'",
            "L.L. identified as Laura Lyons, daughter of Frankland, residing in Coombe Tracey",
            "The burnt fragment pleaded: 'If you are a gentleman, burn this letter and be at the gate at ten'",
        ],
        "clues_cn": [
            "管家白利墨吐露查尔斯爵士猝死当晚前往侧门，系赴一位署名‘L.L.’的神秘女性之约",
            "通过排查锁定‘L.L.’正是诉讼狂弗兰克兰老头与之断绝关系的贫困女儿劳拉·里昂斯",
            "壁炉残灰碎屑拼出绝命信尾：‘倘若您是位绅士，请将此信烧毁，并于今晚十点在侧门相候’",
        ],
        "choices_en": [
            {"id": "h_ch10_c1", "text": "Descend to Coombe Tracey in disguise to interrogate Mrs. Laura Lyons directly.", "target": "holmes_ch11_part1_lyons"},
            {"id": "h_ch10_c2", "text": "Instruct Cartwright to shadow Laura Lyons and obtain her financial records.", "target": "holmes_ch11_part1_lyons"},
        ],
        "choices_cn": [
            {"id": "h_ch10_c1", "text": "微服潜下黑色岩岗奔赴库姆马西，直接对劳拉·里昂斯夫人展开高压质询。", "target": "holmes_ch11_part1_lyons"},
            {"id": "h_ch10_c2", "text": "密令卡特赖特紧盯劳拉·里昂斯的打字行，调取其全部私人财务账目与借贷记录。", "target": "holmes_ch11_part1_lyons"},
        ],
        "content_en": """Watson's second dispatch arrived via Cartwright on the morning of October 23rd. It contained the missing link that connected the London conspiracies with the death of Sir Charles Baskerville.

Barrymore, in gratitude to Sir Henry for not prosecuting his convict brother-in-law, had made a clean breast of a secret that had tortured his conscience for months.

On the morning of Sir Charles's death, the old baronet had received a letter from the postman, postmarked Coombe Tracey. Later that night, while cleaning the study fireplace, Mrs. Barrymore had found the charred ashes of this letter. All was consumed save the very postscript at the bottom of the page, written in a delicate feminine hand:

'Please, please, as you are a gentleman, burn this letter, and be at the gate by ten o'clock.'

The initials below the plea were 'L.L.'!

I leaped to my feet, my heart pounding against my ribs. 'L.L.'!

Who in this isolated district bore those initials? My mental catalogue of Dartmoor residents revolved in a flash. Laura Lyons! The beautiful, unfortunate daughter of old Frankland of Cranmer Hall! She had made an imprudent marriage with a runaway artist named Lyons, who had abandoned her in penury. Disowned by her litigious father, she had established a modest typewriting business in Coombe Tracey, supported by the quiet charity of Sir Charles Baskerville—and of Jack Stapleton!

The fatal mechanism stood naked before my eyes. Sir Charles was a recluse who refused to leave his grounds after dark. How could he be lured to the lonely wicker gate at ten o'clock at night?

Only by an urgent appeal to his chivalry! A desperate woman pleading for a secret interview to save her honor or secure her freedom! And behind that appeal, whispering the words into her ear, dictating the very letter—stood Jack Stapleton!

I strapped my revolver beneath my coat. It was time to pay a morning call upon Mrs. Laura Lyons.""",
        "content_cn": """十月二十三日清晨，卡特赖特准时送来了华生的第二份绝密战报。这份墨迹未干的亲笔手稿中，终于补齐了将伦敦的一系列阴谋与查尔斯爵士之死彻底焊死在一起的最后环扣！

管家白利墨为了感激亨利爵士宽宏大量没有追究其接济杀人犯内弟的重罪，终于良心发现，向爵士与华生吐露了一个折磨了他数月之久的惊天隐秘！

在查尔斯爵士暴毙的当天早晨，老爵士曾收到一封来自库姆马西集镇的私人来信。当晚案发之后，白利墨太太在清理书房壁炉时，在一堆灰烬中发现了那封被烧得残缺不全的信件残片。整封信的大部分内容已化为焦炭，唯独纸张最底端用娟秀女性笔迹写就的一行附言侥幸留存：

‘求求您，求求您，倘若您当真是一位绅士，读罢请务必将此信烧毁，并于今晚十点整在侧门相见！’

而在这行绝命哀求之下的署名缩写，赫然正是‘L.L.’！

我霍地从石屋里的石楠花堆上一跃而起，胸腔中的心脏剧烈撞击着肋骨！‘L.L.’！

在这方圆二十英里的荒蛮教区之中，究竟何人拥有这组字母的姓名缩写？我脑海中关于达特穆尔常住居民的档案库以光速飞旋——劳拉·里昂斯（Laura Lyons）！克兰默庄园那个诉讼成癖的弗兰克兰老头与之断绝父女关系的苦命女儿！她当年盲目冲动地嫁给了一位名叫里昂斯的落魄画家，最终惨遭抛弃沦落赤贫。由于暴怒的父亲拒绝施以援手，这位容貌出众的女人只能在库姆马西开办了一家打字行勉强度日，全靠查尔斯爵士以及——杰克·斯台普吞的私下救济！

整个致命杀局的物理齿轮在我眼前展露无遗！查尔斯爵士生前极度迷信魔咒，天黑之后绝不肯踏出庄园半步。究竟何等力量才能诱骗这位年迈体弱的老绅士在夜间十点孤身一人驻足在通往地狱的木栅侧门旁？

唯有一记以救苦救难之名、直击其骑士精神与善心的致命诱饵！一个走投无路的绝望女人，为了挽救自己的名誉或争取离婚自由而发出的午夜密会哀求！而在这封哀求信的背后，那个伏在她耳边吐着毒液、一字一句指点她写下这封索命符的真正操盘手——唯有杰克·斯台普吞！

我迅速将左轮手枪贴身系牢在大衣内侧。是时候亲赴库姆马西，会一会这位劳拉·里昂斯夫人了！"""
    }
])
# Holmes Chapter 11 & 12
HOLMES_NODES.extend([
    # Chapter 11 Part 1
    {
        "id": "holmes_ch11_part1_lyons",
        "ch_idx": 10, "part": 1,
        "title_en": "Chapter 11: The Man on the Tor (Part I: The Inquest of Laura Lyons)",
        "title_cn": "第十一章 岩岗上的人（上：库姆马西的锋芒质询）",
        "pov": "holmes", "type": "anchor", "anchor": "anchor_tor_holmes",
        "clues_en": [
            "Laura Lyons admits writing the appointment letter to Sir Charles at 10 PM",
            "Stapleton promised to marry her once her divorce was financed",
            "Stapleton forbade her to keep the appointment, leaving Sir Charles alone at the gate",
        ],
        "clues_cn": [
            "劳拉·里昂斯在严厉逼问下招认确实写信约见查尔斯爵士于夜间十点在侧门碰头",
            "斯台普吞以许诺与其结婚为诱饵，诱骗其诱出爵士为其筹措高额离婚诉讼费",
            "斯台普吞在当晚强令劳拉取消约会绝不许现身，让老爵士在寒夜侧门孤立无援静候死神",
        ],
        "choices_en": [
            {"id": "h_ch11_p1_c1", "text": "Hasten back to the prehistoric stone hut upon Black Tor before nightfall.", "target": "holmes_ch11_part2_stone_hut"},
            {"id": "h_ch11_p1_c2", "text": "[Switch POV to Dr. Watson] View Watson infiltrating the stone hut with revolver drawn.", "target": "ch11_part2_stone_hut", "pov_switch": "watson"},
        ],
        "choices_cn": [
            {"id": "h_ch11_p1_c1", "text": "在夜幕彻底吞没荒原前全速赶回黑色岩岗石屋，准备与华生迎来戏剧性会师。", "target": "holmes_ch11_part2_stone_hut"},
            {"id": "h_ch11_p1_c2", "text": "【视角切换：约翰·H·华生】端详华生在黄昏中端枪逼近石屋、誓要缉拿‘岩岗怪客’的英姿。", "target": "ch11_part2_stone_hut", "pov_switch": "watson"},
        ],
        "content_en": """I found Mrs. Laura Lyons at her modest apartment in Coombe Tracey. She was an extraordinarily handsome woman, with rich hazel hair and hazel eyes, but her mouth had that hardened, bitter downturn which comes from prolonged social humiliation and desperate poverty.

At first, she met my inquiries with haughty evasion, denying that she had ever corresponded with Sir Charles on the day of his death.

'Mrs. Lyons,' said I, leaning forward and fixing her with my keenest gaze, 'the matter is far too grave for falsehood. We are investigating a murder. The letter you sent was burned, but the postscript in your hand was rescued from the grate: 'Please, please, as you are a gentleman, burn this letter, and be at the gate by ten o'clock.' If you refuse to speak, you stand in the shadow of the gallows as an accessory to murder!'

The blood fled from her cheeks, leaving her white as chalk. She covered her face with her hands, trembling violently.

'I did not know!' she sobbed. 'As God is my judge, I swore it was for my salvation! Mr. Stapleton told me that if I could obtain two thousand pounds to secure my legal divorce, he would make me his lawful wife! He dictated the letter. He told me that Sir Charles was proud and sensitive, and that an interview in the garden was the only way to touch his heart!'

'And why did you not keep the appointment?'

'Because Mr. Stapleton came to me that very afternoon!' she cried. 'He told me that his own pride could not endure that another man should pay for my freedom. He swore that he would provide every guinea himself, and commanded me—on my love for him—never to go near Baskerville Hall that night! And next morning, I read that Sir Charles was dead!'

The devilish scheme was complete in every detail. Stapleton had used this unhappy woman to draw Sir Charles to the gate, kept her away, and brought his glowing hell-hound to the appointment!

Leaving her weeping in remorse, I struck out across the heath at a rapid pace. The shadows were lengthening, and I knew that Watson was searching for the tenant of the hut.""",
        "content_cn": """我在库姆马西集镇一处清贫简朴的公寓里见到了劳拉·里昂斯夫人。她无疑是一位具有非凡美貌的绝色女子，拥有如绸缎般浓密的栗色秀发与明澈的眼眸，然而她的唇角却带着一种因长期遭受社会冷眼欺凌与贫困折磨而特有的坚硬苦涩。

起初，面对我的试探，她极力保持着傲慢与戒备，断然否认自己在老爵士暴毙当天曾与之通邮。

‘里昂斯夫人，’我身躯微微前倾，以最冷峻锐利的目光死死锁定她的双眸，‘人命关天，此案已绝非任何妇人之仁的虚与委蛇所能掩盖。我们正在调查一桩蓄谋已久的谋杀案！你写给爵士的亲笔信固然被投入了炉膛，然而留在灰烬中的附言却已铁证如山：“求求您，倘若您当真是一位绅士，读罢请将此信烧毁，并于今晚十点在侧门相见！”倘若你此刻依然拒绝吐露实情，那么等待你的将是作为谋杀从犯同赴绞刑架的万劫不复！’

刹那间，她面上的血色褪得一干二净，惨白得如同一尊大理石雕。她用颤抖的双手死死捂住面孔，浑身如风中落叶般剧烈战栗起来。

‘我真的不知道……我发誓我什么都不知道！’她掩面失声痛哭，‘以上帝的名义起誓，我当年以为那是拯救我脱离苦海的唯一生路！是斯台普吞先生告诉我，只要能筹集到两千英镑办理合法的离婚手续，他便会明媒正娶我为合法的妻子！整封信是他一字一句口述逼我写下的！他说查尔斯爵士生性矜持好面子，唯有深夜在侧门私下哀求，才能彻底打动那位老人的善心！’

‘那么你当晚为何失约未去？’

‘因为斯台普吞先生在当天下午突然闯进了我的公寓！’她凄厉地抽泣道，‘他向我发誓，说他的大男子尊严绝不能容忍由另一个男人的施舍来赎买我的自由身！他信誓旦旦地保证由他自己筹措这笔巨款，并以我们之间的爱情为由，严令我当晚绝不许踏足巴斯克维尔庄园半步！结果到了第二天早晨，报纸上便刊登出了查尔斯爵士暴毙的死讯！’

整桩魔鬼杀局在这一刻终于彻底水落石出！斯台普吞利用这个苦命女人作为将爵士诱出高墙的诱饵，随后强令其失约退场，自己则牵着那只涂满磷光的恶魔巨兽，在侧门外完成了对老爵士的心脏处决！

任凭这位悔恨交加的妇人在屋内抱头痛哭，我已裹紧风衣大步流星跨入荒原。天际残阳如血，阴影正在迅速吞噬群峰，我知道，忠诚的华生此刻必定正在搜寻石屋的主人！"""
    },

    # Chapter 11 Part 2
    {
        "id": "holmes_ch11_part2_stone_hut",
        "ch_idx": 10, "part": 2,
        "title_en": "Chapter 11: The Man on the Tor (Part II: 'A Lovely Evening, Watson!')",
        "title_cn": "第十一章 岩岗上的人（下：石屋会师与撕破画皮）",
        "pov": "holmes", "type": "branch", "anchor": None,
        "clues_en": [
            "Watson enters hut with drawn revolver; Holmes greets him casually by the fire",
            "Holmes reveals Beryl is Stapleton's lawful wife, not his sister",
            "Stapleton is an imposter possessing sinister natural malice and hereditary claims",
        ],
        "clues_cn": [
            "华生端枪摸入石屋设伏；福尔摩斯在阴影中泰然吐出经典问候：‘天气真好，我亲爱的华生！’",
            "福尔摩斯彻底撕破画皮：揭露贝丽尔实为斯台普吞的原配妻子而非胞妹",
            "斯台普吞真实身份乃是蓄谋侵吞七十四万英镑巨额遗产的巴斯克维尔旁系恶魔",
        ],
        "choices_en": [
            {"id": "h_ch11_p2_c1", "text": "Step outside upon the crags with Watson to evaluate the impending peril.", "target": "holmes_ch12_part1_revelations"},
            {"id": "h_ch11_p2_c2", "text": "Pool all intelligence regarding Laura Lyons and Stapleton's past movements.", "target": "holmes_ch12_part1_revelations"},
        ],
        "choices_cn": [
            {"id": "h_ch11_p2_c1", "text": "与华生并肩步出石屋登上悬崖峭壁，就近在咫尺的生死危局商讨决战策略。", "target": "holmes_ch12_part1_revelations"},
            {"id": "h_ch11_p2_c2", "text": "在石屋月光下全面核对关于劳拉·里昂斯笔供与斯台普吞恶谋的全部绝密拼图。", "target": "holmes_ch12_part1_revelations"},
        ],
        "content_en": """I reached the prehistoric hut just as the last crimson gleams of sunset died upon the western horizon. As I approached the low stone portal, my acute senses detected an unmistakable intruder: the pungent aroma of an Egyptian cigarette, the very brand favoured by my friend Dr. Watson!

I stepped quietly within the threshold. In the dim violet twilight, a figure sprang up from the heather, a cocked revolver gleaming in his fist.

'A lovely evening, my dear Watson!' said I, stepping into the light. 'I really think you will be more comfortable outside than sitting upon that hard granite.'

'Holmes!' he gasped, dropping his pistol upon the bed, his voice trembling with a mixture of immense relief and wounded bewilderment. 'Holmes! Good God, is it you? Can it be possible that you have been here all the time?'

'Every hour of it, my dear fellow,' I replied, lighting my pipe. 'Forgive the necessary deception. Had Sir Henry or the Stapletons known of my presence, our cunning adversary would have retreated into impenetrable caution. By utilizing your honest, open observations, I have operated with total invisibility.'

Watson grasped my hand with all his old soldierly warmth. We sat side by side upon the heather, pooling our discoveries.

'And now, Watson,' said I, 'let me supply the master key to this labyrinth. You have met Miss Stapleton. Has it ever struck you as unnatural that a devoted brother should fly into a murderous frenzy when a wealthy, honourable baronet seeks to marry his penniless sister?'

'It astonished me beyond measure,' Watson admitted.

'It astonished you because you accepted a lie! That lady is not his sister, Watson. She is his lawful wife! A Costa Rican woman whom he married in South America! He brought her here under a false name, forced her to pass as his sister so that she might serve as a decoy to lure wealthy men to their destruction, while he watches her with the savage jealousy of a beast!'

Watson's face darkened with righteous fury. 'Great God! Then Stapleton is—'

'A murderer of the most cold-blooded and calculated type this world has ever seen!'""",
        "content_cn": """当最后一抹血红色的残阳在西天尽头彻底熄灭时，我已疾步返回了黑色岩岗石屋。当我轻手轻脚接近低矮的石门入口时，我那敏锐的感官瞬间捕捉到了一股极其鲜明的陌生气息——那是一股埃及卷烟（Egyptian cigarette）特有的辛辣醇香，正是我的老伙计约翰·H·华生医生平日专用的品牌！

我悄无声息地迈入低矮的门槛。在昏暗紫郁的暮色中，一个矫健的身影猛地从石楠花铺上一跃而起，黑洞洞的左轮手枪枪口在暮色中泛着森冷的光芒！

‘天气真好，我亲爱的华生！’我从容地迎向那柄手枪，微笑着开口道，‘坦白讲，我觉得你坐在外面的草地上吹吹晚风，总比死死窝在这块硬邦邦的花岗岩上要舒服得多。’

‘福尔摩斯！’华生失声惊呼，手中的左轮手枪啪的一声落在了花堆上，嗓音中交织着死里逃生的极度欣喜与被蒙在鼓里的难以置信，‘福尔摩斯！仁慈的上帝啊，真的是你？难道这段日子以来，你竟然一直潜伏在这片荒原上？！’

‘分分秒秒都在这里，我亲爱的老伙计，’我划着火柴点燃了烟斗，‘请原谅我这番必要的善意隐瞒。倘若亨利爵士或是斯台普吞得知我亲临此地，我们那位狡猾阴毒的对手必将退缩到绝对密不透风的坚壳之中。正是借由你那份光明磊落、毫不作伪的公开行动作为掩护，我才能隐蔽在幕后完成全部致命线索的合围！’

华生狠狠握住了我的双手，展现出他老兵特有的热血温情。我们肩并肩席地坐在干燥的石楠花丛上，迅速汇总各自掌握的情报。

‘现在，华生，’我神色肃穆，吐出一口浓烟，‘让我为你递上打开整座迷宫的终极万能钥匙。你多次拜会过那位斯台普吞小姐。难道你就未曾觉得不可思议——一个穷困潦倒的兄长，在面对一位品行高洁、家财万贯的年轻男爵向其胞妹求婚时，竟然会歇斯底里地爆发出一股病态的杀人狂怒？’

‘这件事确实让我百思不得其解！’华生承认道。

‘那是因为你轻信了一句弥天大谎！那位美丽的女士根本就不是他的胞妹，华生。她是他的合法结发妻子！一个他在南美洲迎娶的哥斯达黎加女人！他带着她隐姓埋名潜逃至此，逼迫她伪装成未婚妹妹充当引诱富豪步入死地的致命诱饵，却又在骨子里如恶犬般对她施以惨无人道的严密监控与病态嫉妒！’

华生的面庞因崇高的正义之怒而涨得通红。‘全能的上帝啊！这么说来，斯台普吞竟是一个——’

‘这世间有史以来最冷血、最缜密、最丧心病狂的连环谋杀巨魔！’"""
    },

    # Chapter 12 Part 1
    {
        "id": "holmes_ch12_part1_revelations",
        "ch_idx": 11, "part": 1,
        "title_en": "Chapter 12: Death on the Moor (Part I: The Cry on the Crags)",
        "title_cn": "第十二章 沼地的惨剧（上：悬崖峭壁上的恶犬狂吠）",
        "pov": "holmes", "type": "anchor", "anchor": "anchor_death_holmes",
        "clues_en": [
            "A bloodcurdling hound baying echoes through the fog followed by screams of human agony",
            "Holmes and Watson sprint across the moonlit boulders toward the sound of death",
        ],
        "clues_cn": [
            "浓雾弥漫的花岗岩悬崖方向爆发出一阵震耳欲聋、撕心裂肺的恶犬狂吠与垂死人类惨呼",
            "福尔摩斯与华生拔出左轮手枪，在崎岖遍布的花岗岩乱石间全速飞奔施救",
        ],
        "choices_en": [
            {"id": "h_ch12_p1_c1", "text": "Sprint frantically toward the base of the sheer granite cliff to intercept the tragedy.", "target": "holmes_ch12_part2_selden_death"},
            {"id": "h_ch12_p1_c2", "text": "[Switch POV to Jack Stapleton] View Stapleton unleashing the hound upon Sir Henry's scent.", "target": "stapleton_ch12_part1_screams_on_crags", "pov_switch": "stapleton"},
        ],
        "choices_cn": [
            {"id": "h_ch12_p1_c1", "text": "顺着惨叫声拼死冲向绝壁悬崖底部，拔枪截击地狱恶犬与凶手。", "target": "holmes_ch12_part2_selden_death"},
            {"id": "h_ch12_p1_c2", "text": "【视角切换：杰克·斯台普吞】从斯台普吞视角体会他手持旧靴放出恶犬噬人的癫狂杀意。", "target": "stapleton_ch12_part1_screams_on_crags", "pov_switch": "stapleton"},
        ],
        "content_en": """We stepped out upon the narrow granite ledge outside the hut. The moon had dipped behind a bank of ragged, wind-torn clouds, and the vast expanse of Dartmoor lay buried in deep, suffocating shadow.

'Our case is almost complete, Watson,' I whispered, resting a hand upon his shoulder. 'Laura Lyons has confessed how Sir Charles was lured to the gate. We know of the stolen boots—an old boot used to train a bloodhound to Sir Henry's personal scent. But we lack the tangible physical proof to place before an English jury. We cannot arrest a man upon circumstantial deductions—'

Suddenly, out of the black vastness of the moor, there broke a sound that curdled the blood in our veins.

A hound! Deep, resonant, hollow, booming across the silence of the night!

It was no ordinary bark. It was the baying of a monster on a fresh, hot trail! And then, rising above the terrible baying, came a scream—a scream of utter, mortal agony!

'Great God!' cried Watson, his hand flying to his revolver. 'Did you hear that?'

'Sir Henry!' I gasped, a cold sweat breaking across my forehead. 'He has gone out upon the moor!'

Again the cry rose—closer now, accompanied by the frantic scrabbling of boots upon shale and the heavy, panting thud of galloping paws. A second shriek rent the air, ending in a sickening, splintering crash at the base of the crags, followed by silence—a silence more dreadful than the cries.

'This way, Watson! For God's sake, run!'

We plunged down the jagged slope, leaping from boulder to boulder in the dark, our revolvers cocked, sprinting toward the foot of the sheer granite cliff!""",
        "content_cn": """我和华生并肩踏上石屋外狭窄的花岗岩露台。惨白的月轮已被天际涌起的一层厚重乌云所遮蔽，整片浩瀚无垠的达特穆尔荒原陷入了令人窒息的漆黑深渊。

‘整桩铁案的证据链已然近乎完备，华生，’我按住他的肩膀，神色凝重地低语道，‘劳拉·里昂斯夫人已彻底招供了查尔斯爵士被诱往侧门的全部细节；我们也已洞悉了伦敦失窃旧靴的真相——凶手偷盗穿过的旧皮靴，正是为了训练这只嗜血凶兽死死锁定亨利爵士个人的血肉气味！然而，若要将这个恶魔送上英国法庭的绞刑架，我们还缺少最核心的现行实体物证！在没有抓获恶犬现行之前，纯粹的逻辑演绎还不足以彻底说服陪审团——’

突然之间，从荒原那片死寂漆黑的无底深渊之中，骤然炸响了一声令我们周身血液瞬间凝结成冰的咆哮！

恶犬！那是一种低沉、浑厚、在山谷间激荡共鸣的恐怖轰鸣！

那绝非凡间家犬的吠叫，而是一头来自九幽深渊的食人怪兽咬死热血猎物时的狂欢！而紧接着，在这阵凄厉恶犬狂吠的上空，猛地拔起了一声凄厉尖锐、撕裂云霄的垂死惨嚎！

‘万能的上帝啊！’华生惊骇失声，右手闪电般拔出了腰间的左轮手枪，‘你听到了吗？！’

‘亨利爵士！’我倒吸一口冷气，冷汗如瀑布般从前额狂涌而下，‘他今晚竟然真的擅自踏上了荒原！’

那声惨嚎再次划破夜空——距离我们更近了！其间还伴随着鞋底在碎石碎岩上疯狂打滑的摩擦声，以及一双沉重狂暴的巨爪踩踏苔原的狂暴奔袭声！紧接着，最后一声凄厉欲绝的悲鸣在空中戛然而止，取而代之的是悬崖绝壁底部一声令人毛骨悚然、骨骼碎裂的沉闷撞击巨响！随后，一切重归死寂——那是一种比任何狂嚎更为可怖的永恒死寂！

‘这边，华生！看在上帝的份上，全速冲刺！’

我们毫不犹豫地扑向险峻的花岗岩陡坡，在漆黑的乱石堆中飞身跳跃疾驰，手中的左轮手枪扳机全开，全速冲向绝壁悬崖底部！"""
    },

    # Chapter 12 Part 2
    {
        "id": "holmes_ch12_part2_selden_death",
        "ch_idx": 11, "part": 2,
        "title_en": "Chapter 12: Death on the Moor (Part II: The Fall of the Convict)",
        "title_cn": "第十二章 沼地的惨剧（下：摔碎的替死者与迎面交锋）",
        "pov": "holmes", "type": "branch", "anchor": None,
        "clues_en": [
            "Dead man is Selden the convict, dressed in Sir Henry's discarded old tweed suit",
            "The stolen boot scent caused the hound to track the scent of Sir Henry's clothes",
            "Stapleton emerges from the darkness with a lantern, feigning innocence",
        ],
        "clues_cn": [
            "惨死绝壁之下的死者并非爵士，而是身穿亨利爵士淘汰粗花呢旧衣的逃犯塞尔登",
            "盗取旧皮靴的气味锁定了旧衣服的体味，导致饥饿巨兽将逃犯误作男爵扑下悬崖摔死",
            "斯台普吞手提马灯自夜色中现身试探虚实，被福尔摩斯不动声色的从容伪装彻底迷惑",
        ],
        "choices_en": [
            {"id": "h_ch12_p2_c1", "text": "Return to Baskerville Hall to examine the ancestral portraits and set the final snare.", "target": "holmes_ch13_portrait"},
            {"id": "h_ch12_p2_c2", "text": "Confront Stapleton directly upon the rocks before he retreats to Merripit House.", "target": "holmes_ch13_portrait"},
        ],
        "choices_cn": [
            {"id": "h_ch12_p2_c1", "text": "返回巴斯克维尔庄园检视历代祖先肖像画，铺设彻底歼灭凶手的终极决战罗网。", "target": "holmes_ch13_portrait"},
            {"id": "h_ch12_p2_c2", "text": "在花岗岩乱石堆前与惊魂未定的斯台普吞针锋相对，以高超演技掩盖全部底牌。", "target": "holmes_ch13_portrait"},
        ],
        "content_en": """At the foot of a perpendicular granite crag, forty feet high, lay a dark, crumpled heap.

Watson fell upon his knees beside the body, crying out in bitter despair: 'Sir Henry! Oh, Holmes, the hound has had him!'

The body was clad in a thick, ruddy-tinted tweed suit—the identical suit worn by Sir Henry Baskerville on the morning we had met him in London! The skull was crushed against the stones, and the neck was broken.

I knelt down, struck a match, and turned the blood-stained face to the light. I cried aloud in fierce, triumphant joy!

'Watson! Look at the beard! Look at the forehead! It is not Sir Henry! It is Selden, the escaped convict!'

Watson stared in dumbfounded amazement. 'The convict? But how in heaven's name does he come to be wearing Sir Henry's clothes?'

'Barrymore's wardrobe charity!' I laughed, the terrible weight lifting from my heart. 'Sir Henry gave his cast-off London garments to the butler, and the butler passed them to his starving brother-in-law! The hound was laid on Sir Henry's scent with the stolen boot—it tracked the scent of Sir Henry's clothes across the moor, chased the wretched convict over the edge of the crag, and dashed his brains out upon the stones!'

At that moment, the yellow beam of a lantern bobbed through the darkness. A light, dapper figure stepped from behind the boulders.

Jack Stapleton!

He had come to gloat over Sir Henry's corpse! When his lantern fell upon me, he stopped dead, his face draining of all colour. For three seconds, the master villain stood frozen, caught between mortal terror and criminal cunning.

'Mr. Holmes!' he stammered, recovering himself with an effort that strained every nerve. 'Is it possible? What an unexpected honour! And... who is this unfortunate man?'

'An escaped convict, Mr. Stapleton,' I replied smoothly, puffing my pipe. 'He seems to have fallen from the crags and broken his neck. A tragic accident, nothing more. My friend Watson and I return to London tomorrow, our holiday at an end.'

Stapleton smiled, a smile of infinite relief. The fool believed his secret was safe! In forty-eight hours, the trap would spring.""",
        "content_cn": """在一座足有四十英尺高的刀削般垂直花岗岩绝壁脚下，横卧着一具扭曲折断、血肉模糊的黑影。

华生猛地扑倒在尸骸旁，发出了近乎崩溃的绝望痛呼：‘亨利爵士！天啊，福尔摩斯，恶犬到底还是得手了！’

那具尸体身上紧紧包裹着一套厚重扎实的红褐色粗花呢猎装——正是亨利·巴斯克维尔爵士在伦敦贝克街初次登门时所穿的那套一模一样的衣裳！死者的头颅在乱石上撞得粉碎，颈椎彻底折断扭曲。

我霍地跪下身躯，擦亮一根火柴，一把掰正了那张沾满腥血的死人脸孔。下一秒，我忍不住在夜色中爆发出一声昂扬狂喜的厉声高呼！

‘华生！快看他的胡须！看他的眉骨！这根本不是亨利爵士！这是潜逃的诺丁山杀人犯塞尔登！’

华生目瞪口呆地死死盯着那张狰狞丑陋的面孔。‘逃犯？可看在老天爷的份上，他身上怎么会穿着亨利爵士的贴身行头？！’

‘这是白利墨的施舍善举！’我心中的万钧重担在刹那间烟消云散，忍不住大笑出声，‘爵士将换下来的旧粗花呢大衣随手赏给了老管家，管家转手就送给了荒原上挨冻的杀人犯内弟！斯台普吞用那只偷盗的旧皮靴让恶犬牢牢吸足了爵士的体味——恶兽在夜色中闻着旧衣服的气味一路穷追不舍，硬是将这个倒霉的替死鬼生生逼下了万丈悬崖，摔了个脑浆迸裂！’

就在这千钧一发之际，一束昏黄摇曳的马灯光柱穿透浓雾，自乱石林后缓缓探出。一个身形轻巧利落的影子漫步踱入空地。

杰克·斯台普吞！

这个恶魔专程赶来欣赏亨利爵士横尸荒野的杰作！然而当他手中的马灯光柱骤然照亮我那张冷峻的面庞时，整个人如遭九天惊雷当头劈中，面孔在瞬间褪尽了血色，惨白得犹如一具活尸！足足有三秒钟之久，这位犯罪巨枭彻底僵死在了原地，在濒死的恐惧与亡命的狡诈之间剧烈挣扎！

‘福……福尔摩斯先生！’他拼尽全身力气强行克制住牙关的颤抖，结结巴巴地强挤出一丝干瘪的假笑，‘这怎么可能？当真是三生有幸的大驾光临！只是……这位不幸罹难的先生究竟是哪位？’

‘一个在荒原上越狱的逃犯，斯台普吞先生，’我悠闲地吐出一口烟圈，面无表情地拍了拍大衣上的碎石，‘看来是他失足坠崖跌断了脖子。纯属一桩令人遗憾的意外悲剧。我和华生明天一早便要搭乘早班火车返回伦敦，我们的德文郡度假之旅到此结束了。’

斯台普吞长长地松了一口气，脸上绽放出了一抹如释重负的恶毒冷笑。这个自作聪明的蠢材天真地以为自己的秘密依然固若金汤！再过四十八小时，收口的猎网便将彻底将他送上绞刑架！"""
    }
])
# Holmes Chapter 13 & 14
HOLMES_NODES.extend([
    # Chapter 13
    {
        "id": "holmes_ch13_portrait",
        "ch_idx": 12, "part": 0,
        "title_en": "Chapter 13: Fixing the Nets (The Face of Hugo & The Fatal Dinner Invitation)",
        "title_cn": "第十三章 设网（雨果画像的真面目与致命陷阱）",
        "pov": "holmes", "type": "anchor", "anchor": "anchor_portrait_holmes",
        "clues_en": [
            "Concealing Hugo Baskerville's hat and curls reveals Jack Stapleton's identical face",
            "Stapleton is proven to be the son of Rodger Baskerville, seeking the £740,000 estate",
            "Sir Henry is instructed to dine alone at Merripit House and walk home by the mire path",
        ],
        "clues_cn": [
            "遮挡雨果·巴斯克维尔画像上的宽檐阔帽与长卷假发，赫然露出与斯台普吞一模一样的脸庞",
            "确凿证实斯台普吞实为查尔斯爵士流亡南美的幼弟罗杰·巴斯克维尔之子，谋财篡位动机昭然若揭",
            "命亨利爵士依约孤身赴梅利琵宅邸赴鸿门宴，并严格按照凶手设计在夜间十点沿泥潭小径步行返家",
        ],
        "choices_en": [
            {"id": "h_ch13_c1", "text": "Meet Inspector Lestrade at the station and take position in the rocks outside Merripit House.", "target": "holmes_ch14_part1_fog_ambush"},
            {"id": "h_ch13_c2", "text": "[Switch POV to Jack Stapleton] View the villain preparing the fatal dinner at Merripit House.", "target": "stapleton_ch13_fatal_dinner", "pov_switch": "stapleton"},
        ],
        "choices_cn": [
            {"id": "h_ch13_c1", "text": "前往车站汇合苏格兰场刑警雷斯垂德，深夜埋伏在梅利琵宅邸外围的绝命巨石阵中。", "target": "holmes_ch14_part1_fog_ambush"},
            {"id": "h_ch13_c2", "text": "【视角切换：杰克·斯台普吞】窥视恶魔在梅利琵宅邸暗中研磨剧毒磷光、设宴备战的阴鸷心机。", "target": "stapleton_ch13_fatal_dinner", "pov_switch": "stapleton"},
        ],
        "content_en": """That night, in the great dining-hall of Baskerville Hall, over cold fowl and claret, I stared up at the gallery of family portraits. Watson and Sir Henry watched me in silence.

Suddenly, my eyes fastened upon a canvas dated 1647. It portrayed a cavalier with a harsh, wicked countenance, clad in black velvet and lace.

'Who is that gentleman?' I asked.

'That is the wicked Hugo himself,' said Sir Henry, 'the father of the family legend.'

I waited until Sir Henry left the room. Then, stepping upon a chair, I held a candle before the portrait and placed my flat hands across the cavalier's broad plumed hat and flowing curls, concealing the seventeenth-century costume.

Watson sprang up from the table with a loud cry of astonishment!

'Good heavens!' he shouted. 'It is the face of Jack Stapleton!'

'Precisely!' said I, stepping down. 'A case of hereditary reversion, a physical throwback of two hundred years! Jack Stapleton is a Baskerville! He is the son of Rodger Baskerville, Sir Charles's black-sheep younger brother who fled to South America! He stands next in succession after Sir Henry to the entire £740,000 estate!'

Our net was ready. The next morning, I announced our public departure for London to deceive Stapleton's spies. But at Coombe Tracey station, we slipped from the train and met Inspector Lestrade of Scotland Yard, who had arrived with a search warrant and an English bulldog's tenacity.

My final orders to Sir Henry were severe and absolute: he was to accept Stapleton's dinner invitation at Merripit House, announce that we had returned to London, and at ten o'clock, he must walk home alone across the moor along the track by the Great Grimpen Mire.

The baronet's courage did not falter. He accepted the role of bait in our trap. As darkness gathered over the bog, Watson, Lestrade, and I took up our vigil behind the granite rocks, two hundred yards from the glowing windows of Merripit House.""",
        "content_cn": """当晚，在巴斯克维尔庄园那座空旷阴森的古老橡木大宴会厅里，借着摇曳的烛光，我们用罢冷肉与波尔多红酒。我叼着烟斗，目光长久地在墙壁上那一整排历代先祖油画肖像间缓缓游移。华生与亨利爵士在一旁屏息静候。

突然间，我的目光死死钉在了一幅绘制于一六四七年的古旧肖像画上。画布上描摹着一位面相冷酷残忍的保王党骑士，身着一袭黑丝绒长袍，领口缀着华贵的蕾丝花边。

‘请问那位先生尊姓大名？’我看似漫不经心地随口一问。

‘那正是恶棍雨果·巴斯克维尔本人，’亨利爵士苦笑着摇头，‘引发了我们全家族百年生死诅咒的罪魁祸首。’

我耐心地等待亨利爵士告退回房歇息。随后，我毫不犹豫地搬起一把餐椅踏上高处，手举烛台凑近画布。我伸出两只手掌，精准地遮挡住了画中骑士那顶宽大的插羽软帽与披肩长鬈假发，完全隐去了属于十七世纪的一切时代装束。

华生猛地从餐桌旁一跃而起，在空荡荡的大厅里爆发出了一声惊骇欲绝的高呼！

‘仁慈的上帝啊！’他失声尖叫，‘那是杰克·斯台普吞的脸！’

‘分毫不差！’我跳下餐椅，眼中闪烁着洞悉一切的冰冷光芒，‘这是一起惊人的隔代遗传返祖现象（atavism），两百年前的魔鬼血脉在两百年后肉身复活！杰克·斯台普吞本质上就是一个如假包换的巴斯克维尔！他是查尔斯爵士那位劣迹斑斑、流亡南美洲客死异乡的幼弟罗杰·巴斯克维尔的亲生儿子！只要除掉亨利爵士，他便是七十四万英镑巨额信托遗产的唯一合法继承人！’

收网的时机已然彻底成熟。第二天清晨，我和华生当众演了一出乘马车返英返京的大戏，以麻痹斯台普吞布下的耳目。然而在库姆马西车站，我们悄然潜下车厢，与苏格兰场王牌刑警雷斯垂德（Inspector Lestrade）胜利会师。

而我对亨利爵士下达的最终指令冰冷严酷至极：他必须按原计划孤身前往梅利琵宅邸赴宴，宣称我和华生已然离境；而在深夜十点钟宴席散去之后，他必须孤身一人踏上夜色荒原，沿着大格林盆泥潭边缘的那条必经之路步行折返庄园！

年轻男爵的钢铁意志没有丝毫动摇，他慨然答应充当诱捕恶魔的唯一诱饵。当浓黑的夜幕再次笼罩死沼之时，我、华生与雷斯垂德三人已然荷枪实弹，屏息潜伏在距梅利琵宅邸窗口两百码外那片冰冷刺骨的花岗岩暗礁之后。"""
    },

    # Chapter 14 Part 1
    {
        "id": "holmes_ch14_part1_fog_ambush",
        "ch_idx": 13, "part": 1,
        "title_en": "Chapter 14: The Hound of the Baskervilles (Part I: The Fire-Breathing Beast)",
        "title_cn": "第十四章 巴斯克维尔的猎犬（上：大雾与喷火巨兽）",
        "pov": "holmes", "type": "anchor", "anchor": "anchor_climax_holmes",
        "clues_en": [
            "Thick white fog bank rolls from Grimpen Mire threatening to engulf the path",
            "The gigantic hound bursts through the fog, its jaws and eyes ablaze with phosphorus",
            "Holmes fires five cartridges into the leaping beast, slaying the demon inches from Sir Henry",
        ],
        "clues_cn": [
            "大格林盆泥潭涌起滔天雪白浓雾，如白色潮水般迅速向伏击巨石圈疯狂逼近",
            "一头体格如小牛般庞大的纯黑巨兽破雾而出，口鼻獠牙与双眼周遭燃烧着幽绿的磷光鬼火",
            "福尔摩斯在恶兽凌空扑咬的电光石火间连射五枪，在距离爵士咽喉数寸处将恶魔当场毙命",
        ],
        "choices_en": [
            {"id": "h_ch14_p1_c1", "text": "Storm Merripit House to rescue Beryl and pursue Stapleton into the Great Grimpen Mire.", "target": "holmes_ch14_part2_mire_pursuit"},
            {"id": "h_ch14_p1_c2", "text": "[Switch POV to Jack Stapleton] Experience the agony of defeat and the desperate flight into the mire.", "target": "stapleton_ch14_part2_panic_flight", "pov_switch": "stapleton"},
        ],
        "choices_cn": [
            {"id": "h_ch14_p1_c1", "text": "强攻破入梅利琵宅邸解救惨遭绑架的贝丽尔，紧追凶手足迹杀入大格林盆泥潭深处。", "target": "holmes_ch14_part2_mire_pursuit"},
            {"id": "h_ch14_p1_c2", "text": "【视角切换：杰克·斯台普吞】目睹恶犬被枪毙的绝望崩溃，仓皇逃入噬人死沼深渊。", "target": "stapleton_ch14_part2_panic_flight", "pov_switch": "stapleton"},
        ],
        "content_en": """The night was cold and damp, but our supreme peril came not from the adversary, but from the elements.

From the Great Grimpen Mire, a dense, moonlit fog-bank was rolling inland. It advanced like a white wall, silent, swift, and relentless, creeping across the heather and blotting out the boulder field inch by inch.

'If that fog covers the path before Sir Henry leaves the house,' I muttered through clenched teeth, 'we shall never see him alive!'

At five minutes to ten, the front door of Merripit House opened. Sir Henry stepped out into the night, wrapped in his overcoat. He paused, looked up at the clearing sky, and began to walk briskly along the stone path that skirted the morass.

He had passed our ambush by fifty yards when a sound broke from the fog.

A patter of rapid, galloping feet—heavy, relentless, vibrating the damp earth!

'Look out!' I roared, cocking my revolver. 'It's coming!'

Out of the dense white wall of vapour leaped an apparition so hideous that the blood froze in our veins.

A hound! But such a hound as never mortal eyes had beheld! A huge creature, coal-black, shaped like a cross between a bloodhound and a mastiff, but larger than either. Fire burst from its open mouth, its eyes glowed with smouldering embers, and its muzzle, hackles, and dewlap were outlined in flickering, bluish flame! Never in the delirious dream of a disordered brain could anything more savage, more appalling, more hellish be conceived!

The beast sprang across the heather with giant bounds, its smoking jaws parted, bounding straight for Sir Henry's throat! Sir Henry looked back, shrieked in horror, and fell to his knees upon the path.

I sprang from the rocks, leveled my revolver, and emptied five cartridges into the monster's flank!

The bullets took effect! With a deafening howl of anguish, the beast rolled over upon its back, clawing wildly at the air. It leaped up once more, snapping furiously, but Watson and I fired together. A bullet pierced its brain. It gave a dying shiver, collapsed into the heather, and lay still.

We had broken the curse of the Baskervilles!""",
        "content_cn": """寒夜刺骨入髓，然而在此绝命关头，最致命的强敌并非凶顽狡黠的匪徒，而是大自然无常的造化！

从大格林盆泥潭深处，一堵厚重粘稠、在月光下泛着死白光泽的浓雾之墙正疯狂向内陆滚滚推进！那迷雾如雪崩般寂静无声却迅猛狂暴，寸寸吞噬着石楠花与花岗岩巨石，正以肉眼可见的速度向唯一的返程羊肠小道疯狂蔓延！

‘倘若在爵士踏出房门之前大雾切断了小道，’我咬紧牙关，牙缝中迸出森寒的低语，‘我们便永远无法救下他的性命！’

九点五十五分，梅利琵宅邸的大门吱呀一声被推开了。亨利爵士身裹大衣迈步踏入黑夜。他停下脚步环视四周，深吸了一口寒气，随即迈开稳健急促的步子，顺着紧挨泥潭边缘的那条必经石道快步折返。

他刚从我们埋伏的巨石圈前走过五十码远，大雾深处骤然响起了一阵令人魂飞魄散的死神脚步！

那是一阵沉重、狂暴、踩得湿漉漉的泥炭大地隐隐震颤的狂暴奔蹄声！

‘注意隐蔽！’我厉声暴喝，瞬间将手中的左轮手枪扳机压到极限，‘它来了！’

下一秒，从那堵雪白如墙的翻滚浓雾之中，赫然凌空飞扑出一具即便是最狂乱的疯人梦境也绝难描摹的旷世恶魔！

一只恶犬！然而那是一只凡间肉眼从所未见的巨兽！一头体型硕大如牛犊、毛色漆黑如焦炭的狂暴恶兽，体格兼具寻血猎犬的追踪狂暴与马士提夫獒犬的骇人骨架！更令人毛骨悚然的是，两道幽绿惨淡的烈焰正从其张开的血盆大口中熊熊喷吐，一双巨眼有如燃烧的炭火般闪烁着血光，甚至连它的吻部、颈项的鬃毛与垂肉，都整整齐齐地勾勒在一层闪烁跳跃的幽蓝地狱鬼火之中！

那怪兽以惊人的长距离飞跃在石楠丛上狂暴掠过，带着扑面而来的硫磺焦臭，直取亨利爵士脆弱的咽喉！爵士闻声回头，吓得发出一声撕心裂肺的绝望惨叫，两腿一软当场瘫倒在泥泞小道上！

我猛地从乱石堆上一跃而起，双手握枪稳如磐石，对着那头狂暴巨兽的肋骨连发五枪！

子弹精准命中要害！巨兽在半空中爆发出了一声震耳欲聋、撕裂苍穹的凄厉嚎叫，沉重的躯体在空中猛烈翻滚着重重砸向地面，四只巨爪疯狂抓挠着空气！它在血泊中发狂般挣扎着再次挺起上半身，试图张开滴淌腥血与磷火的獠牙做殊死一搏，然而我和华生同时扣动了扳机！一发铅弹瞬间贯穿了它的颅骨！

那头巨兽浑身剧烈战栗抽搐了一下，庞大的身躯噗通一声瘫软在枯萎的石楠花堆之中，四肢一挺，彻底绝了生息！

巴斯克维尔家族两百年的不散阴魂，在这一刻被现代科学的铅弹彻底打得粉碎！"""
    },

    # Chapter 14 Part 2
    {
        "id": "holmes_ch14_part2_mire_pursuit",
        "ch_idx": 13, "part": 2,
        "title_en": "Chapter 14: The Hound of the Baskervilles (Part II: Sucked into Grimpen Mire)",
        "title_cn": "第十四章 巴斯克维尔的猎犬（下：魔窟搜寻与沉入泥淖）",
        "pov": "holmes", "type": "branch", "anchor": None,
        "clues_en": [
            "Beryl rescued from upstairs bedroom bound and gagged with brass bedpost marks",
            "Phosphorus preparation and Sir Henry's stolen black boot found in mire island lair",
            "Stapleton lost his footing in the dense fog and was swallowed alive by Great Grimpen Mire",
        ],
        "clues_cn": [
            "破门救出被反绑在黄铜床柱上、满身伤痕口塞手帕的贝丽尔·斯台普吞",
            "在泥潭核心孤岛的废弃锡矿工棚中查获磷光特制涂料与亨利爵士失窃的旧黑皮靴",
            "斯台普吞在浓雾慌乱中踏空暗径，被大格林盆泥潭万丈黑泥活活吞噬，尸骨无存",
        ],
        "choices_en": [
            {"id": "h_ch14_p2_c1", "text": "Return to Baker Street to reconstruct the complete retrospective deduction.", "target": "ch15_holmes"},
            {"id": "h_ch14_p2_c2", "text": "Celebrate the heroic partnership with Dr. Watson by the crackling fireside.", "target": "ch15_watson"},
            {"id": "h_ch14_p2_c3", "text": "Review the full triumph of justice and the closure of the Baskerville curse.", "target": "ch15_victory"},
            {"id": "h_ch14_p2_c4", "text": "Reflect solemnly upon the tragic cost exacted from the innocent.", "target": "ch15_tragedy"},
            {"id": "h_ch14_p2_c5", "text": "Ponder the grim justice of the mire that swallowed the cruel murderer.", "target": "ch15_mire"},
            {"id": "h_ch14_p2_c6", "text": "Envision the trial and judgment of the villain before the bar of law.", "target": "ch15_arrest"},
        ],
        "choices_cn": [
            {"id": "h_ch14_p2_c1", "text": "返抵贝克街起居室，在暖融融的壁炉旁为华生展开全案精妙绝伦的总回顾演绎。", "target": "ch15_holmes"},
            {"id": "h_ch14_p2_c2", "text": "高举酒杯向身手果决的华生医生致敬，铭记传奇搭档破灭百年魔咒的不朽篇章。", "target": "ch15_watson"},
            {"id": "h_ch14_p2_c3", "text": "见证正义昭彰与理性大获全胜，巴斯克维尔庄园重归宁静祥和的圆满凯旋。", "target": "ch15_victory"},
            {"id": "h_ch14_p2_c4", "text": "凝视着秋雨敲打的窗扉，为无辜者遭受的沉痛神经创伤与代价肃穆沉思。", "target": "ch15_tragedy"},
            {"id": "h_ch14_p2_c5", "text": "凝视壁炉余烬，感叹那吞噬恶魔的大格林盆远古死沼才是罪恶最公正的天然坟墓。", "target": "ch15_mire"},
            {"id": "h_ch14_p2_c6", "text": "翻阅各大报纸头版，审视法网恢恢老贝利法庭对潜逃罪枭作出的至高正义审判。", "target": "ch15_arrest"},
        ],
        "content_en": """We knelt beside the dead hound. I ran my fingers over its muzzle. The glowing light had ceased, but a slick, greasy paste coated its fur.

'Phosphorus!' whispered Lestrade, touching the wet skin.

'A cunning preparation,' I remarked, wiping my hands. 'Odourless, so as not to spoil the beast's scent, yet luminous in the dark. A mastiff-bloodhound cross, bred and starved for savagery.'

Leaving Lestrade to attend to the trembling Sir Henry, Watson and I battered down the door of Merripit House.

The ground floor was deserted. On the upper floor, behind a locked door, we found a scene of horror. Beryl Stapleton was bound securely to an upright of the bed with heavy curtain cords, her mouth gagged with a scarf. Her delicate wrists and white neck were discoloured by brutal, recent bruises!

Watson severed the cords. As the gag was removed, she gasped in agony:

'Is he safe? Did Sir Henry escape?'

'He is safe,' I answered gently. 'And the hound is dead.'

'Thank God!' she wept, swaying upon her feet. 'He has fled into the Great Grimpen Mire! He has an old tin-mine on an island in the very heart of the bog where he kept the hound! But he can never navigate the path in this fog!'

Guided by the desperate woman's directions, we pushed into the fringes of the morass next morning as the sun burned off the mist. We followed the tiny wands of lath that Stapleton had planted to mark the invisible trail. Halfway to the island, where the slime quivered like green jelly, a black object caught my eye, half-buried in the mud.

I reached out with my crook and dragged it onto the heather.

It was an old black boot, stamped 'Meyers, Toronto' upon the lining! The stolen boot that had sealed Sir Henry's doom—cast aside by the flying murderer in his panic!

Beyond that point, the guiding wands ceased. Upon the wide expanse of trembling mire, there was no trace of a returning footstep. A heel-mark was stamped deep into the green slime, where a man had desperately striven to regain his balance—and failed. The bubbling mud had closed over him.

Somewhere down in the foul slime of the huge morass, that cold, cruel heart was sleeping forever. The Great Grimpen Mire had claimed its master!""",
        "content_cn": """我和华生半跪在那具死透的恶犬尸骸旁。我伸出手指抚摸着它那焦糊的口鼻。虽然烈焰般的荧光已然熄灭，但其皮毛表面依然附着着一层滑腻粘稠的特制油脂。

‘磷光涂料！’雷斯垂德伸手捻了捻湿漉漉的皮毛，忍不住倒吸一口凉气。

‘极其精妙的无机化学配方，’我用手帕擦拭着指尖，冷静地评述道，‘无色无嗅，因而完全不会干扰猎犬敏锐的嗅觉追踪；然而一旦置于暗处，却能泛出骇人的地狱磷火。这是一只兼具马士提夫獒犬体魄与寻血猎犬野性的杂交品种，长期被囚禁在饥饿与暴虐之中以激发嗜血兽性。’

命雷斯垂德在小道上好生照料瘫软战栗的亨利爵士，我和华生拔腿冲向梅利琵宅邸，飞脚踹开了紧闭的厚重大门。

一楼死一般寂静，空无一人。当我们顺着狭窄的楼梯冲向二楼并破开反锁的客房木门时，一幕惨绝人寰的暴行赫然呈现在眼前！贝丽尔·斯台普吞被沉重的窗帘粗绳死死绑在冰冷的黄铜床柱之上，一条厚厚的丝巾勒紧了她的嘴唇。在她雪白幼嫩的手腕与修长的脖颈上，赫然布满了令人触目惊心的乌青掐痕与皮鞭抽打的血印！

华生闪电般割断了绳索。当取下口中的丝巾时，这位饱受折磨的绝美贵妇用尽最后一丝力气凄厉地哀求道：

‘他……他还活着吗？！亨利爵士他死里逃生了吗？！’

‘他安然无恙，’我温和地扶住她摇摇欲坠的身躯，‘而且那只恶犬已被我们当场击毙！’

‘谢天谢地！感谢上帝！’她泪如雨下，浑身剧烈颤抖，‘斯台普吞已经逃进了大格林盆泥潭深处！他在沼泽最核心的孤岛上一座废弃锡矿工棚里筑造了魔窟，平日正是将猎犬隐匿在彼处！然而今晚的大雾如此遮天蔽日，他绝对不可能看清脚下的暗径！’

次日清晨，当惨白的艳阳终于驱散了漫天浓雾时，依照这位重获自由夫人的指引，我和华生踏入了这片死神盘踞的绿色绝境。我们小心翼翼地踩着斯台普吞生前沿途插下用来标记暗径的折断树枝向前摸索。在行进至前往孤岛正中、整片泥浆如绿色果冻般剧烈颤抖翻滚的绝命死地时，一件半陷在黑泥中的黑色异物猛地刺入了我的眼帘。

我探出手杖的长柄弯钩，小心翼翼地将那件物品挑上了结实的草墩。

一只破旧的黑色皮靴，鞋舌内侧清清楚楚地印着多伦多‘迈尔斯鞋行’（Meyers, Toronto）的烫金铭文！正是那只从伦敦诺森伯兰旅馆盗走、险些置爵士于死地的关键证物——恶魔在昨夜惊慌绝命狂奔时随手抛弃的累赘！

而越过这只皮靴，前方标记暗径的折枝彻底断绝了。在浩瀚平整、散发着剧毒硫磺气味的茫茫黑泥表面，再也找不到任何折返的脚印。唯有一道深深滑向万丈深渊的绝望脚跟滑痕，清晰地烙印在浮草边缘——那里见证了一个恶徒在失足倾覆的最后一刹那，曾如何绝望抓挠泥沼试图挽回生机，却最终彻底失败的痕迹！翻滚的黑色泥浆已然无情漫过他的头顶，将其彻底封死在了大地最黑暗的幽室之中。

在大格林盆泥潭那万劫不复的腥臭污泥极深处，那颗冷血、狡诈而残忍至极的心脏已然永远停止了跳动。这片吞噬了无辜生命的古老死沼，最终成为了恶魔自掘的万年坟墓！"""
    }
])
