<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Perfil Cristiano Barbosa</title>
    <style>
        body {
            background-color: #0d1117;
            color: #c9d1d9;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji";
            margin: 0;
            display: flex;
            justify-content: center;
        }

        .container {
            display: flex;
            width: 100%;
            max-width: 1200px; /* Ajuste conforme necessário */
            margin-top: 20px;
        }

        /* Coluna Esquerda (Sidebar) */
        .sidebar {
            width: 300px;
            padding: 20px;
            border-right: 1px solid #30363d;
            box-sizing: border-box;
            position: sticky; /* Mantém a sidebar visível ao rolar (opcional) */
            top: 20px;
            height: fit-content;
        }

        .profile-pic-container {
            width: 100%;
            padding-top: 100%; /* Mantém proporção quadrada */
            border-radius: 50%;
            background-color: #c9d1d9; /* Cor temporária ou de fallback */
            position: relative;
            overflow: hidden;
            border: 1px solid #30363d;
        }

        .profile-pic {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            object-fit: cover; /* Garante que a imagem preencha o círculo */
        }

        .status-dot {
            position: absolute;
            bottom: 5%;
            right: 5%;
            width: 15px;
            height: 15px;
            background-color: #238636; /* Verde online */
            border-radius: 50%;
            border: 2px solid #0d1117;
        }

        .profile-name {
            font-size: 24px;
            font-weight: 600;
            margin-top: 15px;
            margin-bottom: 5px;
            color: #ffffff;
        }

        .profile-username {
            font-size: 16px;
            color: #8b949e;
            margin-bottom: 20px;
        }

        .bio {
            font-size: 14px;
            margin-bottom: 15px;
        }

        .edit-profile-button {
            display: block;
            width: 100%;
            padding: 5px 16px;
            font-size: 14px;
            font-weight: 500;
            color: #c9d1d9;
            background-color: #21262d;
            border: 1px solid rgba(240, 246, 252, 0.1);
            border-radius: 6px;
            text-align: center;
            text-decoration: none;
            margin-bottom: 20px;
        }

        .profile-stats {
            font-size: 12px;
            color: #8b949e;
            margin-bottom: 20px;
        }

        .sidebar-links {
            margin-bottom: 20px;
        }

        .sidebar-link {
            display: flex;
            align-items: center;
            font-size: 14px;
            color: #c9d1d9;
            text-decoration: none;
            margin-bottom: 8px;
        }

        .sidebar-link img {
            margin-right: 8px;
            width: 16px; /* Tamanho do ícone */
            height: 16px;
        }

        .achievements-title {
            font-size: 16px;
            font-weight: 600;
            color: #ffffff;
            margin-top: 20px;
            margin-bottom: 10px;
        }

        .achievements {
            display: flex;
            gap: 10px;
        }

        /* Coluna Direita (Conteúdo Principal) */
        .main-content {
            flex: 1;
            padding: 20px 40px;
            box-sizing: border-box;
        }

        .section-separator {
            border: none;
            border-top: 1px solid #30363d;
            margin: 40px 0;
        }

        /* Estilos específicos para elementos do seu README */
        .philosophy-text b { color: #ffffff; }
        .gif-border {
            border-radius: 12px;
            border: 3px solid #00d2ff;
            box-shadow: 0 0 45px rgba(0, 210, 255, 0.4);
            display: inline-block;
            padding: 5px;
            background: #0d1117;
        }

        .certifications-box {
            display: inline-block;
            background-color: #0d1117;
            padding: 25px;
            border-radius: 15px;
            border: 1px solid #30363d;
            width: 100%;
            max-width: 700px;
        }
    </style>
</head>
<body>

    <div class="container">
        <div class="sidebar">
            <div class="profile-pic-container">
                <img src="" alt="Sua Foto" class="profile-pic">
                <div class="status-dot"></div>
            </div>
            
            <div class="profile-name">Cristiano A. Barbosa</div>
            <div class="profile-username">analytics.barbosa</div> <div class="bio">Phantom Programmer | Incognito Coder. Behind the screen, beyond the scene.</div> <a href="#" class="edit-profile-button">Editar Perfil</a>

            <div class="profile-stats">55 seguidores • 2 seguindo</div>

            <div class="sidebar-links">
                <a href="https://linkedin.com/in/cristiano-alves-barbosa" class="sidebar-link" target="_blank">
                    <img src="https://img.shields.io/badge/LinkedIn-9200ff?style=flat&logo=linkedin&logoColor=ffffff&label=" alt="Linkedin"> Cristiano Alves Barbosa
                </a>
                <a href="mailto:analytics.barbosa@gmail.com" class="sidebar-link">
                    <img src="https://img.shields.io/badge/Email-9200ff?style=flat&logo=gmail&logoColor=ffffff&label=" alt="Email"> analytics.barbosa@gmail.com
                </a>
                <a href="https://alvenato.github.io/Alvenato/" class="sidebar-link" target="_blank">
                    <img src="https://img.shields.io/badge/Portfolio-9200ff?style=flat&logo=about.me&logoColor=ffffff&label=" alt="Portfolio"> Portfolio
                </a>
                <div class="sidebar-link"><img src="https://img.shields.io/badge/Location-9200ff?style=flat&logo=googlemaps&logoColor=ffffff&label=" alt="Location"> 12°38'06.9"S 38°16'05.4"W (Exemplo)</div>
            </div>

            <hr class="section-separator">

            <div class="achievements-title">Achievements</div>
            <div class="achievements">
                <img src="path/to/achievement-icon1.png" alt="Achievement 1" width="30" height="30">
                <img src="path/to/achievement-icon2.png" alt="Achievement 2" width="30" height="30">
            </div>
        </div>

        <div class="main-content">
            
            <div align="center">
                <img src="https://capsule-render.vercel.app/api?type=waving&color=0d1117&customColorList=10,00d2ff,9200ff&height=280&section=header&text=Cristiano%20A.%20Barbosa&fontSize=75&animation=fadeIn&fontAlignY=35&fontColor=00d2ff&desc=CIÊNCIA%20DE%20DADOS%20E%20IA&descSize=30&descAlignY=65" width="100%" />
            </div>

            <br><br>

            <table align="center" width="100%" style="background-color: #0d1117; border-collapse: collapse; border: none;">
                <tr style="border: none;">
                    <td width="55%" style="vertical-align: top; padding: 20px; background-color: #0d1117; border: none;">
                        <h2 align="left" style="color: #00d2ff; border-bottom: none;">Filosofia</h2>
                        <p align="left" style="color: #c9d1d9;">
                            Focado na <b>integridade e visualização de dados</b>. Atuo na linha de frente do processamento de informações (ETL), transformando dados brutos de APIs e bancos SQL em <b>dashboards estratégicos</b> no Power BI e Tableau. Minha missão é garantir o monitoramento preciso de fluxos técnicos e entregar indicadores que facilitem a tomada de decisão em cenários de alta complexidade.
                        </p>
                    </td>
                    <td width="45%" align="center" style="background-color: #0d1117; padding: 10px; border: none; vertical-align: middle;">
                        <div class="gif-border">
                            <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJueGZ3bmZueXp3eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4JmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCZjdD1n/qgQUggAC3Pfv687qPC/giphy.gif" width="100%" style="border-radius: 8px; display: block;"/>
                        </div>
                    </td>
                </tr>
            </table>

            <hr class="section-separator">

            <div align="center">
                <h2 style="color: #9200ff;">Tecnologia</h2>
                <p style="color: #c9d1d9;"><i>Stack tecnológica voltada para pipelines de dados e visualização analítica</i></p>
                <img src="https://skillicons.dev/icons?i=py,postgres,mysql,sqlite,beaver,docker,vscode,github,figma,powerbi,tableau,excel&theme=dark" />
            </div>

            <hr class="section-separator">

            <div align="center">
                <div class="certifications-box">
                    <h3 style="color: #9200ff; margin-bottom: 20px; white-space: nowrap;">Certificações & Educação</h3>
                    <p align="center">
                        <img src="https://assets.dio.me/c_6-enx_gsCjBqdsEtj4RN1yYCoEx9voHbg9U74chJ0/f:webp/q:80/w:120/L2NvdXJzZXMvYmFkZ2UvZDdlNmRkNGQtOTMyNi00OTUwLTgxZWUtNzJjNTc4NTY1M2E1LnBuZw" width="110px" alt="DIO Badge 1" />
                        &nbsp;&nbsp;&nbsp;
                        <img src="https://hermes.dio.me/courses/badge/2cd42ffc-5a40-42d3-b4eb-572d16249cba.png" width="110px" alt="DIO Badge 2" />
                        &nbsp;&nbsp;&nbsp;
                        <img src="https://hermes.dio.me/courses/badge/406684a4-396d-4160-94b9-ead934e18564.png" width="110px" alt="DIO Badge 3" />
                    </p>
                    <p style="color: #c9d1d9; font-size: 15px; line-height: 1.6; margin-top: 15px;">
                        <i>Desenvolvimento contínuo em <b>Ciência de Dados, Inteligência Artificial e Engenharia de Analytics</b> através da Digital Innovation One. Foco constante na atualização técnica para as demandas mais complexas do mercado de dados.</i>
                    </p>
                </div>
            </div>

            <hr class="section-separator">

            <div align="center">
                <h2 style="color: #9200ff;">Análise de Proficiência</h2>
                
                <h3 style="color: #00d2ff; margin-bottom: 15px;">Linguagens mais utilizadas</h3>
                <img width="60%" src="https://github-readme-stats-sigma-five.vercel.app/api/top-langs/?username=Alvenato&layout=compact&theme=tokyonight&hide_border=true&title_color=00d2ff&text_color=ffffff&bg_color=0d1117&langs_count=10&hide_title=true&locale=pt-br&v=6" />

                <br><br><br>

                <h3 style="color: #00d2ff; margin-bottom: 15px;">Frequência de Atividade</h3>
                <img width="100%" src="https://github-readme-activity-graph.vercel.app/graph?username=Alvenato&theme=tokyonight&bg_color=0d1117&area=true&hide_border=true&border_radius=10&line=00d2ff&point=9200ff&color=ffffff" />

                <br>

                <img src="https://github-readme-streak-stats.herokuapp.com/?user=Alvenato&theme=tokyonight&background=0d1117&border_radius=10&hide_border=true&stroke=00d2ff&ring=9200ff&fire=00d2ff" />
            </div>

            <hr class="section-separator">

            <div align="center">
                <img src="https://capsule-render.vercel.app/api?type=waving&color=0d1117&customColorList=10,9200ff,00d2ff&height=80&section=footer" width="100%" />
            </div>
            
        </div>
    </div>

</body>
</html>
