{
    "name": "MTS Connector",
    "category": "MTS",
    "version": "15.0.1.1.0",
    "sequence": 1,
    "author": "OpenG2P",
    "website": "https://github.com/OpenG2P/openg2p-mts",
    "license": "Other OSI approved licence",
    "development_status": "Alpha",
    "depends": ["base", "queue_job"],
    "external_dependencies": {"python": ["pyjq"]},
    "data": [
        "security/ir.model.access.csv",
        "security/security.xml",
        "views/menuitems.xml",
        "views/mts_connector.xml",
    ],
    "assets": {},
    "demo": [],
    "images": [],
    "application": True,
    "installable": True,
    "auto_install": False,
}
