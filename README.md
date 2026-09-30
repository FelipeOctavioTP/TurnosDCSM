# Panel de Turnos DCSM

Calendario de turnos (Energía, Climatización, BMS) en un solo `index.html`, con datos en Supabase.
Modo **Lectura** para todos y modo **Administrador** (PIN) para editar turnos, comentarios, colores y cerrar alertas.

## Puesta en marcha

1. **Base de datos.** En Supabase (proyecto `xnlqyxxyryqyziksmajn`) > SQL Editor:
   1. Abre `supabase/schema.sql`, cambia `TU_PIN_AQUI` por tu clave y ejecútalo completo.
   2. Ejecuta `supabase/seed_turnos_2026.sql` (historial abr–dic 2026).
   3. Ejecuta `supabase/seed_turnos_2027.sql` (propuesta 2027: continúa el ciclo de 15 días de cada técnico).
2. **Conexión.** `index.html` ya trae la URL y la clave *anon public* del proyecto. Nunca pongas la `service_role` ni una `sb_secret_` en este archivo.
3. **Publicar.**
   ```bash
   git init
   git add .
   git commit -m "Panel de turnos DCSM 2027"
   git branch -M main
   git remote add origin https://github.com/TU_USUARIO/turnos-dcsm.git
   git push -u origin main
   ```
   Luego en GitHub: Settings > Pages > Deploy from a branch > `main` / `(root)`.

## Mantenimiento

- **Personal:** se edita en `GROUPS` (arriba en el `<script>` de `index.html`). Si alguien sale o entra, cámbialo ahí.
- **Feriados:** constante `HOLIDAYS`. Agrega los del año siguiente cada diciembre.
- **Supervisores:** rotan cada semana (`SUP_ROTATION`, ancla `2026-04-06`).
- **Año nuevo:** `python3 tools/generar_ciclo.py 2028 > supabase/seed_turnos_2028.sql` y ejecútalo en Supabase.
- **Cambio de PIN:** vuelve a ejecutar la última sentencia de `schema.sql` con el PIN nuevo.

## Seguridad

- Cualquiera con el enlace puede **ver** los turnos. Solo quien tenga el PIN puede **escribir**
  (las tablas no aceptan escritura directa; todo pasa por funciones que validan el PIN, con límite de 10 intentos fallidos cada 10 minutos).
- Las semillas `.sql` traen nombres y turnos: por eso están en `.gitignore`. Si el repo es público, no las subas.
