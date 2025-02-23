
PHREEQC_INPUT_TEMPLATES = {
    "Blank": "",
    "Seawater": """TITLE Seawater
SOLUTION 1  IAPSO Standard Seawater at 35 Salinity
        units   ppm
        pH      8.22
        pe      8.451
        density 1.025
        temp    25.0
        Ca              412
        Mg              1290
        Na              10770
        K               399
        Fe              0.055e-3
        Mn              0.014e-3
        Si              2.8
        Cl              19354
        C(4)            26.6
        S(6)            904
        N(5)            0.42
        N(-3)           0.03    as    NH4
END
""",
}