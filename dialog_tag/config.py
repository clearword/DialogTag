import os

class_labels = {
        "MAPPING" : {'fo_o_fw_"_by_bc': '0', 'ft': '1', 'fc': '2', 'qw': '3', '^g': '4', 'bh': '5', 'qy': '6', 'qrr': '7',
        'fp': '8', 'qo': '9', 'bk': '10', 'h': '11', 'sv': '12', 'ba': '13', 'nn': '14', '^h': '15', '^2': '16', 'aap_am': '17', 
        'qw^d': '18', 'qy^d': '19', 'ng': '20', 'fa': '21', 'b': '22', 'ny': '23', 't3': '24', 'sd': '25', 'br': '26', 
        'oo_co_cc': '27', 'arp_nd': '28', 't1': '29', '^q': '30', 'aa': '31', 'na': '32', 'b^m': '33', 'bd': '34', 'ad': '35',
        'bf': '36', 'qh': '37'}
    }

model_params = {
        "num_labels": int(os.getenv("DIALOGTAG_NUM_LABELS", 38))
    }

model_location = {
        "MODEL" : os.getenv("DIALOGTAG_MODEL_CACHE", "/.dialog-tag/models"),
        "label_mapping" : os.getenv("DIALOGTAG_LABEL_MAP", "/label_map.txt")
    }

model_download_link = {
        "distilbert-base-uncased" : os.getenv("DIALOGTAG_DISTILBERT_BASE_UNCASED", "https://www.dropbox.com/sh/crq7khtdd99u4mo/AABdQb8W1lJ37Cm-CfOSISuBa?dl=1"),
        "bert-base-uncased" : os.getenv("DIALOGTAG_BERT_BASE_UNCASED", "https://www.dropbox.com/sh/ajlwp36obho2cbe/AADHTY4_PhSOAQzveCJIna4Va?dl=1")
}
