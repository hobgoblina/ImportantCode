BEGIN
IF (y = 2) THEN
  BEGIN
    LET z := $36 + $48 * ($((x < '0') ? 1 : 9));
    x := $z % 10;
    WHILE ((x >= 'a' AND x <= 'f')) DO { y := y - 1 };
  END;

END.
