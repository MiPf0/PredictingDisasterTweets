# Einfluss von Ereignisarten auf die Genauigkeit der Textklassifizierung humanitärer Kategorien von Twitter-Katastrophenmeldungen: Ein Ensemble-Lernansatz
Dieses Projekt ist der Fokus meiner BSc-Arbeit an der FH Burgenland für den Studiengang "Software Engineering und vernetzte Systeme".  
Die Daten stammen aus folgender Quelle:  
Firoj Alam, Umair Qazi, Muhammad Imran and Ferda Ofli, HumAID: Human-Annotated Disaster Incidents Data from Twitter, In ICWSM, 2021.
Der Datensatz ist unter https://crisisnlp.qcri.org/humaid_dataset herunterzuladen.  
  
  
Bisherige Ergebnisse  
  
Strategie 01:  
* Trainings-Datensätze mit Oversampler und Undersampler anpassen, um jede Kategorie gleichgewichtet zu haben.  
* Training aller Modelle mit BERT-Algorithmus.  
* Ergebnis: Generelles Humanitäre-Kategorie-Modell performt besser als die Kombination aus Ereignisart-Modell und dem jeweiligen spezialisierten Ereignisart-Humanitäre-Kategorie-Modell.
