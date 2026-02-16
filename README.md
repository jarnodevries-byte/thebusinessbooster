# Business Booster - Outreach Systeem

Complete acquisitie-systeem voor lokale bedrijven in Bunschoten-Spakenburg. Moderne websites voor €150/maand.

## 📁 Overzicht

Dit systeem helpt je om:
1. Websites van prospects te scannen en analyseren
2. Automatisch een moderne preview te genereren
3. Een professionele outreach email te sturen
4. Een contract te tekenen met de klant

## 🎯 Bedrijfsmodel

**The Business Booster** (thebusinessbooster.nl)
- **Prijs:** €150/maand (12 maanden = €1.800)
- **Dienst:** Website design, hosting & onderhoud
- **Doelgroep:** Lokale bedrijven met verouderde websites
- **Contact:** info@thebusinessbooster.nl

## 🛠️ Systeem Componenten

### 1. prospect-scanner.py
Scant een website en extraheert belangrijke informatie.

**Gebruik:**
```bash
python prospect-scanner.py vakgarageblokhuis.nl
python prospect-scanner.py demandemaaker.nl --save
```

**Output:**
- Bedrijfsnaam
- Adres, telefoon, email
- Beschrijving/diensten
- Design kwaliteit score (1-10)
- Logo URL

**Output formaat:** JSON

### 2. template.html
Moderne, responsive HTML/CSS template met:
- ✨ Hero sectie met gradient achtergrond
- 📖 Over ons sectie
- 🎯 Diensten grid
- 📍 Contact sectie met Google Maps
- 📱 Mobile-first design
- 🎨 CSS variabelen voor kleuren
- ⚡ Smooth animations

**Features:**
- Glassmorphism effects
- Gradient backgrounds
- Scroll animations
- Responsive grid layouts
- Google Fonts (Inter + Playfair Display)

### 3. generate-frontpage.py
Genereert een complete HTML pagina vanuit prospect data.

**Gebruik:**
```bash
python generate-frontpage.py vakgarageblokhuis.json
python generate-frontpage.py data.json output.html
```

**Functies:**
- Automatische kleurschema's per bedrijfstype
- Service kaarten genereren
- Contact informatie invullen
- Google Maps integratie
- Moderne placeholder images

**Kleurschema's:**
- **Automotive:** Donkerblauw/Oranje (betrouwbaar, krachtig)
- **Restaurant:** Donkergroen/Goud (warm, elegant)
- **Education:** Fris groen/Blauw (dynamisch, jong)

### 4. contract.html
Professioneel juridisch contract in Nederlands.

**Bevat:**
- Partijen (opdrachtnemer/opdrachtgever)
- Dienstverlening specificatie
- Looptijd: 12 maanden
- Prijs: €150/maand (€1.800 totaal)
- Betalingsvoorwaarden
- Intellectueel eigendom
- Aansprakelijkheid
- Handtekeningvelden

**Gebruik:**
Open in browser → Print naar PDF → Invullen en ondertekenen

### 5. outreach-template.txt
Email templates voor acquisitie.

**Bevat:**
- ✉️ Standaard outreach email (professioneel, persoonlijk)
- 📧 Korte variant (eerste contact)
- 🔄 Follow-up variant (na geen reactie)
- 💬 WhatsApp variant (kort en direct)

**Variabelen:**
- `{{BUSINESS_NAME}}` - Bedrijfsnaam
- `{{CONTACT_NAME}}` - Contactpersoon
- `{{WEBSITE_URL}}` - Huidige website
- `{{PREVIEW_URL}}` - Link naar preview
- `{{IMPROVEMENT_POINTS}}` - Specifieke verbeterpunten
- `{{UNIQUE_SELLING_POINT}}` - USP van bedrijf

**Tips:**
- Personaliseer altijd
- Wees specifiek over wat er mis is met huidige site
- Show don't tell - preview is je sterkste wapen
- Geen druk, blijf vriendelijk
- Timing: di-do, 10:00-15:00
- Max 1 follow-up per maand

## 📦 Voorbeeld Frontpages

In `/examples/` vind je drie volledig uitgewerkte voorbeelden:

### 1. Vakgarage Blokhuis
**Type:** Autobedrijf
**Stijl:** Donkerblauw/Oranje, stoer en betrouwbaar
**Features:**
- 65+ jaar ervaring highlight
- BOVAG/RDW certificering
- Diensten: verkoop, onderhoud, APK, schade, e-bikes
- Automotive color scheme

