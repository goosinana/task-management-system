from flask import Blueprint, render_template
from datetime import datetime

reports_bp = Blueprint('reports', __name__)

@reports_bp.route('/reports')
def show_reports():
    # Пример статистики
    stats = {
        'total_tasks': 10,
        'completed': 4,
        'in_progress': 3,
        'new': 3,
        'generated_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    return render_template('reports.html', stats=stats)
