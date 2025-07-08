# FS Kripto Taramasi

Bu depo, kripto para piyasalarini erken tespit icin kullanilabilecek
cok katmanli bir izleme sisteminin sade bir ornegini icerir. Kodlar
sadece konsepti gosterir; gercek zamanli veri baglantilari ve ag
entegrasyonlari yer almamaktadir.

## Bilesenler

1. **Market Screener** (`market_screener.py`)
   - Hacim artisina, RSI sapmasina ve ani fiyat degisimlerine bakarak
     coin'leri tarar.
2. **Pattern Deviation AI** (`pattern_deviation.py`)
   - Bir coinin bugunku hareketleriyle gecmis verilerini karsilastirip
     pump/dump risk puani cikarir.
3. **On-Chain Radar** (`onchain_radar.py`)
   - Whale transferleri ve diger zincir ustu hareketleri izler.
4. **Sentiment Sniper** (`sentiment_sniper.py`)
   - Sosyal medya platformlarinda ani konusulma artislarini arar.

Her modul icerisinde gercek ag baglantilari yerine sahte veriler
kullanilmistir. Islemleri `main.py` dosyasi uzerinden komut satirindan
calistirabilirsiniz:

```bash
python -m fs_sistem.main screener
python -m fs_sistem.main deviation BTCUSDT
python -m fs_sistem.main onchain
python -m fs_sistem.main sentiment listing burn
```

