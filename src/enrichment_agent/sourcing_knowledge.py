# src/enrichment_agent/sourcing_knowledge.py

"""
Sourcing Knowledge Base for Procurement Agent
---------------------------------------------
This module contains structured knowledge to guide the procurement agent in making
strategic sourcing decisions. It is designed to be used by an LLM acting as a
procurement expert.

Contents:
1.  GENERAL_SOURCING_PRINCIPLES
2.  PRODUCT_CATEGORY_PROFILES
3.  REGIONAL_SOURCING_PROFILES
4.  SUPPLIER_EVALUATION_CRITERIA
5.  RISK_MANAGEMENT_CONSIDERATIONS
6.  COMPLIANCE_AND_REGULATORY_GUIDANCE
7.  NEGOTIATION_TACTICS_OVERVIEW
8.  LOGISTICS_AND_SUPPLY_CHAIN_NOTES
"""

GENERAL_SOURCING_PRINCIPLES = {
    "total_cost_of_ownership_tco": {
        "description": "Evaluate suppliers based on TCO, not just purchase price. Includes acquisition, ownership, and post-ownership costs.",
        "components": ["Purchase Price", "Transportation", "Import Duties & Taxes", "Inventory Holding Costs", "Quality Control & Inspection", "Maintenance & Repair", "Disposal Costs", "Supplier Management Costs"]
    },
    "strategic_sourcing_process": {
        "description": "A systematic approach to optimize an organization's supply base and improve overall value.",
        "steps": [
            "1. Spend Analysis: Understand current spend patterns.",
            "2. Supply Market Assessment: Research potential suppliers and market dynamics.",
            "3. Supplier Survey & RFP/RFQ: Gather information and quotes.",
            "4. Evaluation & Selection: Score suppliers based on predefined criteria.",
            "5. Negotiation & Contracting: Secure favorable terms.",
            "6. Implementation & Supplier Integration: Onboard new suppliers.",
            "7. Performance Monitoring & Continuous Improvement: Track supplier performance."
        ]
    },
    "supplier_relationship_management_srm": {
        "description": "A systematic approach to managing an enterprise's interactions with the organizations that supply the goods and services it uses.",
        "levels": ["Transactional", "Collaborative", "Strategic Alliance"],
        "benefits": ["Improved communication", "Better supplier performance", "Innovation", "Risk reduction"]
    },
    "risk_diversification": {
        "description": "Avoid over-reliance on a single supplier or geographic region to mitigate supply chain disruptions.",
        "strategies": ["Dual/Multi-sourcing", "Geographic diversification", "Developing alternative materials/components"]
    },
    "ethical_and_sustainable_sourcing": {
        "description": "Considering environmental, social, and governance (ESG) factors in procurement decisions.",
        "focus_areas": ["Fair labor practices", "Environmental impact", "Transparency", "Community impact", "Conflict minerals"]
    },
    "make_vs_buy_analysis": {
        "description": "Deciding whether to produce a product/service in-house or procure it from an external supplier.",
        "factors": ["Core competency", "Cost", "Capacity", "Control", "Quality", "IP protection"]
    }
}

