#!/usr/bin/env python3
"""Generate a modern Tailwind static site from CHD City Hospital content."""
from pathlib import Path

ROOT = Path("/workspace/public")

PHONE = "+91 9644000067"
PHONE_HREF = "tel:+919644000067"
PHONE2 = "0172-4006061"
APPT = "+91 7508008115"
APPT_HREF = "tel:+917508008115"
WHATSAPP = "https://wa.me/919644000067"
EMAIL = "info@chdcityhospital.com"
ADDRESS = "SCO 10-11, Madhya Marg, Sector 8C, Chandigarh 160009"

DEPARTMENTS = [
    {
        "slug": "internal-medicine",
        "name": "Internal Medicine & Rheumatology",
        "short": "Diagnosis and long-term care for infections, diabetes, hypertension, arthritis, and autoimmune disease.",
        "lead": "The Department of General Medicine and Rheumatology offers comprehensive care to outpatients and inpatients, with accurate diagnosis, effective treatment, and long-term health management.",
        "body": [
            "Our physicians treat a wide range of conditions including fever, abdominal pain, infections, jaundice, diabetes, hypertension, arthritis, and autoimmune disease. Care is led by experienced internists and rheumatologists in Chandigarh.",
            "Patients with chronic joint pain, inflammatory symptoms, or complex multi-system illness receive an individualised plan that looks beyond symptom control to mobility, comfort, and quality of life.",
            "Preventive check-ups, chronic disease follow-up, and referral-based rheumatology care are available under one roof.",
        ],
        "treatments": [
            "Allergy and immunology",
            "Diabetes and metabolic disorders",
            "Hypertension and cardiac risk",
            "Rheumatology and arthritis",
            "Gastrointestinal and liver care",
            "Kidney-related medical illness",
            "Vaccination and preventive care",
        ],
    },
    {
        "slug": "bariatric-surgery",
        "name": "Minimal Access & Bariatric Surgery",
        "short": "Laparoscopic weight-loss and GI surgery with faster recovery and smaller incisions.",
        "lead": "The Department of Bariatric and Metabolic Surgery provides modern surgical therapy for obesity and related illness, including type 2 diabetes, hypertension, sleep apnea, GERD, and joint problems.",
        "body": [
            "CHD City Hospital is a trusted centre for laparoscopic bariatric surgery in Chandigarh. Minimally invasive techniques mean less pain, smaller scars, and a quicker return to walking after surgery.",
            "The team also performs laparoscopic gallbladder stone surgery, hernia repair, GI surgery, and selected cancer surgeries. Packages include pre-operative investigations without extra cost.",
            "Laparoscopic gallbladder stone removal is offered as a focused package from Rs. 32,000, with free consultation from the gallstone team.",
        ],
        "treatments": [
            "Sleeve gastrectomy",
            "Gastric bypass and mini gastric bypass",
            "Gastric bands",
            "Laparoscopic cholecystectomy",
            "Laparoscopic hernia repair",
            "GI and cancer surgeries",
        ],
    },
    {
        "slug": "orthopaedics",
        "name": "Orthopaedics, Joints & Spine",
        "short": "Joint replacement, trauma, sports injury, and spine care with rehabilitation support.",
        "lead": "Orthopaedics and trauma at CHD City Hospital focuses on bone, joint, and connective tissue problems using both surgical and non-surgical care.",
        "body": [
            "The team treats fractures, arthritis, sports injuries, and complex joint problems. Arthroscopy and joint replacement — including knee replacement — use minimally invasive methods aimed at faster recovery.",
            "Spine, hand, shoulder, elbow, foot and ankle surgery are available, along with paediatric orthopaedics and arthritis injections. Trauma care covers accident-related injuries in a modular OT.",
            "Physiotherapy and post-operative rehabilitation help patients return to daily life. Dr. M. S. Narula leads a high-volume joint replacement and spine practice.",
        ],
        "treatments": [
            "Total joint reconstruction",
            "Knee and hip replacement",
            "Spine surgery",
            "Orthopaedic trauma",
            "Sports injury and arthroscopy",
            "Hand, shoulder and elbow surgery",
            "Foot and ankle surgery",
        ],
    },
    {
        "slug": "obstetrics-gynaecology",
        "name": "Obstetrics & Gynaecology",
        "short": "Pregnancy, delivery, fertility, and laparoscopic gynaecology across every stage of life.",
        "lead": "The Department of Obstetrics and Gynaecology provides complete women’s health care, from adolescence and PCOS through pregnancy, menopause, and gynaec surgery.",
        "body": [
            "Prenatal care, high-risk pregnancy support, and 24×7 paediatric cover for newborns make this a trusted maternity option in Chandigarh. Colposcopy, PAP smears, D&C, and IUCD services are available.",
            "Laparoscopic and gynaec oncology expertise is part of the faculty, with a holistic approach to menstrual, hormonal, and fertility concerns.",
        ],
        "treatments": [
            "Antenatal and postpartum care",
            "High-risk and multiple pregnancy",
            "VBAC and premature labour care",
            "Laparoscopy and hysteroscopy",
            "Endometriosis and ovarian cysts",
            "Infertility evaluation",
            "Pap smear and contraception",
        ],
    },
    {
        "slug": "urology",
        "name": "Urology",
        "short": "Laser kidney stone, prostate, bladder, infertility, and paediatric urology care.",
        "lead": "Urology at CHD City Hospital treats urinary and reproductive conditions in men, women, and children, supported by a Thulium laser system.",
        "body": [
            "Kidney, ureter, and bladder stones are treated with RIRS, PCNL, and laser methods for faster, less painful recovery. Laser prostate surgery helps men with BPH without large incisions.",
            "The team also treats strictures, PUJ obstruction, urinary fistulas, incontinence, hydrocele, male infertility, and paediatric conditions such as hypospadias and PU valves.",
        ],
        "treatments": [
            "Laser kidney stone treatment (RIRS / PCNL)",
            "Laser prostate surgery",
            "Bladder disorder care",
            "Male infertility and microsurgery",
            "Paediatric urology",
            "Incontinence and reconstructive urology",
        ],
    },
    {
        "slug": "ent",
        "name": "ENT",
        "short": "Ear, nose, and throat care including sinus surgery, hearing, and cochlear implants.",
        "lead": "ENT specialists treat infections, hearing loss, sinus disease, balance problems, and head-and-neck conditions in adults and children.",
        "body": [
            "Services include endoscopic nasal surgery, mastoid surgery, myringoplasty, tonsil and salivary gland care, and selected skull-base work. Cochlear implant pathways are available for severe hearing loss.",
            "Doctors explain each step in plain language, from diagnosis through recovery.",
        ],
        "treatments": [
            "Sinusitis and nasal obstruction",
            "Tinnitus and hearing loss",
            "Tonsillitis",
            "Mastoid surgery and myringoplasty",
            "Neck dissections and salivary glands",
            "Cochlear implant pathway",
        ],
    },
    {
        "slug": "endocrinology",
        "name": "Endocrinology",
        "short": "Diabetes, thyroid, PCOS, and hormone disorders with long-term follow-up.",
        "lead": "Endocrinology coordinates diagnosis and treatment for diabetes and other hormone-related conditions.",
        "body": [
            "Consultative, diagnostic, and therapeutic services cover thyroid disease, diabetes, pituitary and growth problems, adrenal disorders, and male and female hormone imbalance.",
        ],
        "treatments": [
            "Diabetes care",
            "Thyroid disorders and thyroid cancer",
            "Hyperthyroidism",
            "Cushing’s disease",
            "PCOS and hormone imbalance",
        ],
    },
    {
        "slug": "radiology",
        "name": "Radiology",
        "short": "X-ray, ultrasound, and coordinated CT, MRI, and image-guided diagnostics.",
        "lead": "Radiology provides diagnostic imaging and selected image-guided procedures so other teams can treat with confidence.",
        "body": [
            "On-site services include X-ray and ultrasound. CT, MRI, fluoroscopy, PET, and arthrograms are coordinated through trusted partners. Reports are reviewed carefully and explained to patients.",
            "Imaging supports orthopaedics, cardiology, neurology, obstetrics, and oncology.",
        ],
        "treatments": [
            "X-ray",
            "Ultrasound",
            "CT scan (tie-up)",
            "MRI (tie-up)",
            "Mammography pathway",
            "Thyroid scan",
        ],
    },
    {
        "slug": "paediatrics",
        "name": "Paediatrics",
        "short": "Newborn, child, and adolescent care with PICU and neonatal support.",
        "lead": "Paediatrics looks after infants, children, and teenagers in a calm, family-centred setting.",
        "body": [
            "The PICU uses monitoring and respiratory support for critically ill children. Neonatology cares for premature and low-birth-weight babies with 24-hour surveillance.",
            "Nutrition guidance, vaccination, developmental checks, and paediatric surgery pathways — including urology, laparoscopy, and neurosurgery — are available.",
        ],
        "treatments": [
            "Newborn and neonatal care",
            "Vaccination",
            "Paediatric surgery",
            "Paediatric urology and endocrinology",
            "PICU support",
        ],
    },
    {
        "slug": "cardiology",
        "name": "Cardiology",
        "short": "Heart evaluation, medical cardiology, and coordinated advanced heart care.",
        "lead": "Cardiology focuses on prevention, diagnosis, and medical management of heart disease for patients across the Tricity.",
        "body": [
            "Chest pain, breathlessness, hypertension, and known heart disease are assessed with ECG and clinical review. DNB cardiology expertise is available on the faculty.",
            "When intervention or tertiary cardiac surgery is needed, the team coordinates the next step and follow-up.",
        ],
        "treatments": [
            "Hypertension and risk assessment",
            "ECG and medical cardiology",
            "Heart failure follow-up",
            "Referral for interventional care",
        ],
    },
    {
        "slug": "physiotherapy",
        "name": "Physiotherapy",
        "short": "Rehab after joint, spine, and sports injury, plus pain and mobility programmes.",
        "lead": "Physiotherapy works with orthopaedics and medicine to restore movement after injury, surgery, or long-term pain.",
        "body": [
            "Programmes cover back and joint pain, post-joint-replacement rehab, sports recovery, and neurological mobilisation. Sessions are planned around each patient’s goals.",
        ],
        "treatments": [
            "Post-operative rehabilitation",
            "Spine and joint physiotherapy",
            "Sports injury recovery",
            "Pain and mobility programmes",
        ],
    },
    {
        "slug": "dentistry",
        "name": "Dentistry",
        "short": "Family dentistry, implants, braces, paediatric dentistry, and oral surgery.",
        "lead": "Dentistry and maxillofacial surgery provide complete oral care for children and adults.",
        "body": [
            "Services include check-ups, implants, invisible braces, laser dentistry, painless root canal, paediatric dentistry, and oral surgery. Cosmetic dentistry is available with PGI-trained faculty.",
        ],
        "treatments": [
            "Dental check-up",
            "Braces and implants",
            "Gum disease care",
            "Root canal and paediatric dentistry",
            "Oral and maxillofacial surgery",
        ],
    },
    {
        "slug": "dermatology",
        "name": "Dermatology",
        "short": "Medical, paediatric, and cosmetic care for skin, hair, and nails.",
        "lead": "Dermatology treats acne, eczema, psoriasis, infections, hair loss, pigmentation, and selected autoimmune skin disease.",
        "body": [
            "Medical, surgical, cosmetic, and paediatric dermatology are offered. Options include laser therapy, chemical peels, biopsies, and vitiligo grafting pathways.",
        ],
        "treatments": [
            "Acne and dermatitis",
            "Hair loss and nail problems",
            "Laser therapy and chemical peels",
            "Biopsies and surgical excision",
            "Paediatric dermatology",
        ],
    },
    {
        "slug": "nephrology",
        "name": "Nephrology",
        "short": "Kidney disease, dialysis support, and coordinated urology care.",
        "lead": "Nephrology cares for chronic kidney disease, diabetic and hypertensive kidney damage, and dialysis support.",
        "body": [
            "Plans are tailored to each patient, with ultrasound, biopsy pathways, and transplant counselling when needed. The team works closely with urology and nutrition.",
        ],
        "treatments": [
            "Chronic kidney disease",
            "Diabetic nephropathy",
            "Dialysis support",
            "Kidney biopsy pathway",
            "Transplant counselling",
        ],
    },
    {
        "slug": "critical-care",
        "name": "Critical Care Medicine",
        "short": "ICU and HDU support for seriously ill medical and surgical patients.",
        "lead": "Critical care provides intensive monitoring and organ support in the hospital ICU and HDU.",
        "body": [
            "The 25-bed hospital includes ICU, HDU, wards, and private rooms. Critical care physicians work with surgeons, internists, and nursing staff around the clock.",
        ],
        "treatments": [
            "Medical and surgical ICU",
            "HDU step-down care",
            "Post-operative intensive support",
            "Ventilatory and monitoring care",
        ],
    },
    {
        "slug": "psychiatry",
        "name": "Psychiatry",
        "short": "Confidential care for anxiety, depression, stress, and child & adolescent mental health.",
        "lead": "Psychiatry helps people whose mood, sleep, concentration, or relationships are being disrupted by stress, anxiety, or depression.",
        "body": [
            "Treatment may combine therapy and medication. Child and adolescent psychiatry support is available. Care is private, practical, and focused on daily function — not stigma.",
        ],
        "treatments": [
            "Medication review",
            "Psychotherapy",
            "Anxiety and depression care",
            "Child and adolescent psychiatry",
            "Support planning",
        ],
    },
    {
        "slug": "neurology",
        "name": "Neurology",
        "short": "Stroke, migraine, epilepsy, Parkinson’s, and coordinated neurosurgery.",
        "lead": "Neurology treats disorders of the brain, spine, and nerves with medical care and, when needed, surgical partners.",
        "body": [
            "Migraine, stroke, epilepsy, Parkinson’s, neuropathies, and multiple sclerosis are evaluated with a customised plan. Neurosurgery covers trauma, tumours, disc disease, and nerve compression.",
            "EMG, lumbar puncture, and rehabilitation complete the pathway from diagnosis to recovery.",
        ],
        "treatments": [
            "Stroke and migraine care",
            "Epilepsy and Parkinson’s",
            "EMG and lumbar puncture",
            "Spine and nerve disorders",
            "Neurosurgical coordination",
        ],
    },
    {
        "slug": "pathology",
        "name": "Pathology",
        "short": "Laboratory diagnostics that support every department’s treatment decisions.",
        "lead": "Pathology provides the laboratory backbone for diagnosis, surgery planning, and follow-up.",
        "body": [
            "Pre-operative investigations are included in many surgical packages. Results are interpreted with the treating doctor so patients understand next steps.",
        ],
        "treatments": [
            "Pre-operative investigations",
            "Routine and specialised lab tests",
            "Histopathology support",
        ],
    },
]

