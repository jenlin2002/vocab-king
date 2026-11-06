# vocab-king（圖解單字）

靜態網站（GitHub Pages：jenlin2002.github.io/vocab-king/）。使用者有 LiveABC《圖解英語單字王》（14 類、73 主題、約 1500 字）和 MP3，要做成成長學習館的一張卡。對象國一、國二。

## 登入改成 Cloudflare Access＋Google 帳號（2026-11-04 規劃，程式已做好、等使用者設定後台）

- 使用者選定：學習網站跟股票網站一樣用 Cloudflare 保護（但兩邊完全分開），BRANDEN、MELISSA 用自己的 Google 帳號、家長用自己的 Gmail 登入，不再「選名字＋4 位數 PIN」。
- 6 個 repo 由首頁 repo（jenlin2002.github.io）的 GitHub Actions「部署到 Cloudflare Pages」合成一個網站（Pages 專案 `bmlearn`，網址 **https://bmlearn.pages.dev**，路徑和 GitHub Pages 一樣；2026-11-05 從 learn-6td.pages.dev 改名，舊網址和 jenlin2002.github.io 都轉到這裡，後台步驟在首頁 repo `CLOUDFLARE-SETUP.md` 第七節），`functions/api/me.js` 用 Access 憑證＋`USER_MAP`（Cloudflare 變數，email 不放 repo）回傳登入者名字。
- `points.js`（各站副本內容相同）：在 Cloudflare 網址打開時問 `/api/me`，自動設定 `quizStudentName`、不出現「你是誰？」關卡；第一階段每台裝置第一次只問一次自己的 PIN；第二階段（Code.gs 加 `cfUser_`、Cloudflare 設 `POINTS_SECRET`）點數改走 `/api/points`，不用 PIN。登出會連 Google 登入一起登出。在 jenlin2002.github.io 舊網址一切照舊。
- 後台設定步驟、測試方法、第二階段 Code.gs 改法都在首頁 repo 的 `CLOUDFLARE-SETUP.md`。密碼、金鑰一律使用者自己在 Cloudflare／GitHub／Google 後台輸入。
- 之後新做的頁面照舊用相對路徑；子站寫死的 `https://jenlin2002.github.io/` 部署時會自動改成 `/`。Cloudflare Pages 單檔上限 25 MB、整站 20000 個檔（2026-11-04 約 15300 個），大檔（>24 MB）部署時自動改由 `/api/big` 轉給登入的人（2026-11-05 起；要有 `REPOS_TOKEN`，repo 改 Private 也能讀；金鑰到期要重做，見首頁 repo `CLOUDFLARE-SETUP.md` 第八節）。寫頁面照舊連原本的相對路徑，不用改。
## 使用者與工作方式（四個 repo 共用同一段，2026-10-13）

- 使用者在三個地方用 Claude Code：**家裡電腦、公司電腦**（兩台都有 GitHub Desktop，用它 Pull／Push）、**外出用手機 App（雲端版）**。學習成長網站已經做很久了，不用從頭介紹。
- **不用教 git／GitHub Desktop／PowerShell 的操作。** 改完直接開 PR 合併到 `main`（使用者另一台電腦用 GitHub Desktop Pull 就好），只要回報「改了什麼、合併到哪裡」。
- 一律用**繁體中文**回覆。
- **每次結束前**：把這次做的事、待辦更新到這個 CLAUDE.md，合併到 `main`，下一個地方 Pull 後就接得上。
- 學習網站的 repo（都在 jenlin2002 底下，GitHub Pages 從 `main` 發布）：
  `jenlin2002.github.io`（網站首頁＝成長學習館總入口、點數存摺、B&M 學習 App）、`english-quiz`（英文測驗系統）、
  `daily_life_listening`（美式生活館）、`vocab-king`（圖解單字）、`nat-geo-reading`（國家地理風閱讀）、`exam-bank`（段考題庫）。
  雲端版只讀得到這次有載入的 repo；要改的 repo 沒載入時，直接用 add_repo 加進來。
- 股票（`stock`、`stock-dashboard`）和學習網站分開，學習網站裡不要放股票相關的東西。

