import os
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import RunReportRequest, DateRange, Dimension, Metric
import json

# Caminho da sua chave (Mantenha o seu caminho completo)
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Users\Cristiano A. Barbosa\OneDrive\Desktop\unidade-visual-code-studio-9dbbd743890a.json"
property_id = "473359623" 

client = BetaAnalyticsDataClient()

def get_data():
    # Pedido de dados: Acessos por Data e Cidade
    request = RunReportRequest(
        property=f"properties/{property_id}",
        dimensions=[Dimension(name="date"), Dimension(name="city")],
        metrics=[Metric(name="activeUsers")],
        date_ranges=[DateRange(start_date="30daysAgo", end_date="today")],
    )
    
    response = client.run_report(request)
    
    data = []
    for row in response.rows:
        data.append({
            "date": row.dimension_values[0].value,
            "city": row.dimension_values[1].value,
            "users": int(row.metric_values[0].value)
        })
    
    with open('analytics_data.json', 'w') as f:
        json.dump(data, f)
    print("✅ Dados geográficos atualizados com sucesso!")

get_data()
