import os
import json
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    DateRange,
    Metric,
    Dimension,
    RunReportRequest,
)

# Configurações - AJUSTE AQUI
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Users\Cristiano A. Barbosa\OneDrive\Desktop\unidade-visual-code-studio-9dbbd743890a.json"
PROPERTY_ID = "513962275"

def get_analytics_data():
    client = BetaAnalyticsDataClient()

    # Pedindo usuários ativos por data nos últimos 30 dias
    request = RunReportRequest(
        property=f"properties/{PROPERTY_ID}",
        dimensions=[Dimension(name="date")],
        metrics=[Metric(name="activeUsers")],
        date_ranges=[DateRange(start_date="30daysAgo", end_date="today")],
    )
    
    response = client.run_report(request)
    
    data = []
    for row in response.rows:
        # Formatando a data de AAAAMMDD para AAAA-MM-DD
        raw_date = row.dimension_values[0].value
        formatted_date = f"{raw_date[:4]}-{raw_date[4:6]}-{raw_date[6:]}"
        data.append({
            "date": formatted_date,
            "users": int(row.metric_values[0].value)
        })

    # Ordenar por data
    data.sort(key=lambda x: x['date'])

    # Salvar para o site ler
    with open('analytics_data.json', 'w') as f:
        json.dump(data, f)
    
    print("✅ Dados atualizados com sucesso no arquivo analytics_data.json!")

if __name__ == "__main__":
    get_analytics_data()
