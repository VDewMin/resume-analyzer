import streamlit as st
from parser import extract_text_from_pdf
from analyzer import analyze_resume

st.set_page_config(page_title="AI Resume Analyzer", page_icon="📄", layout="centered")
st.title("📄 AI Resume Analyzer")
st.markdown("Upload your resume and paste a job description to see how well you match.")
st.divider()

#Inputs
col1, col2 = st.columns(2)
with col1:
    st.markdown("**Upload your resume (PDF)**")
    uploaded_file = st.file_uploader("", type="pdf")
with col2:
    st.markdown("**Paste the job description**")
    job_description = st.text_area("", height=200, placeholder="Copy and paste the full job description here...")

analyze_btn = st.button("Analyze", use_container_width=True, type="primary")

#analysis

if analyze_btn:
    if not uploaded_file:
        st.warning("⚠️ Please upload your resume.")
    elif not job_description.strip():
        st.warning("⚠️ Please paste a job description")
    else:
        with st.spinner("Analyzing your resume..."):
            resume_text = extract_text_from_pdf(uploaded_file)
            result = analyze_resume(resume_text, job_description)

        if "error" in result:
            st.error(f"Something went wrong: {result['error']}")
        else:
            st.divider()

            #Match score
            score = int(result.get("match_score", 0))

            if score >= 75:
                score_color = "🟢"
            elif score >= 50:
                score_color = "🟡"
            else:
                score_color = "🔴"

            st.markdown(f"## {score_color} Match Score: {score} / 100")
            st.progress(score/100)
            st.divider()

            #matched skills

            col_match, col_miss = st.columns(2)

            with col_match:
                st.subheader("✅ Matched Skills")
                matched = result.get("matched_skills", [])
                if matched:
                    for skill in matched:
                        st.markdown(f"- {skill}")
                else:
                    st.write("No matched skills found.")

                #missing skills

            with col_miss:    

                st.subheader("❌ Missing Skills")
                missing = result.get("missing_skills", [])
                if missing:
                    for skill in missing:
                        st.markdown(f"- {skill}")
                else:
                    st.success("No missing skills — great match!")

            st.divider()

                #Strengths
            st.subheader("💪 Strengths")
            for strength in result.get("strengths", []):
                st.success(strength)

            st.divider()

                #Improvements
            st.subheader("🔧 Improvements")
            for improvement in result.get("improvements", []):
                st.warning(improvement)

            st.divider()

                #Rewritten Summary
            st.subheader("✍️ Rewritten Summary")
            st.info(result.get("rewritten_summary", ""))
