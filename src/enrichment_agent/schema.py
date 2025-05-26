"""Schema definition for the enrichment agent.

This module contains the schema used for data extraction and validation.
"""

schema = {
    "type": "object",
    "properties": {
        "suppliers": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "name": {"type": "string", "description": "Supplier name"},
                    "description": {
                        "type": "string",
                        "description": "Brief description of the supplier",
                    },
                    "standards_compliance": {
                        "type": "string",
                        "description": "Brief description of the supplier's standards compliance",
                    },
                    "certifications": {
                        "type": "string",
                            "description": "Brief description of the supplier's certifications",
                        },
                        "contact_details": {
                        "type": "object",
                        "properties": {
                            "email": {"type": "string", "description": "Email address of the supplier"},
                            "phone": {"type": "string", "description": "Phone number of the supplier"},
                            "website": {"type": "string", "description": "Website of the supplier (original website or indiamart, tradeindia pages)"},
                        },
                        "description": "Contact details of the supplier",
                    },
                },
                "required": ["name", "description", "standards_compliance", "certifications", "contact_details"],
            },
            "description": "List of suppliers",
        }
    },
    "required": ["suppliers"],
} 