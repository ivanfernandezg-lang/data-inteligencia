#!/usr/bin/env python3
"""
Script de Gestión de Tareas — 

Propósito: Ayudar a crear, organizar y validar tareas de optimización.

Uso:
    python task_manager.py --help
    python task_manager.py create --type problema-cotidiano --id T-001 --name "Ruta de entrega"
    python task_manager.py list
    python task_manager.py validate tarea-T-001-ruta-entrega.md
"""

import argparse
import os
import sys
from datetime import datetime
from pathlib import Path
import json


class TaskManager:
    """Gestor de tareas de optimización."""
    
    TASK_TYPES = {
        'problema-cotidiano': 'tarea-problema-cotidiano.md',
        'especializacion': 'tarea-especializacion.md',
        'investigacion': 'tarea-investigacion.md',
        'proyecto': 'tarea-proyecto.md',
    }
    
    def __init__(self):
        """Inicializar gestor."""
        self.root = Path(__file__).parent.parent
        self.tareas_dir = self.root / 'tareas'
        self.plantillas_dir = self.tareas_dir / 'plantillas'
        self.resueltas_dir = self.tareas_dir / 'resueltas'
        self.progreso_dir = self.tareas_dir / 'en-progreso'
        
    def create_task(self, task_type: str, task_id: str, name: str) -> None:
        """Crear nueva tarea desde plantilla."""
        if task_type not in self.TASK_TYPES:
            print(f"❌ Tipo inválido. Opciones: {list(self.TASK_TYPES.keys())}")
            return
        
        template_name = self.TASK_TYPES[task_type]
        template_path = self.plantillas_dir / template_name
        
        if not template_path.exists():
            print(f"❌ Plantilla no encontrada: {template_path}")
            return
        
        # Leer plantilla
        with open(template_path, 'r') as f:
            content = f.read()
        
        # Personalizar
        # (En versión futura, reemplazar [placeholders])
        
        # Crear archivo
        filename = f"{task_id}-{name.lower().replace(' ', '-')}.md"
        output_path = self.progreso_dir / filename
        
        if output_path.exists():
            response = input(f"⚠️  Archivo existe. ¿Sobrescribir? (y/n): ")
            if response.lower() != 'y':
                print("Operación cancelada.")
                return
        
        with open(output_path, 'w') as f:
            f.write(content)
        
        print(f"✅ Tarea creada: {output_path}")
        print(f"   Abre y edita el archivo para completar la tarea.")
        
    def list_tasks(self, status: str = 'all') -> None:
        """Listar tareas."""
        print("\n📋 TAREAS EN PROGRESO:")
        self._list_directory(self.progreso_dir)
        
        print("\n✅ TAREAS RESUELTAS:")
        self._list_directory(self.resueltas_dir)
    
    def _list_directory(self, directory: Path) -> None:
        """Listar archivos en directorio."""
        if not directory.exists():
            print("   (Sin tareas)")
            return
        
        files = sorted(directory.glob('*.md'))
        if not files:
            print("   (Sin tareas)")
            return
        
        for f in files:
            # Extraer info del archivo
            with open(f, 'r') as file:
                first_line = file.readline()
                # Parsear: # Tarea T-XXX: Nombre
                if 'Tarea' in first_line:
                    print(f"   • {f.name}")
    
    def validate_task(self, filepath: str) -> None:
        """Validar completitud de tarea."""
        path = Path(filepath)
        if not path.exists():
            print(f"❌ Archivo no encontrado: {filepath}")
            return
        
        with open(path, 'r') as f:
            content = f.read()
        
        # Checklist de validación
        checks = {
            "Encabezado (Tipo, Fecha)": "**Tipo:**" in content,
            "Sección 1 (Contexto)": "## 1." in content,
            "Sección 2 (Modelamiento)": "## 2." in content,
            "Sección 3 (Método)": "## 3." in content,
            "Sección 4 (Implementación)": "## 4." in content,
            "Sección 5 (Verificación)": "## 5." in content,
            "Sección 6 (Interpretación)": "## 6." in content,
            "Sección 7 (Conclusiones)": "## 7." in content,
            "Código Python (```python)": "```python" in content,
            "Ecuaciones LaTeX ($)": "$" in content,
            "Tabla (|)": "|" in content,
        }
        
        print(f"\n📋 VALIDACIÓN: {path.name}")
        print("-" * 50)
        
        completed = 0
        for check_name, result in checks.items():
            symbol = "✓" if result else "✗"
            print(f"{symbol} {check_name}")
            if result:
                completed += 1
        
        percentage = (completed / len(checks)) * 100
        print("-" * 50)
        print(f"Completitud: {completed}/{len(checks)} ({percentage:.0f}%)")
        
        if percentage >= 90:
            print("✅ Tarea prácticamente lista para entregar")
        elif percentage >= 70:
            print("⚠️  Tarea en progreso avanzado, faltan detalles")
        elif percentage >= 50:
            print("📝 Tarea en progreso, falta más trabajo")
        else:
            print("🚧 Tarea en etapa inicial")
    
    def move_to_completed(self, filepath: str) -> None:
        """Mover tarea a carpeta de resueltas."""
        path = Path(filepath)
        if not path.exists():
            print(f"❌ Archivo no encontrado: {filepath}")
            return
        
        target = self.resueltas_dir / path.name
        if target.exists():
            response = input(f"⚠️  Archivo existe en resueltas. ¿Sobrescribir? (y/n): ")
            if response.lower() != 'y':
                return
        
        path.rename(target)
        print(f"✅ Tarea movida: {target}")
    
    def stats(self) -> None:
        """Mostrar estadísticas."""
        en_progreso = len(list(self.progreso_dir.glob('*.md'))) if self.progreso_dir.exists() else 0
        resueltas = len(list(self.resueltas_dir.glob('*.md'))) if self.resueltas_dir.exists() else 0
        
        print("\n📊 ESTADÍSTICAS:")
        print(f"   En progreso: {en_progreso}")
        print(f"   Resueltas: {resueltas}")
        print(f"   Total: {en_progreso + resueltas}")


