[start]
Neben dem Bett steht eine alte Holzkiste. Sie ist verschlossen, aber nur mit einem eher einfachen Schloß versehen.

Was willst du tun?

? (str > 5) Die Kiste auf brechen.
  Du hackst das Holz in Stücke! Zwischen den Splittern findest du etwas...
  <loot> Ui, fein. 

? (dex > 5) Das Schloß knacken.
  Mit geschickten Handgriffen öffnest du das Schloß. Glitzert da nicht etwas?
  <loot>

? Der Inhalt geht mich nichts an.
  Da wird wohl eh nichts wertvolles drin sein. Wobei... was soll das Schloß, wenn es nichts wertvolles beschützt?

  ? Ich bin kein Dieb!
    OK ok, war ja nur ein Gedanke
    <no_loot>

  ? Nagut, ich überleg es mir das nochmal.
    <start>

[loot] Zwei Silbermünzen wandern in deine Tasche.
! add money 20

[no_loot] Du verlässt das Zimmer ohne Beute.