DOCTORS = [
    {"slug": "dr-manpal-singh-narula", "name": "Dr. Manpal Singh Narula", "role": "Orthopaedics, Joints & Spine", "dept": "orthopaedics", "edu": "MBBS, MS Orthopaedics", "bio": "Leading orthopaedic surgeon with over 20 years of experience in trauma, joint replacement, spine disease, and sports injuries. He has performed over 2,000 joint replacement and spine surgeries and is a visiting surgeon at New Yorkshire hospitals, UK. His 5E philosophy: Ethical, Efficient, Empathetic care backed by Experience and Expertise."},
    {"slug": "dr-gursimran-singh", "name": "Dr. Gursimran Singh", "role": "Minimal Access & Bariatric Surgery", "dept": "bariatric-surgery", "edu": "MBBS, MS (General Surgery), F.MAS, D.MAS", "bio": "MS in General Surgery from ASCOMS, Jammu, and MBBS from Guru Ram Das Medical College. Awarded Excellence — Young Healthcare Personality in Minimal Access & Bariatric Surgery (2018). Member of SELSI and WALS. Interests: laparoscopy, bariatric surgery, and onco-surgery."},
    {"slug": "dr-vibha-sharma", "name": "Dr. Vibha Sharma", "role": "Obstetrics & Gynaecology", "dept": "obstetrics-gynaecology", "edu": "Obstetrics & Gynaecology", "bio": "Senior gynaecologist known to patients for attentive maternity and women’s health care. Families frequently mention her and the nursing team in hospital reviews."},
    {"slug": "dr-bimaldeep-singh", "name": "Dr. Bimaldeep Singh", "role": "Dentistry", "dept": "dentistry", "edu": "MDS (PGI), Cosmetic Dentistry (USA), MBA (Hospital Admin & HR)", "bio": "13+ years in dentistry. MD from PGI with BDS and MDS in paediatric and preventive dentistry, plus cosmetic dentistry training in the United States and an MBA in hospital administration."},
    {"slug": "dr-manoj-sharma", "name": "Dr. Manoj Sharma", "role": "Urology", "dept": "urology", "edu": "MBBS, MS, MCh", "bio": "Urologist providing laser stone, prostate, and reconstructive urology care as part of the hospital’s Thulium laser programme."},
    {"slug": "dr-gaurav-sharma", "name": "Dr. Gaurav Sharma", "role": "Orthopaedics", "dept": "orthopaedics", "edu": "MBBS, MS Orthopaedics", "bio": "Orthopaedic surgeon involved in trauma, joint, and musculoskeletal care alongside the hospital’s replacement and spine programme."},
    {"slug": "dr-rp-singh", "name": "Dr. R. P. Singh", "role": "Cardiology", "dept": "cardiology", "edu": "MD General Medicine, DNB Cardiology", "bio": "Cardiologist focused on medical heart care, hypertension, and coordinated advanced cardiac treatment."},
    {"slug": "dr-gourav-jain", "name": "Dr. Gourav Jain", "role": "Neurology", "dept": "neurology", "edu": "MD, DM Neurology", "bio": "Neurologist for migraine, stroke, epilepsy, and chronic neurological disease."},
    {"slug": "dr-ravi-garg", "name": "Dr. Ravi Garg", "role": "Neurosurgery", "dept": "neurology", "edu": "MS, MCh Neurosurgery", "bio": "Neurosurgeon for brain, spine, and nerve surgery in coordination with the neurology team."},
    {"slug": "dr-deepak-tyagi", "name": "Dr. Deepak Tyagi", "role": "Neurosurgery", "dept": "neurology", "edu": "MBBS, MS, MCh Neurosurgery", "bio": "Senior neurosurgeon supporting trauma, spine, and cranial surgical care."},
    {"slug": "dr-neha-garg", "name": "Dr. Neha Garg", "role": "Nephrology", "dept": "nephrology", "edu": "MBBS, MD Medicine, DM Nephrology", "bio": "Nephrologist for chronic kidney disease, dialysis support, and medical kidney care."},
    {"slug": "dr-itee-sidana", "name": "Dr. Itee Sidana", "role": "Psychiatry", "dept": "psychiatry", "edu": "MBBS, MD Psychiatry, STT Child & Adolescent Psychiatry", "bio": "Psychiatrist with additional training in child and adolescent mental health."},
    {"slug": "dr-ashish-garg", "name": "Dr. Ashish Garg", "role": "Critical Care Medicine", "dept": "critical-care", "edu": "MBBS, MD, FNB", "bio": "Critical care physician for ICU and HDU patients after major surgery or severe medical illness."},
    {"slug": "dr-prateek-soni", "name": "Dr. Prateek Soni", "role": "ENT", "dept": "ent", "edu": "MS ENT", "bio": "ENT surgeon for sinus, hearing, throat, and head-and-neck conditions."},
    {"slug": "dr-rishi-mangat", "name": "Dr. Rishi Mangat", "role": "General Physician", "dept": "internal-medicine", "edu": "MBBS, Fellow in Diabetes", "bio": "General physician with a diabetes fellowship, supporting internal medicine and metabolic care."},
    {"slug": "dr-anila-sharma", "name": "Dr. Anila Sharma", "role": "Radiology", "dept": "radiology", "edu": "MBBS, DNB Radio Diagnosis", "bio": "Radiologist with 20+ years of experience. MBBS from Lady Hardinge Medical College, Delhi, and DNB radio diagnosis from the University of Pune."},
    {"slug": "dr-gurmeen-garg", "name": "Dr. Gurmeen Garg", "role": "Pathology", "dept": "pathology", "edu": "MD Pathology", "bio": "Pathologist with 8+ years of laboratory and diagnostic experience supporting surgical and medical teams."},
    {"slug": "dr-lissie-palathingal", "name": "Dr. Lissie Palathingal", "role": "General Practice", "dept": "internal-medicine", "edu": "MBBS", "bio": "General practitioner with 15+ years of experience. MBBS from Gandhi Medical College, Bhopal. Oversees corporate health checks."},
    {"slug": "dr-preeti-sharma", "name": "Dr. Preeti Sharma", "role": "Pulmonology", "dept": "internal-medicine", "edu": "MBBS, MD", "bio": "Pulmonologist with 12+ years of experience and membership of the Indian Society of Critical Care Medicine."},
    {"slug": "dr-jayanti-jain", "name": "Dr. Jayanti Jain", "role": "Dermatology", "dept": "dermatology", "edu": "Dermatology", "bio": "Dermatologist specialising in acne, eczema, hair loss, and pigmentation."},
    {"slug": "dr-vimal", "name": "Dr. Vimal", "role": "General Surgery", "dept": "bariatric-surgery", "edu": "MBBS, MS General Surgery", "bio": "General surgeon supporting laparoscopic and open surgical care."},
    {"slug": "dr-virender-dhankar", "name": "Dr. Virender Dhankar", "role": "Consultant", "dept": "internal-medicine", "edu": "Consultant physician", "bio": "Consultant on the CHD City Hospital faculty, providing specialist clinical care as part of the multidisciplinary team."},
]

