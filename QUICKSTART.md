# 🚀 Quick Start Guide

Kom in 15 minuten je eerste klant binnen met dit systeem.

## 1. Setup (5 minuten)

```bash
cd /Users/j.k.devries/clawd/projects/business-booster

# Install dependencies
pip install requests beautifulsoup4

# Test het systeem
python prospect-scanner.py vakgarageblokhuis.nl
```

## 2. Maak je eerste preview (5 minuten)

### Optie A: Gebruik voorbeeld (snelst)
```bash
cd examples
python generate-examples.py
open vakgarageblokhuis.html
```

### Optie B: Scan een eigen prospect
```bash
# Scan website
python prospect-scanner.py www.lokaal-bedrijf.nl --save

# Genereer preview
python generate-frontpage.py lokaal_bedrijf_nl.json preview.html

# Open preview
open preview.html
```

## 3. Upload preview (2 minuten)

### GitHub Pages (gratis)
```bash
# Clone je thebusinessbooster.nl repo
git clone https://github.com/jarnodevries-byte/thebusinessbooster.git

# Maak previews folder
mkdir -p previews
cp preview.html previews/bedrijf.html

# Push
git add previews/bedrijf.html
git commit -m "Add preview for Bedrijf"
git push
```

Preview URL: `https://thebusinessbooster.nl/previews/bedrijf.html`

## 4. Verstuur outreach (3 minuten)

1. Open `outreach-template.txt`
2. Kopieer de "KORTE VARIANT" (beste voor eerste contact)
3. Vul in:
   - `{{BUSINESS_NAME}}` → Bedrijfsnaam
   - `{{CONTACT_NAME}}` → Contactpersoon (of "team")
   - `{{PREVIEW_URL}}` → Je preview link
4. Verstuur via Gmail/Outlook

**Voorbeeld:**
```
Onderwerp: Vakgarage Blokhuis - website upgrade?

Beste team Vakgarage Blokhuis,

Ik bezocht vakgarageblokhuis.nl en zie veel potentieel.

Om te laten zien wat mogelijk is, heb ik een moderne preview gemaakt:
👉 https://thebusinessbooster.nl/previews/vakgarageblokhuis.html

€150/maand - all-in (design, hosting, onderhoud)

Interesse in een gesprek? 

Groet,
Jarno | The Business Booster
info@thebusinessbooster.nl
```

## 5. Follow-up

**Week 1:** Verstuur email
**Week 2:** Follow-up als geen reactie
```
Onderwerp: Re: Vakgarage Blokhuis - website upgrade?

Beste team,

Heeft u de kans gehad om naar de preview te kijken?
👉 https://thebusinessbooster.nl/previews/vakgarageblokhuis.html

Laat me weten als dit op een beter moment uitkomt!

Groet, Jarno
```

**Week 4:** Laatste poging
```
Laatste keer dat ik u lastigval! 😊

Preview: [link]

Interesse? Laat maar weten. Geen interesse? Ook prima.

Groet, Jarno
```

## 6. Contract

Bij interesse:
```bash
# Open contract in browser
open contract.html

# Print to PDF
# Vul klantgegevens in
# Verstuur voor handtekening
```

## ✅ Checklist Eerste Klant

- [ ] Systeem getest
- [ ] Drie voorbeelden gegenereerd  
- [ ] GitHub Pages opgezet
- [ ] Email account klaar (info@thebusinessbooster.nl)
- [ ] Lijst van 10 prospects gemaakt
- [ ] Eerste 3 previews gegenereerd
- [ ] Eerste 3 emails verstuurd
- [ ] Calendar reminder voor follow-ups
- [ ] Contract klaarliggen

## 🎯 Target Deze Week

- **Dag 1:** Setup + 3 previews maken
- **Dag 2:** 5 outreach emails versturen
- **Dag 3:** 5 outreach emails versturen
- **Dag 4:** Follow-up op reacties
- **Dag 5:** 5 nieuwe outreach emails
- **Dag 6-7:** Rest + nieuwe prospects zoeken

**Verwachting:** 1-2 interested leads na 10-15 emails

## 💡 Pro Tips

**Email timing:** di-do, 10:00-15:00
**Subject line:** Kort en specifiek met bedrijfsnaam
**Preview:** Je sterkste wapen - laat het spreken!
**Persoonlijk:** Noem altijd iets specifieks over hun bedrijf
**No pressure:** Geen verkooppraat, gewoon vriendelijk aanbod

## 🆘 Hulp Nodig?

**Scanner werkt niet:**
```bash
pip install --upgrade requests beautifulsoup4
```

**Preview ziet er raar uit:**
- Check of alle CSS geladen is
- Test in Chrome/Firefox
- Check console voor errors (F12)

**Email komt in spam:**
- Gebruik professioneel email domein
- Start met kleine hoeveelheden (5/dag)
- Personaliseer elke email
- Geen spam trigger words

## 📊 Tracking

Maak een simpele spreadsheet:

| Bedrijf | Email datum | Reactie | Status | Waarde |
|---------|-------------|---------|--------|--------|
| Vakgarage Blokhuis | 16-02-2024 | Ja | Interested | €150/mnd |
| De Mandemaaker | 16-02-2024 | Nee | Follow-up | - |

**Target eerste maand:** 3-5 klanten = €450-750 MRR

## 🚀 Go!

Je hebt alle tools. Nu gewoon doen:

1. **Vandaag:** 3 previews + 3 emails
2. **Deze week:** 15 emails totaal
3. **Deze maand:** First paying customer!

**Veel succes! 💪**

---

*Questions? info@thebusinessbooster.nl*
