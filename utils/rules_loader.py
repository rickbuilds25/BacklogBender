import os

LABEL_RULES = {}


def load_label_rules(file_path="config/scoring_rules.txt"):
    """
    Loads score thresholds and labels from scoring_rules.txt
    Returns a dictionary like:
    {
        'thresholds': { 'Must-Have': 400, ... },
        'labels': { 'Must-Have': '🚀 Must-Have', ... }
    }
    """
    thresholds = {}
    labels = {}
    current_section = None

    if not os.path.exists(file_path):
        print(f"⚠️ Rules file not found at {file_path}. Skipping labeling.")
        return {'thresholds': {}, 'labels': {}}

    with open(file_path, "r") as f:
        for line in f:
            line = line.strip()
            if line.startswith("[") and line.endswith("]"):
                current_section = line[1:-1].strip()
                continue

            if "=" in line and current_section:
                key, val = line.split("=", 1)
                key = key.strip()
                val = val.strip()

                if current_section == "THRESHOLDS":
                    try:
                        thresholds[key] = float(val)
                    except ValueError:
                        print(f"⚠️ Invalid threshold value for '{key}': {val}")

                elif current_section == "LABELS":
                    labels[key] = val

    return {'thresholds': thresholds, 'labels': labels}
