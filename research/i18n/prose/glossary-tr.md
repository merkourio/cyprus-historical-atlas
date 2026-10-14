# Turkish glossary (tr) – Cyprus Historical Atlas prose

Terminology for translating `chunks/c00–c16.json` into `out/cNN.tr.json`.
**`i18n-existing.json` → `tr` always wins.** Where an entry here clashes with it, follow the JSON (e.g. the era name is *Çanak Çömleksiz Neolitik*, not *Akeramik*). Format: `English → Türkçe`, with a short note where needed.

---

## 0. Style guide

### Register
- Clear, readable Turkish for a general reader, as in good popular-history writing (think *Atlas* / *NTV Tarih*, not a dissertation). Sentences should be shorter than the English if needed, active where possible.
- Modern Turkish (öz Türkçe where natural: *yerleşim, kazı, buluntu, yazıt, kutsal alan*), but use the **proper Ottoman administrative vocabulary** for the Ottoman period (*eyalet, sancak, kaza, beylerbeyi, muhassıl, kadı, iltizam, malikâne, cizye, vakıf, reaya, Babıâli*). Give a short gloss the first time a term appears in a string if the English glosses it (e.g. "the cizye or poll tax" → "cizye, yani baş vergisi").
- Circumflex only where it changes meaning or is customary in history writing: *malikâne, Babıâli, Hükûmet* not needed (write *hükümet*), *merkezî, idarî* (relative -î kept, as in existing JSON: *merkezî*).
- Archaeological terms: follow Turkish Anatolian/Cypriot archaeology usage (Ankara Üniversitesi Kıbrıs Arkeolojisi, DergiPark/Belleten usage): *astarlı* = slip, *perdahlı* = burnished/polished, *boyalı* = painted, *bezemeli* = decorated, *çark yapımı* = wheelmade, *el yapımı* = handmade.

### Neutrality and place names
- Place names: **exactly as in `i18n-existing.json`**. Pattern: established Turkish names for towns and many villages (Lefkoşa, Gazimağusa, Girne, Baf, Limasol, Larnaka, Güzelyurt, Lapta, Değirmenlik, Tuzla, Beylerbeyi, Ağrotur, Dikelya, Pile, Piskopi, Kukla, Trodos, Beşparmak, Mesarya, Karpaz, Maraş, Erenköy, Dipkarpaz, Tatlısu, Yiğitler, Düzce, Boltaşlı, Sipahi, Akdeniz [Ayia Irini]); Greek names in plain Latin transliteration for southern villages without a Turkish name (Kalavasos, Kissonerga, Sotira, Erimi, Alassa, Kakopetria, Lagoudera…). Keep the archaeological double names as in the JSON (*Kalavasos-Tenta*, *Çatalköy-Vrysi*, *Beylerbeyi-Vounous*).
- Ancient cities keep their ancient names: Salamis, Kition, Kurion, Amathus, İdalion, Tamassos, Soli, Marion, Golgoi, Hytroi, Ledra, Karpasia, Konstantia. Paphos: ancient kingdom/city = *Paphos* (*Eski Baf/Palaepaphos*, *Yeni Baf/Nea Paphos* for the two sites); the modern town and district = *Baf*. Kyrenia/Lapithos in any period = *Girne* / *Lapta*.
- Communities: *Greek Cypriots → Kıbrıslı Rumlar*, *Turkish Cypriots → Kıbrıslı Türkler*, *Greek Cypriot/Turkish Cypriot* (adj.) → *Kıbrıslı Rum / Kıbrıslı Türk*. Ancient/medieval *Greeks* → *Yunanlar*; *Greek* (language) → *Yunanca* (*Kıbrıs Yunancası* for the dialect). *Orthodox Christians* → *Ortodoks Hristiyanlar*.
- Translate what the English says, no more, no less. Do not add or strip political colouring: no *Barış Harekâtı*, no *Kıbrıs Rum Kesimi/GKRY*, no *KKTC* unless the English uses the name. See §12 for the agreed renderings of the 1963–1974 vocabulary.

### Names of people
- Ordinals before the name, Roman numerals with a dot: *Evagoras I → I. Euagoras*, *Peter I → I. Pierre*, *Makarios III → III. Makarios*.
- *X of Salamis* (king) → *Salamis Kralı X* in headings, *Salamisli X* or *Salamis kralı X* in running text. Bishops: *Epiphanius of Salamis → Salamisli Epiphanios*.
- **Ancient Greeks/Cypriots**: Greek forms in Latin letters, Turkish-friendly: Euagoras (EN Evagoras), Onesilos, Evelthon, Gorgos, Stasikypros, Nikokles, Nikokreon, Pnytagoras, Pasikypros, Stasanor, Praxippos, Androkles, Eunostos, Menelaos, Kinyras, Zenon (Kitionlu Zenon). Phoenician kings: Baalmilk, Milkyaton, Pumayyaton, Azbaal, Melekiathon (as in English). Assyrian/Persian: Esarhaddon → *Asarhaddon*, Sargon II → *II. Sargon*, Cyrus → *Kiros*, Darius → *Dareios*, Artaxerxes → *Artakserkses*, Alexander → *İskender* (Büyük İskender).
- **Ptolemies and Romans**: Ptolemy → *Ptolemaios* (I. Ptolemaios, *Ptolemaios Makron*); Seleucus → *Selevkos*; Antigonus → *Antigonos*; Demetrius Poliorcetes → *Demetrios Poliorketes*. Romans in Latin form: Augustus, Tiberius, Trajan → *Traianus*, Hadrian → *Hadrianus*, Cato → *Cato*, Cicero → *Cicero*, Sergius Paulus.
- **Byzantines** in Greek form: Isaac Komnenos → *İsaakios Komnenos*, Justinian → *Iustinianos* (I./II. Iustinianos), Constantius II → *II. Konstantios*, Zeno → *Zenon*, Heraclius → *Herakleios*, Nikephoros Phokas → *Nikephoros Fokas*, Alexios Komnenos → *Aleksios Komnenos*, Manuel → *Manuel*, John Doukas → *Ioannis Dukas*, Eumathios Philokales, Rhapsomates (unchanged). Saints/bishops: *Aziz Barnabas, Aziz Lazaros, Aziz Hilarion, Aziz Neofitos* (but site names as JSON: *Ayios Neophytos Manastırı*).
- **Lusignans** in French form (Turkish historiography follows the French): Guy de Lusignan, Aimery → *Amaury* (Aimery acceptable), Hugh → *Hugues* (I. Hugues), Henry → *Henri*, Peter → *Pierre*, James → *Jacques*, John II → *II. Jean*, Janus → *Janus*, Charlotte, Eleanor of Aragon → *Aragonlu Eleonora*. On the first mention in a ruler heading you may add the English form in parentheses only if the English text cross-refers to it; otherwise not.
- **Venetians** in Italian: Caterina Cornaro, Marcantonio Bragadin, Nicolò Dandolo, Sebastiano Venier, Astorre Baglione, Francesco Barbarigo.
- **Ottomans** in Turkish spelling: Lala Mustafa Paşa, Muzaffer Paşa, Piyale Paşa, Ebubekir Paşa, Cil Osman Ağa, Küçük Mehmed, Seyyid Mehmed Emin, II. Selim, Kanuni Sultan Süleyman (EN "Suleiman" → *Süleyman*), II. Mahmud, Kıbrıslı Mehmed Kâmil Paşa. Greek Ottoman-era notables: Hadjigeorgakis Kornesios → *Hacı Yorgaki Kornesios*; Archbishop Kyprianos → *Başpiskopos Kiprianos*.
- **British**: unchanged, with Turkish titles: *Sir Garnet Wolseley*, *Mareşal Sir John Harding*, *Tuğamiral Lord John Hay*, *Sir Ronald Storrs*.
- **Modern**: as they spell themselves in Latin script: Makarios (III. Makarios), Glafkos Klerides (Turkish press usage; EN Glafcos Clerides), Rauf Denktaş, Fazıl Küçük, Spyros Kyprianou, Tassos Papadopoulos, Dimitris Hristofyas (EN Demetris Christofias), Nikos Anastasiadis, Nikos Hristodulidis. Modern scholars: unchanged (Karageorghis, Peltenburg, Dikaios, Gjerstad).
- Gods: Aphrodite → *Afrodit*, Apollo → *Apollon*, Zeus, Athena → *Athena*, Astarte, Melqart → *Melkart*, Reshef, Baal, Herakles, Dionysos, Ishtar → *İştar*, Hathor, Bes. *Paphian Aphrodite → Paphoslu Afrodit*, *Wanassa → Wanassa ("Hanım/Kraliçe")*.

