#import lostrommel
#import vergleicher
#import tippschein
import eingabe
import ausgabe
import spiel

spiel.Ausspielung(eingabe.Tastatur(), ausgabe.Html()).ausfuehrung()
spiel.Ausspielung(eingabe.Datei("Tippschein.json"), ausgabe.Html()).ausfuehung()

spiel.Ausspielung(eingabe.DjangoReader(), ausgabe.DjangoWriter()).ausfuehrung()
