import hashlib

agent_data = f"{organization_id}:{agent_type}:{timestamp}"
agent_id = hashlib.sha256(agent_data.encode()).hexdigest()