PRODUCT_CATEGORY_PROFILES = {
    "raw_materials": {
        "description": "Basic materials used in production processes (e.g., metals, minerals, agricultural products, chemicals).",
        "sourcing_characteristics": ["Commodity markets common", "Price volatility", "Quality specifications critical", "Global sourcing often required", "Long-term contracts or spot buys"],
        "key_considerations": ["Purity/Grade", "Supply reliability", "Hedging against price fluctuations", "Storage and handling requirements"],
        "common_regions": {
            "Metals": ["Australia (Iron Ore, Lithium)", "Chile (Copper)", "China (Rare Earths)"],
            "Agricultural": ["USA (Corn, Soy)", "Brazil (Coffee, Sugar)", "India (Cotton, Spices)"],
            "Chemicals": ["Germany", "USA", "China", "India (Specialty Chemicals)"]
        }
    },
    "standard_components_and_parts": {
        "description": "Off-the-shelf parts used in assemblies (e.g., fasteners, bearings, resistors, capacitors, generic hardware).",
        "sourcing_characteristics": ["High volume, low mix", "Price sensitive", "Standardized specifications", "Distributor networks common"],
        "key_considerations": ["Availability & Lead Time", "Volume discounts", "Interchangeability", "Quality consistency"],
        "common_regions": ["China", "Taiwan", "Southeast Asia (for electronics)", "Local distributors for MRO"]
    },
    "custom_engineered_components": {
        "description": "Parts designed and manufactured to specific customer requirements (e.g., custom molds, specialized machinery parts, unique electronic modules).",
        "sourcing_characteristics": ["Low volume, high mix", "High switching costs", "Close supplier collaboration required", "IP protection critical"],
        "key_considerations": ["Supplier's technical capability", "Prototyping and NPI process", "Quality assurance", "Long-term partnership potential"],
        "common_regions": ["Varies by industry: Germany (Automotive, Machinery)", "USA (Aerospace, Medical)", "Japan (Precision Engineering)", "Taiwan/South Korea (Custom ICs)"]
    },
    "finished_goods_for_resale": {
        "description": "Products purchased for direct resale without further modification (e.g., consumer electronics, apparel, tools by a retailer/distributor).",
        "sourcing_characteristics": ["Branding and packaging critical", "Demand forecasting crucial", "Supply chain visibility important"],
        "key_considerations": ["Supplier reliability & capacity", "Product quality & compliance", "Margin analysis", "Inventory management"],
        "common_regions": ["China (Consumer Goods, Electronics)", "Bangladesh/Vietnam (Apparel)", "India (Textiles, Handicrafts)"]
    },
    "capital_equipment_machinery": {
        "description": "Large, expensive assets used in production or operations (e.g., manufacturing machinery, construction equipment, IT servers).",
        "sourcing_characteristics": ["High value, infrequent purchase", "Long lead times", "Complex specifications", "After-sales service and support critical"],
        "key_considerations": ["Lifecycle cost (TCO)", "Technical specifications & performance", "Installation & training", "Warranty & maintenance contracts", "Supplier's financial stability"],
        "common_regions": ["Germany (Machinery)", "Japan (Robotics, Machine Tools)", "USA (Heavy Equipment, IT Infrastructure)", "Italy (Specialized Machinery)"]
    },
    "indirect_goods_services_mro": {
        "description": "Goods and services not directly incorporated into a product but necessary for operations (e.g., office supplies, IT services, maintenance, repair, operations items, marketing services, consulting).",
        "sourcing_characteristics": ["Fragmented spend", "Many suppliers", "Often locally sourced", "Process efficiency is key"],
        "key_considerations": ["Spend consolidation opportunities", "Service Level Agreements (SLAs) for services", "Ease of ordering (e-procurement)", "Contract compliance"],
        "common_regions": ["Primarily local/national, but global for some services like IT outsourcing (India, Philippines, Eastern Europe)"]
    },
    "software_and_it_services": {
        "description": "Includes enterprise software (ERP, CRM), cloud services (IaaS, PaaS, SaaS), custom software development, IT consulting.",
        "sourcing_characteristics": ["Subscription models common for SaaS", "Vendor lock-in potential", "Data security and privacy are critical", "Integration with existing systems"],
        "key_considerations": ["Functionality & Scalability", "Total Cost of Ownership (TCO)", "Service Level Agreements (SLAs)", "Vendor reputation & support", "Data residency & compliance (e.g., GDPR)"],
        "common_regions": {
            "SaaS/Cloud": ["Global providers (USA-centric often)"],
            "IT Outsourcing/Development": ["India", "Philippines", "Eastern Europe", "Latin America"]
        }
    },
    "professional_services": {
        "description": "Services like legal, accounting, consulting, marketing, HR.",
        "sourcing_characteristics": ["Expertise and reputation are key", "Difficult to quantify value", "Relationship-based"],
        "key_considerations": ["Provider's track record and references", "Scope of work definition", "Fee structure (fixed, hourly, retainer)", "Confidentiality"],
        "common_regions": ["Often local/national, but global firms exist for specialized needs."]
    }
}

