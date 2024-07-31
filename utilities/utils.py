"""TEMPORARY PLACEHOLDER DOCSTRING!"""

import uuid


def generate_id(id_for: str) -> str:
    """TEMPORARY PLACEHOLDER DOCSTRING!"""
    id = "m_" + str(uuid.uuid4()) if id_for == "marker" else "u_" + str(uuid.uuid4())
    return id
