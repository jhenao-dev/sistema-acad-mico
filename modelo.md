estudiante
──────────
id
nombre
apellido
documento
fecha_nacimiento
estrato

profesor
────────
id
nombre
apellido
documento
especialidad

materia
───────
id
nombre
descripcion
profesor_id

periodo
───────
id
nombre (ej: "2026-1")
fecha_inicio
fecha_fin

matricula
─────────
id
estudiante_id
materia_id
periodo_id
nota
fecha_matricula

asistencia
──────────
id
estudiante_id
materia_id
fecha
asistio
justificada