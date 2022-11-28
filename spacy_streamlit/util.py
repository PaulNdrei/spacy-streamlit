from enum import Enum
import streamlit as st
import spacy
import base64

from spacy_streamlit.logos_svg import plantl_svg, default_svg, aina_svg


class Demotype(Enum):
    PLANTL = 1
    AINA = 2


@st.cache(allow_output_mutation=True, suppress_st_warning=True)
def load_model(name: str) -> spacy.language.Language:
    """Load a spaCy model."""
    return spacy.load(name)


@st.cache(allow_output_mutation=True, suppress_st_warning=True)
def process_text(model_name: str, text: str) -> spacy.tokens.Doc:
    """Process a text and create a Doc object."""
    nlp = load_model(model_name)
    return nlp(text)


def get_svg(svg: str, style: str = "", wrap: bool = True):
    """Convert an SVG to a base64-encoded image."""
    b64 = base64.b64encode(svg.encode("utf-8")).decode("utf-8")
    html = f'<img src="data:image/svg+xml;base64,{b64}" style="{style}"/>'
    return get_html(html) if wrap else html


def get_html(html: str):
    """Convert HTML so it can be rendered."""
    WRAPPER = """<div style="overflow-x: auto; border: 1px solid #e6e9ef; border-radius: 0.25rem; padding: 1rem; margin-bottom: 2.5rem">{}</div>"""
    # Newlines seem to mess with the rendering
    html = html.replace("\n", " ")
    return WRAPPER.format(html)


def get_logo(demo_type):
    if demo_type is Demotype.PLANTL:
        return get_svg(plantl_svg, wrap=False, style="max-width: 100%; max-height: 6em; margin-bottom: 25px")
    elif demo_type is Demotype.AINA:
        return get_svg(aina_svg, wrap=False, style="max-width: 100%; max-height: 4em; margin-bottom: 25px")
    return get_svg(default_svg, wrap=False, style="max-width: 100%;  margin-bottom: 25px")