BLOGS = [
    {"slug": "when-to-see-orthopedic-doctor", "title": "Joint Pain, Sports Injury or Arthritis? When to Visit an Orthopaedic Doctor", "date": "2026-07-12", "dept": "orthopaedics", "summary": "Persistent joint pain, swelling after injury, or stiffness that limits walking deserves a specialist review. Early assessment can separate simple strain from ligament injury or arthritis that needs structured treatment."},
    {"slug": "best-physiotherapist-back-joint-pain", "title": "How to Choose Physiotherapy for Back and Joint Pain", "date": "2026-07-05", "dept": "physiotherapy", "summary": "Look for a programme tied to diagnosis, not only machines. Good physiotherapy explains the plan, measures progress, and coordinates with your orthopaedic or medical doctor."},
    {"slug": "knee-replacement-signs", "title": "10 Signs You May Need Knee Replacement Surgery", "date": "2026-06-28", "dept": "orthopaedics", "summary": "Night pain, giving way, failed medicines and physiotherapy, and X-rays showing advanced arthritis are common reasons patients discuss replacement with a knee surgeon."},
    {"slug": "gynecologist-pregnancy-delivery", "title": "Choosing a Gynaecology Hospital for Pregnancy and Delivery", "date": "2026-06-20", "dept": "obstetrics-gynaecology", "summary": "Maternity care should include antenatal visits, a plan for high-risk pregnancy, paediatric cover at birth, and a team you can reach at odd hours."},
    {"slug": "dentist-general-vs-specialist", "title": "General Dentist or Specialist in Chandigarh?", "date": "2026-06-14", "dept": "dentistry", "summary": "Routine check-ups and fillings stay with a family dentist. Implants, braces, oral surgery, and complex paediatric cases often need a specialist under the same hospital roof."},
    {"slug": "vaccination-schedule-children", "title": "Vaccination Schedule Explained by Child Specialists", "date": "2026-06-08", "dept": "paediatrics", "summary": "Keeping immunisations on time protects infants and the wider family. Our paediatric team walks parents through the national schedule and catch-up doses."},
    {"slug": "fertility-myths", "title": "Fertility Myths Busted by Gynaecologists", "date": "2026-05-30", "dept": "obstetrics-gynaecology", "summary": "Age, irregular cycles, and untreated infections matter more than most internet advice. A structured evaluation is kinder than waiting another year on a guess."},
    {"slug": "safe-pregnancy-care", "title": "What Safe Pregnancy Care Looks Like", "date": "2026-05-22", "dept": "obstetrics-gynaecology", "summary": "Regular scans, blood pressure checks, anaemia treatment, and a documented birth plan reduce surprises. High-risk mothers need a hospital with ICU and neonatal backup."},
    {"slug": "ent-sinus-allergy-hearing", "title": "ENT Care for Sinus, Allergy and Hearing Problems", "date": "2026-05-15", "dept": "ent", "summary": "Blocked nose that lasts months, repeated ear infections, or hearing drop should not be ignored. Endoscopic and audiology pathways exist for precise treatment."},
    {"slug": "diabetes-endocrinology", "title": "Expert Diabetes Care with Endocrinology Support", "date": "2026-05-08", "dept": "endocrinology", "summary": "Good diabetes care is more than a single sugar reading. Medication, diet, kidney and eye screening, and thyroid review belong in one follow-up plan."},
    {"slug": "stress-autoimmune", "title": "When Stress and Autoimmune Symptoms Need a Rheumatologist", "date": "2026-04-28", "dept": "internal-medicine", "summary": "Unexplained joint swelling, rashes, and fatigue can be inflammatory disease — not “just stress”. Internal medicine and rheumatology can sort the cause."},
    {"slug": "when-to-see-psychiatrist", "title": "How to Know You Need a Psychiatrist", "date": "2026-04-18", "dept": "psychiatry", "summary": "If sleep, work, or relationships are breaking down, a confidential psychiatric review is appropriate. Asking for help is clinical care, not a last resort."},
    {"slug": "heart-specialist-chandigarh", "title": "How to Know When You Need a Heart Specialist", "date": "2026-04-10", "dept": "cardiology", "summary": "Chest discomfort, breathlessness on mild effort, or a strong family history of heart disease should trigger an ECG and cardiology opinion."},
    {"slug": "neurology-migraine-stroke", "title": "Expert Care for Migraine and Stroke", "date": "2026-04-02", "dept": "neurology", "summary": "Sudden weakness, speech change, or the worst headache of your life is an emergency. Recurrent migraine also deserves a neurologist, not only painkillers."},
    {"slug": "dermatologist-skin-hair", "title": "When to Visit a Dermatologist for Skin and Hair Problems", "date": "2026-03-25", "dept": "dermatology", "summary": "Acne that scars, sudden hair fall, or rashes that do not settle with home care are reasons to see a skin specialist."},
]

