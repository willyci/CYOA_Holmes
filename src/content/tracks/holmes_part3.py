# src/content/tracks/holmes_part3.py
"""Sherlock Holmes Perspective: Chapters 11 through 14 (Expanded Novel-Length Edition).
Covers:
- Ch 11: The Inquest of Laura Lyons & The Reunion in the Stone Hut
- Ch 12: The Secret Revealed & Selden's Death upon the Moor
- Ch 13: The Ancestral Portrait of Hugo Baskerville & Fixing the Net
- Ch 14: The Ambush in the Fog & The Pursuit into the Great Grimpen Mire
"""

HOLMES_NODES_PART3 = [
    # -------------------------------------------------------------------------
    # Chapter 11: Part 1
    # -------------------------------------------------------------------------
    {
        "id": "holmes_ch11_part1_lyons",
        "ch_idx": 10, "part": 1,
        "title_en": "Chapter 11: The Man on the Tor (Part I: The Inquest of Laura Lyons)",
        "title_cn": "第十一章 岩岗上的人（上：击碎谎言与劳拉的泣诉）",
        "pov": "holmes", "type": "branch", "anchor": None,
        "clues_en": [
            "Confronted Laura Lyons in Coombe Tracey regarding her midnight letter to Sir Charles",
            "Produced documentary proof that Jack Stapleton is legally married to Beryl Garcia of Costa Rica",
            "Laura confessed: Stapleton dictated the letter, promised marriage, then forbade her from attending",
        ],
        "clues_cn": [
            "在库姆·特雷西打字事务所当面质询劳拉·里昂斯夫人，逼其招供致查尔斯爵士绝命信真相",
            "当场出示约克郡私塾档案与哥斯达黎加天主教婚书，证实斯台普吞与贝丽尔系合法夫妻",
            "劳拉痛哭招供：斯台普吞以许诺婚约为诱饵逼其写信，却在最后时刻严厉禁止其赴约，暗中纵犬行凶",
        ],
        "choices_en": [
            {"id": "h_ch11_p1_c1", "text": "Return across the moor to your stone hut to rendezvous with Watson.", "target": "holmes_ch11_part2_stone_hut"},
            {"id": "h_ch11_p1_c2", "text": "[Switch POV to Dr. Watson] See Watson investigating the prehistoric hut on Black Tor.", "target": "ch11_part2_stone_hut", "pov_switch": "watson"},
        ],
        "choices_cn": [
            {"id": "h_ch11_p1_c1", "text": "策马穿过暮色苍茫的荒原，返回黑色岩岗石屋与摸索而来的华生正面对决。", "target": "holmes_ch11_part2_stone_hut"},
            {"id": "h_ch11_p1_c2", "text": "【视角切换：约翰·H·华生】以华生医生的第一人称视角搜查神秘石屋并拔枪设伏。", "target": "ch11_part2_stone_hut", "pov_switch": "watson"},
        ],
        "content_en": """The market town of Coombe Tracey lay nestled in a sheltered coombe some five miles to the north-east of the moor. By two o’clock that afternoon, I had exchanged my rough frieze jacket for a clean suit of dark tweed and sat in the modest sitting-room of Mrs. Laura Lyons.

She was an extraordinarily handsome woman, with rich hazel eyes, dark curls piled upon a graceful neck, and a delicate, flushed complexion. Yet there was that in the set of her mouth and the nervous twitching of her fingers which betrayed a woman living under intolerable strain. When I introduced myself as an investigator looking into the death of Sir Charles Baskerville, a sudden spasm of terror flitted across her features.

“I have already told Dr. Watson everything that I know,” said she, holding her head high with defensive pride. “Sir Charles was an extraordinarily noble benefactor. He assisted me in establishing this typewriting business. I had no other relations with him.”

“Mrs. Lyons,” said I, leaning forward and fixing her with my cold, grey eyes, “you are playing with fire. The official inquest is one thing; a criminal investigation for murder is another. If you persist in falsehood, you may find yourself standing in the dock as an accessory before the fact to the murder of Sir Charles Baskerville!”

She blanched to the roots of her hair. “Murder? It was declared heart failure!”

“It was murder, madam. Cold, calculating, brutal murder. And you were the instrument employed to draw the victim to his slaughter.”

“No! No! As God is my witness, I swear I wished him no harm!”

“Then why did you write to him on the day of his death, begging him to meet you at the gate of the Yew Alley at ten o’clock at night?”

She buried her face in her hands, her shoulders heaving with dry, silent sobs. For several minutes the clock on the mantelpiece ticked loudly in the silence.

“I was desperate,” she whispered through her fingers. “My father had cast me off. My wretched husband in London threatened to return and claim my small earnings under the matrimonial law. I was told that if I could raise a certain sum of money, a legal divorce could be obtained. I appealed to Sir Charles’s chivalry.”

“And who suggested that you should appeal to him?”

She hesitated, her eyes darting towards the door. “A... a friend.”

“A friend named Jack Stapleton!” I thundered, striking the table with my palm.

She gasped and shrank back into her armchair as though I had struck her.

“Listen to me, Mrs. Lyons,” I continued, my voice sinking into an earnest, commanding cadence. “You imagine that Jack Stapleton loves you. You imagine that when you are free, he will make you his wife and restore you to society. You are clinging to a spider’s web woven across an open grave!”

“He loves me!” she cried passionately, her hazel eyes flashing through her tears. “He has sworn it a thousand times! He is unmarried; his sister Beryl lives with him—”

I reached into my pocket and drew forth a folded legal document, laying it flat before her eyes.

“This is an attested copy of the register of marriage from the Church of San Pedro in San Jose, Costa Rica, dated seven years ago. It records the union of Jack Vandeleur, formerly of York, with Senorita Beryl Garcia. And this second document is a prospectus of a private preparatory school in Yorkshire, featuring portraits of Mr. Vandeleur and his charming Latin wife.”

Laura Lyons stared at the papers. Her eyes dilated; her jaw fell slack; every drop of blood drained from her lips until she looked like a corpse carved in marble.

“His... his wife?” she choked. “Beryl is his wife?”

“Beryl is his lawful wife,” I answered pitilessly. “He has passed her off as his sister because an unmarried beauty is a far more effective decoy in his bloody schemes. He had promised to marry you, madam, while his wife sat in the next room listening to your shame!”

A terrible cry broke from the woman’s lips—a shriek of wounded pride, betrayed love, and murderous fury that would have chilled Stapleton’s soul had he heard it. She sprang to her feet, her hands clenched into fists, her eyes blazing like a fury’s.

“The villain! The monstrous, cowardly villain!” she gasped, trembling in every limb. “He used me! He used my agony to murder that saintly old man!”

“Tell me everything, Mrs. Lyons,” I said gently, drawing a chair towards her. “The law will protect you if you speak the truth.”

She sank back into her seat, weeping tears of bitter rage. “He dictated the letter, Mr. Holmes! Every word of it! He told me that Sir Charles would never grant an interview in daylight for fear of local gossip, but that if I pleaded for his help at the moor-gate, he would give me the funds for my divorce. And then—on that very afternoon—Stapleton came to this room. He told me that his pride would not permit another man to pay for my freedom; he swore that he would find the money himself; and he made me swear upon the Bible that I would not go near Baskerville Hall that night!”

“And you stayed away?”

“I stayed here in this room, thanking God for his noble generosity! And the next morning, when the news arrived that Sir Charles was dead... Stapleton came back. He stood where you are standing now, his face pale as paper, his eyes like two coals. He told me that if I ever breathed a syllable about that letter, the police would arrest me for murder, and that my silence was his only hope and mine!”

I rose and took my hat. “You have done your duty, Mrs. Lyons. You have placed the noose around the neck of Sir Charles’s assassin. Remain in this house; speak to no one; and remember that the law will soon settle your accounts with Mr. Jack Stapleton.”

I strode out into the market square, my heart bounding within my chest. The last missing link of the chain was welded! Now, across the darkening moor, my good Watson was waiting in my mountain lair!""",
        "content_cn": """库姆·特雷西集镇静静坐落在一处距离荒原东北方向约五英里、背风幽静的狭长峡谷深处。当天下午两点整，我换下了那身粗糙油腻的水手粗呢工装，换上了一套干净整洁的深色粗花呢常礼服，端坐在劳拉·里昂斯夫人那间陈设简朴的打字行起居室里。

这位年轻的妇人生得极其美艳动人，一双明艳动人的榛色大眼睛在纤巧秀美的鼻梁两侧顾盼生姿，浓密的深黑色卷发高高挽在优美白皙的天鹅颈上，白里透红的娇嫩面庞透着名门闺秀特有的高贵气质。然而，从她那微微紧抿的薄唇线条，以及十指在膝头神经质般不受控制的痉挛性抽动中，无一不暴露出这名可怜女子长期生活在何等令人窒息的精神重压之下。当我表明自己的侦探身份、并直截了当提及查尔斯·巴斯克维尔爵士的猝死惨案时，一道剧烈的绝望惊骇如电光般猛然从她的面庞上掠过！

‘我所知晓的一切，早已一五一十向华生医生全盘托出了，’她下巴高高昂起，极力维持着被逼入绝境时的最后自尊，‘查尔斯爵士是一位对我恩重如山的高尚长者。正是他仁慈出资帮助我开办了这家维持温饱的打字行。除此以外，我与他老人家绝无任何私下瓜葛！’

‘里昂斯夫人，’我身子微微前倾，那双冰冷彻骨的灰色鹰隼眼眸死死锁定了她的视线，‘你此刻正在玩火自焚！郡验尸法庭那场走过场的平庸听证会是一回事；而苏格兰场即将发起的蓄意谋杀刑事指控则是另一回事！如果你继续在虚假的谎言迷宫中顽抗，不出四十八小时，你就会作为谋害查尔斯·巴斯克维尔爵士的事前从谋重犯，被戴上手铐押上老贝利法庭的被告席！’

她脸上的血色在一瞬间褪得干干净净，惨白如纸：‘谋杀？！法医早已断定是心脏衰竭自然死亡！’

‘那是谋杀，夫人！一场精心策划、冷血残暴到了极点的蓄意谋杀！而你——正是凶手用来将那位善良老人诱入死地的一把淬毒凶刃！’

‘不！不！当着全能上帝的面，我敢对着自己的灵魂发誓，我绝无半点谋害爵士的歹念！’

‘既然如此，你为何在查尔斯爵士遇害当天的清晨，用急迫的语气给他写信，乞求他在午夜十点整私自守候在水松夹道的偏僻木门前赴约？！’

她发出一声窒息般的悲咽，双手掩面，两肩在剧烈无声的抽泣中颤抖如风中落叶。整座房间里，唯有壁炉架上发条座钟那单调沉闷的滴答声在死寂中回响。

‘我当时快要被逼疯了，’她透过指缝，声音沙哑微弱，‘我那顽固的父亲断绝了与我的一切骨肉亲情；而我在伦敦那个禽兽不如的恶棍丈夫，却公然写信威胁要回到德文郡，依据婚姻财产法强行剥夺我这家小店的所有微薄血汗收入！有人向我进言：只要我能筹得一笔高昂的法庭诉讼费，便能彻底斩断这段地狱般的婚姻，重获清白自由之身！在万般走投无路之下，我唯有向查尔斯爵士骑士般的仁慈孤注一掷！’

‘是谁暗中指使你向查尔斯爵士写信借钱的？’

她的呼吸一滞，眼神惊惶失措地飘向紧闭的房门：‘一……一位热心帮助我的至交挚友。’

‘一位名叫杰克·斯台普吞的“挚友”！’我猛地一掌拍在面前的橡木小茶几上，爆发出雷霆般的断喝！

她整个人剧烈战栗，发出一声短促的尖叫，身子如被重锤击中般重重撞在椅背上。

‘看着我，里昂斯夫人！’我的声音压得极低，却带着一种不容置疑的审判威权，‘你天真地坚信那个恶魔深爱着你！你痴心妄想着只要你办妥了离婚手续，他便会明媒正娶迎娶你过门，让你重回体面上流社会的怀抱！你此刻死死抓着的，是一根悬在万丈坟墓上方的剧毒蛛丝！’

‘他爱我！’她突然失控地尖叫起来，泪水如断线珍珠般从那双绝美的榛色眼眸中汹涌而出，‘他当着上帝的面对我发过一万次誓言！他是单身贵族；与他同住的只有他的亲妹妹贝丽尔——’

我冷笑一声，伸手探入大衣内侧口袋，取出一张折叠平整的加盖公章法律文书，狠狠拍在了她面前的茶几上！

‘这是七年前哥斯达黎加圣何塞圣佩德罗天主教堂正式登记造册的结婚公证书影印件！上面清清楚楚、白纸黑字地铭刻着原籍约克郡的杰克·范德勒先生，与当地名媛贝丽尔·加西亚小姐结为神圣夫妇的永恒契约！而这第二份文件，则是约克郡那所破产私塾的原始招生简章——上面印着范德勒先生及其“迷人的拉丁裔贤内助贝丽尔夫人”的半身肖像版画！’

劳拉·里昂斯的双眼死死黏在那些盖有朱红火漆印鉴的铁证文书上。她的瞳孔在刹那间放大到了非人的极限，下巴颓然脱落，整张脸上甚至连最后一丝生命的血色都彻底被抽空，整个人宛如一具由大理石雕琢而成的冰冷僵尸！

‘他的……妻子？！’她的喉咙里挤出了一阵近乎撕裂的破音，‘贝丽尔竟然是他的合法结发妻子？！’

‘正是他的结发妻子！’我毫不留情地用真理的利刃剖开脓疮，‘他之所以逼迫自己的妻子对外伪装成未婚胞妹，是因为一个待字闺中的异域绝色尤物，在他贪婪的血腥掠夺棋局中，是一张百试百灵的夺命王牌！当他用虚伪的海誓山盟哄骗你在信纸上写下绝命附笔之时，他的正牌夫人就在隔壁的房间里，冷眼旁观着你跳入他精心编织的死亡陷阱！’

一声令人脊背生寒、毛骨悚然的凄厉狂嚎，骤然从这位绝望美人的胸腔中爆发开来！那是一声混杂着至高自尊被践踏的剧痛、真挚爱情被背叛的绝望、以及滔天杀意复仇怒焰的尖啸！她霍然从椅子上一跃而起，两只粉拳捏得指节发白，眼底燃烧着宛如复仇女神般的熊熊烈火！

‘那个恶魔！那个灭绝人性的卑鄙懦夫！’她全身剧烈颤抖，牙齿咬得咯咯作响，‘他利用了我！他竟然利用我对自由的绝望渴望，亲手谋害了那位像圣徒一样仁慈无辜的老爵士！’

‘把全部实情交代出来，里昂斯夫人，’我温和地将木椅推到她身前，‘只要你向法庭吐露真相，大英帝国的法律必将成为你坚不可摧的庇护所。’

她无力地瘫软回椅背上，滚烫的泪水洗刷着她惨白的面庞。‘那封信全是他亲口逐字指使的，福尔摩斯先生！每一个字都是他逼我写的！他说查尔斯爵士为了避嫌，绝不肯在大白天登门给年轻女子送钱；唯有在深夜的偏僻栅门前私会，老爵士才会毫无顾忌地奉上那笔昂贵的离婚律师费！然而——就在当天下午四点！斯台普吞突然神色匆匆地闯进了我这间屋子！他向我信誓旦言地说他的绅士尊严绝不容许别的男人替我赎身！他发誓他已经亲自筹措到了这笔巨款，并逼着我手按《圣经》发下毒誓：当晚十点整绝不许踏进巴斯克维尔庄园半步！’

‘于是你便留在家里了？’

‘我当晚一直待在这间屋里，甚至在祷告中向上帝感激他那“高尚无私的慷慨”！直到第二天清晨，噩耗传来，查尔斯爵士倒毙在水松夹道……斯台普吞面无人色、双眼如血炭般再次闯了进来！他就站在你此刻伫立的位置，恶狠狠地威胁我说：一旦我敢向任何人吐露那封信的半个字，郡警察局就会立刻以谋杀罪将我逮捕绞死！他说我的绝对沉默，是他也是我唯一能活命的护身符！’

我站起身，优雅地戴上了软呢帽：‘你已经履行了作为守法公民的最高天职，里昂斯夫人。你刚刚亲手将绞刑架上的夺命绞索，套在了那个杀人恶魔的脖颈上！安心留在这间屋里，不要向任何乡邻透露半句风声；相信我——用不了多久，法律与正义就会彻底替你向杰克·斯台普吞清算所有的血债！’

我大步流星迈出打字事务所，推开厚重的橡木大门，秋日清澈凛冽的狂风迎面扑来，吹拂着我滚烫的胸膛。这条横跨数月的血腥杀人证据链，如今已被我彻底锻造合龙！而在那片暮色降临的苍茫荒原绝壁之上，我那忠诚勇敢的华生，此刻正严阵以待，守候在我们那座高耸的史前石峰鹰巢之中！"""
    },

    # -------------------------------------------------------------------------
    # Chapter 11: Part 2
    # -------------------------------------------------------------------------
    {
        "id": "holmes_ch11_part2_stone_hut",
        "ch_idx": 10, "part": 2,
        "title_en": "Chapter 11: The Man on the Tor (Part II: “A Lovely Evening, Watson!”)",
        "title_cn": "第十一章 岩岗上的人（下：石屋对峙与故友重逢）",
        "pov": "holmes", "type": "anchor", "anchor": "anchor_man_on_tor",
        "clues_en": [
            "Returned to Black Tor to find Watson lying in ambush inside the stone hut with cocked revolver",
            "Greeted Watson with the iconic: “A lovely evening, my dear Watson!”",
            "Synthesized dossiers: Beryl’s true identity as Stapleton’s wife and the Laura Lyons trap",
        ],
        "clues_cn": [
            "黄昏返回黑色岩岗，敏锐察觉史前石屋内残留布拉德利卷烟气息与华生伏击痕迹",
            "在夕阳熔金的花岗岩门洞前从容道出经典问候：‘真是个可爱的黄昏，我亲爱的华生！’",
            "两名老战友在石屋内会师：将劳拉绝命信口供与斯台普吞假兄妹真夫妻的铁证彻底合龙",
        ],
        "choices_en": [
            {"id": "h_ch11_p2_c1", "text": "Compare dossiers and reveal the master plot to Watson before tragedy strikes.", "target": "holmes_ch12_part1_revelations"},
            {"id": "h_ch11_p2_c2", "text": "[Switch POV to Jack Stapleton] Discover Stapleton preparing the fatal scent on the moor.", "target": "stapleton_ch11_part2_setting_scent", "pov_switch": "stapleton"},
        ],
        "choices_cn": [
            {"id": "h_ch11_p2_c1", "text": "在石屋昏黄烛光下向华生彻底复盘全案因果，迎接荒原惨剧爆发前的致命倒计时。", "target": "holmes_ch12_part1_revelations"},
            {"id": "h_ch11_p2_c2", "text": "【视角切换：杰克·斯台普吞】窥视凶手在沼泽小径上用旧靴铺设气味追踪线的恶毒步骤。", "target": "stapleton_ch11_part2_setting_scent", "pov_switch": "stapleton"},
        ],
        "content_en": """The sunset was dying behind the western ridges of Dartmoor in a glory of blood-red and molten gold. A bitter, stinging frost was settling over the heather as I climbed the steep rock-chimney of Black Tor. My long walk from Coombe Tracey had left my limbs tired, but my spirit was soaring on wings of fire. Every piece of the puzzle had fallen into its appointed slot.

As I approached the low entrance of my stone hut, my nostrils caught a familiar, pungent whiff upon the evening breeze.

I stopped dead upon the rock shelf.

It was the delicate, fragrant aroma of a Turkish cigarette—imprinted with the brand of “Bradley, Oxford Street.”

I smiled in the darkness. There was only one man in the West of England who smoked Bradley’s cigarettes with that particular blend of Latakia and Virginia leaf.

“Watson has found me,” I thought with a throb of genuine affection. “The old bulldog has run me to earth at last!”

I stepped silently across the granite threshold. Inside, the shadows were thick as velvet. Across the earthen floor, on a flat slab of granite which served as my desk, lay my tin pannikin, a crust of bread, and a slip of paper scrawled in Cartwright’s hand: “Dr. Watson has gone to Coombe Tracey.”

And from the deepest recess of the stone wall came the sharp, unmistakable metallic click of a cocked Adams revolver!

“A lovely evening, my dear Watson!” I said quietly, leaning against the door lintel and striking a wax match.

A cry of pure, bewildered stupefaction broke from the shadows. The match flared yellow, illuminating my hooked nose, my tweed cap, and my laughing eyes.

There, crouching behind a boulder with his service revolver leveled straight at my heart, sat Dr. John H. Watson!

“Holmes!” he shouted, springing to his feet, his jaw dropping so low that his cigarette tumbled into the fern-bedding. “Holmes! Good God in heaven! Is it possible?”

“Never more possible, my dear fellow,” I answered, stepping inside and extending my hand. “And never more welcome!”

Watson seized my hand with a grip that nearly crushed my knuckles. For a moment, his honest, bronzed face was a battleground of conflicting emotions: first incredulous joy, then sharp, soldierly reproach, and finally an indignant flush of injured dignity.

“You have been here all the time?” he stammered, pointing a trembling finger at my blankets and my tin plates. “You were the Man on the Tor whom I shot at under the full moon? You let me believe you were in London? You let me write all those long, laborious reports—”

“Every line of which was of the most vital, supreme importance to me!” I interrupted warmly, clapping him on the shoulder. “Listen to me, Watson! You have every right to be angry, but before God, I tell you that my deception was the only weapon that could save Sir Henry’s life! If you had known I was here, your loyalty to me would have betrayed you. A glance, an altered tone of voice, a hesitation in your step—and Jack Stapleton would have known that Sherlock Holmes was upon the moor! The spider would have retreated into the depths of the bog, and we should never have caught him red-handed!”

Watson looked into my eyes, and the anger melted from his honest countenance like mist before the sun.

“You caught him?” he asked, his voice hushed with awe.

“I have him in the palm of my hand!” I declared, seating myself beside him on the heather bedding. “Listen, Watson: Beryl Stapleton is not his sister—she is his wife! Laura Lyons was the decoy who lured Sir Charles to his doom! And Jack Stapleton is none other than the son of Rodger Baskerville—the rightful heir to the title and the £740,000 fortune!”

Watson gasped, staring at me in the gloom of the ancient hut. And then, before he could utter another syllable...

A sound broke across the dark moor that froze the marrow in our bones!""",
        "content_cn": """夕阳在达特荒原西侧那起伏如巨浪的花岗岩山脊后缓缓沉没，将整片苍茫的天穹泼洒成一片由猩红与熔金交织而成的壮烈血海。刺骨的凛冽严霜随着夜风悄然降临在石楠荒原之上，而我正踏着轻快的步伐攀登黑色岩岗陡峭的石缝天梯。从库姆·特雷西村跋涉数英里而来的双腿虽感疲惫，然而我的灵魂却在胜利的狂喜烈焰中振翅高翔！

整座宏大阴谋的每一块散落拼图，如今都已被我严丝合缝地嵌入了它命定的凹槽！

然而，正当我猫着腰悄然接近史前石屋那道低矮的门洞时，清冽刺骨的晚风中飘来的一丝极其微弱的气味，猛然刺动了我的嗅觉神经！

我的脚步在一瞬间钉死在门外的花岗岩石台上。

那是一种极其清雅芬芳的特制土耳其卷烟香气——那是唯有在伦敦牛津街‘布拉德利’烟草行才能买到的高档拉塔基亚与弗吉尼亚混合烟丝！

在深邃的夜色中，我的嘴角缓缓绽放出一抹由衷的温暖笑意。在整个英格兰西部的广袤原野上，唯有一位正直高尚的英国绅士，才会随身携带着这种印有特定防伪标记的雅致卷烟！

‘华生终于循着蛛丝马迹找到我的巢穴了，’我在心底涌起一股深沉的战友挚情，‘这只忠诚执拗的老猎犬，到底还是把我给刨出来了！’

我悄无声息地迈过冰冷的花岗岩门槛。石屋内侧，浓稠如黑丝绒般的夜色笼罩了一切。在泥土地面中央那块充当书桌的平整花岗岩石板上，摆放着我的马口铁水壶、半块粗麦面包、以及卡特赖特用铅笔写下的一张字条：‘华生医生已前往库姆·特雷西’。

紧接着，在石壁最深邃的漆黑阴影深处，猛然爆发出了一声极其刺耳、清脆而决然的金属咬合声——那是一支军用阿达姆斯左轮手枪撞针被狠狠扳开、压上待发击铁的致命动静！

‘真是个可爱的黄昏，我亲爱的华生！’我倚着低矮的门框，神情自若地划燃了一根黄磷火柴。

一声混杂着极度惊骇与不可思议的失声狂呼，骤然从黑暗中炸裂开来！火柴的亮黄色火苗在黑暗中跳跃闪烁，清晰地照亮了我那标志性的鹰钩鼻、粗花呢鸭舌帽、以及嘴角噙着的那抹爽朗笑意。

只见在那块平整巨石后方的阴影里，一个黑洞洞的左轮手枪枪口原本死死指着我的心脏，而握着手枪蹲伏在地的，赫然正是约翰·H·华生医生！

‘福尔摩斯！’他失声大叫，整个人猛地从地上一跃而起，下巴惊得几乎掉在地毯上，原本叼在嘴角的半截卷烟‘啪嗒’一声滑落进了羊齿草堆里，‘福尔摩斯！天哪！我的上帝啊！这……这怎么可能？！’

‘绝无第二种可能，我最亲爱的朋友，’我微笑着大步迈入石屋，向他伸出了右手，‘而且，你的到访从来没有像今夜这般令人欢欣鼓舞！’

华生一把狠狠抓住了我的右手，其握力之大险些将我的指骨捏碎。在摇曳的火光下，他那张饱经风霜的古铜色硬汉面庞，在一瞬间化作了无数激烈情感交织的战场：起初是由衷的狂喜与宽慰，继而化作军人被蒙在鼓里的严厉责问，最终凝固成一种遭到挚友戏弄后的愤懑与委屈！

‘你一直都在这里？！’他用颤抖的手指指着我的行军毯、陶土烟斗和罐头盒，结结巴巴地质问道，‘你就是那个在满月下伫立在山巅、我开枪射击的岩岗幽灵？！你竟然让我一直以为你安然留在伦敦？！你竟然让我每天绞尽脑汁给你写那些长篇累牍的侦查密报——’

‘而你的每一封密报中的每一个字，都对我起到了无可估量、扭转乾坤的至高价值！’我一把按住他的肩膀，用力晃了晃，语气无比真挚而严肃，‘听我说，华生！你有权对我发火，但对着全能的上帝起誓，我的隐瞒是唯一能够保住亨利爵士性命的战略王牌！如果你知晓我就潜伏在侧，你对我的忠诚与敬意会在瞬间出卖你！你眼神的每一个微小变化、你语气的每一次细微波动、甚至你在碎石路上迈出的每一步步伐，都会在二十四小时内被狡诈如狐的斯台普吞洞若观火！那只剧毒的蜘蛛会立刻缩回泥潭的最深处，而我们将永远丧失在案发现场人赃俱获将他送上绞刑架的绝佳战机！’

华生深深地注视着我如烈火般灼灼的双眼，眼底的委屈与怒火如晨雾遇骄阳般彻底冰释融化。

‘你……你抓住那个幕后真凶了？’他以近乎敬畏的耳语急切问道。

‘他此刻已经稳稳落在我的手掌心之中了！’我拉着他在羊齿草毯上并肩坐下，压低声音道，‘听着，华生：贝丽尔·斯台普吞绝非他的亲妹妹——她是他的合法结发妻子！劳拉·里昂斯夫人正是那个被蒙在鼓里、将查尔斯爵士引诱至死亡栅门的无辜诱饵！而那个所谓的博物学者杰克·斯台普吞，他的真实身份——正是老查尔斯的亲弟弟罗杰·巴斯克维尔遗留在南美的亲生儿子！他是巴斯克维尔家族货真价实的合法继承人！’

华生倒吸了一口凉气，在石屋幽暗昏惑的阴影中难以置信地瞪大了双眼。

然而，还没等他来得及吐出下一个字……

一道撕裂夜空的恐怖凄厉惨叫，骤然在漆黑如墨的荒原绝壁上炸裂开来！"""
    },

    # -------------------------------------------------------------------------
    # Chapter 12: Part 1
    # -------------------------------------------------------------------------
    {
        "id": "holmes_ch12_part1_revelations",
        "ch_idx": 11, "part": 1,
        "title_en": "Chapter 12: Death on the Moor (Part I: The Cry on the Crags)",
        "title_cn": "第十二章 沼地的惨剧（上：峭壁惊魂与绝望悲鸣）",
        "pov": "holmes", "type": "branch", "anchor": "anchor_revelation",
        "clues_en": [
            "Synthesized the complete criminal architecture of Stapleton’s conspiracy",
            "A blood-curdling human scream of agony echoes across the rocky crags",
            "The deep, booming roar of the enormous hound shatters the midnight silence",
        ],
        "clues_cn": [
            "在石屋内向华生彻底复盘斯台普吞利用恶犬谋害亲族、夺取巨额遗产的完整作案逻辑",
            "一声充斥着濒死绝望与极度痛苦的人类凄厉惨叫，骤然从近在咫尺的花岗岩绝壁上传来",
            "凶兽狂暴嗜血的浑厚咆哮声如闷雷般在黑夜中隆隆回荡，宣告惨剧已然爆发",
        ],
        "choices_en": [
            {"id": "h_ch12_p1_c1", "text": "Sprint blindly through the darkness towards the cries of agony and hound roars.", "target": "holmes_ch12_part2_selden_death"},
            {"id": "h_ch12_p1_c2", "text": "[Switch POV to Jack Stapleton] See Stapleton releasing the phosphorescent beast.", "target": "stapleton_ch12_part1_screams_on_crags", "pov_switch": "stapleton"},
        ],
        "choices_cn": [
            {"id": "h_ch12_p1_c1", "text": "拔出手枪在乱石嶙峋的漆黑荒原上狂奔冲刺，直扑惨叫与恶犬狂吠处！", "target": "holmes_ch12_part2_selden_death"},
            {"id": "h_ch12_p1_c2", "text": "【视角切换：杰克·斯台普吞】窥视凶手在沼泽深处为恶犬涂抹发光磷药并纵犬扑杀的狂乱瞬间。", "target": "stapleton_ch12_part1_screams_on_crags", "pov_switch": "stapleton"},
        ],
        "content_en": """The cry that shattered the stillness of the Dartmoor night was unlike any sound I had ever heard in all my years in London. It was not a shout; it was a shriek of mortal agony, a long, bubbling scream of horror that rose into a shrill, piercing wail and then choked off in a terrible, suffocating gasp.

Watson and I leaped to our feet as though an electric current had passed through our bodies.

“What was that?” Watson gasped, his face as white as paper.

“The hound!” I shouted, catching up my heavy cudgel and drawing my loaded revolver from my belt. “Great God, Watson, run! Run for your life!”

We scrambled through the low doorway of the stone hut, plunging headlong into the pitch-black night. A dense mist was rising from the bog, and the moon was obscured by driving clouds. We could see scarcely ten yards ahead of us among the jagged boulders of the plateau.

And then the sound rose again.

It came from the high granite ridge to our left—a deep, booming, savage roar that seemed to tear the very air to ribbons. And beneath that monstrous baying, running through the darkness like the squeal of a tortured rabbit, came the frantic, panting gasps of a human being in flight!

“He has overtaken him!” I yelled, leaping over a deep fissure in the rock. “This way, Watson! For God’s sake, faster!”

We bounded across the rough heather like madmen. The stones were slippery with ice, and twice I fell heavily upon my knees, bruising myself against the granite, only to scramble up and dash forward again. My heart was pounding against my ribs like a sledgehammer.

“If Sir Henry has fallen,” I thought in a paroxysm of bitter self-reproach, “his blood is upon my head! I delayed; I calculated; I waited for complete legal proof—and while I spun my web, the monster has struck!”

Ahead of us rose the sheer granite precipice of Black Tor—a vertical wall of rock forty feet high, dropping sheer into a wild, boulder-strewn amphitheatre below.

As we reached the crest of the ridge, a final, blood-curdling yell of despair echoed up from the black gulf beneath our feet!

It was followed by the dull, sickening thud of a heavy body crashing against the rocks below—a sound of splintering bone and crushed flesh that turned my stomach sick. Then a long, low groan... and then, absolute, terrifying silence.

The baying of the hound had ceased. The moor was as still as a graveyard.

“He is dead,” whispered Watson, leaning against a crag, his chest heaving as though his lungs would burst. “We are too late, Holmes. Too late!”

“We must know the worst,” I said through my teeth. “Come, Watson. There is a path down the eastern gully.”

With our revolvers cocked in our hands, our thumbs resting upon the hammers, we picked our way down the steep rock chimney into the dark amphitheatre below.""",
        "content_cn": """那声撕裂了达特荒原死寂夜空的惨叫，完全不同于我在伦敦历经的所有谋杀现场所听闻过的任何声音。那绝非人类愤怒或求救的呼喊；那是一声由纯粹绝望与极致肉体痛楚撕扯出的濒死哀嗥——凄厉尖锐的惨嚎在山谷间疯狂爬升，旋即在一种窒息般咳血的咯咯声中戛然而止！

我和华生宛如遭受了高压电击般从羊齿草毯上霍然弹起！

‘那……那是什么声音？！’华生满脸煞白，声音剧烈颤抖。

‘是恶犬！’我厉声大吼，一把抄起手边的粗橡木手杖，另一手以雷霆万钧之势拔出了腰间的阿达姆斯左轮手枪，‘天哪，华生，跑起来！快跑！’

我们连滚带爬地钻出低矮的史前石屋门洞，一头扎入了伸手不见五指的漆黑荒野！浓密的夜雾正从泥潭边缘急剧升腾，暴风撕扯的浓云彻底遮蔽了月光。在周围那些如犬牙交错的花岗岩乱石堆中，我们的视野甚至不足十码！

紧接着，那道可怖的声响再度炸裂开来！

声音来自我们左侧高耸的花岗岩山脊——一声浑厚、狂暴、宛如远古巨兽般的地狱咆哮，几乎要将整片夜空撕成碎片！而在那恐怖长嗥的正下方，顺着夜风传来的，赫然是一个人类在黑夜乱石中亡命狂奔时那如同拉风箱般急促绝望的喘息声与碎石崩裂声！

‘它追上他了！’我一边飞跃过一道深达数英尺的岩石裂隙，一边声嘶力竭地狂吼，‘这边，华生！看在上帝的份上，再快点！’

我们二人宛如发了狂的野兽般在崎岖坎坷的石楠丛中拼命冲刺。冰冷的冻霜让每一块花岗岩都湿滑如油，我两次重重地单膝砸在坚硬的乱石上，膝盖被撞得鲜血淋漓，却根本顾不上疼痛，连滚带爬地再次向前狂奔！我的心脏宛如一柄疯狂擂动的铁锤，重重砸击着我的肋骨。

‘如果倒下的人是亨利爵士，’一股前所未有的剧烈自责与悔恨如毒药般噬咬着我的理智，‘那么他的鲜血就将彻底溅在我的手上！我算计得太深了！我权衡得太细了！我一心想要拿到无可辩驳的法庭铁证——然而就在我自鸣得意地编织罗网之时，恶魔却已然抢先下了杀手！’

在我们正前方，黑色岩岗那座高达四十英尺、直插云霄的花岗岩垂直绝壁骤然拔地而起，绝壁下方是一片布满锋利崩塌巨石的巨大深谷！

就在我们狂奔冲上山脊绝顶的同一瞬间，最后一声撕裂肺腑、令人肝胆俱裂的凄厉绝望尖叫，自我们脚下的万丈深渊中轰然回荡而起！

紧接着，是一记沉闷、令人毛骨悚然的重物坠地撞击声——那是沉重的血肉之躯以惊人速度砸在锋利花岗岩巨石上发出的可怕闷响，伴随着骨骼寸寸碎裂的渗人破裂声！一声微弱悠长的垂死呻吟在风中滑落……旋即，整座荒原陷入了一片宛如停尸房般的死寂！

恶犬的咆哮停息了。整座荒原安静得如同千年的坟冢。

‘他死了，’华生瘫软在悬崖边缘的一块怪石旁，胸膛剧烈起伏，大口大口地喘着粗气，‘我们来晚了，福尔摩斯……我们彻底来晚了！’

‘就算是死，我也必须亲眼看到最坏的真相！’我咬牙切齿地从牙缝中挤出这几个字，‘走，华生！东侧裂隙有一条通往谷底的泄洪石道！’

我们二人双手紧紧平举着大口径转轮手枪，拇指死死扣住击铁，借着微弱的天光，沿着险峻湿滑的乱石峭壁，一步步向那片弥漫着死亡气息的黑色谷底摸索潜行！"""
    },

    # -------------------------------------------------------------------------
    # Chapter 12: Part 2
    # -------------------------------------------------------------------------
    {
        "id": "holmes_ch12_part2_selden_death",
        "ch_idx": 11, "part": 2,
        "title_en": "Chapter 12: Death on the Moor (Part II: The Fall of the Convict)",
        "title_cn": "第十二章 沼地的惨剧（下：囚徒之死与正面对决）",
        "pov": "holmes", "type": "branch", "anchor": None,
        "clues_en": [
            "Discovered body at base of cliff was dressed in Sir Henry’s distinctive ruddy tweed suit",
            "Turned corpse over: it was Selden the convict, who wore Sir Henry’s cast-off clothes given by Barrymore",
            "Hound followed the boot-scent on the clothing and drove the fugitive over the forty-foot precipice",
            "Stapleton emerged with a lantern expecting Sir Henry; Holmes bluffed, claiming to return to London tomorrow",
        ],
        "clues_cn": [
            "绝壁谷底的尸身赫然身披亨利爵士那套极其扎眼的红褐色粗花呢猎装",
            "翻开面容震惊发现：死者实为杀人犯塞尔登！他因身穿管家私赠的爵士旧衣而惨遭凶犬错认扑杀",
            "恶犬循着旧衣物上的体味气味狂追，迫使惊恐万状的逃犯在黑暗中失足坠落四十英尺绝壁粉身碎骨",
            "斯台普吞手持马灯如幽灵般现身现场，满心以为亨利暴卒；福尔摩斯从容示弱，谎称明晨即刻返回伦敦",
        ],
        "choices_en": [
            {"id": "h_ch12_p2_c1", "text": "Inspect the ancestral portraits at Baskerville Hall to uncover the physical link.", "target": "holmes_ch13_portrait"},
            {"id": "h_ch12_p2_c2", "text": "[Switch POV to Jack Stapleton] Experience Stapleton’s horror upon seeing Holmes beside the corpse.", "target": "stapleton_ch12_part2_confronting_holmes", "pov_switch": "stapleton"},
        ],
        "choices_cn": [
            {"id": "h_ch12_p2_c1", "text": "前往巴斯克维尔庄园检视古代家族肖像油画，寻找敲定血缘的铁证原画。", "target": "holmes_ch13_portrait"},
            {"id": "h_ch12_p2_c2", "text": "【视角切换：杰克·斯台普吞】窥视凶手提灯走向尸体、猛然撞见福尔摩斯如天神般伫立时的万丈恐慌。", "target": "stapleton_ch12_part2_confronting_holmes", "pov_switch": "stapleton"},
        ],
        "content_en": """At the base of the sheer granite precipice, wedged between two jagged slabs of fallen rock, lay a crumpled heap of dark clothing.

Watson reached it first. He struck a wax match, shielding the tiny flame with his cupped hand.

The light flickered across a pair of sturdy limbs twisted at an unnatural angle, a broken neck, and a coat of distinctive, ruddy-tinted Canadian tweed.

“Sir Henry!” Watson wailed, falling upon his knees, tears streaming down his face. “Oh, Holmes, it is Sir Henry! The noble, generous lad!”

A wave of black nausea swept through my mind. I sank down upon the wet stones, burying my face in my hands. In that terrible moment, all my intellectual vanity, all my cold pride in my own methods, seemed shattered beyond redemption. I had trifled with a living demon; I had played chess with a human life; and I had lost!

“Turn him over, Watson,” I whispered, my voice cracked and dry. “Let me look upon his face.”

Watson took the prostrate figure by the shoulders and turned the head towards the matchlight.

I struck a second match.

The light flared over the dead features. And in that instant, a cry of thunderous, ecstatic relief tore from my throat!

It was not Sir Henry Baskerville!

The face was broad, coarse, and brutal. The forehead was low and animal; the teeth were bared in a snarl of beast-like rage; and the matted black beard was caked with blood and mud!

“Selden!” I shouted, laughing like a madman, seizing Watson by the shoulders and shaking him until his teeth rattled. “It is Selden, the convict! It is the Notting Hill murderer!”

Watson stared at the corpse, his eyes round as saucers. “Selden? But how in heaven’s name comes he to be dressed in Sir Henry’s tweed suit?”

“The clothes, Watson! The clothes!” I cried, tapping the tweed fabric with my fingers. “Don’t you remember Barrymore’s confession? Sir Henry gave his cast-off wardrobe to his butler, and Barrymore passed it to his starving brother-in-law on the moor! The stolen black boot! The scent! Stapleton gave the hound the scent of Sir Henry’s boots, loosed the monster upon the moor, and the beast ran down the tweed clothes, chasing this miserable wretch over the edge of the precipice!”

At that instant, a tiny yellow point of light appeared among the boulders two hundred yards to the east. A man was approaching through the rocks, carrying a swinging lantern.

“Hist!” I hissed, pulling Watson down into the deep shadow of the cliff. “The master of the hounds comes to view his kill! Keep your revolver ready, but let me do the talking!”

The footsteps crunching over the gravel drew nearer. The light of the lantern fell across the corpse. Behind it stepped Jack Stapleton.

He was breathing heavily, his pale, ferret-face flushed with triumphant excitement. He held the lantern aloft, leaning over the dead body.

“Sir Henry?” he whispered, gloating over the tweed suit. “Sir Henry Baskerville?”

“No, Mr. Stapleton,” I said, stepping calmly out from the shadow of the rock into the yellow circle of his lantern. “It is not Sir Henry. It is an unfortunate convict who has broken his neck upon the stones.”

The lantern dropped two inches in Stapleton’s grasp.

For five seconds, the man stood as though struck by lightning. His jaw dropped; his eyes started from his head; the blood drained from his cheeks until he looked more dead than the corpse at his feet! His gaze flicked from my face to Watson’s, and in that instant, I saw the sheer, unadulterated terror of a trapped beast flare in his eyes.

“Mr.... Mr. Sherlock Holmes!” he gasped, his voice cracking like a dry reed.

“At your service, sir,” I answered with a courteous bow. “I arrived from London this afternoon, just in time to witness this tragic accident.”

Stapleton recovered his nerve with a speed that did credit to his villainy. He forced a sickly, trembling smile onto his lips. “A... an accident, of course! A dreadful misstep in the dark! We heard screams from Merripit House, and I feared that young Sir Henry might have come to harm.”

“Sir Henry is dining at the Hall, perfectly safe,” said I smoothly. “Watson and I shall escort the body to the village morgue. Tomorrow morning, we must return to London to attend to pressing matters in Baker Street.”

Stapleton’s eyes gleamed with sudden, desperate hope. “You return to London tomorrow?”

“By the ten o’clock train,” I replied without blinking an eye. “Our mission here is concluded.”

The murderer bowed, his lantern shaking as he turned back towards Merripit House.

When his light had vanished into the fog, Watson turned to me, his brow furrowed in utter bewilderment. “Holmes! You told him we are leaving tomorrow? You are letting him go?”

“I have given him twelve hours of false security, Watson,” I whispered, my teeth bared in a feral grin. “He believes Sir Henry will be left entirely alone on the moor tomorrow night! Tomorrow, the trap closes. But first—to Baskerville Hall! We have an ancestral portrait to inspect!”""",
        "content_cn": """在那道笔直陡峭如刀削般的花岗岩垂直绝壁正下方，在两块巨大的坠石夹缝深处，扭曲地倒卧着一堆深色的人形衣物。

华生率先冲到了那堆衣物前。他迅速划燃了一根黄磷火柴，用颤抖的手掌死死护住微弱的火苗。

昏黄跳动的火光，照亮了一双呈现出极其可怖、完全违反人体生理结构的畸形扭曲双腿，一截彻底折断的颈椎，以及一件剪裁考究、质地精良、泛着极具辨识度红褐色光泽的加拿大粗花呢猎装！

‘亨利爵士！’华生发出一声凄厉至极的悲号，重重双膝跪倒在冰冷的碎石地上，热泪瞬间夺眶而出，‘哦，福尔摩斯！是亨利爵士啊！那个高尚、勇敢、慷慨的年轻人！’

一股排山倒海般的冰冷眩晕与剧烈干呕，瞬间席卷了我的整个大脑。我整个人无力地瘫坐在湿冷的乱石堆上，双手死死捂住了面孔。在那一刹那，我所有的智力虚荣、所有对我严密科学推理法则的自负与骄傲，仿佛在一瞬间被现实击得粉碎！我竟然在与一个活生生的地狱恶魔玩弄自鸣得意的智力游戏；我竟然拿一条年轻无辜的生命作为下注的棋子；而我——彻底输了！

‘把他的尸体翻过来，华生，’我的声音沙哑、干涩得宛如砂纸摩擦，‘让我最后看一眼他的面容。’

华生颤抖着伸出双手，抓住倒卧死者的宽厚肩膀，将那颗歪斜折断的头颅缓缓翻向火柴的微光。

我划燃了第二根火柴。

耀眼的火光在一瞬间照亮了死者那张沾满血污的面孔。而在看清那张脸的百分之一秒内，一声惊天动地、混杂着无尽狂喜与解脱的狂暴长啸，骤然从我的胸腔深处轰然炸响！

不是亨利·巴斯克维尔爵士！

那张面孔宽阔、粗鄙、凶蛮到了极点！前额极低，生着一双暴虐如野兽般的下吊眼，参差不齐的黄牙在临死前的狂怒咆哮中森森外露，而那满脸杂乱如草窝的大胡子上，厚厚包裹着风干硬化的黑泥炭与暗红色的脑浆！

‘塞尔登！’我大笑着从地上一跃而起，状若癫狂地狠狠抓住华生的双肩用力摇晃，‘是塞尔登！那个从普林斯敦监狱逃出来的诺丁山杀人狂魔！’

华生目瞪口呆地死死盯着地上的尸体，一双眼珠险些从眼眶里瞪出来：‘塞尔登？！看在上帝的份上，他怎么可能身穿亨利爵士这套独一无二的红褐色粗花呢猎装？！’

‘是衣服，华生！是衣服救了亨利爵士的命！’我激动得热血沸腾，指尖狠狠戳向死者身上的粗呢面料，‘难道你忘了巴里摩尔的招供吗？！亨利爵士入驻庄园后，将自己换下的旧衣服赏赐给了管家，而巴里摩尔转手就把这套昂贵御寒的猎装偷偷送给了在荒原上挨饿受冻的小舅子！那只在诺森伯兰饭店失窃的旧黑皮靴！那只浸透了亨利爵士汗液与体味的旧皮靴！斯台普吞让恶犬嗅了旧靴子的气味，在今夜纵犬搜山猎杀！恶犬在乱石中精准锁定了这套沾满爵士体味的红呢大衣，一路狂吠追杀，把这个可怜的替死鬼生生逼下了四十英尺高的万丈绝壁！’

就在这一瞬间，东侧两百码开外的怪石阴影深处，忽然亮起了一点摇曳晃动的昏黄灯光。一个人正手提防风马灯，脚踩碎石，鬼鬼祟祟地向深谷摸索而来。

‘嘘！’我发出一声毒蛇吐信般的极速低嘶，一把将华生扯入了绝壁下方浓重的石阴之中，‘恶犬的主人亲自赶来验尸了！握紧你的转轮手枪，但切记——一句话也别说，一切交由我来应对！’

碎石被踩碎的沉闷脚步声越来越近。马灯昏黄的光晕终于扫过了地上那具扭曲惨死的尸体。在灯光背后，赫然露出了杰克·斯台普吞那张泛着惨白冷光的尖削面孔。

他的呼吸沉重急促，眼神中翻滚着大仇得报、巨额遗产唾手可得时的狂乱狂喜！他将马灯高高举过头顶，贪婪而兴奋地俯身端详着那具红呢大衣尸体：

‘亨利爵士？’他的声音因极度的激动而发颤，贪婪地盯着那套衣服，‘亨利·巴斯克维尔爵士？’

‘不，斯台普吞先生，’我双手插在大衣口袋里，从容不迫地自巨石阴影中迈步而出，稳稳踏入了马灯的光圈正中心，‘很遗憾，这不是亨利爵士。这只是一位在黑夜中不慎失足坠崖、摔断了颈椎的可怜逃犯。’

斯台普吞手中的马灯猛地向下一坠，险些砸在地上！

在整整五秒钟的时间里，这个男人宛如被五雷轰顶般僵死在原地！他的下巴彻底脱臼般大张着，眼珠几乎要从眼眶里崩裂而出，脸上的每一丝血色在转瞬之间退得干干净净，惨白得甚至远比脚下那具死尸更加骇人！他的视线在我和华生身上来回疯狂扫射，在那一刹那，我清晰地目睹了捕兽夹猛然合拢时野兽眼中爆发出的纯粹绝望恐惧！

‘福……歇洛克·福尔摩斯先生！’他从喉咙深处挤出一声干涩如碎苇般的尖叫。

‘随时为您效劳，先生，’我极其优雅地欠身脱帽致意，‘我今天下午刚乘车从伦敦赶来，恰好有幸亲眼目睹了这场令人扼腕的意外惨剧。’

斯台普吞展现出了一名顶级罪犯所特有的惊人心理素质。在短短数秒内，他竟然强行将那抹滔天骇浪压回心底，脸上挤出了一抹比哭还要难看、剧烈抽搐的扭曲微笑：‘意外……当然，这真是一场可怕的意外！我们在梅立坪宅邸隐约听到了惨叫声，我还唯恐是年轻的亨利爵士在荒原上遭遇了不测。’

‘亨利爵士此刻正在庄园安然享用晚宴，毫发无损，’我语气波澜不惊，语调轻松得如同在谈论天气，‘我和华生医生待会儿便会将这具尸体移交村里的停尸房。明天上午，我和华生就必须搭乘头班早车返回伦敦，贝克街还有几桩要案急需我亲自坐镇。’

斯台普吞那双狭窄的死鱼眼里，瞬间迸发出一丝绝处逢生、几乎难以自持的狂喜毒焰！‘您……您明天上午就要返回伦敦？！’

‘乘十点整的早车，’我面不改色，连眼皮都未眨一下，‘我们在德文郡的调查已然彻底画上了句号。’

这个阴险的恶魔深深鞠了一躬，提着颤抖的马灯，步履仓皇地转身没入了漆黑的荒原夜色之中。

当那点微弱的灯光彻底消失在大雾深处之后，华生猛然转过身，满脸茫然与焦灼地质问我：‘福尔摩斯！你疯了吗？！你竟然告诉他我们明天一早就要离开？！难道你要眼睁睁放任这个杀人凶手逍遥法外？！’

‘我给了他整整十二个小时的致命安全错觉，华生，’在凛冽的高原寒风中，我嘴角咧开了一抹冷酷如恶狼般的森森狞笑，‘他坚信明天深夜，亨利爵士将孤身一人暴露在这座毫无戒备的荒原之上！明晚，终极陷阱就将彻底闭合！但现在——先跟我回巴斯克维尔庄园！那里有一幅至关重要的古代家族肖像油画，正等待着我们亲自过目！’"""
    },

    # -------------------------------------------------------------------------
    # Chapter 13
    # -------------------------------------------------------------------------
    {
        "id": "holmes_ch13_portrait",
        "ch_idx": 12, "part": 1,
        "title_en": "Chapter 13: Fixing the Nets (The Face of Hugo & The Fatal Dinner Invitation)",
        "title_cn": "第十三章 织网布阱（雨果画像的真容与绝命晚宴）",
        "pov": "holmes", "type": "branch", "anchor": "anchor_portrait",
        "clues_en": [
            "Concealed the wig and clothing of the 1647 Hugo Baskerville portrait to reveal Jack Stapleton’s face",
            "Confirmed Stapleton is the legitimate son of Rodger Baskerville, claiming the direct succession",
            "Instructed Sir Henry to accept Stapleton’s dinner invitation and walk home alone across the moor",
            "Secretly met Inspector Lestrade at Coombe Tracey station with an arrest warrant",
        ],
        "clues_cn": [
            "用双手遮挡1647年雨果·巴斯克维尔画像上的卷曲假发与服饰，赫然露出斯台普吞分毫不差的面容",
            "彻底坐实血缘铁证：斯台普吞实为查尔斯二弟罗杰的亲生儿子，系巴斯克维尔家族第三顺位直系血脉",
            "严令亨利爵士如期赴约前往梅立坪宅邸享用晚宴，并在夜深后务必孤身一人徒步穿越荒原小径返回",
            "与华生假意乘车离去，实则潜伏库姆·特雷西车站秘密迎接手持法庭逮捕令的苏格兰场雷斯垂德侦探",
        ],
        "choices_en": [
            {"id": "h_ch13_c1", "text": "Deploy the Scotland Yard ambush in the rocks near Merripit House.", "target": "holmes_ch14_part1_fog_ambush"},
            {"id": "h_ch13_c2", "text": "[Switch POV to Jack Stapleton] Discover how Stapleton prepared the final trap.", "target": "stapleton_ch13_fatal_dinner", "pov_switch": "stapleton"},
        ],
        "choices_cn": [
            {"id": "h_ch13_c1", "text": "率领雷斯垂德与华生在梅立坪宅邸外围的花岗岩乱石堆中设立终极伏击线。", "target": "holmes_ch14_part1_fog_ambush"},
            {"id": "h_ch13_c2", "text": "【视角切换：杰克·斯台普吞】窥视凶手在宅邸内捆绑妻子并点燃壁炉准备终极绝杀的疯狂举动。", "target": "stapleton_ch13_fatal_dinner", "pov_switch": "stapleton"},
        ],
        "content_en": """The great dining hall of Baskerville Hall was an imposing chamber paneled in blackened oak, beneath a high-raftered roof that echoed with the memories of three centuries. Above the dark wainscoting hung a long gallery of ancestral portraits—cavaliers in ruffs, roundheads in steel corselets, Georgian ladies with powdered coiffures, and judges in flowing scarlet robes.

After dinner, when Sir Henry had withdrawn to the library, I took a tall silver candelabrum and strolled down the length of the portrait gallery, holding the light close to the ancient canvases.

Watson followed behind, watching me with that curious, questioning expression which I know so well.

“A fine collection of ancestors,” he remarked.

“A most singular collection,” I replied, pausing before an oil painting dated 1647. It depicted a broad-shouldered gentleman with long, curled locks falling over a lace cravat, dressed in a black velvet doublet slashed with white silk. The face was pale, thin-lipped, cold, and arrogant.

“Who is that?” asked Watson.

“That, my dear fellow, is the cause of all our troubles. That is Hugo Baskerville—the author of the Hound.”

Watson stepped closer, peering at the cracked varnish. “A wicked-looking fellow, undoubtedly, but not unlike the others.”

“Watson,” said I, stepping back and holding the candle at arm’s length, “do you see nothing there? Look at the face. Do not look at the wide-brimmed plumed hat, nor the flowing Cavalier curls, nor the lace band. Look purely at the bone structure: the narrow, ferret jaw; the high cheekbones; the pale, cold, calculating eyes!”

I stepped forward, raised my two hands, and placed them over the canvas, covering the broad hat and the flowing ringlets.

Watson cried aloud in utter, thunderstruck astonishment.

“Great heavens!” he gasped, clutching my arm. “It is Stapleton! It is the face of Jack Stapleton!”

“Yes,” said I quietly. “The fellow is a Baskerville. That is the physical proof for which I have been seeking! He is the son of that younger brother, Rodger Baskerville, who fled to Central America after committing a crime and was believed to have died unmarried in Costa Rica. But Rodger left a son—this man Jack, who married the local beauty Beryl Garcia, stole a fortune in public funds, fled to England under the name of Vandeleur, established that failed school in Yorkshire, and finally tracked down his ancestral heritage here on the borders of Dartmoor!”

“And his motive?”

“The estate, Watson! The title and £740,000! With Sir Charles dead and Sir Henry murdered, this fellow, claiming the property through a distant branch in America, would walk into possession of the entire Baskerville fortune!”

I turned away from the portrait, my eyes flashing with the cold fury of the hunter.

The next morning, our counter-trap was sprung with surgical precision.

At breakfast, I announced to Sir Henry that pressing duties in London compelled Watson and me to depart immediately. Sir Henry was crestfallen, but I laid down my instructions with iron authority:

“You have accepted Mr. Stapleton’s invitation to dine at Merripit House tonight. You will go, Sir Henry. But mark this: you will send your carriage back. You will inform your host that you intend to walk home alone across the moor path at ten o’clock!”

“Walk alone in the dark?” cried the baronet. “After what happened to Selden?”

“You have placed your life in my hands, Sir Henry. Follow my instructions to the letter, and not a hair of your head shall be harmed.”

At nine o’clock that morning, Watson and I boarded the London train at Coombe Tracey station in full view of the stationmaster and several local villagers. But at the very next stop—the tiny country halt of High Barrow—we slipped out of our carriage, doubled back through the wooded valleys on foot, and met the fast express from London.

As the carriage doors opened, a dapper, wiry little gentleman in a tweed traveling suit and gaiters stepped onto the gravel platform, carrying a stout carpet-bag.

It was Inspector Lestrade of Scotland Yard!

“You have the warrant, Lestrade?” I asked, clasping his hand.

“Signed and sealed, Mr. Holmes,” the little detective grinned, patting his breast pocket. “Armed assault, attempted fraud, and murder. Where is our man?”

“He is at Merripit House, preparing a dinner for his guest,” I answered grimly. “And tonight, Lestrade, you shall assist at the most singular banquet ever served in the county of Devon!”""",
        "content_cn": """巴斯克维尔庄园那座宏伟的大宴会厅，是一处由通体乌黑的古老橡木护墙板包裹的森严殿堂。在高达数丈的古老原木人字梁穹顶下方，回荡着沉淀了整整三个世纪的名门回响。在深色的护墙板上方，悬挂着一整排长长的历代先祖油画肖像长廊——身披硬翻领的保皇党骑士、胸披精钢胸甲的圆颅党军官、高耸假发涂满香粉的乔治时代贵妇、以及身披猩红法袍的威严大法官。

晚宴过后，趁着亨利爵士告退返回图书室小憩的间隙，我手托一具沉甸甸的纯银高足五头大烛台，缓步穿行在这条幽暗深邃的油画长廊之中，将微弱的烛火贴近那些布满细密裂纹的古老画布。

华生紧随在我身后，用他那双写满了好奇与探寻的诚挚双眼注视着我的一举一动。

‘极其显赫的一门列祖列宗，’他随口感叹道。

‘一处蕴藏着惊天密码的非凡宝库，’我平静地回答，脚步最终在一幅落款为西元一六四七年的大幅油画前蓦然伫立。画布上绘制着一位身材魁梧、长发如黑色波浪般垂落在精美蕾丝领巾上的贵族绅士。他身披一件缀有白色丝绸暗纹的黑天鹅绒双排扣猎装，整张面孔苍白削瘦、嘴唇薄如刀刃，眉宇间流露出一股冷酷、傲慢且残忍至极的暴虐神采。

‘这位先人是谁？’华生凑上前问道。

‘这位，我亲爱的朋友，正是我们眼下经历的所有恐怖苦难的总源头。这位——就是那位著名的雨果·巴斯克维尔！那个招致魔犬诅咒的恶贯满盈之徒！’

华生又向前迈近了半步，隔着镜片端详着龟裂的松节清漆：‘确实生着一副十足的恶相，然而平心而论，与画廊里的其他几位先祖相比，倒也并没有显得格外异样。’

‘华生，’我向后退开两步，将银烛台平举至半空中，‘难道你当真没有看出任何端倪？看着那张脸！不要去看那顶饰有野鸡羽毛的宽檐阔帽，不要去看那些披散如瀑布般的保皇党大波浪卷发，更不要去理会那繁复华丽的蕾丝褶边！把你全部的注意力，纯粹聚焦在那张脸的骨骼解剖结构上：看那狭窄如雪貂般的尖下巴；看那耸立的高颧骨；看那双冰冷、死寂、宛如淬毒寒冰般的灰色眼眸！’

我大步上前，缓缓抬起双手，用两只展开的手掌严严实实地遮挡住了画布上方宽大的阔边软帽，以及垂落两侧的浓密假发。

华生在刹那间倒吸了一口凉气，从喉咙深处爆发出了一声近乎被五雷轰顶般的骇然尖叫！

‘天哪！全能的上帝啊！’他一把死死掐住我的小臂，失声狂呼，‘是斯台普吞！那是杰克·斯台普吞的面孔！’

‘是的，’我收回手掌，眼神冷冽如刀，‘那个恶魔体内流淌着纯正的巴斯克维尔家族之血！这就是我苦苦寻觅的最后一道血缘物理铁证！他正是老查尔斯那个在早年犯下重罪潜逃南美、相传在哥斯达黎加未婚早逝的三弟罗杰·巴斯克维尔留下的亲生儿子！罗杰在美洲留下了一脉骨肉——正是这位精通生物生理学的杰克。他迎娶了当地名媛贝丽尔·加西亚，侵吞了巨额公款潜逃回英国，改名范德勒开办了约克郡那所倒闭的私塾，并最终循着血脉的指引，将贪婪的目光死死锁定在了德文郡这片祖业荒原之上！’

‘他的终极目的？’

‘整座庄园，华生！世袭准男爵的无上荣耀，以及七十四万英镑的惊天巨资！只要老查尔斯突发心脏病暴毙，而唯一的侄儿亨利爵士也在这片被诅咒的荒原上死于非命，这个恶魔只需在遥远的南美伪造一套身份证明，便能以唯一的合法血脉旁系顺位继承人身份，光明正大地入主巴斯克维尔庄园！’

我猛然转身离开油画，眼眸中燃烧着猎手即将收网时的冷酷杀机。

次日清晨，一场精密宛如外科手术般的反猎杀大戏，在德文郡按部就班地轰然拉开了帷幕。

在庄园丰盛的早餐桌上，我当众向年轻的亨利爵士宣布：因伦敦有十万火急的机密要案催促，我和华生必须立即搭乘早班特快列车返回贝克街。年轻的爵士失望沮丧到了极点，然而我却以一种不容置疑的钢铁威权，向他下达了严苛的行动指南：

‘您今晚已然应允了斯台普吞前往梅立坪宅邸共进晚餐的邀请。您必须如期赴约，亨利爵士。但请您务必字字句句牢记我的叮嘱：抵达梅立坪后，您必须立刻打发您的马车独自返回庄园！您要当着斯台普吞的面明确告知他——您今夜打算在夜深十点之后，孤身一人徒步沿着荒原小径走回庄园！’

‘在漆黑一片的荒原上孤身徒步夜行？！’年轻的爵士失声惊呼，‘在昨夜那个越狱犯惨死之后？！’

‘您已经将您的性命完全托付到了我的手中，亨利爵士。只要您不折不扣地遵从我的每一条指令，我敢以歇洛克·福尔摩斯的名誉向您担保——您头顶的一根汗毛也绝不会受到任何伤害！’

当天上午九点整，我和华生在库姆·特雷西火车站当着站长与诸多乡民的面，大模大样地登上了开往伦敦的特快列车。然而，仅仅在列车驶出下一站——偏僻狭小的海巴罗乡村小站时，我和华生便迅速闪身跳下车厢，借着幽深的林间河谷徒步折返回秘密集结地。

就在正午时分，从伦敦疾驰而来的第二列快车在小站缓缓刹停。车厢门猛然弹开，一位身穿粗呢猎装、腿裹结实行军绑腿、手提厚重地毯布旅行手提包、身材精瘦敏捷的矮个子绅士，精神抖擞地踏上了站台的碎石地面。

正是苏格兰场的王牌刑警——雷斯垂德侦探！

‘拘捕令带来了吗，雷斯垂德？’我迎上前，有力地握住了他的手。

‘加盖了大理石法庭红火漆印鉴，福尔摩斯先生！’这位矮个子神探咧开嘴露出了一抹狡黠的快意笑容，拍了拍胸口沉甸甸的内袋，‘蓄意谋杀、诈骗、纵火以及非法持有杀伤性生物凶器！我们的目标在哪儿？’

‘他正在梅立坪宅邸，为他的贵客精心烹调一场绝命的断头晚餐，’我眼神阴鸷，声音冰冷如霜，‘而今夜，雷斯垂德——你将有幸亲眼见证一场全德文郡有史以来最惊心动魄的终极盛宴！’"""
    },

    # -------------------------------------------------------------------------
    # Chapter 14: Part 1
    # -------------------------------------------------------------------------
    {
        "id": "holmes_ch14_part1_fog_ambush",
        "ch_idx": 13, "part": 1,
        "title_en": "Chapter 14: The Hound of the Baskervilles (Part I: The Fire-Breathing Beast)",
        "title_cn": "第十四章 巴斯克维尔的猎犬（上：幽冥恶犬与迷雾伏击）",
        "pov": "holmes", "type": "branch", "anchor": "anchor_climax",
        "clues_en": [
            "Lurked with Watson and Lestrade in the rocks 50 yards from Merripit House",
            "A dense, blinding white fog rolled in from Grimpen Mire, threatening to blind the ambush",
            "Sir Henry stepped onto the moor path; an enormous, glowing phosphorescent hound burst from the mist",
            "Fired five rapid revolver rounds, killing the beast as it bore Sir Henry to the earth",
        ],
        "clues_cn": [
            "率领华生与雷斯垂德潜伏在梅立坪宅邸外五十码的花岗岩低洼乱石阵中设伏",
            "大格林盆泥潭深处翻滚起厚达数丈的白色浓雾，逐渐封锁了亨利爵士归途的荒原小径",
            "亨利爵士刚步入迷雾，一只通体喷吐幽蓝磷火、硕大如牛的黑色凶兽破雾咆哮扑杀而出",
            "在恶犬将爵士扑倒在地的千钧一发之际连开五枪，以五发实弹当场击毙魔犬救下爵士",
        ],
        "choices_en": [
            {"id": "h_ch14_p1_c1", "text": "Rescue the bound Beryl Stapleton and plunge into Grimpen Mire to pursue the murderer.", "target": "holmes_ch14_part2_mire_pursuit"},
            {"id": "h_ch14_p1_c2", "text": "[Switch POV to Jack Stapleton] See Stapleton’s panic as five gunshots ring out in the fog.", "target": "stapleton_ch14_part2_panic_flight", "pov_switch": "stapleton"},
        ],
        "choices_cn": [
            {"id": "h_ch14_p1_c1", "text": "破门营救被捆绑拷打的贝丽尔夫人，顺着秘密泥潭标桩直扑泥潭深处追捕元凶！", "target": "holmes_ch14_part2_mire_pursuit"},
            {"id": "h_ch14_p1_c2", "text": "【视角切换：杰克·斯台普吞】目睹恶犬中弹毙命、枪声大作、反派在极度恐惧中仓皇奔逃泥潭。", "target": "stapleton_ch14_part2_panic_flight", "pov_switch": "stapleton"},
        ],
        "content_en": """The night was cold, raw, and bitterly damp.

We lay crouched behind a low ridge of granite boulders fifty yards from the lighted windows of Merripit House. Lestrade was shivering beside me, his teeth chattering in the moorland chill, clutching his service revolver beneath his tweed coat. Watson lay upon my right, his eyes glued to the lighted dining-room window.

Through the uncurtained glass, the interior of the cottage was plainly visible. Sir Henry sat at the table, leaning back in his chair with a coffee-cup in his hand, chatting amiably. Across from him sat Jack Stapleton, smiling, gesturing, playing the genial host. But of Beryl Stapleton there was no sign.

“Where is the lady?” whispered Watson.

“She refused to be an accomplice to murder,” I muttered through my clenched teeth. “The brute has locked her away.”

At that moment, my eyes caught a white, creeping menace moving across the lower hollows of the moor.

From the Great Grimpen Mire, a dense, dense bank of white fog was rolling westward. It did not rise high into the air, but clung to the ground like a thick, impenetrable blanket of wool. It was creeping across the heather with terrifying speed, extinguishing the boulders, swallowing the sheep-paths, and advancing relentlessly towards the narrow strip of gravel path which Sir Henry must traverse on his journey home!

“Look!” I whispered, gripping Watson’s arm. “The fog! It is our only enemy!”

“It is creeping towards the path,” Watson muttered.

“In fifteen minutes it will have enveloped the house! We shall not be able to see our hands before our faces! If he comes out after the fog covers the path, we shall be blind!”

At that instant, the door of Merripit House opened. A bright rectangle of yellow light spilled out onto the dark gravel.

Sir Henry stepped out upon the threshold.

He paused for a second, looking up at the sky, pulling his overcoat closely around his chin. Then he strode out briskly along the path, his boots crunching upon the gravel. He passed within thirty yards of our hiding-place, his silhouette sharp and dark against the white wall of the advancing fog. He had scarcely vanished into the mist when a terrible sound froze the breath in our throats.

From the very heart of the rolling white fog bank came a patter—a swift, heavy, rhythmic pattering of paws upon the heather!

“Look out!” I yelled, springing to my feet. “It is coming!”

Lestrade gave a shriek of sheer, unadulterated horror and hurled himself face downward upon the turf. Watson gasped, raising his revolver.

Out from the dense wall of rolling white fog leaped a shape—a creature so appalling, so nightmarish, that for a fraction of a second my own thumb seemed paralyzed upon the hammer of my gun!

It was a hound of gigantic proportions—a monster coal-black as a mastiff, gaunt as a hound, with a head like an iron anvil. But it was not merely an enormous beast: from its gaping jaws burst a fire of smoldering, flickering flame! Its eyes glowed with dull, bluish embers; its muzzle, its lips, its jowls, and its arched hackles were outlined in a flickering, spectral light of hellish luminescence! Never in the delirium of fever had a mortal mind conceived anything more savage, more appalling, more demoniac than that dark form bounding through the fog!

With long, springy bounds, the glowing monster raced down the path straight towards the retreating form of Sir Henry!

I broke the paralysis that gripped my limbs. I raised my revolver, took deliberate aim at the glowing flank, and fired! Watson fired in the same split second!

A blood-curdling howl of agony broke from the beast. It had been hit! But it did not falter; with a furious snarl, it bounded through the heather and leaped straight upon the shoulders of Sir Henry Baskerville!

The young baronet went down beneath the weight of the monster with a cry of mortal terror, rolling upon the turf as the snapping, fiery jaws lunged for his throat!

I did not think; I did not feel. I ran like a cheetah across the forty paces of broken rocks, leaping boulders, my revolver leveled in my outstretched hand. The beast had pinned Sir Henry to the earth, its dripping, glowing fangs inches from his jugular vein.

I thrust the muzzle of my revolver straight against the monster’s ear and pulled the trigger five times in rapid, deafening succession!

A torrent of black blood and smoking tissue erupted into the air. The giant beast gave one final, convulsive shudder, rolled off Sir Henry’s body, thrashed its massive legs against the heather, and lay still upon the moor!

Sir Henry lay upon the turf, his eyes rolled back, white as chalk, having fainted from sheer horror. Watson rushed to his side, tearing open his collar, while Lestrade stood trembling like an aspen leaf, staring at the steaming carcass.

I dropped to one knee and touched the glowing muzzle with my naked fingertips. When I held my fingers up to my nose, there was no smell of burning flesh—only the cold, chemical odour of inorganic science.

“Phosphorus,” I said, wiping my hand upon my handkerchief. “A special, odorless preparation of phosphorus that does not destroy the scent. The brute was a master of his craft.”

Watson looked up from Sir Henry. “He is alive, Holmes! His heart is beating!”

“Thank God!” I breathed. “And now—for Jack Stapleton!”""",
        "content_cn": """夜色冰冷、阴湿、透骨生寒。

我们三人屏息潜伏在距离梅立坪宅邸透光窗户不足五十码开外的一道花岗岩低矮乱石阵背后。雷斯垂德紧挨在我身侧，牙齿在荒原的阴风中不受控制地剧烈打战，双手在粗花呢大衣下死死攥着他的转轮手枪。华生伏在我的右侧，目光如利刃般穿透夜幕，紧盯着那扇亮着昏黄煤油灯光的一楼大窗户。

透过未拉窗帘的玻璃，宅邸起居室内的景象一览无余。亨利爵士端坐在餐桌前，身子惬意地向后倚靠在椅背上，手中端着一杯冒着热气的咖啡，正神态自若地同主人谈笑着。坐在他对面的杰克·斯台普吞满面堆笑，双手在空中夸张地比划着，极力扮演着一位热情好客的乡村绅士。然而，整间屋子里却丝毫不见贝丽尔夫人的踪影。

‘那位夫人去了哪儿？’华生压低声音问道。

‘她拒绝成为这场血腥谋杀的共犯，’我从紧咬的齿缝中挤出这句断语，‘那个畜生已经将她秘密拘禁起来了。’

就在这千钧一发的紧要关头，我眼角的余光忽然捕捉到了荒原低洼处正悄然蔓延的一道致命白色阴影！

顺着大格林盆泥潭的方向，一片浓稠、厚重、宛如凝固羊毛般的惨白大雾，正贴着地面以惊人的速度向西翻滚蔓延！它并不向高空升腾，而是像一条巨大的白色巨蟒，贴着石楠荒原低矮的凹地极速滑行！它吞噬着一座座花岗岩巨石，抹平了沿途所有狭窄的羊肠小径，并且正以不可阻挡的势头，朝着亨利爵士今夜返回庄园必须途径的那条碎石小径疯狂逼近！

‘看！’我一把死死掐住华生的大臂，语气变得极其急迫严峻，‘浓雾！这才是我们今晚唯一的死敌！’

‘它正在吞没道路，’华生低呼。

‘不出十五分钟，整片荒原小径就将被这片白雾彻底吞噬！到时候我们连自己伸出的手指都休想看清！如果亨利爵士在大雾封路之后才走出大门，我们将彻底变成瞎子！’

仿佛是在回应我的焦虑，梅立坪宅邸的大门在这一瞬间‘吱呀’一声骤然推开了！一道耀眼的长方形黄色光柱瞬间撕破了门外的漆黑夜色。

亨利爵士大步迈上了门前的石阶。

他在门廊前停顿了片刻，抬头望了一眼漆黑的天空，将身上厚重大衣的风领紧紧立起、裹住下巴。紧接着，他迈着坚实的步伐踏上了碎石小径，脚下的皮靴在碎石上踩出富有节奏的喀嚓声响。他在距离我们伏击掩体不足三十码的距离从容走过，挺拔的身影在逼近的浓雾背景下呈现出清晰坚挺的黑色剪影。

然而，就在他刚走入那片翻滚白雾边缘的短短数秒之内——一声令人全身血液彻底冻结的声响，骤然从浓雾深处狂暴轰鸣而起！

自那堵翻滚狂涌的惨白雾墙正中心，传来了一阵急促、沉重、富有毁灭性节奏的巨爪蹬地声！

‘小心！’我猛地从巨石掩体后一跃而起，声嘶力竭地怒吼，‘它冲过来了！’

雷斯垂德从喉咙深处爆发出了一声近乎魂飞魄散的绝望尖叫，整个人吓得一头栽倒在草皮上！华生猛吸一口凉气，双手颤抖着平举起了左轮手枪！

从那堵翻滚狂暴的白色浓雾正中央，猛然破空扑出了一道令凡人理智彻底崩溃的恐怖凶兽！在看到它的百分之一秒内，我扣在手枪击铁上的大拇指，竟然因视觉遭受的极限震撼而陷入了短暂的神经麻痹！

那是一只体形庞大如小牛犊般的恶犬——通体漆黑如墨，有着马士提夫獒犬般坚硬如铁砧的宽阔头颅，以及猎犬般修长精悍的嗜血躯干。然而，最令人毛骨悚然的，是这只狂奔巨兽的全身！从它血盆大张的巨口与喉管深处，正疯狂喷吐着一团团明灭闪烁的幽蓝火焰！它的双眼宛如两枚深陷在白骨眼眶中的惨绿燃烧火炭；它的鼻吻、唇瓣、下颚垂肉、乃至背脊上根根倒竖的狂暴鬃毛，全都被包裹在一层跳跃闪烁、散发着地狱幽冥恶臭的惨绿荧光烈焰之中！凡间任何发高烧的疯汉在最荒诞的谵妄梦魇里，也绝不可能构想出比眼前这只在迷雾中踏火飞奔的狂暴恶魔更加狰狞可怖的怪物！

恶犬迈着巨大而富有弹性的狂暴步伐，如同一团燃烧的幽蓝彗星，沿着小径直扑正茫然回头的年轻亨利爵士！

我体内的神经麻痹在瞬间被狂暴的肾上腺素冲得粉碎！我双手稳稳托住枪柄，枪口死死套住那团疾驰的幽蓝火光，狠狠扣动了扳机！华生几乎在同一毫秒内同时鸣枪！

一声撕心裂肺的凶暴惨嚎骤然从恶犬口中爆裂开来！它中弹了！然而子弹并未能瞬间阻止这头狂兽的冲势；伴随着一声嗜血的狂怒咆哮，它借助惯性腾空跃起，庞大的身躯狠狠砸在了亨利爵士的后背上！

年轻的巴斯克维尔爵士在这股雷霆万钧的重压下发出一声绝望的惨叫，重重跌翻在泥泞的草皮上，而那张滴淌着绿色磷火与血腥涎水的森森利齿，已然狂暴地撕咬向他的咽喉！

我没有任何思考，没有任何权衡。我的身体如同一头在非洲草原上全速冲刺的猎豹，跨越了脚下嶙峋的花岗岩乱石，整个人凌空扑向了战团！恶犬已然将年轻的爵士死死按在爪下，尖锐的犬齿距离他的颈动脉仅剩最后一寸之遥！

我将阿达姆斯转轮手枪滚烫的枪口，狠狠顶进了这头巨兽的耳孔深处，食指如狂风骤雨般连续扣动了整整五次扳机！

伴随着五声震耳欲聋的剧烈轰鸣，一团混杂着黑血与脑浆的焦黑碎肉在火光中狂暴喷溅而出！那只庞大如怪兽般的恶犬爆发出一阵剧烈至极的濒死抽搐，庞大的身躯从爵士身上滚落，巨大的四肢在石楠丛中疯狂蹬动了几下，旋即轰然瘫软在地，彻底毙命！

亨利爵士面如白纸，双眼翻白，已然在极度的惊骇中彻底昏厥了过去。华生飞扑上前，迅速扯开他的衬衣领扣施救；而雷斯垂德则如秋风中的落叶般剧烈颤抖着，惊魂未定地死死盯着地上那具依旧冒着青烟的庞大残骸。

我单膝跪倒在巨犬的尸身旁，伸出右手食指，轻轻触摸着巨犬鼻吻处依旧散发着幽蓝微光的荧光涂层。我将指尖凑近鼻端嗅了嗅——没有皮肉烧焦的恶臭，唯有一股冰冷纯粹的现代无机化学制剂气味。

‘白磷化合物，’我掏出手帕仔细擦拭着指尖，冷冷地宣布，‘一种经过特殊除臭脱脂工艺调配的特制高粘性无味发光磷胶。它既能在夜色中散发骇人的幽冥冷火，又丝毫不影响恶犬灵敏的嗅觉追踪。我们的这位凶手，真不愧是一位卓越的生物化学大师。’

华生从亨利爵士身旁抬起头，满头大汗：‘他还活着，福尔摩斯！脉搏虽然微弱，但心脏还在有力跳动！’

‘谢天谢地！’我深深呼出了一口浊气，猛然站起身，目光如利剑般直刺梅立坪宅邸的大门，‘现在——该去彻底了结我们与杰克·斯台普吞的总账了！’"""
    },

    # -------------------------------------------------------------------------
    # Chapter 14: Part 2
    # -------------------------------------------------------------------------
    {
        "id": "holmes_ch14_part2_mire_pursuit",
        "ch_idx": 13, "part": 2,
        "title_en": "Chapter 14: The Hound of the Baskervilles (Part II: Sucked into Grimpen Mire)",
        "title_cn": "第十四章 巴斯克维尔的猎犬（下：泥潭追凶与深渊吞噬）",
        "pov": "holmes", "type": "branch", "anchor": "anchor_mire",
        "clues_en": [
            "Rescued Beryl Stapleton bound and gagged to an upright post in the locked upstairs bedroom",
            "Beryl revealed Stapleton fled into the Great Grimpen Mire to his secret tin-mine island refuge",
            "Discovered Sir Henry’s stolen black boot dropped along the submerged stake pathway in the mire",
            "Stapleton missed the submerged path in the blinding fog and was swallowed alive by the bottomless quagmire",
        ],
        "clues_cn": [
            "撞开梅立坪宅邸二楼暗门，解救被麻绳死死捆绑在承重木柱上、浑身遍布鞭痕的贝丽尔夫人",
            "贝丽尔泣血指认：斯台普吞在枪响后已发疯般逃向大格林盆泥潭深处的废弃锡矿孤岛据点",
            "在泥潭暗道边缘寻获亨利爵士此前在伦敦失窃、被用作恶犬追踪气味源的旧黑皮靴",
            "斯台普吞在浓密大雾中迷失了脚下暗桩的方位，失足坠入万劫不复的食人死沼，被彻底吞噬没顶",
        ],
        "choices_en": [
            {"id": "h_ch14_p2_c1", "text": "Ending: Holmes’s Master Deduction (Conclude in Baker Street with the complete retrospection).", "target": "ch15_holmes"},
            {"id": "h_ch14_p2_c2", "text": "Ending: Watson’s Heroic Chronicle (Celebrate Dr. Watson’s steadfast loyalty and bravery).", "target": "ch15_watson"},
            {"id": "h_ch14_p2_c3", "text": "Ending: The Complete Canonical Victory (Sir Henry restored, justice triumphantly served).", "target": "ch15_victory"},
            {"id": "h_ch14_p2_c4", "text": "Ending: The Dark Moor Tragedy (Contemplate the heavy toll exacted by the family curse).", "target": "ch15_tragedy"},
            {"id": "h_ch14_p2_c5", "text": "Ending: Sucked into the Mire (The grim retribution of the Great Grimpen Mire).", "target": "ch15_mire"},
            {"id": "h_ch14_p2_c6", "text": "Ending: The Old Bailey Trial (Lestrade’s court victory and the Exeter gallows).", "target": "ch15_arrest"},
        ],
        "choices_cn": [
            {"id": "h_ch14_p2_c1", "text": "结局：神探巅峰演绎（重返贝克街221号B壁炉旁，开启全盘案情深度回溯复盘）。", "target": "ch15_holmes"},
            {"id": "h_ch14_p2_c2", "text": "结局：华生英雄史诗（致敬华生医生的铁血忠诚与英勇无畏，载入探案纪实永恒正典）。", "target": "ch15_watson"},
            {"id": "h_ch14_p2_c3", "text": "结局：正义圆满昭彰（亨利爵士重获新生继承祖业，正义破晓降临达特荒原）。", "target": "ch15_victory"},
            {"id": "h_ch14_p2_c4", "text": "结局：荒原宿命悲歌（哀悼在阴谋诅咒中无辜陨落的生灵，叹息人性深渊的幽暗）。", "target": "ch15_tragedy"},
            {"id": "h_ch14_p2_c5", "text": "结局：沉沦万丈泥渊（泥潭吞噬恶魔的冷酷宿命，大自然对罪恶实施终极天谴裁决）。", "target": "ch15_mire"},
            {"id": "h_ch14_p2_c6", "text": "结局：老贝利正义审判（雷斯垂德携手警署铁证如山，埃克塞特绞刑架终结连环罪恶）。", "target": "ch15_arrest"},
        ],
        "content_en": """Leaving Watson to attend to Sir Henry, Lestrade and I dashed forward across the lawn towards Merripit House. The front door was wide open, flapping in the wind. We burst into the hallway, our revolvers ready, our boots thudding against the flagstones.

The house was dark, silent, and deserted. On the dining table, the coffee-cups were half-empty; in the parlour, the hearth was dying.

“Upstairs!” I shouted. “Follow me!”

We took the narrow wooden stairs three at a time. On the upper landing were three doors. Two stood open, revealing empty bedrooms. The third—at the rear of the house overlooking the great swamp—was locked and bolted with a heavy brass key from the outside.

I threw back the bolt, turned the key, and flung the door open, holding my revolver before me.

The sight that met our eyes made the blood boil in my veins.

Tied securely to an upright wooden post that supported the roof rafters was Beryl Stapleton. Sheets and towels had been wrapped around her body and bound with heavy cord, so tightly that the fibers were cutting into her flesh. A woolen scarf was gagged across her mouth, leaving only her dark, terrified eyes visible. Across her neck and bare arms were red, angry wheals—the unmistakable marks of a horsewhip where her brutal husband had lashed her before locking her away!

Lestrade sprang forward with his pocket-knife, slicing through the cords, while I drew the gag from her lips.

The woman collapsed into my arms, weeping hysterical tears of pain and gratitude.

“Is he safe?” she gasped, her voice broken and raspy. “Sir Henry—is he safe?”

“He is safe, madam,” said I, supporting her to a chair. “And the hound is dead.”

A shudder of relief passed through her bruised frame. “Thank God! Oh, thank God! The monster... he tied me here when I refused to help him lure Sir Henry into the fog! He whipped me... he swore he would return and take me across the sea once the fortune was his!”

“Where is he now?” I demanded, kneeling beside her. “Where has he fled?”

“To the mire!” she cried, pointing towards the window. “In the heart of the Great Grimpen Mire, upon a small island of dry peat, there are the ruins of an abandoned tin-mine. It was there that he kept the hound chained! He has a path marked with submerged willow stakes that only he can tread. If he reaches the island, he can hide there for weeks!”

I turned to Lestrade. “Guard the lady, Lestrade. Watson and I will finish this.”

At the first grey glimmer of dawn, the fog began to lift from the bog. Watson and I stood upon the edge of that quivering, emerald sea of mud. Beryl Stapleton, leaning upon Lestrade’s arm, pointed out the starting-point of the hidden trail: a small cluster of dry rushes marked by a rusted iron stake.

Holding long alder poles to test the mud before each step, Watson and I set out into the Great Grimpen Mire.

It was a journey across the threshold of hell. On either side of the narrow submerged path, the mud quivered like a living thing—black, viscous, bottomless. Every yard was fraught with mortal peril. The green slime rose and fell with a sickening, undulating rhythm, and the stench of decay was heavy in the morning air.

Fifty yards along the track, something dark caught my eye, half-submerged in a patch of green moss.

I reached out with the hook of my pole and fished it from the mud.

It was a heavy black leather boot, stamped inside with the maker’s mark: “Meyers, Toronto.”

“Sir Henry’s stolen black boot!” Watson ejaculated.

“The boot that gave the hound his scent,” I said, tossing it to the dry path. “He dropped it in his panic as he fled.”

We pushed forward another quarter of a mile into the dead heart of the mire. And then, at the base of a jagged ridge of black peat, the submerged willow stakes abruptly ended.

I stopped dead upon the shaking tussock. Before us stretched an unbroken expanse of oily, bubbling green slime, thirty yards wide, stretching towards the barren knoll where the stone ruins of the tin-mine stood.

Upon the very edge of the mud lay an object.

I leaned forward. It was Jack Stapleton’s green butterfly net, floating lightly upon the surface of the green moss. And beside it, sinking slowly into the black muck, was a single, frantic hand-print—the deep, gouged furrow where five human fingers had clawed desperately at the peat before being dragged down into the bottomless abyss!

Watson stared in horror at the bubbles bursting upon the slime. “He missed the path!” he whispered. “In the fog... he took a false step!”

I stood upon the trembling bog, leaning upon my pole, my eyes fixed upon that green, unbroken crust beneath which the body of the last evil Baskerville lay entombed in ten fathoms of liquid mud.

“Somewhere down in the dark heart of the Great Grimpen Mire,” said I solemnly, removing my hat, “down in the foul slime where the wild ponies die, lies the cleverest and most cold-blooded scoundrel that our modern age has produced. The swamp has claimed its own, Watson. Justice has been done!”""",
        "content_cn": """留下华生在草皮上悉心抢救昏厥的亨利爵士，我和雷斯垂德拔出武器，如离弦之箭般径直冲向了梅立坪宅邸的大门。房门在狂风中大敞着，门轴发出嘎吱的刺耳呻吟。我们二人双手平举手枪，皮靴在门厅冰冷的石板地面上踏出急促震耳的回响。

整栋小楼阴暗、死寂、空无一人。餐桌上，两只粗瓷咖啡杯里的残浆尚存余温；壁炉里的炭火正化为灰白的死灰。

‘上楼！’我厉声大喝，‘跟紧我！’

我们三步并作两步飞跨上狭窄的木质楼梯。二楼的回廊深处共有三扇房门，前两扇半敞着，露出空荡荡的简陋客房。而位于回廊最深处、正对着大格林盆泥潭方向的第三扇厚重木门，却从外侧被一根粗重的纯铜插销死死反锁着！

我大步上前，猛然拉开插销，一脚将沉重的木门狠狠踹开，枪口如闪电般率先探入屋内！

眼前浮现出的可怖一幕，在一瞬间让我全身的血液彻底沸腾！

在二楼这间低矮逼仄的杂物间正中心，整个人被粗麻绳死死捆绑在一根支撑屋顶的粗大承重木柱上的，赫然正是贝丽尔·斯台普吞夫人！厚重的床单与毛巾死死缠绕着她的身躯，粗糙的麻绳深陷进她的皮肉之中，几乎勒断了她的呼吸。一根粗羊毛围巾勒在她口中充当口塞，唯有一双布满血丝与泪水的绝望黑眸在乱发下剧烈战栗。而在她裸露的白皙颈项与手臂上，赫然纵横交错着数道皮开肉绽、鲜血淋漓的猩红鞭痕——那是那个禽兽不如的恶魔丈夫在逃跑前，用马鞭对她实施疯狂抽打拷问留下的残暴铁证！

雷斯垂德掏出折叠锋利的随身小刀，飞扑上前割断了紧绷的绳索，而我则轻柔地摘下了勒在她口中的粗毛巾。

在束缚解开的一刹那，这名遭受了无尽折磨的可怜女子整个人虚脱般滑倒在我的臂弯中，从喉咙深处爆发出了一阵夹杂着剧痛与解脱的嚎啕痛哭！

‘他……他平安吗？！’她顾不上喘息，用干涩沙哑到了极点的嗓音拼死抓住我的衣领，‘亨利爵士……他逃过那一劫了吗？！’

‘他安然无恙，夫人，’我小心翼翼地将她搀扶到一旁的木椅上，‘而那只地狱恶犬，此刻已经身中数弹、彻底毙命了。’

一股长长的战栗席卷了她遍体鳞伤的身躯。‘谢天谢地！全能的上帝啊！那个恶魔……当我坚决拒绝帮他把亨利爵士引向迷雾小径时，他发了疯般抽打我，把我死死绑在这里！他扬言只要那笔七十四万英镑的遗产到手，他就会带着这笔巨款强行把我掳去大洋彼岸的蛮荒异国！’

‘他现在逃向了何处？’我单膝跪在她身旁，语气如刀锋般迅疾严厉，‘快告诉我，他的逃亡路线究竟在哪儿！’

‘泥潭！’她用颤抖的手指死死指向窗外漆黑一片的死亡死沼，‘在大格林盆泥潭的最核心腹地，在一片被沼泽隔绝的干燥泥炭孤岛上，耸立着一座废弃数百年的古老锡矿石屋废墟！正是他在那里圈养驯化了那只恶犬！他在那片万劫不复的死沼泥浆下方，用深埋的秘密枯柳木桩铺设了一条唯有他一人知晓的暗道！只要让他逃上那座孤岛，他便能在那里凭借储备的罐头坚守数周之久！’

我霍然站起身，转头看向雷斯垂德：‘守在夫人身边寸步不离，雷斯垂德。最后的抓捕行动，由我和华生来彻底终结！’

拂晓时分，天际终于泛起了一抹惨白凄冷的鱼肚白，盘踞在泥潭上空的厚重迷雾开始逐渐稀薄飘散。我和华生手持长达十英尺的结实赤杨木探路长竿，伫立在了那片翻滚着幽绿毒光、令人望而生畏的无垠食人泥海边缘。在雷斯垂德的搀扶下，贝丽尔夫人为我们指明了那条绝密死径的唯一起始坐标：一丛插着生锈铁标的干枯芦苇丛。

每迈出一步，都必须用木竿狠狠探刺泥浆深处的硬底暗桩；我和华生就这样踏上了这条通往地狱深渊的狭窄独木桥。

这是一场在死神鼻息之下的惊险涉渡。在脚下不足一尺宽的湿滑暗桩两侧，深不见底的黑泥浆宛如活物般微微起伏蠕动，散发着令人作呕的强烈沼气与腐烂恶臭。稍有半寸的失足滑跌，便是万劫不复的灭顶之灾！

顺着暗桩前行了约五十码后，在一丛鲜艳翠绿的剧毒水藓边缘，一件半陷在烂泥中的深色物件猛然扯动了我的双眼。

我伸出探路木竿的铁钩，小心翼翼地将那个物体从黑泥中挑了出来。

那是一只沉甸甸的纯黑小牛皮短靴，鞋舌内侧用烫金字样清晰地印着加拿大制鞋商的名号：‘梅耶斯，多伦多’。

‘亨利爵士在伦敦失窃的那只旧黑靴！’华生失声惊呼。

‘正是凶手用来给恶犬记忆气味的真正死神引信，’我将靴子随手扔在脚下坚硬的岩脊上，‘他在极度仓皇的奔逃中，不慎将这件作案凶器遗落在了泥水里。’

我们二人强忍着泥浆的恶臭，顺着曲折蜿蜒的暗桩再度向泥潭腹心艰难推进了四分之一英里。然而，就在靠近一座突兀高耸的花岗岩黑色泥炭岩丘边缘时，脚下那些深埋在泥水中的枯柳暗桩——竟然突兀地彻底中断了！

我的脚步在剧烈颤抖的泥草墩上骤然刹停。在我们眼前，横亘着一片宽达三十码、表面泛着一层恶臭油光的平整翡翠色泥沼，而在那片死泥的对岸，隐约耸立着那座废弃锡矿的古老石墙残骸。

就在我们脚下这片烂泥的最边缘浮皮上，静静漂浮着一件微小的物件。

我倾身望去。那是杰克·斯台普吞随身不离的那只长柄绿色捕蝶网，正轻飘飘地浮在绿藓之上。而在那只捕蝶网身旁不足两尺处，一处正在被黑泥浆缓缓灌满的凹陷痕迹里，赫然印着一个深达数寸、手指极度张开拼命抓挠挣扎的绝望人类手印！

华生目瞪口呆地注视着泥浆表面不断冒出破裂的黑色沼气气泡，声音颤抖得宛如梦呓：‘他……他迷失了暗桩的方位！在大雾中……他踩空了！’

我拄着手中的赤杨木竿，静静伫立在这座颤抖起伏的食人死沼边缘，摘下头顶的软呢帽，目光深邃冷酷地注视着这片平整如镜、深达十丈的恐怖泥潭深渊。在这片幽冷沉寂的死水下方，那个自诩智力超绝的最后恶魔，已然被德文郡大地那冰冷无情的地底黑渊彻底吸入没顶，化作了千万年泥炭层深处的一缕尘埃。

‘在这座浩瀚广袤的大格林盆泥潭最冰冷、最漆黑的死泥深处，’在漫天初升的荒原晨光中，我对着苍穹发出了沉痛而庄严的终极裁决，‘在那些吞噬无辜生灵的万丈泥渊底下，长眠着我们这个现代社会所能孕育出的最聪明、也最残暴冷血的无耻恶棍。大自然已经收回了他欠下的血债，华生。正义——终于在这片被诅咒的荒原上，得到了最庄严的昭雪！’"""
    },
]
