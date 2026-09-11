"""Chinese narrative content adapting 'The Hound of the Baskervilles' by Sir Arthur Conan Doyle.
《巴斯克维尔的猎犬》多视角互动小说中文版。
故事从贝克街221B第一章开始，完整涵盖伦敦线索追查、达特沼地探险及六大多重结局。
底本：book_cn.txt 经典权威中文译本
"""

from src.models import Choice, NodeType, POV, PassageNode, StoryGraph


def build_story_cn() -> StoryGraph:
    """Constructs the Chinese StoryGraph starting from Chapter 1."""
    nodes: dict[str, PassageNode] = {}

    # =========================================================================
    # CHAPTERS 1-5: LONDON PROLOGUE (WATSON POV)
    # =========================================================================
    nodes["watson_ch1_baker_street"] = PassageNode(
        id="watson_ch1_baker_street",
        title="第一章 歇洛克·福尔摩斯先生",
        pov=POV.WATSON,
        node_type=NodeType.ANCHOR,
        anchor_name="anchor_chapter1",
        content=(
            "歇洛克·福尔摩斯先生坐在贝克街221B的早餐桌旁。他除了时常彻夜不眠之外，早晨总是起得很晚的。"
            "我站在壁炉前的小地毯上，拿起了昨晚那位神秘客人遗忘在椅旁的手杖。这是一根很精致而沉重的手杖，"
            "顶端有个疙疸，由槟榔子木制成。紧挨顶端的下面是一圈近一英寸宽的银箍，上面刻着："
            "‘送给皇家外科医学院学士杰姆士·摩梯末，C.C.H.的朋友们赠，一八八四年。’\n\n"
            "‘啊，华生，你对它的看法怎么样？’福尔摩斯背对着我，一边喝着咖啡一边发问，"
            "‘既然昨晚咱们错过了他，对他此来的目的也一无所知，这件意外的纪念品就变得更重要了。请你在仔细观察后，把这个人给我形容一番吧。’"
        ),
        choices=[
            Choice(
                id="w_guess_hunt_club",
                text="推测C.C.H.代表当地某个猎人会，并指出磨损的铁包头和狗咬的牙印。",
                target_node_id="watson_ch2_mortimer",
            ),
            Choice(
                id="w_guess_hospital",
                text="根据M.R.C.S.头衔，推断C.C.H.代表查林十字医院，客人曾是一位任职医院的乡村医生。",
                target_node_id="watson_ch2_mortimer",
            ),
        ],
        clues_discovered=[
            "刻有‘送给皇家外科医学院学士杰姆士·摩梯末，C.C.H.的朋友们赠，一八八四年’的槟榔子木手杖",
            "手杖中央留有卷毛长耳獚犬咬过的清晰牙印",
        ],
    )

    nodes["watson_ch2_mortimer"] = PassageNode(
        id="watson_ch2_mortimer",
        title="第二章 巴斯克维尔的灾祸",
        pov=POV.WATSON,
        node_type=NodeType.BRANCH,
        content=(
            "杰姆士·摩梯末医生走了进来——他是一个又高又瘦的人，长长的鼻子像只鸟嘴，金边眼镜后闪烁着两只敏锐的灰眼睛。"
            "他从胸前口袋里掏出一份泛黄破旧的古老手稿，年代确为一七四二年。那是巴斯克维尔家族祖传的恐怖传说：荒淫残暴的老修果·巴斯克维尔强掳少女，"
            "最终在沼地深处被一只巨大如妖魔的黑色猎犬咬断了喉咙。\n\n"
            "随后，摩梯末医生又拿出了五月十四日的《德文郡纪事报》，向我们披露了三个月前查尔兹·巴斯克维尔爵士在水松夹道栅门前的离奇暴毙。"
            "医生环视室内，声音颤抖地吐露出连验尸官都隐瞒的绝密事实：\n"
            "‘福尔摩斯先生，在距离尸体二十码外的湿软地面上……全都是一只巨大的猎犬的脚印！’"
        ),
        choices=[
            Choice(
                id="w_ask_footprint",
                text="追问摩梯末医生为何在官方验尸公听会上刻意隐瞒猎犬爪印的事实。",
                target_node_id="watson_ch4_henry",
            ),
            Choice(
                id="w_ask_heir",
                text="探询即将由加拿大抵达伦敦滑铁卢车站的合法继承人亨利·巴斯克维尔爵士的处境。",
                target_node_id="watson_ch4_henry",
            ),
        ],
        clues_discovered=[
            "一七四二年修果·巴斯克维尔魔犬传说手稿",
            "查尔兹爵士尸体二十码外发现巨大猎犬爪印",
        ],
    )

    nodes["watson_ch4_henry"] = PassageNode(
        id="watson_ch4_henry",
        title="第四章 亨利·巴斯克维尔爵士",
        pov=POV.WATSON,
        node_type=NodeType.BRANCH,
        content=(
            "次日早晨，新任继承人亨利·巴斯克维尔爵士亲临贝克街。他年约三十，短小精悍，生着一双黑眼睛，神情坚毅好斗。"
            "他刚在诺桑勃兰旅馆落脚，便收到了一封神秘匿名信，信封用粗糙笔迹写就，信瓤中央赫然是用短指甲剪从昨日《泰晤士报》社论上剪下贴成的警告文字：\n"
            "‘若你看重你的生命的价值或还有理性的话，远离沼地。’\n\n"
            "更离奇的是，亨利爵士昨晚放在门外等待擦拭的一双簇新浅棕色高筒靴，竟不翼而飞了一只！"
        ),
        choices=[
            Choice(
                id="w_follow_henry_regent",
                text="跟随福尔摩斯敏捷地冲出公寓，暗中尾随亨利爵士与摩梯末步入摄政街。",
                target_node_id="watson_ch5_london_spy",
            ),
            Choice(
                id="w_examine_letter",
                text="用放大镜仔细检验警告信纸的水印、茉莉香气及剪贴刀口的特征。",
                target_node_id="watson_ch5_london_spy",
            ),
        ],
        clues_discovered=[
            "匿名剪报警告信：‘若你看重你的生命的价值或还有理性的话，远离沼地。’",
            "诺桑勃兰旅馆神秘失窃的未着浅棕色新皮靴",
        ],
    )

    nodes["watson_ch5_london_spy"] = PassageNode(
        id="watson_ch5_london_spy",
        title="第五章 三条断了的线索",
        pov=POV.WATSON,
        node_type=NodeType.ANCHOR,
        anchor_name="anchor_london_mission",
        content=(
            "我们尾随亨利爵士来到摄政街。福尔摩斯突然瞥见一辆缓缓滑行的双轮马车（车号2704号）。"
            "侧窗里探出一张留着浓密大黑胡须、戴着深色眼镜的面孔，正死死盯住亨利爵士！"
            "福尔摩斯拔步飞奔追赶，那马车夫却挥鞭狂奔，瞬间消失在牛津街的车水马龙之中。\n\n"
            "返回旅馆后，离奇的事情再次发生：失踪的浅棕色新鞋被悄悄归还，但亨利爵士一只穿过的旧黑皮靴却被偷走了！"
            "随后应召而来的车夫约翰·克雷顿更证实，那个黑胡子神秘乘客竟狂妄留言：‘你可以告诉他，你的乘客就是歇洛克·福尔摩斯！’\n\n"
            "危险已迫在眉睫。福尔摩斯神情严肃地拍着我的肩膀：‘华生，这是一汪深不可测的险水。你必须带上陆军左轮手枪，"
            "日夜寸步不离地护卫亨利爵士前往巴斯克维尔庄园，并将荒原上的一举一动详尽向我报告！’"
        ),
        choices=[
            Choice(
                id="w_board_express",
                text="整理行装与手枪，陪同亨利爵士登上前往德文郡的大西部特快列车。",
                target_node_id="watson_start",
            ),
            Choice(
                id="w_review_clues",
                text="在前往帕丁顿车站前，与福尔摩斯再次复盘失窃皮靴与幽灵马车的线索。",
                target_node_id="watson_start",
            ),
        ],
        clues_discovered=[
            "乘坐2704号双轮马车、黑胡须深色眼镜并出言挑衅福尔摩斯的神秘暗探",
            "真正被盗、带有亨利爵士浓重体味的旧黑皮靴",
        ],
    )

    # =========================================================================
    # CHAPTERS 1-5: LONDON PROLOGUE (HOLMES POV)
    # =========================================================================
    nodes["holmes_ch1_baker_street"] = PassageNode(
        id="holmes_ch1_baker_street",
        title="第一章 演绎法的推演",
        pov=POV.HOLMES,
        node_type=NodeType.ANCHOR,
        anchor_name="anchor_chapter1",
        content=(
            "我背对着华生坐在早餐桌旁，通过镀银咖啡壶光亮的曲面注视着他的动作。他正在壁炉毯上煞有介事地把玩昨夜客人遗落的手杖。"
            "华生是一根极佳的光的传导者——他那些充满善意而又漏洞百出的推论，往往能精准地将真理的大门推开一条缝隙。\n\n"
            "我取过那根沉重斑驳的槟榔子木手杖，在明媚的晨光下用放大镜扫视：底端磨损剥蚀的厚铁包头，昭示着持杖者常在粗粝的乡间砾石上步行；"
            "‘C.C.H.’并非什么乡野猎人会，而是伦敦查林十字医院的缩写；一八八四年的赠礼日期，正印证了一位有前途的年轻住院外科医生在结婚自行开业时辞别都市；"
            "而木杖中央清晰交错的凹痕，其牙距比狸犬宽、比獒犬窄——一条活泼的卷毛长耳獚犬！"
            "门铃声适时响起，窗外楼阶下，这条獚犬与它的主人正叩响贝克街的门扉。"
        ),
        choices=[
            Choice(
                id="h_welcome_mortimer",
                text="迎接杰姆士·摩梯末医生进门，请他陈述那桩令他深感棘手的非凡疑案。",
                target_node_id="holmes_ch2_mortimer",
            ),
            Choice(
                id="h_examine_cranial",
                text="让摩梯末医生惊叹于你的长颅骨标本价值，同时冷静梳理思绪准备切入正题。",
                target_node_id="holmes_ch2_mortimer",
            ),
        ],
        clues_discovered=[
            "摩梯末：查林十字医院住院外科医生，现达特沼地乡村医生",
            "在贝克街门阶得到印证的卷毛长耳獚犬",
        ],
    )

    nodes["holmes_ch2_mortimer"] = PassageNode(
        id="holmes_ch2_mortimer",
        title="第二章 荒原上的神秘疑案",
        pov=POV.HOLMES,
        node_type=NodeType.BRANCH,
        content=(
            "摩梯末医生展开了一七四二年的羊皮古卷，讲述了修果·巴斯克维尔的恶灵血仇。尽管世俗法庭将查尔兹爵士之死归结为心脏衰竭，"
            "但摩梯末披露的密情却令人玩味：水松夹道栅门前的泥土里，清晰地印着一只体型骇人的巨犬爪印！\n\n"
            "查尔兹爵士曾在夜色中的栅门前伫立了五至十分钟，烟灰两度掉落在沙砾上。随后，他仿佛遭遇了难以名状的狂恐，"
            "发足沿夹道狂奔，足迹因极度惊骇甚至化为踮足奔跑的凹痕，直至脆弱的心脏破裂。\n\n"
            "最后一位法定继承人亨利·巴斯克维尔爵士尚余一小时便将自加拿大抵英。他是否应该踏入达特沼地那片凶险之地？"
        ),
        choices=[
            Choice(
                id="h_plan_regent_meeting",
                text="叮嘱摩梯末务必在滑铁卢车站接应亨利爵士，并于明日上午十点整一同来贝克街。",
                target_node_id="holmes_ch4_regent_street",
            ),
            Choice(
                id="h_smoke_meditation",
                text="在浓密的烟草冥想中展开达特沼地军用地图，彻夜推演水松夹道的地势与逃生路线。",
                target_node_id="holmes_ch4_regent_street",
            ),
        ],
        clues_discovered=[
            "水松夹道栅门处的巨大猎犬爪印",
            "查尔兹爵士曾驻足吸雪茄五至十分钟后发足狂奔",
        ],
    )

    nodes["holmes_ch4_regent_street"] = PassageNode(
        id="holmes_ch4_regent_street",
        title="第四章 摄政街的幽灵马车",
        pov=POV.HOLMES,
        node_type=NodeType.BRANCH,
        content=(
            "年轻的亨利爵士如约而至，带来了那封散发着白茉莉清香的警告信。文字是从昨日《泰晤士报》社论上用短刃剪刀剪下的铅印字体，"
            "而他在诺桑勃兰旅馆的一只崭新浅棕色皮靴已离奇被窃。\n\n"
            "当客人离去后，我同华生紧紧缀在他们百码之后走入摄政街。街道对面，一辆车牌2704号的双轮出租马车正悄无声息地尾随追踪。"
            "隔着车窗，一个蓄着浓密黑髯、戴着遮光眼镜的暗探赫然在目！当我与之目光交汇的刹那，对手骤然喝令车夫扬鞭，马车疾驰没入车流。"
        ),
        choices=[
            Choice(
                id="h_trace_cab_2704",
                text="通过出租马车登记处追查2704号车夫约翰·克雷顿，传唤其至贝克街对质。",
                target_node_id="holmes_ch5_broken_threads",
            ),
            Choice(
                id="h_search_hotel_boots",
                text="亲赴诺桑勃兰旅馆盘问侍者，追查皮靴失窃的内部接应。",
                target_node_id="holmes_ch5_broken_threads",
            ),
        ],
        clues_discovered=[
            "带有茉莉香气、《泰晤士报》剪贴而成的警告信",
            "2704号双轮马车里浓密黑须、戴眼镜的跟踪者",
        ],
    )

    nodes["holmes_ch5_broken_threads"] = PassageNode(
        id="holmes_ch5_broken_threads",
        title="第五章 布局达特沼地",
        pov=POV.HOLMES,
        node_type=NodeType.ANCHOR,
        anchor_name="anchor_london_mission",
        content=(
            "车夫约翰·克雷顿向我证实：他的神秘乘客下车时竟狂傲地自称是‘歇洛克·福尔摩斯先生’！"
            "与此同时，旅馆传讯称：未穿过的新棕靴被退回，但亨利爵士一只饱含个人体味的旧黑皮靴却被偷换了。\n\n"
            "脉络瞬间洞若观火：新靴无气味，偷窃旧靴是为了让一头真正的猎兽熟悉并锁定亨利爵士的体味追踪扑杀！"
            "这是一位心思缜密、极度凶残的旗鼓相当的对手。若我大张旗鼓护送亨利爵士前往德文郡，狡狐必将遁入阴影。"
            "唯有伪装留守伦敦，让华生作为明盾护卫爵士，而我暗中潜入达特荒原史前石棚营地隐匿布控，方能引蛇出洞一网打尽！"
        ),
        choices=[
            Choice(
                id="h_dispatch_watson_ahead",
                text="向华生交代保卫守则，派其护卫亨利爵士先行奔赴德文郡，同时暗度陈仓。",
                target_node_id="holmes_start",
            ),
            Choice(
                id="h_instruct_cartwright_secret",
                text="密令机敏少年卡特莱购置干粮装备，暗中运送至荒原史前石棚营地作为秘密指挥所。",
                target_node_id="holmes_start",
            ),
        ],
        clues_discovered=[
            "对手盗窃旧黑皮靴系为训练实体恶犬嗅觉追踪",
            "启动达特沼地石棚营地绝密潜伏计划",
        ],
    )

    # =========================================================================
    # CHAPTERS 1-5: LONDON PROLOGUE (STAPLETON POV)
    # =========================================================================
    nodes["stapleton_ch1_london"] = PassageNode(
        id="stapleton_ch1_london",
        title="第四章 潜伏伦敦的密谋",
        pov=POV.STAPLETON,
        node_type=NodeType.ANCHOR,
        anchor_name="anchor_chapter1",
        content=(
            "戴着精心粘合的浓密假黑胡子和深色平光眼镜，我从南安普敦一路盯梢亨利·巴斯克维尔至伦敦诺桑勃兰旅馆。"
            "我那个心慈手软的妻子贝瑟尔妄图用剪自《泰晤士报》的字条向他预警，被我当场察觉并施以惩戒，可惜信件已先行落入邮筒。\n\n"
            "在旅馆走廊里，我用半枚金币买通了一个蠢笨的杂役，命他从爵士门外偷出一只皮靴。"
            "可那个蠢货竟偷来了一只从未着地的全新浅棕色高筒靴！未穿过的皮革毫无活人体味，如何能用以激发猛兽狂暴的嗅觉追踪？"
            "我必须退还废靴，命他换偷一只亨利实际穿过、浸透气味的旧黑皮靴。"
        ),
        choices=[
            Choice(
                id="s_demand_worn_boot",
                text="威逼利诱旅馆仆役，必须趁乱偷出亨利爵士穿过的那双旧黑皮靴。",
                target_node_id="stapleton_ch4_cab",
            ),
            Choice(
                id="s_shadow_baker_street",
                text="雇佣双轮马车，暗中监视亨利爵士与摩梯末医生前往贝克街求援的行踪。",
                target_node_id="stapleton_ch4_cab",
            ),
        ],
        clues_discovered=[
            "化名与伪装：浓密假黑须与深色遮光眼镜",
            "未穿过的棕靴无气味被弃，锁定带有体味的旧黑皮靴",
        ],
    )

    nodes["stapleton_ch4_cab"] = PassageNode(
        id="stapleton_ch4_cab",
        title="第五章 2704号马车的较量",
        pov=POV.STAPLETON,
        node_type=NodeType.BRANCH,
        content=(
            "我雇下了特拉法尔加广场的2704号双轮马车，命车夫约翰·克雷顿尾随亨利前往贝克街221B。"
            "但当那个短小精悍的爵士踏入大门时，一个高瘦、生着鹰钩鼻的敏锐身影赫然步入街面——歇洛克·福尔摩斯！"
            "在摄政街的橱窗前，那双令全欧洲罪犯胆寒的灰眼睛猛地刺穿了马车的侧窗玻璃！\n\n"
            "我霍地顶开车顶望孔：‘车夫，拼命跑！去滑铁卢车站！甩掉他们我赏你两个金币！’"
            "在滑铁卢车站喧嚣的站台，接过浸透雨水的金币时，我忍不住对目瞪口呆的车夫报以狂妄的戏谑："
            "‘回去告诉你所有的朋友，你刚才拉的乘客就是歇洛克·福尔摩斯！’"
        ),
        choices=[
            Choice(
                id="s_take_early_express",
                text="收好取回的沾满气味的旧黑皮靴，搭乘早班大西部特快潜回德文郡大荒原。",
                target_node_id="stapleton_ch5_devon_prep",
            ),
            Choice(
                id="s_vanish_in_crowd",
                text="在滑铁卢人潮中曲折回旋，彻底切断贝克街眼线的任何追踪可能。",
                target_node_id="stapleton_ch5_devon_prep",
            ),
        ],
        clues_discovered=[
            "乘坐2704号马车成功从福尔摩斯眼皮底下脱身",
            "狂妄假报福尔摩斯之名羞辱贝克街名侦探",
        ],
    )

    nodes["stapleton_ch5_devon_prep"] = PassageNode(
        id="stapleton_ch5_devon_prep",
        title="第五章 返回大格林盆泥潭",
        pov=POV.STAPLETON,
        node_type=NodeType.ANCHOR,
        anchor_name="anchor_london_mission",
        content=(
            "亨利·巴斯克维尔那只穿过的旧黑皮靴，已被我用涂油丝绸妥帖裹好藏在手提箱底。我登上了返回德文郡的特快列车。"
            "亨利与那位迟钝的军医华生将在两天后抵达，他们满以为那位伦敦大侦探会在此案中护佑左右，殊不知贝克街已经被我远远甩在了身后。\n\n"
            "梅利琵宅邸的戏台已经搭好。大格林盆泥潭深处废弃锡矿棚里的那头混血恶兽，已经整整绝食了两天。"
            "只待将这只散发着猎物浓郁气息的旧皮靴送到它涎水淋漓的巨吻之下。"
        ),
        choices=[
            Choice(
                id="s_to_mire_kennel",
                text="踏上隐秘的沼泽栈道，前往泥潭孤岛展开恶犬的气味嗜血训练。",
                target_node_id="stapleton_start",
            ),
            Choice(
                id="s_to_merripit_prep",
                text="返回梅利琵宅邸彻底威慑贝瑟尔，为年轻爵士的踏入布设致命鸿门宴。",
                target_node_id="stapleton_start",
            ),
        ],
        clues_discovered=[
            "已取得沾染亨利爵士体味的旧皮靴供猎犬嗅闻",
            "梅利琵宅邸陷阱已备，静候华生与爵士到来",
        ],
    )

    # --- WATSON (CN) ---
    nodes["watson_start"] = PassageNode(
        id="watson_start",
        title="第六章 抵达达特沼地",
        pov=POV.WATSON,
        node_type=NodeType.ANCHOR,
        anchor_name="anchor_arrival",
        content=(
            "列车在德文郡达特沼地的小站颤抖着停了下来。十月的寒风夹杂着凄清与荒凉，从高耸黝黑的花岗石山岗上呼啸吹来。"
            "亨利·巴斯克维尔爵士踏上了石子月台，端正了一下粗花呢猎帽。持枪的骑警在铁道两侧来回巡逻——臭名昭著的逃犯塞尔登刚刚从王子镇大监狱脱逃。\n\n"
            "歇洛克·福尔摩斯先生将亨利爵士的安危托付于我。当我们乘坐的双轮敞篷马车向着暮色中阴森对峙的巴斯克维尔双塔疾驰而去时，"
            "那片辽阔苍茫的大沼地在眼前伸展开来，宛如一片凝固而沉寂的波涛巨浪。"
        ),
        choices=[
            Choice(
                id="w_to_hall",
                text="直接前往巴斯克维尔庄园，向神色慌乱的总管白瑞摩探询内情。",
                target_node_id="watson_baskerville_hall",
            ),
            Choice(
                id="w_to_alley",
                text="先勘察查尔兹爵士猝死的水松夹道与通往沼地的栅门边缘。",
                target_node_id="watson_yew_alley",
            ),
            Choice(
                id="w_to_stapleton",
                text="沿着荒原边缘独自行走，前往附近的梅利琵宅邸拜访邻里。",
                target_node_id="watson_meet_stapleton",
            ),
        ],
        clues_discovered=["沼地上搜捕逃犯塞尔登的武装卫兵"],
    )

    nodes["watson_baskerville_hall"] = PassageNode(
        id="watson_baskerville_hall",
        title="巴斯克维尔庄园的阴影",
        pov=POV.WATSON,
        node_type=NodeType.BRANCH,
        content=(
            "巴斯克维尔庄园是一座被常春藤遮蔽的古老花岗石宅邸，到处弥漫着阴暗与霉烂的气息。"
            "总管白瑞摩虽以深沉周到的礼数接待了我们，但他那双黑眼睛却闪烁着难以掩饰的局促与心神不宁。"
            "午夜时分，长廊深处竟隐隐传来白瑞摩太太压抑而凄凉的抽泣声。\n\n"
            "我必须查明白瑞摩夫妇究竟在隐瞒什么，还是应当按照福尔摩斯的叮嘱，前往考姆·特雷西调查查尔兹爵士生前通信的另一端。"
        ),
        choices=[
            Choice(
                id="w_watch_barrymore",
                text="在深夜走廊中设下伏击暗哨，暗中监视白瑞摩鬼祟的夜行举动。",
                target_node_id="watson_night_watch",
            ),
            Choice(
                id="w_visit_lyons",
                text="雇佣轻便双轮车前往考姆·特雷西，当面质询那位神秘的劳拉·里昂斯夫人。",
                target_node_id="watson_laura_lyons",
            ),
        ],
        clues_discovered=["白瑞摩惊慌失措的神情", "深夜宅邸长廊中的女人哭泣声"],
    )

    nodes["watson_yew_alley"] = PassageNode(
        id="watson_yew_alley",
        title="水松夹道与通往沼地的栅门",
        pov=POV.WATSON,
        node_type=NodeType.BRANCH,
        content=(
            "水松夹道是一条被十二英尺高茂密水松树篱紧紧围拢的长道，幽深如隧道。在长道的尽头处，"
            "一道简陋的小栅门直通那片浩瀚无垠的达特沼地。数月前的深夜，查尔兹爵士曾在此站立良久，弹落了两次雪茄烟灰，随后便陷入狂乱奔逃骤然猝死。\n\n"
            "摩梯末医生那令人胆寒的耳语仍在我耳际回响：‘福尔摩斯先生，那地上分明是一只极大的猎狗的爪印！’"
            "栅门之外，几丛石楠植物在秋风中瑟瑟发抖，荒原小径蜿蜒伸向致命的大格林盆泥潭深处。"
        ),
        choices=[
            Choice(
                id="w_alley_to_mire",
                text="穿过水松夹道栅门，顺着荒地小径探向远方的梅利琵宅邸。",
                target_node_id="watson_meet_stapleton",
            ),
            Choice(
                id="w_alley_to_hall",
                text="返回庄园主楼，与亨利爵士汇合并筹备今夜的长廊守夜。",
                target_node_id="watson_night_watch",
            ),
        ],
        clues_discovered=["栅门处的雪茄烟灰残余", "伸向荒原深处的野草折痕"],
    )

    nodes["watson_meet_stapleton"] = PassageNode(
        id="watson_meet_stapleton",
        title="大格林盆泥潭的博物学家",
        pov=POV.WATSON,
        node_type=NodeType.BRANCH,
        content=(
            "一个身形干练、手持捕蝶网和铁皮标本盒的男子在泥沼旁向我招手。他自称杰克·斯台普吞，梅利琵宅邸的博物学家。"
            "正当交谈间，一匹误入沼地的矮种马踏上了那片鲜绿的草皮，仅仅数秒间，沼泥便狂暴地吞噬了马匹的四蹄与脊背，在一阵凄惨的悲鸣中彻底沉没无踪！\n\n"
            "‘一步之差便是灭顶之灾，’斯台普吞微笑着说。片刻后，他的胞妹贝瑟尔·斯台普吞小姐仓皇赶来。"
            "在浓雾中，她误将我当成了亨利爵士，紧紧抓住我的衣袖，急迫而凄厉地颤声道：‘快回伦敦去！今晚就走，永远别再回来！’"
        ),
        choices=[
            Choice(
                id="w_interrogate_beryl",
                text="将斯台普吞小姐拉至岩石旁，追问她这绝望预警的背后缘由。",
                target_node_id="watson_beryl_warning",
            ),
            Choice(
                id="w_return_with_caution",
                text="保持警惕，不当着杰克·斯台普吞的面打草惊蛇，折返庄园报告。",
                target_node_id="watson_night_watch",
            ),
        ],
        clues_discovered=["大格林盆泥潭吞噬活物的绝险沼径", "贝瑟尔绝望而迫切的警告"],
    )

    nodes["watson_beryl_warning"] = PassageNode(
        id="watson_beryl_warning",
        title="凄切的低语警告",
        pov=POV.WATSON,
        node_type=NodeType.BRANCH,
        content=(
            "当斯台普吞小姐得知我是华生医生而非巴斯克维尔继承人时，面色惨白如纸。"
            "‘忘掉我刚才说的话吧！’她颤声哀求，眼眸中却翻涌着极度的恐惧，‘我哥哥绝不能知道我同你交谈过。"
            "但是危险正在这片沼地上的每一块岩石后潜伏！倘若你在乎亨利爵士的性命，立刻带他逃离此地！’\n\n"
            "暮色沉沉降临。我回眸远眺，只见在黑色岩岗那高耸入云的荒凉峰顶上，月华如水，一个孤单高大的黑影正如雕像般迎风屹立，冷冷注视着整座原野。"
        ),
        choices=[
            Choice(
                id="w_beryl_to_watch",
                text="火速赶回巴斯克维尔庄园，寸步不离贴身保护亨利爵士。",
                target_node_id="watson_night_watch",
            ),
            Choice(
                id="w_scout_the_tor",
                text="攀登乱石嶙峋的花岗石孤峰，查探那位神秘的岩岗窥探者。",
                target_node_id="watson_stalk_figure",
            ),
        ],
        clues_discovered=["屹立在黑色岩岗顶端的神秘黑影", "贝瑟尔对兄长斯台普吞的极度畏惧"],
    )

    nodes["watson_night_watch"] = PassageNode(
        id="watson_night_watch",
        title="西窗上的烛光",
        pov=POV.WATSON,
        node_type=NodeType.ANCHOR,
        anchor_name="anchor_convict",
        content=(
            "凌晨两点，我和亨利爵士悄无声息地潜行在漆黑的回廊中。总管白瑞摩手持蜡烛伫立在西窗前，"
            "向着漆黑一片的荒原打出忽明忽暗的火光信号！在我们严厉逼问下，他痛哭承认：逃犯塞尔登正是白瑞摩太太的亲生胞弟！\n\n"
            "就在此刻，夜风中陡然自死寂的沼地深处腾起一声漫长、凄绝、撕心裂肺的狂暴狂吠！"
            "那声音在夜空中回荡震颤，不似寻常狼犬，而是充满了地狱恶魔般的狞恶杀气，令听者血凝心悸！"
        ),
        choices=[
            Choice(
                id="w_pursue_moor",
                text="拔出左轮手枪，同亨利爵士冲入黑夜沼地，循着烛火信号追踪逃犯。",
                target_node_id="watson_moor_pursuit",
            ),
            Choice(
                id="w_track_watcher",
                text="将逃犯留待警方搜捕，集中精力暗查岩岗顶峰那位行踪莫测的监视者。",
                target_node_id="watson_stalk_figure",
            ),
        ],
        clues_discovered=["白瑞摩利用烛光向逃犯塞尔登报信", "深夜原野上那声毛骨悚然的狂吠"],
    )

    nodes["watson_moor_pursuit"] = PassageNode(
        id="watson_moor_pursuit",
        title="荒原石丘上的追击",
        pov=POV.WATSON,
        node_type=NodeType.BRANCH,
        content=(
            "冰冷的雨丝刺痛了我和亨利爵士的脸颊。在忽明忽灭的闪电与微弱月光下，我们窥见了逃犯塞尔登那犹如野兽般粗犷凶狞的面孔。"
            "亨利爵士举枪射击，子弹在花岗岩上迸出火花，逃犯敏捷如猿猴般没入了犬牙交错的巨石阵中。\n\n"
            "我猛然抬头望向穿破云层的皓月——在不远处的尖耸石岗之巅，赫然伫立着另一个神秘人！"
            "那人身形消瘦修长，披着深色斗篷，双手抱臂，以君临大地般冷静深邃的目光俯瞰着这场惊心动魄的夜猎。"
        ),
        choices=[
            Choice(
                id="w_follow_second_man",
                text="攀上陡峭的山岩，顺着脚印搜查那黑影落脚的史前石屋巢穴。",
                target_node_id="watson_stalk_figure",
            ),
            Choice(
                id="w_switch_to_holmes",
                text="【转换视角：切换至歇洛克·福尔摩斯在荒原石屋中的行动】",
                target_node_id="holmes_hut_interior",
                pov_switch=POV.HOLMES,
            ),
        ],
        clues_discovered=["石岗顶峰那黑影身姿颀长，神态镇定从容"],
    )

    nodes["watson_stalk_figure"] = PassageNode(
        id="watson_stalk_figure",
        title="史前石屋中的窥探",
        pov=POV.WATSON,
        node_type=NodeType.BRANCH,
        content=(
            "我小心翼翼地攀上远古不列颠人遗留下的圆形石屋。屋内避风处铺着粗呢毯子，摆放着面包与牛舌肉罐头。"
            "在一块平整的花岗石板上，赫然躺着一枚抽剩的香烟蒂——上面清晰印着‘牛津街布莱德雷商店’字样！"
            "旁边还有一张铅笔草签：‘华生医生已前往考姆·特雷西。’\n\n"
            "门口光线陡然暗了下来。一具高挑的身影投射在石壁之上，一只手静静搭在石门框边。"
        ),
        choices=[
            Choice(
                id="w_wait_gun_drawn",
                text="扳开左轮手枪机头，厉声喝令来者举起双手投降！",
                target_node_id="watson_hut_reunion",
            ),
            Choice(
                id="w_flank_hut",
                text="侧身滑出石屋死角，自乱石背侧包抄伏击来客！",
                target_node_id="holmes_moor_ambush",
            ),
        ],
        clues_discovered=["布莱德雷商店的精制烟头", "记录着华生行踪的侦查便条"],
    )

    nodes["watson_laura_lyons"] = PassageNode(
        id="watson_laura_lyons",
        title="劳拉·里昂斯夫人的秘密",
        pov=POV.WATSON,
        node_type=NodeType.BRANCH,
        content=(
            "在考姆·特雷西，神色凄楚的劳拉·里昂斯夫人在我严词追问下掩面痛哭："
            "‘是杰克·斯台普吞！是他指使我给查尔兹爵士写信，约他深夜在水松夹道栅门相会资助我的离婚官司！"
            "可到了最后一刻，他却严厉勒令我绝不可赴约，声称他自己会妥善料理一切……’\n\n"
            "真相犹如霹雳般在我脑海中炸裂！查尔兹爵士是在斯台普吞蓄意诱导的约会中，迎面遭遇了那头恶魔巨兽！"
        ),
        choices=[
            Choice(
                id="w_lyons_to_hut",
                text="火速折回原野寻找那位神秘隐士，合力揭发斯台普吞的弑亲毒计。",
                target_node_id="watson_hut_reunion",
            ),
            Choice(
                id="w_lyons_confront_stapleton",
                text="直接赶往梅利琵宅邸，赶在斯台普吞再次行凶前当面撕下其伪善假面！",
                target_node_id="watson_direct_confrontation",
            ),
        ],
        clues_discovered=["斯台普吞指使诱骗查尔兹爵士夜赴死地的铁证"],
    )

    nodes["watson_hut_reunion"] = PassageNode(
        id="watson_hut_reunion",
        title="荒原石屋的重逢",
        pov=POV.WATSON,
        node_type=NodeType.BRANCH,
        content=(
            "门外传来一个平静、亲切而带着戏谑的声音：‘多么美好的傍晚啊，我亲爱的华生！"
            "你真的不该坐在离洞口这么近的地方，你的影子早在五十码外就出卖了你。’\n\n"
            "我目瞪口呆地垂下手枪。走进石屋的竟是歇洛克·福尔摩斯先生！他目光如炬，清瘦从容，嘴角挂着熟悉的微笑。"
            "‘华生，我潜伏在沼地，正是为了让斯台普吞误以为我远在伦敦！法网已经收紧，今晚亨利爵士将赴梅利琵宅邸赴宴，决战时刻到了！’"
        ),
        choices=[
            Choice(
                id="w_reunion_to_dinner",
                text="与苏格兰场警官雷斯垂德汇合，在梅利琵宅邸外设下包围圈。",
                target_node_id="holmes_merripit_dinner",
                pov_switch=POV.HOLMES,
            ),
            Choice(
                id="w_take_vantage",
                text="潜伏至梅利琵宅邸餐厅窗外的花岗岩石块后，严密监视室内动静。",
                target_node_id="watson_climax_vigil",
            ),
        ],
        clues_discovered=["歇洛克·福尔摩斯早已亲临达特沼地实地指挥"],
    )

    nodes["watson_direct_confrontation"] = PassageNode(
        id="watson_direct_confrontation",
        title="梅利琵宅邸的不期而遇",
        pov=POV.WATSON,
        node_type=NodeType.BRANCH,
        content=(
            "我孤身一人赶至梅利琵宅邸。斯台普吞迎入客厅，脸上的假笑紧绷而抽搐。"
            "院落后方一间废弃的外屋中，陡然传来一声低沉雄浑、令人骨髓发冷的闷雷般犬吠，连地板都微微震颤。"
            "斯台普吞的手指缓缓滑向了身旁那柄沉重的手杖。\n\n"
            "‘华生医生，您似乎心神不宁，’他柔声细语，‘不如随我去后院观赏一下新采集的飞蛾标本？’"
        ),
        choices=[
            Choice(
                id="w_force_outhouse",
                text="拔出手枪，强行勒令斯台普吞交出后院锁闭外屋的钥匙！",
                target_node_id="watson_hound_early_release",
            ),
            Choice(
                id="w_feign_retreat",
                text="托辞亨利爵士有紧急传话，假装告退，迅速向外围的福尔摩斯报信。",
                target_node_id="watson_climax_vigil",
            ),
        ],
    )

    nodes["watson_climax_vigil"] = PassageNode(
        id="watson_climax_vigil",
        title="沼地白雾中的警戒",
        pov=POV.WATSON,
        node_type=NodeType.ANCHOR,
        anchor_name="anchor_climax",
        content=(
            "我屏息蹲伏在梅利琵宅邸餐厅窗外的石块后。透过微启的窗帘，我看到亨利爵士与斯台普吞正相对对饮，斯台普吞频频查看着金表。\n\n"
            "然而屋外正发生着一场致命的灾难：一堵浓重冰凉的惨白色雾墙，正自大格林盆泥潭方向汹涌滚滚翻腾而来！"
            "不出五分钟，整个回返庄园的小径就会被浓雾彻底吞没。倘若视线完全受阻，我们便根本无法拦截即将来袭的凶兽！"
        ),
        choices=[
            Choice(
                id="w_signal_holmes",
                text="立即向岩岗后的福尔摩斯与雷斯垂德发出紧急射击预警信号！",
                target_node_id="climax_fog_advance",
            ),
            Choice(
                id="w_storm_house",
                text="踢破餐厅大门，赶在亨利爵士踏出房门之前将他当场救出！",
                target_node_id="ending_watson_heroic",
            ),
        ],
        clues_discovered=["自大格林盆泥潭吞没道路的浓烈地表死雾"],
    )

    nodes["watson_hound_early_release"] = PassageNode(
        id="watson_hound_early_release",
        title="恶犬破笼而出",
        pov=POV.WATSON,
        node_type=NodeType.BRANCH,
        content=(
            "斯台普吞狞笑着扭转了铁锁！厚重的木门轰然弹开！一头宛如来自地狱最深处的恐怖造物狂跃而出——"
            "一头体型极其庞大的黑犬，全身上下烈焰蒸腾，嘴角淌着幽蓝的荧光，张开血盆大口直扑我的喉咙！"
        ),
        choices=[
            Choice(
                id="w_stand_and_fire",
                text="扎稳马步，瞄准那燃烧着荧光的胸膛连扣扳机！",
                target_node_id="ending_watson_heroic",
            ),
            Choice(
                id="w_dodge_for_cover",
                text="扑倒在花岗石矮墙背后，等待山梁上福尔摩斯精准致命的步枪支援！",
                target_node_id="ending_canon",
            ),
        ],
    )

    # --- HOLMES (CN) ---
    nodes["holmes_start"] = PassageNode(
        id="holmes_start",
        title="石屋中的侦探",
        pov=POV.HOLMES,
        node_type=NodeType.ANCHOR,
        anchor_name="anchor_arrival",
        content=(
            "冰冷粗粝的史前石屋已做为我的秘密指挥所整整三天。华生以为我仍在伦敦贝克街。"
            "若他得知我的行踪，以他忠厚热忱的天性必会频繁与我联络，那狡猾的对手势必闻风遁形。\n\n"
            "小车夫卡特莱特悄然从考姆·特雷西为我运来面包与衣物。在诺桑勃兰旅馆被窃的两只鞋子是全案的枢纽——"
            "第一只全新的黄皮鞋因毫无气味而被弃；第二只旧黑皮鞋饱含亨利爵士的个人体味被窃贼盗走。"
            "凶手饲养着一头活生生的嗜血猎犬，且正在用气味对它进行严苛训练。"
        ),
        choices=[
            Choice(
                id="h_analyze_boot",
                text="在显微镜下化验泥潭芦苇刮下的荧光化学涂料残渍。",
                target_node_id="holmes_chemical_analysis",
            ),
            Choice(
                id="h_telescope_moor",
                text="用袖珍蔡司望远镜监视巴斯克维尔庄园与梅利琵宅邸的动静。",
                target_node_id="holmes_moor_surveillance",
            ),
            Choice(
                id="h_intercept_cartwright",
                text="接见小报童卡特莱特，详阅华生医生每日送达的侦查手记。",
                target_node_id="holmes_read_reports",
            ),
        ],
        clues_discovered=["利用被盗旧皮鞋进行猎犬气味追踪训练的严密阴谋"],
    )

    nodes["holmes_chemical_analysis"] = PassageNode(
        id="holmes_chemical_analysis",
        title="荧光化学试剂的分析",
        pov=POV.HOLMES,
        node_type=NodeType.BRANCH,
        content=(
            "在我的便携化学试验包中，从格林盆泥潭枯草上取下的涂料成分昭然若揭："
            "这是一种经由特殊石蜡调和的无味磷光制剂！由于完全隔绝了异味，它既不会干扰猎犬敏锐的嗅觉，"
            "又能在漆黑的深夜中发出令人魂飞魄散的耀眼蓝白荧火！\n\n"
            "将古老诅咒赋予血肉实体的，是一位智力绝顶、精通动物学的非凡凶徒。"
            "在这片荒原之上，究竟何人既懂科学，又对巴斯克维尔庞大遗产虎视眈眈？"
        ),
        choices=[
            Choice(
                id="h_research_ancestry",
                text="追查巴斯克维尔家族族谱中流亡美洲的分支血脉。",
                target_node_id="holmes_ancestral_clue",
            ),
            Choice(
                id="h_scout_mire_island",
                text="趁着暮色苍茫，沿着泥潭暗桩摸入泥沼中央孤岛侦察犬舍。",
                target_node_id="holmes_mire_recon",
            ),
        ],
        clues_discovered=["不伤及猎犬嗅觉的特殊调配无味磷光化合物"],
    )

    nodes["holmes_moor_surveillance"] = PassageNode(
        id="holmes_moor_surveillance",
        title="望远镜下的沼地",
        pov=POV.HOLMES,
        node_type=NodeType.BRANCH,
        content=(
            "高倍望远镜将原野上的纤毫毕现展现在我眼前。斯台普吞手持捕蝶网穿行在大格林盆泥潭边缘，"
            "其落足步伐异乎寻常地精准——常人陷足立毙的泥泞，他竟如履平地。\n\n"
            "华生正在接近他。那位所谓的胞妹贝瑟尔急促奔出，神情激愤，手势极其决绝。"
            "那不是寻常的兄妹口角——她在警告华生！这个女人是被胁迫的从犯，心怀良知与绝望。"
        ),
        choices=[
            Choice(
                id="h_surveillance_to_mire",
                text="勘测斯台普吞插在泥潭死地中的秘密柳木标记残桩。",
                target_node_id="holmes_mire_recon",
            ),
            Choice(
                id="h_surveillance_to_reports",
                text="返回石屋基地，批阅华生自庄园送达的第一手调查文报。",
                target_node_id="holmes_read_reports",
            ),
        ],
        clues_discovered=["隐匿于大格林盆泥潭中的柳木寻路暗桩"],
    )

    nodes["holmes_read_reports"] = PassageNode(
        id="holmes_read_reports",
        title="华生医生的情报信件",
        pov=POV.HOLMES,
        node_type=NodeType.BRANCH,
        content=(
            "华生展现了出色的观察力。他记录了白瑞摩的烛火暗号并锁定了越狱犯塞尔登。"
            "更为关键的是，他查出查尔兹爵士临死当夜约见的女子缩写为‘L.L.’。\n\n"
            "经我调取教区档案，此人正是考姆·特雷西的劳拉·里昂斯夫人！"
            "而全额出资为她聘请律师办理离婚手续的幕后善人，正是这位看似甘于清贫的斯台普吞！"
        ),
        choices=[
            Choice(
                id="h_investigate_ancestry",
                text="前往庄园长廊深研巴斯克维尔历代祖先画像的骨骼面相。",
                target_node_id="holmes_ancestral_clue",
            ),
            Choice(
                id="h_observe_night_chase",
                text="夜幕低垂时登临黑色岩岗，暗中俯瞰围捕塞尔登的战局。",
                target_node_id="holmes_figure_on_tor",
            ),
        ],
        clues_discovered=["斯台普吞暗中掌控劳拉·里昂斯的资金流水"],
    )

    nodes["holmes_ancestral_clue"] = PassageNode(
        id="holmes_ancestral_clue",
        title="雨果·巴斯克维尔的画像",
        pov=POV.HOLMES,
        node_type=NodeType.BRANCH,
        content=(
            "巴斯克维尔庄园餐厅墙上的古老画像解开了一切谜团！当我用手掌遮掩住凶暴的雨果爵士头上的卷发与宽檐帽，"
            "画中那副阴险、贪婪而冷酷的面孔，竟然与杰克·斯台普吞分毫不差！\n\n"
            "他正是查尔兹爵士亡故的三弟罗杰·巴斯克维尔在南美洲所生的私生子！"
            "他化名凡德勒潜回英国，只要查尔兹与亨利相继暴亡，他就是这百万镑豪门家产毫无争议的法定第一继承人！"
        ),
        choices=[
            Choice(
                id="h_summon_lestrade",
                text="火速电召苏格兰场雷斯垂德警官携正式拘捕令赶赴德文郡！",
                target_node_id="holmes_merripit_dinner",
            ),
            Choice(
                id="h_reunion_with_watson",
                text="在荒原石屋等候华生归来，向他彻底揭开全盘阴谋。",
                target_node_id="watson_hut_reunion",
                pov_switch=POV.WATSON,
            ),
        ],
        clues_discovered=["斯台普吞正是罗杰·巴斯克维尔的亲子与合法继承人"],
    )

    nodes["holmes_figure_on_tor"] = PassageNode(
        id="holmes_figure_on_tor",
        title="黑色岩岗上的身影",
        pov=POV.HOLMES,
        node_type=NodeType.ANCHOR,
        anchor_name="anchor_convict",
        content=(
            "黑色岩岗之上，狂风如长号哀鸣。山谷深处，巴斯克维尔庄园的窗前闪过一豆烛火，随后传来两人围堵塞尔登的枪声。"
            "刹那间，那声令人血液冻结的恐怖咆哮骤然在死寂的沼地上空炸响！\n\n"
            "在我脚下的乱石岗中，亡命狂奔的塞尔登身上，竟然穿着白瑞摩赠予他的亨利爵士旧粗呢猎装！"
            "那头习惯以气味辨认目标的恶犬一旦捕获气味，定会将他当成亨利爵士生生撕碎！"
        ),
        choices=[
            Choice(
                id="h_race_to_selden",
                text="飞身跃下石崖，赶在巨犬撕咬前拦截凶案发生！",
                target_node_id="holmes_selden_crisis",
            ),
            Choice(
                id="h_slip_back_to_hut",
                text="悄然潜回石屋基地，在行踪彻底暴露前同华生汇合。",
                target_node_id="holmes_hut_interior",
            ),
            Choice(
                id="h_switch_to_stapleton",
                text="【转换视角：切换至杰克·斯台普吞操控恶犬的暗夜现场】",
                target_node_id="stapleton_moor_night",
                pov_switch=POV.STAPLETON,
            ),
        ],
    )

    nodes["holmes_selden_crisis"] = PassageNode(
        id="holmes_selden_crisis",
        title="绝壁下的惨剧",
        pov=POV.HOLMES,
        node_type=NodeType.BRANCH,
        content=(
            "一声惨绝人寰的尖叫撕裂了夜空，伴随着骨骼撞击坚硬岩石的沉闷钝响。我飞奔至峭壁下方，"
            "塞尔登横尸于乱石丛中，颅骨粉碎。石楠草丛间还弥漫着浓烈的硫磺与磷化物气味。\n\n"
            "一阵轻微脚步声自雾中传来，斯台普吞手提马灯急匆匆拨开草丛——他满怀期待，以为倒在血泊中的正是亨利爵士！"
        ),
        choices=[
            Choice(
                id="h_confront_stapleton_now",
                text="当场撕下伪装，当面对质指控其杀人罪行！",
                target_node_id="ending_holmes_master_deduction",
            ),
            Choice(
                id="h_play_the_fool",
                text="假称这只是一场越狱犯失足坠崖的醉汉意外，将他诱入梅利琵晚宴法网。",
                target_node_id="holmes_merripit_dinner",
            ),
        ],
    )

    nodes["holmes_hut_interior"] = PassageNode(
        id="holmes_hut_interior",
        title="侦探的荒原庇护所",
        pov=POV.HOLMES,
        node_type=NodeType.BRANCH,
        content=(
            "我踏入史前石屋，立刻察觉到了外人留下的痕迹。布莱德雷香烟的余温尚未散尽，"
            "门前横石后潜伏着一个紧握左轮的熟悉身影——正是我的老朋友华生！\n\n"
            "我以愉快的招呼化解了他的戒备。我们彻夜梳理了全盘案情：被盗的鞋子、磷光制剂以及斯台普吞血统的最终证据。"
        ),
        choices=[
            Choice(
                id="h_hut_to_dinner",
                text="为明晚梅利琵宅邸晚宴布下苏格兰场致命杀局！",
                target_node_id="holmes_merripit_dinner",
            ),
            Choice(
                id="h_hut_to_mire_recon",
                text="连夜潜行，对大格林盆泥潭中的凶手密窟实施特种侦察。",
                target_node_id="holmes_mire_recon",
            ),
        ],
    )

    nodes["holmes_moor_ambush"] = PassageNode(
        id="holmes_moor_ambush",
        title="石屋外的机警识破",
        pov=POV.HOLMES,
        node_type=NodeType.BRANCH,
        content=(
            "我在乱石之后微笑着截住了试图绕后包抄的华生。"
            "‘相当出色的战术迂回，我的好华生，’我走出阴影笑道，‘不过在盯梢一名咨询侦探时，最好别踩碎脚下的枯石楠。’\n\n"
            "华生欣喜若狂地紧紧握住我的双手。潜伏帷幕就此拉开，反击的号角已经吹响。"
        ),
        choices=[
            Choice(
                id="h_ambush_to_dinner",
                text="向华生部署决战方案，集结警力赶往梅利琵宅邸外围布控。",
                target_node_id="holmes_merripit_dinner",
            ),
        ],
    )

    nodes["holmes_mire_recon"] = PassageNode(
        id="holmes_mire_recon",
        title="泥潭孤岛上的犬舍",
        pov=POV.HOLMES,
        node_type=NodeType.BRANCH,
        content=(
            "循着隐没在污泥中的柳木细枝，我涉足深不可测的大格林盆泥潭。在一座长满芦苇的荒凉泥炭孤岛上，"
            "残存着一座废弃锡矿工棚。在锈迹斑斑的铁链束缚下，一头混杂着寻血猎犬与马士提夫獒犬血统的庞然巨兽正呲牙低吼，凶残饥渴！\n\n"
            "在它的锁链旁，赫然扔着亨利爵士失窃的那只黑色旧皮鞋。"
        ),
        choices=[
            Choice(
                id="h_recon_to_dinner",
                text="悄然撤出，在行凶预定现场梅利琵宅邸外设网全歼！",
                target_node_id="holmes_merripit_dinner",
            ),
            Choice(
                id="h_recon_strike_now",
                text="不等凶手行动，即刻率领警力突击泥潭孤岛人赃并获！",
                target_node_id="ending_holmes_master_deduction",
            ),
        ],
    )

    nodes["holmes_merripit_dinner"] = PassageNode(
        id="holmes_merripit_dinner",
        title="梅利琵宅邸外的伏击",
        pov=POV.HOLMES,
        node_type=NodeType.ANCHOR,
        anchor_name="anchor_climax",
        content=(
            "苏格兰场的雷斯垂德警官已与华生和我并肩埋伏在距梅利琵宅邸五十码的花岗石低脊后。"
            "亨利爵士已与斯台普吞用罢晚膳，正孤身步入漆黑的荒原小径准备返程。\n\n"
            "然而自南面泥潭深处，一堵遮天蔽日的厚重白雾正如决堤般滚滚袭来，迅猛抹平了眼前的整条归途！"
            "再过五分钟，我们的射界将荡然无存！"
        ),
        choices=[
            Choice(
                id="h_hold_fire",
                text="原地隐蔽固守，屏息等待那头恶兽撞入近距有效火网！",
                target_node_id="climax_fog_advance",
            ),
            Choice(
                id="h_charge_forward",
                text="果断前插冲入浓雾，赶在恶犬扑咬前切入亨利爵士身前！",
                target_node_id="climax_fog_advance",
            ),
        ],
    )

    # --- STAPLETON (CN) ---
    nodes["stapleton_start"] = PassageNode(
        id="stapleton_start",
        title="梅利琵宅邸的毒网",
        pov=POV.STAPLETON,
        node_type=NodeType.ANCHOR,
        anchor_name="anchor_arrival",
        content=(
            "查尔兹爵士已长眠地下，正如我精密设计的那样，被猎犬的狂吠活活吓死在水松夹道栅门前。"
            "如今新继承人亨利爵士来到了德文郡。他只带了一个平庸迟钝的退役军医华生，而大名鼎鼎的福尔摩斯却在伦敦作茧自缚。\n\n"
            "一百万镑巨额遗产与巴斯克维尔庄园的古老荣耀近在咫尺。只要解决掉亨利，"
            "我便能以南美洲侨民凡德勒的身份，合法认领这片富庶的祖产！"
        ),
        choices=[
            Choice(
                id="s_scout_watson",
                text="手提捕蝶网，在格林盆泥潭边缘‘偶遇’初来乍到的华生医生。",
                target_node_id="stapleton_moor_stroll",
            ),
            Choice(
                id="s_check_hound",
                text="涉险潜入泥潭荒岛，检查恶犬的饥饿状态与气味记忆。",
                target_node_id="stapleton_check_hound",
            ),
        ],
        clues_discovered=["斯台普吞对巴斯克维尔百万遗产的法定继承主张"],
    )

    nodes["stapleton_moor_stroll"] = PassageNode(
        id="stapleton_moor_stroll",
        title="伪装温和的博物学家",
        pov=POV.STAPLETON,
        node_type=NodeType.BRANCH,
        content=(
            "我将谦逊和蔼的昆虫学者扮演得惟妙惟肖。为了让华生亲眼见识泥潭的恐怖，我冷漠地指着一匹泥足深陷的马驹在绝望嘶鸣中沉没。"
            "可就在此时，贝瑟尔竟如疯癫般从石楠中冲出！她误将华生当做亨利爵士，歇斯底里地发出预警！\n\n"
            "这愚蠢而叛逆的女人若敢毁掉我数年心血，我决不吝惜彻底剥夺她的自由。"
        ),
        choices=[
            Choice(
                id="s_chastise_beryl",
                text="闭门严惩贝瑟尔，彻底击垮她的反抗意图。",
                target_node_id="stapleton_beryl_control",
            ),
            Choice(
                id="s_charm_watson",
                text="对贝瑟尔的反常举动巧言掩饰，用沼泽植被学说引开华生注意力。",
                target_node_id="stapleton_deceive_watson",
            ),
        ],
    )

    nodes["stapleton_check_hound"] = PassageNode(
        id="stapleton_check_hound",
        title="泥潭锡矿里的巨兽",
        pov=POV.STAPLETON,
        node_type=NodeType.BRANCH,
        content=(
            "我轻车熟路地踩着隐秘草甸来到废弃锡矿棚。铁链哗哗作响，嗜血巨兽喉中翻滚着嗜杀的闷雷。"
            "我将亨利爵士那只带有浓重足部汗渍的黑色旧皮鞋死死按在它的鼻孔前，直到涎水湿透它的獠牙。\n\n"
            "石蜡磷光糊已经熬制完毕——无色无味，在黑夜中能释放出令迷信懦夫神智崩塌的幽蓝烈焰。"
        ),
        choices=[
            Choice(
                id="s_apply_phosphor",
                text="将发光磷糊浓墨重彩地涂抹在巨犬的吻部与眼窝四周。",
                target_node_id="stapleton_phosphor_prep",
            ),
            Choice(
                id="s_plan_dinner",
                text="返回梅利琵宅邸，亲赴庄园邀请亨利爵士参加最后的鸿门宴。",
                target_node_id="stapleton_invite_henry",
            ),
        ],
        clues_discovered=["已完成气味锁定与荧光涂饰的恶魔猎犬"],
    )

    nodes["stapleton_beryl_control"] = PassageNode(
        id="stapleton_beryl_control",
        title="囚禁叛逆的妻子",
        pov=POV.STAPLETON,
        node_type=NodeType.BRANCH,
        content=(
            "在锁死的寝室中，贝瑟尔泪流满面却目光坚定。她断然拒绝继续扮演胞妹替我诱惑亨利。"
            "‘杰克，你是一个地狱里爬出来的恶魔！’她尖叫道。\n\n"
            "那又何妨？一束结实的麻绳与一块毛巾足以买下整个夜晚的绝对安宁。在她吐露只字片语之前，一切都将尘埃落定。"
        ),
        choices=[
            Choice(
                id="s_bind_now",
                text="将贝瑟尔牢牢绑死在黄铜床柱上并堵住嘴唇，专心布置晚宴。",
                target_node_id="stapleton_bind_beryl",
            ),
            Choice(
                id="s_patrol_tors",
                text="在晚宴前巡视荒原花岗石岗，清除任何潜藏的不安定因素。",
                target_node_id="stapleton_search_tors",
            ),
        ],
    )

    nodes["stapleton_deceive_watson"] = PassageNode(
        id="stapleton_deceive_watson",
        title="试探华生医生的虚实",
        pov=POV.STAPLETON,
        node_type=NodeType.BRANCH,
        content=(
            "在梅利琵宅邸的午茶桌上，我试探性地打听福尔摩斯的近况。华生坚称大侦探正忙于伦敦的一桩公款侵吞大案。"
            "但他游移不定的眼神却屡次瞟向黑色岩岗方向。\n\n"
            "难道那些史前石屋中潜伏着来自伦敦的不速之客？午后我确曾注意到石堆中升起了一缕淡淡的青烟。"
        ),
        choices=[
            Choice(
                id="s_investigate_hut",
                text="携带卡宾枪登上山岗，清查史前石屋深处的秘密。",
                target_node_id="stapleton_search_tors",
            ),
            Choice(
                id="s_ignore_smoke",
                text="将其视作寻常放牧者或逃犯，毫不动摇地推进亨利爵士的晚宴刺杀计划。",
                target_node_id="stapleton_invite_henry",
            ),
        ],
    )

    nodes["stapleton_phosphor_prep"] = PassageNode(
        id="stapleton_phosphor_prep",
        title="地狱般的发光巨犬",
        pov=POV.STAPLETON,
        node_type=NodeType.BRANCH,
        content=(
            "发光膏料在黑暗中散发出幽绿而冰冷的光辉。在这废弃的泥潭矿棚里，这头猛兽犹如直接脱胎于但丁神曲中的幽冥守卫！"
            "没有任何凡人的心脏能经受得住这等魔怪迎面扑咬而不当场骤停！\n\n"
            "大局已定。只待亨利爵士踏入这片夜黑风高的无情原野。"
        ),
        choices=[
            Choice(
                id="s_phosphor_to_bind",
                text="锁闭矿棚，折回宅邸将贝瑟尔五花大绑彻底封口。",
                target_node_id="stapleton_bind_beryl",
            ),
        ],
    )

    nodes["stapleton_search_tors"] = PassageNode(
        id="stapleton_search_tors",
        title="岩岗上的一缕青烟",
        pov=POV.STAPLETON,
        node_type=NodeType.BRANCH,
        content=(
            "我举起野战双筒镜远眺黑色岩岗。在圆形石屋门前，一个小信使正在卸下新鲜面包与罐头。"
            "屋里住着一个极其冷酷、作息规律、纪律森严的人！\n\n"
            "倘若是伦敦来的暗探，就必须在今夜与华生合流之前彻底灭口！"
        ),
        choices=[
            Choice(
                id="s_hound_the_hut",
                text="夜间将恶犬引向石屋方向，率先拔除这颗致命钉子！",
                target_node_id="stapleton_attack_hut",
            ),
            Choice(
                id="s_proceed_with_henry",
                text="亨利爵士才是真正的遗产关键，不必节外生枝，按时赴宴！",
                target_node_id="stapleton_invite_henry",
            ),
        ],
    )

    nodes["stapleton_moor_night"] = PassageNode(
        id="stapleton_moor_night",
        title="追捕逃犯的黑夜",
        pov=POV.STAPLETON,
        node_type=NodeType.ANCHOR,
        anchor_name="anchor_convict",
        content=(
            "今夜原野上呼喊四起，华生与亨利正在山野围堵逃犯。我抓住这天赐良机，循着亨利皮鞋的气味放出了猎犬！\n\n"
            "巨兽在狰狞的花岗岩悬崖上将猎物逼上绝路，伴随着一声撕心裂肺的惊呼，一个人影坠落悬崖！"
            "我欣喜若狂地提着马灯上前验尸——然而横陈在泥泞中的，竟然是穿着亨利旧衣服的越狱犯塞尔登！"
        ),
        choices=[
            Choice(
                id="s_salvage_plan",
                text="痛斥失误，迅速遁入黑暗，赶在华生抵达前邀请亨利明晚赴宴弥补战机！",
                target_node_id="stapleton_invite_henry",
            ),
            Choice(
                id="s_panic_escape",
                text="恐惧暴露！带上金条潜入大格林盆泥潭密径仓皇出逃！",
                target_node_id="ending_stapleton_tragedy",
            ),
        ],
    )

    nodes["stapleton_attack_hut"] = PassageNode(
        id="stapleton_attack_hut",
        title="突袭石屋的伏击",
        pov=POV.STAPLETON,
        node_type=NodeType.BRANCH,
        content=(
            "我驱使发光恶犬扑向史前石屋。然而就在巨犬腾空的刹那，乱石堆中轰然爆出一声枪响！"
            "子弹贯穿恶犬前肩，怪物痛嗥着窜入荒原。而在浓烟散去之处，歇洛克·福尔摩斯手持左轮冷峻走出！"
        ),
        choices=[
            Choice(
                id="s_run_for_mire",
                text="掉头拼死狂奔，逃向大格林盆泥潭深处的绝命泥炭孤岛！",
                target_node_id="ending_stapleton_tragedy",
            ),
            Choice(
                id="s_surrender_holmes",
                text="弃械跪地，举手向神探福尔摩斯投降以求免死审判。",
                target_node_id="ending_stapleton_arrest",
            ),
        ],
    )

    nodes["stapleton_bind_beryl"] = PassageNode(
        id="stapleton_bind_beryl",
        title="紧锁门扉的晚宴准备",
        pov=POV.STAPLETON,
        node_type=NodeType.BRANCH,
        content=(
            "我强行将贝瑟尔拖上二楼阁楼，绳索深嵌进她的手腕，丝巾死死堵住了她的嘴。"
            "她眼眸中燃烧着刻骨仇恨，却再也吐不出半句预警之词。\n\n"
            "楼下沉重的门环响起，亨利·巴斯克维尔爵士已欣然踏入这致命的温床。"
        ),
        choices=[
            Choice(
                id="s_host_dinner",
                text="整理西服领结，挂上无比亲切温厚的笑容下楼迎接尊客。",
                target_node_id="stapleton_dinner_trap",
            ),
        ],
    )

    nodes["stapleton_invite_henry"] = PassageNode(
        id="stapleton_invite_henry",
        title="致命的晚宴邀请",
        pov=POV.STAPLETON,
        node_type=NodeType.BRANCH,
        content=(
            "亨利爵士欣喜若狂地接受了我前往梅利琵宅邸共进晚餐的邀请。他渴望见到贝瑟尔。"
            "我热情地劝说他在餐后独自步行穿过荒原返回庄园，‘德文郡干冽的夜风最能舒缓神经’。\n\n"
            "现在我必须赶在开席前彻底封死贝瑟尔的喉舌。"
        ),
        choices=[
            Choice(
                id="s_bind_beryl_now",
                text="立刻上楼将贝瑟尔结结实实捆绑封喉锁入阁楼！",
                target_node_id="stapleton_bind_beryl",
            ),
        ],
    )

    nodes["stapleton_dinner_trap"] = PassageNode(
        id="stapleton_dinner_trap",
        title="梅利琵宅邸的最后晚餐",
        pov=POV.STAPLETON,
        node_type=NodeType.ANCHOR,
        anchor_name="anchor_climax",
        content=(
            "晚餐顺利得无懈可击。亨利大口啜饮着波尔多红酒，仅仅对我托称贝瑟尔‘偏头痛发作’流露出一丝遗憾。"
            "夜里十点，他提起手杖告辞，独自踏入了漆黑空旷的原野。\n\n"
            "大格林盆泥潭正配合地吐出一片铺天盖地的惨白色浓雾——这道雾墙将窒息他的一切惨叫，并致盲任何可能的救援！"
            "我悄无声息地溜向后院，拔出了外屋的铁插销！"
        ),
        choices=[
            Choice(
                id="s_release_beast",
                text="推开厚重木门，放出全身烈焰滚滚的地狱巨犬追踪撕咬！",
                target_node_id="climax_fog_advance",
            ),
            Choice(
                id="s_switch_to_watson",
                text="【转换视角：切换至窗外岩石后隐蔽监视的华生医生】",
                target_node_id="watson_climax_vigil",
                pov_switch=POV.WATSON,
            ),
        ],
    )

    # --- CLIMAX & ENDINGS (CN) ---
    nodes["climax_fog_advance"] = PassageNode(
        id="climax_fog_advance",
        title="巴斯克维尔的猎犬现身",
        pov=POV.WATSON,
        node_type=NodeType.CLIMAX,
        anchor_name="anchor_climax",
        content=(
            "自那翻腾咆哮的白雾深处，传来了急促刺耳的爪甲踏地声与低沉欲裂的嗜血咆哮！"
            "突然间，跃破白雾帐幔的，竟是一头只能在但丁神曲最深噩梦中出现的恐怖巨兽！"
            "一头巨大如牛犊的纯黑猛犬，张开的大口吞吐着熊熊烈火，双眼跳动着诡异的蓝白磷火，整个吻部与额顶都勾勒在灼热的发光雾霭之中！\n\n"
            "亨利爵士发出绝望惨叫，仰面跌翻在草甸之上，巨兽凌空跃起，獠牙直指他的喉管！"
        ),
        choices=[
            Choice(
                id="climax_shoot_beast",
                text="福尔摩斯、华生与雷斯垂德同时扣动扳机，爆发出雷鸣般的轮番齐射！",
                target_node_id="ending_canon",
            ),
            Choice(
                id="climax_watson_shield",
                text="华生挺身飞扑而出，用自己的血肉之躯在恶犬身下护住亨利爵士！",
                target_node_id="ending_watson_heroic",
            ),
            Choice(
                id="climax_fog_blind",
                text="惨白的地表死雾瞬间遮蔽了准星，子弹全部盲目地擦空射入泥浆！",
                target_node_id="ending_stapleton_triumph",
            ),
        ],
    )

    nodes["ending_canon"] = PassageNode(
        id="ending_canon",
        title="正典结局：恶犬伏诛，泥潭吞没主谋",
        pov=POV.HOLMES,
        node_type=NodeType.ENDING,
        content=(
            "五颗左轮子弹如雷霆般尽数灌入了恶犬的胸腔与侧腹。在凄厉欲绝的濒死长嗥中，那头磷光怪物轰然栽倒在地，抽搐数下后彻底毙命。\n\n"
            "亨利爵士虽惊魂未定，却毫发无伤。我们踹开梅利琵宅邸顶楼的密门，解救了伤痕累累的贝瑟尔。"
            "她指着外面的绝地哭喊道：‘他逃向大格林盆泥潭深处的孤岛了！’\n\n"
            "翌日清晨，在达特沼地的秋阳下，我和华生循着残存的柳桩搜寻至泥潭中央。"
            "在散发着恶臭的黑浆之上，仅有一只亨利爵士失窃的旧黑鞋浮在水面。而杰克·斯台普吞留在世间的最后痕迹，"
            "仅仅是一个深深滑入冰冷油腻污泥中的鞋跟印。\n\n"
            "在那不见天日的大格林盆泥潭最深处，恶魔巨犬的主谋永远长眠于永恒的恶臭黑沼之下。"
        ),
        choices=[],
    )

    nodes["ending_watson_heroic"] = PassageNode(
        id="ending_watson_heroic",
        title="华生英勇制敌：医生的荣耀时刻",
        pov=POV.WATSON,
        node_type=NodeType.ENDING,
        content=(
            "在这生死攸关的千钧一发之际，我以当年阿富汗战场的豪勇挺身而出，将左轮枪管死死顶入巨犬满是磷火的咽喉，连开三枪将其当场击毙！\n\n"
            "瞥见浓雾中一道黑影狂窜，我飞身穷追不舍，在废弃采石场的悬崖死角，用枪口将两手空空的斯台普吞逼入绝境，"
            "直到气喘吁吁的福尔摩斯与雷斯垂德携手铐飞奔赶来！\n\n"
            "‘干得漂亮，华生！’福尔摩斯紧紧拍着我的肩膀，眼中闪烁着无上赞许，‘这不仅是勇气的杰作，更是大不列颠军医的至高荣誉！’"
            "巴斯克维尔的百年诅咒，就此在华生医生的枪火中化为尘埃！"
        ),
        choices=[],
    )

    nodes["ending_holmes_master_deduction"] = PassageNode(
        id="ending_holmes_master_deduction",
        title="福尔摩斯缜密推演：法网难逃",
        pov=POV.HOLMES,
        node_type=NodeType.ENDING,
        content=(
            "怀揣着被窃的旧皮鞋、化验出的磷光毒物配方以及南美领事馆调出的血缘证明，"
            "我在斯台普吞尚未及放出恶犬之前，便以无可辩驳的证据链当场剥夺了他的一切侥幸。\n\n"
            "雷斯垂德警官将冰冷的钢手铐狠狠铐在了斯台普吞的双腕之上。"
            "‘杰克·斯台普吞——或者说罗杰·巴斯克维尔，你因谋害查尔兹爵士及企图谋杀亨利爵士被捕了。’\n\n"
            "斯台普吞瘫倒在泥泞之中。两个月后的埃克塞特巡回审判庭上，如山铁证令全陪审团一致裁定绞刑。"
            "纯粹演绎推导的又一场完胜。"
        ),
        choices=[],
    )

    nodes["ending_stapleton_triumph"] = PassageNode(
        id="ending_stapleton_triumph",
        title="黑暗继承：斯台普吞的阴谋得逞",
        pov=POV.STAPLETON,
        node_type=NodeType.ENDING,
        content=(
            "汹涌的沼泽死雾彻底致盲了那群愚蠢的伦敦警察。他们的枪声在雾海中徒劳呼啸，子弹尽数没入泥潭草丛。"
            "当他们摸索至小径时，亨利爵士早已被恶犬撕心裂肺的烈焰幻象当场吓断了心脉，身上未留半分暴力伤痕。\n\n"
            "我吹出密哨召回巨犬，用泥浆洗净磷光，从容折回宅邸。德文郡验尸官再次作出了‘巴斯克维尔诅咒引发心力衰竭’的结论。\n\n"
            "半年之后，在巴黎繁华的林荫大道上，我以‘凡德勒先生’的身份，合法、完整地继承了巴斯克维尔庄园与一百万英镑巨款。"
            "这场博弈，我是最终赢家。"
        ),
        choices=[],
    )

    nodes["ending_stapleton_tragedy"] = PassageNode(
        id="ending_stapleton_tragedy",
        title="大格林盆泥潭吞噬一切",
        pov=POV.STAPLETON,
        node_type=NodeType.ENDING,
        content=(
            "极度的惊恐彻底击垮了我的理智。四周的枪声与警笛宛如鬼影重重，我不管不顾地扎入了浓雾翻滚的大格林盆泥潭。\n\n"
            "在白茫茫的雾幕中，我的右脚猛然踏空——没有踩中坚韧的草甸柳枝，而是深深陷进了冰冷、腐烂、深不见底的黑沼死泥！"
            "我拼死挣扎，却被那股沉重冰冷的巨大吸力拖向深渊。泥浆漫过了脚踝、膝盖、胸膛、最后是咽喉……\n\n"
            "我竭力向浓雾绝望惨呼，唯有荒原鸥鸟发出凄凉嘲弄的哀啼。恶臭的黑泥咕嘟冒出两串浊泡，大地复归死寂。"
        ),
        choices=[],
    )

    nodes["ending_stapleton_arrest"] = PassageNode(
        id="ending_stapleton_arrest",
        title="达特沼地的正义伸张",
        pov=POV.STAPLETON,
        node_type=NodeType.ENDING,
        content=(
            "在福尔摩斯冰冷的枪口与雷斯垂德清脆的警笛包围下，我彻底失去了拔枪的勇气，瘫软地弃械投降。"
            "恶犬中弹逃逸，贝瑟尔获救，我那自以为天衣无缝的宏大构想，在贝克街冰冷深邃的理智光芒下化作碎屑。\n\n"
            "囚车颠簸着开向埃克塞特重犯监狱。我最后一次回望达特沼地那灰黑色的险峻岩岗，"
            "等待着我的，将是漫漫寒冬尽头那座冰冷的绞刑台。"
        ),
        choices=[],
    )


    return StoryGraph(
        language="cn",
        title="巴斯克维尔的猎犬：多视角互动小说",
        author="阿瑟·柯南·道尔 著（多视角改编）",
        description=(
            "改编自柯南·道尔经典侦探杰作《巴斯克维尔的猎犬》，从贝克街221B第一章启程，"
            "可从华生医生、歇洛克·福尔摩斯以及凶手斯台普吞三大视角亲历这场迷案。"
        ),
        start_nodes={
            POV.WATSON: "watson_ch1_baker_street",
            POV.HOLMES: "holmes_ch1_baker_street",
            POV.STAPLETON: "stapleton_ch1_london",
        },
        nodes=nodes,
    )