### Titles of works, institutions, quotations
- **Book, article and journal titles stay in English** (and in italics/quotes as in the source); describe them in Turkish ("*Ancient Cyprus* adlı kitap"). Do not translate titles of foreign exhibitions, series or reports.
- Inscriptions/quoted primary texts: translate the quotation into Turkish.
- Museums: translate when there is an established Turkish name (§9), otherwise keep the original + Turkish city name (*Ashmolean Museum, Oxford*).

### Dates and numbers
- BCE → **MÖ**, CE → **MS** (placed before the number: *MÖ 1200*, *MS 365*). CE is mostly omitted, as in English; write MS only where the English writes CE or ambiguity arises.
- c. → **yak.** (*yak. MÖ 4500–3800*). In running text *yaklaşık*, *dolaylarında* or *civarında* are fine.
- Centuries: *4th century BCE → MÖ 4. yüzyıl*; *mid-5th century BCE → MÖ 5. yüzyılın ortası*; *late 6th century → 6. yüzyılın sonu*; *early 13th → 13. yüzyılın başı*; *the 1570s → 1570'ler*; *millennium → binyıl* (*MÖ 9. binyıl*).
- *fl. 431 → 431'de etkin* (in date fields: *etkinliği yak. 478–488*). *before 306 → 306'dan önce*. *Legendary → Efsanevi*. *?–312 BCE → ?–MÖ 312*. Slashes stay: *392/391–362/361 MÖ* → write *MÖ 392/391–362/361*.
- Ranges with en dash, no spaces. Thousands with a dot (*186.173*), decimals with a comma (*1,2 milyon*). Ordinal dates: *9 Eylül 1570*.
- Suffixes on years with apostrophe and vowel harmony: *1571'de, 1878'den, 1960'ta, 1974'ten, MÖ 1200'e dek*.
- Measurements: *m, km, ha (hektar)*, *£70.000 → 70.000 sterlin*.

### Recurring short labels
- In situ → **Yerinde** (*In situ, Khirokitia → Yerinde, Hirokitya*); *In situ (closed to visitors) → Yerinde (ziyarete kapalı)*.
- *with the Department of Antiquities → Eski Eserler Dairesi'nde*; *now in X → bugün X'te*; *lost / whereabouts unknown → kayıp / yeri bilinmiyor*; *private collection → özel koleksiyon*; *destroyed → yıkıldı/yok edildi*.
- *Ruler headings*: *The beylerbeyis → Beylerbeyiler*; *The ten kings of Esarhaddon's prism → Asarhaddon prizmasındaki on kral*.

---

## 1. Periods and chronology

