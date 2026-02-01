"""
BBP Road Application - Streamlit Frontend
Professional Industrial Design - Gemini Style
"""
import streamlit as st
import pandas as pd
import numpy as np
import requests
import folium
from streamlit_folium import st_folium
from datetime import datetime

# ============== Configuration ==============
BACKEND_URL = "https://huxuyan.onrender.com"

# ============== Complete Translations ==============
TRANSLATIONS = {
    "en": {
        "app_name": "BBP Road Monitor",
        "app_subtitle": "Intelligent Road Condition Analysis System",
        "dashboard": "Dashboard",
        "route_planning": "Route Planning",
        "segments": "Segments",
        "reports": "Reports",
        "trips": "Trips",
        "auto_detection": "Auto Detection",
        "settings": "Settings",
        "navigation": "Navigation",
        "logout": "Sign Out",
        "logged_in": "Active Session",
        "login": "Sign In",
        "register": "Register",
        "username": "Username",
        "enter_username": "Enter your username",
        "login_register": "Sign In / Register",
        "login_hint": "Enter any username to sign in. New users are automatically registered.",
        "please_enter_username": "Please enter a username",
        "user_profile": "User Profile",
        "member_since": "Member since",
        "user_id": "User ID",
        "account_status": "Account Status",
        "active": "Active",
        "system_overview": "System Overview",
        "total_segments": "Total Segments",
        "active_reports": "Active Reports",
        "completed_trips": "Completed Trips",
        "system_status": "System Status",
        "online": "Online",
        "recent_activity": "Recent Activity",
        "quick_stats": "Quick Statistics",
        "road_conditions": "Road Conditions",
        "good": "Good",
        "moderate": "Moderate",
        "poor": "Poor",
        "critical": "Critical",
        "plan_route": "Plan Route",
        "origin": "Origin",
        "destination": "Destination",
        "latitude": "Latitude",
        "longitude": "Longitude",
        "find_routes": "Find Routes",
        "route_results": "Route Results",
        "no_routes_found": "No routes found",
        "distance": "Distance",
        "duration": "Duration",
        "route_quality": "Route Quality",
        "road_segments": "Road Segments",
        "add_segment": "Add Segment",
        "segment_name": "Segment Name",
        "start_point": "Start Point",
        "end_point": "End Point",
        "segment_details": "Segment Details",
        "condition": "Condition",
        "last_updated": "Last Updated",
        "no_segments": "No segments available",
        "create_segment": "Create Segment",
        "segment_created": "Segment created successfully",
        "submit_report": "Submit Report",
        "report_type": "Report Type",
        "severity": "Severity",
        "description": "Description",
        "location": "Location",
        "select_segment": "Select Segment",
        "report_submitted": "Report submitted successfully",
        "existing_reports": "Existing Reports",
        "no_reports": "No reports available",
        "pothole": "Pothole",
        "crack": "Crack",
        "flooding": "Flooding",
        "debris": "Debris",
        "other": "Other",
        "low": "Low",
        "medium": "Medium",
        "high": "High",
        "trip_history": "Trip History",
        "start_trip": "Start Trip",
        "end_trip": "End Trip",
        "trip_in_progress": "Trip in Progress",
        "no_active_trip": "No Active Trip",
        "trip_started": "Trip started",
        "trip_ended": "Trip ended",
        "no_trips": "No trips recorded",
        "trip_details": "Trip Details",
        "start_time": "Start Time",
        "end_time": "End Time",
        "status": "Status",
        "sensor_simulation": "Sensor Simulation",
        "current_speed": "Current Speed",
        "simulate_event": "Simulate Event",
        "normal": "Normal",
        "bump": "Bump",
        "severe": "Severe",
        "peak_acceleration": "Peak Acceleration",
        "detection_result": "Detection Result",
        "smooth_surface": "Road surface is smooth",
        "minor_irregularity": "Minor road irregularity detected",
        "significant_defect": "Significant road defect detected",
        "major_damage": "Major road damage detected",
        "submit_detection": "Submit Detection",
        "apply_to_segment": "Apply to Segment",
        "detection_submitted": "Detection submitted",
        "language_preference": "Language Preference",
        "display_settings": "Display Settings",
        "notification_settings": "Notification Settings",
        "enable_notifications": "Enable Notifications",
        "save_settings": "Save Settings",
        "settings_saved": "Settings saved successfully",
        "language": "Language",
        "dark_mode": "Dark Mode",
        "notifications": "Notifications",
        "theme": "Theme",
        "light": "Light",
        "dark": "Dark",
        "save": "Save",
        "cancel": "Cancel",
        "delete": "Delete",
        "edit": "Edit",
        "view": "View",
        "loading": "Loading...",
        "error": "Error",
        "success": "Success",
        "warning": "Warning",
        "info": "Information",
        "confirm": "Confirm",
        "submit": "Submit",
        "search": "Search",
        "refresh": "Refresh",
        "connection_error": "Cannot connect to server",
        "api_error": "API Error",
        "routes_found": "routes found",
        "requesting_location": "Requesting location...",
        "allow_location": "Please allow location access",
        "location_acquired": "Location acquired",
        "gps_active": "GPS signal active",
        "location_unavailable": "Location unavailable",
        "geolocation_not_supported": "Geolocation not supported",
        "using_default": "Using default location",
        "speed_help": "Use this if GPS speed is not available",
    },
    "zh": {
        "app_name": "BBP 道路监测",
        "app_subtitle": "智能道路状况分析系统",
        "dashboard": "仪表板",
        "route_planning": "路线规划",
        "segments": "路段管理",
        "reports": "问题报告",
        "trips": "行程记录",
        "auto_detection": "自动检测",
        "settings": "系统设置",
        "navigation": "导航菜单",
        "logout": "退出登录",
        "logged_in": "会话活跃",
        "login": "登录",
        "register": "注册",
        "username": "用户名",
        "enter_username": "请输入用户名",
        "login_register": "登录 / 注册",
        "login_hint": "输入任意用户名即可登录，新用户将自动注册。",
        "please_enter_username": "请输入用户名",
        "user_profile": "用户资料",
        "member_since": "注册时间",
        "user_id": "用户ID",
        "account_status": "账户状态",
        "active": "活跃",
        "system_overview": "系统概览",
        "total_segments": "路段总数",
        "active_reports": "活跃报告",
        "completed_trips": "完成行程",
        "system_status": "系统状态",
        "online": "在线",
        "recent_activity": "最近活动",
        "quick_stats": "快速统计",
        "road_conditions": "路况分布",
        "good": "良好",
        "moderate": "一般",
        "poor": "较差",
        "critical": "严重",
        "plan_route": "规划路线",
        "origin": "起点",
        "destination": "终点",
        "latitude": "纬度",
        "longitude": "经度",
        "find_routes": "查找路线",
        "route_results": "路线结果",
        "no_routes_found": "未找到路线",
        "distance": "距离",
        "duration": "时长",
        "route_quality": "路线质量",
        "road_segments": "道路路段",
        "add_segment": "添加路段",
        "segment_name": "路段名称",
        "start_point": "起始点",
        "end_point": "结束点",
        "segment_details": "路段详情",
        "condition": "路况",
        "last_updated": "最后更新",
        "no_segments": "暂无路段数据",
        "create_segment": "创建路段",
        "segment_created": "路段创建成功",
        "submit_report": "提交报告",
        "report_type": "报告类型",
        "severity": "严重程度",
        "description": "详细描述",
        "location": "位置",
        "select_segment": "选择路段",
        "report_submitted": "报告提交成功",
        "existing_reports": "现有报告",
        "no_reports": "暂无报告",
        "pothole": "坑洞",
        "crack": "裂缝",
        "flooding": "积水",
        "debris": "障碍物",
        "other": "其他",
        "low": "低",
        "medium": "中",
        "high": "高",
        "trip_history": "行程历史",
        "start_trip": "开始行程",
        "end_trip": "结束行程",
        "trip_in_progress": "行程进行中",
        "no_active_trip": "无活跃行程",
        "trip_started": "行程已开始",
        "trip_ended": "行程已结束",
        "no_trips": "暂无行程记录",
        "trip_details": "行程详情",
        "start_time": "开始时间",
        "end_time": "结束时间",
        "status": "状态",
        "sensor_simulation": "传感器模拟",
        "current_speed": "当前速度",
        "simulate_event": "模拟事件",
        "normal": "正常",
        "bump": "颠簸",
        "severe": "严重",
        "peak_acceleration": "峰值加速度",
        "detection_result": "检测结果",
        "smooth_surface": "路面平整",
        "minor_irregularity": "检测到轻微路面不平",
        "significant_defect": "检测到明显路面缺陷",
        "major_damage": "检测到严重路面损坏",
        "submit_detection": "提交检测",
        "apply_to_segment": "应用到路段",
        "detection_submitted": "检测已提交",
        "language_preference": "语言偏好",
        "display_settings": "显示设置",
        "notification_settings": "通知设置",
        "enable_notifications": "启用通知",
        "save_settings": "保存设置",
        "settings_saved": "设置保存成功",
        "language": "语言",
        "dark_mode": "深色模式",
        "notifications": "通知",
        "theme": "主题",
        "light": "浅色",
        "dark": "深色",
        "save": "保存",
        "cancel": "取消",
        "delete": "删除",
        "edit": "编辑",
        "view": "查看",
        "loading": "加载中...",
        "error": "错误",
        "success": "成功",
        "warning": "警告",
        "info": "信息",
        "confirm": "确认",
        "submit": "提交",
        "search": "搜索",
        "refresh": "刷新",
        "connection_error": "无法连接到服务器",
        "api_error": "接口错误",
        "routes_found": "条路线",
        "requesting_location": "正在获取位置...",
        "allow_location": "请允许位置访问",
        "location_acquired": "位置已获取",
        "gps_active": "GPS信号活跃",
        "location_unavailable": "无法获取位置",
        "geolocation_not_supported": "不支持地理定位",
        "using_default": "使用默认位置",
        "speed_help": "如果GPS速度不可用，请使用此滑块",
    },
    "it": {
        "app_name": "BBP Monitoraggio Stradale",
        "app_subtitle": "Sistema Intelligente di Analisi Stradale",
        "dashboard": "Cruscotto",
        "route_planning": "Pianificazione Percorso",
        "segments": "Segmenti",
        "reports": "Rapporti",
        "trips": "Viaggi",
        "auto_detection": "Rilevamento Automatico",
        "settings": "Impostazioni",
        "navigation": "Navigazione",
        "logout": "Esci",
        "logged_in": "Sessione Attiva",
        "login": "Accedi",
        "register": "Registrati",
        "username": "Nome utente",
        "enter_username": "Inserisci nome utente",
        "login_register": "Accedi / Registrati",
        "login_hint": "Inserisci un nome utente. I nuovi utenti vengono registrati automaticamente.",
        "please_enter_username": "Inserisci un nome utente",
        "user_profile": "Profilo Utente",
        "member_since": "Membro dal",
        "user_id": "ID Utente",
        "account_status": "Stato Account",
        "active": "Attivo",
        "system_overview": "Panoramica Sistema",
        "total_segments": "Segmenti Totali",
        "active_reports": "Rapporti Attivi",
        "completed_trips": "Viaggi Completati",
        "system_status": "Stato Sistema",
        "online": "Online",
        "recent_activity": "Attivita Recente",
        "quick_stats": "Statistiche Rapide",
        "road_conditions": "Condizioni Stradali",
        "good": "Buono",
        "moderate": "Moderato",
        "poor": "Scarso",
        "critical": "Critico",
        "plan_route": "Pianifica Percorso",
        "origin": "Origine",
        "destination": "Destinazione",
        "latitude": "Latitudine",
        "longitude": "Longitudine",
        "find_routes": "Trova Percorsi",
        "route_results": "Risultati Percorso",
        "no_routes_found": "Nessun percorso trovato",
        "distance": "Distanza",
        "duration": "Durata",
        "route_quality": "Qualita Percorso",
        "road_segments": "Segmenti Stradali",
        "add_segment": "Aggiungi Segmento",
        "segment_name": "Nome Segmento",
        "start_point": "Punto Iniziale",
        "end_point": "Punto Finale",
        "segment_details": "Dettagli Segmento",
        "condition": "Condizione",
        "last_updated": "Ultimo Aggiornamento",
        "no_segments": "Nessun segmento disponibile",
        "create_segment": "Crea Segmento",
        "segment_created": "Segmento creato con successo",
        "submit_report": "Invia Rapporto",
        "report_type": "Tipo Rapporto",
        "severity": "Gravita",
        "description": "Descrizione",
        "location": "Posizione",
        "select_segment": "Seleziona Segmento",
        "report_submitted": "Rapporto inviato con successo",
        "existing_reports": "Rapporti Esistenti",
        "no_reports": "Nessun rapporto disponibile",
        "pothole": "Buca",
        "crack": "Crepa",
        "flooding": "Allagamento",
        "debris": "Detriti",
        "other": "Altro",
        "low": "Basso",
        "medium": "Medio",
        "high": "Alto",
        "trip_history": "Storico Viaggi",
        "start_trip": "Inizia Viaggio",
        "end_trip": "Termina Viaggio",
        "trip_in_progress": "Viaggio in Corso",
        "no_active_trip": "Nessun Viaggio Attivo",
        "trip_started": "Viaggio iniziato",
        "trip_ended": "Viaggio terminato",
        "no_trips": "Nessun viaggio registrato",
        "trip_details": "Dettagli Viaggio",
        "start_time": "Ora Inizio",
        "end_time": "Ora Fine",
        "status": "Stato",
        "sensor_simulation": "Simulazione Sensore",
        "current_speed": "Velocita Attuale",
        "simulate_event": "Simula Evento",
        "normal": "Normale",
        "bump": "Dosso",
        "severe": "Grave",
        "peak_acceleration": "Accelerazione Massima",
        "detection_result": "Risultato Rilevamento",
        "smooth_surface": "Superficie stradale liscia",
        "minor_irregularity": "Irregolarita stradale minore rilevata",
        "significant_defect": "Difetto stradale significativo rilevato",
        "major_damage": "Danno stradale maggiore rilevato",
        "submit_detection": "Invia Rilevamento",
        "apply_to_segment": "Applica a Segmento",
        "detection_submitted": "Rilevamento inviato",
        "language_preference": "Preferenza Lingua",
        "display_settings": "Impostazioni Display",
        "notification_settings": "Impostazioni Notifiche",
        "enable_notifications": "Abilita Notifiche",
        "save_settings": "Salva Impostazioni",
        "settings_saved": "Impostazioni salvate con successo",
        "language": "Lingua",
        "dark_mode": "Modalita Scura",
        "notifications": "Notifiche",
        "theme": "Tema",
        "light": "Chiaro",
        "dark": "Scuro",
        "save": "Salva",
        "cancel": "Annulla",
        "delete": "Elimina",
        "edit": "Modifica",
        "view": "Visualizza",
        "loading": "Caricamento...",
        "error": "Errore",
        "success": "Successo",
        "warning": "Avviso",
        "info": "Informazione",
        "confirm": "Conferma",
        "submit": "Invia",
        "search": "Cerca",
        "refresh": "Aggiorna",
        "connection_error": "Impossibile connettersi al server",
        "api_error": "Errore API",
        "routes_found": "percorsi trovati",
        "requesting_location": "Richiesta posizione...",
        "allow_location": "Consenti accesso alla posizione",
        "location_acquired": "Posizione acquisita",
        "gps_active": "Segnale GPS attivo",
        "location_unavailable": "Posizione non disponibile",
        "geolocation_not_supported": "Geolocalizzazione non supportata",
        "using_default": "Utilizzo posizione predefinita",
        "speed_help": "Usa questo se la velocita GPS non e disponibile",
    }
}

