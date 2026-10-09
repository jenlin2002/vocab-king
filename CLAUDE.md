# vocab-king（圖解單字）

靜態網站（GitHub Pages：jenlin2002.github.io/vocab-king/）。使用者有 LiveABC《圖解英語單字王》（14 類、73 主題、約 1500 字）和 MP3，要做成成長學習館的一張卡。對象國一、國二。

## 版權原則（公開網站）
- 只取「單字清單」這種事實；**中文解釋、例句、對話、語音、圖示都是自己編寫／合成**，不放書上的插圖、不放書附 MP3、不照抄書上的對話。
- MP3 只在本機用 faster-whisper（base.en）轉文字，拿來核對單字清單，轉文字結果不進專案（存在 scratchpad）。書中第一類「居家」對應 Track 001–020（奇數軌＝單字表、偶數軌＝對話，每 2 軌一個主題，共 10 個主題；第 1 軌 In a home、3 In a living room、5 In a living room, too、7 In a bathroom、9 toiletries、11 In a bedroom、13 In a basement、15 In a kitchen、17 kitchenware、19 Tools）。
- 圖示用 emoji（示意）；不好表示的字以中文解釋為主。

## 結構
- `index.html`：14 類目錄＋主題清單（`TOPICS` 物件，做好一個主題就加一筆）。
- `topic.html?t=<主題id>`：單一頁面引擎。分頁分兩框：「學習」（圖解單字、情境對話）與「測驗」（看圖選字、聽音選字、拼字，各 10 題，固定種子出題）。
- 測驗規則（使用者的固定要求）：送出前可改答案；每項底下「送出成績」，全部作答才送；送出後標出對錯與正解、鎖住；自動帶登入者（localStorage `quizStudentName`）；`Points.earn` ＋ POST 到英文測驗系統同一份試算表（week=`Vocab｜主題`）；送出後提示其他測驗還差幾題。家長（PARENT）只記點數。
- `topics/<id>.js`：由 `tools/build_topic.py` 從 `tools/data_<名稱>.py` 產生（不要手改）。
- `audio/<id>/`：`w-<單字>.mp3`（單字）、`e-<單字>.mp3`（例句）、`d-NN.mp3`（對話）。`python tools/make_audio.py <id>` 用 Kokoro 產生（模型借用 ../daily_life_listening/tools/models）。聲音：單字與例句 af_heart；對話 Mia=af_sarah、Ben=am_michael。
- `points.js`：點數存摺前端副本（第 7 份；主檔在 english-quiz-plan/points/points.js，改主檔要同步）。

## 新增主題的做法
1. 看書頁照片或 MP3 轉文字取得單字清單（事實）。
2. 複製 `tools/data_home1.py`，寫單字（英文、中文、詞性、emoji、例句＋中文）和一段原創對話（用到該主題的 8 個以上單字）。
3. `python tools/build_topic.py <名稱>` → `python tools/make_audio.py <id>` → 在 `index.html` 的 `TOPICS` 加一筆 → 瀏覽器測試。

## 場景圖
- 每個主題有「🗺️ 場景圖」分頁（自己畫的簡單 SVG＋編號圓點，對應書上『圖＋編號』的學習方式，但不是書上的圖）。home-1 的在 `tools/scene_home1.py`；home-2～10 在 `tools/scenes_home.py`（`pos` 值 `(x,y)`＝圓點放在圖上的物件；`(x,y,'e')`＝放該字 emoji；`pos={}` 的主題＝自動排成架子，盥洗用品、廚房用具、工具用這種）。`build_topic.py` 會檢查每個單字都有位置。`topic.html` 的 `drawScene()` 負責畫圖。`index.html` 的 `TOPICS` 要記得加新主題。`topics/*.js` 與 `audio/` 都要一起提交。

## 進度
- 2026-10-09：居家 10 個主題全部完成（home-1～10，共 173 個單字、120 句原創對話、約 460 個語音檔、場景圖）。已在瀏覽器逐一驗證：音檔齊全、三種測驗全對都 10/10。客廳（二）故意沒放 ashtray／cigarette（書上有，不適合國中生）。單字清單可由 MP3 轉文字（faster-whisper base.en）取得，中文與詞性我自己填，請使用者抽查。
- 2026-10-09（續）：其餘 13 類全部寫完，目前共 14 類、76 個主題（school 8、hospital 3、people 6、transport 4、air 3、town 6、animals 5、food 7、leisure 2、sports 8、restaurant 6、machines 2、misc 6）。資料在 `tools/txt/<類別><編號>.txt`（格式見 build_topic.py 的 parse_txt），`python tools\build_topic.py 名稱…` 產生 `topics/<類別>-N.js`，不帶參數只重建 catalog。
  - 除居家外，其餘主題的場景圖都是「自動貨架格」（emoji＋編號點），不是手繪房間；對話為原創（依書中單字情境改寫，非書上原文）。
  - 已用瀏覽器確認 76 個主題都能載入（單字數、場景點數、頁面文字）；people-1 只有 8 個單字（本來就少）。
  - 語音：`run_audio.py --no-ex` 先只做單字＋對話；缺 mp3 時瀏覽器會用語音合成補上。之後再跑一次不加 `--no-ex` 補例句語音。尚未全部產生，要看 audio/ 資料夾與 %TEMP%\a_main.log、a_rest.log。
  - 故意略過的單字：ashtray、cigarette、gun、lingerie department 等不適合國中生的。
  - 中文與詞性是我依 ASR 單字表自行填寫，ASR 辨識錯的字（例如 Bullisenboard＝bulletin board）已人工修正，仍請抽查。
