"""English narrative content adapting 'The Hound of the Baskervilles' by Sir Arthur Conan Doyle.
Begins at Chapter 1 (221B Baker Street, London) and follows through to Dartmoor and the 6 endings.
Source: book_en.txt
"""

from src.models import Choice, NodeType, POV, PassageNode, StoryGraph


def build_story_en() -> StoryGraph:
    """Constructs the English StoryGraph starting from Chapter 1."""
    nodes: dict[str, PassageNode] = {}

    # =========================================================================
    # CHAPTERS 1-5: LONDON PROLOGUE (WATSON POV)
    # =========================================================================
    nodes["watson_ch1_baker_street"] = PassageNode(
        id="watson_ch1_baker_street",
        title="Chapter 1: Mr. Sherlock Holmes",
        pov=POV.WATSON,
        node_type=NodeType.ANCHOR,
        anchor_name="anchor_chapter1",
        content=(
            "Mr. Sherlock Holmes, who was usually very late in the mornings, save upon those not infrequent "
            "occasions when he was up all night, was seated at the breakfast table at 221B Baker Street. "
            "I stood upon the hearth-rug and picked up the stick which our visitor had left behind him the night before. "
            "It was a fine, thick piece of wood, bulbous-headed, of the sort known as a 'Penang lawyer'. "
            "Just under the head was a broad silver band nearly an inch across: 'To James Mortimer, M.R.C.S., from his friends of the C.C.H., 1884.'\n\n"
            "'Well, Watson, what do you make of it?' asked Holmes, his back turned to me. 'Since we missed him and have no notion "
            "of his errand, this accidental souvenir becomes of importance. Reconstruct the man by an examination of it.'"
        ),
        choices=[
            Choice(
                id="w_guess_hunt_club",
                text="Conclude that C.C.H. stands for a local hunt club, noting the worn iron ferrule and dog tooth-marks.",
                target_node_id="watson_ch2_mortimer",
            ),
            Choice(
                id="w_guess_hospital",
                text="Deduce from M.R.C.S. that C.C.H. refers to Charing Cross Hospital and a country practitioner.",
                target_node_id="watson_ch2_mortimer",
            ),
        ],
        clues_discovered=[
            "Penang-lawyer stick engraved: To James Mortimer, M.R.C.S., from his friends of the C.C.H., 1884",
            "Tooth-marks of a curly-haired spaniel",
        ],
    )

    nodes["watson_ch2_mortimer"] = PassageNode(
        id="watson_ch2_mortimer",
        title="Chapter 2: The Curse of the Baskervilles",
        pov=POV.WATSON,
        node_type=NodeType.BRANCH,
        content=(
            "Dr. James Mortimer entered our room—a tall, thin man with a prominent beak of a nose and two grey eyes behind gold-rimmed glasses. "
            "From his coat pocket he drew an old, yellowed manuscript dated 1742, recounting the terrible legend of wicked Hugo Baskerville "
            "and the foul demon hound that tore out his throat upon the moor.\n\n"
            "Then Mortimer laid before us the May 14 issue of the Devon County Chronicle detailing the sudden demise of Sir Charles Baskerville "
            "at the Yew Alley gate three months ago. Looking cautiously round the room, Mortimer lowered his voice to a trembling whisper:\n"
            "'Mr. Holmes, they were the footprints of a gigantic hound!'"
        ),
        choices=[
            Choice(
                id="w_ask_footprint",
                text="Cross-examine Mortimer on why he concealed the hound footprints from the public inquest.",
                target_node_id="watson_ch4_henry",
            ),
            Choice(
                id="w_ask_heir",
                text="Inquire about the arriving heir, young Henry Baskerville, landing at Waterloo from Canada.",
                target_node_id="watson_ch4_henry",
            ),
        ],
        clues_discovered=[
            "1742 Hugo Baskerville manuscript of the spectral hound",
            "Footprints of a gigantic hound found twenty yards from Sir Charles's body",
        ],
    )

    nodes["watson_ch4_henry"] = PassageNode(
        id="watson_ch4_henry",
        title="Chapter 4: Sir Henry Baskerville",
        pov=POV.WATSON,
        node_type=NodeType.BRANCH,
        content=(
            "The following morning brought Sir Henry Baskerville himself to Baker Street—a sturdy, fiery, dark-eyed gentleman of thirty, "
            "fresh from his farm in Canada. Upon his arrival at the Northumberland Hotel, an anonymous envelope had been delivered to him, "
            "containing words cut with short nail-scissors from yesterday's Times: 'As you value your life or your reason keep away from the moor.'\n\n"
            "More baffling still, Sir Henry reported that one of his brand-new tan boots had mysteriously vanished outside his hotel bedroom door!"
        ),
        choices=[
            Choice(
                id="w_follow_henry_regent",
                text="Accompany Holmes into the street to secretly shadow Sir Henry down Regent Street.",
                target_node_id="watson_ch5_london_spy",
            ),
            Choice(
                id="w_examine_letter",
                text="Examine the Times clipped newsprint under Holmes's magnifying lens for watermarks and perfume.",
                target_node_id="watson_ch5_london_spy",
            ),
        ],
        clues_discovered=[
            "Anonymous warning letter: 'As you value your life or your reason keep away from the moor'",
            "Stolen new tan boot at Northumberland Hotel",
        ],
    )

    nodes["watson_ch5_london_spy"] = PassageNode(
        id="watson_ch5_london_spy",
        title="Chapter 5: Three Broken Threads",
        pov=POV.WATSON,
        node_type=NodeType.ANCHOR,
        anchor_name="anchor_london_mission",
        content=(
            "Trailing Sir Henry down Regent Street, Holmes pointed out a hansom cab crawling along the curb. "
            "Through its side glass glared a passenger sporting a heavy black beard and sharp spectacles! "
            "When Holmes sprinted forward, the cab driver lashed his horse and vanished into Oxford Circus.\n\n"
            "At the hotel, another bizarre twist occurred: Sir Henry's missing tan boot was returned, but an old, worn black boot was stolen in its place! "
            "The cabman, John Clayton, came forward and testified that his passenger had brazenly declared: 'You may tell him that your passenger was Mr. Sherlock Holmes!'\n\n"
            "With the danger now acute, Holmes turned to me: 'Watson, there is deep water here. You must accompany Sir Henry to Baskerville Hall, "
            "guard him day and night with your service revolver, and report every fact to me!'"
        ),
        choices=[
            Choice(
                id="w_board_express",
                text="Pack your revolver and luggage, and board the Devonshire express train from Paddington with Sir Henry.",
                target_node_id="watson_start",
            ),
            Choice(
                id="w_review_clues",
                text="Review the stolen boots and cab mystery with Holmes before departing for Dartmoor.",
                target_node_id="watson_start",
            ),
        ],
        clues_discovered=[
            "Bearded spy in Cab No. 2704 who mocked Holmes",
            "Stolen old black boot saturated with Sir Henry's scent",
        ],
    )

    # --- WATSON AT DARTMOOR ---
    nodes["watson_start"] = PassageNode(
        id="watson_start",
        title="Chapter 6: Arrival at Dartmoor",
        pov=POV.WATSON,
        node_type=NodeType.ANCHOR,
        anchor_name="anchor_arrival",
        content=(
            "The train ground to a shuddering halt at the small Devonshire platform. "
            "Sir Henry Baskerville stepped onto the gravel, adjusting his tweed cap against the chill "
            "October wind that swept down from the desolate granite tors. Mounted soldiers with carbines "
            "patrolled the tracks; the notorious convict Selden has broken out of Princetown Gaol.\n\n"
            "Holmes has entrusted me with the guardianship of Sir Henry. As our wagonette rattles toward "
            "the gloomy twin towers of Baskerville Hall, the vast moor stretches ahead like a petrified ocean."
        ),
        choices=[
            Choice(
                id="w_to_hall",
                text="Proceed directly to Baskerville Hall to interview Barrymore the butler.",
                target_node_id="watson_baskerville_hall",
            ),
            Choice(
                id="w_to_alley",
                text="Inspect the perimeter of the Yew Alley where Sir Charles met his death.",
                target_node_id="watson_yew_alley",
            ),
            Choice(
                id="w_to_stapleton",
                text="Take a solitary walk along the edge of the moor toward Merripit House.",
                target_node_id="watson_meet_stapleton",
            ),
        ],
        clues_discovered=["Soldiers hunting Selden on Dartmoor"],
    )

    nodes["watson_baskerville_hall"] = PassageNode(
        id="watson_baskerville_hall",
        title="The Shadows of Baskerville Hall",
        pov=POV.WATSON,
        node_type=NodeType.BRANCH,
        content=(
            "Baskerville Hall is an imposing, shadowed pile of granite draped in ivy. "
            "Barrymore, the butler, received us with grave courtesy, yet his dark eyes flickered with "
            "restlessness. Later that night, muffled sobbing drifted from Mrs. Barrymore's chambers.\n\n"
            "I must uncover whether Barrymore is concealing a complicity in the curse, or if there is another "
            "thread to pull in Coombe Tracey where Sir Charles was known to receive letters."
        ),
        choices=[
            Choice(
                id="w_watch_barrymore",
                text="Mount a silent night watch in the long corridor to discover Barrymore's purpose.",
                target_node_id="watson_night_watch",
            ),
            Choice(
                id="w_visit_lyons",
                text="Hire a trap and ride to Coombe Tracey to interview Mrs. Laura Lyons.",
                target_node_id="watson_laura_lyons",
            ),
        ],
        clues_discovered=["Barrymore's nervous demeanor", "Weeping woman in the Hall"],
    )

    nodes["watson_yew_alley"] = PassageNode(
        id="watson_yew_alley",
        title="The Yew Alley and the Moor Gate",
        pov=POV.WATSON,
        node_type=NodeType.BRANCH,
        content=(
            "The Yew Alley is a gloomy corridor flanked by twelve-foot yew hedges. At the far end, "
            "a small wicket-gate opens upon the vast expanse of the moor. It was here that Sir Charles "
            "stood for some minutes, dropping cigar ash, before fleeing in blind panic.\n\n"
            "Dr. Mortimer's whisper echoes in my memory: 'Mr. Holmes, they were the footprints of a gigantic hound!' "
            "Beyond the gate, the path meanders toward the green quagmire of the Great Grimpen Mire."
        ),
        choices=[
            Choice(
                id="w_alley_to_mire",
                text="Follow the footpath outward into the moor toward Merripit House.",
                target_node_id="watson_meet_stapleton",
            ),
            Choice(
                id="w_alley_to_hall",
                text="Return to Sir Henry and prepare for the night watch in the west wing.",
                target_node_id="watson_night_watch",
            ),
        ],
        clues_discovered=["Cigar ash at wicket gate", "Footprints leading toward moor"],
    )

    nodes["watson_meet_stapleton"] = PassageNode(
        id="watson_meet_stapleton",
        title="The Naturalist of Grimpen Mire",
        pov=POV.WATSON,
        node_type=NodeType.BRANCH,
        content=(
            "A small, neat man with a butterfly net and tin botanical box hailed me. It was Jack Stapleton, "
            "naturalist of Merripit House. As we conversed, a distant brown pony wandered onto the bright green "
            "turf of the Great Grimpen Mire. Within seconds, it was dragged down into the mire's bottomless throat, "
            "vanishing with a mournful whinny.\n\n"
            "'A false step means death,' smiled Stapleton. Moments later, his sister, Miss Beryl Stapleton, hurried "
            "up. Mistaking me in the mist for Sir Henry, she whispered passionately: 'Go back! Go back to London instantly!'"
        ),
        choices=[
            Choice(
                id="w_interrogate_beryl",
                text="Pull Miss Stapleton aside and demand the reason for her desperate warning.",
                target_node_id="watson_beryl_warning",
            ),
            Choice(
                id="w_return_with_caution",
                text="Note her words, decline to press her in front of Jack, and return to the Hall.",
                target_node_id="watson_night_watch",
            ),
        ],
        clues_discovered=["Great Grimpen Mire treacherous paths", "Beryl's urgent warning"],
    )

    nodes["watson_beryl_warning"] = PassageNode(
        id="watson_beryl_warning",
        title="A Whispered Warning",
        pov=POV.WATSON,
        node_type=NodeType.BRANCH,
        content=(
            "When Miss Stapleton discovered I was Dr. Watson and not the Baskerville heir, her face turned pale. "
            "'Forget what I said,' she pleaded, though her eyes were wild with terror. 'My brother Jack must not know "
            "I spoke. But danger clings to every stone of this moor. If you love Sir Henry's life, take him away!'\n\n"
            "As dusk fell, my eyes caught a tall, solitary figure silhouetted against the rising moon atop the high "
            "pinnacle of Black Tor."
        ),
        choices=[
            Choice(
                id="w_beryl_to_watch",
                text="Return to Baskerville Hall to keep Sir Henry under close guard.",
                target_node_id="watson_night_watch",
            ),
            Choice(
                id="w_scout_the_tor",
                text="Climb toward the rocky tors to investigate the solitary watcher.",
                target_node_id="watson_stalk_figure",
            ),
        ],
        clues_discovered=["Figure on the Tor", "Beryl's terror of her brother"],
    )

    nodes["watson_night_watch"] = PassageNode(
        id="watson_night_watch",
        title="The Candle at the West Window",
        pov=POV.WATSON,
        node_type=NodeType.ANCHOR,
        anchor_name="anchor_convict",
        content=(
            "At two in the morning, Sir Henry and I crept down the corridor. Barrymore stood at the end window, "
            "holding a candle to the pane and peering into the moor. Confronted, he broke down: the signal was "
            "for Selden, the escaped convict, who is Mrs. Barrymore's wayward brother!\n\n"
            "Suddenly, from the black moor outside, rose a long, deep howl—a blood-freezing sound that swelled "
            "and reverberated through the night. It was neither hound nor wolf, but a shriek of unnatural malice."
        ),
        choices=[
            Choice(
                id="w_pursue_moor",
                text="Seize revolvers and plunge into the darkness with Sir Henry to hunt down the signal.",
                target_node_id="watson_moor_pursuit",
            ),
            Choice(
                id="w_track_watcher",
                text="Leave the convict to the police and track the mysterious watcher on the tor.",
                target_node_id="watson_stalk_figure",
            ),
        ],
        clues_discovered=["Barrymore signaling Selden", "The Hound's night howl"],
    )

    nodes["watson_moor_pursuit"] = PassageNode(
        id="watson_moor_pursuit",
        title="Pursuit Across the Tors",
        pov=POV.WATSON,
        node_type=NodeType.BRANCH,
        content=(
            "Cold rain stung our cheeks as Sir Henry and I scrambled over granite boulders. In the flash of a candle, "
            "we glimpsed the gaunt, savage face of Selden scurrying like an animal among the crevices. Sir Henry fired, "
            "but the convict vanished into the labyrinth of rocks.\n\n"
            "Looking up against the moonlit cloudbreak, I froze. High on the granite crag of the tor stood a second man—"
            "tall, thin, cloaked, his arms folded, watching the entire chase in motionless contemplation."
        ),
        choices=[
            Choice(
                id="w_follow_second_man",
                text="Ascend the steep crags toward the stone huts where the watcher made his lair.",
                target_node_id="watson_stalk_figure",
            ),
            Choice(
                id="w_switch_to_holmes",
                text="[Switch POV to Sherlock Holmes inside his moor redoubt]",
                target_node_id="holmes_hut_interior",
                pov_switch=POV.HOLMES,
            ),
        ],
        clues_discovered=["Man on the Tor confirmed cloaked and tall"],
    )

    nodes["watson_stalk_figure"] = PassageNode(
        id="watson_stalk_figure",
        title="The Prehistoric Stone Hut",
        pov=POV.WATSON,
        node_type=NodeType.BRANCH,
        content=(
            "I climbed to the ancient circular stone huts left by prehistoric Britons. Inside one, sheltered from the gale, "
            "lay a blanket, a loaf of bread, and a tin of tongue. On a flat granite slab lay a discarded cigarette stub—"
            "imprinted with 'Bradley, Oxford Street'—and a scrawled note: 'Dr. Watson has gone to Coombe Tracey.'\n\n"
            "A shadow fell across the entrance. A hand rested on the doorframe."
        ),
        choices=[
            Choice(
                id="w_wait_gun_drawn",
                text="Cock your service revolver and order the occupant to surrender.",
                target_node_id="watson_hut_reunion",
            ),
            Choice(
                id="w_flank_hut",
                text="Slip outside to catch the stranger from the blind side of the stones.",
                target_node_id="holmes_moor_ambush",
            ),
        ],
        clues_discovered=["Bradley cigarette stub", "Watson surveillance note"],
    )

    nodes["watson_laura_lyons"] = PassageNode(
        id="watson_laura_lyons",
        title="The Secret of Laura Lyons",
        pov=POV.WATSON,
        node_type=NodeType.BRANCH,
        content=(
            "In Coombe Tracey, Mrs. Laura Lyons sat trembling before me. Under relentless questioning, she wept and confessed: "
            "'It was Jack Stapleton who dictated the letter to Sir Charles, pleading for funds at the Yew Alley gate! "
            "Then, at the last minute, he forbade me from going, promising he would handle the matter himself.'\n\n"
            "The truth struck me like a blow. Stapleton had lured Sir Charles to the gate to unleash the beast!"
        ),
        choices=[
            Choice(
                id="w_lyons_to_hut",
                text="Race back to find the mysterious moor watcher who may hold the key to stopping Stapleton.",
                target_node_id="watson_hut_reunion",
            ),
            Choice(
                id="w_lyons_confront_stapleton",
                text="Ride directly to Merripit House to confront Stapleton before he strikes again.",
                target_node_id="watson_direct_confrontation",
            ),
        ],
        clues_discovered=["Stapleton orchestrated Sir Charles's midnight meeting"],
    )

    nodes["watson_hut_reunion"] = PassageNode(
        id="watson_hut_reunion",
        title="Reunion on the Moor",
        pov=POV.WATSON,
        node_type=NodeType.BRANCH,
        content=(
            "A dry, amused voice broke the tension: 'A lovely evening, my dear Watson. Really, you should not sit "
            "so close to the entrance; your shadow was visible from fifty yards away.'\n\n"
            "I lowered my revolver in astonishment. Sherlock Holmes stepped into the hut, lean, keen-eyed, and smiling! "
            "'I have been living on the moor, Watson, to see with my own eyes while Stapleton believed me in London. "
            "Now the net is closing. Stapleton is our man—and tonight Sir Henry dines at Merripit House!'"
        ),
        choices=[
            Choice(
                id="w_reunion_to_dinner",
                text="Coordinate the Scotland Yard ambush with Holmes outside Merripit House.",
                target_node_id="holmes_merripit_dinner",
                pov_switch=POV.HOLMES,
            ),
            Choice(
                id="w_take_vantage",
                text="Position yourself beneath the lighted dining-room window of Merripit House.",
                target_node_id="watson_climax_vigil",
            ),
        ],
        clues_discovered=["Holmes working incognito on Dartmoor"],
    )

    nodes["watson_direct_confrontation"] = PassageNode(
        id="watson_direct_confrontation",
        title="A Premature Encounter",
        pov=POV.WATSON,
        node_type=NodeType.BRANCH,
        content=(
            "I arrived at Merripit House alone. Stapleton met me in the hall, his smile tight and strained. "
            "From an outhouse across the yard came a deep, muffled growl that vibrated through the floorboards. "
            "Stapleton's hand slipped quietly toward his heavy walking stick.\n\n"
            "'You seem agitated, Doctor,' he said softly. 'Perhaps you would care to inspect my botanical specimens?'"
        ),
        choices=[
            Choice(
                id="w_force_outhouse",
                text="Demand to inspect the locked outhouse immediately.",
                target_node_id="watson_hound_early_release",
            ),
            Choice(
                id="w_feign_retreat",
                text="Feign an excuse about an urgent message from Sir Henry and retreat to signal Holmes.",
                target_node_id="watson_climax_vigil",
            ),
        ],
    )

    nodes["watson_climax_vigil"] = PassageNode(
        id="watson_climax_vigil",
        title="Vigil in the Moor Fog",
        pov=POV.WATSON,
        node_type=NodeType.ANCHOR,
        anchor_name="anchor_climax",
        content=(
            "I crouched beneath the dining room window of Merripit House. Through the parted curtains, "
            "I could see Sir Henry and Stapleton conversing over port. Stapleton checked his watch repeatedly.\n\n"
            "Outside, a creeping disaster was unfolding: a thick, white sea of fog was rolling in from the Great "
            "Grimpen Mire, swiftly burying the path that Sir Henry must take to return home. If the fog covers "
            "the path before Sir Henry passes, we cannot protect him!"
        ),
        choices=[
            Choice(
                id="w_signal_holmes",
                text="Signal Holmes and Lestrade on the ridge that the fog bank threatens the trap.",
                target_node_id="climax_fog_advance",
            ),
            Choice(
                id="w_storm_house",
                text="Burst through the dining room doors to extract Sir Henry before he walks outside.",
                target_node_id="ending_watson_heroic",
            ),
        ],
        clues_discovered=["Dense fog rolling over Grimpen Mire"],
    )

    nodes["watson_hound_early_release"] = PassageNode(
        id="watson_hound_early_release",
        title="The Beast Unleashed",
        pov=POV.WATSON,
        node_type=NodeType.BRANCH,
        content=(
            "Stapleton twisted the iron key. The heavy timber door flew back! Out sprang a creature from the pit: "
            "a colossal hound, black as coal, with fire licking from its gaping jaws and muzzle glowing with "
            "supernatural blue luminescence! It lunged straight at my throat!"
        ),
        choices=[
            Choice(
                id="w_stand_and_fire",
                text="Plant your boots, steady your arm, and fire every chamber into the monster's chest!",
                target_node_id="ending_watson_heroic",
            ),
            Choice(
                id="w_dodge_for_cover",
                text="Dive behind the low granite boundary wall as Holmes's rifle cracks from the ridge!",
                target_node_id="ending_canon",
            ),
        ],
    )

    # =========================================================================
    # CHAPTERS 1-5: LONDON PROLOGUE (HOLMES POV)
    # =========================================================================
    nodes["holmes_ch1_baker_street"] = PassageNode(
        id="holmes_ch1_baker_street",
        title="Chapter 1: The Science of Deduction",
        pov=POV.HOLMES,
        node_type=NodeType.ANCHOR,
        anchor_name="anchor_chapter1",
        content=(
            "Seated with my back to Watson at the breakfast table, watching his reflection in the polished coffee-pot, "
            "I listened to his well-meant analysis of Mortimer's Penang-lawyer walking stick. Watson is a splendid conductor of light; "
            "his very errors frequently illuminate the truth.\n\n"
            "Taking the cane to the window with my lens, the facts arranged themselves with mathematical precision: "
            "the thick iron ferrule worn down with rural walking; the 'C.C.H.' standing not for a hunt club, but for Charing Cross Hospital; "
            "the five-year-old date marking the departure of a young house-surgeon to rural Devonshire; and the canine tooth-impressions "
            "across the center of the wood denoting a creature larger than a terrier, smaller than a mastiff—a curly-haired spaniel. "
            "At that very moment, the bell rang, and through the window I saw the spaniel and its owner ascending our steps."
        ),
        choices=[
            Choice(
                id="h_welcome_mortimer",
                text="Welcome Dr. James Mortimer and invite him to state his grave consultation.",
                target_node_id="holmes_ch2_mortimer",
            ),
            Choice(
                id="h_examine_cranial",
                text="Allow Mortimer to marvel at your dolichocephalic skull while preparing your questions.",
                target_node_id="holmes_ch2_mortimer",
            ),
        ],
        clues_discovered=[
            "Mortimer: Charing Cross Hospital house-surgeon, now rural Devonshire practitioner",
            "Curly-haired spaniel confirmed at Baker Street threshold",
        ],
    )

    nodes["holmes_ch2_mortimer"] = PassageNode(
        id="holmes_ch2_mortimer",
        title="Chapter 2: The Problem of the Moor",
        pov=POV.HOLMES,
        node_type=NodeType.BRANCH,
        content=(
            "Dr. Mortimer laid before us the ancient curse of Sir Hugo and the mysterious demise of Sir Charles. "
            "While the public inquest deemed it heart failure, Mortimer revealed the crucial reality: twenty yards from the body, "
            "in the damp earth near the wicket gate, were the fresh pawprints of an enormous hound.\n\n"
            "Sir Charles had stood waiting at the gate for five to ten minutes, dropping cigar ash twice. Then he had run in terror "
            "down the yew alley, his tracks changing as he ran upon his tiptoes until his diseased heart burst.\n\n"
            "Young Sir Henry Baskerville lands at Waterloo from Canada in one hour. Should he be permitted to enter Dartmoor?"
        ),
        choices=[
            Choice(
                id="h_plan_regent_meeting",
                text="Direct Mortimer to meet Sir Henry and bring him to 221B tomorrow at ten o'clock.",
                target_node_id="holmes_ch4_regent_street",
            ),
            Choice(
                id="h_smoke_meditation",
                text="Spend the night in concentrated smoke meditation with the Ordnance Survey map of Dartmoor.",
                target_node_id="holmes_ch4_regent_street",
            ),
        ],
        clues_discovered=[
            "Giant hound footprints at Yew Alley gate",
            "Sir Charles stood smoking 5-10 minutes before fleeing on tiptoes",
        ],
    )

    nodes["holmes_ch4_regent_street"] = PassageNode(
        id="holmes_ch4_regent_street",
        title="Chapter 4: The Shadow in Regent Street",
        pov=POV.HOLMES,
        node_type=NodeType.BRANCH,
        content=(
            "Sir Henry arrived bearing the cut-and-paste warning letter. The print was clipped from yesterday's Times leading article "
            "with short-bladed nail scissors, smelling faintly of white jessamine. A new tan boot had also disappeared from his hotel room.\n\n"
            "When Sir Henry and Mortimer left, Watson and I shadowed them down Regent Street. Ahead of them crawled a hansom cab. "
            "Through its side window glared a passenger sporting a heavy black beard and spectacles! "
            "The instant he caught my gaze, he raised his hand, and the cab dashed away down Oxford Circus."
        ),
        choices=[
            Choice(
                id="h_trace_cab_2704",
                text="Trace the cab registration number (No. 2704) through the Cabmen's Union registry.",
                target_node_id="holmes_ch5_broken_threads",
            ),
            Choice(
                id="h_search_hotel_boots",
                text="Proceed directly to the Northumberland Hotel to investigate the boots.",
                target_node_id="holmes_ch5_broken_threads",
            ),
        ],
        clues_discovered=[
            "Jessamine-scented Times clipped warning letter",
            "Spy with full black beard in Cab No. 2704",
        ],
    )

    nodes["holmes_ch5_broken_threads"] = PassageNode(
        id="holmes_ch5_broken_threads",
        title="Chapter 5: The Master Strategy",
        pov=POV.HOLMES,
        node_type=NodeType.ANCHOR,
        anchor_name="anchor_london_mission",
        content=(
            "Cabman John Clayton answered my summons: his passenger had insolently proclaimed, 'You may tell him that your passenger was Mr. Sherlock Holmes!' "
            "At the hotel, the new boot had been returned, but an old, worn black boot was stolen.\n\n"
            "The deduction was crystal clear: an unused boot carries no scent. The adversary required an old boot saturated with Sir Henry's scent "
            "to train a live hound to hunt the baronet!\n\n"
            "This adversary is of no mean order. If I accompany Sir Henry to Devonshire openly, the culprit will retreat into hiding. "
            "I must ostensibly remain in London on other business, while secretly slipping down to Dartmoor to establish an undercover vigil "
            "in the prehistoric stone huts, sending Watson ahead as Sir Henry's visible shield."
        ),
        choices=[
            Choice(
                id="h_dispatch_watson_ahead",
                text="Brief Watson on his protective duties, dispatch him to Devonshire, and prepare your undercover post.",
                target_node_id="holmes_start",
            ),
            Choice(
                id="h_instruct_cartwright_secret",
                text="Instruct young Cartwright to prepare secret rations for your moor stone hut headquarters.",
                target_node_id="holmes_start",
            ),
        ],
        clues_discovered=[
            "Adversary requires worn boot to train tracking hound on Sir Henry's scent",
            "Undercover stone hut surveillance strategy initiated",
        ],
    )

    # --- HOLMES AT DARTMOOR ---
    nodes["holmes_start"] = PassageNode(
        id="holmes_start",
        title="Chapter 6: The Detective in the Stone Hut",
        pov=POV.HOLMES,
        node_type=NodeType.ANCHOR,
        anchor_name="anchor_arrival",
        content=(
            "The cold granite walls of the prehistoric hut have been my headquarters for three days. "
            "Watson believes me in Baker Street. Had he known I was here, his natural loyalty would have led "
            "him to communicate with me, and our opponent would have taken alarm.\n\n"
            "Cartwright, the London lad, brings me bread and clean linen from Coombe Tracey. Two stolen boots—"
            "one tan, one black—from Sir Henry's hotel room hold the key. The first boot was new and discarded; "
            "the second boot was old and impregnated with Sir Henry's personal scent. Our adversary possesses a live hound."
        ),
        choices=[
            Choice(
                id="h_analyze_boot",
                text="Examine the scent trail and the chemical traces on the Devon moor soil.",
                target_node_id="holmes_chemical_analysis",
            ),
            Choice(
                id="h_telescope_moor",
                text="Train the pocket telescope on Baskerville Hall and Merripit House.",
                target_node_id="holmes_moor_surveillance",
            ),
            Choice(
                id="h_intercept_cartwright",
                text="Intercept young Cartwright to read Watson's daily field report.",
                target_node_id="holmes_read_reports",
            ),
        ],
        clues_discovered=["Stolen boot used for scent conditioning"],
    )

    nodes["holmes_chemical_analysis"] = PassageNode(
        id="holmes_chemical_analysis",
        title="The Chemical Trace",
        pov=POV.HOLMES,
        node_type=NodeType.BRANCH,
        content=(
            "My pocket laboratory reveals a curious substance scraped from a reed near Grimpen Mire: "
            "a compound of phosphorus and wax, entirely odorless so as not to overpower the hound's delicate "
            "olfactory senses, yet fiercely luminescent in the dark.\n\n"
            "The legend of the spectral hound is being given flesh and blood by an intellect of no mean order. "
            "Who on this moor possesses both deep zoological knowledge and a claim to the Baskerville fortune?"
        ),
        choices=[
            Choice(
                id="h_research_ancestry",
                text="Examine the genealogical records of the Baskerville family branches.",
                target_node_id="holmes_ancestral_clue",
            ),
            Choice(
                id="h_scout_mire_island",
                text="Venture onto the hidden mire path under cover of twilight to locate the kennel.",
                target_node_id="holmes_mire_recon",
            ),
        ],
        clues_discovered=["Odorless luminous phosphorus preparation"],
    )

    nodes["holmes_moor_surveillance"] = PassageNode(
        id="holmes_moor_surveillance",
        title="Field Glass on the Moor",
        pov=POV.HOLMES,
        node_type=NodeType.BRANCH,
        content=(
            "Through my Zeiss glasses, the moor reveals its secrets. I see Jack Stapleton netting insects along "
            "the bog's edge. He moves with uncanny confidence across ground where any other man would sink into eternity.\n\n"
            "Watson is approaching him. Stapleton's sister hurries out to intercept Watson, gesticulating wildly. "
            "A family quarrel? No—she is warning him! The woman is an unwilling accomplice."
        ),
        choices=[
            Choice(
                id="h_surveillance_to_mire",
                text="Track Stapleton's secret willow wand markers into the Great Grimpen Mire.",
                target_node_id="holmes_mire_recon",
            ),
            Choice(
                id="h_surveillance_to_reports",
                text="Return to the hut to decipher Watson's incoming intelligence.",
                target_node_id="holmes_read_reports",
            ),
        ],
        clues_discovered=["Willow wand markers across Grimpen Mire"],
    )

    nodes["holmes_read_reports"] = PassageNode(
        id="holmes_read_reports",
        title="Watson's Bulletins",
        pov=POV.HOLMES,
        node_type=NodeType.BRANCH,
        content=(
            "Watson writes admirably. He details Barrymore's candle signaling and identifies the convict Selden. "
            "More importantly, he notes that Sir Charles was waiting at the Yew Alley gate for a woman with initials L.L.\n\n"
            "A visit to Coombe Tracey parish records gives me the name: Laura Lyons, daughter of the old crank Frankland. "
            "And who paid for her divorce proceedings? None other than Jack Stapleton."
        ),
        choices=[
            Choice(
                id="h_investigate_ancestry",
                text="Investigate the portrait gallery and heritage of the Baskerville line.",
                target_node_id="holmes_ancestral_clue",
            ),
            Choice(
                id="h_observe_night_chase",
                text="Take up vantage on Black Tor as night descends for the Barrymore confrontation.",
                target_node_id="holmes_figure_on_tor",
            ),
        ],
        clues_discovered=["Stapleton funded Laura Lyons"],
    )

    nodes["holmes_ancestral_clue"] = PassageNode(
        id="holmes_ancestral_clue",
        title="The Face of Hugo Baskerville",
        pov=POV.HOLMES,
        node_type=NodeType.BRANCH,
        content=(
            "The family portraits at Baskerville Hall held the final revelation! When I masked the cavalier hat "
            "and curls from the portrait of wicked Sir Hugo, the face looking back at me was unmistakably Jack Stapleton!\n\n"
            "He is Rodger Baskerville's son, born in Costa Rica. He fled to England, married Beryl Garcia, and "
            "adopted the name Stapleton. With Sir Charles dead and Sir Henry murdered, he stands as the undisputed "
            "legal heir to the vast Baskerville estates!"
        ),
        choices=[
            Choice(
                id="h_summon_lestrade",
                text="Telegraph Inspector Lestrade to bring Scotland Yard warrants to Devon immediately.",
                target_node_id="holmes_merripit_dinner",
            ),
            Choice(
                id="h_reunion_with_watson",
                text="Wait inside the stone hut to reveal the entire conspiracy to Watson.",
                target_node_id="watson_hut_reunion",
                pov_switch=POV.WATSON,
            ),
        ],
        clues_discovered=["Stapleton is Rodger Baskerville's son and legal heir"],
    )

    nodes["holmes_figure_on_tor"] = PassageNode(
        id="holmes_figure_on_tor",
        title="The Figure on Black Tor",
        pov=POV.HOLMES,
        node_type=NodeType.ANCHOR,
        anchor_name="anchor_convict",
        content=(
            "The wind howls like a banshee atop Black Tor. Down in the valley, the flash of a candle sparks at "
            "Baskerville Hall, followed by the sound of two men pursuing Selden across the rocks. "
            "Suddenly, the dreadful baying of a hound echoes across the moor!\n\n"
            "Below me, Selden runs for his life—wearing a suit of Sir Henry's cast-off clothing given to him by Barrymore! "
            "If the hound catches his scent, it will tear him to pieces believing him to be the baronet!"
        ),
        choices=[
            Choice(
                id="h_race_to_selden",
                text="Sprint down the tor to prevent the hound from murdering the convict.",
                target_node_id="holmes_selden_crisis",
            ),
            Choice(
                id="h_slip_back_to_hut",
                text="Slip back to your stone hut to coordinate with Watson before Stapleton discovers you.",
                target_node_id="holmes_hut_interior",
            ),
            Choice(
                id="h_switch_to_stapleton",
                text="[Switch POV to Jack Stapleton orchestrating the beast]",
                target_node_id="stapleton_moor_night",
                pov_switch=POV.STAPLETON,
            ),
        ],
    )

    nodes["holmes_selden_crisis"] = PassageNode(
        id="holmes_selden_crisis",
        title="Tragedy on the Crags",
        pov=POV.HOLMES,
        node_type=NodeType.BRANCH,
        content=(
            "A scream of mortal terror ripped through the fog, followed by the dull thud of a falling body. "
            "I arrived at the base of the sheer granite cliff. Selden lay motionless, his skull fractured against the rocks. "
            "A few paces away in the heather, the smell of sulfur and phosphor hung thick in the damp air.\n\n"
            "A soft footstep sounded behind me. Jack Stapleton appeared out of the mist, carrying a lantern, expecting "
            "to find the corpse of Sir Henry Baskerville!"
        ),
        choices=[
            Choice(
                id="h_confront_stapleton_now",
                text="Drop the mask and accuse Stapleton of murder on the spot!",
                target_node_id="ending_holmes_master_deduction",
            ),
            Choice(
                id="h_play_the_fool",
                text="Pretend the death was a mere drunken accident and lure him into the Merripit dinner trap.",
                target_node_id="holmes_merripit_dinner",
            ),
        ],
    )

    nodes["holmes_hut_interior"] = PassageNode(
        id="holmes_hut_interior",
        title="The Detective's Lair",
        pov=POV.HOLMES,
        node_type=NodeType.BRANCH,
        content=(
            "I returned to the prehistoric hut to find someone had breached the perimeter. The scent of a Bradley "
            "cigarette still lingered. A shadow moved near the granite lintel—Watson, revolver in hand!\n\n"
            "With a friendly greeting, I disarmed his tension. Together, we reviewed every thread: the stolen boots, "
            "the phosphorescent compound, and Stapleton's ancestral claim."
        ),
        choices=[
            Choice(
                id="h_hut_to_dinner",
                text="Prepare the Scotland Yard ambush for tomorrow night's dinner at Merripit House.",
                target_node_id="holmes_merripit_dinner",
            ),
            Choice(
                id="h_hut_to_mire_recon",
                text="Conduct a nighttime raid on Stapleton's island kennel in the Grimpen Mire.",
                target_node_id="holmes_mire_recon",
            ),
        ],
    )

    nodes["holmes_moor_ambush"] = PassageNode(
        id="holmes_moor_ambush",
        title="Ambush at the Tor",
        pov=POV.HOLMES,
        node_type=NodeType.BRANCH,
        content=(
            "I caught Watson attempting to circle my stone hut from the rear. 'An admirable tactical maneuver, "
            "my dear Watson,' I called out, stepping from behind a boulder. 'Though I would advise against stepping "
            "on dry heather when stalking a consulting detective.'\n\n"
            "Watson laughed with relief and gripped my hand. The time for secrecy is over; the time for action has arrived."
        ),
        choices=[
            Choice(
                id="h_ambush_to_dinner",
                text="Brief Watson on the final trap and mobilize for the Merripit dinner.",
                target_node_id="holmes_merripit_dinner",
            ),
        ],
    )

    nodes["holmes_mire_recon"] = PassageNode(
        id="holmes_mire_recon",
        title="The Heart of Grimpen Mire",
        pov=POV.HOLMES,
        node_type=NodeType.BRANCH,
        content=(
            "Following the submerged willow stakes, I penetrated the impenetrable Great Grimpen Mire. "
            "On a solitary island of dry peat stood the ruins of an abandoned tin-miner's shack. "
            "Inside, tethered with a logging chain, snarled a monstrous creature—a cross between a bloodhound "
            "and a mastiff, gaunt, savage, and starved for blood.\n\n"
            "Near the chain lay Sir Henry's stolen black boot."
        ),
        choices=[
            Choice(
                id="h_recon_to_dinner",
                text="Slip back silently to lay the trap at Merripit House where the crime will be committed.",
                target_node_id="holmes_merripit_dinner",
            ),
            Choice(
                id="h_recon_strike_now",
                text="Raid the island kennel immediately with Lestrade and handcuffs!",
                target_node_id="ending_holmes_master_deduction",
            ),
        ],
    )

    nodes["holmes_merripit_dinner"] = PassageNode(
        id="holmes_merripit_dinner",
        title="The Ambush at Merripit House",
        pov=POV.HOLMES,
        node_type=NodeType.ANCHOR,
        anchor_name="anchor_climax",
        content=(
            "Lestrade of Scotland Yard joined Watson and me behind a ridge of rocks fifty yards from Merripit House. "
            "Sir Henry had dined with Stapleton and was scheduled to walk home alone across the moor.\n\n"
            "The front door opened. Sir Henry stepped out into the night. But from the south, a white, impenetrable "
            "sea of fog was drifting swiftly toward us, swallowing the path! In five minutes, our field of fire will be gone!"
        ),
        choices=[
            Choice(
                id="h_hold_fire",
                text="Hold position until the creature emerges through the fog bank!",
                target_node_id="climax_fog_advance",
            ),
            Choice(
                id="h_charge_forward",
                text="Advance through the fog to intercept Sir Henry before the hound reaches him!",
                target_node_id="climax_fog_advance",
            ),
        ],
    )

    # =========================================================================
    # CHAPTERS 1-5: LONDON PROLOGUE (STAPLETON POV)
    # =========================================================================
    nodes["stapleton_ch1_london"] = PassageNode(
        id="stapleton_ch1_london",
        title="Chapter 4: The Stalker in London",
        pov=POV.STAPLETON,
        node_type=NodeType.ANCHOR,
        anchor_name="anchor_chapter1",
        content=(
            "Disguised beneath a full false black beard and dark spectacles, I shadowed young Sir Henry Baskerville from the moment "
            "his ship docked from Canada to the Northumberland Hotel. Beryl, my captive wife, secretly attempted to warn him with words "
            "cut from the Times, but I caught her in time—though the meddling letter had already slipped into the mail.\n\n"
            "At the hotel, I tipped a chambermaid half a sovereign to purloin the baronet's boot from outside his door. "
            "To my fury, the careless girl brought me a brand-new tan boot that had never touched human skin! "
            "An unworn boot carries no scent. I cast it back and ordered a boot that Sir Henry had actually walked in—an old, worn black boot."
        ),
        choices=[
            Choice(
                id="s_demand_worn_boot",
                text="Bribe the hotel servant to steal Sir Henry's old, worn black boot from the corridor.",
                target_node_id="stapleton_ch4_cab",
            ),
            Choice(
                id="s_shadow_baker_street",
                text="Follow Sir Henry and Dr. Mortimer as they walk toward Baker Street.",
                target_node_id="stapleton_ch4_cab",
            ),
        ],
        clues_discovered=[
            "Disguise: false black beard and dark spectacles",
            "Unworn boot rejected; worn black boot needed for scent conditioning",
        ],
    )

    nodes["stapleton_ch4_cab"] = PassageNode(
        id="stapleton_ch4_cab",
        title="Chapter 5: The Encounter in Cab 2704",
        pov=POV.STAPLETON,
        node_type=NodeType.BRANCH,
        content=(
            "I hailed hansom cab No. 2704 on Trafalgar Square and instructed driver John Clayton to tail Sir Henry to 221B Baker Street. "
            "As the baronet entered the building, a cold jolt went through me: stepping onto the pavement came Sherlock Holmes himself, "
            "his piercing gaze sweeping the street!\n\n"
            "His eyes fixed upon my cab window! Instantly I threw up the trap-door: 'Driver, gallop for Waterloo Station! Two sovereigns if you outrun him!' "
            "At Waterloo, as I pressed the coins into Clayton's hand, I could not resist leaving a mocking parting thrust: "
            "'If you want to know, tell your friends your passenger was Sherlock Holmes!'"
        ),
        choices=[
            Choice(
                id="s_take_early_express",
                text="Collect the stolen worn black boot and take the early express train back to Devonshire.",
                target_node_id="stapleton_ch5_devon_prep",
            ),
            Choice(
                id="s_vanish_in_crowd",
                text="Disappear through the Waterloo crowd to ensure no detective followed.",
                target_node_id="stapleton_ch5_devon_prep",
            ),
        ],
        clues_discovered=[
            "Cab No. 2704 escape from Sherlock Holmes",
            "Brazen mockery of Baker Street",
        ],
    )

    nodes["stapleton_ch5_devon_prep"] = PassageNode(
        id="stapleton_ch5_devon_prep",
        title="Chapter 5: Return to Grimpen Mire",
        pov=POV.STAPLETON,
        node_type=NodeType.ANCHOR,
        anchor_name="anchor_london_mission",
        content=(
            "With Sir Henry's old, worn black boot securely wrapped in oiled silk in my valise, I caught the early Great Western express back to Devonshire. "
            "Sir Henry and Watson will follow in two days, entirely unaware that the London detective they so admire has been left far behind.\n\n"
            "The stage at Merripit House is set. The hound in the abandoned mire tin-mine has not eaten meat in forty-eight hours. "
            "All that remains is to bring the boot to its muzzle."
        ),
        choices=[
            Choice(
                id="s_to_mire_kennel",
                text="Trek across the hidden mire path to begin scent-training the beast on the island.",
                target_node_id="stapleton_start",
            ),
            Choice(
                id="s_to_merripit_prep",
                text="Return to Merripit House and enforce Beryl's total obedience before the baronet arrives.",
                target_node_id="stapleton_start",
            ),
        ],
        clues_discovered=[
            "Scented boot secured for the hound",
            "Merripit House trap prepared ahead of Watson's arrival",
        ],
    )

    # --- STAPLETON AT DARTMOOR ---
    nodes["stapleton_start"] = PassageNode(
        id="stapleton_start",
        title="Chapter 6: The Web of Merripit House",
        pov=POV.STAPLETON,
        node_type=NodeType.ANCHOR,
        anchor_name="anchor_arrival",
        content=(
            "Sir Charles is buried, dead of heart failure at the Yew Alley gate, exactly as I designed. "
            "Now the new heir, Sir Henry, has arrived in Devon. He brought with him a bumbling military doctor "
            "named Watson, while Sherlock Holmes remains in London, blind to what transpires on Dartmoor.\n\n"
            "The prize is within my grasp: Baskerville Hall and a fortune of a million pounds. "
            "I only need to eliminate this last heir, and the estate will fall to me under my South American alias."
        ),
        choices=[
            Choice(
                id="s_scout_watson",
                text="Take the butterfly net and intercept Dr. Watson along the fringe of Grimpen Mire.",
                target_node_id="stapleton_moor_stroll",
            ),
            Choice(
                id="s_check_hound",
                text="Venture onto the mire island to inspect the hound and test the scent trail.",
                target_node_id="stapleton_check_hound",
            ),
        ],
        clues_discovered=["Stapleton's claim to Baskerville inheritance"],
    )

    nodes["stapleton_moor_stroll"] = PassageNode(
        id="stapleton_moor_stroll",
        title="Playing the Naturalist",
        pov=POV.STAPLETON,
        node_type=NodeType.BRANCH,
        content=(
            "I played the gentle entomologist to perfection. To impress Watson with the lethal nature of the moor, "
            "I pointed out a pony sinking helplessly into the bog. But suddenly Beryl ran toward us across the heather! "
            "Believing Watson was Sir Henry, she began to utter frantic warnings!\n\n"
            "If that foolish woman ruins my months of preparation, I will silence her permanently."
        ),
        choices=[
            Choice(
                id="s_chastise_beryl",
                text="Confront Beryl in private and break her rebellious spirit.",
                target_node_id="stapleton_beryl_control",
            ),
            Choice(
                id="s_charm_watson",
                text="Laugh off Beryl's eccentricity and divert Watson with botanical talk.",
                target_node_id="stapleton_deceive_watson",
            ),
        ],
    )

    nodes["stapleton_check_hound"] = PassageNode(
        id="stapleton_check_hound",
        title="The Hound on the Mire Island",
        pov=POV.STAPLETON,
        node_type=NodeType.BRANCH,
        content=(
            "I stepped carefully across the hidden tussocks of Grimpen Mire to the abandoned tin mine. "
            "In the darkness, the bloodhound-mastiff brute rattled its iron chain and snarled hungrily. "
            "I held Sir Henry's stolen worn boot beneath its nostrils until its jowls dripped with saliva.\n\n"
            "The phosphor paste is mixed—luminous, odorless, terrifying to superstitious fools."
        ),
        choices=[
            Choice(
                id="s_apply_phosphor",
                text="Coat the hound's jaws and eyes with the luminous compound.",
                target_node_id="stapleton_phosphor_prep",
            ),
            Choice(
                id="s_plan_dinner",
                text="Return to Merripit House to invite Sir Henry to his final dinner.",
                target_node_id="stapleton_invite_henry",
            ),
        ],
        clues_discovered=["Phosphor paste prepared on hound"],
    )

    nodes["stapleton_beryl_control"] = PassageNode(
        id="stapleton_beryl_control",
        title="The Captive Wife",
        pov=POV.STAPLETON,
        node_type=NodeType.BRANCH,
        content=(
            "Behind the locked door of our bedchamber, Beryl wept and defied me. She refuses to play the bait "
            "for Sir Henry any longer. 'You are a monster, Jack!' she cried.\n\n"
            "No matter. I will bind and gag her in the upstairs room before Sir Henry arrives for dinner. "
            "Her silence is easily purchased with hemp rope."
        ),
        choices=[
            Choice(
                id="s_bind_now",
                text="Bind Beryl securely to the bedpost and proceed with the dinner trap.",
                target_node_id="stapleton_bind_beryl",
            ),
            Choice(
                id="s_patrol_tors",
                text="Inspect the surrounding tors for any uninvited observers first.",
                target_node_id="stapleton_search_tors",
            ),
        ],
    )

    nodes["stapleton_deceive_watson"] = PassageNode(
        id="stapleton_deceive_watson",
        title="Probing the Doctor",
        pov=POV.STAPLETON,
        node_type=NodeType.BRANCH,
        content=(
            "Over tea at Merripit House, I probed Watson regarding Sherlock Holmes. The doctor insists Holmes "
            "is occupied with an embezzlement case in London. Yet Watson's eyes wandered toward the tors.\n\n"
            "Could someone be hiding out among the prehistoric ruins? I noticed smoke rising from a stone hut "
            "earlier this afternoon."
        ),
        choices=[
            Choice(
                id="s_investigate_hut",
                text="Take a carbine and scout the stone huts on the tor.",
                target_node_id="stapleton_search_tors",
            ),
            Choice(
                id="s_ignore_smoke",
                text="Dismiss it as a shepherd or convict and press forward with Sir Henry's dinner.",
                target_node_id="stapleton_invite_henry",
            ),
        ],
    )

    nodes["stapleton_phosphor_prep"] = PassageNode(
        id="stapleton_phosphor_prep",
        title="A Monster in the Dark",
        pov=POV.STAPLETON,
        node_type=NodeType.BRANCH,
        content=(
            "The luminous paste glistens over the beast's muzzle and brow. In the pitch black of the tin shack, "
            "it looks like a demon wrenched from the bowels of hell! No human heart could withstand its charge "
            "without freezing in terror.\n\n"
            "The stage is set. All that remains is to bring Sir Henry out onto the moor alone at night."
        ),
        choices=[
            Choice(
                id="s_phosphor_to_bind",
                text="Lock up the beast and secure Beryl in the upper room.",
                target_node_id="stapleton_bind_beryl",
            ),
        ],
    )

    nodes["stapleton_search_tors"] = PassageNode(
        id="stapleton_search_tors",
        title="Smoke on the Tors",
        pov=POV.STAPLETON,
        node_type=NodeType.BRANCH,
        content=(
            "I climbed Black Tor with my field glass. Outside one of the stone huts, a boy was delivering supplies. "
            "Someone is living there—someone disciplined, orderly, and patient.\n\n"
            "If it is a London detective, he must be eliminated before he joins forces with Watson."
        ),
        choices=[
            Choice(
                id="s_hound_the_hut",
                text="Release the hound tonight toward the stone hut to eliminate the spy!",
                target_node_id="stapleton_attack_hut",
            ),
            Choice(
                id="s_proceed_with_henry",
                text="The spy poses no threat if Sir Henry dies tonight. Return to Merripit House.",
                target_node_id="stapleton_invite_henry",
            ),
        ],
    )

    nodes["stapleton_moor_night"] = PassageNode(
        id="stapleton_moor_night",
        title="The Convict Hunt",
        pov=POV.STAPLETON,
        node_type=NodeType.ANCHOR,
        anchor_name="anchor_convict",
        content=(
            "The moor is alive with shouts tonight. Watson and Sir Henry are hunting Selden, the escaped convict. "
            "I released the hound on Sir Henry's boot-scent to strike in the confusion!\n\n"
            "The beast pursued its quarry up the jagged granite cliffs. A man plunged screaming to his death! "
            "I hurried forward with my lantern—only to discover Selden's corpse, dressed in Sir Henry's cast-off clothes!"
        ),
        choices=[
            Choice(
                id="s_salvage_plan",
                text="Curse the blunder, retreat before Watson arrives, and lure Sir Henry to dinner tomorrow.",
                target_node_id="stapleton_invite_henry",
            ),
            Choice(
                id="s_panic_escape",
                text="Panic! Assume the law is closing in and attempt a midnight flight across the mire.",
                target_node_id="ending_stapleton_tragedy",
            ),
        ],
    )

    nodes["stapleton_attack_hut"] = PassageNode(
        id="stapleton_attack_hut",
        title="The Ambush at the Hut",
        pov=POV.STAPLETON,
        node_type=NodeType.BRANCH,
        content=(
            "I unleashed the hound toward the prehistoric hut. But as the beast leaped forward, a rifle cracked "
            "from the rocks! The bullet struck the hound's shoulder, sending it howling into the darkness. "
            "Out from the shadows stepped Sherlock Holmes, his revolver leveled at my chest!"
        ),
        choices=[
            Choice(
                id="s_run_for_mire",
                text="Turn and sprint blindly for the safety of the Great Grimpen Mire!",
                target_node_id="ending_stapleton_tragedy",
            ),
            Choice(
                id="s_surrender_holmes",
                text="Throw down your weapon and raise your hands in surrender.",
                target_node_id="ending_stapleton_arrest",
            ),
        ],
    )

    nodes["stapleton_bind_beryl"] = PassageNode(
        id="stapleton_bind_beryl",
        title="Silencing the House",
        pov=POV.STAPLETON,
        node_type=NodeType.BRANCH,
        content=(
            "I dragged Beryl up the narrow stairs, tied her wrists to the brass bedpost, and gagged her with a scarf. "
            "She glared at me with pure hatred, but she can utter no sound.\n\n"
            "Downstairs, the heavy knocker sounded. Sir Henry Baskerville has arrived for dinner."
        ),
        choices=[
            Choice(
                id="s_host_dinner",
                text="Smooth your coat, assume an air of genial hospitality, and welcome the baronet.",
                target_node_id="stapleton_dinner_trap",
            ),
        ],
    )

    nodes["stapleton_invite_henry"] = PassageNode(
        id="stapleton_invite_henry",
        title="The Fatal Invitation",
        pov=POV.STAPLETON,
        node_type=NodeType.BRANCH,
        content=(
            "Sir Henry gladly accepted my invitation to dine at Merripit House. He is desperate to see Beryl again. "
            "I insisted he walk home alone across the moor, promising that the night air would clear his head.\n\n"
            "Now I must prepare the house and ensure Beryl does not whisper a single word of warning."
        ),
        choices=[
            Choice(
                id="s_bind_beryl_now",
                text="Lock and bind Beryl in the upper bedchamber before Sir Henry arrives.",
                target_node_id="stapleton_bind_beryl",
            ),
        ],
    )

    nodes["stapleton_dinner_trap"] = PassageNode(
        id="stapleton_dinner_trap",
        title="Dinner at Merripit House",
        pov=POV.STAPLETON,
        node_type=NodeType.ANCHOR,
        anchor_name="anchor_climax",
        content=(
            "Dinner went flawlessly. Sir Henry drank freely of my port, saddened only by Beryl's 'sudden migraine.' "
            "At ten o'clock, he took his cane and stepped out the door to walk the lonely moor path back to Baskerville Hall.\n\n"
            "A magnificent, dense fog is rolling in across Grimpen Mire—a white wall that will smother his cries and "
            "blind any rescue. I slip quietly to the outhouse to release the flaming demon!"
        ),
        choices=[
            Choice(
                id="s_release_beast",
                text="Unlock the outhouse door and unleash the hound upon Sir Henry's trail!",
                target_node_id="climax_fog_advance",
            ),
            Choice(
                id="s_switch_to_watson",
                text="[Switch POV to Dr. Watson watching from the rocks outside]",
                target_node_id="watson_climax_vigil",
                pov_switch=POV.WATSON,
            ),
        ],
    )

    # =========================================================================
    # CLIMAX & MULTIPLE ENDINGS
    # =========================================================================
    nodes["climax_fog_advance"] = PassageNode(
        id="climax_fog_advance",
        title="The Hound of the Baskervilles",
        pov=POV.WATSON,
        node_type=NodeType.CLIMAX,
        anchor_name="anchor_climax",
        content=(
            "A sound came out of the rolling white fog—a patter of rapid footsteps and a low, guttural snarl. "
            "Suddenly, leaping through the curtain of vapor, came a beast that might have sprung from the nightmares of Dante! "
            "It was a hound of enormous size, coal-black, with fire bursting from its gaping mouth, its eyes glowing with "
            "smoldering blue flame, its muzzle and dewlaps outlined in flickering phosphor light!\n\n"
            "Sir Henry screamed in terror and fell backward onto the turf. The monster soared through the air, "
            "its fangs aimed straight for his throat!"
        ),
        choices=[
            Choice(
                id="climax_shoot_beast",
                text="Holmes, Watson, and Lestrade unleash a simultaneous volley of revolver fire!",
                target_node_id="ending_canon",
            ),
            Choice(
                id="climax_watson_shield",
                text="Watson dives forward with his service revolver to shield Sir Henry with his own body!",
                target_node_id="ending_watson_heroic",
            ),
            Choice(
                id="climax_fog_blind",
                text="The dense white fog blinds the marksmen; the shots go wild into the night!",
                target_node_id="ending_stapleton_triumph",
            ),
        ],
    )

    nodes["ending_canon"] = PassageNode(
        id="ending_canon",
        title="Canon Triumph: The Hound Destroyed",
        pov=POV.HOLMES,
        node_type=NodeType.ENDING,
        content=(
            "Five revolver bullets slammed into the flank of the leaping beast. With a ferocious howl of agony, "
            "the monstrous hound crashed to earth, thrashing in its death throes upon the heather before lying stone dead.\n\n"
            "Sir Henry was fainting, but untouched. We dashed to Merripit House, kicked down the locked bedroom door, "
            "and cut the cords that bound the bruised and weeping Beryl. She pointed toward the Great Grimpen Mire: "
            "'He has fled to his island in the bog!'\n\n"
            "The following morning, beneath the bright autumn sun, Holmes and I followed Stapleton's willow wands into the mire. "
            "Halfway across, on a wretched patch of slime, lay Sir Henry's stolen black boot. But of Jack Stapleton, "
            "there was no trace save for a single heel-mark sinking into the black, sucking peat.\n\n"
            "Somewhere in the heart of the Great Grimpen Mire, down in the foul slime of the bottomless quagmire, "
            "the cold, ruthless master of the hound sleeps forever."
        ),
        choices=[],
    )

    nodes["ending_watson_heroic"] = PassageNode(
        id="ending_watson_heroic",
        title="Watson's Valor: The Doctor's Triumph",
        pov=POV.WATSON,
        node_type=NodeType.ENDING,
        content=(
            "Placing myself directly between Sir Henry and the leaping monster, I thrust the muzzle of my service revolver "
            "straight into the phosphorescent jaw and pulled the trigger three times! The beast dropped like a stone.\n\n"
            "Catching sight of a dark figure bolting through the fog, I gave chase with all the vigor of my Afghan campaign days. "
            "I cornered Jack Stapleton against the shear granite face of an abandoned quarry, holding him at gunpoint until "
            "Holmes and Lestrade rushed up with handcuffs.\n\n"
            "'Splendid, Watson!' cried Holmes, clapping me on the shoulder. 'A masterstroke of courage! England has many detectives, "
            "but only one John H. Watson!' The Baskerville curse is broken forever by the hand of the good doctor."
        ),
        choices=[],
    )

    nodes["ending_holmes_master_deduction"] = PassageNode(
        id="ending_holmes_master_deduction",
        title="Holmes's Masterstroke: Judicial Triumph",
        pov=POV.HOLMES,
        node_type=NodeType.ENDING,
        content=(
            "With the stolen boots, the phosphorus formula, and the Costa Rican birth records in my pocket, "
            "I stepped forward and presented the complete chain of evidence before Jack Stapleton could even unleash the hound.\n\n"
            "Lestrade snapped the steel manacles onto Stapleton's wrists. 'Jack Stapleton—or rather, Rodger Baskerville—"
            "you are under arrest for the murder of Sir Charles Baskerville and the attempted murder of Sir Henry.'\n\n"
            "Stapleton collapsed in defeat. Two months later at Exeter Assizes, the evidence was found incontestable, "
            "and the murderer met his just fate upon the scaffold. Another triumph of pure deduction."
        ),
        choices=[],
    )

    nodes["ending_stapleton_triumph"] = PassageNode(
        id="ending_stapleton_triumph",
        title="The Dark Inheritance: Stapleton's Victory",
        pov=POV.STAPLETON,
        node_type=NodeType.ENDING,
        content=(
            "The rolling fog blinded the foolish London marksmen. Their bullets whistled harmlessly into the peat. "
            "By the time they reached the path, Sir Henry lay still, his heart stopped by sheer terror before the hound's "
            "flaming jaws, leaving no mark of human violence.\n\n"
            "I recalled the hound with a low whistle, washed its jaws in the mire stream, and slipped back to Merripit House. "
            "The Devon coroner once again ruled the death as heart failure caused by the ancient family curse.\n\n"
            "Six months later, residing in Paris under the name Vandeleur, I quietly stepped forward to claim the title, "
            "Baskerville Hall, and the fortune of a million pounds. The game is won."
        ),
        choices=[],
    )

    nodes["ending_stapleton_tragedy"] = PassageNode(
        id="ending_stapleton_tragedy",
        title="The Grimpen Mire Consumes Its Own",
        pov=POV.STAPLETON,
        node_type=NodeType.ENDING,
        content=(
            "Panic gripped my heart. Gunfire and shouting echoed from all corners of the moor. "
            "I plunged headlong into the darkness toward my willow-marked path across the Great Grimpen Mire.\n\n"
            "In the blinding swirl of fog, my foot plunged not onto firm reed tussock, but into foul, greasy black slime. "
            "I threw out my arms, but found only clutching quagmire. The bog seized my knees, my waist, my chest, "
            "pulling with inexorable, suffocating weight.\n\n"
            "I screamed into the mist, but only the crying of the plovers answered. The black mire bubbled once, "
            "twice, and closed forever over my head."
        ),
        choices=[],
    )

    nodes["ending_stapleton_arrest"] = PassageNode(
        id="ending_stapleton_arrest",
        title="Justice on Dartmoor",
        pov=POV.STAPLETON,
        node_type=NodeType.ENDING,
        content=(
            "Surrounded by Holmes's revolver and Lestrade's Scotland Yard whistle, I threw down my weapons. "
            "The hound was shot, Beryl freed, and my brilliant plot shattered by the cold intellect of Baker Street.\n\n"
            "As the carriage rattled away toward Exeter Gaol, I looked back one last time at the grim tors of Dartmoor, "
            "knowing that the gallows awaited me in the winter chill."
        ),
        choices=[],
    )

    return StoryGraph(
        language="en",
        title="The Hound of the Baskervilles: Multi-POV Interactive Edition",
        author="Sir Arthur Conan Doyle (Interactive Adaptation)",
        description=(
            "A Choose Your Own Adventure adaptation experienced through three perspectives: "
            "Dr. John H. Watson, Sherlock Holmes, and Jack Stapleton. Starting from Chapter 1 at 221B Baker Street."
        ),
        start_nodes={
            POV.WATSON: "watson_ch1_baker_street",
            POV.HOLMES: "holmes_ch1_baker_street",
            POV.STAPLETON: "stapleton_ch1_london",
        },
        nodes=nodes,
    )
