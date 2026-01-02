# Subnetting - Praktisk Övningsguide

## Lär dig beräkna subnet för hand

---

## 📋 Innehållsförteckning

1. [Vad är Subnetting?](#vad-är-subnetting)
2. [Grundläggande Koncept](#grundläggande-koncept)
3. [Steg-för-Steg Metod](#steg-för-steg-metod)
4. [Exempel från Föreläsningen](#exempel-från-föreläsningen)
5. [Snabbregler & Tips](#snabbregler--tips)
6. [Övning](#övning)
7. [Cheat Sheet](#cheat-sheet)

---

## 🎯 Vad är Subnetting?

**Subnetting** = Dela upp ett IP-nätverk i mindre subnät

**Vad vi ska kunna beräkna:**

- **Network Address** - Första adressen i subnätet
- **Broadcast Address** - Sista adressen i subnätet
- **First Host** - Första användbara IP-adressen
- **Last Host** - Sista användbara IP-adressen
- **Next Subnet** - Första adressen i nästa subnät

**Verktyg för övning:**

- 🌐 [subnet-ipv4.com](http://subnet-ipv4.com) - Genererar övningar
- ✋ **Papper och penna** - Lös för hand!

⚠️ **VIKTIGT**: Använd INTE subnet-kalkylatorer! Målet är att förstå logiken.

---

## 📚 Grundläggande Koncept

### IP-adress med CIDR-notation

**Format:** `IP-adress/prefix`

**Exempel:** `192.168.1.0/24`

- IP-adress: `192.168.1.0`
- Prefix: `/24` (subnet mask)

### Prefix och Subnet Mask

| CIDR | Subnet Mask | Antal nätverk | Antal hosts |
|------|-------------|---------------|-------------|
| /8 | 255.0.0.0 | 1 byte | 16,777,214 |
| /16 | 255.255.0.0 | 2 bytes | 65,534 |
| /24 | 255.255.255.0 | 3 bytes | 254 |
| /25 | 255.255.255.128 | 3.5 bytes | 126 |
| /26 | 255.255.255.192 | 3.75 bytes | 62 |
| /27 | 255.255.255.224 | ~3.875 bytes | 30 |
| /28 | 255.255.255.240 | ~3.9375 bytes | 14 |
| /29 | 255.255.255.248 | ~3.96875 bytes | 6 |
| /30 | 255.255.255.252 | ~3.984375 bytes | 2 |

### Network vs Host-delen

En IP-adress består av två delar:

- **Network-delen** - Identifierar nätverket
- **Host-delen** - Identifierar enheten i nätverket

**Prefix anger var gränsen går:**

```
192.168.1.100/24
└─ Network ─┘└ Host ┘
   (24 bits)  (8 bits)
```

### Binära Positioner

**Varje byte har 8 bitar:**

```
Position:  1    2    4    8    16   32   64   128
Binär:    [0/1][0/1][0/1][0/1][0/1][0/1][0/1][0/1]
```

**Exempel: 192 i binärt**

```
128 + 64 = 192
[1] [1] [0] [0] [0] [0] [0] [0]
```

---

## 🔢 Steg-för-Steg Metod

### Steg 1: Hitta Gränsen

**Given:** IP-adress/prefix (ex: `192.168.1.100/26`)

**Beräkna var network-delen slutar:**

- Totalt: 32 bitar (4 bytes × 8 bits)
- Prefix: `/26` betyder 26 bitar för network

**Räkna:**

- Byte 1: Bit 1-8 (8 bitar)
- Byte 2: Bit 9-16 (16 bitar totalt)
- Byte 3: Bit 17-24 (24 bitar totalt)
- Byte 4: Bit 25-32

**Gränsen vid /26:**

- 24 bitar täcker 3 hela bytes
- 26 - 24 = 2 bitar in i byte 4
- Gränsen går efter bit 26

```
Byte 1    Byte 2    Byte 3    Byte 4
[8 bits]  [8 bits]  [8 bits]  [8 bits]
[─────────────────26 bits────────]│[6 bits]
        Network-delen            │ Host-delen
```

### Steg 2: Konvertera till Binärt

**Metod: Subtrahera från vänster till höger**

**För varje byte:**

1. Jämför med 128 - Större eller lika? → 1, annars → 0
2. Om ja: subtrahera 128
3. Jämför resten med 64
4. Om ja: subtrahera 64
5. Fortsätt: 32, 16, 8, 4, 2, 1

**Exempel: Konvertera 192**

```
Är 192 ≥ 128? Ja → 1, resten: 192-128=64
Är 64 ≥ 64?   Ja → 1, resten: 64-64=0
Är 0 ≥ 32?    Nej → 0
Är 0 ≥ 16?    Nej → 0
Är 0 ≥ 8?     Nej → 0
Är 0 ≥ 4?     Nej → 0
Är 0 ≥ 2?     Nej → 0
Är 0 ≥ 1?     Nej → 0

Resultat: 11000000 = 192
```

### Steg 3: Fyll i Network-delen

**Konvertera alla bytes fram till gränsen:**

För `/26`:

- Byte 1, 2, 3: Konvertera helt
- Byte 4: Konvertera bara första 2 bitar

### Steg 4: Beräkna Adresser

**Network Address:**

- Network-delen (som den är)
- Host-delen: **Alla nollor**

**Broadcast Address:**

- Network-delen (som den är)
- Host-delen: **Alla ettor**

**First Host:**

- Network Address + 1
- Eller: Network-delen + `00000001`

**Last Host:**

- Broadcast Address - 1
- Eller: Network-delen + `11111110`

**Next Subnet:**

- Addera 1 på sista biten i network-delen
- Host-delen: alla nollor

### Steg 5: Konvertera Tillbaka till Decimal

**Metod: Addera alla positioner med 1**

**Exempel:**

```
Binärt:    1 1 0 0 0 0 0 0
Position: 128 64 32 16 8 4 2 1
Värde:    128+64 = 192
```

---

## 📖 Exempel från Föreläsningen

### Exempel 1: 137.92.49.86/17

**Steg 1: Hitta gränsen**

```
/17 = 8 + 8 + 1
Gränsen går efter bit 17 (i byte 3)
```

**Steg 2: Konvertera till binärt**

**Byte 1: 137**

```
137 ≥ 128? Ja → 1, rest: 9
9 ≥ 64?    Nej → 0
9 ≥ 32?    Nej → 0
9 ≥ 16?    Nej → 0
9 ≥ 8?     Ja → 1, rest: 1
1 ≥ 4?     Nej → 0
1 ≥ 2?     Nej → 0
1 ≥ 1?     Ja → 1, rest: 0

137 = 10001001
```

**Byte 2: 92**

```
92 ≥ 128?  Nej → 0
92 ≥ 64?   Ja → 1, rest: 28
28 ≥ 32?   Nej → 0
28 ≥ 16?   Ja → 1, rest: 12
12 ≥ 8?    Ja → 1, rest: 4
4 ≥ 4?     Ja → 1, rest: 0
0 ≥ 2?     Nej → 0
0 ≥ 1?     Nej → 0

92 = 01011100
```

**Byte 3: 49 (endast första biten behövs för /17)**

```
49 ≥ 128?  Nej → 0
49 ≥ 64?   Nej → 0
49 ≥ 32?   Ja → 1, rest: 17
...fortsätt om nödvändigt

49 = 00110001 (men vi bryr oss bara om första biten: 0)
```

**Byte 4: 86** (host-delen, ignorera för network)

**Steg 3: Binär representation**

```
Byte 1      Byte 2      Byte 3    Byte 4
10001001 . 01011100 . 0│??????? . ????????
         Network (17)  │    Host (15)
```

**Steg 4: Beräkna adresser**

**Network Address:**

```
10001001 . 01011100 . 00000000 . 00000000
= 137.92.0.0/17
```

**Broadcast Address:**

```
10001001 . 01011100 . 01111111 . 11111111
= 137.92.127.255/17

Byte 3: 01111111 = 64+32+16+8+4+2+1 = 127
Byte 4: 11111111 = 128+64+32+16+8+4+2+1 = 255
```

**First Host:**

```
Network + 1 = 137.92.0.1/17
```

**Last Host:**

```
Broadcast - 1 = 137.92.127.254/17
```

**Next Subnet:**

```
Network-delen + 1 (på bit 17):
10001001 . 01011100 . 1│0000000 . 00000000
= 137.92.128.0/17
```

---

### Exempel 2: 200.0.250.59/27

**Steg 1: Hitta gränsen**

```
/27 = 8 + 8 + 8 + 3
Gränsen går efter bit 27 (3 bitar in i byte 4)
```

**Steg 2-3: Konvertera och identifiera**

**Bytes 1-3:** Helt i network (konvertera alla)

```
200 = 11001000
0   = 00000000
250 = 11111010
```

**Byte 4: 59** (först 3 bitar för network)

```
59 ≥ 128?  Nej → 0
59 ≥ 64?   Nej → 0
59 ≥ 32?   Ja → 1, rest: 27

Första 3 bitar: 001
```

**Binär representation:**

```
11001000 . 00000000 . 11111010 . 001│?????
              Network (27)           │ Host (5)
```

**Steg 4: Beräkna adresser**

**Network Address:**

```
11001000 . 00000000 . 11111010 . 00100000
Byte 4: 00100000 = 32
= 200.0.250.32/27
```

**Broadcast Address:**

```
11001000 . 00000000 . 11111010 . 00111111
Byte 4: 00111111 = 32+16+8+4+2+1 = 63
= 200.0.250.63/27
```

**First Host:**

```
= 200.0.250.33/27
```

**Last Host:**

```
= 200.0.250.62/27
```

**Next Subnet:**

```
Network-delen + 1:
11001000 . 00000000 . 11111010 . 01000000
Byte 4: 01000000 = 64
= 200.0.250.64/27
```

---

### Exempel 3: 194.184.226.53/29

**Steg 1: Hitta gränsen**

```
/29 = 32 - 29 = 3 bitar för host
Gränsen går efter bit 29 (5 bitar in i byte 4)
```

**Steg 2-3: Konvertera**

**Bytes 1-3:** (Helt i network)

```
194 = 11000010
184 = 10111000
226 = 11100010
```

**Byte 4: 53** (första 5 bitar för network)

```
53 = 00110101
Network: 00110│
Host:         │101
```

**Steg 4: Beräkna adresser**

**Network Address:**

```
194.184.226 . 00110000
Byte 4: 00110000 = 32+16 = 48
= 194.184.226.48/29
```

**Broadcast Address:**

```
194.184.226 . 00110111
Byte 4: 00110111 = 32+16+4+2+1 = 55
= 194.184.226.55/29
```

**First Host:**

```
= 194.184.226.49/29
```

**Last Host:**

```
= 194.184.226.54/29
```

**Next Subnet:**

```
194.184.226 . 00111000
Byte 4: 00111000 = 32+16+8 = 56
= 194.184.226.56/29
```

---

## 💡 Snabbregler & Tips

### Snabbmetod för Binär Konvertering

**Kom ihåg positionerna:**

```
128  64  32  16  8  4  2  1
```

**För varje position från vänster till höger:**

1. Kan jag dra av detta värde?
2. Om JA → sätt 1, dra av värdet
3. Om NEJ → sätt 0, gå vidare

### Läsning av Binärt till Decimal

**Addera bara positioner med 1:**

```
Binärt:    1  0  1  1  0  1  0  1
Position: 128 64 32 16  8  4  2  1
Summera:  128+0+32+16+0+4+0+1 = 181
```

### Genvägar

**Network Address:**

- Bytes före gränsen: Ändras inte
- Byte vid gränsen: Behåll network-bitar, nollställ host-bitar
- Bytes efter gränsen: Alla nollor

**Broadcast Address:**

- Bytes före gränsen: Ändras inte
- Byte vid gränsen: Behåll network-bitar, ettor i host-bitar
- Bytes efter gränsen: Alla ettor (255)

**First Host:**

- Network Address + 1 (alltid)

**Last Host:**

- Broadcast Address - 1 (alltid)

**Next Subnet:**

- Addera 1 på sista network-biten
- Kan påverka föregående bytes om det blir "overflow"

### Minnesregler

**Alla nollor i host → Network**
**Alla ettor i host → Broadcast**
**Network + 1 → First Host**
**Broadcast - 1 → Last Host**
**Network + subnet size → Next Subnet**

### Vanliga CIDR-värden

| CIDR | Sista Byte Range | Subnet Size | Hosts |
|------|------------------|-------------|-------|
| /24 | 0-255 | 256 | 254 |
| /25 | 0-127, 128-255 | 128 | 126 |
| /26 | 0-63, 64-127, ... | 64 | 62 |
| /27 | 0-31, 32-63, ... | 32 | 30 |
| /28 | 0-15, 16-31, ... | 16 | 14 |
| /29 | 0-7, 8-15, ... | 8 | 6 |
| /30 | 0-3, 4-7, ... | 4 | 2 |

---

## 🎓 Övning

### Övningsverktyg

**Rekommenderat:** [subnet-ipv4.com](http://subnet-ipv4.com)

**Inställningar:**

- Genererar slumpmässiga IP/CIDR
- Visa/dölj lösning
- Olika svårighetsgrader

### Övningsprocess

1. **Få en övningsuppgift** från subnet-ipv4.com
2. **Lös för hand** på papper
3. **Kontrollera svaret** på webbplatsen
4. **Repetera** tills du känner dig säker

### Vad att Öva På

**Steg 1: Grundläggande (/24, /16, /8)**

- Gränsen går mellan bytes
- Enklare att visualisera

**Steg 2: Medel (/25, /26, /27)**

- Gränsen går inom sista byten
- Vanligaste i praktiken

**Steg 3: Avancerat (/28, /29, /30)**

- Mycket små subnät
- Precision krävs

**Steg 4: Udda Gränser (/17, /23, /19)**

- Gränsen inte vid "runda" värden
- Testa din förståelse

### Målet

**Kunna lösa utan:**

- ❌ Kalkylator för binär konvertering
- ❌ Subnet-kalkylator
- ❌ Googling

**Med endast:**

- ✅ Papper
- ✅ Penna
- ✅ Din hjärna

### När Är Du Klar?

**Du är redo när du kan:**

1. Snabbt identifiera var gränsen går
2. Konvertera decimal ↔ binär utan att tänka
3. Beräkna alla 5 värden konsekvent rätt
4. Förklara varför varje steg fungerar

---

## 📋 Cheat Sheet

### Process - Kort Sammanfattning

```
1. Hitta gränsen
   /prefix → Räkna bits → Markera var network slutar

2. Konvertera till binärt
   Decimal → Binär (subtraktionsmetoden)

3. Fyll i network-delen
   Konvertera bytes fram till gränsen

4. Beräkna adresser:
   Network   = Network-delen + 00000...
   Broadcast = Network-delen + 11111...
   First     = Network + 1
   Last      = Broadcast - 1
   Next      = Network-delen + 1 (på network-position)

5. Konvertera tillbaka
   Binär → Decimal (additionsmetoden)
```

### Binär Konvertering - Snabbguide

**Decimal → Binär:**

```
For varje position (128, 64, 32, 16, 8, 4, 2, 1):
  Om (värde ≥ position):
    Sätt 1
    värde = värde - position
  Annars:
    Sätt 0
```

**Binär → Decimal:**

```
For varje position med 1:
  Addera positionens värde
Summan = decimal värde
```

### CIDR Snabbreferens

| CIDR | Network Bits | Host Bits | Subnet Size |
|------|--------------|-----------|-------------|
| /8 | 8 | 24 | 16,777,216 |
| /16 | 16 | 16 | 65,536 |
| /24 | 24 | 8 | 256 |
| /25 | 25 | 7 | 128 |
| /26 | 26 | 6 | 64 |
| /27 | 27 | 5 | 32 |
| /28 | 28 | 4 | 16 |
| /29 | 29 | 3 | 8 |
| /30 | 30 | 2 | 4 |

### Minneslappar

**Beräkna host-bits:**

```
Host bits = 32 - CIDR
Exempel: /27 → 32-27 = 5 host bits
```

**Beräkna subnet size:**

```
Subnet size = 2^(host bits)
Exempel: 5 host bits → 2^5 = 32
```

**Beräkna användbara hosts:**

```
Användbara = Subnet size - 2
(minus network och broadcast)
Exempel: 32 - 2 = 30 hosts
```

---

## 🎯 Vanliga Misstag

### Misstag 1: Fel Gräns

❌ **Fel:**

```
/25 → Gränsen i byte 3
```

✅ **Rätt:**

```
/25 → 24 bits i första 3 bytes + 1 bit i byte 4
Gränsen går i byte 4
```

### Misstag 2: Glömmer Binär Konvertering

❌ **Fel:**

```
Network för 192.168.1.100/26
= 192.168.1.0 (gissar)
```

✅ **Rätt:**

```
Konvertera 100 till binärt: 01100100
26 bits = 24 + 2
Network: 192.168.1.01000000 = 192.168.1.64
```

### Misstag 3: Broadcast är Inte Alltid .255

❌ **Fel:**

```
Broadcast för något/26 = x.x.x.255
```

✅ **Rätt:**

```
/26 → 6 host bits
Broadcast beror på var subnet börjar
Kan vara .63, .127, .191, eller .255
```

### Misstag 4: Next Subnet

❌ **Fel:**

```
Next subnet = Network + 1
```

✅ **Rätt:**

```
Next subnet = Network + subnet size
Eller: Broadcast + 1
```

---

## 📚 Sammanfattning

### Vad Vi Lärde Oss

1. ✅ Konvertera decimal ↔ binär
2. ✅ Identifiera network/host-gränsen
3. ✅ Beräkna network address
4. ✅ Beräkna broadcast address
5. ✅ Beräkna first/last host
6. ✅ Beräkna next subnet

### Nyckelpunkter

**Subnetting är:**

- Logiskt, inte svårt
- Baserat på binär aritmetik
- Följer fasta regler
- Övar gör mästare

**Reglerna:**

1. Gränsen bestäms av CIDR (/prefix)
2. Network = network-delen + nollor
3. Broadcast = network-delen + ettor
4. First = Network + 1
5. Last = Broadcast - 1
6. Next = Network + subnet size

### Nästa Steg

1. 📝 Öva på [subnet-ipv4.com](http://subnet-ipv4.com)
2. 🎯 Börja med enkla (/24, /16)
3. 📈 Arbeta upp till svårare (/27, /29, /17)
4. 🔁 Repetera tills det sitter
5. ⏱️ Öka hastighet med övning

### Tips för Framgång

- **Öva varje dag** - Även 10 minuter hjälper
- **Använd papper** - Ingen shortcuts
- **Förstå varför** - Inte bara hur
- **Gör misstag** - Lär från dem
- **Testa dig själv** - Utan lösning först

---

**Lycka till med subnetträningen! 🚀**

*Matematik är bara ett verktyg - logik är din superkraft!*
