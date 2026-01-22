
import streamlit as st
import base64
from openai import OpenAI
from docx import Document
import os
from io import BytesIO
import tempfile

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Image to Word Converter",
    page_icon="📝",
    layout="wide"
)

# -----------------------------
# STYLING
# -----------------------------
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
        background-color: #4CAF50;
        color: white;
        padding: 0.5rem;
        font-size: 16px;
    }
    .success-box {
        padding: 1rem;
        border-radius: 0.5rem;
        background-color: #d4edda;
        border: 1px solid #c3e6cb;
        color: #155724;
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------
# HELPERS
# -----------------------------
@st.cache_data
def encode_image_from_bytes(image_bytes):
    """Encode image bytes to base64."""
    return base64.b64encode(image_bytes).decode("utf-8")

def extract_and_structure(image_files, api_key, progress_bar):
    """Send images + prompt to Groq Vision model."""
    # Configure OpenAI client with Groq
    client = OpenAI(
        api_key=api_key,
        base_url="https://api.groq.com/openai/v1"
    )
    
    # Build vision input list
    vision_input = []
    for idx, img_file in enumerate(image_files):
        progress_bar.progress((idx + 1) / (len(image_files) + 1), 
                              f"Processing image {idx + 1}/{len(image_files)}...")
        b64 = encode_image_from_bytes(img_file.getvalue())
        vision_input.append({
            "type": "input_image",
            "detail": "auto",
            "image_url": f"data:image/jpeg;base64,{b64}"
        })
    
    # Build the model prompt
    full_input = [
        {
            "role": "user",
            "content": [
                {
                    "type": "input_text",
                    "text": (
                        "Do not add anything from your own or dont give any explaination just copy text equation graphs diagram (if available) in the image "     
                        "Extract everything from these images exactly as it appears. "
                        "Do NOT change anything, do NOT correct or rewrite, do NOT "
                        "summarize or interpret. Include all text (handwritten or printed), "
                        "equations, formulas, graphs, arrows, annotations, bullets, numbering, "
                        "diagrams described literally in words. If something is not text "
                        "but a shape or line or arrow, describe it exactly as seen. "
                        "Do NOT add anything that is not visually present in the images."
                    )
                },
            ] + vision_input
        }
    ]
    
    progress_bar.progress(0.9, "Sending to AI model...")
    
    response = client.responses.create(
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        input=full_input,
        max_output_tokens=8192,
        temperature=0.1
    )
    
    progress_bar.progress(1.0, "Complete!")
    return response.output_text

def create_word_document(text):
    """Create a Word document from text and return as bytes."""
    doc = Document()
    for line in text.split("\n"):
        doc.add_paragraph(line)
    
    # Save to BytesIO object
    doc_io = BytesIO()
    doc.save(doc_io)
    doc_io.seek(0)
    return doc_io

# -----------------------------
# MAIN APP
# -----------------------------
def main():
    # Header
    st.title("📝 Image to Word Document Converter")
    st.markdown("Convert images containing text, equations, and diagrams into a Word document using AI.")
    
    # Sidebar for API key
    with st.sidebar:
        st.header("⚙️ Configuration")
        api_key = st.text_input(
            "Groq API Key",
            type="password",
            value=os.environ.get("GROQ_API_KEY", ""),
            help="Enter your Groq API key. Get one at https://console.groq.com"
        )
        
        st.markdown("---")
        st.markdown("### About")
        st.info(
            "This tool uses Groq's Vision AI to extract text, equations, "
            "and diagrams from images and convert them into a Word document."
        )
        
        st.markdown("### Supported Formats")
        st.markdown("- JPG/JPEG\n- PNG\n- WebP")
    
    # Main content
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.header("Upload Images")
        uploaded_files = st.file_uploader(
            "Choose image files",
            type=["jpg", "jpeg", "png", "webp"],
            accept_multiple_files=True,
            help="Upload one or more images containing text, equations, or diagrams"
        )
        
        if uploaded_files:
            st.success(f"✅ {len(uploaded_files)} image(s) uploaded")
            
            # Display uploaded images
            with st.expander("Preview Uploaded Images", expanded=False):
                cols = st.columns(3)
                for idx, img_file in enumerate(uploaded_files):
                    with cols[idx % 3]:
                        st.image(img_file, caption=img_file.name, use_container_width=True)
    
    with col2:
        st.header("Actions")
        
        if not api_key:
            st.warning("⚠️ Please enter your Groq API key in the sidebar")
        
        process_button = st.button(
            "🚀 Convert to Word",
            disabled=(not uploaded_files or not api_key),
            use_container_width=True
        )
    
    # Processing
    if process_button and uploaded_files and api_key:
        try:
            # Progress tracking
            progress_bar = st.progress(0, "Starting conversion...")
            
            # Extract text from images
            with st.spinner("Processing images with AI..."):
                extracted_text = extract_and_structure(uploaded_files, api_key, progress_bar)
            
            # Clear progress bar
            progress_bar.empty()
            
            # Display results
            st.success("✅ Extraction complete!")
            
            # Show extracted text
            with st.expander("📄 Preview Extracted Content", expanded=True):
                st.text_area("Extracted Text", extracted_text, height=300)
            
            # Create Word document
            with st.spinner("Creating Word document..."):
                doc_bytes = create_word_document(extracted_text)
            
            # Download button
            st.download_button(
                label="⬇️ Download Word Document",
                data=doc_bytes,
                file_name="extracted_notes.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                use_container_width=True
            )
            
            st.balloons()
            
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
            st.exception(e)
    
    # Footer
    st.markdown("---")
    st.markdown(
        "<div style='text-align: center; color: #666;'>"
        "Made with ❤️ using Streamlit and Groq AI"
        "</div>",
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()