<!-- Copyright (c) 2026 kraynux - kraynux@proton.me - Licence MIT (voir fichier LICENSE) -->
<div align="center">
  <img src="https://raw.githubusercontent.com/kraynux/kraynux/refs/heads/main/docs/assets/omega-suite.png" alt="Omega-Suite" width="384">
</div>


#  OMEGA-SUITE

**مجموعة ماسحات "OMEGA" كلها موحّدة في واجهة واحدة ومكتبة مشتركة**

> طوّره **kraynux** من أجل **Omega-server** 
[kraynux.snake-mackarel](https://kraynux.snake-mackarel.ts.net)

الصفحة الرسمية: [OMEGA-SUITE](https://kraynux.snake-mackarel.ts.net/omega-suite/) &nbsp;   
لقطات الشاشة ← [omega-scan](https://kraynux.snake-mackarel.ts.net/omega-scan/screenshots/) · [omega-check](https://kraynux.snake-mackarel.ts.net/omega-check/screenshots/) · [omega-deep](https://kraynux.snake-mackarel.ts.net/omega-deep/screenshots/) · [omega-fold](https://kraynux.snake-mackarel.ts.net/omega-fold/screenshots/) · [omega-track](https://kraynux.snake-mackarel.ts.net/omega-track/screenshots/) · [omega-fuzz](https://kraynux.snake-mackarel.ts.net/omega-fuzz/screenshots/) · [omega-stress](https://kraynux.snake-mackarel.ts.net/omega-stress/screenshots/) 

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](../../../LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/Platform-Linux-informational.svg)](https://www.linux.org/)
[![Interface](https://img.shields.io/badge/Interface-Textual%20TUI-cyan.svg)](https://github.com/Textualize/textual)

**اللغات:**
<img src="https://flagcdn.com/w20/fr.png" alt="France" style="height:14px;"> [Français](../../../README.md) · <img src="https://flagcdn.com/w20/gb.png" alt="English" style="height:14px;"> [English](../en/README.md) · <img src="https://flagcdn.com/w20/es.png" alt="Español" style="height:14px;"> [Español](../es/README.md) · <img src="https://flagcdn.com/w20/br.png" alt="Português (Brasil)" style="height:14px;"> [Português (Brasil)](../pt-BR/README.md) · <img src="https://flagcdn.com/w20/it.png" alt="Italiano" style="height:14px;"> [Italiano](../it/README.md) · <img src="https://flagcdn.com/w20/de.png" alt="Deutsch" style="height:14px;"> [Deutsch](../de/README.md) · <img src="https://flagcdn.com/w20/nl.png" alt="Nederlands" style="height:14px;"> [Nederlands](../nl/README.md) · <img src="https://flagcdn.com/w20/pl.png" alt="Polski" style="height:14px;"> [Polski](../pl/README.md) · <img src="https://flagcdn.com/w20/ru.png" alt="Русский" style="height:14px;"> [Русский](../ru/README.md) · <img src="https://flagcdn.com/w20/cn.png" alt="中文" style="height:14px;"> [中文](../zh-CN/README.md) · <img src="https://flagcdn.com/w20/vn.png" alt="Tiếng Việt" style="height:14px;"> [Tiếng Việt](../vi/README.md) · <img src="https://flagcdn.com/w20/th.png" alt="ไทย" style="height:14px;"> [ไทย](../th/README.md) · <img src="https://flagcdn.com/w20/id.png" alt="Bahasa Indonesia" style="height:14px;"> [Bahasa Indonesia](../id/README.md) · <img src="https://flagcdn.com/w20/jp.png" alt="日本語" style="height:14px;"> [日本語](../ja/README.md) · <img src="https://flagcdn.com/w20/kr.png" alt="한국어" style="height:14px;"> [한국어](../ko/README.md) · <img src="https://flagcdn.com/w20/in.png" alt="हिन्दी" style="height:14px;"> [हिन्दी](../hi/README.md) · <img src="https://flagcdn.com/w20/ae.png" alt="العربية" style="height:14px;"> [العربية](README.md)

---
**Omega-Suite** واجهة موحّدة لمجموعة أدوات المسح **omega-**:  
[omega-scan](https://github.com/kraynux/omega-scan) و[omega-check](https://github.com/kraynux/omega-check) و[omega-deep](https://github.com/kraynux/omega-deep) و[omega-fold](https://github.com/kraynux/omega-fold) و[omega-stress](https://github.com/kraynux/omega-stress) و[omega-track](https://github.com/kraynux/omega-track) و[omega-fuzz](https://github.com/kraynux/omega-fuzz)  
مجتمعة في تطبيق TUI واحد (شبكة أزرار في الشاشة الرئيسية أو شريط تبويبات دائم، حسب اختيار المستخدم) مع مكتبة مشتركة [(`omega-lib`)](https://github.com/kraynux/omega-lib).


تبقى كل أداة قابلة للتشغيل بشكل مستقل (`omega-check scan ...`
ما زال يعمل) - فـ omega-suite واجهة إضافية، وليس
بديلًا.

انظر `~/DEV/SUITE/OMEGA-SUITE_SPECIFICATIONS.md` و
`~/DEV/SUITE/DECISIONS_ARCHITECTURE.md` (D-014/D-015) لتفاصيل
خيارات البنية وسهولة الاستخدام.

## التقديم

يعمل Omega-Suite بوصفه **مركز قيادة** لماسحات Omega من أجل أمان الشبكة

### الأهداف

- جمع أدوات **ماسحات omega** السبع في واجهة متسقة، دون تعديلها أو استبدالها أبدًا.
- سمة واحدة، وملف عرض واحد، وأسلوب تنقل واحد للأدوات السبع - تُهيّأ مرة واحدة بدلًا من 7 مرات.
- الانتقال من أداة إلى أخرى دون فقدان السياق: تبقى كل مجموعة شاشات كما هي في الخلفية.
- البقاء خفيفًا رغم جمع الأدوات السبع: لا يُحمَّل شيء في الذاكرة قبل أول فتح فعلي له.

## الوظائف

- **تطبيق TUI واحد** (Textual) لـ Omega-SCAN و-CHECK و-DEEP و-FOLD و-STRESS و-TRACK و-FUZZ.
- **أسلوبا تنقل** للاختيار (الإعدادات، مع اقتراح إعادة التشغيل فورًا): شبكة أزرار من الشاشة الرئيسية، أو شريط تبويبات دائم يبقى ظاهرًا حتى في العمق (السجل، إعدادات أداة...)، دون العودة إلى الشاشة الرئيسية أبدًا.
- **تحميل كسول**: لا تُستورد كل أداة (شيفرة Python والاعتماديات) إلا عند فتحها لأول مرة في الجلسة - فيبقى زمن البدء والذاكرة متناسبين مع الأدوات المستخدمة فعلًا.
- **سمة وملف عرض مشتركان**: تتغير السمة فورًا للأدوات السبع معًا؛ أما ملف العرض وأسلوب التنقل، الأكثر بنيوية، فيقترحان إعادة تشغيل omega-suite على الفور.
- **مساعدة سياقية**: اختصارات عامة ونظرة شاملة على نطاق الأدوات السبع من الشاشة الرئيسية، ومساعدة خاصة بالأداة النشطة من التبويب.
- **حذف شامل للتصديرات** الخاصة بالأدوات السبع بنقرة واحدة (إعدادات المجموعة)، حتى للأدوات التي لم تُفتح قط في الجلسة.
- **عزل صارم بين الأدوات السبع** رغم مشاركة تطبيق واحد: لا تسرّب للأنماط ولا للحالة من أداة إلى أخرى.
- **تبقى كل أداة قابلة للاستخدام باستقلالية تامة** (TUI وCLI خاصتان بها، و`omega-check scan ...` ما زال يعمل) - فـ omega-suite ليس إلا واجهة إضافية، وليس بديلًا أبدًا.

## التثبيت

يُقدَّم الأرشيف الرسمي بصيغة `.tar.gz`. تحقق من سلامته قبل التثبيت:

```bash
sha256sum omega-suite.tar.gz
```

```bash
./install.sh
./omega-suite.sh
```


## الاستخدام
### التشغيل

```bash
cd ~/omega-suite
./omega-suite.sh
```

###  أو ببساطة، إذا أُنشئ الاسم المستعار، اكتب في الطرفية:
```bash
suite
```
## لغات الواجهة

الواجهة متاحة بـ 17 لغة. يتم الاختيار في إعدادات الحزمة («Langue / Language») ويُطبَّق على الأدوات السبع بعد إعادة تشغيل الواجهة؛ ويفرض المتغيّر `OMEGA_SUITE_LANG` لغة طوال جلسة واحدة. ويحدّد إعداد منفصل، «لغة التصدير»، لغة التقارير التي تصدّرها الأدوات السبع. على وحدة التحكم النصية في Linux (TTY)، تُعرض اللغات ذات الكتابة غير اللاتينية بالإنجليزية طوال الجلسة. ويبقى سطر الأوامر بالفرنسية.

## توافق الطرفيات

تكتشف الواجهة التفاعلية (Textual) قدرات الطرفية (المحاكي، والحجم) تلقائيًا وتكيّف ورقة أنماطها البنيوية وفقًا لذلك (`complete`/`standard`/`reduced`/`mono`)، دون أي علم يدوي. يبقى وضع سطر الأوامر دائمًا نصًا بسيطًا، مستقلًا عن الطرفية. سياسة مشتركة بين مجموعة `omega-` كلها (`omega-lib`، `terminal/policies.py`) — مطابقة لسياسة `omega-check`/`omega-fire`.

### ملف العرض حسب المحاكي المكتشف

| المحاكي | ملف العرض الأولي |
|---|---|
| Ghostty, Alacritty, WezTerm, Kitty | `complete` |
| Konsole, GNOME Terminal, Terminator, Xfce4 Terminal | `standard` |
| xterm، urxvt، SSH حديث | `reduced` |
| TTY لينكس، SSH قديم | `mono` |
| محاكي غير معروف | `reduced` (الرجوع الافتراضي) |

### ملف العرض حسب حجم الطرفية

| الحجم الأدنى (أعمدة × أسطر) | سقف ملف العرض |
|---|---|
| 120 × 32 | `complete` |
| 100 × 28 | `standard` |
| 80 × 24 | `reduced` |
| أقل من ذلك | `mono` |

ملف العرض النهائي المعتمد هو **الأكثر تقييدًا بين الاثنين** (المحاكي والحجم) — فـ Ghostty بملء الشاشة بعد تصغيره إلى 70 عمودًا ينزل إلى `mono`، حتى لو كان محاكيه يسمح بـ `complete`. يمكن تحديثه مباشرة بالمفتاح `r`، أو تجاوزه يدويًا من إعدادات المجموعة (المفتاح `s`).

## البنية

### مبادئ التصميم

- **واجهة تركيب، وليست أبدًا طبقة أعمال ثامنة**: لا يملك omega-suite مجلد `domain/` خاصًا به - بل يجمّع الحاويات السبع التي تحقق منها كل مشروع مسبقًا بشكل مستقل، دون إعادة تنفيذ منطقها.
- **لا يُعدَّل أي ملف من ملفات الأدوات السبع.** تُرقَّع فئات الشاشات/العناصر المشتركة لديها في الذاكرة، مرة واحدة فقط، عند أول فتح فعلي لتلك الأداة في الجلسة: عزل CSS (لا يمكن لأداة أبدًا أن ترث نمط أداة أخرى)، وإعادة توجيه « الخروج » الداخلي للأداة إلى التبويب الرئيسي للمجموعة، وإدراج شريط التبويبات إذا كان أسلوب التنقل هذا نشطًا.
- **`textual` ممنوع خارج `interfaces/tui/`** (يتحقق منه `import-linter` عند كل تعديل): يبقى `app/` مستقلًا عن العرض، ويمكنه نظريًا خدمة واجهة أخرى.
- **بناء كسول على مستويين**: محوّل الأداة (استيراد شيفرتها)، ثم حاويتها (قاعدة SQLite، ومجسات الشبكة) - ولا تُدفع كلفة أي منهما قبل أول زيارة فعلية لتلك الأداة بعينها.

### بنية البيانات

```text
src/omega_suite/
├── app/              التجميع: DependencyContainer كسول، والتمهيد، ومحوّلات الأدوات السبع
│                     (tool_adapters.py)، والإعدادات المشتركة (السمة، وملف العرض، وأسلوب التنقل)
├── infrastructure/   مسارات وقت التشغيل (var/)، وتخزين الإعدادات (JSON)
├── interfaces/
│   ├── tui/          المكان الوحيد الذي يستورد Textual: App، وشاشات المجموعة الخاصة (الرئيسية، والإعدادات،
│   │                 والمساعدة، وSplash)، وترقيع شاشات الأدوات السبع في الذاكرة (screen_patching.py)
│   └── cli/          محجوز، فارغ حتى الآن - تحتفظ كل أداة بوضع CLI الخاص بها، ويُستدعى مباشرة
└── ports/            العقود التي يتوقعها app/ (SettingsStore)
```

## المتطلبات المسبقة

### النظام

- Python 3.10+
- Linux (يعمل Textual على أنظمة أخرى، لا يختبرها هذا المشروع ولا يدعمها)
- أي طرفية - تُكتشف قدراتها الفعلية تلقائيًا ويتكيف العرض معها (انظر « توافق الطرفيات » أعلاه)، حتى TTY بسيطة

### اعتماديات Python

معلنة في `pyproject.toml`، وتجمعها كلها بيئة افتراضية واحدة (انظر `install.sh`):

- `omega-lib`: مكتبة مشتركة (السمات، واكتشاف الطرفية، ومستويات الثقة)
- `omega-scan` و`omega-check` و`omega-deep` و`omega-fold` و`omega-stress` و`omega-track` و`omega-fuzz`: الأدوات السبع المدمجة، ولكل منها اعتمادياتها المتعدية الخاصة
- `textual`: واجهة TUI
- اعتماديات التطوير (`pip install -e ".[dev]"`): `pytest` و`pytest-asyncio` و`pytest-cov` و`ruff` و`mypy` و`import-linter`

### التصدير

تكتب كل أداة تصديراتها الخاصة في `var/<الأداة>/exports/` ولقطات شاشتها في `var/<الأداة>/screenshots/` - و`var/` نسبي إلى المجلد الذي شُغّل منه omega-suite، أو `$OMEGA_SUITE_VAR_DIR` لتجاوزه. ولا يكون أبدًا `var/` الافتراضي للأداة عند تشغيلها منفردة: فلا يختلط الاستخدامان (المستقل أو المدمج في المجموعة) أبدًا. ويمكن لكل أداة إعادة تحديد مجلد الوجهة الخاص بها من إعداداتها الخاصة. ويُفرغ زر « إفراغ كل التصديرات » (إعدادات المجموعة) هذا المجلد للأدوات السبع دفعة واحدة، حتى لتلك التي لم تُفتح قط في الجلسة - انظر مساعدة المجموعة (المفتاح `a` من الشاشة الرئيسية) للتفاصيل.

---

## الأمان

- لا يجري omega-suite نفسه أي طلب شبكي ولا يمسح شيئًا: بل ينسّق عرض الأدوات السبع، وتحتفظ كل منها بضماناتها الخاصة كاملة (انظر نطاق كل منها في مساعدة المجموعة، أو في ملف README الخاص بها).
- لا يتعامل omega-suite نفسه مع أي سر أو بيانات اعتماد. وما تخزّنه كل أداة (الأهداف المثبّتة، والسجل، والإعدادات الخاصة) يبقى في مجلدها الفرعي الخاص `var/<الأداة>/`، دون أن تغيّره المجموعة.
- الحالة الوحيدة الخاصة بـ omega-suite (السمة، وملف العرض، وأسلوب التنقل) موجودة في `var/settings.json`، دون أي بيانات حساسة.
- يمنع `import-linter` عند كل تعديل أي استيراد لـ `textual` خارج `interfaces/tui/` (انظر البنية) - وهو ضمان بنيوي، لا مجرد اصطلاح.

## الاختبارات والجودة

```bash
source .venv/bin/activate
pip install -e ".[dev]"
lint-imports        # يتحقق من Dependency Rule (textual ممنوع خارج interfaces/tui)
pytest -q
ruff check src tests
mypy -p omega_suite
```

## إلغاء التثبيت

لا يلمس omega-suite أي شيء خارج مجلده الخاص والاسم المستعار للتشغيل:

1. احذف السطر `alias suite="..."` الذي أضافه `install.sh` في `~/.bashrc` و`~/.zshrc`.
2. احذف المجلد `omega-suite/` (بما فيه البيئة الافتراضية `.venv/` والبيانات `var/` والإعدادات).

لا تتأثر الأدوات السبع المثبتة بشكل منفصل (أو قيد التطوير في مجلداتها الخاصة): تبقى كل منها قابلة للتثبيت/إلغاء التثبيت باستقلالية، باتباع ملف README الخاص بها.

## الرخصة

يُوزَّع Omega-Suite بموجب رخصة **MIT**. راجع الملف [`LICENSE`](../../../LICENSE) للاطلاع على النص الكامل.

---

> **Omega-Suite — راقب، وقُد، ودقّق، لتأمين أفضل.**
>
> واجهة TUI موحّدة لماسحات Omega-
