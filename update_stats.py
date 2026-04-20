import os
import json
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import RunReportRequest, DateRange, Dimension, Metric

# Configurações de Ambiente
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Users\Cristiano A. Barbosa\OneDrive\Desktop\unidade-visual-code-studio-9dbbd743890a.json"
property_id = "473359623"

client = BetaAnalyticsDataClient()

def get_full_analytics():
    # Requisitando múltiplas dimensões para um panorama completo
    request = RunReportRequest(
        property=f"properties/{property_id}",
        dimensions=[
            Dimension(name="date"), 
            Dimension(name="city"), 
            Dimension(name="country"),
            Dimension(name="deviceCategory"),
            Dimension(name="pageTitle")
        ],
        metrics=[Metric(name="activeUsers")],
        date_ranges=[DateRange(start_date="30daysAgo", end_date="today")],
    )

    response = client.run_report(request)
    
    report_data = []
    for row in response.rows:
        report_data.append({
            "date": row.dimension_values[0].value,
            "city": row.dimension_values[1].value,
            "country": row.dimension_values[2].value,
            "device": row.dimension_values[3].value,
            "page": row.dimension_values[4].value,
            "users": int(row.metric_values[0].value)
        })

    # Salvando com indentação para facilitar leitura se necessário
    with open('analytics_data.json', 'w', encoding='utf-8') as f:
        json.dump(report_data, f, ensure_ascii=False, indent=4)
    
    print(f"✅ [{row.dimension_values[0].value}] Dados completos atualizados!")

if __name__ == "__main__":
    get_full_analytics()