| English | Türkçe | Note |
|---|---|---|
| Epipalaeolithic | Epipaleolitik | |
| Aceramic Neolithic | Çanak Çömleksiz Neolitik | JSON era name; *Akeramik Neolitik* only as an occasional synonym |
| Pre-Pottery Neolithic (A/B) | Çanak Çömleksiz Neolitik (A/B) | PPNA/PPNB → ÇÇN A / ÇÇN B; Cypro-PPNB → Kıbrıs ÇÇN B |
| Cypro-PPNB | Kıbrıs Çanak Çömleksiz Neolitik B | |
| Khirokitia culture | Hirokitya kültürü | |
| Ceramic / Pottery Neolithic | Çanak Çömlekli Neolitik | JSON |
| Sotira culture | Sotira kültürü | |
| Chalcolithic (Early/Middle/Late) | (Erken/Orta/Geç) Kalkolitik | |
| Erimi culture | Erimi kültürü | |
| Philia phase / culture | Philia evresi / kültürü | |
| Bronze Age | Tunç Çağı | not *Bronz Çağı* (JSON uses Tunç) |
| Early / Middle / Late Bronze Age | Erken / Orta / Geç Tunç Çağı | |
| Early Cypriot (EC I–III) | Erken Kıbrıs (EK I–III) | keep sub-phase numerals: *Erken Kıbrıs III* |
| Middle Cypriot (MC) | Orta Kıbrıs (OK) | |
| Late Cypriot (LC IA … IIIB) | Geç Kıbrıs (GK IA … IIIB) | *Late Cypriot IIC → Geç Kıbrıs IIC* |
| Iron Age | Demir Çağı | |
| Cypro-Geometric (CG I–III) | Kıbrıs-Geometrik (KG I–III) | |
| Cypro-Archaic (CA I–II) | Kıbrıs-Arkaik | era label: *Arkaik* |
| Cypro-Classical | Kıbrıs-Klasik | era label: *Klasik* |
| Archaic / Classical | Arkaik / Klasik | |
| Hellenistic | Helenistik | |
| Roman (Early/Late) | (Erken/Geç) Roma | |
| Late Antiquity, late antique | Geç Antik Çağ, geç antik | |
| Early Christian | Erken Hristiyan | |
| Byzantine (Early/Middle/Late) | (Erken/Orta/Geç) Bizans | |
| Post-Byzantine | Bizans sonrası | |
| Arab raids (period of) | Arap akınları (dönemi) | |
| Condominium (688–965) | ortak yönetim dönemi | JSON: *Bizans ile Halifelik arasında ortak yönetim* |
| Frankish / Lusignan period | Frank / Lüzinyan dönemi | |
| Venetian period | Venedik dönemi | TDV: *Venedik idaresi* |
| Ottoman period | Osmanlı dönemi | |
| British period / colonial period | İngiliz dönemi / sömürge dönemi | |
| Dark Age (Greece) | Karanlık Çağ | |
| Bronze Age collapse | Tunç Çağı çöküşü | |
| Sea Peoples | Deniz Kavimleri | |
| Amarna letters | Amarna mektupları | |
| prehistory, prehistoric | tarihöncesi, tarihöncesi (sıfat) / prehistorik | |
| protohistoric | protohistorik | |
| phase / horizon / level / stratum | evre / ufuk / tabaka / tabaka | |
| hiatus, gap | kesinti, boşluk | |
| radiocarbon date | radyokarbon tarihi | *radiocarbon dating → radyokarbon tarihlemesi* |
| millennium | binyıl | |

## 2. Peoples, languages, scripts

| English | Türkçe | Note |
|---|---|---|
| Cypriots / first Cypriots | Kıbrıslılar / ilk Kıbrıslılar | |
| Eteocypriot(s) | Eteokıbrıslı(lar); dil: Eteokıbrısça | JSON: *Eteokıbrıslı Amathus* |
| Cypro-Minoan (script) | Kıbrıs-Minos yazısı | |
| Cypriot syllabary / syllabic script | Kıbrıs hece yazısı | *syllabic inscription → hece yazılı yazıt* |
| Arcado-Cypriot (dialect) | Arkadya-Kıbrıs lehçesi | |
| Linear A / Linear B | Lineer A / Lineer B | |
| Greek alphabet / Phoenician alphabet | Yunan alfabesi / Fenike alfabesi | |
| koine | koine (ortak Yunanca) | |
| Phoenicians, Phoenician | Fenikeliler, Fenike (sıfat) | *Phoenician Kition → Fenike Kition'u* |
| Achaeans / Mycenaeans | Akhalar / Mikenliler | |
| Aegean(s) | Ege halkları; sıfat: Egeli/Ege | |
| Levantine | Levant (sıfat: Levantlı) | |
| Anatolian | Anadolulu, Anadolu (sıfat) | |
| Assyrians, Egyptians, Persians | Asurlular, Mısırlılar, Persler | |
| Franks, Frankish | Franklar, Frank | |
| Latins, Latin (church) | Latinler, Latin | |
| Genoese | Cenevizliler, Ceneviz | JSON: *Cenevizli Gazimağusa* |
| Venetians | Venedikliler | |
| Maronites | Maruniler | |
| Armenians | Ermeniler | |
| Linobambaki | Linobambaki ("keten-pamuklular"), gizli Hristiyanlar | |
| Muslims / Christians / Jews | Müslümanlar / Hristiyanlar / Yahudiler | |
| refugees / displaced persons | mülteciler / yerinden edilmiş kişiler (göçmenler) | Turkish Cypriot usage also *göçmen* |
| missing persons | kayıp şahıslar | *Committee on Missing Persons → Kayıp Şahıslar Komitesi* |

## 3. Pottery and wares

General: *ware → mal / seramik grubu*; use **"X seramiği"** in running text (*Red Polished pottery → Kırmızı Perdahlı seramik*), and capitalised ware names. On first use in a string the English name may follow in brackets when the text is technical.

| English | Türkçe | Note |
|---|---|---|
| pottery / ceramics | çanak çömlek / seramik | |
| ware | mal, seramik (grubu) | *Red Polished Ware → Kırmızı Perdahlı mal/seramik* |
| sherd(s) | (seramik) parça(ları) | |
| vessel | kap | |
| slip / slipped | astar / astarlı | |
| burnished / polished | perdahlı | |
| painted | boyalı | |
| incised / incised decoration | kazıma / kazıma bezemeli | |
| combed | tarak bezemeli | |
| handmade / wheelmade | el yapımı / çark yapımı | |
| potter's wheel | çömlekçi çarkı | |
| kiln | fırın (çömlekçi fırını) | |
| fabric / clay | hamur / kil | |
| Combed Ware (Sotira/Neolithic) | Tarak Bezemeli seramik | |
| Red-on-White | Beyaz Üzerine Kırmızı (Red-on-White) | Chalcolithic |
| Red and Black Stroke-Burnished | Kırmızı-Siyah Çizgi Perdahlı | |
| Dark Faced Burnished | Koyu Yüzlü Perdahlı | |
| Red Polished | Kırmızı Perdahlı | Ankara Üniv. usage |
| Philia Red Polished | Philia Kırmızı Perdahlı | |
| Black Polished | Siyah Perdahlı | |
| Black Slip | Siyah Astarlı | |
| White Painted | Beyaz Boyalı | (WP I–VI) |
| Red Slip | Kırmızı Astarlı | not to be confused with Late Roman *Kıbrıs Kırmızı Astarlı* (Cypriot Red Slip, sigillata) |
| Red-on-Black | Siyah Üzerine Kırmızı | |
| Black-on-Red | Kırmızı Üzerine Siyah | Cypro-Phoenician |
| Bichrome | İki Renkli (Bichrome) | |
| Bichrome Wheelmade | Çark Yapımı İki Renkli | |
| Monochrome | Tek Renkli | |
| Proto-White Slip | Proto-Beyaz Astarlı | |
| White Slip (I, II) | Beyaz Astarlı (I, II) | milk bowl → *süt kâsesi* |
| Base Ring (I, II) | Base Ring (Halka Dipli) | keep "Base Ring"; gloss once as *halka dipli* |
| Plain White | Sade Beyaz | |
| White Shaved | Beyaz Kazınmış | |
| Mycenaean pottery / Mycenaean IIIC | Miken seramiği / Miken IIIC | |
| Late Helladic | Geç Hellas | |
| Proto-White Painted | Proto-Beyaz Boyalı | |
| Cypriot Sigillata / terra sigillata | Kıbrıs Sigillatası / terra sigillata | |
| amphora(e) | amfora(lar) | |
| pithos (pithoi) | küp (pithos) | first use *pithos (büyük depolama küpü)* |
| krater | krater | |
| jug / juglet | testi / küçük testi | |
| bowl | kâse, çanak | |
| milk bowl | süt kâsesi | White Slip shape |
| askos | askos | |
| oinochoe | oinokhoe | |
| lamp | kandil | |
| cooking pot | pişirme kabı | |
| spouted bowl | emzikli kâse | |
| tankard | maşrapa | |
| "Pithos House" | Pithos Evi | |

