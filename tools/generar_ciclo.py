#!/usr/bin/env python3
"""Genera el SQL de turnos para un año continuando el ciclo de 15 días de cada técnico.

Uso:  python3 tools/generar_ciclo.py 2028 > supabase/seed_turnos_2028.sql

CICLO: 3 días (D), 2 libres, 3 noches (N), 2 libres, 3 tardes (T), 2 libres.
FASE:  posición de cada técnico dentro del ciclo el 2027-01-01 (0 = primer día D).
Si alguien cambia de grupo de turno, ajusta su fase aquí o edita el panel directamente.
"""
import sys, datetime as dt

CICLO = "DDDLLNNNLLTTTLL"
REF = dt.date(2027, 1, 1)
FASES = {
    "Lucas Morales": 2,
    "Damián Aguilar": 11,
    "Jeremías Gómez": 14,
    "Javiera Muñoz": 5,
    "Raúl Santander": 8,
    "Ciomara Sepúlveda": 2,
    "Franco Tamburini": 11,
    "Luis Valenzuela": 14,
    "Francisca Albarrán": 5,
    "Caroline Aróstica": 8,
    "Billy Ritz": 8,
    "Ricardo Alvarado": 5,
    "Matías Carrasco": 2,
    "José Gamboa": 11,
    "Gonzalo Parra": 14
}

def main(year):
    rows = []
    d = dt.date(year, 1, 1)
    while d.year == year:
        for nombre, fase in FASES.items():
            c = CICLO[(fase + (d - REF).days) % len(CICLO)]
            rows.append("('%s','%s','%s')" % (nombre, d.isoformat(), c))
        d += dt.timedelta(days=1)
    for i in range(0, len(rows), 1000):
        print("insert into public.turnos_dcsm (tecnico, fecha, codigo) values")
        print(",\n".join(rows[i:i + 1000]))
        print("on conflict (tecnico, fecha) do nothing;\n")

if __name__ == "__main__":
    main(int(sys.argv[1]))