REGIONAL_SOURCING_PROFILES = {
    "china": {
        "strengths": ["Mass manufacturing capabilities", "Extensive supplier ecosystem", "Cost competitiveness for many standard goods", "Developed logistics infrastructure", "Special Economic Zones (SEZs)"],
        "weaknesses": ["Rising labor costs", "IP protection concerns", "Geopolitical risks & trade tensions", "Quality consistency can vary", "Language and cultural barriers"],
        "key_industries": ["Electronics assembly", "Textiles & Apparel", "Toys", "Furniture", "Machinery parts", "Consumer goods"],
        "sourcing_tips": ["Verify supplier credentials thoroughly (e.g., factory audits)", "Clear and detailed specifications are crucial", "Use formal contracts", "Consider using sourcing agents or third-party QA", "Build relationships (Guanxi)"],
        "popular_platforms": ["Alibaba", "Made-in-China.com", "Global Sources", "DHGate"]
    },
    "india": {
        "strengths": ["Large skilled and semi-skilled labor pool", "Growing manufacturing sector ('Make in India' initiative)", "Strong IT and software services", "Pharmaceuticals and chemicals expertise", "English widely spoken in business"],
        "weaknesses": ["Infrastructure challenges in some areas", "Bureaucracy and regulatory hurdles can be complex", "Logistics can be less efficient than China", "Variable quality standards if not managed"],
        "key_industries": ["IT services & BPO", "Pharmaceuticals (generics)", "Textiles & Apparel", "Automotive components", "Engineering goods", "Chemicals", "Handicrafts"],
        "sourcing_tips": ["Due diligence on supplier's financial health and capacity", "Understand local regulations and tax structures (GST)", "Focus on quality control processes", "Leverage local expertise for navigating business culture"],
        "popular_platforms": ["IndiaMART", "TradeIndia", "ExportersIndia"]
    },
    "vietnam": {
        "strengths": ["Lower labor costs than China (though rising)", "Government incentives for FDI", "Young workforce", "Increasingly part of global supply chains (China+1 strategy)"],
        "weaknesses": ["Infrastructure still developing", "Smaller supplier base than China", "Supply chain bottlenecks can occur", "Skill levels may vary"],
        "key_industries": ["Apparel & Footwear", "Electronics assembly (growing)", "Furniture", "Agricultural products"],
        "sourcing_tips": ["Popular for 'China Plus One' diversification", "Verify factory compliance with labor and environmental standards", "Understand lead times carefully"]
    },
    "mexico": {
        "strengths": ["Proximity to US market (USMCA benefits)", "Established manufacturing base (Maquiladoras)", "Skilled labor in automotive and electronics", "Lower transportation costs to North America"],
        "weaknesses": ["Security concerns in some regions", "Labor laws and unions", "Infrastructure can be inconsistent"],
        "key_industries": ["Automotive parts & assembly", "Electronics", "Medical devices", "Aerospace components"],
        "sourcing_tips": ["Leverage USMCA for tariff benefits if applicable", "Strong for nearshoring to supply North American markets", "Assess security risks for logistics"]
    },
    "eastern_europe": {
        "countries": ["Poland", "Czech Republic", "Hungary", "Romania"],
        "strengths": ["Skilled labor at competitive rates (vs Western Europe)", "Proximity to Western European markets", "EU membership (for many) ensures standards", "Good infrastructure"],
        "weaknesses": ["Rising labor costs in some areas", "Geopolitical situation (e.g., Ukraine conflict impacts)", "Language barriers outside business hubs"],
        "key_industries": ["Automotive components", "Machinery", "Electronics assembly", "IT outsourcing & software development"],
        "sourcing_tips": ["Good for supplying European markets", "High quality standards often met", "Consider cultural nuances in business"]
    },
    "germany": {
        "strengths": ["High quality and precision engineering ('German Engineering')", "Strong in specialized machinery, automotive, chemicals", "Innovation leader", "Reliable suppliers"],
        "weaknesses": ["High labor costs", "Less flexible than some other regions", "Can be expensive"],
        "key_industries": ["Automotive", "Machinery & Industrial Equipment", "Chemicals", "Medical Technology", "Renewable Energy"],
        "sourcing_tips": ["Focus on value and TCO, not just price", "Suppliers expect detailed specifications and professional interaction", "Long-term relationships valued"]
    },
    "usa": {
        "strengths": ["Large domestic market", "Innovation and technology leader", "High quality standards", "Strong IP protection", "Diverse industrial base"],
        "weaknesses": ["High labor costs", "Regulatory complexity varies by state", "Can be expensive for standard goods"],
        "key_industries": ["Aerospace & Defense", "Pharmaceuticals & Biotech", "Software & IT", "Advanced Manufacturing", "Medical Devices", "Oil & Gas"],
        "sourcing_tips": ["'Made in USA' can be a selling point for some markets", "Understand state-specific regulations", "Strong for high-tech and IP-sensitive items"]
    },
    "taiwan_south_korea": {
        "strengths": ["Leaders in advanced electronics, semiconductors, display technology", "High quality and innovation", "Efficient manufacturing"],
        "weaknesses": ["Geopolitical risks (Taiwan)", "Concentrated in specific high-tech industries", "Can be higher cost for some components"],
        "key_industries": ["Semiconductors (TSMC, Samsung)", "Consumer Electronics (Samsung, LG)", "Display Panels", "Automotive Electronics"],
        "sourcing_tips": ["Critical for cutting-edge electronics", "Strong IP, but be clear on ownership", "Understand Chaebol (SK) business culture"]
    }
}