## 4. Prehistoric and Bronze Age material culture

| English | Türkçe | Note |
|---|---|---|
| round house / roundhouse | yuvarlak ev | |
| tholos (tholoi) | tholos (tholoslar) | for Khirokitia houses: *yuvarlak taş ev (tholos)* |
| pit house / sunken house | çukur kulübe / çukur ev | JSON: *çukur kulübe* |
| semi-subterranean dwelling | yarı yeraltı konutu | |
| wattle and daub / mudbrick | dal örgü ve sıva / kerpiç | |
| pisé | kerpiç (sıkıştırılmış toprak) | |
| hearth | ocak | |
| enclosure wall | çevre duvarı | |
| ditch | hendek | |
| well (Neolithic water well) | kuyu | |
| rock shelter | kaya sığınağı | JSON |
| hunters' camp | avcı kampı | JSON |
| pygmy/dwarf hippopotamus | cüce su aygırı | |
| dwarf elephant | cüce fil | |
| fallow deer | alageyik | |
| sheep, goat, cattle, pig | koyun, keçi, sığır, domuz | |
| cat burial | kedi gömüsü | |
| obsidian / chert / flint | obsidyen / çört / çakmaktaşı | |
| picrolite | pikrolit | soft blue-green stone |
| cruciform figurine | haç biçimli figürin | |
| figurine | figürin | |
| plank figure / plank idol | tahta biçimli figür (plank idol) | |
| Lemba Lady | Lemba Hanımı | |
| birth / fertility figure | doğum / bereket figürü | |
| stone vessel / stone bowl | taş kap / taş kâse | |
| quern / grinding stone | el değirmeni taşı / öğütme taşı | |
| millstone | değirmen taşı | |
| spindle whorl | ağırşak | |
| loomweight | tezgâh ağırlığı | |
| pendant / bead | kolye ucu / boncuk | |
| dentalium shell | dentalium kabuğu | |
| grave goods | mezar armağanları | |
| burial / inhumation / cremation | gömü / inhumasyon (toprağa gömü) / kremasyon (yakma) | |
| chamber tomb | oda mezar | |
| shaft grave | kuyu mezar | JSON: *kuyu mezar* |
| pit grave | çukur mezar | |
| cist grave / cist | sandık mezar | |
| dromos | dromos (giriş koridoru) | |
| tumulus | tümülüs | |
| cenotaph | kenotaf (boş mezar) | |
| necropolis / cemetery | nekropol / mezarlık | |
| copper / copper ore | bakır / bakır cevheri | |
| arsenical copper / tin bronze | arsenikli bakır / kalaylı tunç | |
| bronze | tunç (malzeme ve eser: *tunç*; *bronz* acceptable in object labels) | |
| smelting / smelt | ergitme / ergitmek | |
| slag (heap) | cüruf (yığını) | |
| furnace / crucible / tuyère | fırın / pota / körük ağzı | |
| oxhide ingot | öküz derisi biçimli külçe | |
| ingot | külçe | |
| mine, gallery, shaft | maden, galeri, kuyu | |
| metallurgy, metalworking | metalurji, maden işçiliği | |
| olive press / oil press | zeytinyağı presi / yağ işliği | |
| perfume workshop | parfüm atölyesi | Pyrgos-Mavroraki |
| textile / dye / loom | dokuma / boya / dokuma tezgâhı | |
| cylinder seal | silindir mühür | |
| stamp seal / seal | damga mühür / mühür | |
| scarab | skarabe | |
| faience | fayans (sırlı frit) | |
| ivory | fildişi | |
| gold / silver / electrum | altın / gümüş / elektron | |
| clay tablet | kil tablet | |
| ashlar (masonry) | kesme taş (duvarcılığı) | *ashlar building → kesme taş yapı* |
| megalithic | megalitik | |
| stone anchor | taş çapa | |
| shipwreck | batık | *Kyrenia ship → Girne batığı* |
| harbour | liman | |
| warehouse / storeroom | depo / ambar | |
| sanctuary | kutsal alan | JSON |
| temple | tapınak | |
| altar / horns of consecration | sunak / kutsama boynuzları | |
| bothros | bothros (adak çukuru) | |
| temenos | temenos (kutsal alan çevresi) | |
| cult / cult building | kült / kült yapısı | |
| ritual | ritüel, tören | |
| votive / offering | adak / sunu | *votive figures → adak heykelcikleri* |
| hoard | define | *coin hoard → sikke definesi* |
| Great Goddess / goddess | Büyük Tanrıça / tanrıça | |
| bull mask | boğa maskesi | |
| Ingot God | Külçe Tanrı | Enkomi |
| Horned God | Boynuzlu Tanrı | Enkomi |

## 5. Iron Age to Roman: kingdoms, art, monuments

