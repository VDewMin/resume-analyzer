def build_prompt(resume_text, job_description):
    return f"""You are a resume analysis tool. You must analyze ONLY the exact text provided below. 
Do NOT use any external knowledge, assumptions, or invented data.
Only use information explicitly present in the RESUME TEXT and JOB DESCRIPTION TEXT provided.

Return your response in exactly this JSON format with no extra text, no markdown, no preamble:
{{
  "match_score": <integer 0-100>,
  "matched_skills": [<skills explicitly mentioned in BOTH the resume and job description>],
  "missing_skills": [<skills required in job description but NOT found anywhere in resume>],
  "strengths": [<3 specific strengths based ONLY on what is written in the resume>],
  "improvements": [<3 specific improvements based ONLY on the gap between this resume and this job description>],
  "rewritten_summary": "<rewritten summary based ONLY on the candidate's actual background in the resume, tailored to this specific job>"
}}

RESUME TEXT:
{resume_text}

JOB DESCRIPTION TEXT:
{job_description}

Remember: Analyze ONLY the text above. Do not invent experience, skills, or qualifications not present in the resume.
"""