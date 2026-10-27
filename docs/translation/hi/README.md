<!-- Copyright (c) 2026 kraynux - kraynux@proton.me - Licence MIT (voir fichier LICENSE) -->
<div align="center">
  <img src="https://raw.githubusercontent.com/kraynux/kraynux/refs/heads/main/docs/assets/omega-suite.png" alt="Omega-Suite" width="384">
</div>


#  OMEGA-SUITE

**सभी "OMEGA" स्कैनर एक ही इंटरफ़ेस और एक साझा लाइब्रेरी में एकीकृत**

> **kraynux** द्वारा **Omega-server** के लिए विकसित 
[kraynux.snake-mackarel](https://kraynux.snake-mackarel.ts.net)

आधिकारिक पेज: [OMEGA-SUITE](https://kraynux.snake-mackarel.ts.net/omega-suite/) &nbsp;   
स्क्रीनशॉट → [omega-scan](https://kraynux.snake-mackarel.ts.net/omega-scan/screenshots/) · [omega-check](https://kraynux.snake-mackarel.ts.net/omega-check/screenshots/) · [omega-deep](https://kraynux.snake-mackarel.ts.net/omega-deep/screenshots/) · [omega-fold](https://kraynux.snake-mackarel.ts.net/omega-fold/screenshots/) · [omega-track](https://kraynux.snake-mackarel.ts.net/omega-track/screenshots/) · [omega-fuzz](https://kraynux.snake-mackarel.ts.net/omega-fuzz/screenshots/) · [omega-stress](https://kraynux.snake-mackarel.ts.net/omega-stress/screenshots/) 

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](../../../LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/Platform-Linux-informational.svg)](https://www.linux.org/)
[![Interface](https://img.shields.io/badge/Interface-Textual%20TUI-cyan.svg)](https://github.com/Textualize/textual)

**भाषाएँ:**
<img src="https://flagcdn.com/w20/fr.png" alt="France" style="height:14px;"> [Français](../../../README.md) · <img src="https://flagcdn.com/w20/gb.png" alt="English" style="height:14px;"> [English](../en/README.md) · <img src="https://flagcdn.com/w20/es.png" alt="Español" style="height:14px;"> [Español](../es/README.md) · <img src="https://flagcdn.com/w20/br.png" alt="Português (Brasil)" style="height:14px;"> [Português (Brasil)](../pt-BR/README.md) · <img src="https://flagcdn.com/w20/it.png" alt="Italiano" style="height:14px;"> [Italiano](../it/README.md) · <img src="https://flagcdn.com/w20/de.png" alt="Deutsch" style="height:14px;"> [Deutsch](../de/README.md) · <img src="https://flagcdn.com/w20/nl.png" alt="Nederlands" style="height:14px;"> [Nederlands](../nl/README.md) · <img src="https://flagcdn.com/w20/pl.png" alt="Polski" style="height:14px;"> [Polski](../pl/README.md) · <img src="https://flagcdn.com/w20/ru.png" alt="Русский" style="height:14px;"> [Русский](../ru/README.md) · <img src="https://flagcdn.com/w20/cn.png" alt="中文" style="height:14px;"> [中文](../zh-CN/README.md) · <img src="https://flagcdn.com/w20/vn.png" alt="Tiếng Việt" style="height:14px;"> [Tiếng Việt](../vi/README.md) · <img src="https://flagcdn.com/w20/th.png" alt="ไทย" style="height:14px;"> [ไทย](../th/README.md) · <img src="https://flagcdn.com/w20/id.png" alt="Bahasa Indonesia" style="height:14px;"> [Bahasa Indonesia](../id/README.md) · <img src="https://flagcdn.com/w20/jp.png" alt="日本語" style="height:14px;"> [日本語](../ja/README.md) · <img src="https://flagcdn.com/w20/kr.png" alt="한국어" style="height:14px;"> [한국어](../ko/README.md) · <img src="https://flagcdn.com/w20/in.png" alt="हिन्दी" style="height:14px;"> [हिन्दी](README.md) · <img src="https://flagcdn.com/w20/ae.png" alt="العربية" style="height:14px;"> [العربية](../ar/README.md)

---
**Omega-Suite** **omega-** स्कैनर टूल सूट का एकीकृत इंटरफ़ेस है:  
[omega-scan](https://github.com/kraynux/omega-scan), [omega-check](https://github.com/kraynux/omega-check), [omega-deep](https://github.com/kraynux/omega-deep), [omega-fold](https://github.com/kraynux/omega-fold), [omega-stress](https://github.com/kraynux/omega-stress), [omega-track](https://github.com/kraynux/omega-track) और [omega-fuzz](https://github.com/kraynux/omega-fuzz)  
एक ही TUI एप्लिकेशन में एकत्रित (उपयोगकर्ता की पसंद के अनुसार होम ग्रिड या स्थायी टैब बार), एक साझा लाइब्रेरी [(`omega-lib`)](https://github.com/kraynux/omega-lib) के साथ।


हर टूल अब भी स्वतंत्र रूप से चलाया जा सकता है (`omega-check scan ...`
अब भी काम करता है) - omega-suite एक अतिरिक्त अग्रभाग है, कोई
प्रतिस्थापन नहीं।

आर्किटेक्चर और उपयोगिता से जुड़े निर्णयों के विवरण के लिए
`~/DEV/SUITE/OMEGA-SUITE_SPECIFICATIONS.md` और
`~/DEV/SUITE/DECISIONS_ARCHITECTURE.md` (D-014/D-015) देखें।

## परिचय

Omega-Suite नेटवर्क सुरक्षा के लिए Omega स्कैनरों के **नियंत्रण केंद्र** का काम करता है

### उद्देश्य

- 7 **omega स्कैनर** टूल को एक सुसंगत इंटरफ़ेस में लाना, उन्हें कभी बदले या उनकी जगह लिए बिना।
- 7 टूल के लिए एक थीम, एक रेंडरिंग प्रोफ़ाइल, एक नेविगेशन शैली - 7 बार के बजाय एक बार कॉन्फ़िगर।
- संदर्भ खोए बिना एक टूल से दूसरे पर जाना: हर स्क्रीन स्टैक पृष्ठभूमि में जस का तस रहता है।
- 7 टूल एक साथ होने के बावजूद हल्का बने रहना: पहली वास्तविक बार खोलने से पहले कुछ भी मेमोरी में लोड नहीं होता।

## सुविधाएँ

- Omega-SCAN, -CHECK, -DEEP, -FOLD, -STRESS, -TRACK और -FUZZ के लिए **एक ही TUI एप्लिकेशन** (Textual)।
- चुनने के लिए **दो नेविगेशन शैलियाँ** (सेटिंग्स, तुरंत रीस्टार्ट का प्रस्ताव): होम से बटनों का ग्रिड, या गहराई में भी दिखने वाला स्थायी टैब बार (इतिहास, किसी टूल की सेटिंग्स...), होम पर लौटे बिना।
- **आलसी लोडिंग**: हर टूल (Python कोड और डिपेंडेंसी) सत्र में पहली बार खोलने पर ही इम्पोर्ट होता है - शुरुआत का समय और मेमोरी वास्तव में उपयोग किए गए टूल के अनुपात में रहते हैं।
- **साझा थीम और रेंडरिंग प्रोफ़ाइल**: थीम सभी 7 टूल के लिए एक साथ तुरंत बदलती है; रेंडरिंग प्रोफ़ाइल और नेविगेशन शैली, जो अधिक संरचनात्मक हैं, omega-suite को तुरंत रीस्टार्ट करने का प्रस्ताव देती हैं।
- **संदर्भ-आधारित सहायता**: होम से वैश्विक शॉर्टकट और 7 टूल के दायरे का अवलोकन, किसी टैब से सक्रिय टूल की अपनी सहायता।
- 7 टूल के **एक्सपोर्ट की वैश्विक सफ़ाई** एक क्लिक में (सूट की सेटिंग्स), उन टूल की भी जो सत्र में कभी नहीं खोले गए।
- एक ही एप्लिकेशन साझा करने के बावजूद **7 टूल के बीच सख़्त अलगाव**: एक टूल से दूसरे में शैली या स्थिति का कोई रिसाव नहीं।
- **हर टूल पूरी तरह स्वतंत्र रूप से उपयोग योग्य रहता है** (अपना TUI और CLI, `omega-check scan ...` अब भी काम करता है) - omega-suite उसका केवल एक अतिरिक्त अग्रभाग है, कभी प्रतिस्थापन नहीं।

## इंस्टॉलेशन

आधिकारिक आर्काइव `.tar.gz` फ़ॉर्मेट में दिया जाता है। इंस्टॉलेशन से पहले उसकी अखंडता जाँचें:

```bash
sha256sum omega-suite.tar.gz
```

```bash
./install.sh
./omega-suite.sh
```


## उपयोग
### शुरू करना

```bash
cd ~/omega-suite
./omega-suite.sh
```

###  या बस, यदि alias बनाया गया है, तो टर्मिनल में टाइप करें:
```bash
suite
```
## टर्मिनल संगतता

इंटरैक्टिव इंटरफ़ेस (Textual) टर्मिनल की क्षमताओं (एमुलेटर, आकार) को स्वचालित रूप से पहचानता है और उसके अनुसार अपनी संरचनात्मक स्टाइलशीट (`complete`/`standard`/`reduced`/`mono`) बदलता है, बिना मैनुअल flag के। CLI मोड हमेशा सादे टेक्स्ट में रहता है, टर्मिनल से स्वतंत्र। पूरे `omega-` सूट द्वारा साझा नीति (`omega-lib`, `terminal/policies.py`) — `omega-check`/`omega-fire` जैसी ही।

### पहचाने गए एमुलेटर के अनुसार प्रोफ़ाइल

| एमुलेटर | प्रारंभिक प्रोफ़ाइल |
|---|---|
| Ghostty, Alacritty, WezTerm, Kitty | `complete` |
| Konsole, GNOME Terminal, Terminator, Xfce4 Terminal | `standard` |
| xterm, urxvt, आधुनिक SSH | `reduced` |
| Linux TTY, पुराना SSH | `mono` |
| अपरिचित एमुलेटर | `reduced` (डिफ़ॉल्ट वापसी) |

### टर्मिनल के आकार के अनुसार प्रोफ़ाइल

| न्यूनतम आकार (कॉलम × पंक्तियाँ) | प्रोफ़ाइल की ऊपरी सीमा |
|---|---|
| 120 × 32 | `complete` |
| 100 × 28 | `standard` |
| 80 × 24 | `reduced` |
| इससे कम | `mono` |

अंतिम रूप से चुना गया प्रोफ़ाइल **दोनों में से सबसे प्रतिबंधात्मक** होता है (एमुलेटर और आकार) — 70 कॉलम तक छोटा किया गया फ़ुल-स्क्रीन Ghostty `mono` पर उतर आता है, भले ही उसका एमुलेटर `complete` की अनुमति देता हो। कुंजी `r` से लाइव ताज़ा किया जा सकता है, या सूट की सेटिंग्स (कुंजी `s`) से हाथ से बदला जा सकता है।

## आर्किटेक्चर

### डिज़ाइन सिद्धांत

- **संयोजन का अग्रभाग, कभी 8वीं व्यावसायिक परत नहीं**: omega-suite का अपना कोई `domain/` नहीं है - यह हर प्रोजेक्ट द्वारा स्वतंत्र रूप से पहले से सत्यापित 7 कंटेनरों को जोड़ता है, उनका तर्क दोबारा लागू किए बिना।
- **7 टूल की कोई भी फ़ाइल नहीं बदली जाती।** उनकी साझा स्क्रीन/widget क्लासें मेमोरी में केवल एक बार पैच की जाती हैं, सत्र में उस टूल को पहली बार वास्तव में खोलने पर: CSS अलगाव (कोई टूल कभी दूसरे टूल की शैली नहीं अपना सकता), टूल के आंतरिक « बाहर निकलें » को सूट के होम टैब की ओर मोड़ना, और यदि यह नेविगेशन शैली सक्रिय हो तो टैब बार जोड़ना।
- **`interfaces/tui/` के बाहर `textual` वर्जित** (हर बदलाव पर `import-linter` द्वारा जाँचा गया): `app/` प्रदर्शन से स्वतंत्र रहता है और सिद्धांततः किसी दूसरे इंटरफ़ेस की सेवा कर सकता है।
- **दो स्तरों पर आलसी निर्माण**: किसी टूल का adapter (उसके कोड का इम्पोर्ट), फिर उसका कंटेनर (SQLite डेटाबेस, नेटवर्क प्रोब) - दोनों में से किसी की भी लागत उस विशेष टूल की पहली वास्तविक यात्रा से पहले नहीं चुकाई जाती।

### डेटा संरचना

```text
src/omega_suite/
├── app/              संयोजन: आलसी DependencyContainer, बूटस्ट्रैप, 7 टूल के adapter
│                     (tool_adapters.py), साझा सेटिंग्स (थीम, रेंडरिंग प्रोफ़ाइल, नेविगेशन शैली)
├── infrastructure/   रनटाइम पाथ (var/), सेटिंग्स का भंडारण (JSON)
├── interfaces/
│   ├── tui/          Textual इम्पोर्ट करने वाली एकमात्र जगह: App, सूट की अपनी स्क्रीनें (होम, सेटिंग्स,
│   │                 सहायता, Splash), 7 टूल की स्क्रीनों का मेमोरी में पैच (screen_patching.py)
│   └── cli/          आरक्षित, अभी खाली - हर टूल अपना CLI मोड रखता है, जिसे सीधे बुलाया जाता है
└── ports/            app/ द्वारा अपेक्षित अनुबंध (SettingsStore)
```

## पूर्व-आवश्यकताएँ

### सिस्टम

- Python 3.10+
- Linux (Textual अन्य सिस्टम पर भी चलता है, जिन्हें यह प्रोजेक्ट न परखता है न समर्थित करता है)
- कोई भी टर्मिनल - उसकी वास्तविक क्षमताएँ स्वचालित रूप से पहचानी जाती हैं और रेंडरिंग उनके अनुसार ढलती है (ऊपर « टर्मिनल संगतता » देखें), साधारण TTY तक

### Python डिपेंडेंसी

`pyproject.toml` में घोषित, एक ही वर्चुअल एनवायरनमेंट सबको एक साथ रखता है (`install.sh` देखें):

- `omega-lib`: साझा लाइब्रेरी (थीम, टर्मिनल पहचान, विश्वास स्तर)
- `omega-scan`, `omega-check`, `omega-deep`, `omega-fold`, `omega-stress`, `omega-track`, `omega-fuzz`: 7 एकीकृत टूल, हर एक अपनी सकर्मक डिपेंडेंसी के साथ
- `textual`: TUI इंटरफ़ेस
- विकास डिपेंडेंसी (`pip install -e ".[dev]"`): `pytest`, `pytest-asyncio`, `pytest-cov`, `ruff`, `mypy`, `import-linter`

### एक्सपोर्ट

हर टूल अपने एक्सपोर्ट `var/<टूल>/exports/` में और अपने स्क्रीनशॉट `var/<टूल>/screenshots/` में लिखता है - `var/` उस फ़ोल्डर के सापेक्ष जहाँ से omega-suite चलाया गया, या उसे बदलने के लिए `$OMEGA_SUITE_VAR_DIR`। यह कभी अकेले चलाए गए टूल का डिफ़ॉल्ट `var/` नहीं होता: दोनों उपयोग (स्वतंत्र या सूट में एकीकृत) कभी आपस में नहीं मिलते। हर टूल अपनी सेटिंग्स से अपना गंतव्य फ़ोल्डर फिर से निर्धारित कर सकता है। « सभी एक्सपोर्ट खाली करें » बटन (सूट की सेटिंग्स) इस फ़ोल्डर को सभी 7 टूल के लिए एक साथ खाली करता है, उन टूल के लिए भी जो सत्र में कभी नहीं खोले गए - विवरण के लिए सूट की सहायता देखें (होम से कुंजी `a`)।

---

## सुरक्षा

- omega-suite स्वयं कोई नेटवर्क अनुरोध नहीं करता और कुछ भी स्कैन नहीं करता: यह 7 टूल के प्रदर्शन का समन्वय करता है, और हर टूल अपने सुरक्षा उपाय पूरी तरह बनाए रखता है (हर एक का दायरा सूट की सहायता या उसके अपने README में देखें)।
- omega-suite स्वयं कोई रहस्य या पहचान-विवरण नहीं संभालता। हर टूल जो सहेजता है (पिन किए गए लक्ष्य, इतिहास, अपनी सेटिंग्स) वह उसके अपने उप-फ़ोल्डर `var/<टूल>/` में ही रहता है, सूट द्वारा अपरिवर्तित।
- omega-suite की एकमात्र अपनी स्थिति (थीम, रेंडरिंग प्रोफ़ाइल, नेविगेशन शैली) `var/settings.json` में रहती है, बिना किसी संवेदनशील डेटा के।
- `import-linter` हर बदलाव पर `interfaces/tui/` के बाहर `textual` के किसी भी इम्पोर्ट को रोकता है (आर्किटेक्चर देखें) - यह संरचनात्मक गारंटी है, केवल परंपरा नहीं।

## परीक्षण और गुणवत्ता

```bash
source .venv/bin/activate
pip install -e ".[dev]"
lint-imports        # Dependency Rule जाँचता है (interfaces/tui के बाहर textual वर्जित)
pytest -q
ruff check src tests
mypy -p omega_suite
```

## अनइंस्टॉलेशन

omega-suite अपने फ़ोल्डर और शुरू करने वाले alias के अलावा कुछ नहीं छूता:

1. `install.sh` द्वारा `~/.bashrc` और `~/.zshrc` में जोड़ी गई पंक्ति `alias suite="..."` हटाएँ।
2. `omega-suite/` फ़ोल्डर हटाएँ (वर्चुअल एनवायरनमेंट `.venv/`, डेटा `var/` और सेटिंग्स सहित)।

अलग से इंस्टॉल किए गए 7 टूल (या अपने फ़ोल्डरों में विकास में चल रहे टूल) प्रभावित नहीं होते: हर टूल अपने README के अनुसार स्वतंत्र रूप से इंस्टॉल/अनइंस्टॉल किया जा सकता है।

## लाइसेंस

Omega-Suite **MIT** लाइसेंस के तहत वितरित है। पूरे पाठ के लिए फ़ाइल [`LICENSE`](../../../LICENSE) देखें।

---

> **Omega-Suite — देखें, नियंत्रित करें, ऑडिट करें, बेहतर सुरक्षा के लिए।**
>
> Omega- स्कैनरों के लिए एक एकीकृत TUI इंटरफ़ेस