| English | Türkçe | Note |
|---|---|---|
| city-kingdom | kent-krallık | JSON |
| king / queen / royal | kral / kraliçe / kraliyet | |
| dynasty | hanedan | |
| tyrant | tiran | |
| vassal / tribute | vasal (tabi) / haraç, vergi | JSON: *Hitit vasallığı* |
| satrap / satrapy | satrap / satraplık | |
| Beyond the River (satrapy) | Nehrin Ötesi | JSON |
| strategos | strategos (vali-komutan) | JSON |
| proconsul / senatorial province | prokonsül / senato eyaleti | JSON |
| province | eyalet | (Roman) |
| Koinon of the Cypriots | Kıbrıslılar Birliği (Koinon) | |
| Ionian Revolt | İyon İsyanı | |
| King's Peace | Kral Barışı | |
| siege / besieged | kuşatma / kuşatıldı | |
| siege ramp / siege mound | kuşatma rampası | Palaepaphos |
| royal tomb(s) | kraliyet mezarı/mezarları | |
| sacrificed horses / chariot | kurban edilmiş atlar / savaş arabası | Salamis |
| prism (Esarhaddon) | prizma | |
| stele (stelae) | stel (steller) | *Stele of Sargon II → II. Sargon Steli* |
| inscription | yazıt | |
| bilingual | iki dilli | |
| coin / coinage / mint | sikke / sikke basımı / darphane | |
| stater / siglos / tetradrachm | stater / siglos / tetradrahmi | |
| limestone sculpture / statue | kireçtaşı heykel / heykel | |
| terracotta | pişmiş toprak | *terracotta figures → pişmiş toprak heykelcikler* |
| kouros / kore | kuros / kore | |
| sarcophagus (-i) | lahit (lahitler) | *Amathus sarcophagus → Amathus lahdi* |
| relief | kabartma | |
| palace | saray | *Vouni Sarayı* |
| acropolis | akropol | |
| fortification walls | sur duvarları, surlar | |
| agora | agora | |
| theatre / odeon | tiyatro / odeon | |
| gymnasium | gymnasion | |
| baths | hamam (Roma hamamı) | for Roman: *Roma hamamı*; Ottoman: *hamam* |
| nymphaeum | nymphaeum (çeşme anıtı) | |
| aqueduct | su kemeri | JSON |
| villa / House of Dionysos | villa / Dionysos Evi | *House of Theseus → Theseus Villası* (as known in TR); *House of Aion → Aion Evi*; *House of Orpheus → Orfeus Evi*; *House of Eustolios → Eustolios Evi* |
| peristyle | peristil (sütunlu avlu) | |
| mosaic / floor mosaic | mozaik / taban mozaiği | |
| opus sectile | opus sectile | |
| Labours of Heracles | Herakles'in On İki Görevi | |
| Sanctuary of Apollo Hylates | Apollon Hylates Kutsal Alanı | |
| Sanctuary of Aphrodite | Afrodit Kutsal Alanı | |
| Temple of Astarte | Astarte Tapınağı | |
| Tombs of the Kings | Kralların Mezarları | Nea Paphos |
| Jewish revolt (115–117) | Yahudi ayaklanması | |
| earthquake | deprem | |

## 6. Byzantine church and monastic vocabulary

| English | Türkçe | Note |
|---|---|---|
| Church of Cyprus | Kıbrıs Kilisesi | |
| autocephalous / autocephaly | otosefal / otosefali (bağımsızlık) | gloss: *bağımsız (otosefal)* |
| archbishop / archbishopric | başpiskopos / başpiskoposluk | |
| Archbishop of Cyprus | Kıbrıs Başpiskoposu | |
| bishop / bishopric / see | piskopos / piskoposluk / piskoposluk merkezi | |
| metropolitan / metropolis | metropolit / metropolitlik | *Metropolis of Morphou → Güzelyurt Metropolitliği* |
| suffragan bishop | bağlı piskopos | |
| patriarch / patriarchate | patrik / patrikhane (patriklik) | |
| Ecumenical Council | Ekümenik Konsil | *Council of Ephesus → Efes Konsili*; *Nicaea → İznik Konsili*; *Chalcedon → Kadıköy Konsili* |
| Iconoclasm | İkonoklazma (tasvir kırıcılığı) | |
| icon | ikona | |
| miracle-working icon | mucizevi ikona | |
| acheiropoietos | akheiropoietos ("insan eliyle yapılmamış") | |
| church / chapel / cathedral | kilise / şapel / katedral | |
| basilica (three-aisled) | (üç nefli) bazilika | JSON |
| nave / aisle | orta nef / yan nef | |
| apse | apsis | |
| narthex | narteks | |
| naos | naos | |
| bema / templon | bema / templon | |
| iconostasis | ikonostasis | |
| synthronon | synthronon | |
| dome / pendentive / barrel vault | kubbe / pandantif / beşik tonoz | |
| cross-in-square | kapalı Yunan haçı planlı | |
| steep-pitched timber roof | dik eğimli ahşap çatı | Troodos churches |
| atrium | atriyum | |
| baptistery | vaftizhane | |
| ambo | ambon | |
| reliquary / relic | röliker / kutsal emanet (rölik) | |
| fresco / wall painting | fresk / duvar resmi | |
| painted church | freskli kilise | JSON |
| programme (of paintings) | resim programı | |
| Pantokrator | Pantokrator | |
| Virgin, Theotokos, Panagia | Meryem Ana, Theotokos, Panagia | keep *Panagia* in proper names |
| Tree of Jesse | İşay Ağacı | |
| Deesis | Deesis | |
| Annunciation / Ascension / Dormition | Müjde / Göğe Yükseliş / Meryem'in Ölümü (Koimesis) | |
| Last Judgement | Son Yargı (Kıyamet) | |
| apse mosaic (Kiti, Kanakaria) | apsis mozaiği | |
| Italo-Byzantine | İtalyan-Bizans | |
| monastery / convent | manastır | |
| katholikon | katholikon (manastırın ana kilisesi) | |
| abbey | manastır kilisesi / manastır | JSON *Abbey → Manastır kilisesi*; Bellapais = *Bellapais Manastırı* |
| abbot / hegumen | başrahip / igumen | |
| monk / nun / hermit | keşiş, rahip / rahibe / münzevi | |
| enkleistra / hermitage | enkleistra (inziva hücresi) / inziva yeri | |
| founder (ktetor) / donor portrait | kurucu (ktitor) / bağışçı portresi | |
| pilgrim / pilgrimage | hacı / hac (ziyaret) | |
| saint / St | Aziz / Azize | in site names follow JSON (*Ayios, Ayia, Panagia*) |
| theme (Byzantine province) | thema | JSON: *themanın merkezi* |
| katepano / doux | katepano / duks | |
| governor (Byzantine) | vali | |
| Arab raids | Arap akınları | |
| Constantinople | Konstantinopolis | JSON |

