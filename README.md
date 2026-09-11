# The Hound of the Baskervilles: Multi-POV Interactive Fiction
# 《巴斯克维尔的猎犬》多视角互动小说

A bilingual (English & Chinese / 中英双语) Choose Your Own Adventure (CYOA) adaptation of Sir Arthur Conan Doyle's *The Hound of the Baskervilles*, based on canonical source texts:
- `src/content/book_en.txt`: Arthur Conan Doyle original English text
- `src/content/book_cn.txt`: Classic Chinese translated text

---

## Highlights

1. **Kindle Web Browser Edition (`dist/web/index.html`):**
   - **Starts from Chapter 1:** Investigation begins directly at 221B Baker Street examining Dr. Mortimer's walking stick and the 1742 manuscript.
   - **Language Selection at Start:** Readers choose **English** or **中文版** on launch.
   - **Instant Mid-Story Language Toggle:** Readers can flip between English and Chinese mid-investigation without losing their scene location or discovered clues.
   - **E-Ink Optimizations:** High-contrast monochrome typography (Bookerly & CJK Serif), zero CSS animation delay, large tap targets (>50px) with instant inverted touch feedback.
   - **Three Offline Download Formats (AZW3 / EPUB / MOBI):** Direct buttons in the header and landing page for all three formats in both English and Chinese.

2. **Native Kindle Formats (.azw3 & .mobi):**
   - **`dist/hound_of_the_baskervilles_en.azw3`** & **`dist/hound_of_the_baskervilles_cn.azw3`** (KF8): Best for modern Kindles (Paperwhite, Oasis, Scribe, Voyage, Basic) via direct USB transfer to the `documents` folder.
   - **`dist/hound_of_the_baskervilles_en.mobi`** & **`dist/hound_of_the_baskervilles_cn.mobi`**: Dual-format MOBI for vintage/legacy Kindles (Kindle 1-3, Keyboard, DX).

3. **Offline Interactive EPUB 3 Edition:**
   - **`dist/hound_of_the_baskervilles_en.epub`** (English Edition, 54 interactive passages)
   - **`dist/hound_of_the_baskervilles_cn.epub`** (中文版, 54 interactive passages)
   - Standard EPUB 3 + NCX fallback compliant with Amazon **Send to Kindle** (web/email sync), Apple Books, Kobo, and Calibre.

4. **Twine / Twee 3 Source:**
   - `dist/hound_of_the_baskervilles_en.twee`
   - `dist/hound_of_the_baskervilles_cn.twee`

---

## Playable Perspectives / 可选探案视角

| Perspective | 探案视角 | Role / 角色背景 |
| :--- | :--- | :--- |
| **Dr. John H. Watson** | **约翰·H·华生医生** | From 221B Baker Street to Dartmoor: examines Dr. Mortimer's stick, shadows the London cab, guards Sir Henry at Baskerville Hall. / 从贝克街221B启程推演摩梯末手杖，摄政街追踪幽灵马车，贴身护卫亨利爵士。 |
| **Sherlock Holmes** | **歇洛克·福尔摩斯** | From breakfast deduction in London to covert stone hut surveillance on Dartmoor. / 从早餐桌演绎法破译失窃皮靴与气味追踪，暗中潜入荒原石屋布下天罗地网。 |
| **Jack Stapleton** | **杰克·斯台普吞** | Antagonist: shadowing Henry in London, bribing hotel servants for scented boots, conditioning the hound in Grimpen Mire. / 乔装潜伏伦敦谋盗带味黑靴，2704号马车戏弄名侦探，引恶犬诱杀继承人谋夺巨产。 |

Shared canon milestone anchors:
- **Anchor 1 / 节点一:** Chapter 1 Consultation / 第一章 贝克街咨询 (`anchor_chapter1`)
- **Anchor 2 / 节点二:** London Mission & Departure / 第五章 伦敦布局与出发 (`anchor_london_mission`)
- **Anchor 3 / 节点三:** Dartmoor Arrival / 第六章 抵达达特沼地 (`anchor_arrival`)
- **Anchor 4 / 节点四:** Night of the Escaped Convict / 追捕逃犯塞尔登之夜 (`anchor_convict`)
- **Anchor 5 / 节点五:** Merripit House Dinner & Climax / 梅利琵宅邸晚宴与泥潭决战 (`anchor_climax`)

---

## Quick Start / 快速上手

### 1. Build All Distributions / 编译生成所有版本
```bash
python main.py build
```
Compiled targets in `./dist/`:
- `dist/web/index.html` (Bilingual Kindle Web Reader)
- `dist/hound_of_the_baskervilles_en.azw3` (English AZW3 / KF8)
- `dist/hound_of_the_baskervilles_cn.azw3` (Chinese AZW3 / KF8)
- `dist/hound_of_the_baskervilles_en.epub` (English Offline EPUB 3)
- `dist/hound_of_the_baskervilles_cn.epub` (Chinese Offline EPUB 3)
- `dist/hound_of_the_baskervilles_en.mobi` (English Offline MOBI)
- `dist/hound_of_the_baskervilles_cn.mobi` (Chinese Offline MOBI)
- `dist/hound_of_the_baskervilles_en.twee` (English Twine source)
- `dist/hound_of_the_baskervilles_cn.twee` (Chinese Twine source)

### 2. Preview the Kindle Web Reader / 本地预览网页版
```bash
python main.py serve --port 8080
```
Open [http://localhost:8080](http://localhost:8080) on your desktop browser or on your Kindle device (connected to the same Wi-Fi, using your PC's IP e.g. `http://192.168.x.x:8080/`).

### 3. Transfer to Kindle / 导入 Kindle 阅读
- **Direct USB Sideload (Modern Kindles):** Connect Kindle via USB cable, copy `.azw3` directly into the `documents` folder on the Kindle drive.
- **Send to Kindle (Wireless / Email):** Upload `.epub` via [Amazon Send to Kindle](https://www.amazon.com/sendtokindle) or email to your `@kindle.com` address.
- **Legacy Kindles:** Copy `.mobi` directly into the `documents` folder via USB.

---

## Automated Verification / 自动化测试
```bash
python -m pytest tests
```
Verifies NetworkX reachability and zero dangling links across both languages, valid uncompressed mimetype, strict XML parsing of all 102 XHTML passages, and bilingual web bundle integrity.