REVIEWS = [
    {"name": "Sanju Khatri", "text": "My wife was admitted under Dr Vibha Sharma — excellent doctor and nursing staff. Best faculty in the region."},
    {"name": "Jasleen Kaur", "text": "My father went for a major hip replacement under Dr M S Narula. His expertise is unmatched. He explained the surgery well and answered every question. Staff like Pooja, the IPD coordinator, were really kind."},
    {"name": "Jaspreet Dhaliwal", "text": "My mother was admitted for gallbladder and stone removal under Dr. Gursimran Singh. Excellent staff, top-notch facilities, and a highly skilled surgeon. A very positive experience."},
]


def esc(s: str) -> str:
    return (
        s.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def prefix(depth: int) -> str:
    return "../" * depth


def header(depth: int, active: str) -> str:
    p = prefix(depth)

    def nav(key, href, label):
        cls = "text-teal-800 font-semibold" if active == key else "text-slate-600 hover:text-teal-800"
        return f'<a href="{p}{href}" class="{cls}">{label}</a>'

    return f"""
  <div class="bg-slate-900 text-slate-100 text-sm">
    <div class="mx-auto max-w-7xl px-4 py-2 flex flex-wrap items-center justify-between gap-2">
      <p>NABH accredited · 24×7 emergency · Sector 8C, Chandigarh</p>
      <p class="flex flex-wrap gap-4">
        <a class="hover:text-white" href="{PHONE_HREF}">{PHONE}</a>
        <a class="hover:text-white" href="{APPT_HREF}">Appointments {APPT}</a>
      </p>
    </div>
  </div>
  <header class="sticky top-0 z-40 bg-white/95 backdrop-blur border-b border-slate-200">
    <div class="mx-auto max-w-7xl px-4 py-3 flex items-center justify-between gap-4">
      <a href="{p}index.html" class="flex items-center gap-3 min-w-0">
        <img src="{p}assets/logo.svg" alt="CHD City Hospital" class="h-12 w-auto">
      </a>
      <nav class="hidden lg:flex items-center gap-6 text-sm">
        {nav("home", "index.html", "Home")}
        {nav("about", "about/index.html", "About")}
        {nav("departments", "departments/index.html", "Departments")}
        {nav("doctors", "doctors/index.html", "Doctors")}
        {nav("blog", "blog/index.html", "Health Guide")}
        {nav("contact", "contact/index.html", "Contact")}
      </nav>
      <div class="flex items-center gap-3">
        <a href="{p}appointment/index.html" class="hidden sm:inline-flex rounded-full bg-teal-700 px-4 py-2 text-sm font-semibold text-white hover:bg-teal-800">Book appointment</a>
        <button type="button" data-menu-btn class="lg:hidden rounded-md border border-slate-300 p-2" aria-label="Open menu">
          <span class="block w-5 h-0.5 bg-slate-800 mb-1"></span>
          <span class="block w-5 h-0.5 bg-slate-800 mb-1"></span>
          <span class="block w-5 h-0.5 bg-slate-800"></span>
        </button>
      </div>
    </div>
    <div data-menu class="hidden lg:hidden border-t border-slate-200 bg-white px-4 py-4 space-y-3 text-sm">
      <a class="block" href="{p}index.html">Home</a>
      <a class="block" href="{p}about/index.html">About</a>
      <a class="block" href="{p}departments/index.html">Departments</a>
      <a class="block" href="{p}doctors/index.html">Doctors</a>
      <a class="block" href="{p}blog/index.html">Health Guide</a>
      <a class="block" href="{p}contact/index.html">Contact</a>
      <a class="block font-semibold text-teal-800" href="{p}appointment/index.html">Book appointment</a>
    </div>
  </header>
"""


def footer(depth: int) -> str:
    p = prefix(depth)
    dept_links = "\n".join(
        f'<li><a class="hover:text-white" href="{p}departments/{d["slug"]}/index.html">{esc(d["name"])}</a></li>'
        for d in DEPARTMENTS[:8]
    )
    return f"""
  <footer class="bg-slate-950 text-slate-300 mt-20">
    <div class="mx-auto max-w-7xl px-4 py-14 grid gap-10 md:grid-cols-2 lg:grid-cols-4">
      <div>
        <img src="{p}assets/logo.svg" alt="" class="h-10 mb-4 brightness-0 invert">
        <p class="text-sm leading-relaxed">CHD City Hospital LLP is a 25-bed NABH accredited hospital in Sector 8C, Chandigarh, owned and run by specialist doctors. Values: Expertise, Ethics and Empathy.</p>
      </div>
      <div>
        <h2 class="text-white font-semibold mb-3">Visit</h2>
        <p class="text-sm">{esc(ADDRESS)}</p>
        <p class="text-sm mt-2"><a href="{PHONE_HREF}">{PHONE}</a><br>{PHONE2}<br><a href="mailto:{EMAIL}">{EMAIL}</a></p>
        <p class="text-sm mt-2">Open 24×7</p>
      </div>
      <div>
        <h2 class="text-white font-semibold mb-3">Departments</h2>
        <ul class="text-sm space-y-1">{dept_links}</ul>
      </div>
      <div>
        <h2 class="text-white font-semibold mb-3">Hospital</h2>
        <ul class="text-sm space-y-1">
          <li><a class="hover:text-white" href="{p}about/index.html">About us</a></li>
          <li><a class="hover:text-white" href="{p}quality/index.html">Quality &amp; safety</a></li>
          <li><a class="hover:text-white" href="{p}faq/index.html">FAQ</a></li>
          <li><a class="hover:text-white" href="{p}careers/index.html">Careers</a></li>
          <li><a class="hover:text-white" href="{p}testimonials/index.html">Patient stories</a></li>
          <li><a class="hover:text-white" href="{p}privacy/index.html">Privacy policy</a></li>
          <li><a class="hover:text-white" href="{p}appointment/index.html">Request an appointment</a></li>
        </ul>
      </div>
    </div>
    <div class="border-t border-slate-800 text-xs text-slate-500 px-4 py-4 text-center">
      © 2026 CHD City Hospital · Sector 8C, Chandigarh · Redesigned independently from public website content.
    </div>
  </footer>
  <a href="{WHATSAPP}" class="fixed bottom-5 right-5 z-50 rounded-full bg-emerald-500 text-white shadow-lg px-4 py-3 text-sm font-semibold hover:bg-emerald-600">WhatsApp</a>
  <script>
    document.querySelectorAll("[data-menu-btn]").forEach((btn) => {{
      btn.addEventListener("click", () => {{
        document.querySelectorAll("[data-menu]").forEach((m) => m.classList.toggle("hidden"));
      }});
    }});
  </script>
"""


def shell(title: str, description: str, depth: int, active: str, body: str) -> str:
    p = prefix(depth)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{esc(title)}</title>
  <meta name="description" content="{esc(description)}">
  <link rel="icon" href="{p}assets/logo.svg">
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {{
      theme: {{
        extend: {{
          fontFamily: {{ sans: ["Plus Jakarta Sans", "system-ui", "sans-serif"] }}
        }}
      }}
    }};
  </script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <style>
    body {{ font-family: "Plus Jakarta Sans", system-ui, sans-serif; }}
  </style>
</head>
<body class="bg-slate-50 text-slate-800 antialiased">
{header(depth, active)}
{body}
{footer(depth)}
</body>
</html>
"""


def write(rel: str, html: str) -> None:
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(html, encoding="utf-8")


def home():
    cards = "\n".join(
        f"""
        <a href="departments/{d['slug']}/index.html" class="group rounded-2xl bg-white p-6 shadow-sm ring-1 ring-slate-200 hover:shadow-md hover:ring-teal-200 transition">
          <h3 class="font-semibold text-slate-900 group-hover:text-teal-800">{esc(d['name'])}</h3>
          <p class="mt-2 text-sm text-slate-600">{esc(d['short'])}</p>
        </a>"""
        for d in DEPARTMENTS
    )
    docs = "\n".join(
        f"""
        <a href="doctors/{d['slug']}/index.html" class="rounded-2xl bg-white p-5 ring-1 ring-slate-200 hover:ring-teal-300">
          <div class="h-14 w-14 rounded-full bg-teal-100 text-teal-800 grid place-items-center font-bold">{esc(d['name'].split()[1][0] if len(d['name'].split())>1 else d['name'][0])}</div>
          <h3 class="mt-3 font-semibold">{esc(d['name'])}</h3>
          <p class="text-sm text-teal-800">{esc(d['role'])}</p>
        </a>"""
        for d in DOCTORS[:8]
    )
    revs = "\n".join(
        f"""
        <blockquote class="rounded-2xl bg-white p-6 ring-1 ring-slate-200">
          <div class="text-amber-500 text-sm font-semibold">4.9 / 5 on Google</div>
          <p class="mt-3 text-slate-700">“{esc(r['text'])}”</p>
          <footer class="mt-4 text-sm font-medium text-slate-900">{esc(r['name'])}</footer>
        </blockquote>"""
        for r in REVIEWS
    )
    body = f"""
  <section class="relative overflow-hidden bg-gradient-to-br from-teal-900 via-slate-900 to-slate-950 text-white">
    <div class="mx-auto max-w-7xl px-4 py-20 lg:py-28 grid lg:grid-cols-2 gap-12 items-center">
      <div>
        <p class="text-teal-200 font-semibold tracking-wide uppercase text-xs">NABH accredited · 21+ specialties</p>
        <h1 class="mt-3 text-4xl sm:text-5xl lg:text-6xl font-extrabold tracking-tight">Find the care you need at CHD City Hospital</h1>
        <p class="mt-5 text-lg text-slate-200 max-w-xl">A doctor-led hospital in the heart of Chandigarh. ICU, HDU, modular OT, private rooms, and a faculty known for orthopaedics, laparoscopy, maternity, and urology.</p>
        <div class="mt-8 flex flex-wrap gap-3">
          <a href="appointment/index.html" class="rounded-full bg-teal-400 text-slate-950 px-6 py-3 font-semibold hover:bg-teal-300">Request a callback</a>
          <a href="departments/index.html" class="rounded-full border border-white/30 px-6 py-3 font-semibold hover:bg-white/10">Browse departments</a>
        </div>
      </div>
      <div class="rounded-3xl bg-white/10 backdrop-blur p-6 ring-1 ring-white/15">
        <p class="text-teal-200 text-sm font-semibold">Featured package</p>
        <h2 class="text-2xl font-bold mt-2">Laparoscopic gallbladder stone removal</h2>
        <p class="mt-2 text-3xl font-extrabold">₹32,000</p>
        <ul class="mt-4 space-y-2 text-sm text-slate-100">
          <li>Includes pre-operative investigations</li>
          <li>Minimal incision · less pain · quicker recovery</li>
          <li>Free consultation with the gallstone team</li>
        </ul>
        <a href="{APPT_HREF}" class="mt-6 inline-flex rounded-full bg-white text-slate-900 px-5 py-2.5 font-semibold">Call {APPT}</a>
      </div>
    </div>
  </section>
  <section class="mx-auto max-w-7xl px-4 -mt-8 grid sm:grid-cols-3 gap-4">
    <div class="rounded-2xl bg-white p-5 shadow-sm ring-1 ring-slate-200"><p class="text-3xl font-bold text-teal-800">25</p><p class="text-sm text-slate-600">Beds with ICU, HDU, wards and private rooms</p></div>
    <div class="rounded-2xl bg-white p-5 shadow-sm ring-1 ring-slate-200"><p class="text-3xl font-bold text-teal-800">21+</p><p class="text-sm text-slate-600">Clinical specialties in one multidisciplinary setting</p></div>
    <div class="rounded-2xl bg-white p-5 shadow-sm ring-1 ring-slate-200"><p class="text-3xl font-bold text-teal-800">4.9</p><p class="text-sm text-slate-600">Google rating from 250+ patient reviews</p></div>
  </section>
  <section class="mx-auto max-w-7xl px-4 py-16">
    <div class="flex items-end justify-between gap-4 mb-8">
      <div><h2 class="text-3xl font-bold text-slate-900">Departments</h2><p class="text-slate-600 mt-1">Integrated medical and surgical care close to home.</p></div>
      <a href="departments/index.html" class="text-teal-800 font-semibold">All departments</a>
    </div>
    <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-4">{cards}</div>
  </section>
  <section class="bg-white py-16">
    <div class="mx-auto max-w-7xl px-4">
      <h2 class="text-3xl font-bold text-slate-900">Why patients choose us</h2>
      <div class="mt-8 grid md:grid-cols-4 gap-6">
        <div><h3 class="font-semibold">More experience</h3><p class="text-sm text-slate-600 mt-2">Be confident in the treatment plan and your doctor’s abilities.</p></div>
        <div><h3 class="font-semibold">The right answers</h3><p class="text-sm text-slate-600 mt-2">Get answers and assurance with accuracy you can trust.</p></div>
        <div><h3 class="font-semibold">Seamless care</h3><p class="text-sm text-slate-600 mt-2">Compassionate healthcare from OPD to OT to recovery.</p></div>
        <div><h3 class="font-semibold">Unparalleled expertise</h3><p class="text-sm text-slate-600 mt-2">Specialist-owned hospital with national and international faculty experience.</p></div>
      </div>
    </div>
  </section>
  <section class="mx-auto max-w-7xl px-4 py-16">
    <div class="flex items-end justify-between mb-8">
      <h2 class="text-3xl font-bold">Our doctors</h2>
      <a href="doctors/index.html" class="text-teal-800 font-semibold">Meet the team</a>
    </div>
    <div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-4">{docs}</div>
  </section>
  <section class="mx-auto max-w-7xl px-4 pb-8">
    <h2 class="text-3xl font-bold mb-8">Patients in their own words</h2>
    <div class="grid md:grid-cols-3 gap-4">{revs}</div>
  </section>
"""
    write("index.html", shell("CHD City Hospital | Best Private Hospital in Chandigarh", "NABH accredited 25-bed multidisciplinary hospital in Sector 8C, Chandigarh.", 0, "home", body))


def about():
    body = f"""
  <section class="bg-teal-900 text-white py-16"><div class="mx-auto max-w-7xl px-4">
    <p class="text-teal-200 text-sm font-semibold">About us</p>
    <h1 class="text-4xl font-extrabold mt-2 max-w-3xl">We push the limits of what is possible for our patients</h1>
  </div></section>
  <section class="mx-auto max-w-3xl px-4 py-12 space-y-5 text-slate-700 leading-relaxed">
    <p>CHD CITY HOSPITAL LLP has rich experience in healthcare and is known for quality care for domestic and international patients. Offerings are supported by compassionate specialists with deep domain knowledge. CHD City Hospital has been a household name for families across the region.</p>
    <p>Services span orthopaedics, obstetrics, gynaecology, urology, general and laparoscopic surgery, and many other disciplines. The 25-bed hospital is equipped with ICU, HDU, ward, private rooms, and a modular OT. CHD City Hospital is NABH accredited.</p>
    <p>With over 21 clinical specialties, patients get integrated care in a multidisciplinary setting from doctors, nurses, and healthcare professionals. The hospital is owned and run by medical specialists and surgeons, organised around Expertise, Ethics and Empathy.</p>
    <p>Care is individualised while keeping treatment, infection, and patient-safety protocols. Hand-holding extends beyond in-house services to home and recuperation care. The vision is to be the first choice for healthcare in the Tricity.</p>
    <div class="grid sm:grid-cols-2 gap-4 pt-4">
      <div class="rounded-2xl bg-white p-5 ring-1 ring-slate-200"><h2 class="font-semibold">Facilities</h2><p class="text-sm mt-2">ICU, HDU, wards, private rooms, modular OT, parking for patients and visitors.</p></div>
      <div class="rounded-2xl bg-white p-5 ring-1 ring-slate-200"><h2 class="font-semibold">Location</h2><p class="text-sm mt-2">{esc(ADDRESS)}</p></div>
    </div>
  </section>
"""
    write("about/index.html", shell("About CHD City Hospital", "NABH accredited doctor-led hospital in Sector 8C, Chandigarh.", 1, "about", body))


def departments_index():
    cards = "\n".join(
        f"""<a href="{d['slug']}/index.html" class="rounded-2xl bg-white p-6 ring-1 ring-slate-200 hover:ring-teal-300">
          <h2 class="font-semibold text-lg">{esc(d['name'])}</h2>
          <p class="text-sm text-slate-600 mt-2">{esc(d['short'])}</p>
        </a>"""
        for d in DEPARTMENTS
    )
    body = f"""
  <section class="bg-slate-900 text-white py-14"><div class="mx-auto max-w-7xl px-4">
    <h1 class="text-4xl font-extrabold">All departments</h1>
    <p class="mt-3 text-slate-300 max-w-2xl">Compassionate care, advanced medicine, close to home. Dedicated to helping people feel and live better.</p>
  </div></section>
  <section class="mx-auto max-w-7xl px-4 py-12 grid sm:grid-cols-2 lg:grid-cols-3 gap-4">{cards}</section>
"""
    write("departments/index.html", shell("All Departments | CHD City Hospital", "21+ clinical specialties including orthopaedics, maternity, urology, and laparoscopy.", 1, "departments", body))


def department_page(d: dict):
    treatments = "".join(f"<li class='rounded-lg bg-teal-50 px-3 py-2 text-sm'>{esc(t)}</li>" for t in d["treatments"])
    paras = "".join(f"<p>{esc(p)}</p>" for p in d["body"])
    related = [x for x in DOCTORS if x["dept"] == d["slug"]][:4]
    docs = "".join(
        f"""<a href="../../doctors/{x['slug']}/index.html" class="block rounded-xl bg-white p-4 ring-1 ring-slate-200">
        <p class="font-semibold">{esc(x['name'])}</p><p class="text-sm text-teal-800">{esc(x['role'])}</p></a>"""
        for x in related
    ) or "<p class='text-sm text-slate-600'>See the full faculty on our doctors page.</p>"
    body = f"""
  <section class="bg-teal-900 text-white py-14"><div class="mx-auto max-w-7xl px-4">
    <p class="text-teal-200 text-sm"><a href="../index.html">Departments</a> / {esc(d['name'])}</p>
    <h1 class="text-4xl font-extrabold mt-2">{esc(d['name'])}</h1>
    <p class="mt-3 max-w-3xl text-teal-50">{esc(d['lead'])}</p>
    <a href="../../appointment/index.html" class="mt-6 inline-flex rounded-full bg-white text-teal-900 px-5 py-2 font-semibold">Request appointment</a>
  </div></section>
  <section class="mx-auto max-w-7xl px-4 py-12 grid lg:grid-cols-3 gap-10">
    <div class="lg:col-span-2 space-y-4 leading-relaxed text-slate-700">{paras}</div>
    <aside class="space-y-6">
      <div class="rounded-2xl bg-white p-5 ring-1 ring-slate-200">
        <h2 class="font-semibold mb-3">Treatments</h2>
        <ul class="space-y-2">{treatments}</ul>
      </div>
      <div class="rounded-2xl bg-white p-5 ring-1 ring-slate-200">
        <h2 class="font-semibold mb-3">Related doctors</h2>
        <div class="space-y-3">{docs}</div>
      </div>
    </aside>
  </section>
"""
    write(f"departments/{d['slug']}/index.html", shell(f"{d['name']} | CHD City Hospital", d["short"], 2, "departments", body))


def doctors_index():
    cards = "\n".join(
        f"""<a href="{d['slug']}/index.html" class="rounded-2xl bg-white p-6 ring-1 ring-slate-200 hover:ring-teal-300">
          <h2 class="font-semibold">{esc(d['name'])}</h2>
          <p class="text-sm text-teal-800 mt-1">{esc(d['role'])}</p>
          <p class="text-sm text-slate-600 mt-2">{esc(d['edu'])}</p>
        </a>"""
        for d in DOCTORS
    )
    body = f"""
  <section class="bg-slate-900 text-white py-14"><div class="mx-auto max-w-7xl px-4">
    <h1 class="text-4xl font-extrabold">Our doctors</h1>
    <p class="mt-3 max-w-3xl text-slate-300">You are the top priority. Physicians, specialists, and support staff are experienced, highly trained, and committed to you.</p>
  </div></section>
  <section class="mx-auto max-w-7xl px-4 py-12 grid sm:grid-cols-2 lg:grid-cols-3 gap-4">{cards}</section>
"""
    write("doctors/index.html", shell("Our Doctors | CHD City Hospital Chandigarh", "Meet orthopaedic, surgical, maternity, and medical specialists at CHD City Hospital.", 1, "doctors", body))


def doctor_page(d: dict):
    body = f"""
  <section class="mx-auto max-w-4xl px-4 py-14">
    <p class="text-sm text-teal-800"><a href="../index.html">Doctors</a> / {esc(d['name'])}</p>
    <h1 class="text-4xl font-extrabold mt-2">{esc(d['name'])}</h1>
    <p class="text-lg text-teal-800 mt-2">{esc(d['role'])}</p>
    <p class="mt-2 text-slate-600">{esc(d['edu'])}</p>
    <div class="prose mt-8 text-slate-700 leading-relaxed"><p>{esc(d['bio'])}</p></div>
    <div class="mt-8 flex flex-wrap gap-3">
      <a href="../../appointment/index.html" class="rounded-full bg-teal-700 text-white px-5 py-2.5 font-semibold">Book a visit</a>
      <a href="../../departments/{d['dept']}/index.html" class="rounded-full border border-slate-300 px-5 py-2.5 font-semibold">View department</a>
    </div>
  </section>
"""
    write(f"doctors/{d['slug']}/index.html", shell(f"{d['name']} | {d['role']}", d["bio"][:150], 2, "doctors", body))


def blog_index():
    cards = "\n".join(
        f"""<a href="{b['slug']}/index.html" class="rounded-2xl bg-white p-6 ring-1 ring-slate-200 hover:ring-teal-300">
          <p class="text-xs text-slate-500">{esc(b['date'])}</p>
          <h2 class="font-semibold mt-2">{esc(b['title'])}</h2>
          <p class="text-sm text-slate-600 mt-2">{esc(b['summary'])}</p>
        </a>"""
        for b in BLOGS
    )
    body = f"""
  <section class="bg-teal-900 text-white py-14"><div class="mx-auto max-w-7xl px-4">
    <h1 class="text-4xl font-extrabold">Health guide</h1>
    <p class="mt-3 text-teal-100">Practical articles from the same specialties you will find in the hospital.</p>
  </div></section>
  <section class="mx-auto max-w-7xl px-4 py-12 grid md:grid-cols-2 gap-4">{cards}</section>
"""
    write("blog/index.html", shell("Health Guide | CHD City Hospital Blog", "Articles on orthopaedics, maternity, heart, skin, and more.", 1, "blog", body))


def blog_page(b: dict):
    body = f"""
  <article class="mx-auto max-w-3xl px-4 py-14">
    <p class="text-sm text-teal-800"><a href="../index.html">Health guide</a> · {esc(b['date'])}</p>
    <h1 class="text-4xl font-extrabold mt-2">{esc(b['title'])}</h1>
    <p class="mt-6 text-lg text-slate-700 leading-relaxed">{esc(b['summary'])}</p>
    <p class="mt-4 text-slate-700 leading-relaxed">This guide is written from the public education themes on the original CHD City Hospital website. It is not a substitute for a consultation. If symptoms are severe or sudden, call the hospital or visit emergency care.</p>
    <a href="../../departments/{b['dept']}/index.html" class="mt-8 inline-flex rounded-full bg-teal-700 text-white px-5 py-2.5 font-semibold">Related department</a>
  </article>
"""
    write(f"blog/{b['slug']}/index.html", shell(b["title"], b["summary"], 2, "blog", body))


def contact():
    body = f"""
  <section class="bg-slate-900 text-white py-14"><div class="mx-auto max-w-7xl px-4">
    <h1 class="text-4xl font-extrabold">Contact us</h1>
    <p class="mt-3 text-slate-300">The hospital team will help you reach the right department. Parking is available; drop-off is preferred when you can manage it.</p>
  </div></section>
  <section class="mx-auto max-w-7xl px-4 py-12 grid lg:grid-cols-2 gap-10">
    <div class="space-y-5">
      <div class="rounded-2xl bg-white p-6 ring-1 ring-slate-200">
        <h2 class="font-semibold">Address</h2>
        <p class="mt-2">{esc(ADDRESS)}</p>
        <p class="mt-2"><a class="text-teal-800 font-semibold" href="{PHONE_HREF}">{PHONE}</a><br>{PHONE2}<br><a href="mailto:{EMAIL}">{EMAIL}</a></p>
        <p class="mt-2 text-sm text-slate-600">Opening hours: 24×7</p>
      </div>
      <div class="rounded-2xl bg-white p-6 ring-1 ring-slate-200">
        <h2 class="font-semibold">Patient concerns</h2>
        <p class="mt-2 text-sm text-slate-600">If you have a concern about care, speak with your attending doctor or the hospital desk. We record the issue, review it internally, and get back to you.</p>
      </div>
    </div>
    <form class="rounded-2xl bg-white p-6 ring-1 ring-slate-200 space-y-4" action="mailto:{EMAIL}" method="post" enctype="text/plain">
      <h2 class="font-semibold text-lg">Send a message</h2>
      <label class="block text-sm">Name<input required name="name" class="mt-1 w-full rounded-lg border border-slate-300 px-3 py-2"></label>
      <label class="block text-sm">Phone<input required name="phone" class="mt-1 w-full rounded-lg border border-slate-300 px-3 py-2"></label>
      <label class="block text-sm">Message<textarea name="message" rows="4" class="mt-1 w-full rounded-lg border border-slate-300 px-3 py-2"></textarea></label>
      <button class="rounded-full bg-teal-700 text-white px-5 py-2.5 font-semibold">Send</button>
    </form>
  </section>
"""
    write("contact/index.html", shell("Contact CHD City Hospital", f"Visit {ADDRESS} or call {PHONE}.", 1, "contact", body))


def appointment():
    opts = "".join(f'<option>{esc(d["name"])}</option>' for d in DEPARTMENTS)
    body = f"""
  <section class="mx-auto max-w-3xl px-4 py-14">
    <h1 class="text-4xl font-extrabold">Request an appointment</h1>
    <p class="mt-3 text-slate-600">Call {APPT} for a same-day request, or share your details and we will call back.</p>
    <form class="mt-8 rounded-2xl bg-white p-6 ring-1 ring-slate-200 space-y-4" action="mailto:{EMAIL}" method="post" enctype="text/plain">
      <label class="block text-sm">Full name<input required name="name" class="mt-1 w-full rounded-lg border border-slate-300 px-3 py-2"></label>
      <label class="block text-sm">Phone<input required name="phone" class="mt-1 w-full rounded-lg border border-slate-300 px-3 py-2"></label>
      <label class="block text-sm">Department<select name="department" class="mt-1 w-full rounded-lg border border-slate-300 px-3 py-2">{opts}</select></label>
      <label class="block text-sm">Preferred time<input name="time" class="mt-1 w-full rounded-lg border border-slate-300 px-3 py-2" placeholder="Today evening / tomorrow morning"></label>
      <label class="block text-sm">Notes<textarea name="notes" rows="4" class="mt-1 w-full rounded-lg border border-slate-300 px-3 py-2"></textarea></label>
      <button class="rounded-full bg-teal-700 text-white px-5 py-2.5 font-semibold">Request callback</button>
    </form>
  </section>
"""
    write("appointment/index.html", shell("Request an Appointment | CHD City Hospital", "Book a callback or same-day appointment.", 1, "contact", body))


def simple(path, title, desc, active, heading, paragraphs, depth=1):
    paras = "".join(f"<p class='text-slate-700 leading-relaxed'>{esc(p)}</p>" for p in paragraphs)
    body = f"""
  <section class="bg-slate-900 text-white py-14"><div class="mx-auto max-w-7xl px-4"><h1 class="text-4xl font-extrabold">{esc(heading)}</h1></div></section>
  <section class="mx-auto max-w-3xl px-4 py-12 space-y-4">{paras}</section>
"""
    write(path, shell(title, desc, depth, active, body))


def faq():
    items = [
        ("Is the hospital open at night?", "Yes. CHD City Hospital runs 24×7 emergency and inpatient services in Sector 8C, Chandigarh."),
        ("Do you offer same-day appointments?", "Call 7508008115 or request a callback. Many OPD slots can be arranged the same day depending on the specialty."),
        ("Is gallbladder stone surgery a package?", "Laparoscopic gallbladder stone removal is listed from Rs. 32,000 and includes pre-operative investigations. Final fitness is confirmed after clinical review."),
        ("Is CHD City Hospital NABH accredited?", "Yes. The hospital is NABH accredited and follows infection-control and patient-safety protocols."),
        ("Where can I park?", "There is a parking lot for patients and visitors. If your health allows, drop-off or nearby parking is appreciated to keep the lot free for those who need it."),
        ("How do I raise a concern about care?", "Speak with your attending doctor or the hospital desk. The team records the concern, reviews it, and contacts you with the outcome."),
        ("What is primary care here?", "Internal medicine and general practice are the first stop for prevention, chronic disease, and coordination with specialists."),
        ("Do you treat children?", "Yes. Paediatrics includes newborn care, vaccination, PICU pathways, and paediatric surgery support."),
    ]
    qa = "".join(
        f"<details class='rounded-2xl bg-white p-5 ring-1 ring-slate-200'><summary class='font-semibold cursor-pointer'>{esc(q)}</summary><p class='mt-3 text-slate-600'>{esc(a)}</p></details>"
        for q, a in items
    )
    body = f"""
  <section class="bg-teal-900 text-white py-14"><div class="mx-auto max-w-7xl px-4">
    <h1 class="text-4xl font-extrabold">Frequently asked questions</h1>
    <p class="mt-3 text-teal-100">CHD City Hospital is always ready to answer queries.</p>
  </div></section>
  <section class="mx-auto max-w-3xl px-4 py-12 space-y-3">{qa}</section>
"""
    write("faq/index.html", shell("FAQ | CHD City Hospital", "Answers about appointments, packages, NABH accreditation, and visiting.", 1, "about", body))


def main():
    # remove leftover hello-world files
    for leftover in [ROOT / "index.html", ROOT / "logo.svg"]:
        if leftover.exists():
            leftover.unlink()

    home()
    about()
    departments_index()
    for d in DEPARTMENTS:
        department_page(d)
    doctors_index()
    for d in DOCTORS:
        doctor_page(d)
    blog_index()
    for b in BLOGS:
        blog_page(b)
    contact()
    appointment()
    faq()
    simple(
        "quality/index.html",
        "Quality & Safety | CHD City Hospital",
        "How CHD City Hospital approaches patient safety and NABH standards.",
        "about",
        "Quality and safety",
        [
            "CHD City Hospital aims at supreme patient care. Performance is measured against internal standards and reviewed so care keeps improving.",
            "Priorities include superior outcomes, outstanding patient safety, timely care, and fair access. NABH accreditation is part of that commitment.",
            "Infection control, protocol-based treatment, and transparent communication with families are built into daily work — from OPD to ICU.",
            "If you want to know more about safety practices during your stay, ask your nurse or coordinator. We believe sharing results with patients is an obligation.",
        ],
    )
    simple(
        "careers/index.html",
        "Careers | CHD City Hospital",
        "Join the clinical and support teams at CHD City Hospital, Chandigarh.",
        "about",
        "Careers",
        [
            "You are the future of healthcare. CHD City Hospital looks for people who want to deliver exceptional care in a specialist-run hospital.",
            "We need clinicians, nurses, coordinators, and support staff who can enhance lives with both skill and kindness. Roles range from OT and ICU to front desk and IPD coordination.",
            "To apply, email your CV to info@chdcityhospital.com with the role in the subject line, or visit the hospital desk at Sector 8C.",
        ],
    )
    simple(
        "testimonials/index.html",
        "Patient Stories | CHD City Hospital",
        "Reviews from patients treated at CHD City Hospital, Chandigarh.",
        "about",
        "Patient stories",
        [f"{r['name']}: {r['text']}" for r in REVIEWS]
        + ["Overall Google rating: 4.9 out of 5 from 250+ reviews."],
    )
    simple(
        "privacy/index.html",
        "Privacy Policy | CHD City Hospital",
        "How CHD City Hospital collects and uses website information.",
        "about",
        "Privacy policy",
        [
            "At CHD City Hospital we safeguard the privacy of website visitors. Using the site means you consent to the practices below.",
            "Personal information such as name, phone, and email is collected only when you volunteer it through forms. It is used to respond to enquiries and improve the site.",
            "Non-personal data such as IP address and browser type may be collected automatically. Cookies can be disabled in your browser; some features may then be limited.",
            "We may share information with service providers bound by confidentiality, or if required by law. No internet transmission is 100% secure.",
            "The site is not intended for children under 16. For questions contact CHD City Hospital, SCO 10-11, Madhya Marg, Sector 8C, Chandigarh 160009, phone +91 7508008117.",
        ],
    )
    write(
        "404.html",
        shell(
            "Page not found | CHD City Hospital",
            "The page you requested is not available.",
            0,
            "home",
            """<section class="mx-auto max-w-xl px-4 py-24 text-center">
            <h1 class="text-4xl font-extrabold">Page not found</h1>
            <p class="mt-3 text-slate-600">Try the homepage or departments list.</p>
            <a href="index.html" class="mt-6 inline-flex rounded-full bg-teal-700 text-white px-5 py-2.5 font-semibold">Go home</a>
            </section>""",
        ),
    )
    print("Wrote site under", ROOT)


if __name__ == "__main__":
    main()