## 版權原則（公開網站）
- 只取「單字清單」這種事實；**中文解釋、例句、對話、語音、圖示都是自己編寫／合成**，不放書上的插圖、不放書附 MP3、不照抄書上的對話。
- MP3 只在本機用 faster-whisper（base.en）轉文字，拿來核對單字清單，轉文字結果不進專案（存在 scratchpad）。書中第一類「居家」對應 Track 001–020（奇數軌＝單字表、偶數軌＝對話，每 2 軌一個主題，共 10 個主題；第 1 軌 In a home、3 In a living room、5 In a living room, too、7 In a bathroom、9 toiletries、11 In a bedroom、13 In a basement、15 In a kitchen、17 kitchenware、19 Tools）。
- 圖示用 emoji（示意）；不好表示的字以中文解釋為主。
- **目錄 14 張分類卡改成照片（2026-11-03 使用者要求，在 english-quiz 的工作階段做）**：`img/cats/<分類id>.jpg`（Pexels，16:10、640×400，出處在 `img/cats/PHOTO-CREDITS.md`），`index.html` 的 `draw()` 在卡片上方放 `<img class="ph">`，載入失敗時自動換回原本的 emoji。使用者選「先換分類卡，單字之後再一個主題一個主題換」——單字圖示目前仍是 emoji，之後要換照片就照 english-quiz 單字區的做法（Pexels 搜尋→逐張檢查→裁切→附出處）。
- **居家 10 個主題的單字改成照片（2026-11-03）**：照片放 `img/words/<主題id>/<slug>.jpg`（Pexels，4:3、640×480，出處在 `img/words/PHOTO-CREDITS.md`）。`tools/build_topic.py` 發現有照片就在單字資料加 `photo` 欄位，`topic.html` 的單字卡（`cardPic`）和看圖選字／拼字題（`quizPic`）優先用照片，沒有才用 emoji；場景圖的小圖示仍是 emoji。173 個字有 154 張照片，其餘 19 個（wall、toilet、scale、razor blade、scissors、ladle、cleaver、rice cooker、hot mitt、plastic wrap、fluorescent light、ladder、bucket、dryer、undershirt、two-pronged fork、bottle opener、rice spatula、paint）找不到清楚合適的照片，保留 emoji。換新照片後要重跑 `python tools/build_topic.py <名稱>`。其他類還是 emoji，之後一類一類換。
- **校園的單字改成照片（2026-11-03）**：做法同居家。school-1 校園場所、school-2 教室、school-3 文具、school-8 地理共 76 字，有 67 張照片；沒有合適照片的保留 emoji：principal's office、guidance counselor's office、class schedule、desk mat、overhead projector、correction fluid、stapler、glue、basin。school-4 月份星期、school-5 顏色、school-6 形狀與數學符號、school-7 標點符號是抽象的，照片反而看不懂，整個主題保留 emoji／符號。出處一起寫在 `img/words/PHOTO-CREDITS.md`。
- **醫院的單字改成照片（2026-11-03）**：hospital-1～3 共 46 字，有 42 張照片；保留 emoji 的是 emergency room（找不到清楚的急診室照片）、ear thermometer（搜到的都是耳鏡）、draw blood、blood transfusion（避免血液畫面）。手術類照片選沒有傷口、血的。
- **人（people）的單字改成照片（2026-11-05 公司電腦，使用者說「繼續換照片」）**：people-1～6 共 113 字，有 82 張照片。保留 emoji 的：親戚稱謂（uncle、aunt、cousin、nephew、niece、各種 in-law、elder brother、younger sister、wife、husband，照片看不出關係）、內臟（brain、lung、liver、heart、stomach、intestine）、會露身體或內衣的字（buttocks、navel、chest、abdomen、thigh、bra、panties、pantyhose、boxers）、skirt、gown、scrunchie、tie clip（找不到合適照片）。
  做法（可重複用在其他分類）：在內建瀏覽器開 pexels.com，用 JS fetch `/search/<關鍵字>/` 讀 `__NEXT_DATA__` 的 `props.pageProps.initialData.data`（取橫的照片 id、slug）→ 挑一張 → Python 下載 `images.pexels.com/photos/<id>/pexels-photo-<id>.jpeg?w=1280`（少數檔名不同，從照片頁的 og:image 取）→ 置中裁 4:3、640×480 → 做縮圖總表逐張看過（暴露、看不清楚、幾乎全白的換掉）→ 出處加到 PHOTO-CREDITS.md → `python tools\build_topic.py people1 …`。
- **交通（transport）的單字改成照片（2026-11-05）**：transport-1～4 共 61 字，有 54 張照片（交通標誌用真的路牌照片）。保留 emoji：no U-turn、signal ahead、merge、no right turn（找不到清楚的標誌）、corner、curb、traffic light（照片看不出重點）。
  還沒換的分類：航空、城內、動植物、食物、休閒、運動、餐廳、機器、其他。測驗方式（使用者想改成跟 english-quiz 國中 2000 字一樣）也還沒改。