## 7. Lusignan, Genoese and Venetian periods

| English | Türkçe | Note |
|---|---|---|
| Kingdom of Cyprus | Kıbrıs Krallığı | |
| Lusignan dynasty | Lüzinyan Hanedanı | |
| Lord of Cyprus | Kıbrıs Senyörü | |
| King of Jerusalem / of Armenia | Kudüs Kralı / Ermeni Kralı | titular → *unvanen* |
| coronation | taç giyme (töreni) | |
| regent / regency | naip / naiplik | |
| Crusade / crusader | Haçlı Seferi / Haçlı | |
| Templars | Tapınak Şövalyeleri | |
| Hospitallers / Knights of St John | Hastane Şövalyeleri / Saint-Jean Şövalyeleri | |
| Commandery (Kolossi) | Komutanlık (commanderie) | *Grand Commandery → Büyük Komutanlık* |
| Teutonic Knights | Töton Şövalyeleri | |
| High Court (Haute Cour) | Yüksek Divan (Haute Cour) | |
| Assizes of Jerusalem | Kudüs Kanunları (Assises de Jérusalem) | |
| vassal / liege lord / fief | vasal / metbu (senyör) / fief (dirlik) | gloss *fief* once as *dirlik*; do not use *tımar* for Lusignan fiefs |
| knight / baron / noble | şövalye / baron / soylu | |
| seneschal / constable / marshal / chamberlain | seneşal / konstabl / mareşal / mabeyinci | |
| bailli / bailiff | bailli (vekil, kâhya) | Genoese/Venetian *bailo* → *balyos* |
| serfs (paroikoi) | serfler (parikoi) | |
| francomati (free peasants) | frankomati (özgür köylüler) | |
| Latin archbishop / Latin church | Latin başpiskoposu / Latin Kilisesi | |
| Bulla Cypria | Bulla Cypria | |
| Gothic (cathedral) | Gotik (katedral) | |
| Saint Sophia, Nicosia | Ayasofya Katedrali (bugün Selimiye Camii) | |
| Saint Nicholas, Famagusta | Aziz Nikolaos Katedrali (bugün Lala Mustafa Paşa Camii) | |
| War of the Lombards | Lombard Savaşı | |
| Black Death / plague | Kara Ölüm / veba | |
| Mamluk invasion (1426), Battle of Khirokitia | Memlük seferi, Hirokitya Muharebesi | |
| sugar works / sugar plantation | şeker işliği / şeker kamışı tarlası | JSON |
| Genoese invasion / occupation of Famagusta | Ceneviz istilası / Gazimağusa'nın Ceneviz işgali | |
| Venetian Republic / Serenissima | Venedik Cumhuriyeti | |
| Doge | Doç (Venedik Doçu) | |
| Luogotenente | Luogotenente (vali) | JSON |
| Provveditore | Provveditore (askerî müfettiş) | JSON |
| Consiglieri | Consiglieri (danışmanlar) | |
| Captain of Famagusta / Capitano | Gazimağusa Kaptanı (Capitano) | |
| Lieutenant of Cyprus | Kıbrıs Luogotenente'si | |
| stradioti | stradiotlar (Arnavut-Rum atlı askerler) | |
| bastion | tabya | |
| curtain wall | sur perdesi | |
| moat / ditch | hendek | |
| ravelin | ravelin (ön tabya) | |
| citadel / keep | iç kale / burç | *Othello's Tower → Othello Kalesi (iç kale)* |
| castle / fortress / fort | kale / hisar / tahkimat | JSON *Castle → Kale* |
| gate (Famagusta Gate) | kapı (Mağusa Kapısı) | Venetian walls of Nicosia: *Mağusa, Girne, Baf kapıları* |
| watchtower | gözetleme kulesi | JSON |
| camel-track bridge | deve yolu köprüsü | JSON |
| Venetian walls | Venedik surları | |
| siege of Famagusta (1571) | Gazimağusa kuşatması | |
| Lepanto | İnebahtı | |

## 8. Ottoman period

| English | Türkçe | Note |
|---|---|---|
| Ottoman conquest (1570–71) | Osmanlı fethi, Kıbrıs'ın fethi | TDV usage *fetih* is standard in Turkish; neutral enough |
| the Porte / Sublime Porte | Babıâli | |
| Sultan / Grand Vizier | padişah, sultan / sadrazam | |
| Kapudan Pasha | Kaptan-ı Derya (Kaptan Paşa) | |
| Divan | Divan-ı Hümayun | |
| province (Ottoman) | eyalet | JSON |
| Eyalet of Cyprus / beylerbeylik | Kıbrıs Eyaleti / Kıbrıs Beylerbeyliği | |
| sanjak | sancak | |
| kaza (district) | kaza | |
| Cezayir-i Bahr-i Sefid | Cezayir-i Bahr-i Sefid Eyaleti | |
| beylerbeyi (pl. beylerbeyis) | beylerbeyi (beylerbeyiler) | |
| pasha / aga / bey / efendi | paşa / ağa / bey / efendi | |
| governor (Ottoman) | vali; for muhassıl period *muhassıl* | |
| muhassıl | muhassıl | |
| mütesellim | mütesellim | |
| mutasarrıf | mutasarrıf | |
| kadı (judge) | kadı | |
| naib, mufti, defterdar | naib, müftü, defterdar | |
| dragoman (of the Serai) | (saray) tercümanı, dragoman | TDV: *saray tercümanı (dragoman)* |
| archbishop as ethnarch | etnark (millet başı) olarak başpiskopos | |
| millet system | millet sistemi | |
| reaya / subjects | reaya | |
| timar / timariot | tımar / tımarlı sipahi | |
| tax-farm, tax-farming | iltizam | *tax farmer → mültezim* |
| life-lease tax farm | malikâne | |
| poll tax (jizya) | cizye (baş vergisi) | |
| tithe | öşür | |
| avarız | avarız | |
| land survey / tax register | tahrir / tahrir defteri | |
| waqf, pious foundation | vakıf | *Haramayn foundation → Haremeyn vakfı*; *Evkaf → Evkaf (Vakıflar İdaresi)* |
| janissary | yeniçeri | |
| sipahi | sipahi | |
| garrison | garnizon; Ottoman context *muhafız askerleri* | |
| Friday prayer | cuma namazı | |
| mosque / minaret / mihrab / minbar | cami / minare / mihrap / minber | |
| tekke / dervish lodge | tekke / dergâh | *Mevlevi tekke → Mevlevîhane* |
| tomb (of a saint) | türbe | *Tomb of Umm Haram → Ümmü Haram Türbesi* |
| Hala Sultan Tekke | Hala Sultan Tekkesi | JSON site name: *Hala Sultan Tekke* |
| madrasa | medrese | |
| han / caravanserai | han / kervansaray | *Büyük Han, Kumarcılar Hanı* |
| bedesten (covered market) | bedesten | |
| hamam | hamam | |
| fountain / sebil | çeşme / sebil | |
| aqueduct (Bekir Pasha) | Bekir Paşa Su Kemeri | JSON |
| inscription (kitabe) | kitabe | Ottoman building inscriptions → *kitabe*; ancient → *yazıt* |
| Tanzimat | Tanzimat | |
| uprising of 1821 / executions | 1821 olayları / idamlar | |
| locusts | çekirge istilası | |
| plague, famine | veba, kıtlık | |
| Russo-Turkish War (1877–78) | 1877–78 Osmanlı-Rus Savaşı (93 Harbi) | |
| Cyprus Convention (1878) | Kıbrıs Sözleşmesi | |
| consul | konsolos | |