SUPPLIER_EVALUATION_CRITERIA = {
    "quality": {
        "description": "Ability to consistently meet specifications and standards.",
        "metrics": ["Defect rates (PPM)", "Compliance certifications (ISO 9001, etc.)", "Quality management systems in place", "Customer return rates", "Product/service reliability"]
    },
    "cost_competitiveness": {
        "description": "Pricing relative to market and value provided (TCO focus).",
        "metrics": ["Unit price", "Volume discounts", "Payment terms", "Landed cost", "Price stability/history"]
    },
    "delivery_reliability_lead_time": {
        "description": "Ability to deliver on time and in full (OTIF).",
        "metrics": ["On-time delivery rate", "Lead time accuracy and consistency", "Order fulfillment rate", "Shipping and logistics capabilities"]
    },
    "technical_capability_innovation": {
        "description": "Expertise, R&D capabilities, and ability to support new product development.",
        "metrics": ["Engineering resources", "R&D investment", "Patents", "Ability to customize", "Use of modern technology/processes"]
    },
    "financial_stability": {
        "description": "Supplier's financial health and ability to remain a long-term partner.",
        "metrics": ["Credit ratings", "Profitability", "Debt levels", "Cash flow", "Years in business", "Customer references"]
    },
    "service_and_support": {
        "description": "Responsiveness, communication, and after-sales support.",
        "metrics": ["Customer service responsiveness", "Technical support quality", "Warranty terms", "Problem resolution efficiency"]
    },
    "capacity_and_scalability": {
        "description": "Ability to meet current and future volume requirements.",
        "metrics": ["Production capacity", "Scalability plans", "Flexibility to handle demand fluctuations", "Sub-supplier management"]
    },
    "esg_compliance_ethical_practices": {
        "description": "Adherence to environmental, social, governance, and ethical standards.",
        "metrics": ["Sustainability reports", "Labor practice audits", "Environmental certifications (ISO 14001)", "Ethical sourcing policies", "Diversity and inclusion initiatives"]
    },
    "risk_management_business_continuity": {
        "description": "Supplier's ability to mitigate risks and ensure supply continuity.",
        "metrics": ["Business Continuity Plan (BCP)", "Disaster recovery capabilities", "Geographic risk exposure", "Supply chain visibility"]
    }
}

RISK_MANAGEMENT_CONSIDERATIONS = {
    "geopolitical_risks": ["Trade wars & Tariffs", "Political instability", "Sanctions", "Changes in trade agreements"],
    "economic_risks": ["Currency fluctuations", "Inflation/deflation", "Supplier bankruptcy", "Recession"],
    "operational_risks": ["Supplier capacity issues", "Quality failures", "Logistics disruptions", "Labor strikes", "Natural disasters impacting supplier"],
    "compliance_regulatory_risks": ["Changes in laws", "Failure to meet standards (environmental, safety, labor)", "IP infringement"],
    "cybersecurity_risks": ["Data breaches at supplier", "Disruption of supplier's IT systems affecting supply"],
    "mitigation_strategies": ["Diversification of supply base", "Dual/multi-sourcing", "Building safety stock", "Hedging (currency, commodity)", "Strong contracts with clear SLAs and penalty clauses", "Supplier audits and monitoring", "Investing in supply chain visibility tools"]
}