def t(key: str) -> str:
    """Translate a key to current language."""
    lang = st.session_state.get("language", "en")
    return TRANSLATIONS.get(lang, TRANSLATIONS["en"]).get(key, key)

# ============== Page Configuration ==============
st.set_page_config(
    page_title="BBP Road Monitor",
    page_icon="B",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============== Session State ==============
if "user" not in st.session_state:
    st.session_state.user = None
if "language" not in st.session_state:
    st.session_state.language = "en"
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False
if "current_page" not in st.session_state:
    st.session_state.current_page = "dashboard"

# ============== Professional CSS - Gemini Style ==============
def get_theme_css():
    if st.session_state.dark_mode:
        return """
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
            
            .stApp {
                background: #131314 !important;
                font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
            }
            
            [data-testid="stSidebar"] {
                background: #1e1f20 !important;
                border-right: 1px solid #303134 !important;
            }
            [data-testid="stSidebar"] > div:first-child {
                background: #1e1f20 !important;
            }
            
            .stApp, .stApp p, .stApp span, .stApp label, .stApp div {
                color: #e3e3e3 !important;
            }
            
            h1, h2, h3, h4, h5, h6 {
                color: #ffffff !important;
                font-weight: 600 !important;
                letter-spacing: -0.02em !important;
            }
            
            .stTextInput input, .stSelectbox > div > div, .stNumberInput input {
                background: #303134 !important;
                border: 1px solid #5f6368 !important;
                border-radius: 8px !important;
                color: #e3e3e3 !important;
            }
            .stTextInput input:focus, .stSelectbox > div > div:focus {
                border-color: #8ab4f8 !important;
                box-shadow: 0 0 0 2px rgba(138, 180, 248, 0.2) !important;
            }
            
            .stButton > button {
                background: #303134 !important;
                border: 1px solid #5f6368 !important;
                border-radius: 24px !important;
                color: #e3e3e3 !important;
                font-weight: 500 !important;
                padding: 8px 24px !important;
                transition: all 0.2s ease !important;
            }
            .stButton > button:hover {
                background: #3c4043 !important;
                border-color: #8ab4f8 !important;
            }
            .stButton > button[kind="primary"] {
                background: #8ab4f8 !important;
                color: #202124 !important;
                border: none !important;
            }
            
            [data-testid="stMetric"] {
                background: #1e1f20 !important;
                border: 1px solid #303134 !important;
                border-radius: 12px !important;
                padding: 16px !important;
            }
            [data-testid="stMetricValue"] {
                color: #8ab4f8 !important;
            }
            
            .streamlit-expanderHeader {
                background: #1e1f20 !important;
                border: 1px solid #303134 !important;
                border-radius: 8px !important;
            }
            
            hr {
                border-color: #303134 !important;
            }
            
            ::-webkit-scrollbar {
                width: 8px;
                height: 8px;
            }
            ::-webkit-scrollbar-track {
                background: #1e1f20;
            }
            ::-webkit-scrollbar-thumb {
                background: #5f6368;
                border-radius: 4px;
            }
        </style>
        """
    else:
        return """
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
            
            .stApp {
                background: #ffffff !important;
                font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
            }
            
            [data-testid="stSidebar"] {
                background: #f8f9fa !important;
                border-right: 1px solid #e8eaed !important;
            }
            [data-testid="stSidebar"] > div:first-child {
                background: #f8f9fa !important;
            }
            [data-testid="stSidebar"] * {
                color: #202124 !important;
            }
            
            .stApp, .stApp p, .stApp span, .stApp label, .stApp div {
                color: #202124 !important;
            }
            
            h1, h2, h3, h4, h5, h6 {
                color: #202124 !important;
                font-weight: 600 !important;
                letter-spacing: -0.02em !important;
            }
            
            .stTextInput input, .stSelectbox > div > div, .stNumberInput input {
                background: #ffffff !important;
                border: 1px solid #dadce0 !important;
                border-radius: 8px !important;
                color: #202124 !important;
            }
            .stTextInput input:focus, .stSelectbox > div > div:focus {
                border-color: #1a73e8 !important;
                box-shadow: 0 0 0 2px rgba(26, 115, 232, 0.2) !important;
            }
            
            .stButton > button {
                background: #ffffff !important;
                border: 1px solid #dadce0 !important;
                border-radius: 24px !important;
                color: #202124 !important;
                font-weight: 500 !important;
                padding: 8px 24px !important;
                transition: all 0.2s ease !important;
            }
            .stButton > button:hover {
                background: #f1f3f4 !important;
                border-color: #1a73e8 !important;
            }
            .stButton > button[kind="primary"] {
                background: #1a73e8 !important;
                color: #ffffff !important;
                border: none !important;
            }
            
            [data-testid="stMetric"] {
                background: #f8f9fa !important;
                border: 1px solid #e8eaed !important;
                border-radius: 12px !important;
                padding: 16px !important;
            }
            [data-testid="stMetricValue"] {
                color: #1a73e8 !important;
            }
            
            .streamlit-expanderHeader {
                background: #f8f9fa !important;
                border: 1px solid #e8eaed !important;
                border-radius: 8px !important;
            }
            
            hr {
                border-color: #e8eaed !important;
            }
        </style>
        """

st.markdown(get_theme_css(), unsafe_allow_html=True)

# Additional common styles
st.markdown("""
<style>
    .profile-section {
        padding: 16px;
        margin-bottom: 16px;
        border-radius: 12px;
    }
    
    .profile-avatar {
        width: 36px;
        height: 36px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 600;
        font-size: 14px;
        margin-right: 12px;
    }
    
    .section-header {
        font-size: 13px;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        opacity: 0.6;
        margin: 24px 0 12px 16px;
    }
    
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stDeployButton {display: none;}
    
    .main .block-container {
        padding: 2rem 3rem;
        max-width: 1400px;
    }
</style>
""", unsafe_allow_html=True)

# ============== Helper Functions ==============
def api_get(endpoint: str, params: dict = None):
    try:
        resp = requests.get(f"{BACKEND_URL}{endpoint}", params=params, timeout=10)
        resp.raise_for_status()
        return resp.json()
    except:
        return None

def api_post(endpoint: str, json_data: dict = None, params: dict = None):
    try:
        resp = requests.post(f"{BACKEND_URL}{endpoint}", json=json_data, params=params, timeout=10)
        resp.raise_for_status()
        return resp.json()
    except:
        return None

def api_patch(endpoint: str, json_data: dict = None):
    try:
        resp = requests.patch(f"{BACKEND_URL}{endpoint}", json=json_data, timeout=10)
        resp.raise_for_status()
        return resp.json()
    except:
        return None

def get_seg_name(seg):
    return seg.get("road_name") or seg.get("name") or f"Segment {seg.get('id', '?')}"

def get_seg_coords(seg):
    start_lat = seg.get("start_lat") or seg.get("from_lat", 0)
    start_lon = seg.get("start_lon") or seg.get("from_lon", 0)
    end_lat = seg.get("end_lat") or seg.get("to_lat", 0)
    end_lon = seg.get("end_lon") or seg.get("to_lon", 0)
    return start_lat, start_lon, end_lat, end_lon

# ============== Sidebar ==============
with st.sidebar:
    st.markdown(f"### {t('app_name')}")
    st.caption(t('app_subtitle'))
    
    st.markdown("---")
    
    lang_options = ["en", "zh", "it"]
    lang_labels = {"en": "English", "zh": "中文", "it": "Italiano"}
    current_lang_idx = lang_options.index(st.session_state.language) if st.session_state.language in lang_options else 0
    
    new_lang = st.selectbox(
        t("language"),
        options=lang_options,
        format_func=lambda x: lang_labels[x],
        index=current_lang_idx,
        key="lang_selector"
    )
    
    if new_lang != st.session_state.language:
        st.session_state.language = new_lang
        if st.session_state.user:
            api_patch(f"/api/users/{st.session_state.user['id']}/settings", {"language": new_lang})
        st.rerun()

# ============== Login Section ==============
if st.session_state.user is None:
    st.markdown(f"# {t('app_name')}")
    st.markdown(f"#### {t('app_subtitle')}")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("---")
        username = st.text_input(t("username"), placeholder=t("enter_username"))
        
        if st.button(t("login_register"), use_container_width=True, type="primary"):
            if username.strip():
                result = api_post("/api/users", {"username": username.strip()})
                if result:
                    st.session_state.user = result
                    settings = api_get(f"/api/users/{result['id']}/settings")
                    if settings:
                        st.session_state.language = settings.get("language", "en")
                        st.session_state.dark_mode = settings.get("dark_mode", False)
                    st.rerun()
            else:
                st.warning(t("please_enter_username"))
        
        st.markdown("---")
        st.info(t("login_hint"))
    
    st.stop()

# ============== Main App ==============
user = st.session_state.user
user_id = user["id"]

with st.sidebar:
    st.markdown(f"""
    <div class="profile-section">
        <div style="display: flex; align-items: center;">
            <div class="profile-avatar" style="background: linear-gradient(135deg, #1a73e8, #8ab4f8); color: white;">
                {user['username'][0].upper()}
            </div>
            <div>
                <div style="font-weight: 600;">{user['username']}</div>
                <div style="font-size: 12px; opacity: 0.7;">{t('logged_in')}</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button(t("logout"), use_container_width=True):
        st.session_state.user = None
        st.session_state.dark_mode = False
        st.session_state.language = "en"
        st.session_state.current_page = "dashboard"
        st.rerun()
    
    st.markdown("---")
    st.markdown(f"<div class='section-header'>{t('navigation')}</div>", unsafe_allow_html=True)
    
    nav_items = [
        ("dashboard", t("dashboard")),
        ("route_planning", t("route_planning")),
        ("segments", t("segments")),
        ("reports", t("reports")),
        ("trips", t("trips")),
        ("auto_detection", t("auto_detection")),
        ("settings", t("settings"))
    ]
    
    for key, label in nav_items:
        is_active = st.session_state.current_page == key
        if st.button(
            label,
            key=f"nav_{key}",
            use_container_width=True,
            type="primary" if is_active else "secondary"
        ):
            st.session_state.current_page = key
            st.rerun()

menu = st.session_state.current_page

# ============== Dashboard ==============
if menu == "dashboard":
    st.title(t("dashboard"))
    st.markdown(f"##### {t('system_overview')}")
    
    segments = api_get("/api/segments", {"user_id": user_id}) or []
    reports = api_get("/api/reports", {"user_id": user_id}) or []
    trips = api_get("/api/trips", {"user_id": user_id}) or []
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(t("total_segments"), len(segments))
    with col2:
        st.metric(t("active_reports"), len(reports))
    with col3:
        st.metric(t("completed_trips"), len(trips))
    with col4:
        st.metric(t("system_status"), t("online"))
    
    st.markdown("---")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown(f"##### {t('road_segments')}")
        m = folium.Map(location=[41.9028, 12.4964], zoom_start=12)
        
        for seg in segments[:20]:
            start_lat, start_lon, end_lat, end_lon = get_seg_coords(seg)
            if start_lat and start_lon:
                condition = seg.get("condition", "unknown")
                colors = {"good": "#34a853", "moderate": "#fbbc04", "poor": "#ea4335", "critical": "#9c27b0"}
                color = colors.get(condition, "#1a73e8")
                
                folium.PolyLine(
                    locations=[[start_lat, start_lon], [end_lat, end_lon]],
                    color=color,
                    weight=4,
                    opacity=0.8
                ).add_to(m)
        
        st_folium(m, width=None, height=400, returned_objects=[])
    
    with col2:
        st.markdown(f"##### {t('quick_stats')}")
        
        conditions = {"good": 0, "moderate": 0, "poor": 0, "critical": 0}
        for seg in segments:
            cond = seg.get("condition", "good")
            if cond in conditions:
                conditions[cond] += 1
        
        for cond, count in conditions.items():
            st.markdown(f"**{t(cond)}**: {count}")
        
        st.markdown("---")
        st.markdown(f"##### {t('recent_activity')}")
        if reports:
            for report in reports[:3]:
                st.markdown(f"- {report.get('description', 'Report')[:40]}...")

# ============== Route Planning ==============
elif menu == "route_planning":
    st.title(t("route_planning"))
    st.markdown(f"##### {t('plan_route')}")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"**{t('origin')}**")
        origin_lat = st.number_input(t("latitude"), value=41.9028, key="origin_lat", format="%.6f")
        origin_lon = st.number_input(t("longitude"), value=12.4964, key="origin_lon", format="%.6f")
    
    with col2:
        st.markdown(f"**{t('destination')}**")
        dest_lat = st.number_input(t("latitude"), value=41.9100, key="dest_lat", format="%.6f")
        dest_lon = st.number_input(t("longitude"), value=12.5000, key="dest_lon", format="%.6f")
    
    if st.button(t("find_routes"), type="primary"):
        payload = {
            "origin": {"lat": origin_lat, "lon": origin_lon},
            "destination": {"lat": dest_lat, "lon": dest_lon}
        }
        routes = api_post("/api/path/search", json_data=payload)
        
        if routes:
            st.success(f"{t('route_results')}: {len(routes)} {t('routes_found')}")
            
            m = folium.Map(location=[origin_lat, origin_lon], zoom_start=14)
            
            folium.Marker([origin_lat, origin_lon], popup=t("origin"), 
                         icon=folium.Icon(color="green")).add_to(m)
            folium.Marker([dest_lat, dest_lon], popup=t("destination"),
                         icon=folium.Icon(color="red")).add_to(m)
            
            colors = ["#1a73e8", "#34a853", "#fbbc04"]
            for i, route in enumerate(routes[:3]):
                if "path" in route:
                    coords = [[p["lat"], p["lon"]] for p in route["path"] if "lat" in p and "lon" in p]
                    if coords:
                        folium.PolyLine(coords, color=colors[i % 3], weight=4).add_to(m)
            
            st_folium(m, width=None, height=400, returned_objects=[])
        else:
            st.warning(t("no_routes_found"))

# ============== Segments ==============
elif menu == "segments":
    st.title(t("segments"))
    
    segments = api_get("/api/segments", {"user_id": user_id})
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown(f"##### {t('road_segments')}")
        
        if segments:
            m = folium.Map(location=[41.9028, 12.4964], zoom_start=12)
            
            for seg in segments:
                start_lat, start_lon, end_lat, end_lon = get_seg_coords(seg)
                if start_lat and start_lon:
                    condition = seg.get("condition", "unknown")
                    colors = {"good": "#34a853", "moderate": "#fbbc04", "poor": "#ea4335", "critical": "#9c27b0"}
                    
                    folium.PolyLine(
                        locations=[[start_lat, start_lon], [end_lat, end_lon]],
                        color=colors.get(condition, "#1a73e8"),
                        weight=4,
                        popup=f"{get_seg_name(seg)} - {condition}"
                    ).add_to(m)
            
            st_folium(m, width=None, height=400, returned_objects=[])
        else:
            st.info(t("no_segments"))
    
    with col2:
        st.markdown(f"##### {t('add_segment')}")
        
        with st.form("add_segment_form"):
            seg_name = st.text_input(t("segment_name"))
            st.markdown(f"**{t('start_point')}**")
            start_lat = st.number_input(t("latitude"), value=41.9028, key="seg_start_lat", format="%.6f")
            start_lon = st.number_input(t("longitude"), value=12.4964, key="seg_start_lon", format="%.6f")
            st.markdown(f"**{t('end_point')}**")
            end_lat = st.number_input(t("latitude"), value=41.9050, key="seg_end_lat", format="%.6f")
            end_lon = st.number_input(t("longitude"), value=12.5000, key="seg_end_lon", format="%.6f")
            
            if st.form_submit_button(t("create_segment"), type="primary"):
                result = api_post("/api/segments", {
                    "user_id": user_id,
                    "road_name": seg_name,
                    "start_lat": start_lat,
                    "start_lon": start_lon,
                    "end_lat": end_lat,
                    "end_lon": end_lon
                })
                if result:
                    st.success(t("segment_created"))
                    st.rerun()
        
        st.markdown("---")
        st.markdown(f"##### {t('segment_details')}")
        if segments:
            for seg in segments[:5]:
                with st.expander(get_seg_name(seg)):
                    st.markdown(f"**ID**: {seg.get('id')}")
                    st.markdown(f"**{t('condition')}**: {seg.get('condition', 'N/A')}")

# ============== Reports ==============
elif menu == "reports":
    st.title(t("reports"))
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown(f"##### {t('submit_report')}")
        
        segments = api_get("/api/segments", {"user_id": user_id}) or []
        
        with st.form("submit_report_form"):
            if segments:
                segment_options = {s["id"]: get_seg_name(s) for s in segments}
                segment_id = st.selectbox(
                    t("select_segment"),
                    options=list(segment_options.keys()),
                    format_func=lambda x: segment_options[x]
                )
            else:
                st.info(t("no_segments"))
                segment_id = None
            
            report_types = {
                "pothole": t("pothole"),
                "crack": t("crack"),
                "flooding": t("flooding"),
                "debris": t("debris"),
                "other": t("other")
            }
            report_type = st.selectbox(
                t("report_type"),
                options=list(report_types.keys()),
                format_func=lambda x: report_types[x]
            )
            
            severity_options = {
                "low": t("low"),
                "medium": t("medium"),
                "high": t("high")
            }
            severity = st.selectbox(
                t("severity"),
                options=list(severity_options.keys()),
                format_func=lambda x: severity_options[x]
            )
            
            description = st.text_area(t("description"))
            
            if st.form_submit_button(t("submit"), type="primary"):
                if segment_id:
                    result = api_post("/api/reports", {
                        "user_id": user_id,
                        "segment_id": segment_id,
                        "report_type": report_type,
                        "severity": severity,
                        "description": description
                    })
                    if result:
                        st.success(t("report_submitted"))
                        st.rerun()
    
    with col2:
        st.markdown(f"##### {t('existing_reports')}")
        reports = api_get("/api/reports", {"user_id": user_id})
        
        if reports:
            for report in reports:
                with st.expander(f"{report.get('report_type', 'Report')} - {report.get('severity', '')}"):
                    st.markdown(f"**{t('description')}**: {report.get('description', 'N/A')}")
                    st.markdown(f"**{t('status')}**: {report.get('status', 'pending')}")
        else:
            st.info(t("no_reports"))

# ============== Trips ==============
elif menu == "trips":
    st.title(t("trips"))
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown(f"##### {t('start_trip')}")
        
        segments = api_get("/api/segments", {"user_id": user_id}) or []
        
        if segments:
            segment_options = {s["id"]: get_seg_name(s) for s in segments}
            selected_segment = st.selectbox(
                t("select_segment"),
                options=list(segment_options.keys()),
                format_func=lambda x: segment_options[x],
                key="trip_segment"
            )
            
            if st.button(t("start_trip"), type="primary"):
                result = api_post("/api/trips", {
                    "user_id": user_id,
                    "segment_id": selected_segment
                })
                if result:
                    st.success(t("trip_started"))
                    st.rerun()
    
    with col2:
        st.markdown(f"##### {t('trip_history')}")
        trips = api_get("/api/trips", {"user_id": user_id})
        
        if trips:
            for trip in trips:
                with st.expander(f"Trip #{trip.get('id')} - {trip.get('status', 'unknown')}"):
                    st.markdown(f"**{t('start_time')}**: {trip.get('start_time', 'N/A')}")
                    st.markdown(f"**{t('end_time')}**: {trip.get('end_time', 'N/A')}")
                    st.markdown(f"**{t('status')}**: {trip.get('status', 'N/A')}")
                    
                    if trip.get("status") == "in_progress":
                        if st.button(t("end_trip"), key=f"end_trip_{trip['id']}"):
                            api_post(f"/api/trips/{trip['id']}/end")
                            st.success(t("trip_ended"))
                            st.rerun()
        else:
            st.info(t("no_trips"))

# ============== Auto Detection ==============
elif menu == "auto_detection":
    st.title(t("auto_detection"))
    
    # Real GPS Location via JavaScript
    st.markdown(f"##### {t('location')}")
    
    # Initialize location in session state
    if "gps_lat" not in st.session_state:
        st.session_state.gps_lat = 41.9028
    if "gps_lon" not in st.session_state:
        st.session_state.gps_lon = 12.4964
    if "gps_speed" not in st.session_state:
        st.session_state.gps_speed = 0.0
    
    # JavaScript for getting real GPS location and speed
    st.components.v1.html("""
    <div id="gps-status" style="padding: 16px; background: #f8f9fa; border-radius: 8px; margin-bottom: 16px; font-family: 'Inter', sans-serif;">
        <div style="display: flex; align-items: center; margin-bottom: 12px;">
            <span id="status-icon" style="font-size: 24px; margin-right: 12px;">📍</span>
            <div>
                <div id="status-text" style="font-weight: 600;">Requesting location...</div>
                <div id="status-sub" style="font-size: 13px; color: #666;">Please allow location access</div>
            </div>
        </div>
        <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; margin-top: 12px;">
            <div style="background: white; padding: 12px; border-radius: 6px; text-align: center;">
                <div style="font-size: 12px; color: #666;">Latitude</div>
                <div id="lat-value" style="font-size: 16px; font-weight: 600;">--</div>
            </div>
            <div style="background: white; padding: 12px; border-radius: 6px; text-align: center;">
                <div style="font-size: 12px; color: #666;">Longitude</div>
                <div id="lon-value" style="font-size: 16px; font-weight: 600;">--</div>
            </div>
            <div style="background: white; padding: 12px; border-radius: 6px; text-align: center;">
                <div style="font-size: 12px; color: #666;">Speed (km/h)</div>
                <div id="speed-value" style="font-size: 16px; font-weight: 600; color: #1a73e8;">--</div>
            </div>
        </div>
    </div>
    <script>
        let watchId = null;
        const statusIcon = document.getElementById('status-icon');
        const statusText = document.getElementById('status-text');
        const statusSub = document.getElementById('status-sub');
        const latValue = document.getElementById('lat-value');
        const lonValue = document.getElementById('lon-value');
        const speedValue = document.getElementById('speed-value');
        
        if ("geolocation" in navigator) {
            watchId = navigator.geolocation.watchPosition(
                function(position) {
                    const lat = position.coords.latitude;
                    const lon = position.coords.longitude;
                    const speed = position.coords.speed;
                    const speedKmh = speed ? (speed * 3.6).toFixed(1) : '0.0';
                    
                    statusIcon.textContent = '✅';
                    statusText.textContent = 'Location acquired';
                    statusSub.textContent = 'GPS signal active';
                    latValue.textContent = lat.toFixed(6);
                    lonValue.textContent = lon.toFixed(6);
                    speedValue.textContent = speedKmh;
                    
                    // Store in window for Streamlit to access
                    window.gpsData = {lat: lat, lon: lon, speed: parseFloat(speedKmh)};
                },
                function(error) {
                    statusIcon.textContent = '⚠️';
                    statusText.textContent = 'Location unavailable';
                    statusSub.textContent = error.message;
                    latValue.textContent = '41.9028';
                    lonValue.textContent = '12.4964';
                    speedValue.textContent = '0.0';
                },
                {enableHighAccuracy: true, timeout: 10000, maximumAge: 1000}
            );
        } else {
            statusIcon.textContent = '❌';
            statusText.textContent = 'Geolocation not supported';
            statusSub.textContent = 'Using default location';
        }
    </script>
    """, height=180)
    
    st.markdown("---")
    st.markdown(f"##### {t('sensor_simulation')}")
    
    col1, col2 = st.columns(2)
    with col1:
        # Manual speed input as fallback
        speed = st.slider(f"{t('current_speed')} (km/h)", 0, 50, 18, help="Use this if GPS speed is not available")
    with col2:
        severity_options = {
            "Normal": t("normal"),
            "Bump": t("bump"),
            "Pothole": t("pothole"),
            "Severe": t("severe")
        }
        severity = st.selectbox(
            t("simulate_event"),
            options=list(severity_options.keys()),
            format_func=lambda x: severity_options[x]
        )
    
    severity_multiplier = {"Normal": 1, "Bump": 3, "Pothole": 5, "Severe": 8}
    mult = severity_multiplier.get(severity, 1)
    
    sensor_data = pd.DataFrame(
        np.random.randn(50, 3) * mult,
        columns=['Accel_X', 'Accel_Y', 'Accel_Z']
    )
    
    st.line_chart(sensor_data)
    
    max_accel = float(sensor_data.abs().values.max())
    st.metric(t("peak_acceleration"), f"{max_accel:.1f} m/s²")
    
    if max_accel > 25:
        st.error(t("major_damage"))
    elif max_accel > 15:
        st.warning(t("significant_defect"))
    elif max_accel > 8:
        st.info(t("minor_irregularity"))
    else:
        st.success(t("smooth_surface"))
    
    st.markdown("---")
    st.markdown(f"##### {t('submit_detection')}")
    
    segments = api_get("/api/segments", {"user_id": user_id})
    if segments:
        segment_options = {s["id"]: get_seg_name(s) for s in segments}
        segment_id = st.selectbox(
            t("apply_to_segment"),
            options=list(segment_options.keys()),
            format_func=lambda x: segment_options[x]
        )
        
        if st.button(t("submit_detection"), type="primary"):
            reading = {
                "acceleration_x": float(sensor_data["Accel_X"].iloc[-1]),
                "acceleration_y": float(sensor_data["Accel_Y"].iloc[-1]),
                "acceleration_z": float(sensor_data["Accel_Z"].iloc[-1]),
                "speed_mps": speed / 3.6,
                "gps_accuracy_m": 5.0
            }
            result = api_post(f"/api/segments/{segment_id}/auto-detect", reading)
            if result:
                st.success(t("detection_submitted"))

# ============== Settings ==============
elif menu == "settings":
    st.title(t("settings"))
    
    settings = api_get(f"/api/users/{user_id}/settings")
    if settings:
        st.session_state.language = settings.get("language", "en")
        st.session_state.dark_mode = settings.get("dark_mode", False)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"##### {t('display_settings')}")
        
        dark_mode = st.toggle(t("dark_mode"), value=st.session_state.dark_mode)
        
        st.markdown(f"##### {t('notification_settings')}")
        notifications = st.toggle(t("enable_notifications"), value=settings.get("notifications_enabled", True) if settings else True)
        
        if st.button(t("save_settings"), type="primary", use_container_width=True):
            result = api_patch(f"/api/users/{user_id}/settings", {
                "language": st.session_state.language,
                "dark_mode": dark_mode,
                "notifications_enabled": notifications
            })
            if result:
                st.session_state.dark_mode = dark_mode
                st.success(t("settings_saved"))
                st.rerun()
    
    with col2:
        st.markdown(f"##### {t('user_profile')}")
        
        created_at = user.get('created_at', '')
        if created_at:
            try:
                dt = datetime.fromisoformat(created_at.replace('Z', '+00:00'))
                formatted_date = dt.strftime('%Y-%m-%d')
            except:
                formatted_date = created_at[:10] if len(created_at) >= 10 else created_at
        else:
            formatted_date = 'N/A'
        
        border_color = '#303134' if st.session_state.dark_mode else '#e8eaed'
        st.markdown(f"""
        <div style="padding: 24px; border-radius: 12px; border: 1px solid {border_color};">
            <div style="display: flex; align-items: center; margin-bottom: 20px;">
                <div style="width: 48px; height: 48px; border-radius: 50%; background: linear-gradient(135deg, #1a73e8, #8ab4f8); display: flex; align-items: center; justify-content: center; font-size: 20px; font-weight: 600; color: white; margin-right: 16px;">
                    {user['username'][0].upper()}
                </div>
                <div>
                    <div style="font-size: 18px; font-weight: 600;">{user['username']}</div>
                    <div style="font-size: 13px; opacity: 0.6;">{t('account_status')}: {t('active')}</div>
                </div>
            </div>
            <div style="border-top: 1px solid {border_color}; padding-top: 16px;">
                <div style="display: flex; justify-content: space-between; margin-bottom: 12px;">
                    <span style="opacity: 0.7;">{t('user_id')}</span>
                    <span style="font-weight: 500;">{user['id']}</span>
                </div>
                <div style="display: flex; justify-content: space-between;">
                    <span style="opacity: 0.7;">{t('member_since')}</span>
                    <span style="font-weight: 500;">{formatted_date}</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

# ============== Footer ==============
st.sidebar.markdown("---")
st.sidebar.caption(f"BBP v2.0 | {datetime.now().strftime('%Y')}")