## 結構
- `index.html`：14 類目錄＋主題清單（`TOPICS` 物件，做好一個主題就加一筆）。
- `topic.html?t=<主題id>`：單一頁面引擎。分頁分兩框：「學習」（圖解單字、情境對話）與「測驗」（看圖選字、聽音選字、拼字，各 10 題，固定種子出題）。
- 測驗規則（使用者的固定要求）：送出前可改答案；每項底下「送出成績」，全部作答才送；送出後標出對錯與正解、鎖住；自動帶登入者（localStorage `quizStudentName`）；`Points.earn` ＋ POST 到英文測驗系統同一份試算表（week=`Vocab｜主題`）；送出後提示其他測驗還差幾題。家長（PARENT）只記點數。
- **測驗套用段考題庫的新規則（2026-10-18 使用者要求）**：送出成績自動對答案（綠對紅錯、標你的答案與正解）→ 有錯題時上方「✏️ 訂正錯誤」：答對的題目鎖住、錯題清空重答（黃框）→「送出訂正」再對答案，直到全對；全部訂正完成補送 1 點（`Points.earn` `kind:'fix-bonus'`，label＝`Vocab｜主題・測驗名`，三種測驗各自可補送）。還有錯題沒訂正完不能離開這一頁（擋連結、關分頁跳確認）；測試帳號 TEST、家長 PARENT 有「🚪 立即離開」（回圖解單字目錄／主頁面）。點數只算第一次作答。試算表：每次訂正記一筆，mode＝`測驗名【第 N 次訂正】`（只含訂正的題目），全部訂正完成另記 `測驗名【全部訂正完成】補送 1 點`。**暫存**：「💾 暫存」＋作答時自動暫存（localStorage `vocabDraft:主題:登入者`），下次打開同一主題自動接續，送出後清掉。程式在 `topic.html` 的 `drawQuiz()`、`fixBarHtml()`、送出處理與暫存區塊（`z.status`：open／graded／fixing）。
- 情境對話有「▶ 全部播放」（2026-10-13）：一句接一句播，正在播的那句加金框、自動捲到；再按一次停止；切換分頁或單獨按某句 🔊 會停止。程式在 `topic.html` 的 `playAll()`／`stopAll()`。
- `topics/<id>.js`：由 `tools/build_topic.py` 從 `tools/data_<名稱>.py` 產生（不要手改）。
- `audio/<id>/`：`w-<單字>.mp3`（單字）、`e-<單字>.mp3`（例句）、`d-NN.mp3`（對話）。`python tools/make_audio.py <id>` 用 Kokoro 產生（模型借用 ../daily_life_listening/tools/models）。聲音：單字與例句 af_heart；對話 Mia=af_sarah、Ben=am_michael。
- `points.js`：點數存摺前端副本（第 7 份；主檔在 english-quiz-plan/points/points.js，改主檔要同步）。

## 新增主題的做法
1. 看書頁照片或 MP3 轉文字取得單字清單（事實）。
2. 複製 `tools/data_home1.py`，寫單字（英文、中文、詞性、emoji、例句＋中文）和一段原創對話（用到該主題的 8 個以上單字）。
3. `python tools/build_topic.py <名稱>` → `python tools/make_audio.py <id>` → 在 `index.html` 的 `TOPICS` 加一筆 → 瀏覽器測試。

## 場景圖
- 每個主題有「🗺️ 場景圖」分頁（自己畫的簡單 SVG＋編號圓點，對應書上『圖＋編號』的學習方式，但不是書上的圖）。home-1 的在 `tools/scene_home1.py`；home-2～10 在 `tools/scenes_home.py`（`pos` 值 `(x,y)`＝圓點放在圖上的物件；`(x,y,'e')`＝放該字 emoji；`pos={}` 的主題＝自動排成架子，盥洗用品、廚房用具、工具用這種）。`build_topic.py` 會檢查每個單字都有位置。`topic.html` 的 `drawScene()` 負責畫圖。`index.html` 的 `TOPICS` 要記得加新主題。`topics/*.js` 與 `audio/` 都要一起提交。
- 2026-10-13：架子格的編號圓點改放在 emoji 左邊（太靠左就放右邊），不再蓋住圖。籃球場（sports-3）改成手繪真實球場（`tools/scene_sports3.py`：俯視球場＋籃框特寫，線條、球員、裁判、板凳、計分板都畫出來）。其他主題要換成真實場景，就照這支寫 `scene_<名稱>.py`（例如 `scene_sports1.py`），`build_topic.py` 會自動採用。雲端環境連不到 Pexels／Wikimedia，沒辦法下載照片。

