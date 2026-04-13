"""Seed script — populates exam_packs + exam_subjects with the 16 exam types.

Run standalone:  python -m deeptutor.services.exam.seed
Or called from application startup when tables are empty.
"""

from __future__ import annotations

import asyncio
import logging
import uuid

from sqlalchemy import func, select

from deeptutor.services.exam.db import get_session, init_pg
from deeptutor.services.exam.models import ExamPack, ExamSubject

logger = logging.getLogger("exam.seed")

EXAM_PACKS: list[dict] = [
    # India
    {"country_code": "IN", "country_name": "India", "name": "JEE Main", "tier": 1, "price_display": "₹499/mo", "currency": "INR", "question_count": 2400, "subjects": ["Physics", "Chemistry", "Mathematics"]},
    {"country_code": "IN", "country_name": "India", "name": "JEE Advanced", "tier": 1, "price_display": "₹699/mo", "currency": "INR", "question_count": 1800, "subjects": ["Physics", "Chemistry", "Mathematics"]},
    {"country_code": "IN", "country_name": "India", "name": "NEET UG", "tier": 1, "price_display": "₹499/mo", "currency": "INR", "question_count": 3200, "subjects": ["Physics", "Chemistry", "Biology"]},
    {"country_code": "IN", "country_name": "India", "name": "CBSE 10th", "tier": 2, "price_display": "₹199/mo", "currency": "INR", "question_count": 2000, "subjects": ["Mathematics", "Science", "English", "SST"]},
    {"country_code": "IN", "country_name": "India", "name": "CBSE 12th", "tier": 2, "price_display": "₹299/mo", "currency": "INR", "question_count": 2500, "subjects": ["Physics", "Chemistry", "Mathematics"]},
    {"country_code": "IN", "country_name": "India", "name": "CAT", "tier": 2, "price_display": "₹599/mo", "currency": "INR", "question_count": 1500, "subjects": ["Quant", "VARC", "DILR"]},
    {"country_code": "IN", "country_name": "India", "name": "GATE (CS)", "tier": 2, "price_display": "₹499/mo", "currency": "INR", "question_count": 1800, "subjects": ["DSA", "OS", "DBMS", "Networks"]},
    {"country_code": "IN", "country_name": "India", "name": "UPSC Prelims", "tier": 3, "price_display": "₹799/mo", "currency": "INR", "question_count": 3000, "subjects": ["GS", "CSAT", "Current Affairs"]},
    # USA
    {"country_code": "US", "country_name": "USA", "name": "SAT", "tier": 1, "price_display": "$9.99/mo", "currency": "USD", "question_count": 2000, "subjects": ["Math", "Reading", "Writing"]},
    {"country_code": "US", "country_name": "USA", "name": "ACT", "tier": 1, "price_display": "$9.99/mo", "currency": "USD", "question_count": 1800, "subjects": ["English", "Math", "Reading", "Science"]},
    {"country_code": "US", "country_name": "USA", "name": "AP Calculus AB", "tier": 2, "price_display": "$7.99/mo", "currency": "USD", "question_count": 800, "subjects": ["Limits", "Derivatives", "Integrals"]},
    {"country_code": "US", "country_name": "USA", "name": "AP Physics 1", "tier": 2, "price_display": "$7.99/mo", "currency": "USD", "question_count": 700, "subjects": ["Mechanics", "Waves", "Circuits"]},
    {"country_code": "US", "country_name": "USA", "name": "AP Chemistry", "tier": 2, "price_display": "$7.99/mo", "currency": "USD", "question_count": 750, "subjects": ["Atomic", "Bonding", "Reactions"]},
    {"country_code": "US", "country_name": "USA", "name": "GRE", "tier": 2, "price_display": "$14.99/mo", "currency": "USD", "question_count": 1500, "subjects": ["Quant", "Verbal", "AWA"]},
    {"country_code": "US", "country_name": "USA", "name": "GMAT", "tier": 2, "price_display": "$14.99/mo", "currency": "USD", "question_count": 1200, "subjects": ["Quant", "Verbal", "IR", "AWA"]},
    # China
    {"country_code": "CN", "country_name": "China", "name": "高考 (Gaokao)", "tier": 1, "price_display": "¥39/月", "currency": "CNY", "question_count": 3000, "is_coming_soon": True, "subjects": ["语文", "数学", "英语", "理综/文综"]},
    {"country_code": "CN", "country_name": "China", "name": "中考 (Zhongkao)", "tier": 2, "price_display": "¥29/月", "currency": "CNY", "question_count": 2000, "is_coming_soon": True, "subjects": ["语文", "数学", "英语", "物理", "化学"]},
    # ── Spain (es) ──────────────────────────────────────────────────────────────
    {"country_code": "ES", "country_name": "España", "name": "EBAU / Selectividad", "tier": 1, "price_display": "€7,99/mes", "currency": "EUR", "question_count": 2200, "subjects": ["Matemáticas", "Lengua Castellana", "Inglés", "Historia de España"]},
    # ── Mexico (es-419) ────────────────────────────────────────────────────────
    {"country_code": "MX", "country_name": "México", "name": "EXANI-II (CENEVAL)", "tier": 1, "price_display": "$149/mes", "currency": "MXN", "question_count": 1800, "subjects": ["Matemáticas", "Pensamiento Analítico", "Español", "Inglés"]},
    {"country_code": "MX", "country_name": "México", "name": "COMIPEMS", "tier": 2, "price_display": "$99/mes", "currency": "MXN", "question_count": 1500, "subjects": ["Matemáticas", "Español", "Ciencias Naturales", "Historia"]},
    # ── Colombia (es-419) ──────────────────────────────────────────────────────
    {"country_code": "CO", "country_name": "Colombia", "name": "Saber 11 (ICFES)", "tier": 1, "price_display": "$29.900/mes", "currency": "COP", "question_count": 2000, "subjects": ["Matemáticas", "Lectura Crítica", "Ciencias Naturales", "Sociales y Ciudadanas", "Inglés"]},
    # ── Egypt (ar) ─────────────────────────────────────────────────────────────
    {"country_code": "EG", "country_name": "مصر", "name": "الثانوية العامة (Thanawiya Amma)", "tier": 1, "price_display": "99 ج.م/شهر", "currency": "EGP", "question_count": 2500, "subjects": ["الرياضيات", "الفيزياء", "الكيمياء", "اللغة العربية", "اللغة الإنجليزية"]},
    # ── Saudi Arabia (ar) ──────────────────────────────────────────────────────
    {"country_code": "SA", "country_name": "السعودية", "name": "اختبار القدرات (Qudurat)", "tier": 1, "price_display": "39 ر.س/شهر", "currency": "SAR", "question_count": 1800, "subjects": ["الكمي", "اللفظي"]},
    {"country_code": "SA", "country_name": "السعودية", "name": "اختبار التحصيلي (Tahsili)", "tier": 1, "price_display": "39 ر.س/شهر", "currency": "SAR", "question_count": 2000, "subjects": ["الرياضيات", "الفيزياء", "الكيمياء", "الأحياء"]},
    # ── UAE (ar) ────────────────────────────────────────────────────────────────
    {"country_code": "AE", "country_name": "الإمارات", "name": "EmSAT", "tier": 2, "price_display": "29 د.إ/شهر", "currency": "AED", "question_count": 1500, "subjects": ["Mathematics", "English", "Arabic", "Physics"]},
    # ── France (fr) ────────────────────────────────────────────────────────────
    {"country_code": "FR", "country_name": "France", "name": "Baccalauréat", "tier": 1, "price_display": "€7,99/mois", "currency": "EUR", "question_count": 2500, "subjects": ["Mathématiques", "Physique-Chimie", "Français", "Philosophie", "Histoire-Géographie"]},
    {"country_code": "FR", "country_name": "France", "name": "Brevet des collèges", "tier": 2, "price_display": "€4,99/mois", "currency": "EUR", "question_count": 1500, "subjects": ["Mathématiques", "Français", "Sciences", "Histoire-Géographie"]},
    # ── Germany (de) ───────────────────────────────────────────────────────────
    {"country_code": "DE", "country_name": "Deutschland", "name": "Abitur", "tier": 1, "price_display": "€7,99/Monat", "currency": "EUR", "question_count": 2000, "subjects": ["Mathematik", "Physik", "Deutsch", "Englisch", "Geschichte"]},
    {"country_code": "DE", "country_name": "Deutschland", "name": "Mittlere Reife (Realschulabschluss)", "tier": 2, "price_display": "€4,99/Monat", "currency": "EUR", "question_count": 1200, "subjects": ["Mathematik", "Deutsch", "Englisch", "Naturwissenschaften"]},
    # ── Indonesia (id) ─────────────────────────────────────────────────────────
    {"country_code": "ID", "country_name": "Indonesia", "name": "UTBK-SNBT", "tier": 1, "price_display": "Rp49.000/bln", "currency": "IDR", "question_count": 2000, "subjects": ["Penalaran Umum", "Pengetahuan Kuantitatif", "Literasi Bahasa Indonesia", "Literasi Bahasa Inggris"]},
    {"country_code": "ID", "country_name": "Indonesia", "name": "AKM (Asesmen Kompetensi Minimum)", "tier": 2, "price_display": "Rp29.000/bln", "currency": "IDR", "question_count": 1200, "subjects": ["Literasi Membaca", "Numerasi"]},
    # ── Japan (ja) ─────────────────────────────────────────────────────────────
    {"country_code": "JP", "country_name": "日本", "name": "共通テスト (Kyōtsū Test)", "tier": 1, "price_display": "¥980/月", "currency": "JPY", "question_count": 2200, "subjects": ["数学", "英語", "国語", "理科", "社会"]},
    {"country_code": "JP", "country_name": "日本", "name": "高校入試 (Kōkō Nyūshi)", "tier": 2, "price_display": "¥680/月", "currency": "JPY", "question_count": 1500, "subjects": ["数学", "英語", "国語", "理科", "社会"]},
    # ── South Korea (ko) ───────────────────────────────────────────────────────
    {"country_code": "KR", "country_name": "대한민국", "name": "수능 (CSAT / Suneung)", "tier": 1, "price_display": "₩9,900/월", "currency": "KRW", "question_count": 2500, "subjects": ["국어", "수학", "영어", "탐구", "한국사"]},
    # ── Brazil (pt) ────────────────────────────────────────────────────────────
    {"country_code": "BR", "country_name": "Brasil", "name": "ENEM", "tier": 1, "price_display": "R$19,90/mês", "currency": "BRL", "question_count": 2800, "subjects": ["Matemática", "Ciências da Natureza", "Linguagens", "Ciências Humanas", "Redação"]},
    {"country_code": "BR", "country_name": "Brasil", "name": "Vestibular (FUVEST/UNICAMP)", "tier": 2, "price_display": "R$14,90/mês", "currency": "BRL", "question_count": 1500, "subjects": ["Matemática", "Física", "Química", "Biologia", "Português"]},
    # ── Portugal (pt) ──────────────────────────────────────────────────────────
    {"country_code": "PT", "country_name": "Portugal", "name": "Exames Nacionais", "tier": 2, "price_display": "€5,99/mês", "currency": "EUR", "question_count": 1200, "subjects": ["Matemática A", "Português", "Física e Química A", "Biologia e Geologia"]},
    # ── Russia (ru) ────────────────────────────────────────────────────────────
    {"country_code": "RU", "country_name": "Россия", "name": "ЕГЭ (Единый государственный экзамен)", "tier": 1, "price_display": "₽499/мес", "currency": "RUB", "question_count": 2500, "subjects": ["Математика", "Русский язык", "Физика", "Информатика", "Обществознание"]},
    {"country_code": "RU", "country_name": "Россия", "name": "ОГЭ (Основной государственный экзамен)", "tier": 2, "price_display": "₽299/мес", "currency": "RUB", "question_count": 1800, "subjects": ["Математика", "Русский язык", "Предмет по выбору"]},
]