## 9. Institutions, museums, research

| English | Türkçe | Note |
|---|---|---|
| Department of Antiquities (Republic of Cyprus) | Eski Eserler Dairesi (Kıbrıs Cumhuriyeti) | Use *Kıbrıs Eski Eserler Dairesi* if no context |
| Department of Antiquities (colonial, before 1960) | (sömürge yönetiminin) Eski Eserler Dairesi | |
| Turkish Cypriot antiquities authority | Eski Eserler ve Müzeler Dairesi | only when the English refers to it; *Kıbrıslı Türk Eski Eserler ve Müzeler Dairesi* |
| Cyprus Museum, Nicosia | Kıbrıs Müzesi, Lefkoşa | |
| District Museum / District Archaeological Museum | Bölge Müzesi / Bölge Arkeoloji Müzesi | *Larnaca District Museum → Larnaka Bölge Arkeoloji Müzesi* |
| Paphos / Limassol District Museum | Baf / Limasol Bölge Arkeoloji Müzesi | |
| Local Museum (Kouklia, Marion, Idalion) | Yerel Müze (Kukla Yerel Müzesi, Marion-Arsinoe Yerel Müzesi, İdalion Yerel Müzesi) | |
| Kourion Museum, Episkopi | Kurion Müzesi, Piskopi | |
| Byzantine Museum (Archbishop Makarios III Foundation) | Bizans Müzesi (Başpiskopos III. Makarios Vakfı) | |
| Cyprus Medieval Museum (Limassol Castle) | Kıbrıs Orta Çağ Müzesi (Limasol Kalesi) | |
| Larnaca Medieval Museum | Larnaka Orta Çağ Müzesi | |
| Pierides Museum | Pierides Müzesi | |
| Thalassa Museum, Ayia Napa | Thalassa Müzesi, Ayia Napa | |
| Shipwreck Museum, Kyrenia Castle | Batık Müzesi, Girne Kalesi | TC name: *Batık Gemi Müzesi* |
| Kykkos Museum | Kykkos Müzesi | |
| Ethnological Museum / Folk Art Museum | Etnografya Müzesi / Halk Sanatı Müzesi | |
| Museum of Traditional Embroidery | Geleneksel Nakış Müzesi | |
| Cyprus Railway Museum | Kıbrıs Demiryolu Müzesi | |
| Icon Museum (St Barnabas) | İkona Müzesi (Aziz Barnabas) | |
| British Museum, London | British Museum, Londra | *İngiliz Müzesi* acceptable in running text |
| Louvre | Louvre Müzesi, Paris | |
| Metropolitan Museum of Art, New York (the Met) | Metropolitan Sanat Müzesi, New York | |
| Cesnola Collection | Cesnola Koleksiyonu | |
| Penn Museum (University of Pennsylvania Museum) | Penn Müzesi (Pennsylvania Üniversitesi Müzesi), Philadelphia | |
| Ashmolean Museum, Oxford | Ashmolean Müzesi, Oxford | |
| Fitzwilliam, World Museum Liverpool, Vorderasiatisches Museum, Museum of Fine Arts Boston | names kept + *Müzesi* where natural: *World Museum, Liverpool*; *Vorderasiatisches Museum, Berlin*; *Güzel Sanatlar Müzesi, Boston* | |
| Bodrum Museum of Underwater Archaeology | Bodrum Sualtı Arkeoloji Müzesi | |
| National Archives, Kew | Ulusal Arşivler (The National Archives), Kew | |
| Swedish Cyprus Expedition | İsveç Kıbrıs Seferi (Swedish Cyprus Expedition) | |
| expedition / mission | kazı ekibi, araştırma heyeti | |
| University of Cyprus | Kıbrıs Üniversitesi | |
| CAARI | Kıbrıs Amerikan Arkeoloji Araştırma Enstitüsü (CAARI) | |
| Technical Committee on Cultural Heritage | Kültürel Miras Teknik Komitesi | bicommunal → *iki toplumlu* |
| UNESCO World Heritage (Site/List) | UNESCO Dünya Mirası (Alanı/Listesi) | |
| excavation / excavated / dig | kazı / kazıldı, kazılarak açığa çıkarıldı / kazı | |
| season (of excavation) | kazı sezonu | |
| survey | yüzey araştırması | |
| rescue excavation | kurtarma kazısı | |
| stratigraphy | stratigrafi | |
| looting, illicit excavation / antiquities market | yağma, kaçak kazı / eski eser piyasası | |
| repatriation / returned | iade / iade edildi | |
| conservation / restoration | koruma / restorasyon | |
| in situ | yerinde | |
| find(s) | buluntu(lar) | JSON |
| assemblage | buluntu topluluğu | |
| catalogue / excavation report | katalog / kazı raporu | |
| reading list labels | see JSON *read.*: Kitap, Akademik, Makale, Deneme, Birincil kaynak, Kurgu | |

## 10. British period

