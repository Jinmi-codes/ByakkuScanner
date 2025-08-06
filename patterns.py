import re


#Additional patterns can be added here by whoever clones the repo.
#Follow the format as seen below
regex_patterns = {
    "AWS Access Key": r"AKIA[0-9A-Z]{16}",
    "AWS Secret Key": r"(?i)aws(.{0,20})?(secret|private)?(.{0,20})?['\"][0-9a-zA-Z/+]{40}['\"]",
    "Slack Token": r"xox[baprs]-[0-9a-zA-Z]{10,48}",
    "JWT": r"eyJ[A-Za-z0-9-_]+?\.[A-Za-z0-9-_]+?\.[A-Za-z0-9-_]+",
    "Generic API Key": r"(?i)(api_key|apikey|secret|token)['\"]?\s*[:=]\s*['\"][A-Za-z0-9-_]{16,45}['\"]?",
    "Google API key": r"AIza[0-9A-Za-z-_]{35}",
    "PostgreSQL Connection String": r"postgres:\/\/[^:\s]+:[^@\s]+@[^:\s]+:\d+\/\S+",
    "Heroku API key": r"(?i)heroku.*['\"][0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}['\"]",
    "Base64 String": r"[A-Za-z0-9+/]{40,}={0,2}",  # overly long base64 strings
}