## 進度
- 2026-10-09：居家 10 個主題全部完成（home-1～10，共 173 個單字、120 句原創對話、約 460 個語音檔、場景圖）。已在瀏覽器逐一驗證：音檔齊全、三種測驗全對都 10/10。客廳（二）故意沒放 ashtray／cigarette（書上有，不適合國中生）。單字清單可由 MP3 轉文字（faster-whisper base.en）取得，中文與詞性我自己填，請使用者抽查。
- 2026-10-09（續）：其餘 13 類全部寫完，目前共 14 類、76 個主題（school 8、hospital 3、people 6、transport 4、air 3、town 6、animals 5、food 7、leisure 2、sports 8、restaurant 6、machines 2、misc 6）。資料在 `tools/txt/<類別><編號>.txt`（格式見 build_topic.py 的 parse_txt），`python tools\build_topic.py 名稱…` 產生 `topics/<類別>-N.js`，不帶參數只重建 catalog。
  - 除居家外，其餘主題的場景圖都是「自動貨架格」（emoji＋編號點），不是手繪房間；對話為原創（依書中單字情境改寫，非書上原文）。
  - 已用瀏覽器確認 76 個主題都能載入（單字數、場景點數、頁面文字）；people-1 只有 8 個單字（本來就少）。
  - 語音：`run_audio.py --no-ex` 先只做單字＋對話；缺 mp3 時瀏覽器會用語音合成補上。之後再跑一次不加 `--no-ex` 補例句語音。尚未全部產生，要看 audio/ 資料夾與 %TEMP%\a_main.log、a_rest.log。
  - 故意略過的單字：ashtray、cigarette、gun、lingerie department 等不適合國中生的。
  - 中文與詞性是我依 ASR 單字表自行填寫，ASR 辨識錯的字（例如 Bullisenboard＝bulletin board）已人工修正，仍請抽查。

## 測驗規則統一以段考題庫為準（2026-10-18 使用者要求，以後新做的測驗也照做）

- **成長學習館各單元有測驗的地方，作答、送出、計分、訂正方式一律以國中英語段考題庫（exam-bank `sync.js`）為準**（使用者已測試驗證 OK）：
  送出成績（全部作答才送）→ 馬上對答案（綠對紅錯＋正解）→ 有錯題時上方「✏️ 訂正錯誤」＋「錯誤全部訂正完畢再另加補送 1 點」（答對的鎖住、錯題清空重答）→「送出訂正」直到全對 → 補送 1 點（`Points.earn` `kind:'fix-bonus'`）；
  沒訂正完不能離開這一頁（擋連結、關分頁跳確認）；測試帳號 TEST、家長 PARENT 有「🚪 立即離開」；試算表每次訂正 mode／單元名稱註明「【第 N 次訂正】」、完成記「【全部訂正完成】補送 1 點」；點數只算第一次作答；「💾 暫存」＋自動暫存接續作答。
- 各站的做法：段考題庫 `sync.js`；圖解單字 `topic.html`；國家地理閱讀 `fixkit.js`（`points-glue.js` 載入）；英文測驗系統 `eqfix.js`；美式生活館 `lifefix.js`（engine.js、index.html 用）。
  英文測驗系統、美式生活館是「一題一題做、答完看解說」的形式，使用者選擇保留，只把結果頁改成訂正規則（只重做錯題、直到全對）。
- 這個 repo：`topic.html` 的測驗（見上面「測驗套用段考題庫的新規則」）。

## 連續學習紅利＋稱讚畫面（2026-10-18）

- 送出測驗後跳出稱讚卡（得幾點、連續第幾天、還差幾點到 100 點）；每跨過 100 點跳出大的恭喜兌換畫面。
- 連續學習紅利：第 2 天 +2、第 3、4 天 +3、第 5 天起每天 +4（2026-10-18 使用者改），中斷就重算；不算在每天 50 點上限內；存摺分頁記成類型「紅利」。
- **答對率計分（2026-10-18）**：答對 1 題得幾點看答對率（第三版，2026-10-18 使用者定）：低於 30% 0.25、30～50% 0.5、50～60% 0.8、60～70% 1、70～90% 1.2、90% 以上 1.5、全對 2，四捨五入成整數（80～90% 使用者沒另外寫，同 7～8 成）；後端 `Code.gs` 的 `CONFIG.RATE_TIERS`，要重新部署 Apps Script 才生效。
- **段考訂正完成補送 1 點（2026-10-18）**：段考題庫錯題全部訂正完成後 `Points.earn({kind:'fix-bonus'})`，後端 `fixBonus_()` 記一筆類型「訂正獎勵」+`CONFIG.FIX_BONUS`（1）點，同一份考卷每天一次、不算每天上限與連續天數；要重新部署 Apps Script 才生效（舊版後端會當成一般賺點、全對每題 2 點＝給 2 點）。
- 程式在 `points.js`（7 份副本內容一致，主檔在 english-quiz-plan `points/points.js`）與後端 `Code.gs`（`CONFIG.STREAK_BONUS`）。
- **要先更新 Apps Script 後端（貼新版 Code.gs → 部署新版本）紅利才會開始算**，步驟在 english-quiz-plan `points/README-點數存摺.md` 最後一節。