### 2. Restaurant De Mandemaaker
**Type:** Restaurant
**Stijl:** Donkergroen/Goud, warm en elegant
**Features:**
- Michelin/Gault Millau erkenning
- Haven locatie highlight
- Verse vis & zeevruchten focus
- Restaurant color scheme

### 3. Rijschool Vermeer
**Type:** Rijschool
**Stijl:** Fris groen/Wit, jong en dynamisch
**Features:**
- 45 jaar ervaring
- Meerdere rijbewijs types
- Code 95 nascholing
- Education color scheme

**Genereren:**
```bash
cd examples
python generate-examples.py
```

## 🚀 Workflow

### Stap 1: Prospect Vinden
Zoek bedrijven in Bunschoten-Spakenburg met verouderde websites:
- Google: "bedrijf Bunschoten-Spakenburg"
- Lokale bedrijvengidsen
- Fysiek rondrijden en notities maken

### Stap 2: Website Scannen
```bash
python prospect-scanner.py www.bedrijf.nl --save
```

### Stap 3: Preview Genereren
```bash
python generate-frontpage.py bedrijf_nl.json preview.html
```

### Stap 4: Preview Uploaden
Upload naar GitHub Pages of andere hosting:
```bash
# Voorbeeld met GitHub Pages
cp preview.html ~/thebusinessbooster.nl/previews/bedrijf.html
cd ~/thebusinessbooster.nl
git add previews/bedrijf.html
git commit -m "Add preview for Bedrijf"
git push
```

### Stap 5: Outreach Email Versturen
1. Open `outreach-template.txt`
2. Vul variabelen in:
   - `{{BUSINESS_NAME}}` → Bedrijf Naam
   - `{{CONTACT_NAME}}` → Jan Jansen
   - `{{PREVIEW_URL}}` → https://thebusinessbooster.nl/previews/bedrijf.html
   - `{{IMPROVEMENT_POINTS}}` → Specifieke problemen
3. Verstuur via je email client

**Voorbeeld:**
```
Onderwerp: Moderne website voor Vakgarage Blokhuis - Gratis design preview

Beste [Naam],

Mijn naam is Jarno en ik help lokale bedrijven in Bunschoten-Spakenburg 
met professionele, moderne websites.

Ik bezocht onlangs vakgarageblokhuis.nl en zie dat jullie een prachtige 
zaak hebben met meer dan 65 jaar ervaring. Echter, de huidige website 
doet uw bedrijf niet volledig recht.

Om te laten zien wat mogelijk is, heb ik een preview gemaakt:
👉 https://thebusinessbooster.nl/previews/vakgarageblokhuis.html

€150 per maand - all-in (design, hosting, onderhoud)

Interesse in een vrijblijvend gesprek?

Groet,
Jarno | The Business Booster
```

### Stap 6: Follow-up
- Week 1: Verstuur initiële email
- Week 2: Follow-up als geen reactie
- Week 4: Laatste follow-up
- Daarna: Markeer als "niet geïnteresseerd"

### Stap 7: Contract
Bij interesse:
1. Open `contract.html` in browser
2. Print naar PDF
3. Vul gegevens opdrachtgever in
4. Verstuur voor handtekening (digitaal of fysiek)
5. Na ondertekening: Start met website bouw

## 💡 Pro Tips

### Design Kwaliteit Verbeteren
- **Kleuren:** Gebruik kleurenschema passend bij branche
- **Typografie:** Inter voor body, Playfair Display voor headers
- **Afbeeldingen:** Gebruik Unsplash voor professionele stock foto's
- **Animaties:** Subtiel, niet overdreven
- **Whitespace:** Genoeg ruimte, niet te vol