COMPLIANCE_AND_REGULATORY_GUIDANCE = {
    "general_trade_compliance": ["Import/Export documentation (Commercial Invoice, Packing List, Bill of Lading, Certificate of Origin)", "Customs valuation", "Incoterms usage", "Tariff codes (HS codes)"],
    "product_specific_compliance": {
        "electronics": ["RoHS (Restriction of Hazardous Substances)", "WEEE (Waste Electrical and Electronic Equipment)", "FCC (USA)", "CE (Europe)"],
        "medical_devices": ["FDA (USA - e.g., 510(k), PMA)", "CE Marking (Europe - MDR/IVDR)", "ISO 13485 (Quality Management)", "Local health authority approvals (e.g., CDSCO in India)"],
        "food_and_beverage": ["FDA (USA - FSMA)", "HACCP", "GFSI recognized standards (SQF, BRC)", "Local food safety laws"],
        "chemicals": ["REACH (Europe)", "TSCA (USA)", "GHS (Globally Harmonized System for classification and labeling)"],
        "toys_childrens_products": ["ASTM F963 (USA)", "EN 71 (Europe)", "CPSIA (USA)"]
    },
    "labor_and_ethics": ["ILO Conventions", "Local labor laws (minimum wage, working hours)", "Anti-bribery and corruption laws (FCPA, UK Bribery Act)", "Modern Slavery Acts"],
    "environmental_compliance": ["ISO 14001 (Environmental Management)", "Local environmental regulations (emissions, waste disposal)", "Sustainability reporting standards (GRI, SASB)"]
}

NEGOTIATION_TACTICS_OVERVIEW = {
    "preparation": ["Know your BATNA (Best Alternative To a Negotiated Agreement)", "Research supplier's position and market", "Define objectives and walk-away points"],
    "anchoring": ["Making the first offer to set the negotiation range."],
    "principled_negotiation": ["Focus on interests, not positions", "Invent options for mutual gain", "Insist on using objective criteria"],
    "bundling_unbundling": ["Combining multiple items for a better deal, or separating items to negotiate individually."],
    "good_cop_bad_cop": ["One negotiator is aggressive, the other more conciliatory (use with caution, can be transparent)."],
    "nibbling": ["Asking for small concessions after the main agreement seems settled."],
    "pressure_tactics": ["Deadlines, limited-time offers (use ethically)."],
    "building_rapport": ["Establishing a positive relationship can lead to more collaborative outcomes."]
}

LOGISTICS_AND_SUPPLY_CHAIN_NOTES = {
    "incoterms": {
        "importance": "Define responsibilities, costs, and risks between buyer and seller for international shipments.",
        "common_terms": ["EXW (Ex Works)", "FOB (Free on Board)", "CIF (Cost, Insurance and Freight)", "DDP (Delivered Duty Paid)"]
    },
    "transportation_modes": ["Sea Freight (cost-effective for bulk, slow)", "Air Freight (fast, expensive)", "Rail Freight (good for long distances over land)", "Road Freight (flexible, for domestic/regional)"],
    "freight_forwarders_customs_brokers": ["Role in managing international shipments, customs clearance, documentation."],
    "inventory_management": ["Just-in-Time (JIT)", "Economic Order Quantity (EOQ)", "Safety Stock", "Vendor-Managed Inventory (VMI)"],
    "warehousing_distribution": ["Considerations for storage, handling, and distribution network optimization."],
    "supply_chain_visibility": ["Importance of tracking goods and information flow throughout the supply chain."]
}

# Example of how to access knowledge:
# sourcing_knowledge.PRODUCT_CATEGORY_PROFILES["raw_materials"]["key_considerations"]
# sourcing_knowledge.REGIONAL_SOURCING_PROFILES["china"]["sourcing_tips"] 