# ---------------------------------------------------------------------------
# Exam format / syllabus / scoring metadata
# Keyed by exam name — merged into ExamPack.metadata_ at seed time.
# ---------------------------------------------------------------------------
EXAM_METADATA: dict[str, dict] = {
    # ── India ──────────────────────────────────────────────────────────────────
    "JEE Main": {
        "format": {
            "duration_minutes": 180,
            "total_marks": 300,
            "sections": ["Physics (25 MCQ + 5 Numerical)", "Chemistry (25 MCQ + 5 Numerical)", "Mathematics (25 MCQ + 5 Numerical)"],
            "question_types": ["MCQ (4 options)", "Numerical Value"],
            "negative_marking": True,
            "negative_scheme": "-1 for wrong MCQ, no penalty for numerical",
            "calculator_allowed": False,
            "language": ["English", "Hindi", "Gujarati", "Bengali", "Tamil", "Telugu", "Marathi", "Urdu", "Assamese", "Kannada", "Odia", "Punjabi", "Malayalam"],
        },
        "syllabus": {
            "key_topics": ["Mechanics", "Electrodynamics", "Modern Physics", "Organic Chemistry", "Inorganic Chemistry", "Physical Chemistry", "Calculus", "Algebra", "Coordinate Geometry", "Trigonometry"],
            "official_board": "National Testing Agency (NTA)",
            "syllabus_url": "https://jeemain.nta.nic.in",
        },
        "scoring": {"max_score": 300, "passing_score": None, "grading_method": "Percentile-based ranking", "total_candidates": 1_200_000},
        "schedule": {"frequency": "2 sessions/year (Jan & Apr)", "typical_months": ["January", "April"]},
        "eligibility": "Class 12 pass or appearing, no age limit",
    },
    "JEE Advanced": {
        "format": {
            "duration_minutes": 360,
            "total_marks": 360,
            "sections": ["Paper 1 – Physics, Chemistry, Maths (3 hrs)", "Paper 2 – Physics, Chemistry, Maths (3 hrs)"],
            "question_types": ["MCQ single correct", "MCQ multiple correct", "Numerical value", "Matching", "Paragraph-based"],
            "negative_marking": True,
            "negative_scheme": "Varies by question type: -1 for single MCQ, -2 for multi-correct partial",
            "calculator_allowed": False,
            "language": ["English", "Hindi"],
        },
        "syllabus": {
            "key_topics": ["Advanced Calculus", "Mechanics", "Thermodynamics", "Optics", "Electrochemistry", "Organic Synthesis", "Matrices", "Complex Numbers", "Probability"],
            "official_board": "IIT conducting body (rotates annually)",
            "syllabus_url": "https://jeeadv.ac.in",
        },
        "scoring": {"max_score": 360, "passing_score": None, "grading_method": "Aggregate marks → All India Rank", "total_candidates": 250_000},
        "schedule": {"frequency": "Once/year", "typical_months": ["May", "June"]},
        "eligibility": "Top 2,50,000 in JEE Main, max 2 attempts",
    },
    "NEET UG": {
        "format": {
            "duration_minutes": 200,
            "total_marks": 720,
            "sections": ["Physics (35 + 15 MCQ)", "Chemistry (35 + 15 MCQ)", "Biology: Botany (35 + 15 MCQ)", "Biology: Zoology (35 + 15 MCQ)"],
            "question_types": ["MCQ (4 options)"],
            "negative_marking": True,
            "negative_scheme": "+4 correct, -1 wrong",
            "calculator_allowed": False,
            "language": ["English", "Hindi", "Urdu", "Bengali", "Tamil", "Telugu", "Marathi", "Gujarati", "Assamese", "Kannada", "Odia", "Punjabi", "Malayalam"],
        },
        "syllabus": {
            "key_topics": ["Human Physiology", "Genetics", "Ecology", "Organic Chemistry", "Mechanics", "Optics", "Thermodynamics", "Cell Biology", "Plant Physiology"],
            "official_board": "National Testing Agency (NTA)",
            "syllabus_url": "https://neet.nta.nic.in",
        },
        "scoring": {"max_score": 720, "passing_score": None, "grading_method": "NEET Score → AIR → Counselling cutoffs", "total_candidates": 2_400_000},
        "schedule": {"frequency": "Once/year", "typical_months": ["May"]},
        "eligibility": "Class 12 with PCB, minimum 50% aggregate (General), age 17+",
    },
    "CBSE 10th": {
        "format": {
            "duration_minutes": 180,
            "total_marks": 80,
            "sections": ["Section A (MCQ)", "Section B (Short Answer)", "Section C (Long Answer)", "Section D (Case-based)"],
            "question_types": ["MCQ", "Short answer (2–3 marks)", "Long answer (5 marks)", "Case-based (4 marks)"],
            "negative_marking": False,
            "calculator_allowed": False,
            "language": ["English", "Hindi"],
        },
        "syllabus": {
            "key_topics": ["Real Numbers", "Polynomials", "Linear Equations", "Quadratic Equations", "Triangles", "Coordinate Geometry", "Chemical Reactions", "Acids & Bases", "Life Processes", "Electricity"],
            "official_board": "CBSE (Central Board of Secondary Education)",
        },
        "scoring": {"max_score": 80, "passing_score": 33, "grading_method": "Internal (20) + Board (80) = 100 per subject", "total_candidates": 3_800_000},
        "schedule": {"frequency": "Once/year", "typical_months": ["February", "March"]},
        "eligibility": "CBSE Class 10 students",
    },
    "CBSE 12th": {
        "format": {
            "duration_minutes": 180,
            "total_marks": 70,
            "sections": ["Section A (MCQ)", "Section B (Short Answer)", "Section C (Long Answer)", "Section D (Case-based)", "Section E (Competency)"],
            "question_types": ["MCQ", "Short answer (2–3 marks)", "Long answer (5 marks)", "Case/competency-based"],
            "negative_marking": False,
            "calculator_allowed": False,
            "language": ["English", "Hindi"],
        },
        "syllabus": {
            "key_topics": ["Electrostatics", "Current Electricity", "Optics", "Modern Physics", "Solid State", "Solutions", "Electrochemistry", "Chemical Kinetics", "Relations & Functions", "Calculus", "Vectors", "Probability"],
            "official_board": "CBSE",
        },
        "scoring": {"max_score": 70, "passing_score": 23, "grading_method": "Internal (30) + Board (70) = 100", "total_candidates": 3_500_000},
        "schedule": {"frequency": "Once/year", "typical_months": ["February", "March"]},
        "eligibility": "CBSE Class 12 students",
    },
    "CAT": {
        "format": {
            "duration_minutes": 120,
            "total_marks": 198,
            "sections": ["VARC (24 Qs, 40 min)", "DILR (20 Qs, 40 min)", "QA (22 Qs, 40 min)"],
            "question_types": ["MCQ", "Non-MCQ (TITA – Type In The Answer)"],
            "negative_marking": True,
            "negative_scheme": "-1 for wrong MCQ, no penalty for TITA",
            "calculator_allowed": True,
            "language": ["English"],
        },
        "syllabus": {
            "key_topics": ["Reading Comprehension", "Para Jumbles", "Data Interpretation", "Logical Reasoning", "Arithmetic", "Algebra", "Geometry", "Number Systems"],
            "official_board": "IIM (rotates annually)",
        },
        "scoring": {"max_score": 198, "passing_score": None, "grading_method": "Scaled score → Percentile", "total_candidates": 300_000},
        "schedule": {"frequency": "Once/year", "typical_months": ["November"]},
        "eligibility": "Bachelor's degree with 50% (45% for SC/ST)",
    },
    "GATE (CS)": {
        "format": {
            "duration_minutes": 180,
            "total_marks": 100,
            "sections": ["General Aptitude (15 marks)", "Engineering Mathematics (13 marks)", "Core CS (72 marks)"],
            "question_types": ["MCQ", "MSQ (Multiple Select)", "NAT (Numerical Answer)"],
            "negative_marking": True,
            "negative_scheme": "-1/3 for 1-mark MCQ, -2/3 for 2-mark MCQ; no penalty for MSQ/NAT",
            "calculator_allowed": True,
            "language": ["English"],
        },
        "syllabus": {
            "key_topics": ["Data Structures", "Algorithms", "Operating Systems", "DBMS", "Computer Networks", "Theory of Computation", "Compiler Design", "Digital Logic", "Computer Organization"],
            "official_board": "IIT (rotates)",
            "syllabus_url": "https://gate.iitk.ac.in",
        },
        "scoring": {"max_score": 100, "passing_score": None, "grading_method": "Normalized marks → GATE Score", "total_candidates": 100_000},
        "schedule": {"frequency": "Once/year", "typical_months": ["February"]},
        "eligibility": "B.E./B.Tech or equivalent (final year eligible)",
    },
    "UPSC Prelims": {
        "format": {
            "duration_minutes": 240,
            "total_marks": 400,
            "sections": ["Paper I – General Studies (100 Qs, 2 hrs)", "Paper II – CSAT (80 Qs, 2 hrs)"],
            "question_types": ["MCQ (4 options)"],
            "negative_marking": True,
            "negative_scheme": "-1/3 of assigned marks for wrong answer",
            "calculator_allowed": False,
            "language": ["English", "Hindi"],
        },
        "syllabus": {
            "key_topics": ["Indian Polity", "Geography", "History", "Economy", "Environment", "Science & Tech", "Current Affairs", "Comprehension", "Logical Reasoning", "Basic Numeracy"],
            "official_board": "Union Public Service Commission (UPSC)",
            "syllabus_url": "https://upsc.gov.in",
        },
        "scoring": {"max_score": 400, "passing_score": None, "grading_method": "Only Paper I counts for merit; Paper II qualifying (33%)", "total_candidates": 1_100_000},
        "schedule": {"frequency": "Once/year", "typical_months": ["May", "June"]},
        "eligibility": "Indian citizen, age 21–32, Bachelor's degree",
    },
    # ── USA ─────────────────────────────────────────────────────────────────────
    "SAT": {
        "format": {
            "duration_minutes": 134,
            "total_marks": 1600,
            "sections": ["Reading & Writing Module 1 (32 min, 27 Qs)", "Reading & Writing Module 2 (32 min, 27 Qs)", "Math Module 1 (35 min, 22 Qs)", "Math Module 2 (35 min, 22 Qs)"],
            "question_types": ["MCQ (4 options)", "Student-Produced Response (grid-in)"],
            "negative_marking": False,
            "calculator_allowed": True,
            "language": ["English"],
        },
        "syllabus": {
            "key_topics": ["Algebra", "Advanced Math", "Problem Solving & Data Analysis", "Geometry & Trigonometry", "Reading Comprehension", "Standard English Conventions", "Expression of Ideas"],
            "official_board": "College Board",
            "syllabus_url": "https://satsuite.collegeboard.org",
        },
        "scoring": {"max_score": 1600, "passing_score": None, "grading_method": "200–800 per section (EBRW + Math)", "total_candidates": 2_200_000},
        "schedule": {"frequency": "7 times/year", "typical_months": ["March", "May", "June", "August", "October", "November", "December"]},
        "eligibility": "High school students (typically Juniors/Seniors), no age limit",
    },
    "ACT": {
        "format": {
            "duration_minutes": 175,
            "total_marks": 36,
            "sections": ["English (75 Qs, 45 min)", "Math (60 Qs, 60 min)", "Reading (40 Qs, 35 min)", "Science (40 Qs, 35 min)", "Writing (optional, 40 min)"],
            "question_types": ["MCQ (4 options for English/Reading/Science, 5 for Math)"],
            "negative_marking": False,
            "calculator_allowed": True,
            "language": ["English"],
        },
        "syllabus": {
            "key_topics": ["Grammar & Usage", "Pre-Algebra through Trigonometry", "Reading Comprehension", "Scientific Reasoning", "Data Interpretation"],
            "official_board": "ACT Inc.",
            "syllabus_url": "https://www.act.org",
        },
        "scoring": {"max_score": 36, "passing_score": None, "grading_method": "Composite = average of 4 section scores (1–36)", "total_candidates": 1_400_000},
        "schedule": {"frequency": "7 times/year", "typical_months": ["February", "April", "June", "July", "September", "October", "December"]},
        "eligibility": "High school students, no age limit",
    },
    "AP Calculus AB": {
        "format": {
            "duration_minutes": 195,
            "total_marks": 108,
            "sections": ["Section I: MCQ Part A (30 Qs, 60 min, no calc)", "Section I: MCQ Part B (15 Qs, 45 min, calc allowed)", "Section II: FRQ Part A (2 Qs, 30 min, calc)", "Section II: FRQ Part B (4 Qs, 60 min, no calc)"],
            "question_types": ["MCQ (5 options)", "Free Response (show work)"],
            "negative_marking": False,
            "calculator_allowed": True,
            "language": ["English"],
        },
        "syllabus": {
            "key_topics": ["Limits & Continuity", "Differentiation", "Applications of Derivatives", "Integration", "Applications of Integrals", "Differential Equations"],
            "official_board": "College Board / AP Program",
        },
        "scoring": {"max_score": 5, "passing_score": 3, "grading_method": "Raw score → 1–5 scale (3+ for college credit)", "total_candidates": 140000},
        "schedule": {"frequency": "Once/year", "typical_months": ["May"]},
        "eligibility": "Enrolled in AP course or self-study, no restrictions",
    },
    "AP Physics 1": {
        "format": {
            "duration_minutes": 180,
            "total_marks": None,
            "sections": ["Section I: MCQ (40 Qs, 90 min)", "Section II: FRQ (5 Qs, 90 min)"],
            "question_types": ["MCQ (4 options)", "Free Response (conceptual + quantitative)"],
            "negative_marking": False,
            "calculator_allowed": True,
            "language": ["English"],
        },
        "syllabus": {
            "key_topics": ["Kinematics", "Newton's Laws", "Work & Energy", "Momentum", "Rotation", "Simple Harmonic Motion", "Waves & Sound"],
            "official_board": "College Board / AP Program",
        },
        "scoring": {"max_score": 5, "passing_score": 3, "grading_method": "Raw score → 1–5 scale", "total_candidates": 170000},
        "schedule": {"frequency": "Once/year", "typical_months": ["May"]},
        "eligibility": "Enrolled in AP course or self-study",
    },
    "AP Chemistry": {
        "format": {
            "duration_minutes": 195,
            "total_marks": None,
            "sections": ["Section I: MCQ (60 Qs, 90 min)", "Section II: FRQ (7 Qs, 105 min)"],
            "question_types": ["MCQ (4 options)", "Free Response (calculations, lab design, conceptual)"],
            "negative_marking": False,
            "calculator_allowed": True,
            "language": ["English"],
        },
        "syllabus": {
            "key_topics": ["Atomic Structure", "Chemical Bonding", "Intermolecular Forces", "Chemical Reactions", "Kinetics", "Thermodynamics", "Equilibrium", "Acids & Bases", "Electrochemistry"],
            "official_board": "College Board / AP Program",
        },
        "scoring": {"max_score": 5, "passing_score": 3, "grading_method": "Raw score → 1–5 scale", "total_candidates": 160000},
        "schedule": {"frequency": "Once/year", "typical_months": ["May"]},
        "eligibility": "Enrolled in AP course or self-study",
    },
    "GRE": {
        "format": {
            "duration_minutes": 118,
            "total_marks": 340,
            "sections": ["Verbal Reasoning (2 sections, 27 Qs, 41 min)", "Quantitative Reasoning (2 sections, 27 Qs, 47 min)", "Analytical Writing (1 essay, 30 min)"],
            "question_types": ["MCQ", "Multiple-select", "Numeric entry", "Text completion", "Sentence equivalence", "Essay"],
            "negative_marking": False,
            "calculator_allowed": True,
            "language": ["English"],
        },
        "syllabus": {
            "key_topics": ["Vocabulary", "Reading Comprehension", "Text Completion", "Arithmetic", "Algebra", "Geometry", "Data Analysis", "Analytical Writing"],
            "official_board": "ETS (Educational Testing Service)",
            "syllabus_url": "https://www.ets.org/gre",
        },
        "scoring": {"max_score": 340, "passing_score": None, "grading_method": "130–170 per section (Verbal + Quant); AWA 0–6", "total_candidates": 340000},
        "schedule": {"frequency": "Year-round (computer-based)", "typical_months": ["Any"]},
        "eligibility": "No restrictions; intended for graduate school applicants",
    },
    "GMAT": {
        "format": {
            "duration_minutes": 135,
            "total_marks": 805,
            "sections": ["Quantitative (21 Qs, 45 min)", "Verbal (23 Qs, 45 min)", "Data Insights (20 Qs, 45 min)"],
            "question_types": ["MCQ", "Data Sufficiency", "Multi-Source Reasoning", "Graphics Interpretation", "Two-Part Analysis"],
            "negative_marking": False,
            "calculator_allowed": False,
            "language": ["English"],
        },
        "syllabus": {
            "key_topics": ["Problem Solving", "Data Sufficiency", "Critical Reasoning", "Sentence Correction", "Reading Comprehension", "Multi-Source Reasoning", "Graph Interpretation"],
            "official_board": "GMAC (Graduate Management Admission Council)",
            "syllabus_url": "https://www.mba.com/gmat",
        },
        "scoring": {"max_score": 805, "passing_score": None, "grading_method": "205–805 total (Focus Edition)", "total_candidates": 200000},
        "schedule": {"frequency": "Year-round", "typical_months": ["Any"]},
        "eligibility": "No age restriction; intended for MBA/business school",
    },
    # ── China ───────────────────────────────────────────────────────────────────
    "高考 (Gaokao)": {
        "format": {
            "duration_minutes": 570,
            "total_marks": 750,
            "sections": ["语文 Chinese (150 pts, 150 min)", "数学 Math (150 pts, 120 min)", "外语 Foreign Language (150 pts, 120 min)", "综合 Comprehensive (300 pts, 150 min)"],
            "question_types": ["MCQ", "Fill-in-the-blank", "Essay", "Proof/Calculation", "Reading comprehension"],
            "negative_marking": False,
            "calculator_allowed": False,
            "language": ["中文 (Chinese)"],
        },
        "syllabus": {
            "key_topics": ["古文/现代文 Classical & Modern Chinese", "函数/微积分 Functions & Calculus", "解析几何 Analytic Geometry", "力学/电学 Mechanics & Electrodynamics", "有机化学 Organic Chemistry", "遗传学 Genetics"],
            "official_board": "教育部 (Ministry of Education, PRC)",
        },
        "scoring": {"max_score": 750, "passing_score": None, "grading_method": "Total score → province-level rank → university admission", "total_candidates": 12900000},
        "schedule": {"frequency": "Once/year", "typical_months": ["June"]},
        "eligibility": "High school graduates or equivalent",
    },
    "中考 (Zhongkao)": {
        "format": {
            "duration_minutes": 480,
            "total_marks": 660,
            "sections": ["语文 (120 min)", "数学 (100 min)", "英语 (100 min)", "物理 (80 min)", "化学 (80 min)"],
            "question_types": ["MCQ", "Fill-in-the-blank", "Short answer", "Calculation", "Essay"],
            "negative_marking": False,
            "calculator_allowed": False,
            "language": ["中文 (Chinese)"],
        },
        "syllabus": {
            "key_topics": ["初中数学 Junior Math", "初中物理 Junior Physics", "初中化学 Junior Chemistry", "语文阅读写作 Chinese Reading & Writing", "英语听力阅读 English Listening & Reading"],
            "official_board": "地方教育局 (Local Education Bureaus)",
        },
        "scoring": {"max_score": 660, "passing_score": None, "grading_method": "Varies by city; total score → high school admission", "total_candidates": 15000000},
        "schedule": {"frequency": "Once/year", "typical_months": ["June"]},
        "eligibility": "Grade 9 students",
    },
    # ── Spain (es) ──────────────────────────────────────────────────────────────
    "EBAU / Selectividad": {
        "format": {
            "duration_minutes": 270,
            "total_marks": 14,
            "sections": ["Fase Obligatoria: Lengua Castellana, Historia de España, Inglés, Materia troncal", "Fase Voluntaria: hasta 4 asignaturas adicionales"],
            "question_types": ["Desarrollo (essay)", "Problemas (calculation)", "Análisis de texto", "Preguntas cortas"],
            "negative_marking": False,
            "calculator_allowed": True,
            "language": ["Español", "co-official languages (Catalán, Euskera, Gallego, Valenciano)"],
        },
        "syllabus": {
            "key_topics": ["Análisis Matemático", "Álgebra Lineal", "Sintaxis y Comentario de Texto", "Historia Contemporánea de España", "Reacciones Químicas", "Mecánica"],
            "official_board": "Universidades públicas de cada Comunidad Autónoma",
        },
        "scoring": {"max_score": 14, "passing_score": 5, "grading_method": "60% nota Bachillerato + 40% fase obligatoria; voluntaria sube hasta 4 pts", "total_candidates": 300000},
        "schedule": {"frequency": "Once/year (convocatoria ordinaria + extraordinaria)", "typical_months": ["June", "July"]},
        "eligibility": "Bachillerato completo o equivalente",
    },
    # ── Mexico (es-419) ────────────────────────────────────────────────────────
    "EXANI-II (CENEVAL)": {
        "format": {
            "duration_minutes": 180,
            "total_marks": 1300,
            "sections": ["Pensamiento Matemático", "Pensamiento Analítico", "Estructura de la Lengua", "Comprensión Lectora", "Módulo de diagnóstico disciplinar"],
            "question_types": ["Opción múltiple (4 opciones)"],
            "negative_marking": False,
            "calculator_allowed": False,
            "language": ["Español"],
        },
        "syllabus": {
            "key_topics": ["Aritmética", "Álgebra", "Geometría Analítica", "Estadística", "Gramática", "Comprensión de textos", "Razonamiento lógico"],
            "official_board": "CENEVAL (Centro Nacional de Evaluación)",
            "syllabus_url": "https://www.ceneval.edu.mx",
        },
        "scoring": {"max_score": 1300, "passing_score": None, "grading_method": "Índice CENEVAL (700–1300); cada universidad define su corte", "total_candidates": 1500000},
        "schedule": {"frequency": "Varies by university", "typical_months": ["March", "June"]},
        "eligibility": "Certificado de bachillerato o constancia de estudios",
    },
    "COMIPEMS": {
        "format": {
            "duration_minutes": 180,
            "total_marks": 128,
            "sections": ["Habilidad Verbal", "Habilidad Matemática", "Español", "Matemáticas", "Ciencias Naturales", "Ciencias Sociales", "Historia"],
            "question_types": ["Opción múltiple (4 opciones)"],
            "negative_marking": False,
            "calculator_allowed": False,
            "language": ["Español"],
        },
        "syllabus": {
            "key_topics": ["Comprensión lectora", "Aritmética y geometría básica", "Biología", "Física elemental", "Historia de México", "Formación Cívica y Ética"],
            "official_board": "COMIPEMS (Comisión Metropolitana de Instituciones Públicas de Educación Media Superior)",
        },
        "scoring": {"max_score": 128, "passing_score": 31, "grading_method": "Aciertos → Asignación por orden de preferencia", "total_candidates": 340000},
        "schedule": {"frequency": "Once/year", "typical_months": ["June"]},
        "eligibility": "Estudiantes egresados de secundaria en la ZMVM",
    },
    # ── Colombia (es-419) ──────────────────────────────────────────────────────
    "Saber 11 (ICFES)": {
        "format": {
            "duration_minutes": 270,
            "total_marks": 500,
            "sections": ["Lectura Crítica", "Matemáticas", "Sociales y Ciudadanas", "Ciencias Naturales", "Inglés"],
            "question_types": ["Opción múltiple (4 opciones)", "Preguntas abiertas (Inglés writing)"],
            "negative_marking": False,
            "calculator_allowed": False,
            "language": ["Español"],
        },
        "syllabus": {
            "key_topics": ["Comprensión de textos", "Razonamiento cuantitativo", "Competencias ciudadanas", "Indagación científica", "Comunicación en inglés"],
            "official_board": "ICFES (Instituto Colombiano para la Evaluación de la Educación)",
            "syllabus_url": "https://www.icfes.gov.co",
        },
        "scoring": {"max_score": 500, "passing_score": None, "grading_method": "Puntaje global (0–500); cada módulo 0–100", "total_candidates": 600000},
        "schedule": {"frequency": "2 sessions/year", "typical_months": ["March", "August"]},
        "eligibility": "Estudiantes de grado 11 o bachilleres",
    },
    # ── Egypt (ar) ─────────────────────────────────────────────────────────────
    "الثانوية العامة (Thanawiya Amma)": {
        "format": {
            "duration_minutes": 180,
            "total_marks": 410,
            "sections": ["المواد الإجبارية: اللغة العربية، اللغة الإنجليزية", "شعبة علمي: الرياضيات، الفيزياء، الكيمياء", "شعبة أدبي: التاريخ، الجغرافيا، الفلسفة"],
            "question_types": ["اختيار من متعدد", "أسئلة مقالية", "حل مسائل"],
            "negative_marking": False,
            "calculator_allowed": False,
            "language": ["العربية"],
        },
        "syllabus": {
            "key_topics": ["النحو والبلاغة", "الميكانيكا", "الكيمياء العضوية", "التفاضل والتكامل", "الفيزياء الحديثة", "التاريخ المعاصر"],
            "official_board": "وزارة التربية والتعليم المصرية",
        },
        "scoring": {"max_score": 410, "passing_score": 205, "grading_method": "مجموع الدرجات → تنسيق الجامعات", "total_candidates": 700000},
        "schedule": {"frequency": "مرة سنوياً", "typical_months": ["June", "July"]},
        "eligibility": "طلاب الصف الثالث الثانوي",
    },
    # ── Saudi Arabia (ar) ──────────────────────────────────────────────────────
    "اختبار القدرات (Qudurat)": {
        "format": {
            "duration_minutes": 150,
            "total_marks": 100,
            "sections": ["القسم الكمي (52 سؤال)", "القسم اللفظي (68 سؤال)"],
            "question_types": ["اختيار من متعدد (4 خيارات)"],
            "negative_marking": False,
            "calculator_allowed": False,
            "language": ["العربية"],
        },
        "syllabus": {
            "key_topics": ["الحساب", "الهندسة", "الجبر", "التحليل", "استيعاب المقروء", "إكمال الجمل", "التناظر اللفظي", "الخطأ السياقي"],
            "official_board": "هيئة تقويم التعليم والتدريب (ETEC)",
            "syllabus_url": "https://www.etec.gov.sa",
        },
        "scoring": {"max_score": 100, "passing_score": None, "grading_method": "درجة موحدة 0–100; صالحة لمدة 5 سنوات", "total_candidates": 500000},
        "schedule": {"frequency": "عدة مرات سنوياً (ورقي + محوسب)", "typical_months": ["Any"]},
        "eligibility": "طلاب الثانوية والخريجون",
    },
    "اختبار التحصيلي (Tahsili)": {
        "format": {
            "duration_minutes": 150,
            "total_marks": 100,
            "sections": ["الأحياء", "الكيمياء", "الفيزياء", "الرياضيات"],
            "question_types": ["اختيار من متعدد"],
            "negative_marking": False,
            "calculator_allowed": False,
            "language": ["العربية"],
        },
        "syllabus": {
            "key_topics": ["أحياء: الوراثة والتكاثر", "كيمياء: الاتزان والحموض", "فيزياء: الحركة والقوى", "رياضيات: التفاضل والتكامل والمصفوفات"],
            "official_board": "هيئة تقويم التعليم والتدريب (ETEC)",
        },
        "scoring": {"max_score": 100, "passing_score": None, "grading_method": "درجة 0–100; مطلوبة للقبول الجامعي", "total_candidates": 350000},
        "schedule": {"frequency": "مرتين سنوياً", "typical_months": ["March", "June"]},
        "eligibility": "طلاب الثالث ثانوي (علمي) والخريجون",
    },
    # ── UAE (ar) ────────────────────────────────────────────────────────────────
    "EmSAT": {
        "format": {
            "duration_minutes": 120,
            "total_marks": 2000,
            "sections": ["EmSAT English", "EmSAT Math", "EmSAT Arabic", "EmSAT Physics (optional)"],
            "question_types": ["MCQ", "Fill-in-the-blank", "Essay (English)"],
            "negative_marking": False,
            "calculator_allowed": True,
            "language": ["English", "العربية"],
        },
        "syllabus": {
            "key_topics": ["Grammar & Vocabulary", "Reading", "Writing", "Algebra", "Geometry", "Statistics", "النحو والصرف", "البلاغة"],
            "official_board": "Ministry of Education, UAE",
            "syllabus_url": "https://emsat.gov.ae",
        },
        "scoring": {"max_score": 2000, "passing_score": None, "grading_method": "Score bands per subject; university cutoffs vary", "total_candidates": 80000},
        "schedule": {"frequency": "Multiple times/year", "typical_months": ["March", "June", "September", "December"]},
        "eligibility": "Grade 12 students and graduates in the UAE",
    },
    # ── France (fr) ────────────────────────────────────────────────────────────
    "Baccalauréat": {
        "format": {
            "duration_minutes": 240,
            "total_marks": 20,
            "sections": ["Épreuves de tronc commun: Français (écrit + oral), Philosophie, Grand oral", "Épreuves de spécialité: 2 matières au choix (4h chacune)"],
            "question_types": ["Dissertation", "Commentaire de texte", "Exercices et problèmes", "QCM (certaines spécialités)", "Oral"],
            "negative_marking": False,
            "calculator_allowed": True,
            "language": ["Français"],
        },
        "syllabus": {
            "key_topics": ["Analyse et géométrie", "Probabilités", "Mécanique newtonienne", "Thermodynamique", "Réactions chimiques", "Littérature française", "Philosophie morale et politique"],
            "official_board": "Ministère de l'Éducation nationale",
        },
        "scoring": {"max_score": 20, "passing_score": 10, "grading_method": "Moyenne pondérée sur 20; contrôle continu (40%) + épreuves terminales (60%)", "total_candidates": 730000},
        "schedule": {"frequency": "Une fois/an", "typical_months": ["June"]},
        "eligibility": "Élèves de Terminale",
    },
    "Brevet des collèges": {
        "format": {
            "duration_minutes": 300,
            "total_marks": 800,
            "sections": ["Français (3h)", "Mathématiques (2h)", "Histoire-Géographie-EMC (2h)", "Sciences (1h): 2 matières parmi Physique-Chimie, SVT, Technologie"],
            "question_types": ["QCM", "Rédaction", "Exercices", "Analyse de documents"],
            "negative_marking": False,
            "calculator_allowed": True,
            "language": ["Français"],
        },
        "syllabus": {
            "key_topics": ["Dictée et rédaction", "Géométrie et algèbre", "La République française", "Géographie de la France", "Énergie et transformations", "Le vivant"],
            "official_board": "Ministère de l'Éducation nationale",
        },
        "scoring": {"max_score": 800, "passing_score": 400, "grading_method": "Contrôle continu (400 pts) + épreuves finales (400 pts)", "total_candidates": 850000},
        "schedule": {"frequency": "Une fois/an", "typical_months": ["June"]},
        "eligibility": "Élèves de 3ème (collège)",
    },
    # ── Germany (de) ───────────────────────────────────────────────────────────
    "Abitur": {
        "format": {
            "duration_minutes": 270,
            "total_marks": 900,
            "sections": ["3 schriftliche Prüfungen (je 4–5 Std.)", "1 mündliche Prüfung (30 min)", "2 Leistungskurse + 2 Grundkurse"],
            "question_types": ["Klausur (essay/calculation)", "Erörterung", "Textanalyse", "Experiment-Auswertung", "Mündliche Präsentation"],
            "negative_marking": False,
            "calculator_allowed": True,
            "language": ["Deutsch"],
        },
        "syllabus": {
            "key_topics": ["Analysis (Kurvendiskussion, Integrale)", "Lineare Algebra (Vektoren, Matrizen)", "Stochastik", "Mechanik", "Elektrodynamik", "Literaturgeschichte", "Erörterung"],
            "official_board": "Kultusministerkonferenz (KMK) + Landesbehörden",
        },
        "scoring": {"max_score": 900, "passing_score": 300, "grading_method": "Punktesystem 0–15 pro Fach; Gesamtqualifikation 300–900 → Abiturnote 1,0–4,0", "total_candidates": 350000},
        "schedule": {"frequency": "Einmal jährlich", "typical_months": ["March", "April", "May"]},
        "eligibility": "Schüler der Qualifikationsphase (Jg. 12/13)",
    },
    "Mittlere Reife (Realschulabschluss)": {
        "format": {
            "duration_minutes": 180,
            "total_marks": None,
            "sections": ["Deutsch (Aufsatz + Diktat/Sprachbetrachtung)", "Mathematik", "Englisch"],
            "question_types": ["Aufsatz", "Textverständnis", "Rechnen und Sachaufgaben", "Listening & Reading Comprehension"],
            "negative_marking": False,
            "calculator_allowed": True,
            "language": ["Deutsch"],
        },
        "syllabus": {
            "key_topics": ["Erörterung und Textanalyse", "Gleichungen und Funktionen", "Geometrie", "Prozentrechnung", "Englische Grammatik und Leseverstehen"],
            "official_board": "Landesbehörden (varies by Bundesland)",
        },
        "scoring": {"max_score": None, "passing_score": None, "grading_method": "Notensystem 1–6 pro Fach; Durchschnitt bestimmt Abschluss", "total_candidates": 400000},
        "schedule": {"frequency": "Einmal jährlich", "typical_months": ["May", "June"]},
        "eligibility": "Schüler der 10. Klasse (Realschule/Gymnasium)",
    },
    # ── Indonesia (id) ─────────────────────────────────────────────────────────
    "UTBK-SNBT": {
        "format": {
            "duration_minutes": 195,
            "total_marks": 1000,
            "sections": ["Tes Potensi Skolastik / TPS (90 min)", "Tes Literasi (45 min)", "Penalaran Matematika (30 min)", "Tes Literasi Bahasa Inggris (30 min)"],
            "question_types": ["Pilihan ganda (4 opsi)"],
            "negative_marking": False,
            "calculator_allowed": False,
            "language": ["Bahasa Indonesia"],
        },
        "syllabus": {
            "key_topics": ["Penalaran Umum", "Pengetahuan dan Pemahaman Umum", "Kemampuan Memahami Bacaan dan Menulis", "Pengetahuan Kuantitatif", "Literasi dalam Bahasa Indonesia dan Inggris"],
            "official_board": "BPPP Kemendikbudristek (Balai Pengelolaan Pengujian Pendidikan)",
            "syllabus_url": "https://snpmb.bppp.kemdikbud.go.id",
        },
        "scoring": {"max_score": 1000, "passing_score": None, "grading_method": "Skor IRT (Item Response Theory); peringkat nasional → seleksi PTN", "total_candidates": 800000},
        "schedule": {"frequency": "Sekali/tahun", "typical_months": ["April", "May"]},
        "eligibility": "Siswa SMA/MA/SMK kelas 12 atau lulusan 3 tahun terakhir",
    },
    "AKM (Asesmen Kompetensi Minimum)": {
        "format": {
            "duration_minutes": 120,
            "total_marks": None,
            "sections": ["Literasi Membaca (20 soal)", "Numerasi (20 soal)"],
            "question_types": ["Pilihan ganda", "Pilihan ganda kompleks", "Menjodohkan", "Isian singkat", "Uraian"],
            "negative_marking": False,
            "calculator_allowed": False,
            "language": ["Bahasa Indonesia"],
        },
        "syllabus": {
            "key_topics": ["Memahami teks informasi dan sastra", "Bilangan dan operasi", "Geometri dan pengukuran", "Data dan ketidakpastian", "Aljabar"],
            "official_board": "Kemendikbudristek",
        },
        "scoring": {"max_score": None, "passing_score": None, "grading_method": "Level kompetensi: Perlu Intervensi Khusus / Dasar / Cakap / Mahir", "total_candidates": 5000000},
        "schedule": {"frequency": "Sekali/tahun (ANBK)", "typical_months": ["September", "October"]},
        "eligibility": "Siswa kelas 5 SD, 8 SMP, 11 SMA (sampel)",
    },
    # ── Japan (ja) ─────────────────────────────────────────────────────────────
    "共通テスト (Kyōtsū Test)": {
        "format": {
            "duration_minutes": 600,
            "total_marks": 900,
            "sections": ["国語 (80 min, 200 pts)", "数学①+② (70+60 min, 200 pts)", "英語リーディング+リスニング (80+30 min, 200 pts)", "理科 (60 min × 2)", "社会 (60 min × 2)"],
            "question_types": ["マークシート (mark-sheet / MCQ)"],
            "negative_marking": False,
            "calculator_allowed": False,
            "language": ["日本語"],
        },
        "syllabus": {
            "key_topics": ["現代文・古文・漢文", "数学I・A・II・B・C", "英語リーディング・リスニング", "物理・化学・生物・地学", "日本史・世界史・地理・公民"],
            "official_board": "大学入試センター (National Center for University Entrance Examinations)",
        },
        "scoring": {"max_score": 900, "passing_score": None, "grading_method": "各科目素点合計 → 大学ごとの配点で換算", "total_candidates": 530000},
        "schedule": {"frequency": "年1回", "typical_months": ["January"]},
        "eligibility": "高校3年生 (卒業見込み) または卒業者",
    },
    "高校入試 (Kōkō Nyūshi)": {
        "format": {
            "duration_minutes": 250,
            "total_marks": 500,
            "sections": ["国語 (50 min, 100 pts)", "数学 (50 min, 100 pts)", "英語 (50 min, 100 pts)", "理科 (50 min, 100 pts)", "社会 (50 min, 100 pts)"],
            "question_types": ["記述式 (essay)", "選択式 (MCQ)", "計算問題"],
            "negative_marking": False,
            "calculator_allowed": False,
            "language": ["日本語"],
        },
        "syllabus": {
            "key_topics": ["方程式と関数", "図形の証明", "英語長文読解", "古文", "理科実験", "歴史と公民"],
            "official_board": "各都道府県教育委員会",
        },
        "scoring": {"max_score": 500, "passing_score": None, "grading_method": "学力検査 + 内申点 (調査書) の合算", "total_candidates": 1100000},
        "schedule": {"frequency": "年1回", "typical_months": ["February", "March"]},
        "eligibility": "中学3年生",
    },
    # ── South Korea (ko) ───────────────────────────────────────────────────────
    "수능 (CSAT / Suneung)": {
        "format": {
            "duration_minutes": 480,
            "total_marks": None,
            "sections": ["국어 (80 min, 45 Qs)", "수학 (100 min, 30 Qs)", "영어 (70 min, 45 Qs)", "한국사 (30 min, 20 Qs)", "탐구 (30 min × 2, 20 Qs each)"],
            "question_types": ["5지선다형 (5-option MCQ)", "주관식 (short answer, Math)"],
            "negative_marking": False,
            "calculator_allowed": False,
            "language": ["한국어"],
        },
        "syllabus": {
            "key_topics": ["독서와 문법", "미적분", "확률과 통계", "기하", "영어 독해와 듣기", "한국사", "사회/과학 탐구 선택"],
            "official_board": "한국교육과정평가원 (KICE)",
        },
        "scoring": {"max_score": None, "passing_score": None, "grading_method": "등급제 1–9 (표준점수 + 백분위); 한국사는 절대평가", "total_candidates": 500000},
        "schedule": {"frequency": "연 1회", "typical_months": ["November"]},
        "eligibility": "고등학교 3학년 또는 검정고시 합격자",
    },
    # ── Brazil (pt) ────────────────────────────────────────────────────────────
    "ENEM": {
        "format": {
            "duration_minutes": 660,
            "total_marks": 1000,
            "sections": ["Dia 1 (5h30): Linguagens (45 Qs) + Ciências Humanas (45 Qs) + Redação", "Dia 2 (5h): Ciências da Natureza (45 Qs) + Matemática (45 Qs)"],
            "question_types": ["Múltipla escolha (5 alternativas)", "Redação dissertativo-argumentativa"],
            "negative_marking": False,
            "calculator_allowed": False,
            "language": ["Português"],
        },
        "syllabus": {
            "key_topics": ["Interpretação de textos", "Gramática", "Funções e geometria", "Estatística", "Mecânica e termodinâmica", "Ecologia", "Química orgânica", "História do Brasil", "Geografia", "Filosofia e Sociologia"],
            "official_board": "INEP (Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira)",
            "syllabus_url": "https://www.gov.br/inep/pt-br/areas-de-atuacao/avaliacao-e-exames-educacionais/enem",
        },
        "scoring": {"max_score": 1000, "passing_score": None, "grading_method": "TRI (Teoria de Resposta ao Item) por área; Redação 0–1000; SISU usa nota do ENEM", "total_candidates": 4500000},
        "schedule": {"frequency": "Uma vez/ano", "typical_months": ["November"]},
        "eligibility": "Concluintes ou egressos do Ensino Médio",
    },
    "Vestibular (FUVEST/UNICAMP)": {
        "format": {
            "duration_minutes": 300,
            "total_marks": None,
            "sections": ["1ª Fase: 90 questões objetivas (5h)", "2ª Fase: Provas discursivas por área (3–4 dias)"],
            "question_types": ["Múltipla escolha", "Dissertativas", "Redação"],
            "negative_marking": False,
            "calculator_allowed": False,
            "language": ["Português"],
        },
        "syllabus": {
            "key_topics": ["Obras literárias obrigatórias", "Matemática avançada", "Física e Química", "Biologia", "História e Geografia", "Inglês"],
            "official_board": "FUVEST (USP) / COMVEST (UNICAMP)",
        },
        "scoring": {"max_score": None, "passing_score": None, "grading_method": "Nota padronizada; corte por curso; 1ª fase elimina, 2ª fase classifica", "total_candidates": 800000},
        "schedule": {"frequency": "Uma vez/ano", "typical_months": ["November", "December", "January"]},
        "eligibility": "Concluintes ou egressos do Ensino Médio",
    },
    # ── Portugal (pt) ──────────────────────────────────────────────────────────
    "Exames Nacionais": {
        "format": {
            "duration_minutes": 150,
            "total_marks": 200,
            "sections": ["Prova de cada disciplina: 2 grupos (I e II)", "Grupo I: itens de seleção", "Grupo II: itens de construção"],
            "question_types": ["Escolha múltipla", "Resposta restrita", "Resposta extensa (desenvolvimento)", "Cálculo com justificação"],
            "negative_marking": False,
            "calculator_allowed": True,
            "language": ["Português"],
        },
        "syllabus": {
            "key_topics": ["Análise Matemática (limites, derivadas, integrais)", "Álgebra Linear", "Probabilidades", "Fernando Pessoa e Heterónimos", "Gil Vicente", "Camões"],
            "official_board": "IAVE (Instituto de Avaliação Educativa)",
            "syllabus_url": "https://iave.pt",
        },
        "scoring": {"max_score": 200, "passing_score": 95, "grading_method": "0–200 pontos; classificação final = 30% exame + 70% interna (ou 50%/50% se melhorar)", "total_candidates": 200000},
        "schedule": {"frequency": "Uma vez/ano (1ª e 2ª fases)", "typical_months": ["June", "July"]},
        "eligibility": "Alunos do 12.º ano do Ensino Secundário",
    },
    # ── Russia (ru) ────────────────────────────────────────────────────────────
    "ЕГЭ (Единый государственный экзамен)": {
        "format": {
            "duration_minutes": 235,
            "total_marks": 100,
            "sections": ["Часть 1: тестовая (задания с кратким ответом)", "Часть 2: развёрнутый ответ (эссе / решение задач)"],
            "question_types": ["Тест с кратким ответом", "Задания с развёрнутым ответом", "Эссе (русский язык)"],
            "negative_marking": False,
            "calculator_allowed": False,
            "language": ["Русский"],
        },
        "syllabus": {
            "key_topics": ["Алгебра и начала анализа", "Планиметрия и стереометрия", "Орфография и пунктуация", "Сочинение по тексту", "Механика", "Электродинамика", "Программирование и логика"],
            "official_board": "Рособрнадзор / ФИПИ (Федеральный институт педагогических измерений)",
            "syllabus_url": "https://fipi.ru",
        },
        "scoring": {"max_score": 100, "passing_score": 36, "grading_method": "Первичные баллы → тестовые баллы (0–100); минимальный порог зависит от предмета", "total_candidates": 700000},
        "schedule": {"frequency": "Один раз в год (основная волна + резервные дни)", "typical_months": ["May", "June", "July"]},
        "eligibility": "Выпускники 11 класса",
    },
    "ОГЭ (Основной государственный экзамен)": {
        "format": {
            "duration_minutes": 235,
            "total_marks": None,
            "sections": ["2 обязательных: русский язык + математика", "2 по выбору из 12 предметов"],
            "question_types": ["Тест с кратким ответом", "Задания с развёрнутым ответом", "Устная часть (иностр. язык)"],
            "negative_marking": False,
            "calculator_allowed": False,
            "language": ["Русский"],
        },
        "syllabus": {
            "key_topics": ["Орфография и пунктуация", "Изложение и сочинение", "Алгебра и геометрия (7–9 класс)", "Предмет по выбору — полный курс основной школы"],
            "official_board": "Рособрнадзор / ФИПИ",
        },
        "scoring": {"max_score": None, "passing_score": None, "grading_method": "Первичные баллы → оценка 2–5; порог зависит от предмета", "total_candidates": 1500000},
        "schedule": {"frequency": "Один раз в год", "typical_months": ["May", "June"]},
        "eligibility": "Выпускники 9 класса",
    },
}


async def seed_exam_packs() -> int:
    """Insert all exam packs if the table is empty.  Returns count inserted."""
    created = 0
    async for session in get_session():
        count = (await session.execute(select(func.count()).select_from(ExamPack))).scalar()
        if count and count > 0:
            logger.info("Exam packs already seeded (%d rows) — skipping", count)
            return 0

        for ep_data in EXAM_PACKS:
            subjects = ep_data.pop("subjects")
            is_coming_soon = ep_data.pop("is_coming_soon", False)
            meta = EXAM_METADATA.get(ep_data.get("name"), {})
            ep = ExamPack(is_coming_soon=is_coming_soon, metadata_=meta, **ep_data)
            session.add(ep)
            await session.flush()

            for i, subj_name in enumerate(subjects):
                session.add(ExamSubject(exam_pack_id=ep.id, name=subj_name, order=i))

            created += 1

        await session.commit()
        logger.info("Seeded %d exam packs", created)
    return created


async def _main():
    ok = await init_pg()
    if not ok:
        print("PG_HOST not set — cannot seed")
        return
    n = await seed_exam_packs()
    print(f"Seeded {n} exam packs")


if __name__ == "__main__":
    asyncio.run(_main())