def main():
    """Función principal."""
    parser = argparse.ArgumentParser(
        description="Gestor de tareas — ",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos:
  python task_manager.py create --type problema-cotidiano --id T-001 --name "Ruta de entrega"
  python task_manager.py list
  python task_manager.py validate documentation/tareas/en-progreso/tarea-T-001-*.md
  python task_manager.py move documentation/tareas/en-progreso/tarea-T-001-*.md
  python task_manager.py stats
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Comando')
    
    # Comando: create
    create_parser = subparsers.add_parser('create', help='Crear nueva tarea')
    create_parser.add_argument('--type', required=True, 
                               choices=['problema-cotidiano', 'especializacion', 'investigacion', 'proyecto'],
                               help='Tipo de tarea')
    create_parser.add_argument('--id', required=True, help='ID de tarea (ej: T-001)')
    create_parser.add_argument('--name', required=True, help='Nombre descriptivo')
    
    # Comando: list
    subparsers.add_parser('list', help='Listar tareas')
    
    # Comando: validate
    validate_parser = subparsers.add_parser('validate', help='Validar tarea')
    validate_parser.add_argument('file', help='Ruta del archivo .md')
    
    # Comando: move
    move_parser = subparsers.add_parser('move', help='Mover tarea a resueltas')
    move_parser.add_argument('file', help='Ruta del archivo .md')
    
    # Comando: stats
    subparsers.add_parser('stats', help='Mostrar estadísticas')
    
    args = parser.parse_args()
    
    manager = TaskManager()
    
    if args.command == 'create':
        manager.create_task(args.type, args.id, args.name)
    elif args.command == 'list':
        manager.list_tasks()
    elif args.command == 'validate':
        manager.validate_task(args.file)
    elif args.command == 'move':
        manager.move_to_completed(args.file)
    elif args.command == 'stats':
        manager.stats()
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