### Email Response Rate Verhogen
- **Subject line:** Beknopt en specifiek
- **Personalisatie:** Noem iets unieks over hun bedrijf
- **Bewijs:** Link naar preview (show don't tell)
- **Timing:** Stuur di-do tussen 10:00-15:00
- **Follow-up:** Max 2x, dan stoppen

### Conversie Verhogen
- **Portfolio:** Toon meerdere voorbeelden
- **Testimonials:** Vraag tevreden klanten om reviews
- **Garantie:** Bied "30 dagen niet goed, geld terug"
- **Spoed:** "Beperkt aantal plaatsen per maand"
- **Lokaal:** Benadruk lokale focus en persoonlijk contact

## 🔧 Technische Details

### Dependencies
```bash
pip install requests beautifulsoup4
```

### Hosting Opties
- **GitHub Pages** (gratis, eenvoudig)
- **Netlify** (gratis, betere features)
- **Vercel** (gratis, zeer snel)

### Custom Domain Setup
1. Koop domein (bijv. thebusinessbooster.nl)
2. Configureer DNS naar hosting
3. Upload website files
4. Wacht op propagatie (24u)

### Email Setup
- Gebruik professioneel email: info@thebusinessbooster.nl
- Gmail/Outlook OK voor starten
- Later: TransactionalEmail service (SendGrid, etc.)

## 📊 Tracking & Analytics

### Belangrijke Metrics
- **Prospects gescand:** Hoeveel bedrijven bekeken?
- **Previews gemaakt:** Hoeveel designs aangemaakt?
- **Emails verstuurd:** Hoeveel outreach?
- **Response rate:** % dat reageert
- **Conversie rate:** % dat tekent
- **MRR:** Monthly Recurring Revenue

### Spreadsheet Template
```
| Bedrijf | URL | Email verstuurd | Reactie | Status | Waarde |
|---------|-----|-----------------|---------|--------|--------|
| Vakgarage Blokhuis | vakgarageblokhuis.nl | 2024-02-16 | Ja | Getekend | €150/mnd |
```

## 🎨 Aanpassingen

### Template Aanpassen
Edit `template.html`:
- **Kleuren:** Wijzig CSS variabelen (`:root`)
- **Fonts:** Verander Google Fonts imports
- **Secties:** Voeg toe/verwijder HTML blokken
- **Animaties:** Pas CSS transitions aan

### Generator Uitbreiden
Edit `generate-frontpage.py`:
- **Nieuwe business types:** Voeg kleurschema toe
- **Extra services:** Breid service lijst uit
- **Custom logic:** Voeg bedrijfsspecifieke regels toe

### Scanner Verbeteren
Edit `prospect-scanner.py`:
- **Betere extractie:** Verbeter regex patterns
- **Meer data:** Voeg extra velden toe
- **AI scoring:** Gebruik AI voor betere design score

## 🚨 Veelvoorkomende Problemen

### "Module not found"
```bash
pip install requests beautifulsoup4
```

### "Permission denied"
```bash
chmod +x prospect-scanner.py
chmod +x generate-frontpage.py
```

### Email komt in spam
- Gebruik professioneel email domein
- Vermijd spam trigger words
- Niet teveel emails tegelijk
- Warm up email account (start klein)

### Preview laadt niet
- Check of HTML bestand geldig is
- Controleer of hosting actief is
- Test in verschillende browsers

## 📈 Groeiplan

### Maand 1-3: Launch (0-5 klanten)
- Perfectioneer systeem
- Maak 10+ previews
- Stuur 50+ outreach emails
- Target: 3-5 klanten (€450-750/mnd)

### Maand 4-6: Scale (5-15 klanten)
- Automatiseer meer
- Bouw portfolio uit
- Testimonials verzamelen
- Target: 10-15 klanten (€1.500-2.250/mnd)

### Maand 7-12: Optimize (15-30 klanten)
- Hire VA voor outreach
- Premium tier (€250/mnd)
- Referral programma
- Target: 20-30 klanten (€3.000-4.500/mnd)

### Jaar 2: Enterprise (30-50 klanten)
- White label voor andere regio's
- Additional services (SEO, ads)
- Agency model
- Target: 40-50 klanten (€6.000-7.500/mnd)

## 📝 Checklist

- [ ] Install dependencies (`pip install requests beautifulsoup4`)
- [ ] Test prospect scanner op eigen website
- [ ] Generate drie voorbeeld frontpages
- [ ] Upload voorbeelden naar GitHub Pages
- [ ] Setup professionele email (info@thebusinessbooster.nl)
- [ ] Maak lijst van 20 prospects in Bunschoten-Spakenburg
- [ ] Scan eerste 5 prospects
- [ ] Genereer 5 previews
- [ ] Verstuur eerste 5 outreach emails
- [ ] Setup tracking spreadsheet
- [ ] Test contract template
- [ ] Maak LinkedIn/social aanwezigheid

## 🔗 Links

- Website: thebusinessbooster.nl
- Email: info@thebusinessbooster.nl
- GitHub: github.com/jarnodevries-byte/thebusinessbooster

## 📄 Licentie

Proprietary - The Business Booster © 2024

---

**Veel succes met je acquisitie! 🚀**

*Questions? Contact: info@thebusinessbooster.nl*