| English | Türkçe | Note |
|---|---|---|
| occupation and administration (1878) | işgal ve yönetim | JSON |
| annexation (1914) | ilhak | |
| Crown Colony (1925) | Kraliyet Sömürgesi | JSON |
| High Commissioner | Yüksek Komiser | |
| Governor | Vali | |
| Government House | Hükümet Konağı | JSON |
| Chief Secretary | Başsekreter | |
| Commissioner (district) | (kaza) komiseri | |
| Legislative Council | Yasama Meclisi | |
| Executive Council | Yürütme Konseyi | |
| Colonial Office / Secretary of State for the Colonies | Sömürgeler Bakanlığı / Sömürgeler Bakanı | |
| tribute (Cyprus tribute) | Kıbrıs vergisi (haraç) | |
| enosis | enosis (Yunanistan'la birleşme) | |
| taksim | taksim | |
| October 1931 riots (Oktovriana) | 1931 Ekim olayları | |
| Palmerokratia | Palmer yönetimi (Palmerokratia) | |
| EOKA | EOKA | |
| TMT | TMT (Türk Mukavemet Teşkilatı) | |
| Emergency (1955–59) | Olağanüstü hâl (1955–59) | |
| detention camp | gözaltı kampı | |
| Field Marshal / Rear-Admiral / Major-General | Mareşal / Tuğamiral / Tümgeneral | |
| Cyprus Government Railway | Kıbrıs Hükümet Demiryolu | JSON |
| hill station / summer capital | yayla yerleşimi / yazlık başkent | JSON |
| census | nüfus sayımı | |
| Sovereign Base Areas | Egemen Üs Bölgeleri | JSON |
| Zurich and London Agreements | Zürih ve Londra antlaşmaları | JSON |
| Treaty of Guarantee / Treaty of Lausanne | Garanti Antlaşması / Lozan Antlaşması | |

## 11. Republic and after (1960–2026)

| English | Türkçe | Note |
|---|---|---|
| Republic of Cyprus | Kıbrıs Cumhuriyeti | JSON |
| President / Vice-President | Cumhurbaşkanı / Cumhurbaşkanı Yardımcısı | |
| House of Representatives | Temsilciler Meclisi | |
| constitution / breakdown (1963) | anayasa / anayasal düzenin çöküşü | |
| intercommunal violence / fighting | toplumlar arası şiddet / çatışmalar | |
| enclave(s) | yerleşim bölgesi (enklav) | |
| Green Line | Yeşil Hat | |
| buffer zone | ara bölge (BM ara bölgesi) | JSON: *BM Koruma Bölgesi* for the airport — use *ara bölge* generally |
| ceasefire line | ateşkes hattı | JSON |
| UNFICYP / UN peacekeepers | UNFICYP (BM Barış Gücü) / BM barış gücü askerleri | |
| Security Council resolution 550 | Güvenlik Konseyi'nin 550 sayılı kararı | |
| Greek junta | Yunan cuntası | |
| bizonal, bicommunal federation | iki bölgeli, iki toplumlu federasyon | |
| Annan Plan / Crans-Montana | Annan Planı / Crans-Montana | |
| Non-Aligned Movement | Bağlantısızlar Hareketi | |
| European Union / euro | Avrupa Birliği / avro | |
| Federation of Labour (PEO / SEK) | İşçi Federasyonu | |
| Bank of Cyprus | Kıbrıs Bankası | |
| European Capital of Culture | Avrupa Kültür Başkenti | |
| crossing point | geçiş noktası | |

## 12. Sensitive 1963–1974 vocabulary (neutral, faithful renderings)

Translate the English faithfully; these are the agreed, neutral equivalents. Flag to the editor rather than soften or sharpen.

| English | Türkçe | Note |
|---|---|---|
| the 1974 coup | 1974 darbesi (Yunan cuntası destekli darbe) | |
| Turkish invasion (1974) | 1974 Türk işgali / Türkiye'nin işgali (verb: işgal etmek) | EDITOR DECISION: translate the English literally so all three languages say the same thing; do not substitute *müdahale* or *Barış Harekâtı* |
| Turkish army | Türk ordusu | |
| the occupied north | işgal altındaki kuzey (or adanın kuzeyi where only location matters) | EDITOR DECISION: literal, matching the English |
| the north declares itself the Turkish Republic of Northern Cyprus, recognised only by Turkey | kuzey, yalnızca Türkiye'nin tanıdığı Kuzey Kıbrıs Türk Cumhuriyeti'ni ilan eder | full name, no abbreviation |
| government-controlled areas | hükümetin denetimindeki bölgeler | JSON |
| division of the island | adanın bölünmesi | |
| fled / displaced | kaçtı / yerinden edildi | |
| Varosha | Maraş | JSON |
| reunification talks | yeniden birleşme görüşmeleri | |

## 13. General recurring vocabulary

| English | Türkçe | Note |
|---|---|---|
| settlement / village / town / city | yerleşim / köy / kasaba / kent | JSON: *Kent ya da şehir* |
| harbour town / harbour city | liman kasabası / liman kenti | JSON |
| hamlet | mezra, küçük köy | |
| quarter / suburb | mahalle / banliyö | |
| district (modern) | bölge (*Larnaka bölgesi*) | JSON; Ottoman → *kaza* |
| island-wide | ada genelinde | |
| foothills | etekler | *Trodos etekleri* |
| plain / valley / bay / cape / islet | ova / vadi / körfez / burun / adacık | |
| salt lake | tuz gölü | *Larnaka Tuz Gölü* |
| river (Kouris, Pedieos) | ırmak, dere (*Kouris ırmağı*; *Kanlıdere [Pedieos]*) | |
| landmark | simge yapı | JSON |
| works (industrial) | tesis, işlik | JSON |
| trade / exports / imports | ticaret / ihracat / ithalat | |
| carob / olive / wine / cotton / sugar | keçiboynuzu / zeytin / şarap / pamuk / şeker | *Commandaria → Kumandarya şarabı* |
| asbestos mine | asbest madeni | JSON |
| copper-bearing | bakırlı, bakır içeren | |
| water supply / irrigation | su temini / sulama | |
| source(s) (historical) | kaynak(lar) | |
| scholars / historians / archaeologists | araştırmacılar / tarihçiler / arkeologlar | |
| according to tradition / legend | geleneğe göre / efsaneye göre | |
| debated / disputed | tartışmalı | |
| attested | belgelenmiş, (kaynaklarda) geçen | |
| founded / abandoned / destroyed / rebuilt | kuruldu / terk edildi / yıkıldı / yeniden inşa edildi | |
| survives / standing | ayakta kalmıştır / ayakta | JSON *list.standing* |
| closed to visitors | ziyarete kapalı | |
